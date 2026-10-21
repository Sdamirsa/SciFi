"""The three hooks, invoked as shell scripts with crafted stdin, plus the install and package
scripts end to end."""
import json
import os
import sys
import time
import unittest
import zipfile
from pathlib import Path

from _helpers import HOOKS, MINIMAL, REPO, SCRIPTS, init_ws, run, tmpdir, write_json

import _scifi


def hook(name, payload, **env):
    return run(["bash", str(HOOKS / name)], stdin=json.dumps(payload), env_extra=env)


class TestHooksJson(unittest.TestCase):
    def test_wiring(self):
        h = json.loads((HOOKS / "hooks.json").read_text())["hooks"]
        self.assertEqual(h["SessionStart"][0]["matcher"], "startup|resume|compact")
        self.assertEqual(h["PostToolUse"][0]["matcher"], "Write|Edit|MultiEdit")
        for event, groups in h.items():
            for g in groups:
                for c in g["hooks"]:
                    self.assertIn("${CLAUDE_PLUGIN_ROOT}/hooks/", c["command"])
                    self.assertTrue(10 <= c["timeout"] <= 15)
                    script = c["command"].strip('"').split("/hooks/")[1]
                    self.assertTrue(os.access(HOOKS / script, os.X_OK), script)

    def test_manifests(self):
        p = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text())
        self.assertEqual(p["name"], "scifi")
        m = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text())
        self.assertEqual(m["plugins"][0]["source"], "./")


class TestValidateHook(unittest.TestCase):
    def test_envelope_good_and_broken(self):
        with tmpdir() as d:
            p = write_json(Path(d) / "paper/Thinking-space/handshakes/d03.flow-checker.r1.json", MINIMAL["envelope"])
            payload = {"tool_name": "Write", "tool_input": {"file_path": str(p)}}
            r = hook("validate-json.sh", payload)
            self.assertEqual(r.returncode, 0, r.stderr)
            broken = dict(MINIMAL["envelope"])
            broken.pop("status")
            write_json(p, broken)
            r = hook("validate-json.sh", payload)
            self.assertEqual(r.returncode, 2)
            self.assertIn("missing required key 'status'", r.stderr)
            p.write_text("{not json")
            self.assertEqual(hook("validate-json.sh", payload).returncode, 2)

    def test_plugin_root_env_is_used(self):
        with tmpdir() as d:
            p = write_json(Path(d) / "Thinking-space/STATE.json", MINIMAL["state"])
            r = hook("validate-json.sh", {"tool_input": {"file_path": str(p)}}, CLAUDE_PLUGIN_ROOT=str(REPO))
            self.assertEqual(r.returncode, 0, r.stderr)
            r = hook("validate-json.sh", {"tool_input": {"file_path": str(p)}}, CLAUDE_PLUGIN_ROOT=d)
            self.assertEqual(r.returncode, 2)  # no validator there: fails closed

    def test_ignored_paths(self):
        with tmpdir() as d:
            stub = Path(d) / "Thinking-space/handshakes/x.stub.json"
            stub.parent.mkdir(parents=True)
            stub.write_text("{broken")
            other = Path(d) / "elsewhere/data.json"
            other.parent.mkdir()
            other.write_text("{broken")
            for f in (stub, other):
                self.assertEqual(hook("validate-json.sh", {"tool_input": {"file_path": str(f)}}).returncode, 0)
            self.assertEqual(hook("validate-json.sh", {}).returncode, 0)
            self.assertEqual(run(["bash", str(HOOKS / "validate-json.sh")], stdin="garbage").returncode, 0)

    def test_jsonl_logs(self):
        with tmpdir() as d:
            log = Path(d) / ".claude" / "Project-log.jsonl"
            log.parent.mkdir()
            log.write_text('{"type":"mistake"}\n\n{"type":"note"}\n')
            payload = {"tool_input": {"file_path": str(log)}}
            self.assertEqual(hook("validate-json.sh", payload).returncode, 0)
            log.write_text('{"type":"mistake"}\n{"type":\n')
            r = hook("validate-json.sh", payload)
            self.assertEqual(r.returncode, 2)
            self.assertIn("line 2", r.stderr)


class TestSessionStart(unittest.TestCase):
    def test_resume_block(self):
        with tmpdir() as d:
            ws = Path(d) / "paper"
            init_ws(ws, "--journal", "jamia")
            run([sys.executable, str(SCRIPTS / "state.py"), "--workspace", str(ws), "unit", "i01", "drafted"])
            for cwd_env in ({"CLAUDE_PROJECT_DIR": str(ws)}, {"CLAUDE_PROJECT_DIR": d}):
                with self.subTest(env=cwd_env):
                    r = hook("session-start.sh", {"session_id": "s1", "cwd": str(ws)}, **cwd_env)
                    self.assertEqual(r.returncode, 0)
                    self.assertIn("SCIFI RESUME", r.stdout)
                    self.assertIn("stage: init", r.stdout)
                    self.assertIn("journal: jamia", r.stdout)
                    self.assertIn("current unit: i01", r.stdout)
                    self.assertIn("drafted 1", r.stdout)
                    self.assertIn("open NEEDs: 0", r.stdout)
                    self.assertIn("workspace created", r.stdout)
                    self.assertNotIn("RITUAL", r.stdout)

    def test_ritual_nudge(self):
        with tmpdir() as d:
            ws = Path(d) / "paper"
            init_ws(ws)
            old = time.time() - 5 * 86400
            os.utime(ws / ".claude" / "STATUS.md", (old, old))
            r = hook("session-start.sh", {}, CLAUDE_PROJECT_DIR=str(ws))
            self.assertIn("RITUAL", r.stdout)
            self.assertIn("/project-memory", r.stdout)

    def test_no_workspace_and_broken_state(self):
        with tmpdir() as d:
            r = hook("session-start.sh", {}, CLAUDE_PROJECT_DIR=d)
            self.assertEqual((r.returncode, r.stdout.strip()), (0, ""))
            (Path(d) / "Thinking-space").mkdir()
            (Path(d) / "Thinking-space/STATE.json").write_text("{oops")
            r = hook("session-start.sh", {}, CLAUDE_PROJECT_DIR=d)
            self.assertEqual(r.returncode, 0)
            self.assertIn("could not be read", r.stdout)


class TestStopPointer(unittest.TestCase):
    def test_fills_empty_pointer_only(self):
        with tmpdir() as d:
            ws = Path(d) / "paper"
            init_ws(ws)
            r = hook("stop-pointer.sh", {"session_id": "s"}, CLAUDE_PROJECT_DIR=str(ws))
            self.assertEqual(r.returncode, 0)
            st = _scifi.load_state(ws)
            self.assertEqual(st["pointer"], st["next_action"])
            self.assertIn("pointer_at", st)
            self.assertEqual(_scifi.state_errors(st), [])
            run([sys.executable, str(SCRIPTS / "state.py"), "--workspace", str(ws), "pointer", "keep me"])
            hook("stop-pointer.sh", {}, CLAUDE_PROJECT_DIR=str(ws))
            self.assertEqual(_scifi.load_state(ws)["pointer"], "keep me")

    def test_no_workspace(self):
        with tmpdir() as d:
            self.assertEqual(hook("stop-pointer.sh", {}, CLAUDE_PROJECT_DIR=d).returncode, 0)


class TestInstallAndPackage(unittest.TestCase):
    def test_install_local_idempotent(self):
        with tmpdir() as d:
            settings = Path(d) / ".claude" / "settings.json"
            settings.parent.mkdir()
            settings.write_text(json.dumps({"permissions": {"allow": ["Read"]}, "hooks": {"Stop": [
                {"hooks": [{"type": "command", "command": "echo mine"}]}]}}))
            for _ in range(2):
                r = run(["bash", str(SCRIPTS / "install_local.sh"), d])
                self.assertEqual(r.returncode, 0, r.stderr)
            s = json.loads(settings.read_text())
            self.assertEqual(s["permissions"], {"allow": ["Read"]})
            cmds = [h["command"] for g in s["hooks"]["Stop"] for h in g["hooks"]]
            self.assertEqual(cmds, ["echo mine", '"$CLAUDE_PROJECT_DIR"/.claude/hooks/stop-pointer.sh'])
            self.assertEqual(len(s["hooks"]["PostToolUse"]), 1)
            self.assertNotIn("CLAUDE_PLUGIN_ROOT", settings.read_text())
            self.assertTrue(os.access(Path(d) / ".claude/hooks/validate-json.sh", os.X_OK))
            self.assertFalse(list((Path(d) / ".claude").rglob("__pycache__")))
            # the copied hook finds its validator relative to .claude/
            p = write_json(Path(d) / "Thinking-space/STATE.json", {"mode": "co-thinker"})
            r = run(["bash", str(Path(d) / ".claude/hooks/validate-json.sh")],
                    stdin=json.dumps({"tool_input": {"file_path": str(p)}}))
            self.assertEqual(r.returncode, 2)

    def test_package(self):
        with tmpdir() as d:
            r = run([sys.executable, str(SCRIPTS / "package_skills.py"), "--out", d])
            self.assertIn("SciFi-dotclaude.zip", r.stdout)
            with zipfile.ZipFile(Path(d) / "SciFi-dotclaude.zip") as z:
                names = z.namelist()
            self.assertIn(".claude/hooks/hooks.json", names)
            self.assertIn(".claude/scripts/validate_json.py", names)
            self.assertFalse([n for n in names if "__pycache__" in n])
            sw = Path(d) / "scientific-writing.skill"
            self.assertTrue(sw.is_file())
            with zipfile.ZipFile(sw) as z:
                self.assertIn("scientific-writing/SKILL.md", z.namelist())


if __name__ == "__main__":
    unittest.main()
