<!-- Invented for illustration. Written by the master at stage 1 (spine). The study is fictional. -->

# Central claim options (stage 1, 2026-10-19)

Results available. R1 agreement 94.1% (kappa 0.89), R2 accuracy 96.3% versus 88.7%, R3 difference 7.6 points, R4 centre B 95.8%, R5 4.1 s per report, R6 24 of 37 errors in intermediate grades.

## A. Conservative

An open-weight LLM extracts valvular heart disease severity from echocardiography reports more accurately than a rule-based system at two centres.

- One-sentence test: passes.
- Gap: answers half of it (accuracy) and ignores the second centre as a question.
- Results carried: R2, R3, R4. R6 becomes an orphan, and R5 has no home.
- Design: fully supported.
- Weakness: reads as better numbers only. An editor asks what a registry should do differently.

## B. Defensible (picked)

An open-weight LLM run inside the hospital network extracts severity more accurately than rule-based extraction and keeps its accuracy at a second centre, with the remaining errors concentrated in reports that grade a lesion between two categories.

- One-sentence test: passes, at 40 words, the ceiling.
- Gap: matches both halves (local deployment, second centre).
- Results carried: all six, through threads T1 to T4.
- Design: supported. "Keeps its accuracy" rests on one external centre in the same health system, so the Discussion must scope it (thread T2 limitation).
- Stress test: if centre B had dropped to 90%, the claim would fail. It did not (95.8%, CI overlapping the combined estimate).

## C. Bold

Locally deployed open-weight LLMs can replace manual abstraction for valvular heart disease registries.

- One-sentence test: passes.
- Gap: goes beyond it. The study did not measure registry completeness, staff time or prospective use.
- Design: not supported. A retrospective accuracy study cannot show replacement.
- Keep as the implication I4, phrased as the next step.

## Decision

B, agreed by the human in the co-thinker gate. A is kept in `spine.json` alternatives as the fallback if a reviewer challenges the external-centre wording.
