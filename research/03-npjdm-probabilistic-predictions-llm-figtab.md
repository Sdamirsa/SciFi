# Paper

Gu B, Desai RJ, Lin KJ, Yang J. Probabilistic medical predictions of large language models. npj Digit Med 2024;7:367; original research (computational benchmarking); source: arXiv preprint 2408.11316 (Nature page and PMC unreachable), so typeset layout, panel art and colours could not be inspected directly.

# Figures

Three main figures, sixteen supplementary figures. The figure art itself was not visible; findings below rest on captions, legends and in-text references.

- **Figure 1** (2 panels, a and b): AUROCs of large vs small LLMs, panel a on USMLE, panel b on MGB-SDoH. Secondary result (model size effect). Likely paired bars or points per model family, explicit and implicit AUROC per model. Cited as "Figure 1" without panel letters.
- **Figure 2** (2 panels): panel a, AUPRC difference (implicit minus explicit) for large LLMs across imbalance levels on USMLE (legend gives the share of cases where option A is correct); panel b, probability distribution for one model (Llama 3.1 70B) with dashed Gaussian fits, yellow for option A correct, green for option B. Secondary result plus one worked example; the remaining distributions are pushed to Supplementary Figs 11 to 15.
- **Figure 3** (2 panels): panel a, a comparison of probabilistic output across AI model types, using green happy and red unhappy face icons to mark whether each model type suits a use case; panel b, the conceptual framework of the study. This is the orientation figure, yet it is numbered last.

Figure 1 is a result figure, not a design overview. The schematic is Figure 3 because it is first cited in the Introduction (3a) and again in Methods (3b), and the npj convention of numbering by first citation was apparently not applied; numbering follows the order of the Results instead, with the schematic appended.

Numbers on figures: none reported. No values on bars, no n per group, no p values; standard deviations and significance stars live only in the tables. The main result (implicit beats explicit on AUROC and AUPRC) is carried entirely by Tables 2 and 3, and no main figure shows it across all datasets.

Panel references: "Figure 2a", "Figure 2b", "Figure 3a" in the preprint (npj typeset likely "Fig. 2a"). Panel letters in captions are bare lower case ("a AUPRC difference of...").

Colour and encoding: explicit vs implicit is the main contrast; the only stated colours are yellow and green for true label in Fig. 2b, and green vs red faces in Fig. 3a. Imbalance level is encoded as legend categories in Fig. 2a.

Supplementary: ROC and PRC curves for every dataset (Supp Figs 1 to 10), all per-model distributions (11 to 15), and the prompt sensitivity AUROCs (16). Main text keeps one representative example and pushes exhaustive per-dataset plots out.

# Tables

Three main tables, all placed after figure legends at the end in the preprint (inline in Results in the typeset version). All are results tables; there is no baseline or dataset characteristics table, no model table (model details are Supplementary Table 2) and no prompt table (Supplementary Table 1).

- **Table 1**, accuracy: models as rows (6), datasets as columns (5) plus an Average column first. Values in percent, one decimal, mean±SD (for example 86.7±0.1). Bold marks the best and italics the worst model per dataset, both explained in footnotes.
- **Table 2**, AUROC, and **Table 3**, AUPRC: same column logic, but each model is a block of three sub-rows: Explicit, Implicit, Difference. Difference cells carry an asterisk for p < 0.05 and a minus sign when explicit wins (for example -0.9±3.1). Percent, one decimal, ±SD.

Footnotes are short and formulaic: what bold or italics mean, what the asterisk means, what follows the ± symbol. Abbreviations (AUROC, AUPRC, dataset codes) are not expanded in footnotes. The Results text mentions a P-value column that the tables do not have (they use asterisks), a small text and table mismatch. One cell in the preprint has a typo (02. for 0.2).

Prose and tables: the text narrates highlights (best model overall, best on MCMLE, weakest on MCMLE, the one exception where explicit wins) and points to "Table 1 to Table 3" collectively, rather than repeating the full grid.

# Captions

- Structure: a short title, which is then repeated verbatim as the first sentence of the legend, followed by one sentence per panel introduced by a bare letter. Figure 2 and 3 add one encoding sentence (dashed lines and colours; face icons).
- Length: figure titles 6 to 10 words; full figure legends roughly 20 to 45 words (typical about 30). Table titles are 7 to 8 words, with 1 to 3 one-line footnotes.
- Tone: purely descriptive labels, never a claim. Examples: "AUROCs of the large and small LLMs"; "AUPRC difference and probability distribution on the USMLE dataset"; "Accuracy of the LLMs on different datasets".
- Content: what is plotted and on which dataset; colour or line legend where needed. Absent: n, number of runs behind the SD, statistical test, error bar meaning, abbreviation expansions, takeaway.
- Stand-alone: weak. A reader needs the text to know what explicit and implicit mean, what MGB-SDoH is, or how imbalance was created.
- Tables vs figures: table titles are a single noun phrase; all formatting and statistical conventions sit in footnotes. Figure legends carry panel descriptions and encoding.

# Order and organisation

Outline (approximate words, share of about 4,500 words excluding references):

| Section | Words | Share |
|---|---|---|
| Abstract | 120 to 170 | 3% |
| Introduction | 750 to 840 | 18% |
| Results (unheaded opener; LLM Performance; Large LLM vs. Small LLM; Imbalanced Datasets Analysis; LLM probability distribution; Sensitivity Analysis) | 1,300 to 1,400 | 30% |
| Discussion (no subheadings) | 850 to 900 | 20% |
| Methods (Data Source; Experiment Setting; Prediction and Probability Extraction; Evaluation; Imbalanced Datasets Analysis; Sensitivity Analysis) | 1,100 to 1,200 | 26% |
| Data, code availability, acknowledgements, contributions, competing interests | about 200 | 4% |

Methods last (npj default). Coping strategies: the Introduction carries the key definitions and cites the framework schematic (Fig. 3a); the LLM Performance subsection opens by redefining Explicit, Implicit, Difference and P value; the imbalance and sensitivity subsections each open with a sentence restating how the condition was built. Results and Methods share mirrored subheadings (Imbalanced Datasets Analysis, Sensitivity Analysis), which eases cross-reading.

Results ordering: a short unheaded paragraph on format compliance (a data quality check, pointing to Supplementary Table 7), then the main comparison across all models and datasets (Tables 1 to 3), then moderators (model size, class imbalance), then a descriptive look at distributions, then prompt sensitivity. Subsection headings are labels, not claims.

Figure distribution: Tables 1 to 3 feed one subsection; Figure 1 one subsection; Figure 2a and 2b feed two adjacent subsections; Figure 3 feeds Introduction and Methods. Results subsections without a main figure lean on supplementary items.

Discussion sequence (7 paragraphs): restate main finding with scope; clinical stakes of thresholds and miscalibration; how degraded performance amplifies the gap, tied to real clinical contexts; future remedies (fine-tuning under implicit supervision, numerical reasoning); link to hallucination detection as future work; limitations in one paragraph (binary tasks, no chain of thought, open models only, medical only); conclusion urging caution.

Supplementary use: heavy, about 9 pointers in Results alone, phrased as parenthetical "(Supplementary Table 3)" or "(Supplementary Figure 1 to Supplementary Figure 10)", that is, ranges written out in full. Supplementary carries prompts, model details, all per-dataset curves, failure cases and compliance rates.

Boxes: no key points, highlights, graphical abstract or research-in-context panel.

Ease of reading: compact and predictable, with mirrored Methods headings. Harder points: the orientation schematic is numbered last; the headline result has no figure; captions do not stand alone; and the text refers to a P-value column that does not exist.

# Checklist candidates

- Report mean±SD in a single cell with one decimal and state in a footnote what follows the ± symbol. [strong]
- In a comparison table, put models as rows and datasets as columns, and add an Average column. [strong]
- When comparing two methods per model, use stacked sub-rows (method A, method B, Difference) and flag significant differences with an asterisk defined in a footnote. [strong]
- Mark best and worst values typographically (bold, italics) and explain each in a footnote. [weak]
- Keep table titles to one descriptive noun phrase and move every convention to footnotes. [strong]
- Use descriptive caption titles, not claims, and describe each panel in one sentence led by its letter. [strong]
- State the colour or line encoding in the caption whenever the figure relies on it. [strong]
- Show one representative example in the main figure and push the full per-model or per-dataset set to supplementary. [strong]
- Number figures in order of first citation; if a schematic is cited in the Introduction it should be Figure 1. [strong] (this paper violates it)
- Give the headline comparison a main figure, not only a table. [weak] (lesson from its absence)
- When Methods comes last, open each Results subsection with one sentence redefining the condition or metric it reports. [strong]
- Mirror Results subheadings in Methods for each secondary analysis. [strong]
- Open Results with a brief data quality or compliance check before the main outcome. [weak]
- Make sure the text never names a table column that the table does not contain. [strong]
- Cite supplementary items parenthetically at the end of the sentence they support. [strong]

# Notable deviations

- The conceptual framework and study design schematic is Figure 3, cited in the Introduction before Figures 1 and 2, breaking first-citation numbering.
- No main figure shows the primary result; the core evidence is tables only.
- No dataset characteristics table despite five datasets, one private.
- Captions omit n, number of repeats, test and abbreviations, so they do not stand alone.
- Figure 3a uses face emoji icons as a suitability encoding, unusual for npj.
- Text describes a P-value column that the tables replace with asterisks; one cell typo in the preprint.
