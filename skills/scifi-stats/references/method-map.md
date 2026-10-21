# Method map

The standard method for each question and data type, its assumptions, and the fallback when an assumption fails. Every entry is textbook material (Altman, Practical Statistics for Medical Research; Kirkwood and Sterne, Essential Medical Statistics; Harrell, Regression Modeling Strategies; Steyerberg, Clinical Prediction Models; Pepe, The Statistical Evaluation of Medical Tests) or a reporting guideline. If the needed cell is not here, the method needs the complexity guard.

## 1. Describe

| Data | Report | Notes |
|---|---|---|
| continuous, near-normal | mean (SD) | say which summary and why in Methods |
| continuous, skewed | median (IQR as 25th to 75th) | never mean (SD) for skewed data |
| binary or nominal | n (%) | denominators stated when they vary |
| ordinal | median (IQR) or n (%) per level | not mean |
| time-to-event | median follow-up (reverse Kaplan-Meier), events n (%) | |
| Table 1 | the above by the stratification the paper reports on | a p value column is optional and often discouraged for randomised trials |

## 2. Compare groups (one outcome, one grouping)

| Outcome | 2 independent groups | more than 2 independent | paired or matched | Assumptions and fallbacks |
|---|---|---|---|---|
| continuous near-normal | Welch t test (do not assume equal variances) | one-way ANOVA, then pairwise with Holm or Tukey | paired t test | normality of residuals at small n; fallback Mann-Whitney / Kruskal-Wallis / Wilcoxon signed-rank, or a permutation test |
| continuous skewed, ordinal | Mann-Whitney U | Kruskal-Wallis, then Dunn with Holm | Wilcoxon signed-rank | report medians and a Hodges-Lehmann difference with CI, not only p |
| binary | chi-square, Fisher exact when any expected cell < 5 | chi-square | McNemar | report risk difference or ratio with CI |
| count | Poisson or negative binomial regression | same | conditional Poisson | overdispersion decides Poisson versus negative binomial |
| time-to-event | log-rank test, Kaplan-Meier curves | log-rank | stratified log-rank | proportional hazards checked (Schoenfeld); crossing curves need a restricted mean survival time comparison |
| accuracy or AUC of two methods on the same cases | DeLong test for AUC; McNemar for accuracy | | | bootstrap CI for the difference; the two methods must be evaluated on the same cases |

Effect size always: mean difference, median difference, risk difference, risk ratio, odds ratio, hazard ratio, AUC difference, each with a 95% CI. A test without an effect size is incomplete.

## 3. Association or adjusted effect

| Outcome | Model | Report | Assumptions, limits |
|---|---|---|---|
| continuous | linear regression | coefficient (95% CI) per unit | linearity (restricted cubic splines when not), residual normality at small n, homoscedasticity |
| binary | logistic regression | odds ratio (95% CI) | at least about 10 events per candidate predictor; otherwise penalised (ridge, lasso) and say so |
| ordinal | proportional-odds logistic | common OR (95% CI) | proportional odds checked; fallback multinomial |
| count | Poisson or negative binomial | rate ratio (95% CI) | overdispersion; offset for exposure time |
| time-to-event | Cox proportional hazards | hazard ratio (95% CI) | proportional hazards; competing risks need Fine-Gray or cause-specific hazards and a statistician's input |
| clustered or repeated | mixed-effects model (random intercept for the cluster) or GEE | as above with the cluster named | never ignore clustering; choose mixed model for subject-level inference, GEE for population-average |
| matched case-control | conditional logistic regression | OR (95% CI) | |

Confounders are chosen from prior knowledge (a causal diagram or a cited list), fixed before the analysis, never by stepwise selection on p values. Interaction terms only when pre-specified.

## 4. Predict, discriminate, diagnose

| Task | Standard set | Notes |
|---|---|---|
| diagnostic accuracy of a test or model against a reference standard | sensitivity, specificity, PPV, NPV with exact binomial 95% CI; AUROC with DeLong or bootstrap CI; 2 by 2 table shown | STARD; threshold pre-specified or shown across the range |
| prediction model development and validation | AUROC (discrimination), calibration plot with intercept and slope, Brier score, decision curve (net benefit); internal validation by bootstrap or cross-validation; external validation on another site or period | TRIPOD+AI; events per predictor; no "external validation" for a random split |
| classifier comparison (AI models) | per-class accuracy, sensitivity, specificity and F1 only as secondary; AUROC when scores exist; CI by bootstrap over cases (not over runs); paired comparison on the same cases | mean ± SD over runs is a reproducibility statement, not a sampling uncertainty |
| information extraction (LLM labelling) | accuracy, per-category sensitivity and PPV with CI; agreement with the reference standard (kappa) | report the reference standard's own agreement |
| calibration of probabilities | calibration plot, intercept, slope; expected calibration error only alongside the plot | |

## 5. Agreement and reliability

| Data | Method | Notes |
|---|---|---|
| categorical, 2 raters | Cohen's kappa (95% CI); prevalence-adjusted when prevalence is extreme | |
| categorical, more than 2 raters | Fleiss kappa or Krippendorff alpha | |
| continuous | intraclass correlation (model stated: ICC(2,1) or similar) and Bland-Altman with limits of agreement | correlation is not agreement |
| method comparison | Bland-Altman | |

## 6. Change over time, repeated measures

| Design | Method | Notes |
|---|---|---|
| before and after, one group | paired test or mixed model | regression to the mean acknowledged |
| two groups over time | mixed model with time, group and interaction; or ANCOVA on follow-up adjusted for baseline | ANCOVA preferred for two time points in a randomised design |
| many time points | mixed model with random slopes if supported | |

## 7. Sample size and power

State the primary outcome, the effect worth detecting (clinically, with a citation), the SD or event rate assumed (with a citation), alpha 0.05 two-sided, power 80 or 90 percent, and the software. For a retrospective study with a fixed sample, report the sample as fixed and give the minimal detectable effect instead of a post hoc power. For prediction models use the Riley criteria (events per parameter, shrinkage) rather than a rule of thumb.

## 8. Multiplicity and missing data

- Pre-specified primary outcome, one test. Secondary outcomes labelled as such; a correction (Holm, Benjamini-Hochberg) when a family of tests supports one claim.
- Missing data: report the amount per variable, the plausible mechanism, and the method (complete case when small and plausibly random; multiple imputation otherwise, with the imputation model stated); a sensitivity analysis under a different assumption.

## 9. What is out of scope here and needs a statistician

Competing risks, interval censoring, causal inference with time-varying treatment, instrumental variables, adaptive trial design, Bayesian hierarchical models, survey weights, meta-analysis with network structure, measurement error correction.
