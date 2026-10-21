# Paper

Wornow M et al., The shaky foundations of LLMs and FMs for EHRs; npj Digital Medicine 2023; Review Article (narrative review with perspective argument); source: nature.com HTML and PDF (s41746-023-00879-8), read through several WebFetch extractions, so counts are approximate.

# Figures

- **Count and placement.** Four main figures, no extended data, no supplementary figures. Figures are the only display items; there are no tables or boxes.
- **Fig. 1: conceptual framework (orientation).** Two panels (a, b), one per model family: clinical language models (CLaMs) and foundation models for EMRs (FEMRs). Each panel is an input to output schematic (clinical text in, text or representation out; timed patient event sequence in, patient representation out). Figure 1 is the paper's taxonomy, not a study overview: it fixes the two categories that structure every later section. No numbers on the figure.
- **Fig. 2: evidence map for CLaMs (main result).** A grid chart: one column per model, rows for attributes, X for present and asterisk for partially present, and a final column counting entries per row. Three panels: (a) training data and public availability of code and weights; (b) evaluation tasks reported in each model's original paper; (c) the same tasks regrouped into the six claimed FM benefits. Counts per training data group (n = 23, 24, 3) are stated in the caption, and row totals are printed on the figure.
- **Fig. 3: evidence map for FEMRs (main result, parallel design).** Same grid logic and same a, b, c panel order as Fig. 2, so the reader compares the two families panel by panel. Panel b orders tasks by task format (binary, multi-class or multi-label, clustering, regression including time to event). Group counts n = 27, 3, 4.
- **Fig. 4: recommendation summary (synthesis).** Summarises the authors' proposed evaluations for each of the six benefits, for CLaMs and FEMRs. Its exact layout could not be confirmed from the extracted text; it appears to function as a table rendered as a figure, mirroring the numbered list of six proposals in the text.
- **Panel referencing in text.** Lower case letter attached to the number: Fig. 1a, Fig. 2b, Fig. 3c. Whole figures cited as Fig. 2 and Fig. 3 in the Discussion. Cross-figure comparisons are made explicitly in prose (the bottom row of Fig. 3a set against Fig. 2a to contrast weight release).
- **Colour encoding.** Colour codes the training data source of each model column: green clinical text, blue biomedical text, purple general text for CLaMs; red structured codes, orange codes plus text, yellow text only for FEMRs. In Fig. 2b colour also marks whether a task is clinical (green) or biomedical (blue), reusing the same mapping. Distinct hue families for the two model families keep Figs 2 and 3 visually separable.
- **Logic of the sequence.** Define (Fig. 1), map the evidence (Figs 2 and 3), prescribe (Fig. 4). Panel c of Figs 2 and 3 is the bridge: it recodes descriptive data into the paper's own benefit framework, which is where the central claim (evaluation is almost all predictive accuracy) becomes visible.

# Tables

- No tables. Content that would usually be a Table (a model inventory with training data, availability and evaluation tasks for 84 models) is encoded as two grid figures instead. The benefit list and the evaluation proposals, which could be summary tables, are numbered lists in the text, with Fig. 4 as the visual summary.
- Consequence: no Table 1 baseline convention applies. For a review, the "Table 1" role is filled by Fig. 1 (taxonomy) and the inventory role by Figs 2 and 3.

# Captions

- **Structure.** Bold short title as a noun phrase, then descriptive sentences, with panel descriptions introduced by the bold panel letter (a ..., b ..., c ...).
- **Length.** 32 to about 320 words. Fig. 1 about 100 words; Figs 2 and 3 about 310 to 320 words and about 17 sentences each; Fig. 4 about 32 words in 2 sentences. Typical for the data figures is about 300 words; the schematic and synthesis figures are short.
- **Tone.** Titles are descriptive labels, never claims. Examples: "The two types of clinical FMs."; "Overview of CLaMs."; "Better evaluations of clinical FMs." Body text describes what rows, columns and symbols mean; it does not state findings.
- **Contents of the long captions.** How to read the grid (columns are models, rows are attributes, last column is a count), symbol key (X and asterisk), colour legend with n per colour group, panel by panel content, and the source of the data (each model's original paper; a public model hub for weight availability). No statistics, since none are computed.
- **Abbreviations.** Fig. 1 expands CLaM and FEMR in the caption; Figs 2 and 3 use CLaM, FEMR, FM and EMR without expansion, so they rely on the text and do not fully stand alone. The grid legends do stand alone for reading the figure.
- **Parallelism.** Figs 2 and 3 captions use the same sentence order and phrasing, differing only in model family, colours and task categories.

# Order and organisation

**Outline (approximate body words, total about 4,800):**

1. Abstract (about 140 words, unstructured)
2. Introduction, no heading on the page (about 700, 15%)
3. What are clinical FMs? (about 770, 16%), with subsections on CLaMs and FEMRs; Fig. 1a and 1b cited here
4. Benefits of clinical FMs (about 650, 14%): numbered list of six benefits, each opening with a short claim sentence
5. State of published clinical FMs (about 2,250, 47%): opens with how the 84 models were found, then paired subsections alternating CLaMs and FEMRs on training data, availability or accessibility, evaluation on standard tasks, and evaluation on FM benefits; ends with six numbered evaluation proposals, each led by a label and colon, and Fig. 4
6. Discussion (about 400, 8%)
7. End matter: Data availability (one sentence saying the figures contain all data), acknowledgements, author contributions, competing interests. No code availability, no Methods, no supplementary information.

- **Methods placement.** No Methods section. Model identification (citation following and manual curation, cutoff 1 March 2023, explicit disclaimer that the search is not systematic) sits in the first paragraph of the evidence section, immediately before the figures it feeds.
- **Ordering logic in the evidence section.** Frame before data: the benefit framework (section 4) is built before the evidence (section 5), so panel c of Figs 2 and 3 can score the literature against it. Within section 5, each attribute is shown for CLaMs then FEMRs, and each subsection cites one panel. Subsection headings are labels (Training data, Model availability, Evaluation on FM benefits), not claims.
- **Figure distribution.** One figure per model family, with each panel feeding one subsection in a fixed a, b, c order. Fig. 1 serves the definitional section, Fig. 4 closes the evidence section.
- **Discussion sequence (four paragraphs).** (1) Restated finding: evaluation is mostly predictive accuracy, so new value-based evaluations are needed. (2) Extension to general-purpose LLMs and the open question of whether clinical-specific models are still needed. (3) Risks: privacy, interpretability, cost, regulation, automation bias. (4) Short optimistic close with a call to the community.
- **Supplementary material.** None, and none pointed to.
- **Boxes or key points.** None; the two numbered lists of six do the job a box would.
- **Ease of reading.** The repeated six-item frame (benefits list, panel c, proposals list, Fig. 4) and the strict CLaM then FEMR alternation make a long survey section easy to navigate. The weak points are the unlabelled introduction, the heavy evidence section (almost half the text) and the long captions of Figs 2 and 3, which carry reading instructions the text does not repeat.

# Checklist candidates

- For a review, make Figure 1 the taxonomy or conceptual framework that every later section uses. [strong]
- Encode a large model or study inventory as a grid figure (items as columns, attributes as rows, a symbol for present and for partial, a final count column) rather than a long table. [strong]
- When two families of items are compared, give them parallel figures with identical panel order and near identical captions. [strong]
- Order panels so that the last one recodes the descriptive data into the paper's own framework, making the central claim visible. [strong]
- Build the evaluative framework before presenting the evidence that is scored against it. [strong]
- Use one consistent colour mapping for a grouping variable across all panels, and use different hue families for different item families. [weak]
- Give n per colour group inside the caption legend. [strong]
- Cite panels as Fig. 2a style and make cross-figure comparisons explicit in the text. [strong]
- Write figure titles as short descriptive noun phrases, not claims. [strong]
- In data captions, explain how to read the figure (rows, columns, symbols, colour, data source); leave findings to the text. [strong]
- Expand abbreviations in each caption so it stands alone (this paper does so only for Fig. 1). [weak]
- In a narrative review without Methods, state the search approach, date cutoff and non-systematic nature in the first paragraph of the evidence section. [strong]
- End the evidence section with a figure that summarises the recommendations. [weak]
- State in Data availability that all data appear in the figures when that is true. [weak]

# Notable deviations

- No tables at all in an 84-item review; the inventory lives in figures.
- Caption length varies tenfold (about 32 to 320 words) within one paper.
- No Methods section and no supplementary material; the search description is a short in-text paragraph with an explicit non-systematic disclaimer.
- Introduction carries no heading, and the evidence section is close to half the paper while the Discussion is under a tenth.
- Recommendations appear twice, as a numbered list and as Fig. 4, rather than in a box.
