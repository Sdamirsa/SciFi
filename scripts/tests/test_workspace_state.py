"""init_workspace.py builds a valid, idempotent workspace; state.py keeps STATE.json valid
and appends decisions."""
import json
import sys
import unittest
from pathlib import Path

from _helpers import SCRIPTS, init_ws, run, tmpdir

import _scifi


def state_cmd(ws, *args):
    return run([sys.executable, str(SCRIPTS / "state.py"), "--workspace", str(ws), *args])


class TestInitWorkspace(unittest.TestCase):
    def test_creates_valid_state_and_layout(self):
        with tmpdir() as d:
            ws = Path(d) / "paper"
            r = init_ws(ws, "--mode", "human-on-the-loop", "--journal", "npj")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("What goes where", r.stdout)
            st = _scifi.load_state(ws)
            self.assertEqual(_scifi.state_errors(st), [])
            self.assertEqual((st["stage"], st["mode"], st["journal"], st["units"]),
                             ("init", "human-on-the-loop", "npj", {}))
            for rel in ["Manuscript/introduction.md", "Manuscript/results.md", "Literature/README.md",
                        "Literature/fulltext", "Thinking-space/units", "Thinking-space/briefs",
                        "Thinking-space/handshakes", "Thinking-space/comments", "Thinking-space/scratch",
                        ".claude/STATUS.md", ".claude/Project-log.jsonl", ".claude/LESSONS.jsonl"]:
                self.assertTrue((ws / rel).exists(), rel)
            lines = (ws / _scifi.DECISIONS_REL).read_text().splitlines()
            self.assertEqual(len(lines), 1)
            self.assertEqual(json.loads(lines[0])["stage"], "init")
            v = run([sys.executable, str(SCRIPTS / "validate_json.py"), str(ws / _scifi.STATE_REL)])
            self.assertEqual(v.returncode, 0, v.stderr)

    def test_idempotent_never_overwrites(self):
        with tmpdir() as d:
            ws = Path(d) / "paper"
            init_ws(ws)
            intro = ws / "Manuscript" / "introduction.md"
            intro.write_text("my own text\n")
            before = (ws / _scifi.STATE_REL).read_text()
            r = init_ws(ws, "--mode", "fully-automated")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("Nothing to create", r.stdout)
            self.assertEqual(intro.read_text(), "my own text\n")
            self.assertEqual((ws / _scifi.STATE_REL).read_text(), before)
            self.assertEqual(len((ws / _scifi.DECISIONS_REL).read_text().splitlines()), 1)

    def test_bad_mode_is_usage_error(self):
        with tmpdir() as d:
            self.assertNotEqual(init_ws(Path(d) / "p", "--mode", "chaos").returncode, 0)


class TestStateCtl(unittest.TestCase):
    def test_transitions_stay_valid(self):
        with tmpdir() as d:
            ws = Path(d) / "paper"
            init_ws(ws)
            steps = [("stage", "spine"), ("next", "Extract R1..Rn from results.md"),
                     ("unit", "i01", "mapped"), ("unit", "i02", "planned"), ("unit", "i01", "accepted"),
                     ("need", "add", "NEED: fulltext for @smith2024"), ("pointer", "mid-dispatch i02"),
                     ("session",), ("need", "clear", "NEED: fulltext for @smith2024"), ("pointer", "")]
            for step in steps:
                with self.subTest(step=step):
                    r = state_cmd(ws, *step)
                    self.assertEqual(r.returncode, 0, r.stderr)
                    self.assertEqual(_scifi.state_errors(_scifi.load_state(ws)), [])
            st = _scifi.load_state(ws)
            self.assertEqual(st["stage"], "spine")
            self.assertEqual(st["units"], {"i01": "accepted", "i02": "planned"})
            self.assertEqual(st["current_unit"], "i01")
            self.assertEqual(st["open_needs"], [])
            self.assertEqual(st["pointer"], "")
            self.assertEqual(st["session_count"], 1)
            r = state_cmd(ws, "show")
            self.assertEqual(json.loads(r.stdout)["next_action"], "Extract R1..Rn from results.md")

    def test_invalid_input_refused(self):
        with tmpdir() as d:
            ws = Path(d) / "paper"
            init_ws(ws)
            before = (ws / _scifi.STATE_REL).read_text()
            self.assertNotEqual(state_cmd(ws, "stage", "drafting").returncode, 0)
            self.assertNotEqual(state_cmd(ws, "need", "clear", "not there").returncode, 0)
            self.assertEqual((ws / _scifi.STATE_REL).read_text(), before)
            st = _scifi.load_state(ws)
            st["mode"] = "chaos"
            with self.assertRaises(ValueError):
                _scifi.write_state(ws, st)
            self.assertEqual((ws / _scifi.STATE_REL).read_text(), before)

    def test_decision_appends(self):
        with tmpdir() as d:
            ws = Path(d) / "paper"
            init_ws(ws)
            r = state_cmd(ws, "decision", "--stage", "spine", "--decision", "central claim agreed",
                          "--by", "both", "--why", "option B fits R1 and R2", "--options", "A", "B",
                          "--artifacts", "Thinking-space/spine.json")
            self.assertEqual(r.returncode, 0, r.stderr)
            rows = [json.loads(l) for l in (ws / _scifi.DECISIONS_REL).read_text().splitlines()]
            self.assertEqual(len(rows), 2)
            last = rows[-1]
            for k in ["ts", "stage", "unit", "decision", "decided_by", "options", "why", "artifacts"]:
                self.assertIn(k, last)
            self.assertEqual(last["options"], ["A", "B"])
            self.assertEqual(last["decided_by"], "both")

    def test_no_workspace(self):
        with tmpdir() as d:
            self.assertEqual(state_cmd(d, "show").returncode, 1)


if __name__ == "__main__":
    unittest.main()
