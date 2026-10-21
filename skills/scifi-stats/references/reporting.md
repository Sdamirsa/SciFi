# Reporting an analysis

What each kind of result must carry so a reader can judge it, in the number format of the standards (`scientific-writing` SKILL.md section 2). The Methods paragraph template is item 7 of `scientific-writing/references/sections/methods.md`.

## The universal set

- The estimate (difference, ratio, AUROC, kappa) with its 95% CI, in one parenthesis after the claim.
- The n per group and the number of events, in the same sentence or in Table 1.
- The test and the p value when a hypothesis was pre-specified; p to three decimals, "p<0.001" below that; never "p = 0.000", never "NS".
- The method of the CI when it is not the model's default (bootstrap with the number of resamples over cases; exact binomial for proportions).
- Whether the analysis was pre-specified or exploratory.
- The software and version.

## By result type

| Result | Report as |
|---|---|
| group comparison, continuous | mean difference 4.2 (95% CI 1.1 to 7.3), p=0.009, Welch t test, n=120 vs 118 |
| group comparison, skewed | median 12 (IQR 8 to 19) vs 9 (6 to 14); Hodges-Lehmann difference 3 (95% CI 1 to 5), Mann-Whitney U, p=0.004 |
| binary outcome | 23 of 120 (19.2%) vs 11 of 118 (9.3%); risk difference 9.9 percentage points (95% CI 1.2 to 18.5), p=0.03 |
| adjusted effect | adjusted OR 1.84 (95% CI 1.21 to 2.80) per 10 units, adjusted for the listed covariates |
| survival | adjusted HR 2.39 (95% CI 1.92 to 2.96), p<0.001; median follow-up 2.9 years; 610 (6.2%) deaths |
| accuracy | 96.3% (95% CI 95.1 to 97.4; 963 of 1,000) vs 88.7% (87.0 to 90.4); difference 7.6 percentage points (5.8 to 9.4) |
| AUROC | 0.91 (95% CI 0.88 to 0.94); comparison with model B: difference 0.05 (0.02 to 0.08), DeLong p=0.002 |
| calibration | intercept 0.03 (95% CI -0.10 to 0.16), slope 0.96 (0.88 to 1.04); plot in Figure X |
| agreement | kappa 0.89 (95% CI 0.86 to 0.92); ICC(2,1) 0.94 (0.91 to 0.96); Bland-Altman bias 0.4, limits -2.1 to 2.9 |
| sample size | the primary outcome, the effect, the assumed SD or rate with its source, alpha, power, the resulting n, attrition allowance |

## Precision

One decimal for percentages, two for AUROC and ratios near 1 (three in tables), three for p. The same number appears identically in the abstract, Results, Discussion and captions. Ranges and intervals use "to".

## Words

"Associated with" for observational data, "difference" or "effect" only for randomised designs. "Significant" only with its test. No "trend towards significance". A confidence interval that includes the null is reported as such, with the interval, not as "no difference".

## The analysis plan template (`Thinking-space/analysis-plan.md`)

```
# Analysis plan: <study short name>
Status: pre-specified | exploratory | mixed    Date: <ISO>    Decided by: <human | both>

## Question
<one sentence per analysis; primary first>

## Data
Outcome(s): <type, how measured, missingness>
Exposure or groups: <type>
Unit of analysis and clustering: <e.g. report within patient within centre>
Sample: <n per group, events, source, period>

## Design and guideline
<design>; reporting guideline: <STROBE | STARD | TRIPOD+AI | CONSORT | GRRAS>

## Methods
Primary: <method from the map>  Assumptions and checks: <list>  Fallback: <from the map>
Secondary: ...
Confounders (pre-specified, with source): ...
Multiplicity: ...   Missing data: ...   Sensitivity analyses: ...

## Methods considered and rejected
<method>: <reason in one line>   (complexity guard fired: yes | no)

## What will be reported
<estimate with CI, test and p, n and events, per analysis>

## Software
<name and version; script path under Thinking-space/analysis/>
```
