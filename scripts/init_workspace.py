#!/usr/bin/env python3
"""Create (or complete) a SciFi workspace. Stdlib only. Idempotent: existing files are never
overwritten, so it is safe to run on a folder that already holds your manuscript.

Usage:
    python3 init_workspace.py <path> [--mode co-thinker|human-on-the-loop|human-in-the-loop|fully-automated]
                                     [--journal npj|jamia|nature|lancet|ehj|default]

As a plugin:  python3 "${CLAUDE_PLUGIN_ROOT}/scripts/init_workspace.py" <path>
Copied:       python3 .claude/scripts/init_workspace.py <path>

Creates Manuscript/ (one file per section), Literature/ (README, fulltext/), Thinking-space/
(STATE.json at stage init, log/decisions.jsonl, units/, briefs/, handshakes/, comments/,
scratch/) and .claude/ (STATUS.md, Project-log.jsonl, LESSONS.jsonl). The layout is defined in
docs/protocol.md section 2. Exits 0 on success, 1 on a usage error, 2 when STATE.json would be
invalid.
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _scifi  # noqa: E402

MODES = ["co-thinker", "human-on-the-loop", "human-in-the-loop", "fully-automated"]

SECTIONS = {
    "title.md": "<!-- Title. Optional second line \"Target: <journal>\" (npj, jamia, nature, lancet, ehj) tells SciFi which profile to apply. -->\n",
    "abstract.md": "<!-- Abstract. Format follows the journal profile; SciFi drafts it last, from the agreed spine. -->\n",
    "introduction.md": "<!-- Introduction. One paragraph per block, blank line between paragraphs; cite as [@citekey]. -->\n",
    "methods.md": "<!-- Methods. Your text; SciFi checks it and never edits this file. -->\n",
    "results.md": "<!-- Results. Findings with numbers and uncertainty; the spine's R1..Rn are extracted from here. -->\n",
    "discussion.md": "<!-- Discussion. Mirrors the introduction: each thread opened there is closed here. -->\n",
    "captions.md": "<!-- Figure and table captions, one block per display item (F1, T1, ...). -->\n",
}

LIT_README = """# Literature

SciFi reads this folder and never edits it.

- `library.json`: a Better CSL JSON export of the paper's Zotero collection (Better BibTeX,
  "Keep updated"). Citation keys here are the `[@citekey]` used in Manuscript/.
- `fulltext/<citekey>.pdf` or `fulltext/<citekey>.md`: the full text of each cited source, so
  the evidence-checker can verify claims against the source rather than the abstract.

With the Zotero MCP route (`templates/mcp.zotero.json`), library.json is optional. Setup for
both routes: docs/zotero-guide.md.
"""

STATUS_MD = """# STATUS

<!-- Rewritten by the user-typed /project-memory ritual. Read at session start after Thinking-space/STATE.json. -->

## Where the paper is
- Stage: init
- Next: agree the spine (central claim, gap, results, threads)

## Open questions for the human
- none yet

## Recent decisions
- workspace created
"""


def write_if_missing(path: Path, text: str, created: list):
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    created.append(path)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Create a SciFi workspace (idempotent).")
    ap.add_argument("path")
    ap.add_argument("--mode", default="co-thinker", choices=MODES)
    ap.add_argument("--journal", default="default")
    args = ap.parse_args(argv)

    ws = Path(args.path).expanduser().resolve()
    created = []
    for d in ["Manuscript", "Literature/fulltext", "Thinking-space/log", "Thinking-space/units",
              "Thinking-space/briefs", "Thinking-space/handshakes", "Thinking-space/comments",
              "Thinking-space/scratch", ".claude"]:
        p = ws / d
        if not p.is_dir():
            p.mkdir(parents=True, exist_ok=True)
            created.append(p)

    for name, header in SECTIONS.items():
        write_if_missing(ws / "Manuscript" / name, header, created)
    write_if_missing(ws / "Literature" / "README.md", LIT_README, created)

    state_path = ws / _scifi.STATE_REL
    if not state_path.exists():
        route = "bbt-export" if (ws / "Literature" / "library.json").is_file() else "none"
        state = {
            "workspace": str(ws),
            "mode": args.mode,
            "journal": args.journal,
            "stage": "init",
            "units": {},
            "open_needs": [],
            "pointer": "",
            "next_action": "Confirm mode, journal and literature route, then start stage 1 (spine).",
            "literature_route": route,
            "session_count": 0,
            "updated_at": _scifi.now_iso(),
        }
        try:
            _scifi.write_state(ws, state)
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2
        created.append(state_path)

    dec = ws / _scifi.DECISIONS_REL
    if not dec.exists():
        _scifi.append_jsonl(dec, {
            "ts": _scifi.now_iso(), "stage": "init", "unit": "", "decision": "workspace created",
            "decided_by": "human", "options": [], "why": "init_workspace.py",
            "artifacts": ["Thinking-space/STATE.json"],
        })
        created.append(dec)

    write_if_missing(ws / ".claude" / "STATUS.md", STATUS_MD, created)
    write_if_missing(ws / ".claude" / "Project-log.jsonl", "", created)
    write_if_missing(ws / ".claude" / "LESSONS.jsonl", "", created)

    print(f"SciFi workspace: {ws}")
    if created:
        print(f"Created {len(created)} item(s):")
        for p in created:
            print(f"  + {p.relative_to(ws)}")
    else:
        print("Nothing to create; every file already exists (nothing was overwritten).")
    print("""
What goes where:
  Manuscript/     your sections as markdown, citations as [@citekey]. SciFi never edits it.
                  Put "Target: <journal>" on the second line of title.md to pick the profile.
  Literature/     library.json (Better CSL JSON export) and fulltext/<citekey>.pdf or .md.
                  See Literature/README.md. SciFi never edits it.
  Thinking-space/ everything SciFi makes: STATE.json, spine, skeleton, units, briefs,
                  handshakes, comments, log/decisions.jsonl. You can read it; the master writes it.
  .claude/        the memory spine: STATUS.md, Project-log.jsonl, LESSONS.jsonl (/project-memory).
Next: open Claude Code in this folder and type /scifi.""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
