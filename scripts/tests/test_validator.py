"""validate_json.py accepts a minimal valid instance of every schema and rejects one with a
required key removed; schema inference from paths works."""
import copy
import json
import sys
import unittest
from pathlib import Path

from _helpers import MINIMAL, SCRIPTS, run, tmpdir, write_json

import validate_json

PATHS = {
    "brief": "Thinking-space/briefs/d03.flow-checker.r1.json",
    "envelope": "Thinking-space/handshakes/d03.flow-checker.r1.json",
    "synthesis": "Thinking-space/handshakes/d03.synthesis.json",
    "logic": "Thinking-space/units/d03.logic.json",
    "spine": "Thinking-space/spine.json",
    "skeleton": "Thinking-space/skeleton.json",
    "figures": "Thinking-space/figures.json",
    "comments": "Thinking-space/comments/d03.json",
    "state": "Thinking-space/STATE.json",
}


def schema(name):
    return json.loads((validate_json.SCHEMA_DIR / f"{name}.schema.json").read_text(encoding="utf-8"))


class TestValidator(unittest.TestCase):
    def test_all_nine_schemas_covered(self):
        names = sorted(p.name.split(".")[0] for p in validate_json.SCHEMA_DIR.glob("*.schema.json"))
        self.assertEqual(names, sorted(MINIMAL))

    def test_minimal_valid_in_process(self):
        for name, inst in MINIMAL.items():
            with self.subTest(schema=name):
                self.assertEqual(validate_json.validate(inst, schema(name)), [])

    def test_missing_required_key_rejected(self):
        for name, inst in MINIMAL.items():
            for key in schema(name)["required"]:
                with self.subTest(schema=name, key=key):
                    broken = copy.deepcopy(inst)
                    broken.pop(key)
                    errs = validate_json.validate(broken, schema(name))
                    self.assertTrue(any(f"missing required key '{key}'" in e for e in errs), errs)

    def test_inference_and_exit_codes(self):
        with tmpdir() as d:
            for name, rel in PATHS.items():
                with self.subTest(schema=name):
                    self.assertEqual(validate_json.infer_schema(Path(rel)), name)
                    p = write_json(Path(d) / rel, MINIMAL[name])
                    r = run([sys.executable, str(SCRIPTS / "validate_json.py"), str(p)])
                    self.assertEqual(r.returncode, 0, r.stderr)
                    bad = copy.deepcopy(MINIMAL[name])
                    bad.pop(schema(name)["required"][0])
                    write_json(p, bad)
                    r = run([sys.executable, str(SCRIPTS / "validate_json.py"), str(p)])
                    self.assertEqual(r.returncode, 2)
                    self.assertIn("missing required key", r.stderr)

    def test_enum_violation(self):
        bad = dict(MINIMAL["envelope"], status="finished")
        self.assertTrue(validate_json.validate(bad, schema("envelope")))


if __name__ == "__main__":
    unittest.main()
