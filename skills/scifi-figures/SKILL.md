---
name: scifi-figures
description: >
  Plan, caption and generate every figure and table of a scientific paper, and make
  figures and a dashboard from a labelled literature corpus. Use when the user says "what
  figures should I make", "brainstorm figures", "plan my tables", "make Figure 1", "write
  the captions", "generate the figures", "which chart for this result", "do I need a table
  here", "dashboard from my labels", "figures from the ontology", "/scifi-figures", or when
  scifi reaches stage 3. Manuscript mode writes Thinking-space/figures.json and caption units
  c01.., and corpus mode reads Literature/labels/all_papers.json and Literature/ontology.yaml.
argument-hint: "[manuscript|corpus] [item id]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, AskUserQuestion
---

# scifi-figures

One route for all figure work, in two modes. Files and handshakes follow
`${CLAUDE_PLUGIN_ROOT}/docs/protocol.md` (relative to `.claude/` when copied). What to draw
and how to caption it is the standards skill's job, and this skill points to it rather than
repeating it.

| Need | Read |
|---|---|
| Which figures and panels, numbers on figures, supplement | `skills/scientific-writing/references/figures.md` |
| Which tables, layout, footnotes | `skills/scientific-writing/references/tables.md` |
| Caption structure, length, journal lead-ins | `skills/scientific-writing/references/captions.md` |
| Size, type, colour, layout, CrystaLit versus clinical rules | `references/figure-standards.md` |
| Brainstorm procedure and worked example | `references/brainstorm.md` |
| Corpus library, script structure, dashboard, QA | `references/corpus-figures.md` |
| Runnable script skeleton | `references/generate_figures_template.py` |

## Choose the mode

- **Manuscript mode** (default, stage 3 of `scifi`): display items for this paper's results.
  Needs `spine.json` and `skeleton.json` with `status: agreed`. If either is missing, say so
  and offer `scifi-spine` or `scifi-skeleton` first.
- **Corpus mode**: figures about the literature. Needs `Literature/labels/all_papers.json`
  and `Literature/ontology.yaml`. If missing, stop and name the file.

## Who does what

| Step | Actor | Model, effort |
|---|---|---|
| Candidate designs per Results unit | `figure-brainstormer` | sonnet, medium |
| Choice of designs, `figures.json` | master | session |
| Caption drafts as units `c01..` | `drafter` via the `scifi-paragraph` loop | inherit |
| `generate_figures.py` | a sonnet medium subagent with a brief, or the master for one or two figures | sonnet, medium |
| QA of rendered figures | master (views every PNG) | session |
| Every keep, change or drop | human, at the checkpoint | |

## Manuscript mode

1. **Brief the brainstormer.** Task id `figs.figure-brainstormer.r1`. Inputs: `spine.json`,
   `skeleton.json`, `references/brainstorm.md`, `figures.md`, `tables.md`, the journal profile
   entry, and the listing of `Manuscript/figures/`. Non-goals: captions, rendering, prose.
2. **Read the envelope.** Findings with axis `figure` are the candidates, two or three per
   Results unit, plus the fixed set and the rejected ideas.
3. **Decide.** Apply the three questions in `brainstorm.md` section 2 (what it proves, what a
   reviewer expects, what the journal prefers). Check the fixed set (section 5) and the
   journal's main display limit. In co-thinker mode show the options with one pick per unit.
4. **Write `Thinking-space/figures.json`** (schema `scripts/schemas/figures.schema.json`,
   contract below) with `status: draft`, then validate it.
5. **Create caption units.** One `c01..` per chosen item, numbered in citation order, added
   to the Results or Back matter section of `skeleton.json` with the item's takeaway, `does:
   "caption for F3"`, the thread of its results and `display` set to the item id. The logic
   map is `section: caption` with the four parts of `captions.md` section 1 as its steps.
6. **Draft captions** through `scifi-paragraph`: logic-mapper, the checks, drafter,
   standards-gate. Numbers come only from the spine results. Set the item's `caption` field to
   the unit id and its status to `drafted`.
7. **Generate figures (optional).** Only when data exist in `Manuscript/figures/`. Copy
   `generate_figures_template.py` to `Thinking-space/figures/generate_figures.py`, add one
   function per item, set `ARM_COLOURS`, `PANEL_CASE` and `ABBREV_MAP` from the manuscript,
   run it, and set each item's `script` field and status `made`. With no data, write the
   spec only and list the missing files as NEEDs.
8. **QA pass, then the checkpoint** (below). Set `status: agreed` only after it.

## Corpus mode

Follow `references/corpus-figures.md`: summarise the labels, show the summary, build
`Thinking-space/figures/corpus/generate_figures.py` from the template with one function per
figure type that fits, run it, build `dashboard/index.html`, run the QA pass, then the
checkpoint. A corpus figure that enters the manuscript gets a `figures.json` item (role
`taxonomy` or `evidence-map`) and a caption unit like any other.

## The figures.json contract

The master is the only writer. Validate after every write:
`python3 ${CLAUDE_PLUGIN_ROOT}/scripts/validate_json.py Thinking-space/figures.json`.

- `items[]`: `id` (F1, T1, S1), `kind`, `role`, `shows`, `cited_from` (a skeleton unit id),
  `status` are required. Fill `type`, `results` (spine ids), `panels` (letter, shows, n,
  stat), `data_source`, `encoding`, `numbers_on_figure`, `caption` (the `c..` unit id),
  `script`, `alternatives_considered`.
- `rejected[]`: every idea not taken, with `why`.
- Item status moves `brainstormed`, `chosen`, `drafted`, `made`, `accepted`. File status is
  `draft` until the checkpoint, then `agreed`.
- Every number in `numbers_on_figure` exists in `spine.json`. Every item is cited from a unit
  that exists, in numerical order of first citation. Every result with a `display` hint in
  the spine has an item or a `rejected` entry.

## HITL checkpoint

Show all figures and tables together, never one at a time: the rendered PNGs (or the spec
when not rendered), each with its caption draft, the unit that cites it and the results it
carries. Ask for keep, change or drop per item and iterate until the human agrees. Log one
line per decision in `log/decisions.jsonl` and update `STATE.json.next_action`. In
human-on-the-loop and fully-automated modes the checkpoint is a report, and changing an
agreed figure after captions are accepted is a human gate.

## QA pass

View every PNG at print width. Check the anti-patterns and rules in
`references/figure-standards.md` (sections 4 to 8) and the table in
`references/corpus-figures.md` section 5: labels, fonts, legend placement, arm colours,
values on bars, CI definitions, at-risk tables, panel letter case. Then cross-check numbers:
on the art, in the caption, in the spine and in the table must be identical. Fix the script
and regenerate. Report each figure as pass or the fix made.

## Never

Invent or round-trip numbers absent from the spine or the data files, edit `Manuscript/` or
`Literature/`, or mark a figure accepted that the human has not seen.
