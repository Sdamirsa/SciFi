# Paper

Yi J, et al, Slomka PJ. Six-tissue body composition from CTAC for mortality prediction. The Lancet Digital Health 2025;7(5):100862. Original research (retrospective multicentre prognostic study). Source: the medRxiv preprint (v1 HTML full text and PDF, 10.1101/2024.07.30.24311224). The published version could not be read: thelancet.com returned fetch errors, ScienceDirect blocks robots, PMC12190801 served a captcha, and Europe PMC was rate limited. Table bodies are images in the preprint and could not be read, and the figure image files returned server errors. The table notes below therefore rely on titles, Methods statements and the prose.

# Figures

Five main figures, plus at least five supplementary figures (S1 to S5).

| No. | Type | Panels | Purpose |
|---|---|---|---|
| 1 | Study design schematic: CTAC scan, then AI segmentation of six tissues, then mortality prediction | 1 | Orientation |
| 2 | Study flowchart (inclusion and exclusion) | 1 | Cohort derivation |
| 3 | Kaplan-Meier curves, one per tissue, at a high attenuation or high volume index cutoff | 6 (A to F) | Main result |
| 4 | Example segmentation, male patient (BMI given) | 1 | Worked example |
| 5 | Example segmentation, female patient (BMI given) | 1 | Worked example |

- **Figure 1** is a study design overview showing the pipeline from input to endpoint. It is cited in Methods ("Figure 1 summarizes the study design"), not in the Introduction.
- **Figure 2** is a STROBE-style flowchart. The n at each exclusion step sits on the figure itself, and Results cites it in parentheses after the cohort sentence.
- **Figure 3** carries the main result. Each panel corresponds to one tissue (EAT, IMAT, VAT, SAT, bone, skeletal muscle), and its threshold is stated in the caption (for example VAT above minus 80 HU). The caption says unadjusted and adjusted HRs appear on the panels, so the effect sizes with CIs are printed on the plot. Numbers at risk and log-rank p could not be verified.
- **Figures 4 and 5** are paired example cases, with the patient's sex and BMI in the caption. They come last, even though they illustrate the method, and Results cites them as a pair ("Figures 4 and 5 show...").
- **Panel referencing.** The text never cites individual panels. It refers only to "Figure 3", and the A to F letters appear only in the caption.
- **Colour encoding** could not be verified. The design suggests two curves per panel (high vs low, with low as the reference).
- **Supplementary figures** hold the following: segmentation pipeline details and threshold derivation (S1, S2, cited in Methods), and KM stratification by cardiac variables such as perfusion and CAC (S3 to S5, cited in Results). Robustness and stratified analyses go to the supplement.

# Tables

Two main tables and twelve supplementary tables.

- **Table 1**, "Baseline characteristics for all participants stratified by sex", is placed in the first Results subsection. Per Methods, continuous variables are given as median (IQR) and categorical ones as n (%). There is a p value column, with tests chosen by variable type (Wilcoxon rank sum, chi-squared, Fisher's exact). Columns are probably overall, male, female and p, and the rows mix clinical factors with body composition measures. Stratifying by sex rather than by outcome is a choice tied to a finding: sex differences in tissue measures are reported in the prose.
- **Table 2**, "Comparison between unadjusted and adjusted hazard ratios", has tissues and measures as rows and unadjusted vs adjusted HR as columns. Its title carries a methodological note: lower values serve as the reference. The prose quotes HRs in the form "HR 2.39 [1.92, 2.96], p<0.0001", so the cells probably use the same layout, with square-bracket CIs and p values mixing exact values and "<0.0001". The extended version is Supplementary Table 6.
- **Supplementary tables**: baseline characteristics stratified by each tissue cutoff (S1 to S4), Youden cutoffs (S5), extended HRs (S6), and subgroup analyses by sex, race, age and BMI (S7 to S12).
- **Prose overlap.** About six Results sentences restate table values: cohort size, sex split, age and deaths from Table 1, and the three headline adjusted HRs from Table 2. The rest of each table is only pointed to.
- Neither table shows bold for best values, which is expected because nothing is being ranked.

# Captions

- **Structure.** Each caption opens with a short descriptive label as its title ("Study flowchart", "Study design"), sometimes followed by a description. Figure 1 adds one descriptive sentence and an abbreviation definition. Figure 2's legend is only an abbreviation list. Figure 3's caption gives the per-panel cutoffs and states what the HRs are adjusted for (11 clinical and imaging variables plus 18 other body composition measures).
- **Length.** Figures 4 and 5 run about 10 to 15 words, and Figure 3 about 80 to 100. Most captions are under 30 words.
- **Tone.** Descriptive labels throughout, never claims. Example titles: "Study flowchart"; "Kaplan-Meier curves stratified by body composition measures"; "Example of body composition segmentation".
- **Content.** Captions define abbreviations again, even ones defined in the text (CTAC, EAT, SPECT). Figure 3's caption adds the panel-by-panel thresholds and the adjustment set. No caption names a statistical test, says what error bars mean, or tells the reader what to notice.
- **Stand-alone.** Figure 3 nearly stands alone because the cutoffs and adjustment are stated. Figures 1, 2, 4 and 5 rely on the image.
- **Table titles vs figure captions.** Table titles are a single descriptive phrase, and the Table 2 title adds one methods sentence about the reference category. Figure captions carry more definitions.

# Order and organisation

Approximate main text: 2850 words.

| Section | Words | Share |
|---|---|---|
| Summary (structured: Background, Methods, Findings, Interpretation, Funding) | 280 | (separate) |
| Research in context panel | 390 | (separate) |
| Introduction (4 paragraphs) | 350 | 12% |
| Methods: Study population; CTAC acquisition; Clinical data and risk factors; Segmentation and quantification; Statistical analysis; Role of funding source | 1000 | 35% |
| Results: Study population; Predictors in entire group; Predictors in subgroups | 650 | 23% |
| Discussion (6 paragraphs) | 840 | 30% |

- **Methods sit before Results**, Lancet style, so Results does not re-explain the method. The segmentation subsection is the longest Methods block (about 450 words) and holds Figure 1.
- **Results order**: cohort and baseline (Figure 2, Table 1), then the main prognostic effect in the whole cohort (Figure 3, Table 2, examples in Figures 4 and 5), then subgroups (supplementary tables only). Subsection headings are labels, not claims.
- **Distribution.** Figures and tables cluster in the first two Results subsections. The subgroup subsection has no main display item and points only to S7 to S12.
- **Discussion sequence**: principal findings; clinical relevance of body composition phenotypes and the limits of BMI; comparison with prior work and the novelty claim; mechanistic reading of key predictors (EAT, attenuation, VAT across subgroups); limitations as one paragraph of about 170 words; a conclusion paragraph. The Discussion cites no figures or supplementary items.
- **Supplement pointers** are frequent (over 12) and plain, in parentheses: "(Supplementary Table 5)", "Supplementary Table 6 (extended information)", "Supplementary Figures 3-5". There is no "see" phrasing, and ranges are used for runs of tables.
- **Research in context panel**, with three subheadings: Evidence before this study (the search databases, the search date and 34 hits, then the gap: three or fewer tissues, never from CTAC); Added value of this study (an annotation-free six-tissue method with independent prognostic value); Implications of all the available evidence (routine point-of-care use, at no extra radiation). The Evidence section is the longest (about 200 words).
- **Ease of reading.** The three-part Results are easy to follow, and putting the main result in one six-panel figure works well. Two things hurt: the example segmentations are placed after the KM curves, and the subgroup results have no main display item, which forces about 250 words of chained HRs. The adjustment set is given as 11 variables in Methods but 10 in subgroups.

# Checklist candidates

- Make Figure 1 a single-panel study design schematic, from input scan through AI step to clinical endpoint, and cite it in Methods. [strong]
- Make Figure 2 a cohort flowchart with n at each exclusion step on the figure, and cite it from the first Results sentence. [strong]
- Put the headline prognostic result in one multipanel figure with one panel per exposure and the same layout across panels. [strong]
- Print unadjusted and adjusted HRs with 95% CIs on each KM panel, and state the adjustment set in the caption. [strong]
- State each panel's cutoff or definition in the caption, so the figure stands alone. [strong]
- Use a short descriptive label as the caption title, not a claim. [strong]
- Define every abbreviation again in each caption, even if it is defined in the text. [strong]
- Make Table 1 the baseline characteristics table, stratified by the variable the paper reports differences on, with median (IQR), n (%) and a p value column; name the tests in Methods. [strong]
- Give the main effect-size table an extended twin in the supplement, and say so in the text. [weak]
- If a table reports HRs, state the reference category in the table title or a footnote. [strong]
- In Results, restate only the headline values from a table (cohort size, events, two or three key HRs), and point to the table for the rest. [strong]
- Use a single Limitations paragraph near the end of the Discussion, followed by a short conclusion paragraph. [strong]
- In the Research in context panel, give the search databases, the search date and the number of hits, then state the gap as a count of what prior work lacked. [strong]
- Put worked example cases next to the method, or early in Results, not after the main result figure. [weak]
- Give subgroup analyses at least a forest plot in the main text, rather than only prose plus supplementary tables. [weak]

# Notable deviations

- Methods holds Figure 1, so the reader meets the pipeline before Results. This is unusual for a figure numbered first in Lancet papers, but logical here.
- Two of five main figures are single-patient segmentation examples. That is a high share of display space for illustration rather than evidence.
- In the preprint, the p value format mixes exact values with "<0.0001", and CIs sit in square brackets with commas. Lancet copyediting probably changed this to parentheses with "to".
- The adjustment count differs between Methods (11) and the subgroup Results (10).
