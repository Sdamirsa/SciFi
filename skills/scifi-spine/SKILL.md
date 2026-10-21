---
name: scifi-spine
description: >
  Build or extract the spine of a scientific paper: the one central claim, the gap, the
  result statements with their numbers, the implications, and the threads of evidence that
  run from the Introduction through the Results to the Discussion. Use when the user says
  "what is my central claim", "find the threads", "what does my paper actually show", "build
  the spine", "/scifi-spine", or when scifi reaches stage 1. Produces Thinking-space/spine.json.
allowed-tools: Read, Write, Glob, Grep, Agent, AskUserQuestion
---

# scifi-spine

A paper is one claim carried by threads. This skill makes the claim and the threads explicit
in `Thinking-space/spine.json` (schema `scripts/schemas/spine.schema.json`) so every later
unit can be checked against them. The procedure is stage 1 in `skills/scifi/stages.md`.

## What a good spine looks like

- **Central claim**: one sentence, defensible for the design, a conceptual point rather than
  "better numbers": "The accuracy lost at an external site reflects scanner intensity shift
  rather than anatomy, so harmonisation at inference recovers most of it."
- **Gap**: one sentence stating what was unknown, phrased as the question the Introduction
  will leave open: "Whether site-to-site drops are fundamental or fixable is not known."
- **Results** R1..Rn: one finding each, with its number and uncertainty and the display item
  that shows it. Extracted from `results.md` by `logic-mapper`; never invented.
- **Implications** I1..In: what each finding means, at the strength the design allows.
- **Threads** T1..Tn: each links the Introduction sentence that opens it (`opens`), the
  results that carry it (`results`), the implication that closes it (`closes`) and, where it
  applies, the limitation that bounds it. Status `open` (no result yet), `carried` (result
  but no closing), `closed`, or `orphan` (a result that no thread needs).

## How Introduction and Discussion use the threads

The Introduction opens each thread in order, from the broadest (why the field matters) to
the narrowest (the exact unknown), ending in the aim. The Discussion closes them in the
order the Results delivered them, one unit per thread, each unit moving from the finding to
the comparison with prior work to the implication. A thread opened and never closed is an
unkept promise; a Discussion paragraph that closes a thread never opened is scope creep.
`global-aligner` enforces both.

## Procedure

1. Extract results (logic-mapper on `results.md`, or from what the human provides).
2. Extract gap candidates (logic-mapper on `introduction.md`) or draft them.
3. Three candidate claims at three scopes, stress-tested in `scratch/claim-options.md`.
4. Threads from results to gap; mark orphans and unkept promises.
5. `global-aligner` with scope `spine`.
6. Gate per mode; write `spine.json` with `status: agreed`; log the decision with the
   alternatives and why.

## When the spine changes later

Changing an agreed claim after units are accepted is a human gate in every mode. On change,
every accepted unit whose thread moved is set back to `mapped` in the skeleton.
