# scifi: stage procedures

Every stage: do the work, dispatch the stage's agents in parallel, read their envelopes, write the synthesis, resolve per mode, apply, log, update STATE. The dispatch mechanics (brief, envelope, task ids) are in `docs/protocol.md`.

## Stage 1: spine (`scifi-spine`)

Goal: `spine.json` agreed. One central claim as one sentence; the gap; the result statements R1..Rn (each with its number, uncertainty and display item); the implications I1..In; the threads T1..Tn, each linking the sentence that opens it in the Introduction, the results that carry it and the implication that closes it.

1. If `Manuscript/results.md` exists, dispatch `logic-mapper` on it with section `results` to extract R1..Rn (findings with numbers). If `introduction.md` exists, dispatch `logic-mapper` with section `introduction` to extract gap candidates. If neither exists, ask the human for the results in any form (a table, bullet points, figures) and map those.
2. Draft 2 or 3 candidate claims at different scopes (conservative, defensible, bold). Stress-test each against the one-sentence test, the gap, the results and the design. Write the exploration to `scratch/claim-options.md`.
3. Build the threads: every result belongs to at least one thread; every thread opens in the Introduction and closes in the Discussion. A result in no thread is an orphan to be cut or promoted; a thread with no result is a promise the paper cannot keep.
4. Dispatch `global-aligner` on the draft spine (scope: spine) to check claim, gap, results and threads for consistency.
5. Gate: in co-thinker mode, present the candidates with one pick. Write `spine.json` with `status: agreed` only after the gate.

## Stage 2: skeleton (`scifi-skeleton`)

Goal: `skeleton.json` agreed. For each section the journal expects, the ordered units with a one-line takeaway, what the unit does, the thread it serves, keep-here and defer notes, the display item it points to and a target word count from the word budget in `references/organization.md`.

1. Read the journal profile for the section order and the abstract format. Start from `examples/skeleton-original-research.md` or `skeleton-review.md`.
2. Introduction and Discussion are mirrors: each thread opens in one Introduction unit and closes in one Discussion unit; the Discussion order follows the Results order, not the Introduction order, unless the human decides otherwise. Methods units mirror Results units.
3. If a manuscript exists, dispatch `logic-mapper` per existing paragraph (one dispatch per section, `source: extracted`) so each existing paragraph gets a unit id, a takeaway and a thread. Mark units whose takeaway serves no thread.
4. Run the reverse-outline test yourself: read the takeaway column alone. It must tell the whole story to a non-specialist with no gaps and no zig-zag. Dispatch `global-aligner` (scope: skeleton) and `local-aligner` (scope: skeleton, for placement and single-home content).
5. Gate as in stage 1. Write `skeleton.json` with `status: agreed`.

## Stage 3: figures (`scifi-figures`)

Goal: `figures.json` agreed, caption units created. One figure or table per Results unit where possible, Figure 1 as the overview, a flow diagram, a Table 1, a primary result figure with values on it, supplement for the rest.

1. Dispatch `figure-brainstormer` with the spine, the skeleton, `skills/scientific-writing/references/figures.md` and `tables.md`, and `skills/scifi-figures/references/brainstorm.md`: it returns 2 to 3 candidate designs per Results unit with the encoding, the numbers to print and what each would prove, plus a rejected list with reasons.
2. Resolve per mode. Write `figures.json`. Each chosen item gets a caption unit `c01..` in the skeleton with the four-part caption structure as its logic.
3. If data files exist in `Manuscript/figures/`, offer to generate the figures with a script under `Thinking-space/figures/generate_figures.py` following `skills/scifi-figures/references/figure-standards.md`; otherwise write the spec only.

## Stage 4: paragraph loop (`scifi-paragraph`)

For each unit in skeleton order, or the unit the user names. The procedure is in `skills/scifi-paragraph/loop.md`. In short: logic-mapper, then flow-checker, local-aligner, global-aligner, evidence-checker and style-checker in parallel, then the synthesis, then drafter (your model), then standards-gate (your model), then accept or return. In human-in-the-loop mode the drafter step is skipped and the human's text is what the gate judges.

## Stage 5: review (`scifi-review`)

Two uses. (a) After all units are accepted: assemble each section, run `check_manuscript.py` on the whole, dispatch `standards-gate` at section altitude (scope: section) and once at manuscript altitude, and dispatch `global-aligner` on the assembled manuscript for the thread audit (every thread opened, carried, closed; numbers identical across abstract, results, discussion, captions). (b) On an external or finished manuscript: run stages 1 and 2 in extract mode, then the five checks per unit without drafting, and write `comments/<id>.json` and `comments/manuscript.json` with a verdict. The improver then applies accepted comments as diffs into `units/<id>.draft.md`.

## Stage 6: ritual (`project-memory`)

User-typed only. Rewrites `.claude/STATUS.md`, appends to `Project-log.jsonl` and `LESSONS.jsonl`, routes the next session. Suggest it; never run it.

## Dispatch block (fill for every agent)

```json
{
  "task_id": "d03.flow-checker.r1",
  "agent": "flow-checker",
  "objective": "Judge the internal logic and order of unit d03 and return findings.",
  "context": ["Central claim: ...", "Unit takeaway: ...", "Journal: lancet", "Mode: co-thinker"],
  "inputs": ["/abs/ws/Thinking-space/units/d03.logic.json", "/abs/ws/Thinking-space/units/d03.draft.md", "/abs/ws/Thinking-space/skeleton.json"],
  "unit_text": "<the paragraph pasted here>",
  "constraints": ["Read only the listed inputs", "Return findings only; do not edit files", "Do not judge evidence, placement, spine or style; other agents own those"],
  "output_contract": {"envelope": "/abs/ws/Thinking-space/handshakes/d03.flow-checker.r1.json"},
  "done_criteria": ["Envelope validates against envelope.schema.json", "Every finding has a location and a rule"],
  "non_goals": ["Rewriting the paragraph", "Checking citations"],
  "escalation": "If an input is missing, return status blocked with the path in needs. Never guess.",
  "dispatched_at": "<ISO-8601>"
}
```

Resolve every `${CLAUDE_PLUGIN_ROOT}` path in `inputs` to an absolute path. Write the brief to `briefs/<task>.json` first (the validate-json hook checks it), then dispatch the agent with the same JSON as its prompt, preceded by one line: "Your brief follows. Reply with the envelope JSON only."
