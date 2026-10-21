#!/usr/bin/env bash
# stop-pointer.sh - Stop hook. When a turn ends and the workspace STATE.json has an empty
# "pointer", copy next_action into it with a pointer_at timestamp, so a later session knows
# where this one stopped. A non-empty pointer is left alone (the master set it on purpose).
#
# Writes only to the workspace (never to ${CLAUDE_PLUGIN_ROOT}, which changes on update).
# The new STATE.json is validated before it replaces the old one; on any problem nothing is
# written. Always exits 0: a Stop hook must not trap the session.
#
# Usage (Claude Code runs it; to try it by hand):
#   echo '{"session_id":"x"}' | CLAUDE_PROJECT_DIR=/path/to/paper hooks/stop-pointer.sh
#
# Paths: ${CLAUDE_PLUGIN_ROOT}/scripts as a plugin; .claude/scripts (this script's ../scripts) when copied.
export PYTHONUTF8=1
set -u

SP_INPUT="$(cat 2>/dev/null || true)"
export SP_INPUT
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export SCIFI_SCRIPTS="${CLAUDE_PLUGIN_ROOT:-$HERE/..}/scripts"

python3 - <<'PY' 2>/dev/null || true
import json
import os
import sys

sys.path.insert(0, os.environ["SCIFI_SCRIPTS"])
import _scifi

try:
    payload = json.loads(os.environ.get("SP_INPUT") or "{}")
    if not isinstance(payload, dict):
        payload = {}
except Exception:
    payload = {}

ws = _scifi.find_workspace(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd())
if ws is None:
    raise SystemExit(0)
st = _scifi.load_state(ws)
if (st.get("pointer") or "").strip():
    raise SystemExit(0)
nxt = (st.get("next_action") or "").strip()
if not nxt:
    raise SystemExit(0)
st["pointer"] = nxt
st["pointer_at"] = _scifi.now_iso()
_scifi.write_state(ws, st, touch=False)
PY

exit 0
