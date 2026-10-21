# Workflows

How to drive SciFi from Claude Code. Files and handshakes are defined once in
[protocol.md](protocol.md); this page shows which command does what and walks through five
common sessions.

## Commands and phrases

| Type this | Or say | What runs |
|---|---|---|
| `/scifi [workspace] [mode] [journal]` | "start SciFi", "write my paper with SciFi", "resume my manuscript", "draft the discussion", "check my introduction" | the master, which starts or resumes the pipeline |
| `/scifi-spine` | "what is my central claim", "find the threads", "build the spine" | stage 1 only |
| `/scifi-skeleton` | "outline my paper", "reverse outline", "what should each paragraph say" | stage 2 only |
| `/scifi-figures` | "plan my figures", "which tables should I make" | stage 3 only |
| `/scifi-paragraph <id>` | "fix this paragraph", "check paragraph 3 of the discussion", "is this paragraph logical" | the loop on one unit |
| `/scifi-review [path] [journal] [--improve]` | "review my paper", "evaluate this manuscript", "act as reviewer 2" | evaluation, comments, optional diffs |
| `/project-memory` | (user-typed only; phrases get a request to type it) | the end-of-session ritual |
| `/panel-discussion` | "let's debate this", "what would experts think" | a decision utility for hard calls |

`/scifi` with no arguments prints the stages and asks for a workspace.

## The six stages

| Stage | Writes in `Thinking-space/` | Gate |
|---|---|---|
| 1 spine | `spine.json` (claim, gap, R1.., I1.., threads T1..), `scratch/claim-options.md` | you agree the central claim |
| 2 skeleton | `skeleton.json` (units with takeaway, thread, keep and defer notes, word target) | you agree the reverse outline |
| 3 figures | `figures.json`, caption units `c01..` in the skeleton | you pick the display items |
| 4 paragraphs | per unit `units/<id>.logic.json`, `briefs/*`, `handshakes/*`, `<id>.synthesis.json`, `units/<id>.draft.md` | per unit, the standards gate and you |
| 5 review | `comments/<id>.json`, `comments/manuscript.json` | the verdict |
| 6 ritual | `.claude/STATUS.md`, `Project-log.jsonl`, `LESSONS.jsonl`, `STATE.json` next action | none |

Every stage appends to `log/decisions.jsonl` and rewrites `STATE.json`. Procedures are in
`skills/scifi/stages.md`.

## Control modes

Four modes set where you decide: co-thinker (default), human-on-the-loop, human-in-the-loop,
fully-automated. The table is in [protocol.md section 6](protocol.md#6-control-modes). Pass
the mode as the second argument to `/scifi` or say "switch to human-on-the-loop".

## First session

The repo ships `example-workspace/`, an invented echocardiography LLM study with nothing real
in it. Copy it so the original stays clean:

```bash
cp -r /path/to/SciFi/example-workspace ~/scifi-demo
cd ~/scifi-demo && claude
```

1. Type `/scifi example-workspace co-thinker lancet`. The master reads `STATE.json`, names the journal and the
   literature route, and states the plan in three lines.
2. Stage 1. It maps `Manuscript/results.md` into result statements and offers two or three
   central claims with one pick. Agree or edit. `spine.json` is written.
3. Stage 2. It proposes the skeleton. Read the takeaway column alone; it should tell the
   story. Agree. `skeleton.json` is written.
4. Stage 4 on one unit, for example `i01`. You see the five envelopes merged into findings
   with picks, then the draft as a diff, then the gate verdict.
5. Stop at a natural boundary and type `/project-memory`.

For your own paper, `/scifi ~/my-paper` on a folder without `Thinking-space/` runs
`scripts/init_workspace.py` and explains what goes in `Manuscript/` and `Literature/`.

## Resume

Open Claude Code in the workspace. The session-start hook prints the resume block from
`STATE.json`. Type `/scifi` (or say "resume my manuscript"). The master reads `STATE.json`,
the last five lines of `log/decisions.jsonl` and the current unit's files, then continues
from `next_action`. Accepted units are not redrafted. A unit you edited by hand is re-mapped
first. Rules in [protocol.md section 10](protocol.md#10-resume).

## Evaluate an existing manuscript

1. Put the sections in `Manuscript/` and the cited papers in `Literature/`.
2. `/scifi-review . lancet`. The spine and skeleton are extracted and shown to you first;
   correct them if the paper claims something else.
3. The checker script runs on the whole text, then the five checks per unit, then the
   manuscript-level thread audit and verdict.
4. Read `comments/manuscript.json`: verdict, the three problems that matter most, every
   comment with severity, location, rule and fix. Without full texts, evidence comments are
   `unverified`.
5. Mark comments accept, reject or defer, then `/scifi-review --improve` applies the accepted
   ones as minimal diffs into `units/<id>.draft.md`. `Manuscript/` is not touched.

## One paragraph

With an agreed spine and skeleton, `/scifi-paragraph d03`. Without them, paste the paragraph
and say "check this discussion paragraph". It becomes unit `x01`, and the master asks for the
central claim and the results it needs, or runs the spine first. The loop is in
`skills/scifi-paragraph/loop.md`.

## End of session

Type `/project-memory`. It validates every JSON, runs the checker on accepted units, logs the
session, curates lessons, rewrites `.claude/STATUS.md`, proposes at most three changes, and
writes the next action into `STATE.json`. A failed check stops it and says why. Details in
`skills/project-memory/SKILL.md`.

## Export to Word and Google Docs

`/scifi-export --library users/<id>` writes `export/<name>.docx` with Scannable Cite markers for every `[@citekey]`, plus a report of unmapped keys. Then follow the seven steps in [zotero-guide.md](zotero-guide.md#export-to-word-and-google-docs-with-live-citations). Needs `Literature/library.bbt.json` (Better BibTeX JSON export).

## Choose a statistical method

`/scifi-stats <question>` classifies the question, the outcome and exposure types and the design, picks the standard method from `skills/scifi-stats/references/method-map.md`, applies the complexity guard (bespoke methods need a written justification and a human gate), and writes `Thinking-space/analysis-plan.md` plus the Methods statistical-analysis paragraph. It triggers only for analysis questions, not for writing about statistics.
