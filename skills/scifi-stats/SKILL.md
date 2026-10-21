---
name: scifi-stats
description: >
  Choose and justify the biostatistical method for an analysis, from the question, the
  outcome and exposure types, the study design and the sample, favouring the simplest
  standard method whose assumptions hold and blocking bespoke methods that would be valid
  only in this paper. Use when the user says "which test should I use", "how do I analyse
  this", "write the statistical analysis plan", "compare these two groups", "is this the
  right model", "sample size", "do I need a mixed model", "/scifi-stats", or asks to run or
  plan a statistical analysis. Do not use for writing or reviewing text that merely reports
  statistics (that is scientific-writing and the paragraph loop) or for figure design.
argument-hint: "[question] [--data <file>] [--plan]"
allowed-tools: Read, Write, Glob, Grep, Bash(python3 *), AskUserQuestion, Agent
---

# scifi-stats

A method is chosen by the question and the data, not by what sounds impressive. The
pattern to avoid is a model built for this one dataset, with a custom metric and a custom
correction, that no reviewer can check against a textbook. The rule is the opposite: the
simplest standard method that answers the question with its assumptions met, reported with
an effect size and a confidence interval.

## Procedure

1. **State the question in one sentence** and classify it (one of): describe; compare groups;
   measure association or effect; predict or discriminate; measure agreement; time to event;
   change over time or repeated measures; dose or trend. If the user's question mixes two,
   split them into two analyses.
2. **Classify the data.** Outcome type (binary, nominal, ordinal, continuous near-normal,
   continuous skewed, count, time-to-event with censoring, proportion). Exposure or group
   type. Unit of analysis and any clustering (patients within centres, scans within
   patients, raters within cases, repeated visits). Paired or independent. Sample size per
   group and number of events. Missing data and how it arose.
3. **Classify the design.** Randomised or observational; cross-sectional, cohort, case
   control, diagnostic accuracy, model development with internal or external validation,
   reader study, agreement study. Name the reporting guideline the design falls under
   (CONSORT, STROBE, STARD, TRIPOD+AI, GRRAS, QUADAS).
4. **Read `references/method-map.md`** and pick the standard method for that cell. Write
   down the assumptions it needs and how each will be checked (distribution, independence,
   proportional hazards, linearity, event count per predictor). If an assumption fails, take
   the map's listed fallback, not an invented one.
5. **Apply the complexity guard** (`references/complexity-guard.md`). A method passes when
   it is in the map or in a named reporting guideline, textbook or two papers in the target
   journal family. Anything else (a new metric, a custom weighting, a correction chosen
   after seeing the data, a model with more parameters than the events support) needs a
   written justification and a human gate, in every mode, and the simpler alternative is
   reported alongside it.
6. **Decide what is reported**, from `references/reporting.md`: the estimate, its 95% CI,
   the test and p value where a test is appropriate, the n per group, the handling of
   multiplicity and missing data, the sensitivity analyses. Numbers follow the standards
   (`scientific-writing` section 2).
7. **Write the plan** to `Thinking-space/analysis-plan.md` using the template at the end of
   `references/reporting.md`: question, data, design, method with assumptions and checks,
   fallbacks, what is reported, software, and the pre-specified versus exploratory split.
   Then draft the Statistical analysis paragraph for Methods from it (the paragraph template
   is in `scientific-writing/references/sections/methods.md`, item 7).
8. **Only then run anything.** If data are present, run the assumption checks first, then
   the analysis, with a script saved under `Thinking-space/analysis/` so the numbers are
   reproducible. Report the output as it is; a null result is a result.

## Gates and the human

- Co-thinker mode: present the chosen method and one alternative with the trade-off before
  writing the plan. Human-on-the-loop: write the plan, then confirm. Fully-automated: the
  complexity guard still stops at any non-standard method.
- Ask the user, not the data, about the clinical question, the unit of analysis, and
  whether the analysis was pre-specified; those three answers decide more than any test.
- Invite `panel-discussion` only for a real methodological fork (for example, time-to-event
  versus binary outcome at a fixed horizon), not for routine choices.
- When the study needs a statistician (sample size for a trial, competing risks, complex
  survey weights, causal inference with time-varying confounding, Bayesian design), say so
  and stop at the plan.

## What this skill refuses

- To pick a method because it gives a smaller p value.
- To invent a composite metric, a weighting or a threshold without a cited precedent.
- To report a p value without the estimate and its CI, or "significant" without the test.
- To run a model with fewer than about ten events per candidate predictor without saying
  the estimates are unstable and offering penalisation or a smaller model.
- To treat clustered or repeated observations as independent.
