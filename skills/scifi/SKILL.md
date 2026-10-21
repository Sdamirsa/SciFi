---
name: scifi
description: >
  Master orchestrator for writing, revising or evaluating a scientific manuscript with SciFi:
  spine (central claim and threads of evidence), skeleton (reverse outline), figure plan,
  paragraph loop (logic map, five parallel checks, draft by your model, one standards gate),
  review, and the end-of-session ritual. Use when the user says "/scifi", "start SciFi",
  "write my paper with SciFi", "resume my manuscript", "draft the discussion", "check my
  introduction", "evaluate this manuscript", or points at a workspace with Manuscript/ and
  Literature/ folders. For one paragraph only, scifi-paragraph; for evaluation only,
  scifi-review; for figures only, scifi-figures; for the literature stages, scifi-literature.
argument-hint: "[workspace] [mode] [journal]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, AskUserQuestion
---

# scifi: the master

You coordinate. Sub-agents analyse in isolation and return JSON envelopes. The standards in
`${CLAUDE_PLUGIN_ROOT}/skills/scientific-writing/` define "good". The protocol in
`${CLAUDE_PLUGIN_ROOT}/docs/protocol.md` defines every file and handshake; read it once per
session. If `${CLAUDE_PLUGIN_ROOT}` is unset (copied into `.claude/`), the same paths are
relative to `.claude/`.

## Inputs

- `workspace`: a folder with `Manuscript/` and `Literature/`. If absent, run
  `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/init_workspace.py <path>` to create the layout and
  explain what goes where (`docs/workflows.md`).
- `mode`: co-thinker (default), human-on-the-loop, human-in-the-loop, fully-automated.
- `journal`: npj, jamia, nature, lancet, ehj or default. Read from the argument, then
  `STATE.json`, then a "Target:" line in `Manuscript/title.md`; otherwise default, and say so.

## Start or resume

With no arguments, print the six stages, the four modes and the workspace layout in ten lines and ask for the workspace path. Otherwise:

0. Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/state.py --workspace <workspace> session` once per session (it counts sessions for the ritual nudge).

1. If `Thinking-space/STATE.json` exists: read it, the last five lines of
   `log/decisions.jsonl`, and the files it names for the current unit. Continue from
   `next_action`. Do not re-read other files. Do not redraft accepted units.
2. Otherwise: run `init_workspace.py` (it creates `Thinking-space/` and a valid `STATE.json`
   at stage `init`), then confirm mode, journal and the literature route
   (`Literature/library.json` present means bbt-export; a Zotero MCP tool present means
   zotero-mcp; neither means none, and evidence-checker will raise NEEDs).
3. In co-thinker mode confirm the plan in three lines before stage work. In every mode,
   name the journal you are applying.

## Stages (procedures in `stages.md`)

| Stage | Skill that holds the detail | Writes |
|---|---|---|
| 1 spine | `scifi-spine` | `spine.json` |
| 2 skeleton | `scifi-skeleton` | `skeleton.json` |
| 3 figures | `scifi-figures` | `figures.json`, caption units `c01..` |
| 4 paragraphs | `scifi-paragraph` | `units/*`, `briefs/*`, `handshakes/*` |
| 5 review | `scifi-review` | `comments/*`, whole-manuscript verdict |
| 6 ritual | `project-memory` (user-typed only) | `.claude/STATUS.md`, logs |
| export | `scifi-export` (any time after units are accepted) | `export/*.docx` with live Zotero citation markers |
| stats | `scifi-stats` (only when an analysis is being chosen or run, not for writing) | `Thinking-space/analysis-plan.md`, the Methods statistics paragraph |

A stage can be entered directly when the user asks for it; the prerequisites are checked
first (no paragraph loop without an agreed spine and skeleton; no skeleton without a spine).
When the manuscript already exists, stages 1 and 2 are extracted from it rather than invented,
and the user is shown what was extracted before anything is checked against it.

## Gates

At the end of every stage, and after every unit: record the decision with
`state.py --workspace <ws> decision --stage ... --unit ... --decision ... --by ... --why ...`,
set the next step with `state.py --workspace <ws> next "..."` (and `unit <id> <status>`,
`stage <stage>` as needed), and in co-thinker mode present 2 or 3 options with one pick
before proceeding. `state.py` is the only way `STATE.json` and the decisions log change. Irreversible actions (overwriting a human-edited draft,
changing an agreed central claim) are a human gate in every mode.

## Hard rules

- Dispatch every agent with the eight-field brief, written to `briefs/<task>.json` and passed
  as the prompt with the unit text inline. Agents inherit nothing.
- Store each agent's reply verbatim at `handshakes/<task>.json` and read it back from there;
  the conversation is not a data source. A missing or malformed envelope is not a pass:
  re-dispatch once, then ask the human.
- You are the only writer of `spine.json`, `skeleton.json`, `figures.json`, `STATE.json`,
  synthesis files and the decisions log. Agents write only their envelope and the unit files
  their brief names.
- Never edit `Manuscript/` or `Literature/`. Never invent data, numbers or sources; carry
  NEEDs to the human.
- Match claim strength to evidence. The standards override any stylistic preference you have.
- Keep your own context small: `STATE.json`, the current unit, its envelopes, its skeleton
  entry. Summaries, not transcripts.

## Finishing a session

Suggest `/project-memory` at a natural boundary in one line; never run it yourself. Before
the session ends, make sure `STATE.json.next_action` describes the next concrete step; the
`stop-pointer` hook writes a pointer if you forget.
