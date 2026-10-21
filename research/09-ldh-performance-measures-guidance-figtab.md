# Paper
Van Calster B, Collins GS, Vickers AJ, et al. (STRATOS TG6), Lancet Digit Health 2025;7:100916. Methodological guidance review with a worked case study. Source: arXiv preprint full text (https://arxiv.org/html/2412.10288); the published version may relabel Box 1 as a Lancet "Panel" and drop section numbers.

# Figures
- **Count:** 4 main figures and at least 6 supplementary figures (S1 to S7, with S1 showing calibration by menopausal status and S3 to S7 showing the recalibrated model). All figures come from the case study (the ADNEX ovarian cancer model, external validation). None is conceptual.
- **Figure 1 (worked example, discrimination, 3 panels):** A is an ROC curve, B a precision-recall curve, C a partial AUROC plot. There is no study overview figure. Figure 1 is simply the first measure discussed (discrimination), so figure order follows the order of the argument, not the order of importance.
- **Figure 2 (worked example, calibration, 1 panel):** Calibration plot with decile groups and a loess curve against the diagonal.
- **Figure 3 (worked example, overall performance, 1 panel):** Violin and dot plots of predicted risk split by outcome.
- **Figure 4 (worked example, clinical utility, 3 panels):** A net benefit decision curve, B standardised net benefit, C cost curve. It has "All" and "None" reference strategies.
- **Role:** Every figure is a worked example illustrating a class of measure. The taxonomy and the recommendations go in tables. Figures teach how to read a plot. They do not report a headline finding.
- **Numbers on figures:** The values seem to be in Table 3 and the prose, not on the plots. The extract had no images to confirm this.
- **Panel labels:** Capital letters. The text cites "Figure 1A" and "Figure 4C". Captions use both "(panel A)" and "(A)".
- **Encoding:** No colour legend is described. The reference lines (diagonal, treat all, treat none) carry the meaning.
- **Supplementary:** It holds subgroup plots, the recalibrated model's plots, formulas and theory. The main text shows one model state (before recalibration), and Section 7 only points to the "after" figures in the supplement.

# Tables
- **Count and position:** 4 tables, placed at the end in the preprint. Table 1 and Table 2 are first cited in Section 3, Table 3 in Section 5.1, Table 4 in Section 8 (Discussion).
- **Table 1 (taxonomy):** Five domains as rows, grouped under two header rows (probability based, threshold dependent). Columns give the target question and a one-word focus. Text only. In a guidance paper, Table 1 is the conceptual framework, not baseline characteristics.
- **Table 2 (assessment matrix):** 32 measures as rows, grouped by domain. Columns hold two criteria plus a verdict. Cells use symbols (++, +, minus) and Yes/No. A # footnote qualifies one class of measures. The Yes rows add up to the abstract's headline count of 17.
- **Table 3 (case study results):** Measures as rows, grouped by domain. There are two columns, before and after recalibration. Most values have 3 decimals and the 95% CI in parentheses, as estimate (lower, upper). DOR has 1 decimal and loglikelihood is an integer. Footnotes a and b give methodological caveats (CIs for net benefit; the threshold that minimises EC). There is no bold. The extract shows probable errors: one estimate lies outside its CI and one interval is reversed.
- **Table 4 (recommendation summary):** Rows are measures or plots grouped by domain. Columns are measure, a categorical guidance label (Recommended, Inadvisable, and two hedged middle grades) and a short comment. An abbreviation footnote makes it work as a glossary.
- **Prose vs table:** In Sections 5 and 6, key numbers are repeated in prose with CIs, rounded to 2 decimals, and then "(Table 3)" is cited. Section 7 only points to the table. The prose rounds more coarsely than the table.

# Captions
- **Structure:** A title phrase, with no separate bold title sentence in the extract. Figures 1 to 3 have one sentence. Figure 4 runs to a paragraph that adds reading instructions.
- **Length:** Table titles have 3 to 14 words (typically about 10). Figure captions have 15 to about 115 words (typically about 20 to 30). Figure 4 is the outlier.
- **Tone:** Descriptive labels throughout. Captions make no claims. Even Table 4 is framed as "guidance and final comments", not as a verdict.
- **Content:** Panel mapping in the caption (panel A, B, C). There are method details (10 equal-sized groups, loess, central moving averages), the analytic assumption (sensitivity below 0.8 treated as unacceptable), and a pointer to Box 1 for the reasonable threshold range. The captions do not give error bars, n or data source.
- **Abbreviations:** Defined in table footers (Table 4), not in figure captions. ADNEX, EC and "cq." go unexpanded in the captions, so the captions do not fully stand alone.
- **Tables vs figures:** Table titles are short nouns and the detail goes into footnotes. Figure captions carry the method and how to read the plot.
- **Examples:** "Five performance domains." / "Calibration plot for the ADNEX model using 10 groups" / "Performance measures for the ADNEX model before and after recalibration."

# Order and organisation
| Section | ~Words | Share |
|---|---|---|
| Abstract | 230 | n/a |
| 1 Introduction | 520 | 8% |
| 2 Case study | 190 | 3% |
| 3 Taxonomy of five domains (+ Box 1, ~430) | 950 | 14% |
| 4 Key characteristics of a measure | 370 | 5% |
| 5 Probability-based evaluation (5.1 discrimination; 5.2 calibration, 4 levels; 5.3 overall) | 2300 | 34% |
| 6 Threshold-dependent evaluation (6.1 classification; 6.2 clinical utility) | 1250 | 19% |
| 7 Results after recalibration | 230 | 3% |
| 8 Discussion | 850 | 13% |
Back matter: contributors, data sharing, COI, acknowledgments, 148 references.

- **No IMRaD:** The skeleton is framework first (Sections 3 and 4 define domains and criteria), then one section per domain applying the criteria, with a short running case study inside each. The case study is introduced early in a short dedicated section, so later sections never have to re-explain the data.
- **Within each domain subsection:** The recurring sequence is define the measure, judge it against the two criteria, then report the case-study value with a figure. Headings are numbered labels, not claims. Calibration is nested in four levels of increasing stringency.
- **Figure distribution:** One figure per domain subsection (5.1, 5.2.3, 5.3, 6.2). Classification has none in the main text. Table 3 feeds all of Sections 5 to 7.
- **Discussion sequence:** summary of counts (32 measures, 17 pass); core recommendation (discrimination, calibration, utility); core measures and when calibration matters most; a challenge to a common belief (class imbalance, AUPRC, F1); further topics (sample size, heterogeneity, reporting); limitations and scope; a one-line conclusion restating the two criteria. Table 4 is introduced here, so the Discussion doubles as a recommendation summary.
- **Supplementary pointers:** About 12. They are parenthetical and terse, e.g. "(Table S1-S2 for details and formulas)" or "Supplementary Appendix 1 provides an illustration." Formulas and theory are all pushed out.
- **Boxes:** One box, Box 1 on defining a decision threshold. It covers the medical vs statistical rationale, the four outcomes, and the case-study threshold range (5 to 40%). Figure 4's caption cites it. No key points or graphical abstract appear in the preprint. Lancet journals add a "Research in context" panel for research articles but not for reviews.
- **Ease:** Easy to navigate because every domain section has the same shape and one table (Table 2) maps the whole argument. Harder: abbreviations go undefined in captions, there is a typo "Figure 52", and Table 3 has numerical inconsistencies.

# Checklist candidates
- In a guidance or methods review, make Table 1 the conceptual taxonomy, not data. [strong]
- Provide one matrix table that scores every item against the stated criteria, and make its tally match the abstract's headline number. [strong]
- End a guidance paper with a recommendation table that uses a small set of categorical labels plus a one-line rationale per row, introduced in the Discussion. [strong]
- Run one real-data case study through the whole paper. Introduce it in its own short section before the first use. [strong]
- Give each conceptual subsection the same internal order: definition, assessment against criteria, worked value, figure. [strong]
- Use numbered label headings in a review; save claims for the text. [weak]
- Report results as estimate (lower, upper) with consistent decimals per measure. Check that every estimate lies inside its CI. [strong]
- In prose, give rounded key values with the CI and cite the table; leave the full precision to the table. [strong]
- Keep caption titles descriptive. Put plot-reading instructions and analytic assumptions (cut-offs, smoother, grouping) in the caption. [strong]
- Expand every abbreviation in each caption or table footer, including model names. [strong]
- Label panels A, B, C and cite them as "Figure 1A" in the text. [weak]
- Push formulas, theoretical relations, subgroup plots and repeated analyses (for example after recalibration) to the supplement with short parenthetical pointers. [strong]
- Use a box for one self-contained decision concept that several sections and a caption refer back to. [weak]
- Add reference strategies or lines (diagonal, treat all, treat none) to evaluation plots so the reader can judge them without colour. [weak]

# Notable deviations
- No study overview or conceptual figure. Figure 1 is just the first worked plot, unlike the typical clinical-AI Figure 1.
- Tables, not figures, carry the paper's main contribution (Tables 2 and 4).
- A Discussion introduces a new table (Table 4) and that table is the main deliverable.
- Main-text figures show only the pre-recalibration model. Section 7 reports the comparison mainly through Table 3 and the supplementary figures.
- Figure 4's caption (about 115 words) is roughly four times the length of the others, because it doubles as a reading guide.
- Errors that survived review: "Figure 52" (which should be S2), a reversed CI and an estimate outside its CI in Table 3, and an unexpanded "cq." in a caption.
