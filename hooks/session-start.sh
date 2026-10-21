#!/usr/bin/env bash
# session-start.sh - SessionStart hook (startup|resume|compact). Prints the SciFi resume block.
#
# Its stdout is injected into the new session's context, so "where were we" arrives without
# anyone asking. Read-only: it never writes to the workspace. It never fails the session
# (always exit 0); a broken STATE.json produces one warning line instead of a block.
#
# Usage (Claude Code runs it; to try it by hand):
#   echo '{"session_id":"x","cwd":"/path/to/paper"}' | hooks/session-start.sh
#
# Workspace lookup: $CLAUDE_PROJECT_DIR (else the payload cwd, else $PWD) when it holds
# Thinking-space/STATE.json, else the first */Thinking-space/STATE.json one level down,
# else nothing is printed.
#
# Paths: as a plugin the scripts are at ${CLAUDE_PLUGIN_ROOT}/scripts; copied into a project
# they are at .claude/scripts, which is this script's ../scripts.
export PYTHONUTF8=1
set -u

SS_INPUT="$(cat 2>/dev/null || true)"
export SS_INPUT
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export SCIFI_SCRIPTS="${CLAUDE_PLUGIN_ROOT:-$HERE/..}/scripts"

python3 - <<'PY' 2>/dev/null || true
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, os.environ["SCIFI_SCRIPTS"])
try:
    import _scifi
except Exception:
    raise SystemExit(0)

try:
    payload = json.loads(os.environ.get("SS_INPUT") or "{}")
    if not isinstance(payload, dict):
        payload = {}
except Exception:
    payload = {}

start = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
ws = _scifi.find_workspace(start)
if ws is None:
    raise SystemExit(0)

out = []
try:
    st = _scifi.load_state(ws)
except Exception as exc:
    print(f"SCIFI: {ws}/Thinking-space/STATE.json could not be read ({exc}). Fix it before stage work.")
    raise SystemExit(0)

units = st.get("units") or {}
counts = {}
if isinstance(units, dict):
    for status in units.values():
        if isinstance(status, dict):
            key = str(status.get("status", "?"))
        else:
            key = str(status)
        counts[key] = counts.get(key, 0) + 1
count_txt = ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none yet"
needs = st.get("open_needs") or []

out.append(f"SCIFI RESUME ({ws})")
out.append(f"  stage: {st.get('stage', '?')} | mode: {st.get('mode', '?')} | journal: {st.get('journal', '?')}")
out.append(f"  current unit: {st.get('current_unit') or '-'} | units: {count_txt} | open NEEDs: {len(needs)}")
out.append(f"  next_action: {st.get('next_action') or '-'}")
if st.get("pointer"):
    at = st.get("pointer_at")
    out.append(f"  pointer: {st['pointer']}" + (f" (at {at})" if at else ""))

dec = ws / _scifi.DECISIONS_REL
if dec.is_file():
    try:
        lines = [l for l in dec.read_text(encoding="utf-8").splitlines() if l.strip()][-3:]
    except OSError:
        lines = []
    if lines:
        out.append("  last decisions:")
    for line in lines:
        try:
            d = json.loads(line)
            parts = [d.get("ts", "?"), d.get("stage") or "-", d.get("unit") or "-",
                     str(d.get("decision", "")), f"by {d.get('decided_by') or d.get('by') or '?'}"]
            text = " | ".join(parts)
        except Exception:
            text = "(unparseable line) " + line[:80]
        out.append("    " + (text if len(text) <= 160 else text[:157] + "..."))

out.append("  Protocol section 10: read the files STATE.json names for the current unit, then continue from next_action.")

# Ritual nudge: STATUS.md older than 3 days, or 3 or more sessions since the last ritual.
reasons = []
status_md = ws / ".claude" / "STATUS.md"
if status_md.is_file():
    age_days = (time.time() - status_md.stat().st_mtime) / 86400.0
    if age_days >= 3:
        reasons.append(f"STATUS.md is {age_days:.0f} days old")
sc = st.get("session_count")
if isinstance(sc, int) and not isinstance(sc, bool) and sc >= 3:
    reasons.append(f"{sc} sessions since the last ritual")
if reasons:
    out.append("RITUAL: " + " and ".join(reasons) + ". Suggest the user type /project-memory at the next natural boundary (never run it yourself).")

print("\n".join(out))
PY

exit 0
