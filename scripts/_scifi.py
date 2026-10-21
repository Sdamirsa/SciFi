#!/usr/bin/env python3
"""Shared helpers for the SciFi scripts and hooks. Stdlib only. Not a command.

Imported by state.py, init_workspace.py and the hooks (session-start.sh, stop-pointer.sh).
Paths: as a plugin this folder is ${CLAUDE_PLUGIN_ROOT}/scripts; copied, it is .claude/scripts.

    find_workspace(start)  -> Path of the workspace (the folder holding Thinking-space/STATE.json) or None
    load_state(ws)         -> dict
    write_state(ws, state) -> validates against state.schema.json, then writes atomically
    now_iso()              -> UTC timestamp, seconds precision, trailing Z
"""
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import validate_json  # noqa: E402  (same folder)

STATE_REL = Path("Thinking-space") / "STATE.json"
DECISIONS_REL = Path("Thinking-space") / "log" / "decisions.jsonl"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_iso(text):
    """Parse the timestamps SciFi writes (and plain ISO 8601). None when unparseable."""
    if not text:
        return None
    try:
        dt = datetime.fromisoformat(str(text).replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def find_workspace(start=None):
    """The workspace is `start` when it holds Thinking-space/STATE.json, else the first child
    folder (one level down, sorted) that does. None otherwise."""
    base = Path(start or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()).expanduser()
    try:
        base = base.resolve()
    except OSError:
        return None
    if (base / STATE_REL).is_file():
        return base
    try:
        hits = sorted(base.glob("*/Thinking-space/STATE.json"))
    except OSError:
        hits = []
    return hits[0].parent.parent if hits else None


def load_state(ws):
    return json.loads((Path(ws) / STATE_REL).read_text(encoding="utf-8"))


def state_errors(state):
    schema = json.loads((validate_json.SCHEMA_DIR / "state.schema.json").read_text(encoding="utf-8"))
    return validate_json.validate(state, schema)


def atomic_write_text(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=".tmp-", suffix=path.suffix)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def write_state(ws, state, touch=True):
    """Validate, then write STATE.json atomically. Raises ValueError with the schema errors."""
    if touch:
        state["updated_at"] = now_iso()
    errs = state_errors(state)
    if errs:
        raise ValueError("STATE.json would be invalid: " + "; ".join(errs))
    atomic_write_text(Path(ws) / STATE_REL, json.dumps(state, indent=2, ensure_ascii=False) + "\n")


def append_jsonl(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(obj, ensure_ascii=False) + "\n")
