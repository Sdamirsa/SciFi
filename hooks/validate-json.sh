#!/usr/bin/env bash
# validate-json.sh - PostToolUse hook on Write|Edit|MultiEdit. Fails closed on a malformed
# SciFi file so the writer fixes it while it still has the context.
#
# What it checks:
#   - any *.json under a Thinking-space/ folder (briefs, handshakes, units/*.logic.json,
#     comments, spine, skeleton, figures, STATE): scripts/validate_json.py against the schema
#     inferred from the path. Files the validator has no schema for are parse-checked only.
#   - .claude/Project-log.jsonl and .claude/LESSONS.jsonl: every non-empty line must be JSON.
#   - *.stub.json is skipped.
# Exit 2 with the validator's message on stderr (Claude Code feeds it back to the writer);
# exit 0 otherwise.
#
# Usage (Claude Code runs it; to try it by hand):
#   echo '{"tool_name":"Write","tool_input":{"file_path":"/p/Thinking-space/STATE.json"}}' | hooks/validate-json.sh
#
# Paths: as a plugin, ${CLAUDE_PLUGIN_ROOT}/scripts/validate_json.py; copied into a project,
# .claude/scripts/validate_json.py (this script's ../scripts).
export PYTHONUTF8=1
set -u

VJ_INPUT="$(cat 2>/dev/null || true)"
export VJ_INPUT
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS="${CLAUDE_PLUGIN_ROOT:-$HERE/..}/scripts"
VALIDATOR="$SCRIPTS/validate_json.py"

# Decide what the write was, in python (robust JSON parsing); prints "<kind>\t<path>" or nothing.
target="$(python3 - <<'PY'
import json, os
from pathlib import Path
try:
    p = json.loads(os.environ.get("VJ_INPUT") or "{}")
except Exception:
    p = {}
if not isinstance(p, dict):
    p = {}
ti = p.get("tool_input") or {}
fp = ti.get("file_path") if isinstance(ti, dict) else None
if not fp:
    raise SystemExit(0)
path = Path(str(fp)).expanduser()
if not path.is_absolute():
    path = Path(str(p.get("cwd") or os.getcwd())) / path
s = path.as_posix()
if s.endswith(".stub.json"):
    raise SystemExit(0)
if s.endswith(".json") and "/Thinking-space/" in s:
    print(f"json\t{s}")
elif path.name in ("Project-log.jsonl", "LESSONS.jsonl") and path.parent.name == ".claude":
    print(f"jsonl\t{s}")
PY
)" || exit 0

[ -z "$target" ] && exit 0
kind="${target%%$'\t'*}"
file="${target#*$'\t'}"
[ -f "$file" ] || exit 0

if [ "$kind" = "json" ]; then
  if [ ! -f "$VALIDATOR" ]; then
    echo "SCIFI validate-json: validator not found at $VALIDATOR; failing closed. Reinstall SciFi or fix the path." >&2
    exit 2
  fi
  msg="$(python3 "$VALIDATOR" "$file" --quiet 2>&1)"
  rc=$?
  if [ $rc -ne 0 ]; then
    if [ -z "$msg" ]; then msg="$file: validator exited $rc"; fi
    {
      echo "SCIFI validate-json blocked this write. Fix the file and write it again."
      echo "$msg"
      echo "Schemas: $SCRIPTS/schemas/ (contract in docs/protocol.md)."
    } >&2
    exit 2
  fi
  # No schema inferred: still require that the file parses.
  if ! python3 -c 'import json,sys; json.load(open(sys.argv[1], encoding="utf-8"))' "$file" 2>/dev/null; then
    echo "SCIFI validate-json: $file is not valid JSON. Fix it and write it again." >&2
    exit 2
  fi
  exit 0
fi

# jsonl: one complete JSON object per line
msg="$(python3 - "$file" <<'PY'
import json, sys
for n, line in enumerate(open(sys.argv[1], encoding="utf-8"), 1):
    if not line.strip():
        continue
    try:
        json.loads(line)
    except json.JSONDecodeError as e:
        print(f"{sys.argv[1]}: line {n} is not valid JSON ({e.msg}). Append-only logs take one complete JSON object per line.")
        sys.exit(2)
PY
)"
rc=$?
if [ $rc -ne 0 ]; then
  echo "SCIFI validate-json blocked this write. $msg" >&2
  exit 2
fi
exit 0
