#!/usr/bin/env bash
# install_local.sh - install SciFi into one project as a plain .claude/ folder (no plugin).
#
# Usage:
#   scripts/install_local.sh <project-dir>
#
# What it does:
#   1. copies skills/, agents/, hooks/, scripts/, workflows/ (and docs/protocol.md) from this
#      repo into <project-dir>/.claude/ (existing files with the same name are replaced; your
#      other .claude files are untouched; __pycache__ is skipped). In workflows/*.js the
#      agent prefix 'scifi:' becomes '' because agents are not namespaced in a copied install.
#   2. merges the hook wiring from hooks/hooks.json into <project-dir>/.claude/settings.json,
#      idempotently (running it twice adds nothing). Your own hooks and settings are kept.
#
# Paths: inside the plugin the hooks are called as "${CLAUDE_PLUGIN_ROOT}/hooks/x.sh". In a
# copied install there is no plugin root, so every ${CLAUDE_PLUGIN_ROOT} is replaced by
# "$CLAUDE_PROJECT_DIR"/.claude, which is where the files now live. Skills that mention
# ${CLAUDE_PLUGIN_ROOT}/scripts/... resolve to .claude/scripts/... the same way.
#
# Exit 0 on success, 1 on usage error or a failed copy or merge.
set -euo pipefail

if [ $# -ne 1 ] || [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ]; then
  sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'
  exit 1
fi

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT="$1"
if [ ! -d "$PROJECT" ]; then
  echo "install_local: $PROJECT is not a directory" >&2
  exit 1
fi
PROJECT="$(cd "$PROJECT" && pwd)"
DEST="$PROJECT/.claude"
mkdir -p "$DEST"

for d in skills agents hooks scripts workflows; do
  if [ ! -d "$REPO/$d" ]; then
    echo "install_local: $REPO/$d missing" >&2
    exit 1
  fi
  mkdir -p "$DEST/$d"
  # cp -R of the folder contents; then remove caches that came along
  cp -R "$REPO/$d/." "$DEST/$d/"
  # scifi-lite is the claude.ai variant; the full scifi skill replaces it here
  [ "$d" = skills ] && rm -rf "$DEST/skills/scifi-lite"
  if [ "$d" = workflows ]; then
    for f in "$DEST"/workflows/*.js; do
      [ -f "$f" ] && sed -i.bak "s/^const AGENT_PREFIX = 'scifi:'/const AGENT_PREFIX = ''/" "$f" && rm -f "$f.bak"
    done
  fi
  find "$DEST/$d" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
done
if [ -f "$REPO/docs/protocol.md" ]; then
  mkdir -p "$DEST/docs"
  cp "$REPO/docs/protocol.md" "$DEST/docs/protocol.md"
fi
find "$DEST/hooks" "$DEST/scripts" -name '*.sh' -exec chmod +x {} +

python3 - "$REPO/hooks/hooks.json" "$DEST/settings.json" <<'PY'
import json
import os
import sys
import tempfile

src, dst = sys.argv[1], sys.argv[2]
wiring = json.load(open(src, encoding="utf-8"))["hooks"]
PLUGIN = "${CLAUDE_PLUGIN_ROOT}"
LOCAL = '$CLAUDE_PROJECT_DIR"/.claude'   # "${CLAUDE_PLUGIN_ROOT}/hooks/x.sh" -> "$CLAUDE_PROJECT_DIR"/.claude/hooks/x.sh


def localise(cmd):
    # "\"${CLAUDE_PLUGIN_ROOT}/hooks/x.sh\"" becomes "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/x.sh"
    if cmd.startswith('"' + PLUGIN) and cmd.endswith('"'):
        return '"' + LOCAL + cmd[len(PLUGIN) + 1:-1]
    return cmd.replace(PLUGIN, '"$CLAUDE_PROJECT_DIR"/.claude')


settings = {}
if os.path.exists(dst):
    try:
        settings = json.load(open(dst, encoding="utf-8"))
    except Exception as exc:
        print(f"install_local: {dst} is not valid JSON ({exc}); fix it first", file=sys.stderr)
        sys.exit(1)
hooks = settings.setdefault("hooks", {})
added = 0
for event, groups in wiring.items():
    have = hooks.setdefault(event, [])
    existing = {h.get("command") for g in have for h in g.get("hooks", [])}
    for g in groups:
        new_hooks = []
        for h in g.get("hooks", []):
            h = dict(h)
            h["command"] = localise(h["command"])
            if h["command"] not in existing:
                new_hooks.append(h)
                existing.add(h["command"])
        if not new_hooks:
            continue
        group = {k: v for k, v in g.items() if k != "hooks"}
        group["hooks"] = new_hooks
        have.append(group)
        added += len(new_hooks)
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(dst), suffix=".json")
with os.fdopen(fd, "w", encoding="utf-8") as fh:
    json.dump(settings, fh, indent=2)
    fh.write("\n")
os.replace(tmp, dst)
print(f"settings.json: {added} hook command(s) added ({'already wired' if added == 0 else 'merged'})")
PY

cat <<EOF
SciFi installed into $DEST
  skills/ agents/ hooks/ scripts/ workflows/ docs/protocol.md copied (workflows run as /review-all, /literature-all)
  hooks wired in $DEST/settings.json with \${CLAUDE_PLUGIN_ROOT} replaced by "\$CLAUDE_PROJECT_DIR"/.claude
Where a skill says \${CLAUDE_PLUGIN_ROOT}/..., read .claude/... in this project.
Next: python3 .claude/scripts/init_workspace.py <paper-folder>, then open Claude Code and type /scifi.
EOF
