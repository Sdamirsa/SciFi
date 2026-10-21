# Paper
Gaber F et al., Evaluating LLM workflows in clinical decision support for triage, referral and diagnosis; npj Digital Medicine 2025; original research; source: open-access PDF in the MDC Berlin repository (edoc.mdc-berlin.de, eprint 25329), read through WebFetch paraphrase (verbatim text was refused beyond short quotes, so caption word counts are estimates).

# Figures
Eight figures in the main text, no extended data; 11 supplementary figures and 2 supplementary tables.

| Fig. | Type | Panels | Role | Where cited |
|---|---|---|---|---|
| 1 | Workflow schematic (user inputs, prompts, models incl. RAG, comparison with ground truth) | 1 | Orientation, study design | Results, subsection 2 (model selection) |
| 2 | Bar charts: triage level distribution (a), predicted specialty distribution (b) | 2 | Data description | Results, subsection 1 (dataset) |
| 3 | Grouped bars, triage accuracy, exact match vs range | 2 (left/right, not lettered) | Main result | Results, triage |
| 4 | Confusion matrices for the two best models by user setting and evaluation method | 4 (a to d) | Error structure of main result | Results, triage |
| 5 | Grouped bars, specialty accuracy, two metrics | 2 (left/right) | Main result, task 2 | Results, specialty |
| 6 | Grouped bars, diagnosis accuracy, two metrics | 2 (left/right) | Main result, task 3 | Results, diagnosis |
| 7 | Flow diagram of data preprocessing (MIMIC-IV-ED and MIMIC-IV-Note merging, cleaning, extraction) | 1 | Methods support | Methods, data preprocessing |
| 8 | Workflow of the RAG pipeline (query decomposition, embedding, 30 million PubMed abstracts, critique loop) | 1 | Methods support | Methods, RAG-assisted LLM |

- Figure 1 is the pipeline overview: who supplies the input (general user vs clinical user), which models, and how outputs are scored. It works as a graphical abstract. Oddly, the text cites Fig. 2 before Fig. 1 because the dataset subsection comes first.
- Figures 3, 5 and 6 form a deliberate parallel set: one figure per task, identical layout (accuracy [%] across models, strict metric left, lenient metric right). The same numbers are also in Table 1, so the bar charts duplicate a table.
- No error bars, CIs or p values are reported anywhere; the axis unit is written as "Accuracy [%]" in brackets.
- Panel labels are lowercase letters (2a, 2b, 4a to 4d) where used; side-by-side halves of Figs 3, 5, 6 are described as left and right instead of being lettered.
- In-text citation is inconsistent: "Figure 2a" and "Figure 4 presents" in running text, "Fig. 3" elsewhere; supplementary items as "Supplementary Fig. 7".
- Colour encoding cannot be confirmed from text; the captions give no colour legend.
- Two methods figures (7, 8) sit in the main text rather than the supplement; prompts (Supplementary Figs 1 to 6), specialty frequencies (Supp. Fig. 7) and clinician confusion matrices (Supp. Figs 8 to 11) are pushed to the supplement.

# Tables
Six main tables, all text tables placed near first citation.

- Table 1, model performance across tasks and evaluation methods. Rows: models (RAG-assisted LLM, Claude 3.5 Sonnet, Claude 3 Sonnet, Claude 3 Haiku) nested under two user-setting blocks (General User, Clinical User). Columns: grouped headers per task (triage: exact match, range; specialty: matched, at least one; diagnosis: matched, at least one) plus an Average column. Accuracy in percent with two decimals. Bold marks best and underline second best within each user setting and metric, explained in the footnote. No CIs. Table 1 is a results table, not baseline characteristics; there is no cohort characteristics table at all.
- Table 2, change from general to clinical user setting. Same column structure as Table 1, models as rows, signed differences with two decimals; unit not restated.
- Table 3, inter-model agreement. Rows are comparison categories ("Between General and Clinical User", "To model X"), columns are models plus Average; self-comparisons shown as dashes, with a footnote explaining why (to avoid distorting averages).
- Table 4, clinician validation of ground-truth specialties: rows Clinician 1 to 4 plus Average; columns Accurate, Acceptable, Accurate and Acceptable, Error Rate, each with [%] in the header.
- Table 5, clinician rating of LLM-judge diagnoses: two-level headers (metric, then model); union and intersection values given once per clinician pair, leaving blank cells.
- Table 6, worked example (one case: diagnoses, ground-truth specialties, predicted specialties), text only, placed in Methods.
- Units live in column headers in square brackets. Decimals: two throughout, with some inconsistency (100, 81.5).
- Prose repeats selected table values (for example 81.5% and 97.03% for clinician validation) and otherwise points to the table and narrates which model leads.

# Captions
- Structure: short bold title, then a descriptive paragraph for figures; tables have a title plus a footnote-style note beneath rather than a caption paragraph.
- Length: figure captions roughly 45 to 85 words (typical about 50); table titles 5 to 14 words, with notes adding 15 to 70 words.
- Tone: descriptive labels, never claims. Titles often use a "X: A vs. B" pattern. Examples: "Triage level accuracy: exact match vs. range evaluation."; "Confusion matrices for triage level prediction."; "Workflow of the RAG-assisted LLM."
- Content: panel-by-panel description (a, b; left, right), the metric and unit, how to read special encodings (diagonal = exact match, marked cells = correct under range). Methods figures name data sources (MIMIC-IV-ED 2.2, PhysioNet; 30 million PubMed abstracts). No statistics, n per group or error bar definitions, because none exist.
- Table notes carry the formatting legend (bold and underline meaning), unit, and definitions of row categories.
- Abbreviations (LLM, RAG) are not systematically redefined. Captions mostly stand alone for the parallel bar charts, less so for Table 2 where the sign convention is only implied.

# Order and organisation
Outline (approximate words, share of about 6900 words excluding references and back matter):
1. Abstract, 150 (2%)
2. Introduction, unheaded, 800 (12%)
3. Results, 2300 (33%): Curated MIMIC-ED dataset and model evaluation approach; Model selection and RAG-assisted LLM; LLM performance in triage; Predicting appropriate medical specialty referrals from patient data; Evaluating LLM workflows for diagnostic accuracy; Intra-model agreement; Clinician validation of LLM-generated specialties; Inter-rater-agreement on diagnosis evaluation
4. Discussion, no subheadings, 1300 (19%)
5. Methods, 2300 (33%): Data preprocessing; Prompts; Model selection; RAG-assisted LLM; Triage, Specialty and Diagnosis evaluation frameworks; LLM judge; Reader study; Intra-model agreement; Data and Code availability

- Methods comes last (npj format). Results compensates with two setup subsections (dataset, models and user settings) that cost about 500 words before any result, and each task subsection re-explains its metric (ESI, exact vs range, matched vs at least one, LLM judge) in a sentence or two. Model selection and RAG are therefore described twice.
- Results ordering: data, setup, then one subsection per task in the order of the paper title (triage, specialty, diagnosis), then consistency (inter-model agreement), then human evaluation (two clinician subsections). Within each task subsection: metric definition, Fig. (bar chart), Table 1, then Table 2 for the effect of adding vitals.
- Subsection headings are labels, not claims.
- Figure distribution: one figure per task subsection; Table 1 and Table 2 each feed three subsections; agreement and clinician subsections get one table each; methods figures sit in Methods.
- Discussion sequence: main finding and RAG traceability; RAG vs base with vitals; mechanistic hypothesis; literature comparison; triage limitations; future work and prompting; human variability; regulation (EU AI Act, "leaky deployment"); newer reasoning models; conclusion and no-deployment caveat. Limitations are scattered, not in a single block.
- Supplementary pointers are frequent (about 7 places), phrased as "Supplementary Table 1", "Supplementary Fig. 7", "provided in the Supplementary Fig. 8 and 9".
- No boxes, key points or highlights.
- Easy to follow because the three tasks share an identical template; harder because the user-setting comparison lives in a separate table, Fig. 2 precedes Fig. 1, and there are no uncertainty estimates.

# Checklist candidates
- Make Figure 1 a pipeline overview showing inputs, models, outputs and how they are scored against ground truth. [strong]
- Ensure figures are first cited in numerical order; if the dataset subsection comes first, make its figure Figure 1. [strong]
- When a paper evaluates several parallel tasks, give each task a figure with an identical layout, metric and model order. [strong]
- Put one master results table with models as rows nested in setting blocks and grouped metric columns per task, plus an Average column. [strong]
- Explain bold (best) and underline (second best) in the table footnote and state the scope of the comparison. [strong]
- Put units in column headers or axis labels in brackets, for example "Accuracy [%]". [weak]
- Report a delta table when comparing two input conditions, and state the sign convention in its note. [weak]
- Use lowercase panel letters and one citation form ("Fig. 2a") consistently throughout. [strong]
- Write caption titles as descriptive labels, often "Metric: A vs. B", and explain any nonstandard encoding (diagonal, marked cells) in the caption. [strong]
- Report CIs or bootstrap intervals in tables and error bars on bar charts; this paper's omission is a gap reviewers will flag. [strong]
- When Methods comes last, open Results with a short dataset and setup subsection and define each metric in one sentence where it is first used. [strong]
- Order Results as data, setup, primary tasks in title order, consistency analyses, human evaluation. [weak]
- Keep worked examples and pipeline diagrams that only support Methods in the Methods section or supplement. [weak]
- Use a consistent number of decimals within a table. [strong]

# Notable deviations
- No baseline characteristics table; Table 1 is model performance.
- Fig. 2 is cited before Fig. 1.
- No CIs, SDs, p values or kappa statistics anywhere, yet "significant" is used descriptively.
- Bar charts duplicate Table 1 values.
- Two Methods figures and a Methods table (Table 6) in the main text, giving 14 display items, high for npj.
- Halves of multi-part figures labelled left and right instead of lettered panels.
- Unheaded Introduction and an unstructured, ten-paragraph Discussion without a limitations subsection.
