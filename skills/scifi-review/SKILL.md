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
   style in parallel). No drafter, no gate. Write `comments/<id>.json`.
4. **Manuscript altitude.** `global-aligner` with scope `manuscript` (thread audit, number
   identity across abstract, results, discussion and captions, figures cited in order) and
   `standards-gate` with scope `manuscript` for the `manuscript_verdict` (accept, minor, major, reject)
   and the three highest-leverage problems.
5. **Report.** `comments/manuscript.json` with the verdict, the summary, and the comments
   ordered by severity, each with location and fix. In the conversation: the verdict, the
   three problems that matter most, and where the full list is.

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
