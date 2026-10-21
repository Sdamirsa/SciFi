# Results

## Order of subsections

1. **Data or cohort description.** First Results sentence gives the n with the flow figure in parentheses, then the key characteristics with Table 1 ("Baseline characteristics are given in Table 1"). For a benchmark or LLM study, open with a data quality check (format compliance, invalid output rate, number of items after filtering) before any performance number.
2. **Primary analysis.** The headline comparison, with its figure and table.
3. **Secondary analyses.** Other metrics, other datasets, moderators (model size, class imbalance), efficiency (runtime, seconds per case).
4. **Subgroups, robustness, ablations, sensitivity.** Point to supplementary tables; give a forest plot or a single summary table in the main text rather than 250 words of chained hazard ratios.
5. **Human or clinician evaluation.** Open with the sample (number of cases, number and specialty of raters), then one paragraph per rating axis.
6. **Error analysis.** A named failure taxonomy with counts per type and a table of examples. The corpus papers that did this (two) gained the most from it.

For multi-study papers (Study 1, Study 2a, Study 2b, Study 3) tag each subheading with the study and keep the same tags in Figure 1, Methods and captions.

## Subheadings

- Balanced default: descriptive labels naming the analysis ("Prognostic value of individual tissues", "Specialty referral accuracy"). Each label matches a Methods subheading.
- Nature-portfolio option: a claim sentence that states the finding ("Tool use and retrieval improve LLM responses"). Use claims only where the finding is unambiguous; use labels for mixed results. Questions as headings ("Does the patient model affect accuracy?") are acceptable for ablations that answer one question each.

## The paragraph template

1. Open by naming what was measured and the display item: "Figure 3 shows the adjusted hazard ratios for the six tissue measures." When Methods comes last, add one sentence restating the condition, metric or n before the numbers.
2. State the headline value with its uncertainty: "High epicardial fat volume was associated with higher all-cause mortality (adjusted HR 2.39, 95% CI 1.92 to 2.96, p<0.0001)."
3. State the comparison in one sentence with both values side by side: "Accuracy was 87.2% (95/109) with tools versus 30.3% (33/109) without." Keep model or group order fixed throughout the paper; "respectively" may map an ordered list of values onto an ordered list of models once per paragraph.
4. Report secondary values or the exception plainly ("The one dataset where the explicit probability was better was...").
5. Close with at most one sentence stating what the numbers mean in descriptive terms. No mechanism, no implication, no "this crucial finding". Nature-portfolio permits an "In summary" verdict sentence per subsection; nowhere else.

Keep Results paragraphs 60 to 130 words; they are the shortest in the paper.

## Numbers in prose versus display items

- Restate in prose only the headline values (cohort size, events, two or three key effects, the primary comparison). Point to the table for the rest.
- Never let a long prose list be the only source of numbers (11 models by 3 metrics is a table).
- Never name a column or a statistic that the table does not contain.
- Use the same source of truth for every number; copy from the final table, not from an earlier draft.

## Verbs and hedges

- Verbs: was, were, had, showed, increased, decreased, was associated with, was higher than, outperformed (only with a test), did not differ.
- Avoid in Results: suggest, indicate, demonstrate, confirm, may, could, likely, interestingly, notably, surprisingly, strikingly, superior, exceptional, crucial.
- Association language for observational data ("was associated with higher mortality"), not "increased death risk".
- "Significant" only beside its p value or CI.

## Display items in Results

- Every paragraph points to at least one figure or table, by panel where a panel is discussed ("Figure 2b").
- Figures are cited in numerical order.
- A worked example (one patient, one case traced end to end) sits next to the method it illustrates, early in Results or in Methods, not after the main result.

## In a review

- A narrative review has no Results; the evidence section plays the role. Each subsection reports counts ("of 50 models, 27 were trained on...") with the figure panel that shows them and closes with a one sentence verdict against the framework.
- A systematic review opens Results with the PRISMA flow and its counts, then one paragraph per figure in the order of the figures, no subheadings or short labels, past tense for findings, present for "Figure 4 shows", counts as "n (%)", means as "mean (SD)", no "we", no "outperformed".
- A guidance paper reports each item in the same micro-structure: definition, interpretation, critique against the criteria, worked value with CI, verdict in one short sentence.
