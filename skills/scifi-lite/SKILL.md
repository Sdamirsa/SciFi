---
name: scifi-lite
description: >
  Single-session SciFi for claude.ai and the desktop app, where no scifi skill, subagents or
  hooks exist: Claude itself maps the logic of a paragraph, runs the five checks (flow,
  neighbours, spine, evidence, style), redrafts and gates it against the bundled standards,
  writing the same JSON files as the plugin. Use on claude.ai when the user asks to check,
  rewrite, review or evaluate a paragraph, a section or a manuscript "with SciFi", or
  pastes manuscript text and asks for a logic, evidence or style review. Do not use when a
  `scifi` skill is listed; that one runs the full loop with subagents.
One session, one Claude, one unit at a time. The plugin splits this work across isolated
agents; here you play each role in turn and keep them apart by writing each role's output
before starting the next. The file formats are the plugin's, so a workspace started here can
be continued in Claude Code.

## What ships with this skill

- `references/standards/` is a copy of `skills/scientific-writing/references/` from the SciFi
  repo, plus `global-rules.md`, which is section 2 of that skill's `SKILL.md`. The packager
  puts both there. They define "good". Read `global-rules.md` once per session and the one
  section file the unit needs (`references/standards/sections/<section>.md`).
- `scripts/schemas/` is a copy of the plugin schemas and `scripts/validate_json.py` checks a file against them; `scripts/check_manuscript.py` is the style checker. Every JSON you write follows these.
- `references/protocol.md` is a copy of `docs/protocol.md`. Sections 2, 4 and 5 give the
  workspace layout, the finding format and the synthesis.

## Where output goes

- **Files available** (an uploaded folder, a project, code execution): use the workspace
  layout of protocol section 2. Write `Thinking-space/units/<id>.logic.json`,
  `handshakes/<id>.<role>.r<n>.json` per check, `handshakes/<id>.synthesis.json`,
  `units/<id>.draft.md`, and `STATE.json`. With code execution, validate each JSON against
  its schema before moving on.
- **No files**: present each artifact inline as a fenced `json` block headed with its path,
  so the user can save it and carry it into the plugin later. Never skip an artifact because
  there is nowhere to write it.

Never change the user's own text in place. Drafts are proposals next to it.

## Start

Ask, once, for what is missing: the unit (paste or id), its section, the journal (npj, jamia,
nature, lancet, ehj or default, and say which you apply), the mode (protocol section 6,
default co-thinker), and the results (a table, `results.md`, or bullet points). Without a
spine and a skeleton, build them first (below). A resumed workspace starts from `STATE.json`.

## Spine and skeleton (extract mode, for a pasted manuscript)

1. **Spine.** From the Results, list R1..Rn, each one finding with its number and its display
   item. From the Introduction, the gap. Offer 2 or 3 central claims at different scopes with
   one pick. Build threads T1..Tn (opens in the Introduction, carried by results, closes in
   the Discussion). Mark orphan results and unkept promises. Write `spine.json`.
2. **Skeleton.** One unit per paragraph with id (protocol section 2), takeaway, what it does,
   its thread, keep-here and defer notes. Run the reverse-outline test by reading the takeaway
   column alone. Write `skeleton.json`.
3. Show the human what the paper claims before checking anything against it. Proceed on
   agreement.

## The loop for one unit

Do these as separate passes. Finish and write each before reading the next role's rules.
Each check reads only its own rules and the inputs named, and judges only its own axis.

1. **logic-mapper.** Claims in order, each typed (background, gap, finding, interpretation,
   limitation, implication and the rest in the schema), each with evidence (a result id, a
   `[@citekey]`, a step from an earlier claim, or none) and strength; the steps between
   claims; the numbers used. With no text yet, generate the intended logic from the skeleton
   entry and the spine. Write `units/<id>.logic.json`.
2. **The five checks**, one envelope each, in this order:
   - **flow**: one point; first sentence gives context; last sentence is the takeaway; every
     step supports, qualifies, contrasts, extends or bridges; parallel items in parallel form.
     Propose one alternative order.
   - **local**: against the previous and next units. No backward redundancy with Methods or
     Results, no pre-emption of a later unit, a bridge from the previous takeaway, one home
     per subject.
   - **global**: against the spine and results. Serves the central claim, stays in the gap,
     serves its assigned thread, introduces no number absent from the results.
   - **evidence**: every claim against its cited source (only what the user supplied or
     pasted), the results, or a stated logical step. Supported, overstated, unsupported, or
     a NEED when the source is not available. Unverifiable is never reported as supported.
   - **style**: `references/standards/checklist.md` sections A, C, D and the section's letter,
     plus the section file. Length, abbreviations, banned words, colons, semicolons, dashes,
     "significant" without its test, number format.
3. **Synthesis.** Merge findings at the same location, order by severity, resolve each
   (accept, reject with a rule or the human's decision, defer to a named unit) per mode.
   Collect NEEDs. Write `handshakes/<id>.synthesis.json`. In co-thinker mode show the
   findings and your picks and wait for agreement.
4. **drafter.** Rewrite from the logic map and the accepted findings only. Every claim in
   order with its evidence marker, no new claims, no new numbers, pandoc citations. Keep the
   previous text below a `---- previous` marker. Return a short change list.
5. **standards-gate.** Read the draft fresh against the checklist and the section file:
   would a demanding reviewer at the journal accept it as it stands? PASS, or RETURN with at
   most three blockers. One RETURN goes back to step 4; a second goes to the human with both
   drafts.
6. **State.** Update `STATE.json` (unit status, `next_action`) and append one line to
   `log/decisions.jsonl`.

## Finding format (non-negotiable)

Every finding carries `id`, `axis` (flow, local, global, evidence, style, gate), `severity`
(blocker, major, minor, nit), `issue`, `solution`, `location` (`<unit>:s<n>` or a quote of at
most 12 words) and `rule` (the standards item, for example `checklist C2`). A finding without
a location and a rule is not reported; fix it or drop it.

## Evaluation only

For "review" or "evaluate" requests run spine, skeleton and steps 1 to 3 per unit, skip
drafting, and write `comments/<id>.json` plus a verdict (accept, minor, major, reject) with
the three problems that matter most.

## Limits here (say them when they apply)

No isolation between roles, so the checks are less independent than in the plugin. No hooks,
so validation runs only when code execution exists. No Zotero access unless a connector is
present. No end-of-session ritual; suggest the user save `STATE.json`. Details in the repo's
`docs/claude-ai.md`.
