"""Tests for workflows/*.js: built from their templates, syntactically valid, and, run under the
mock harness, they write briefs and envelopes that validate against the schemas and route each
agent to the right type, model and effort. Skipped when node is not on PATH."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HARNESS = REPO / "scripts" / "tests" / "_workflow_harness.js"
NODE = shutil.which("node")


def run_workflow(name, args):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        json.dump(args, fh)
        args_path = fh.name
    r = subprocess.run([NODE, str(HARNESS), str(REPO / "workflows" / f"{name}.js"), args_path], capture_output=True, text=True)
    Path(args_path).unlink()
    if r.returncode != 0:
        raise AssertionError(r.stderr)
    return json.loads(r.stdout)


def validate(path):
    r = subprocess.run([sys.executable, str(REPO / "scripts" / "validate_json.py"), str(path)], capture_output=True, text=True)
    return r.returncode == 0, (r.stdout + r.stderr).strip()


@unittest.skipUnless(NODE, "node not available")
class WorkflowTests(unittest.TestCase):
    def test_built_files_in_sync(self):
        r = subprocess.run([sys.executable, str(REPO / "scripts" / "build_workflows.py"), "--check"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_review_all_end_to_end(self):
        ws = Path(tempfile.mkdtemp())
        units = [
            {"id": "d01", "section": "discussion", "text": "First paragraph text.", "takeaway": "t1", "thread": "T1", "next_takeaway": "t2"},
            {"id": "d02", "section": "limitations", "text": "Second paragraph text.", "takeaway": "t2", "thread": "T2", "prev_takeaway": "t1", "prev_text": "First paragraph text."},
        ]
        out = run_workflow("review-all", {
            "workspace": str(ws), "plugin_root": str(REPO), "journal": "lancet", "mode": "co-thinker",
            "dispatched_at": "2026-10-22T08:00:00Z", "central_claim": "The claim.", "manuscript_files": [str(ws / "Manuscript" / "discussion.md")],
            "has_analysis_plan": False, "units": units,
        })
        result = out["result"]
        self.assertEqual([u["id"] for u in result["units"]], ["d01", "d02"])
        self.assertEqual(result["units_failed"], [])
        self.assertEqual(result["manuscript"]["verdict"], "minor")
        for u in result["units"]:
            self.assertEqual(u["checks_returned"], 5)
            self.assertEqual(u["missing_envelopes"], [])
            self.assertEqual(u["findings"]["minor"], 6)
        briefs = sorted(p.name for p in (ws / "Thinking-space" / "briefs").glob("*.json"))
        self.assertEqual(len(briefs), 2 * 6 + 2, briefs)
        self.assertIn("d02.style-checker.r1.json", briefs)
        self.assertIn("manuscript.standards-gate.r1.json", briefs)
        handshakes = sorted(p.name for p in (ws / "Thinking-space" / "handshakes").glob("*.json"))
        self.assertEqual(len(handshakes), 2 * 6 + 2, handshakes)
        for p in list((ws / "Thinking-space" / "briefs").glob("*.json")) + list((ws / "Thinking-space" / "handshakes").glob("*.json")):
            ok, msg = validate(p)
            self.assertTrue(ok, f"{p.name}: {msg}")
        self.assertTrue((ws / "Thinking-space" / "scratch" / "d01.r1.txt").read_text() == "First paragraph text.")
        style = json.loads((ws / "Thinking-space" / "briefs" / "d02.style-checker.r1.json").read_text())
        self.assertTrue(any(i.endswith("sections/discussion.md") for i in style["inputs"]), style["inputs"])
        local = json.loads((ws / "Thinking-space" / "briefs" / "d02.local-aligner.r1.json").read_text())
        self.assertTrue(any(c.startswith("Previous unit text:") for c in local["context"]))
        # routing: every agent is a typed plugin agent with structured output and no model override
        self.assertTrue(all(c["agentType"] and c["agentType"].startswith("scifi:") and c["model"] is None and c["hasSchema"] for c in out["calls"]))
        self.assertEqual(sorted({c["agentType"] for c in out["calls"]}),
                         ["scifi:evidence-checker", "scifi:flow-checker", "scifi:global-aligner", "scifi:local-aligner", "scifi:logic-mapper", "scifi:scribe", "scifi:standards-gate", "scifi:style-checker"])
        self.assertFalse(any("returned_at" in json.loads(p.read_text()) for p in (ws / "Thinking-space" / "handshakes").glob("*.json")))
        shutil.rmtree(ws)

    def test_review_all_failure_paths(self):
        ws = Path(tempfile.mkdtemp())
        units = [{"id": "d01", "section": "discussion", "text": "One."}, {"id": "d02", "section": "discussion", "text": "Two."},
                 {"id": "d03", "section": "discussion", "text": "Three."}]
        out = run_workflow("review-all", {
            "workspace": str(ws), "plugin_root": str(REPO), "dispatched_at": "2026-10-22T08:00:00Z", "units": units,
            "skip_manuscript_pass": True,
            "__harness": {"fail": ["logic:d01", "evidence-checker:d02", "store:d03"], "block": ["logic:d03"]},
        })
        rows = {u["id"]: u for u in out["result"]["units"]}
        self.assertEqual(out["result"]["units_failed"], [])
        self.assertIsNone(out["result"]["manuscript"])
        # d01: logic map failed, checks skipped, nothing stored for the checks
        self.assertEqual(rows["d01"]["logic_status"], "missing")
        self.assertEqual(rows["d01"]["checks_returned"], 0)
        self.assertIn("logic-mapper", rows["d01"]["missing_envelopes"])
        self.assertFalse(list((ws / "Thinking-space" / "handshakes").glob("d01.*")))
        # d02: one check failed, the other four stored
        self.assertEqual(rows["d02"]["checks_returned"], 4)
        self.assertEqual(rows["d02"]["missing_envelopes"], ["evidence-checker"])
        self.assertEqual(len(list((ws / "Thinking-space" / "handshakes").glob("d02.*"))), 5)
        # d03: logic map blocked, its NEED surfaced, checks not run, store scribe failed so envelopes count as missing
        self.assertEqual(rows["d03"]["logic_status"], "blocked")
        self.assertTrue(rows["d03"]["needs"] and rows["d03"]["needs"][0].startswith("NEED:"))
        self.assertEqual(rows["d03"]["checks_returned"], 0)
        self.assertIn("logic-mapper", rows["d03"]["missing_envelopes"])
        self.assertIn("flow-checker", rows["d03"]["missing_envelopes"])
        self.assertEqual(rows["d03"]["invalid"], ["scribe failed"])
        self.assertFalse(any(c["label"].startswith("flow-checker:d03") for c in out["calls"]))
        shutil.rmtree(ws)

    def test_literature_all_notes_and_labels(self):
        ws = Path(tempfile.mkdtemp())
        papers = [{"citekey": "smith2023deep", "fulltext": str(ws / "Literature/fulltext/smith2023deep.md"), "number": 1},
                  {"citekey": "lee2024echo", "fulltext": None, "zotero_item_key": "ABCD1234", "number": 2}]
        base = {"workspace": str(ws), "plugin_root": str(REPO), "dispatched_at": "2026-10-22T08:00:00Z", "papers": papers, "has_spine": True, "zotero_tools": True}
        for stage, agent in (("notes", "noter"), ("labels", "labeler")):
            out = run_workflow("literature-all", dict(base, stage=stage))
            result = out["result"]
            self.assertEqual(result["failed"], [])
            self.assertEqual([p["citekey"] for p in result["papers"]], ["smith2023deep", "lee2024echo"])
            self.assertTrue(all(p["stored"] for p in result["papers"]))
            self.assertEqual({c["agentType"] for c in out["calls"]}, {f"scifi:{agent}", "scifi:scribe"})
            self.assertFalse(any("result" in p for p in result["papers"]), "rows carry no result paragraph")
            for p in list((ws / "Thinking-space" / "briefs").glob(f"lit-*.{stage}.r1.json")) + list((ws / "Thinking-space" / "handshakes").glob(f"lit-*.{stage}.r1.json")):
                ok, msg = validate(p)
                self.assertTrue(ok, f"{p.name}: {msg}")
            b = json.loads((ws / "Thinking-space" / "briefs" / f"lit-002.{stage}.r1.json").read_text())
            self.assertEqual(b["agent"], agent)
            self.assertTrue(b["output_contract"]["file"].endswith(f"/Literature/{stage}/lee2024echo." + ("md" if stage == "notes" else "json")))
        self.assertIn("Zotero item key: ABCD1234", json.loads((ws / "Thinking-space" / "briefs" / "lit-002.notes.r1.json").read_text())["context"])
        with self.assertRaises(AssertionError):
            run_workflow("literature-all", dict(base, stage="ontology"))
        with self.assertRaises(AssertionError):
            run_workflow("literature-all", dict(base, stage="notes", papers=[{"citekey": "x", "fulltext": None}]))
        # failure paths: a noter that returns null, a blocked noter, a store scribe that fails
        out = run_workflow("literature-all", dict(base, stage="notes", papers=papers + [{"citekey": "kim2025", "fulltext": None, "number": 3}],
                                                  __harness={"fail": ["noter:smith2023deep", "store:kim2025"], "block": ["noter:lee2024echo"]}))
        r = {p["citekey"]: p for p in out["result"]["papers"]}
        self.assertEqual(r["smith2023deep"]["status"], "missing")
        self.assertFalse(r["smith2023deep"]["stored"])
        self.assertEqual(r["lee2024echo"]["status"], "blocked")
        self.assertTrue(r["lee2024echo"]["needs"][0].startswith("NEED:"))
        self.assertFalse(r["kim2025"]["stored"])
        self.assertEqual(r["kim2025"]["invalid"][0], "scribe failed")
        self.assertTrue(r["kim2025"]["invalid"][1].startswith("not written: "))
        self.assertEqual(sorted(out["result"]["not_stored"]), ["kim2025", "smith2023deep"])
        self.assertEqual(out["result"]["failed"], [])
        shutil.rmtree(ws)


if __name__ == "__main__":
    unittest.main()
