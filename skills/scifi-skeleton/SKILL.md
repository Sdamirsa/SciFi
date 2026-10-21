---
name: scifi-skeleton
description: >
  Build or extract the reverse outline of a manuscript: per section, the ordered units with
  a one-line takeaway, what each does, the thread it serves, keep-here and defer notes, the
  display item it points to, and a word target. Use when the user says "outline my paper",
  "reverse outline", "plan the sections", "what should each paragraph say", "/scifi-skeleton",
  or when scifi reaches stage 2. Needs spine.json. Produces Thinking-space/skeleton.json.
allowed-tools: Read, Write, Glob, Grep, Agent, AskUserQuestion
---

# scifi-skeleton

The skeleton is the reverse outline: read the takeaway column alone, top to bottom, and it
tells the whole story. Every unit belongs to one thread of `spine.json`. The file is
`Thinking-space/skeleton.json` (schema `scripts/schemas/skeleton.schema.json`); the
procedure is stage 2 in `skills/scifi/stages.md`.

## Sources of structure

- Section order, abstract format and heading style from
  `skills/scientific-writing/references/journal-profiles.md` for the target journal.
- Word budgets and the move sequence per section from
  `skills/scientific-writing/references/organization.md` and the section files.
- Starting templates in `skills/scientific-writing/examples/skeleton-original-research.md`
  and `skeleton-review.md`.

## Rules the skeleton must satisfy

1. **Mirror.** Each thread opens in exactly one Introduction unit and closes in exactly one
   Discussion unit. Methods units mirror Results units in order and heading.
2. **Single home.** A subject lives in one unit; the `keep_here` and `defer` notes say where.
3. **Logical order.** Units build toward the claim, not in the order the work was done.
4. **One point per unit**, nameable in a short phrase, with a target of 80 to 150 words.
5. **Display items.** Every Results unit names the figure or table it reports; captions
   are units `c01..` with their own logic.
6. **Breadth.** A non-specialist editor can see from the takeaways alone why the paper
   matters.

## Existing manuscripts

Dispatch `logic-mapper` per section with `source: extracted`; each paragraph becomes a unit
with its takeaway and thread. Units whose takeaway serves no thread are flagged, and the
human decides: cut, merge, or add a thread to the spine (which is a spine change, with its
own gate).

## Output

`skeleton.json` with `status: agreed` after the gate, plus one decision line. Units start
with `status: planned` (no text) or `mapped` (text exists). The paragraph loop advances them
to `drafted`, `reviewed`, `accepted`. A unit the human edits by hand becomes `human-edited`
and is re-mapped before any further check.
