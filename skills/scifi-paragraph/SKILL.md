---
name: scifi-paragraph
description: >
  Run the SciFi paragraph loop on one unit: map its logic (claims, evidence, steps), run five
  parallel checks (internal flow, local alignment with neighbours, global alignment with the
  spine and results, evidence backing, length and style), synthesise, redraft with your model,
  and pass one standards gate. Use when the user says "/scifi-paragraph <id>", "fix this
  paragraph", "check paragraph 3 of the discussion", "rewrite the second intro paragraph",
  "is this paragraph logical", or pastes a single paragraph and asks for a review or rewrite.
  Needs an agreed spine.json and skeleton.json; otherwise it runs scifi-spine first.
argument-hint: "[unit-id or 'paste'] [mode]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent, AskUserQuestion
---

# scifi-paragraph

One unit, one loop. The full procedure with the brief for each agent is in `loop.md`; read it
the first time in a session. The protocol is `docs/protocol.md`.

## Steps

1. **Locate the unit.** From `skeleton.json` by id, or from a pasted paragraph (create a
   temporary unit `x01` with the section the user names). Load its skeleton entry, the
   previous and next units' takeaways and drafts, and the spine.
2. **Map.** Dispatch `logic-mapper` (sonnet, medium). It writes `units/<id>.logic.json`:
   claims in order, each typed and tied to evidence (a result id, a citekey, a logical step
   from an earlier claim, or none), the steps between claims, the numbers used. With no text
   yet, it generates the intended logic from the skeleton entry and the spine.
3. **Check, five in parallel.** Write the unit text to `scratch/<id>.r<n>.txt` first for the style-checker.
   Store every reply verbatim at `handshakes/<task>.json`. `flow-checker`, `local-aligner`, `global-aligner`,
   `evidence-checker` (sonnet, medium) and `style-checker` (sonnet, low). Each gets the brief
   in `loop.md`, reads only its inputs, and returns an envelope with findings.
4. **Synthesise.** Read the five envelopes. De-duplicate (the same sentence flagged on two
   axes is one finding with two rules). Resolve each per mode: accept, reject with a reason,
   defer with the unit it belongs to. Write `handshakes/<id>.synthesis.r<n>.json`. Collect NEEDs.
5. **Draft.** Dispatch `drafter` (inherit) with the logic map, the accepted findings, the
   skeleton entry, the section's standards file and the journal. It writes
   `units/<id>.draft.md`, keeping the previous version below a `---- previous` marker.
   In human-in-the-loop mode skip this step; the human's text is the draft.
6. **Gate.** Dispatch `standards-gate` (inherit) once. PASS: mark the unit accepted. RETURN:
   up to three blockers go back to step 5 once; a second RETURN goes to the human with the
   blockers and the two drafts.
7. **Log and state.** Append the decision line, update `STATE.json` (unit status, next unit).

## Rules

- A finding without a `location` and a `rule` is sent back to its agent.
- Numbers in the draft come from `spine.json` results or `results.md`; the drafter never
  introduces a number that is not there, and `global-aligner` fails any that appear.
- Hedges match evidence; the standards' verb table applies. "Significant" needs its test.
- Pandoc citations `[@citekey]` only; every key must exist in `Literature/library.json` or
  resolve through the Zotero MCP, or it becomes a NEED.
- One loop per unit per round. Do not run the five checks again on an unchanged draft.
