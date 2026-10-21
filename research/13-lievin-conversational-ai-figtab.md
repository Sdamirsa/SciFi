# Paper
Lievin V, et al. Towards conversational artificial intelligence for disease management. Nature 2026;655:1292-1299; original research Article (randomized blinded virtual OSCE plus new RxQA benchmark); source: local 28-page PDF read as page images (Supplementary Information not included).

# Figures
**Main text: 5 figures. Extended Data: 9 figures plus 1 table.** Supplementary Information (not in PDF) holds ablations, prompts, scenario metadata, inter-rater reliability and Supplementary Tables up to 34.

- **Fig. 1, Overview of contributions (orientation plus headline result).** Composite with three unlettered zones, each with a small italic-style subtitle under it: top, full system pipeline schematic (simulated dialogue generator, fine-tuning data mix, RL from human/AI feedback, dialogue agent chain of reasoning, Mx agent with NICE and BMJ guideline icons); bottom left, randomized three-visit study design with clocks marking 2-day gaps; bottom right, a hexagonal radar chart of six management axes, AMIE (pink) enclosing PCP (blue), with no numbers or scales. The radar subtitle is itself a claim (AMIE outperforms PCPs on multiple axes). Figure 1 therefore does three jobs: system, design, and result teaser.
- **Fig. 2, structured reasoning (method and worked example).** Panels a to e: a, Python schema on dark code background; b, full reasoning trace as a tree, with green boxes zooming into c, d, e (analysis, goals, cited plan items). Bold lowercase letters in white squares at panel corners.
- **Fig. 3, randomized study design (orientation).** Schematic only: visit timeline, scenario pack, randomized PCP vs AI arm, guideline corpus, post-questionnaires and specialist evaluation listed as bullet text. No panels, no numbers.
- **Fig. 4, management plan quality (main result).** 3 by 5 grid of small line plots (rows: overall, investigations, treatments; columns: five axes), x axis visit 1 to 3, y axis 50 to 100%. AMIE red circles, PCP blue down-triangles. Exact P values in scientific notation are printed along the bottom of each subplot, only where significant. A dashed grey box groups the two guideline columns, labelled "Use of clinical guidelines". No panel letters; text refers to "Fig. 4, right".
- **Fig. 5, MXEKF performance (secondary result).** Small-multiple stacked bars (y: number of scenarios, 0 to 100; x: visit), two perspectives per axis; pink AMIE preferred at bottom, grey tie in middle, light blue PCP preferred at top, 95% CI error bars. No values printed on bars.
- **Extended Data:** ED1 architecture schematic; ED2 auto-evaluation line plots with shaded 95% CI bands (design optimisation); ED3 to ED5 reasoning traces for fictive patients (worked examples); ED6 rater interface screenshots (a, b); ED7, ED8 stacked horizontal bars per rubric item with asterisks and N per row; ED9 RxQA accuracy bars with values printed inside bars, significance brackets with exact P, dashed random baseline.
- **What is pushed out of main text:** all RxQA results (only ED9), all full rubric distributions, the architecture diagram, ablations, rater UI, example traces. Main text keeps design and the two clinician-rated outcomes.
- **Colour convention** is consistent across the paper: AMIE red/pink, PCP blue, ties or NA grey; darker shade for open-book or stronger rating.
- **Referencing style:** "Fig. 2", "Fig. 2a", "Figs. 1 to 3" (typeset as a range), "Extended Data Fig. 6", "Extended Data Figs. 3 to 5", "Fig. 4, right". Panels lowercase bold.

# Tables
- **No main-text tables.** All comparative numbers live in prose and figures.
- **Extended Data Table 1, Evaluation Rubrics**, two parts (a, b): rows are rubric items, columns Feature, Question, Scale, Options, Assessed by. Part b uses spanning grouping rows (Guideline Use, Preciseness, Memory). Key rubric phrases are set in capitals inside each question. Footnote is one line naming the two parts plus a permission credit for the adapted source.
- No Table 1 of baseline characteristics; participant characteristics (21 PCPs, median years of experience with IQR) are given in Methods prose only.
- Detailed result tables (RxQA P values, LLM comparisons, ablations) are in Supplementary Tables and only pointed to ("Supplementary Table 33 provides detailed results").

# Captions
- **Structure:** bold label title ending with a full stop, then a running paragraph in the same block. ED caption titles use Title Case in one case (RxQA Medication Reasoning Accuracy) but sentence case elsewhere.
- **Length:** about 40 to 190 words; typical 100 to 130. Shortest: ED1, ED6 (about 40). Longest: Fig. 4 (about 190) and ED9 (about 150).
- **Tone:** titles are descriptive labels, not claims. Bodies are descriptive, but some ED captions add interpretive guidance (ED3 flags a missing recommendation as an imperfection; ED5 tells the reader what a latent reasoning error looks like).
- **Content:** panel-by-panel walk (Fig. 2, ED2 by "Row 1", "Rows 2 and 3"); scale definitions and binarisation rule; n per axis and exceptions; test name (two-sided McNemar), FDR correction, P threshold for display; error bar meaning (95% CI for binomial proportions); asterisk legend; how ratings were aggregated (median of three raters). Fig. 4 caption repeats the statistical analysis paragraph of Methods nearly in full, so the figure stands alone.
- **Abbreviations:** inconsistent. ED7 and ED8 expand GMCPQ, PACES, MXEKF; Fig. 5 uses MXEKF unexpanded; Fig. 1 expands nothing new. Main-figure captions rely partly on the text.
- **Table vs figure:** the table title is label only with almost no legend; figure captions carry the statistics.
- Example titles: "Overview of contributions."; "Reasoning and planning under structural constraints."; "Management plan quality."

# Order and organisation
Approximate words (main text plus Methods, about 7,600; legends excluded):
1. Abstract, unstructured, about 265 (outside the count).
2. Introduction, no heading, about 800 (11%): field context, gap (management reasoning poorly evaluated), "Our contributions are summarized in Figs. 1 to 3", then three bullet contributions each pointing to a figure.
3. Results, no "Results" heading, about 1,500 (20%), three label subheadings with bold run-in claim headings inside:
   - Management plan quality: run-ins "AMIE plans non-inferior to PCPs.", "AMIE had more precise recommendations.", "AMIE had superior guideline alignment.", "Ablations of model and agents." (one label among claims).
   - Management Reasoning Empirical Key Features: two claim run-ins (preferred by raters; scores evolved across visits).
   - Medication reasoning accuracy: three claim run-ins (RxQA hard for both; AMIE wins on difficult subset; external knowledge helps both).
4. Discussion, about 1,800 (24%).
5. Conclusion, about 150 (2%).
6. Online content statement, references 1 to 32.
7. Methods, about 3,300 (43%): system (dialogue agent, Mx agent, with run-in subheads), Evaluation, Multivisit OSCE study, RxQA benchmark (numbered build steps), Statistical analysis, Data and Code availability, references 33 to 52.
8. Extended Data figures and table, then Nature reporting summary.

- **Methods last:** the Results open each subsection with a short re-explanation (how many axes, raters, scales, what MXEKF is, closed-book vs open-book) and push detail to SI sections. The contribution bullets and Fig. 1 and Fig. 3 act as the design preview the reader needs before Results.
- **Results ordering:** primary clinician-rated outcome first, ablation note, then secondary rubric (MXEKF), then the separate benchmark. No data description subsection; scenario details live in Methods.
- **Discussion sequence:** restated headline; longitudinal value; preciseness; guideline alignment and adaptability; MXEKF as new rubric; LLM progress and ablation lessons; RxQA contribution; limitations block (about 40% of Discussion); art-of-the-possible caveat; RxQA limitations.
- **Figure distribution:** Figs. 1 to 3 are cited in the Introduction; Fig. 4 serves the whole first Results subsection; Fig. 5 the second; the third has no main figure (ED9 only).
- **Supplementary pointers:** very frequent, parenthetical, numbered: "(Supplementary Information section 11)", "Supplementary Tables 21 to 23", "Extended Data Fig. 2". Results paragraphs often carry two or three such pointers.
- No boxes, key points, research-in-context panel or graphical abstract; Fig. 1 functions as the graphical abstract.
- **Ease of reading:** design preview and consistent colours help; missing Results heading, dense per-visit percentage triplets in prose and jargon used before definition hurt.

# Checklist candidates
- Make Figure 1 a composite overview that shows the system, the study design and a one-glance headline result. [strong]
- Give the study design its own schematic figure when the protocol has multiple visits, arms or rater types. [strong]
- End the Introduction with a numbered or bulleted contribution list, each item pointing to its figure. [strong]
- Keep one colour per arm (model vs comparator) identical across every main and extended figure, and state it in a legend. [strong]
- Print exact P values on the figure only for comparisons that survive multiplicity correction, and say so in the caption. [strong]
- In every results caption state the test, sidedness, correction method, n per group and exceptions, and what error bars mean. [strong]
- Start each caption with a bold descriptive label title, then a paragraph that walks the panels in order. [strong]
- Use small multiples (one subplot per axis or metric) rather than one crowded chart when reporting many rubric items over time. [strong]
- Under label subheadings, use bold run-in claim sentences that state each finding. [strong]
- Move full rating distributions, rater interfaces, example outputs and secondary benchmarks to Extended Data, keeping main figures for design and primary outcomes. [strong]
- When Methods comes last, open each Results subsection with one or two sentences re-defining the scale, raters and n. [strong]
- Include worked examples of model output in Extended Data with captions that point out an error or imperfection. [weak]
- Put the rubric or evaluation instrument in a table with columns for item, question, scale, options and rater type. [weak]
- Expand every abbreviation inside each caption so captions stand alone. [weak; the paper is inconsistent]
- Avoid duplicating the full statistical analysis paragraph in a caption; summarise and point to Methods. [weak]

# Notable deviations
- No main-text tables and no baseline characteristics table at all.
- No explicit "Results" heading; contributions list flows straight into result subsections.
- Fig. 1 radar chart shows a result with no numbers, axes values or uncertainty.
- Main figures 1, 3, 4 and 5 have no panel letters despite multiple subplots; text uses positional references ("Fig. 4, right").
- Captions mix "Table SI.33" with "Supplementary Table 33" styles, and title case vs sentence case.
- Methods (43%) outweighs Results (20%) by more than two to one.
