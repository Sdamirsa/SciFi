---
name: project-memory
description: >
  The SciFi end-of-session ritual (CHECK, POLISH, EVOLVE, ROUTE). Validates every
  Thinking-space JSON and runs the manuscript checker on accepted units, appends the session
  to .claude/Project-log.jsonl, curates .claude/LESSONS.jsonl, rewrites .claude/STATUS.md and
  writes the single next action into STATE.json. Only the user opens it, by typing
  /project-memory at the end of a session or after a milestone. When the user says "wrap up",
  "log this session", "update memory", "update status" or "run the ritual", ask them to type
  /project-memory. Not for resuming work (that is /scifi, which reads STATE.json).
disable-model-invocation: true
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion
---

# /project-memory

Four phases, in order: **CHECK, POLISH, EVOLVE, ROUTE**, then one report.

Run it in the main session, never as a sub-agent. You are the only one who saw the whole
conversation, and curation is the part that cannot be rebuilt from disk. The user typed the
command, so this is their ritual. If you were not opened by `/project-memory`, stop and ask
them to type it.

Paths below use `SCIFI` for `${CLAUDE_PLUGIN_ROOT}` when running as a plugin, or `.claude`
when SciFi was copied into the project. `WS` is the workspace (the folder holding
`Thinking-space/`); its memory files live in `WS/.claude/`. File layout and the honesty rule
come from `SCIFI/docs/protocol.md` sections 2 and 11.

## Honesty (applies to every phase)

- Failures come with their output: the error line, the file, the schema message. No paraphrase.
- Every skipped step is named, with the reason.
- "Done" means verified. A check you did not run is reported as "unverified", never as passed.
- Separate what you witnessed in this session from what you inferred from files afterwards.
- No volatile numbers (counts, word totals, scores) in STATUS or the log. Point at the file.

## Phase 1: CHECK

```bash
for f in $(find WS/Thinking-space -name '*.json' -not -path '*/scratch/*'); do
  python3 SCIFI/scripts/validate_json.py "$f" --quiet || echo "FAIL $f"
done
```

Then, for each unit whose status in `STATE.json` (or `skeleton.json`) is `accepted`:

```bash
python3 SCIFI/skills/scientific-writing/scripts/check_manuscript.py \
  WS/Thinking-space/units/<id>.draft.md --journal <journal>
```

Read only the text above the `---- previous` marker; if the checker cannot be pointed at that
part alone, copy it to `scratch/tmp-<id>.md` first.

- A schema **FAIL** stops the ritual. Fix it if you can (the error names the field), rerun,
  and continue only on exit 0. If it cannot be fixed now, say so plainly with the output,
  skip POLISH and EVOLVE, and go to the report. A clean wrap-up over a failed check is the
  false "done" this ritual exists to prevent.
- Checker flags on an accepted unit do not stop the ritual. List them in the report and as a
  next step in STATUS. An accepted unit is not redrafted here.
- Then verify what no script can. Does `STATE.json.next_action` still describe reality? Does
  every unit marked `accepted` have a gate PASS envelope in `handshakes/`? Where they disagree,
  disk wins; correct `STATE.json` first and log the correction.

## Phase 2: POLISH

**2a. Reconstruct the session.** Decisions and their reasons, units drafted or accepted,
spine or skeleton changes, mistakes on both sides, open NEEDs, next steps. Signal only.
`log/decisions.jsonl` is the source for stage decisions; this conversation is the source for
the rest.

**2b. Append to `WS/.claude/Project-log.jsonl`**, one condensed line per real thing:

```json
{"date":"YYYY-MM-DD","type":"decision|deliverable|milestone|analysis|note|mistake|tooling",
 "title":"grep-skimmable","summary":"1-2 sentences: what and why",
 "artifacts":["Thinking-space/relative/path"],"tags":["..."],"source":"session|artifacts|git"}
```

`source` is an epistemic tag. `session` means you witnessed it; `artifacts` or `git` means you
inferred it from files. Append only, one complete line per entry, never rewrite or reorder
past lines. Check each appended line parses
(`tail -n <k> WS/.claude/Project-log.jsonl | python3 -c "import sys,json;[json.loads(l) for l in sys.stdin]"`).

**2c. Curate `WS/.claude/LESSONS.jsonl`.** One row per real mistake (one that cost rework, a
wrong output, lost time or a misleading report), whoever made it:

```json
{"id":"L-<n>","date":"YYYY-MM-DD","who":"agent|human|both","what":"...",
 "root_cause":"...","prevention":"mechanical and checkable","active":true}
```

The prevention must be executable by a future session ("run bbt_check.py before the evidence
pass", "grep results.md for the number before drafting"). "Be more careful" prevents nothing.
Keep one to three rows `active`. Retire a rule by setting `active` to false; never delete a
row. Every `mistake` in the log that could recur gets a row here.

**2d. Rewrite `WS/.claude/STATUS.md` from scratch** using `STATUS.template.md` in this folder.
Fill every section; write "none" rather than dropping one. 15 to 30 lines. Next steps must be
concrete enough to start from cold. Watch-outs mirror the active lessons by id.

## Phase 3: EVOLVE (one soft pass)

Look back at the session for friction: an instruction you needed twice, a finding the human
rejected for the same reason more than once, a skeleton note that kept misleading a checker,
a standards rule that was applied wrongly or missed. Propose **at most three** changes, each
to a skeleton note (`keep_here`, `defer`, a takeaway) or to how the standards are used in this
workspace (which rule to quote in a brief, which section file to load).

Write them under "Proposals" in STATUS.md, each as one line with the evidence and the exact
change. Never apply a proposal silently. If the human approves one now, apply it, log a
`tooling` line, and mark it applied in STATUS. "No proposals: <reason>" is a good outcome.

## Phase 4: ROUTE

1. Decide the single next action, concrete and startable ("Run the loop on d03 with the
   accepted spine; d02 is accepted"). Write it with
   `python3 SCIFI/scripts/state.py --workspace WS next "<action>"`, then run
   `python3 SCIFI/scripts/state.py --workspace WS ritual` (it sets `last_ritual`, resets
   `session_count` and validates `STATE.json`). If a script fails, report its output and do
   not hand-edit around it.
2. Suggest the mode for the next session in one line, with the reason. The modes are in
   `SCIFI/docs/protocol.md` section 6, for example "Stay in co-thinker; the Discussion
   claims still need your calls" or "human-on-the-loop is fine for the Methods units".
   The human sets it; you do not.

## The report

One block, in this order: what CHECK found (failures with output, checker flags per unit,
corrections to STATE), what was logged (titles only) and which lessons are active, what
changed in STATUS, the EVOLVE proposals, the next action and the suggested mode, and every
skipped or unverified step with its reason.

## Not in this ritual

No git commit or push (the human decides that), no generators, no tickets, no edits to
`Manuscript/` or `Literature/`, no redrafting of units.
