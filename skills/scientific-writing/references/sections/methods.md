# Methods

## Subsection order

Use subheadings. A Methods section without them (one corpus review has 1,200 words with none) is the hardest section to navigate. The order below follows the data flow; mirror it in Results.

1. **Study design and ethics.** Design in one sentence (retrospective multicentre cohort, cross-sectional model comparison, randomised blinded reader study, benchmark construction). Ethics approval with committee name and number, consent or its waiver with the reason, Declaration of Helsinki for human data, the data use agreement for controlled data. This is the first paragraph; every strong corpus paper puts it here. Then the reporting guideline followed, with its checklist cited and supplied as a supplement. Lancet asks for the trial or study registration here if any.
2. **Data source and population.** Sites, period, inclusion and exclusion criteria (point to the flow figure), what was excluded from the text (for example the impression section of a report), how development, validation and test sets were formed and whether they differ in period or site. State the split sizes with n. Name "external validation" only for data from a different site or period; a random split of one pool is internal validation.
3. **Reference standard or ground truth.** Who labelled, how many labellers, their qualification, independence, the consensus procedure, the label set, and the agreement statistic with CI. If an LLM produced labels, describe the human validation of a sample.
4. **Intervention, model or pipeline.** For AI models: architecture, base model with exact version string (gpt-4-0613, Llama 3.1 70B), parameter count, quantisation, decoding temperature, max tokens, seeds, number of runs, hardware, software and library versions. Prompts verbatim in the supplement (or in a box if short), with one line of anatomy here (system, user, assistant roles). Justify the model choice in one sentence. For imaging: acquisition parameters, segmentation method, thresholds in HU.
5. **Outcomes and metrics.** Define each metric operationally with numerator and denominator, the unit of analysis, tie rules, and any recoding (an ordinal recoding for MSE). Name the primary metric. Clinical outcomes: definition, ascertainment, follow-up.
6. **Evaluation design.** Comparators, baselines, ablations, subgroup definitions, sensitivity analyses, the human or clinician evaluation (number of raters, cases, blinding, rating scale, interface).
7. **Statistical analysis.** One paragraph, 100 to 200 words: summary statistics by variable type (median with IQR, n with %), tests by variable type, the model (Cox, logistic), adjustment set, how CIs were obtained (bootstrap with the number of resamples, exact binomial), multiple comparison correction, sidedness, alpha, missing data handling, sample size rationale or a statement that none was made, software with version. Nature-portfolio journals require a "Statistics and reproducibility" paragraph covering sample size, exclusions, randomisation, blinding and replicates; write it even where the answer is "none".
8. **Role of the funding source.** Last Methods subsection in Lancet journals: "The funder had no role in study design, data collection, analysis, interpretation or writing."

## Voice and tense

Past tense throughout for what was done. Passive is normal for procedures ("Reports were labelled", "Images were segmented"); "we" for design decisions ("We chose a random forest because..."). Present tense only for how a system works when describing an architecture ("The agent has two roles").

## Level of detail

Enough for replication by someone with the same data. A quick test: could another group rerun the primary analysis from this section plus the supplement without emailing you. The corpus papers that pass this test report model versions, temperature, prompts, annotator process, search query with date window and counts at each step. Those that fail omit the version string, the dispersion behind "±", or how ties were resolved.

Push to the supplement: full prompts, hyperparameter tables, feature definitions, rater instruments, extended cohort tables. Keep in the main text: everything in the eight subsections above at summary level.

## Sentence habits

Methods is where the corpus produces its longest sentences (60 to 97 words, chained with semicolons, nested brackets of covariates). Replace each with a sentence per step or with a numbered list. Covariate lists longer than four items go in a table or a parenthesis after "adjusted for 11 variables (listed in Supplementary Table 2)".

Open a subsection that reports a sub-study with a purpose clause: "To assess whether..., we...". Define the condition before the procedure.

## Statements that are easy to forget

- Consent or its waiver, even for de-identified public data (state the data use agreement and PhysioNet training for MIMIC).
- The date of any literature or database query, and the date of citation counts.
- How proprietary model refusals or invalid outputs were handled and counted.
- The time window separating development and test data.
- Whether raters were blinded to the source of the output.
- What was not done: no risk of bias assessment, no sample size calculation, no segmentation accuracy evaluation, with the reason.

## In a review

- Narrative review or perspective: a paragraph stating the scope, the inclusion and exclusion of topics, how sources were identified, the cut-off date, and an explicit statement that the search was not systematic. Place it at the start of the evidence section if there is no Methods heading.
- Guidance paper with a worked example: a short dedicated section introducing the case study (clinical question, model, development and validation data with n and prevalence, CI method, code and data location) before the first section that uses it.
- Systematic review: registration and reporting checklist first; eligibility with a bulleted exclusion list; search with databases, fields and date, with the full string in Table 1 or the supplement; screening procedure (number of reviewers, tool, calibration sample, agreement); data charting form as a bulleted list; synthesis method; disclosure of any AI tool used and for which step; a statement of what was not done (for example risk of bias).
