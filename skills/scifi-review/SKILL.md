---
name: scifi-review
description: >
  Evaluate a manuscript, a section or a unit without drafting: run the SciFi checks, write
  reviewer-style comments (severity, location, rule, fix) as JSON, give a verdict, and on
  request apply the accepted comments as minimal diffs. Use when the user says "review my
  paper", "evaluate this manuscript", "act as reviewer 2", "what would a Lancet editor say",
  "comment on my discussion", "/scifi-review", or uploads a finished manuscript for
  assessment. Also the whole-manuscript gate at the end of the scifi pipeline.
argument-hint: "[path or unit-id] [journal] [--improve]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, AskUserQuestion
---

# scifi-review

Same agents, same standards, same files as the writing loop, two differences: nothing is
drafted unless `--improve` is given, and the output is `comments/<id>.json` (schema
`comments`) rather than a redraft. Procedure: stage 5 in `skills/scifi/stages.md`.

## Procedure for a whole manuscript

1. **Extract the spine and skeleton** (stages 1 and 2 in extract mode). Show the human what
   the paper claims and promises before checking anything against it; a review built on
   the wrong central claim is useless.
2. **Script pass.** `python3 ${CLAUDE_PLUGIN_ROOT}/skills/scientific-writing/scripts/check_manuscript.py <file> --journal <journal>` on the
   whole manuscript. Its flags become `style` comments.
3. **Per unit**, the five checks (logic-mapper first, then flow, local, global, evidence,
   style in parallel). No drafter, no gate. For more than about six units, or when the user
   says "use a workflow", run steps 3 and 4 as one batch with the `review-all` workflow
   (below) instead of dispatching unit by unit; then synthesise each unit from its envelopes
   in `handshakes/` exactly as for a dispatched unit. Write `comments/<id>.json`.
4. **Manuscript altitude.** `global-aligner` with scope `manuscript` (thread audit, number
   identity across abstract, results, discussion and captions, figures cited in order) and
   `standards-gate` with scope `manuscript` for the `manuscript_verdict` (accept, minor, major, reject)
   and the three highest-leverage problems.
5. **Report.** `comments/manuscript.json` with the verdict, the summary, and the comments
   ordered by severity, each with location and fix. In the conversation: the verdict, the
   three problems that matter most, and where the full list is.

## The `review-all` workflow (steps 3 and 4 as one batch)

`workflows/review-all.js` runs logic-mapper and the five checks on every unit in parallel,
stores every brief and envelope in `briefs/` and `handshakes/` through a scribe agent, runs
the two manuscript-altitude agents, and returns per-unit counts, blockers and NEEDs. Nothing
inside it asks the human, so it fits every mode. Call the Workflow tool with name
`scifi:review-all` (plugin) or `review-all` (copied `.claude/`) and these args, all paths
absolute: `workspace`, `plugin_root`, `journal`, `mode`, `dispatched_at` (the ISO timestamp,
since scripts cannot read the clock), `round`, `central_claim`, `manuscript_files`,
`has_analysis_plan`, and `units`, one entry per skeleton unit with `id`, `section`, `text`,
`takeaway`, `thread`, `prev_takeaway`, `next_takeaway`, `prev_text`, `next_text` and
`word_target`. Read the returned summary, then do step 3's synthesis from the stored
envelopes. A unit in `units_failed` or with `missing_envelopes` is re-dispatched once with
the Agent tool; a unit whose `logic_status` is `blocked` carries a NEED for the human, not a
re-dispatch. A second run after the human has changed text passes `round` n+1 so the earlier
briefs, envelopes and scratch text survive. The header of the script lists the args; protocol section 12 states
what a workflow may and may not do.

## Procedure with `--improve`

After the human resolves the comments (accept, reject, defer; in fully-automated mode the
master resolves), dispatch `improver` per unit with the accepted comments. It applies the
smallest diff that resolves each, lists every change with its comment id, and writes
`units/<id>.draft.md`. The standards gate runs once per improved unit.

## Comment style

Comments read as a careful reviewer writes them: the location, what is wrong, why it matters
(the rule), and the fix. No praise padding, no "consider", no rhetorical questions. Severity:
`blocker` (the paper cannot be accepted with this), `major` (a reviewer would require it),
`minor` (an editor would fix it), `nit` (polish). The same list serves as the response-to-
reviewers skeleton later: each comment id is stable.

## Reviewing someone else's paper

The system reviews what is in front of it and never invents sources. If the cited full texts
are not in `Literature/` and no Zotero route exists, evidence comments are `unverified`, not
`unsupported`, and the report says so.
