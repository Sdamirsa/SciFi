# Paper
Jin Q et al. AgentMD, Nature Communications 16:9377 (2025), original research Article; source: local PDF, all 11 pages read visually (no supplementary pages in file).

# Figures
Five main figures, all multi-panel, lowercase bold panel letters (a, b, c...). No extended data figures in the PDF; supplementary material exists online but is referenced only twice.

- **Fig. 1 (2 panels, orientation).** Architecture overview. Panel a: flow "Medical Literature > AgentMD Tool Curation > RiskCalcs" plus a worked example, the CURB-65 calculator shown as a structured text card (Purpose, Eligibility, Size, Computation, Interpretation, Utility) beside its generated Python function. Panel b: pipeline schematic of tool selection (MedCPT patient embedding, a scatter of RiskCalcs embeddings, relevant calculators), tool computation (LLM looping "x N" with a Python interpreter, showing success and TypeError messages) and summarization (a free-text best/worst case output). Figure 1 is the system pipeline anchored on one concrete example, not a study-design flow chart. No numbers.
- **Fig. 2 (2 panels, main result for curation).** Dense heat-map grids: rows are calculators (top 50 cited in a, random 50 in b), column blocks are Correctness (Logic, Interp.), Unit Tests (Q1 to Q5) and Coverage (MDCalc, Others), with a horizontal bar chart of citation counts appended at the right. Categorical colours (blue correct, light blue partial, red incorrect; green for internal unit test pass). Legends sit as boxed keys above the panels. No numeric values on the figure; the percentages live only in the text.
- **Fig. 3 (4 panels, main benchmark result).** Panel a: schematic of a USMLE-style RiskQA item flowing through tool selection, parameter extraction, computation and prediction (N = 350 in the header). Panels b to d: simple bar charts of accuracy with values printed above each bar to three decimals and error bars; y axis 0 to 1. Baselines (Random, CoT) in grey, AgentMD highlighted in salmon in b and c; in d the AgentMD bars are steel blue against grey MedCPT. The backbone model is written under each bar label.
- **Fig. 4 (3 panels, real-world individual evaluation).** a: schematic (698 notes > 16 calculators > ranking > clinician evaluation). b: horizontal 100% stacked bars for three aspects (Yes/Partial/No in green/yellow/red), with the Yes percentage printed inside the bar. c: annotated heat map of per-calculator scores (two decimals in cells) for three aspects plus an average column, rows sorted by average.
- **Fig. 5 (6 panels, population-level analysis).** a and b: schematics (MIMIC-III notes to risk summaries; patients ranked per calculator). c, d: density curves (calculators per patient; patients per calculator). e: 2 x 4 grid of density plots (two calculators by four LLM scores). f: four ROC curves, AgentMD red vs GPT-4 blue, AUC values in the legend, the gap shaded.

Pattern: each results figure opens with a schematic panel a that restates the task, followed by quantitative panels. Text cites panels as "Fig. 2a", "Fig. 3b", ranges "(b to d)" in captions, and "Figure 3d shows..." at sentence start. Every figure caption ends with a Source Data statement.

# Tables
No tables in the main text. Prompts, normally a table or box, are given inline in Methods as indented verbatim System/User/Output blocks. The Discussion points to Supplementary Table 13 (input parameters requiring extraction), implying at least 13 supplementary tables. No baseline-characteristics Table 1; cohort sizes (350, 698, 9822) are carried in figure headers and text. All key numbers appear in prose and are also printed on figures (Fig. 3, 4), so results are repeated rather than only pointed to.

# Captions
- Structure: bold sentence-case title ending with a period, then panel-by-panel description with bold panel letters, then a definitions or statistics sentence, then "Source data are provided as a Source Data file."
- Length: about 40 to 90 words, typical about 70 (Fig. 1 shortest, Fig. 3 longest).
- Tone: titles are descriptive labels, never claims. Examples: "Overview of AgentMD tool curation and using."; "Quality and coverage analysis of RiskCalcs."; "Evaluations of AgentMD on RiskQA."
- Content: Fig. 3 defines what bar heights and error bars mean (accuracy as proportion correct, N = 350; error bars as standard deviations). Fig. 2 defines its abbreviations (Logic, Interp., Q1 to Q5). Fig. 4 states the sampling (top 5 patients per calculator) and sort order. Fig. 1 gives the source article PMID. One panel description in Fig. 5 is a claim (AgentMD outperforms GPT-4 in f), otherwise neutral.
- Standalone: largely yes; abbreviations such as CoT are expanded again in the caption.
- No table captions to compare.

# Order and organisation
Approximate words (main text about 5,100 excluding references and back matter):
1. Abstract, unstructured (about 145, 3%)
2. Introduction, no heading (about 500, 10%), ends with the two objectives, the tool maker/tool user framing, pointer to Fig. 1, and a preview of the three cohorts and headline numbers.
3. Results (about 1,500, 29%), four claim headings:
   - RiskCalcs tools feature high quality and extensive coverage (Fig. 2)
   - AgentMD can accurately perform risk prediction tasks on the RiskQA benchmark (Fig. 3)
   - AgentMD can accurately calculate individual risks from emergency department notes (Fig. 4)
   - AgentMD can be applied to clinical notes and provide population-level risk insights (Fig. 5)
4. Discussion (about 650, 13%): restated problem and approach; curation findings; comparison with concurrent work (OpenMedCalc, Almanac); benchmark and real-world results recap; limitations paragraph (PubMed abstracts only, GPT-4 cost and local deployment, text only); one-sentence conclusion.
5. Methods (about 2,000, 39%): Compliance statement; Backbone LLMs; Curating calculators (with full prompts); Evaluation as tool maker; Applying calculators to patients; CoT baseline; Evaluation as tool user (RiskQA, ED notes, MIMIC-III, inter-rater agreement with bootstrap CIs); Statistics & reproducibility.
6. Data availability, Code availability, References (36), Acknowledgements, Author contributions, Competing interests, Additional information.

Methods last: Results re-explains each experiment in one or two sentences at the head of each subsection (who annotated, how many, what labels) and leans on the schematic panel a of each figure to carry design. Results order follows the system's lifecycle: build tools, controlled benchmark, real individual notes, population scale; this escalating-realism arc is the backbone. One figure per Results subsection, strictly in order. Supplementary material is nearly invisible (two pointers, phrased "As shown in Supplementary Table 13" and "The Supplementary Materials contain a brief analysis..."). No boxes, key points or graphical abstract. Easy to follow because heading claim, figure and subsection map one to one; harder because Methods holds the per-score definitions (specificity, urgency, severity, absence) needed to read Fig. 5e.

# Checklist candidates
- Make Figure 1 a system overview anchored by one concrete worked example rather than an abstract box diagram. [strong]
- Allocate one main figure per Results subsection, numbered in order of first citation. [strong]
- Open each results figure with a schematic panel a that restates the task and N before the quantitative panels. [strong]
- Write Results subsection headings as full claim sentences naming the system and the finding. [strong]
- Order Results by escalating realism: curated resource, controlled benchmark, real individual data, population scale. [strong]
- Print exact values above bars and state in the caption what bar height and error bars represent, with N. [strong]
- Colour the proposed method consistently against grey baselines within a figure. [weak, colour shifts between Fig. 3c and 3d]
- Start captions with a bold, descriptive (non-claim) title, then bold panel letters with one clause per panel. [strong]
- Define abbreviations used on axes inside the caption. [strong]
- End every figure caption with a Source Data statement (Nature portfolio requirement). [strong]
- Cite panels as "Fig. 2a" in running text and "Figure 3d" at sentence start. [strong]
- Sort heat-map rows by a stated metric and say so in the caption. [weak]
- When Methods comes last, give each Results subsection a one to two sentence design recap. [strong]
- Report inter-rater agreement with bootstrap CIs in Methods, not Results. [weak]

# Notable deviations
- No tables at all, including no cohort characteristics table, which a clinical journal would expect.
- Full prompts are printed inline in Methods rather than in a box, table or supplement, inflating Methods to about 40% of the text.
- Fig. 2 carries no numeric summaries; the reader must take percentages from the text.
- Colour for AgentMD changes from salmon (Fig. 3b,c) to blue (Fig. 3d) to red (Fig. 5f).
- A typo ("CHEIF COMPLAINT") appears in schematic panels of Figs. 1, 4 and 5.
- Limitations are folded into a single Discussion paragraph without a heading.
