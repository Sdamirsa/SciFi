# The complexity guard

Why it exists: a language model asked for "the best analysis" tends to produce a method that is plausible, elaborate and unique to the paper in front of it (a custom composite score, a weighting scheme, a correction chosen after seeing the data, a nested model with more parameters than the sample can support). Such a method cannot be checked against a reference, cannot be reproduced by a reader, and usually hides a weak result. The guard makes "standard" the default and "custom" the exception that must earn its place.

## The test

A method passes without discussion when **all** of these hold:

1. It is the cell in `method-map.md` for this question and data type, or its listed fallback.
2. Its assumptions are named and a check for each is planned.
3. The sample supports it (events per predictor, groups large enough for the asymptotics, no cluster treated as independent).
4. It was decided before looking at the outcome data, or it is labelled exploratory.
5. Its output is an effect estimate with a confidence interval that a reader can interpret without a new definition.

A method **needs a justification and a human gate** when any of these holds:

- A metric, score, index or weighting is defined in this paper for the first time.
- A threshold, cut-off, grouping or transformation was chosen after seeing the results.
- A correction, trimming, outlier rule or exclusion is not in a cited reference.
- The model has more than one parameter per ten events, or more than three interaction terms, or stepwise selection.
- The method appears in no reporting guideline, textbook or two papers in the target journal family (name them).
- The method gives a materially different answer from the standard one, and the standard one is not reported alongside.
- The analysis unit differs from the sampling unit (scans versus patients, segments versus reports) without a clustering term.

## What the justification must contain

1. The standard method and its result (always run first).
2. Why it is insufficient here, in one or two sentences tied to a named assumption or a design feature, not to the size of the effect.
3. A citation for the alternative method as used in a comparable setting.
4. What the alternative adds and what it costs (interpretability, assumptions, degrees of freedom).
5. The statement that both results are reported and which one is primary.

If any of the five cannot be written, the alternative is not used.

## Signals that the guard should fire (seen in practice)

- "We propose a novel metric that combines ..."
- "After inspecting the distribution we chose ..."
- "To account for all factors we built a model with ... 14 covariates" on 60 events.
- "Significance was assessed with ..." a test the reader has to look up.
- Accuracy reported as mean ± SD over three runs with the same cases, presented as uncertainty.
- An AUROC comparison between models evaluated on different test sets.
- A p value from a test on a summary statistic the paper defined.
- "External validation" on a random split of one dataset.

## Allowed "non-simple" methods, because they are the standard for their cell

Mixed-effects models for clustered data, penalised regression for sparse events, restricted cubic splines for non-linearity, Fine-Gray for competing risks (with a statistician), multiple imputation for missing data, bootstrap for confidence intervals of accuracy metrics, DeLong for AUC comparison, decision curve analysis for clinical utility, restricted mean survival time when hazards are not proportional. These are not "complicated"; they are the correct tool for a named situation and the map lists when.

## Where the decision is recorded

In `Thinking-space/analysis-plan.md`, under "Methods considered and rejected", one line per method with the reason, and in `log/decisions.jsonl` with `decided_by` set to the human whenever the gate fired. The evidence-checker reads the plan when it verifies the Methods and Results units, so a method that is not in the plan is flagged as new data.
