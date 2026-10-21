"""Shared fixtures for the SciFi tests: paths, a temp-workspace helper and one minimal valid
instance per schema (the schemas carry no examples of their own)."""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

TESTS = Path(__file__).resolve().parent
SCRIPTS = TESTS.parent
REPO = SCRIPTS.parent
HOOKS = REPO / "hooks"
sys.path.insert(0, str(SCRIPTS))

MINIMAL = {
    "brief": {
        "task_id": "d03.flow-checker.r1", "agent": "flow-checker", "objective": "Check flow of d03.",
        "context": ["central claim C"], "inputs": ["Thinking-space/units/d03.logic.json"],
        "constraints": ["do not edit Manuscript/"], "output_contract": {"envelope": "Thinking-space/handshakes/d03.flow-checker.r1.json"},
        "done_criteria": ["envelope validates"], "non_goals": ["evidence"],
        "escalation": "If blocked, return status blocked or a NEED in needs; never guess.",
        "dispatched_at": "2026-10-21T10:00:00Z",
    },
    "envelope": {"task_id": "d03.flow-checker.r1", "agent_id": "flow-checker", "status": "done",
                 "result": "One point, no zig-zag.", "evidence": ["read d03.logic.json"]},
    "synthesis": {"unit_id": "d03", "round": 1, "reviewed_envelopes": ["d03.flow-checker.r1"],
                  "findings": [], "decided_by": "master", "next": "draft"},
    "logic": {"unit_id": "d03", "section": "discussion", "source": "generated", "point": "x",
              "claims": [{"id": "c1", "text": "A claim.", "kind": "finding",
                          "evidence": [{"kind": "result", "ref": "R1"}], "strength": "strong"}],
              "steps": []},
    "spine": {"central_claim": "C.", "gap": "G.", "results": [{"id": "R1", "statement": "S."}],
              "threads": [{"id": "T1", "name": "n", "opens": "o", "results": ["R1"], "closes": "c"}],
              "status": "draft"},
    "skeleton": {"journal": "npj", "sections": [{"section": "introduction", "units": [
        {"id": "i01", "takeaway": "t", "does": "d", "thread": "T1"}]}], "status": "draft"},
    "figures": {"items": [{"id": "F1", "kind": "figure", "role": "primary", "shows": "s",
                           "cited_from": "r01", "status": "brainstormed"}], "status": "draft"},
    "comments": {"unit_id": "d03", "comments": [{"id": "k1", "severity": "minor", "issue": "i",
                                                 "solution": "s", "location": "d03:s2"}],
                 "created_at": "2026-10-21T10:00:00Z"},
    "state": {"workspace": "/tmp/x", "mode": "co-thinker", "journal": "default", "stage": "init",
              "next_action": "start", "updated_at": "2026-10-21T10:00:00Z"},
}


def tmpdir():
    return tempfile.TemporaryDirectory(prefix="scifi-test-")


def run(cmd, stdin="", env_extra=None, cwd=None):
    env = dict(os.environ)
    env.pop("CLAUDE_PLUGIN_ROOT", None)
    env.pop("CLAUDE_PROJECT_DIR", None)
    if env_extra:
        env.update(env_extra)
    return subprocess.run(cmd, input=stdin, capture_output=True, text=True, env=env, cwd=cwd, timeout=60)


def init_ws(path, *extra):
    return run([sys.executable, str(SCRIPTS / "init_workspace.py"), str(path), *extra])


def write_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj), encoding="utf-8")
    return path
