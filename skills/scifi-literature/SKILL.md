---
name: scifi-literature
description: >
  Build and use the literature behind a SciFi manuscript, in stages: scout (search scope,
  reviews first, role models, Zotero collection layout), notes (one structured note per paper,
  methods and results only), ontology (themes to concepts, lateral reasoning pairs), labels
  (one JSON per paper plus all_papers.json), and the lookup role that resolves a citekey to a
  source for the paragraph loop. Use when the user says "set up my library", "find papers",
  "take notes on my papers", "build an ontology", "label my papers", "crystallise my
  literature", "check this citation", "do I have a source for", "/scifi-literature", or when
  literature-scout or evidence-checker needs the resolution order for a source.
argument-hint: "[scout|notes|ontology|labels|lookup] [citekey or batch]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, AskUserQuestion
---

# scifi-literature

Files and handshakes follow `${CLAUDE_PLUGIN_ROOT}/docs/protocol.md` (relative to `.claude/`
when copied). Connecting Zotero, the citekey formula and the export are in
`docs/zotero-guide.md`. This skill does not write prose about the literature (the paragraph
loop in `scifi-paragraph` does) and does not draw figures from labels (`scifi-figures`,
corpus mode, reads `Literature/labels/all_papers.json` and `Literature/ontology.yaml`).

| Need | Read |
|---|---|
| Search scope, reviews, role models, Zotero collections | `references/library-building.md` |
| The note template and the cardinal rule | `references/note-template.md` |
| Ontology structure, passes, naming, tests, scale | `references/ontology.md` |
| Label format and decision rules | `references/labeling-rules.md` |
| Resolving a citekey, what counts as support, NEED wording | `references/lookup.md` |

## Where outputs go

```
Literature/
  library.json            human-owned export (never edited by SciFi)
  fulltext/<key>.pdf|.md   human-owned full texts (never edited by SciFi)
  notes/<key>.md           stage 1, one note per paper
  ontology.yaml            stage 2
  labels/<key>.json        stage 3, one per paper
  labels/all_papers.json   stage 3, aggregated
```

`notes/`, `ontology.yaml` and `labels/` are the only paths SciFi writes inside `Literature/`,
and only after the human starts this skill. Filenames use the citekey from `library.json`
(or the Zotero MCP) so every note, label and citation share one key.

## Who does what

| Stage | Actor | Model, effort | Writes |
|---|---|---|---|
| 0 scout | master with the human | session | a search plan in `Thinking-space/scratch/search-plan.md` |
| 1 notes | one subagent per paper, dispatched by the master | sonnet, medium | `notes/<key>.md` and its envelope |
| 2 ontology | master | session | `ontology.yaml` after the human gate |
| 3 labels | one subagent per paper, dispatched by the master | sonnet, medium | `labels/<key>.json` and its envelope |
| 3 aggregate | master (a short python3 stdlib script) | session | `labels/all_papers.json` |
| lookup | `literature-scout`, `evidence-checker` | sonnet, low and medium | envelopes only |

Batch dispatch uses the standard eight-field brief from the protocol, one paper per dispatch,
task id `lit-<nnn>.notes.r1` or `lit-<nnn>.labels.r1` with the citekey in `context`. Each
subagent writes only its own note or label file and its envelope, so parallel dispatches never
share a file. Run batches of up to ten in parallel. A missing or unreadable full text is
`status: blocked` with `NEED: full text of @key`, never a note written from the abstract.

## Stage 0: scout

Follow `references/library-building.md`. Help the human write the four-level scope (broad,
adjacent, specific, niche), find one or two reviews per level, then originals, then two or
three role models, and lay out the Zotero collections and tags. Be plain about what AI cannot
do here (the reference has the paragraph). Then connect the library by one of the two routes
in `docs/zotero-guide.md` and run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/bbt_check.py` on the
export route.

**Checkpoint.** Scope covered at every level, role models chosen and representative, PDFs
attached or listed as `full-text-not-found`, collection organised, route working.

## Stage 1: notes

1. List the papers to note (the `Original` and `Role Models` collections, or the keys the
   human names). Skip keys that already have a note unless asked to redo them.
2. Brief per paper. Inputs: the full text path (or the Zotero item key and the MCP tools
   allowed), `references/note-template.md`, and `Thinking-space/spine.json` when it exists.
   Constraints: methods and results only (the cardinal rule), "Not reported" over guessing,
   write only `Literature/notes/<key>.md`. Non-goals: the ontology, labels, judging the
   paper's place in our argument beyond the relevance banner.
3. **Checkpoint after the first two or three notes.** Show them. Ask whether depth, sections
   and the template fit. Adjust the template in the brief, not in each note. Then dispatch
   the rest.
4. Summarise: N notes written, the blocked keys with their NEEDs, papers flagged as not
   original research.

## Stage 2: ontology

Master work, because it holds the whole corpus at once. Follow `references/ontology.md`:
seed themes, populate concepts from the notes' Theme Summaries, refine, then lateral
reasoning pairs. For more than about 40 notes, read the Theme Summary sections only and open
a full note when a concept is unclear.

**Human gate.** Present the YAML with counts (themes, subthemes, groups, concepts, pairs) and
a short narrative of what the structure says about the field. Ask whether themes are well
separated, concepts complete and the pairs worth comparing. The human may edit the YAML.
Write `status: agreed` and a `version` in the file only after the gate. Changing an agreed
ontology after labelling starts is a human gate in every mode, and the changed concepts name
the papers to relabel.

## Stage 3: labels

1. Needs `ontology.yaml` with `status: agreed`; otherwise stop and say so.
2. Brief per paper. Inputs: `ontology.yaml`, `notes/<key>.md`, the full text path for
   ambiguous cases, `references/labeling-rules.md`. Output: `Literature/labels/<key>.json`.
3. **Checkpoint after the first two or three label files.** Review accuracy, coverage and
   rule calibration with the human. Fix the rules in the brief, then dispatch the rest.
4. Aggregate into `labels/all_papers.json` and report the summary statistics and quality
   checks in `references/labeling-rules.md` (papers per concept, unused concepts, sparse
   papers, concepts on more than 80 percent of papers).
5. Figures from the labels: hand over to `scifi-figures` corpus mode.

## Lookup role

When the paragraph loop needs a source, `literature-scout` (find a passage, a key, metadata)
and `evidence-checker` (judge a claim against it) resolve a citekey in this order:
`Literature/library.json`, then `Literature/fulltext/<key>.*`, then the Zotero MCP tools when
the brief lists them, then a NEED. Notes in `Literature/notes/` help locate a passage but are
never the evidence. The order, what counts as support and how NEEDs are phrased are in
`references/lookup.md`. Both agents' briefs point there.

## Gates and logging

Every stage ends with one line in `Thinking-space/log/decisions.jsonl` and a new
`STATE.json.next_action`, as in the master's gates. In human-on-the-loop and fully-automated
modes the sample checkpoints of stages 1 and 3 become reports, but the ontology gate stays a
human gate.

## Never

Edit `library.json` or `fulltext/`. Write a note or label from an abstract alone. Label what
a paper only mentions in its introduction or discussion. Invent a citekey, a number or a
source. Cite a note instead of the paper.
