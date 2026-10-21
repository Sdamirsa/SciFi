# Figures

What to draw, in what order, and how to label it. Derived from 14 papers with 2 to 8 main figures each (median 5), plus extended data and supplementary sets.

## 1. Which figures to make

A clinical-AI original research paper needs, in this order of priority:

1. **Overview (Figure 1).** The study design or system pipeline from input to endpoint, in one panel, optionally paired with one worked example case. Three forms worked well in the corpus: (a) a pipeline from scan or note, through the AI step, to the clinical endpoint; (b) a grid of sub-studies by aim, cohort with n and analysis, for multi-study papers; (c) a composite that shows system, study design and a headline result teaser. For a method or benchmark paper the architecture leads; for a cohort study the design leads. Cite it from the end of the Introduction (Nature-portfolio) or from the first Methods subsection (Lancet, JAMIA, EHJ).
2. **Flow diagram.** Cohort inclusion and exclusion with n at every step on the figure itself (STROBE style), or PRISMA for reviews, or a train, validation, test split schematic with percentages and n. Cited from the first Results sentence.
3. **Primary result.** One multi-panel figure with one panel per outcome, tissue, task or rating axis, identical layout across panels, values printed on the plot (percentages with n/N on bars, HR with 95% CI inside Kaplan-Meier panels, AUC with CI inside ROC panels), number-at-risk tables under survival curves, error bars or CI bands defined in the caption.
4. **Secondary or robustness results.** Subgroups as a forest plot, ablations as grouped bars, calibration plot, decision curve. One representative panel in the main text; the full set in the supplement.
5. **Worked example.** One case traced end to end (input, tool calls, intermediate outputs, final answer) or example outputs side by side with errors highlighted. Place it next to the method it illustrates, not after the main result.
6. **Error analysis.** Confusion matrices or heat maps of predicted versus actual labels, with counts in cells.

Figures that only support Methods (preprocessing flow, prompt anatomy, RAG pipeline) go to the supplement unless the pipeline is the contribution. Four to six main figures is the target for a 3,500 word paper; eight is the upper bound seen.

## 2. Figure types by purpose

| Purpose | Preferred type | Avoid |
|---|---|---|
| Design, system | Schematic with icons and stage numbers | Dense box diagrams without an example |
| Cohort | Flowchart with n per step | Prose only |
| Performance across models or metrics | Bar chart with values on bars and CI error bars; small multiples (one subplot per axis) when there are many rubric items | A single crowded chart; radar charts without numbers |
| Discrimination | ROC with AUC and CI inside the plot; precision-recall for rare outcomes alongside, not instead | Partial curves without a reference line |
| Calibration | Calibration plot with grouped points, a smoother and the diagonal | Calibration slope alone |
| Survival | Kaplan-Meier with HR, CI and p printed, number at risk | Curves without at-risk tables |
| Clinical utility | Decision curve with "treat all" and "treat none" reference lines | Net benefit as a number only |
| Agreement, confusion | Heat map with counts in cells, sorted rows and a stated sort key | Unsorted matrices |
| Inventory of models or studies (reviews) | Grid figure: items as columns, attributes as rows, symbol for present and partial, a count column, colour for one grouping variable | A 60 row table |
| Conceptual framework (reviews) | Taxonomy diagram as Figure 1; worked example scenarios as Figure 2 | Figures that are never cited by panel |

## 3. Panels

- Letter every panel (a, b, c lower case bold for Nature-portfolio and npj; A, B, C upper case for Lancet, JAMIA, EHJ). Use the same case on the art, in the caption and in the text.
- Cite panels in the text whenever a sentence reports one panel's data ("Figure 4b"). Never "left panel", "right", "top", "middle"; four corpus papers did this and it is the first thing a production editor queries.
- Panel order matches the order in which the text discusses them, and the order of the Results subsections.
- A results figure may open with a schematic panel (a) that restates the task and n, followed by the quantitative panels; this helped readers when Methods came last.
- Keep the same comparator order, axis range and encoding across all panels of one figure and across parallel figures.

## 4. Colour and encoding

- One fixed colour per arm, model or group across every figure in the paper (for example the proposed method in one warm colour, baselines in greys, the comparator in one cool colour, ties in light grey). Two corpus papers changed the colour of their own method between figures.
- Encode success, failure and not applicable with the same three colours in every result panel, and say so once in the first caption.
- Do not rely on colour alone to mark errors in example tables or figures; add a symbol or bold.
- Vendor logos, emoji and face icons as encodings are unusual and should be avoided for clinical journals.
- Reference lines (diagonal, treat all, treat none, Bonferroni threshold, random baseline) make a plot readable without colour.

## 5. Numbers on figures

- Print the value on every bar in a headline comparison, with n/N for proportions from small samples.
- Print HR (95% CI) and p on Kaplan-Meier panels; AUC (95% CI) on ROC panels; delta AUC with p on incremental value plots.
- Print exact p values only for comparisons that survive multiplicity correction, and say so in the caption.
- Define every error bar (SD, SE, 95% CI, and how obtained) in the caption. "±" without a definition is the single most common figure defect in the corpus.
- State n per group on the figure or in the caption.

## 6. Supplementary and extended figures

- Extended data (Nature-portfolio): architecture diagrams, rater interfaces, full rubric distributions, per-item results, additional worked examples with captions that point out an error.
- Supplementary: per-dataset curves when one representative panel is in the main text, stability analyses, subgroup Kaplan-Meier curves, recalibrated results, prompts as figures.
- Style supplementary figures like the main ones; default plotting styles next to designed main figures look like an afterthought.
- Every supplementary figure is cited by number in the main text.

## 7. In a review or perspective

- Figure 1 is the conceptual framework or taxonomy that every later section uses; cite it where the concept is introduced.
- Figure 2 shows worked example scenarios (input, query, output) that make abstract capabilities concrete.
- An evidence map (grid figure) can replace a long inventory table; give n per colour group in the legend.
- A final figure or table summarises recommendations against the organising list.
- Credit any reused image with source and licence in the caption.
