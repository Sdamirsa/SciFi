You are analysing ONE published paper for a second, narrower pass. A first pass already extracted the prose patterns; this pass covers (A) figures, (B) tables, (C) captions and (D) the order and organisation of the whole paper. The findings feed a reusable scientific-writing skill for a clinical-AI researcher who publishes in npj Digital Medicine, JAMIA, Nature-portfolio journals and The Lancet Digital Health. Work at medium reasoning effort.

PAPER
{PAPER}

STEP 1: GET THE TEXT AND THE FIGURES
{SOURCE_STEP}
Read the first-pass analysis at {FIRSTPASS} only for its "# Paper" section (source URL, article type); do not repeat its content.

STEP 2: ANALYSE
A. FIGURES (for each main figure, and extended data or supplementary figures if present)
- Number, type (schematic or study overview, flow diagram, bar or box plot, ROC or calibration curve, forest plot, Kaplan-Meier, heat map, example cases or screenshots, workflow, conceptual framework), number of panels, and what the figure is for (orientation, main result, secondary result, robustness, worked example).
- Which figure is Figure 1 and why (study design overview? conceptual framework? pipeline?). Where numbers appear on the figure itself (values on bars, n per group, p values, CIs).
- Panel labelling and how the text refers to panels (Fig. 2b, Figure 2B, Fig. 2, panel b).
- Colour and encoding conventions you can infer from captions and text (model vs baseline, groups).
- How many figures in main text vs supplementary, and what is pushed to supplementary.

B. TABLES
- Number, position in the paper, what each contains (baseline characteristics, model performance by metric, comparison with prior work, hyperparameters, prompt templates, definitions or taxonomy, recommendation summary).
- Column and row logic (models as rows, metrics as columns? subgroups as rows?). Units, decimals, how CIs and p values are laid out in cells, use of bold for best values, footnotes for abbreviations and statistical notes.
- Table 1 convention (baseline characteristics?) and whether results that appear in tables are repeated in the prose or only pointed to.

C. CAPTIONS (figures and tables)
- Structure: one-sentence title then description? Title only? Full paragraph? Title in bold?
- Length in words (give the range and the typical value).
- Tone: declarative claim ("X outperforms Y") vs descriptive label ("Performance of X and Y").
- What the caption contains: panel-by-panel description, definition of abbreviations, statistics used (bootstrap, n, error bar meaning, test), data source, colour legend, what the reader should notice.
- Whether abbreviations are redefined in captions, and whether captions stand alone without the text.
- Table titles vs figure captions: differences.
- Give 2 to 3 example caption titles (quote at most 12 words each).

D. ORDER AND ORGANISATION
- Full section and subsection outline of the paper in order, with approximate word counts per section and the share of the total.
- Where Methods sits (before or after Results) and how the paper copes with that (what the Results section has to re-explain when Methods comes last).
- Within Results: ordering logic (data description first, then main outcome, then secondary analyses, then robustness or ablations, then clinician or human evaluation?). Whether subsection headings are claims or labels.
- Within Discussion: the paragraph-level sequence.
- How figures and tables are distributed across the Results subsections (one figure per subsection? one figure feeding several subsections?).
- How the paper handles supplementary material: how often it points to it and with what phrasing.
- Any boxes, panels, "Research in context", key points, highlights, or graphical abstract, and what they contain.
- Anything about the organisation that makes the paper easy or hard to follow.

STEP 3: WRITE THE ANALYSIS FILE
Write to {OUTFILE} in Markdown with exactly these top-level headings:
# Paper
(one line: short citation, journal, article type, source used)
# Figures
# Tables
# Captions
# Order and organisation
# Checklist candidates
(concrete checkable rules on figures, tables, captions and organisation that this paper supports, each phrased as an instruction, marked [strong] or [weak])
# Notable deviations

Constraints: never quote more than 12 consecutive words from the paper; prefer paraphrase. Do not use em dashes or en dashes anywhere in your file. Keep the file under about 1500 words. When finished, reply with a 5 line summary and confirm the file path.
