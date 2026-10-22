# Installation

SciFi runs in three places. Pick one route; the content is the same.

| Route | Gets you | Use when |
|---|---|---|
| A. Plugin from the marketplace | everything, updated with the repo | you use Claude Code and want SciFi in every project |
| B. Plugin from a local folder | everything, from your clone | you are trying a branch or editing SciFi itself |
| C. Copy into a project's `.claude/` | everything, pinned to that project | you want the files inside one repository |
| D. claude.ai skills | the standards and the single-session loop | you work in claude.ai or the desktop app without Claude Code |

Requirements for A to C: Claude Code and `python3` (standard library only, no packages).

## A. Plugin from the marketplace

Inside Claude Code:

```
/plugin marketplace add Sdamirsa/SciFi
/plugin install scifi@scifi
```

Restart the session so the hooks load. Skills, agents and hooks resolve their paths through
`${CLAUDE_PLUGIN_ROOT}`.

## B. Plugin from a local folder

```bash
git clone https://github.com/Sdamirsa/SciFi.git
claude --plugin-dir /path/to/SciFi
```

The flag applies to that session only. Pass it each time, or use route A.

## C. Copy into a project

```bash
bash /path/to/SciFi/scripts/install_local.sh /path/to/your-project
```

The script copies `skills/`, `agents/`, `hooks/`, `scripts/` and `workflows/` into
`your-project/.claude/` and adds the hook wiring to `.claude/settings.json` (the workflow
commands become `/review-all` and `/literature-all`). Paths that the
plugin resolves through `${CLAUDE_PLUGIN_ROOT}` resolve relative to `.claude/` instead; every
skill names both forms. Run the script again to update; it overwrites SciFi files and leaves
yours alone.

## D. claude.ai

Download from `dist/` in the repo:

- `scientific-writing.skill`: the standards and the checker script.
- `scifi-lite.skill`: the single-session loop, with a copy of the standards inside.

In claude.ai open the Skills section of Settings and upload each file. Code
execution must be on for the checker and for JSON validation. What works there and what does
not is in [claude-ai.md](claude-ai.md).

## Verify

In Claude Code, type `/scifi` with no arguments. It prints the six stages and asks for a
workspace. If it does not:

- `/plugin` lists installed plugins; `scifi` must be enabled (routes A and B).
- `ls .claude/skills/scifi/SKILL.md` must exist (route C).
- `python3 scripts/validate_json.py example-workspace/Thinking-space/STATE.json` from the
  repo root must exit 0, which shows Python and the schemas are in place.

In claude.ai, ask "check this paragraph with SciFi" and paste a paragraph. The reply should
name the five checks and return findings with a location and a rule.

## Optional: workflows

The batch commands (`/scifi:review-all`, `/scifi:literature-all`) are dynamic workflows. They
need workflows enabled in Claude Code (on by default on paid plans; on Pro, the Dynamic
workflows row in `/config`). Claude Code asks once before the first launch. In a headless
run (`claude -p` or the Agent SDK) add `Workflow(scifi:review-all)` and
`Workflow(scifi:literature-all)` to the allow rules, or `Workflow` for both. In a copied
`.claude/` install (route C) `workflows/` is copied too, the commands are `/review-all` and
`/literature-all`, and the allow rules are `Workflow(review-all)` and
`Workflow(literature-all)`. Without workflows, the same stages run unit by unit through the
Agent tool; nothing else changes.

## Optional: literature access

Citations resolve from `Literature/library.json` (a Better BibTeX export) or from the Zotero
MCP server. Setup for both is in [zotero-guide.md](zotero-guide.md).
