# Paper
Schmidgall S, et al. AgentClinic: a multimodal benchmark for tool-using clinical AI agents. npj Digital Medicine 2026;9:499; original research Article (benchmark/resource); source: local 12-page PDF read in full, figures inspected visually.

# Figures
Six main figures, all full width, all in the Results pages. No extended data, no supplementary figures, no supplementary file of any kind.

- **Fig. 1 (orientation, workflow schematic plus worked example).** Left: icon-based workflow showing the doctor agent at the centre, colour-coded arrows to measurement, patient and moderator agents, and a tool box (PubMed, Wikipedia-style logos). Right: a speech-bubble example simulation (headache, MRI request, MRI image strip, diagnosis checked against ground truth with a green "CORRECT" box). Figure 1 is the system overview because the paper is a benchmark: the reader must see the agents before any number.
- **Fig. 2 (main result, bar chart, three groups).** Accuracy bars per doctor model on AgentClinic-MedQA (left, sorted descending, with a human physician bar), per patient model (middle), and per doctor model on MIMIC-IV (right). Model names are written vertically inside bars; vendor logos sit above bars; a shared y axis 0 to 60%. A strip under the bars shows which LLM is the doctor and which the patient, with a question-mark icon for the varied role. No numeric values or error bars on the figure; all numbers (with ± values) are in the prose.
- **Fig. 3 (secondary result, paired bar chart).** Static MedQA accuracy (dashed outline, lighter fill) beside AgentClinic-MedQA accuracy (solid) for each model; logos on the x axis instead of tick labels. No numbers on bars.
- **Fig. 4 (robustness, radar charts plus bar charts).** Top: four radar plots (doctor vs patient bias rows by implicit vs cognitive bias columns) of normalized accuracy, GPT-4 green dashed vs Mixtral orange filled. Bottom: three sorted bar charts of patient confidence, compliance and consultation ratings (0 to 10) across bias conditions for GPT-4.
- **Fig. 5 (subgroup results, three radar charts).** Accuracy by language, by specialty and by agent tool, six models in a shared colour legend at the bottom; axis vertices carry icons.
- **Fig. 6 (multimodal result, schematic plus bar chart).** Left: icon schematic of images and context feeding the doctor agent. Right: accuracy bars with error bars for four models, background shaded pink (image given initially) vs blue (image must be requested).

Panel labelling: no letters anywhere. Panels are named by position (Left, Middle, Right, Top, Bottom) in captions, and the text points with "Fig. 2", "Fig. 2 (middle panel)", "the lower panels of Fig. 4". Citation format is "Fig. N" in running text.

Encoding: each model has a fixed colour that is reused across Figs. 2, 3 and 5 only partly (palettes shift between figures); vendor logos act as a second encoding. Comparison of two models in Fig. 4 uses green vs orange; Fig. 6 uses background shading for condition. Error bars appear only in Fig. 6 and are never defined.

Figure citation order in the text is not sequential: Fig. 4 is cited in the first Results subsection (bias description) before Fig. 2.

# Tables
None. The paper has zero tables, main or supplementary. Every quantitative result that a typical clinical-AI paper would tabulate (11 models by accuracy with ± values, per-tool accuracies, per-language and per-specialty accuracies, bias drops) is written out inline as long comma-separated lists in prose, while the figures show the same data without numbers. Model descriptions, tool descriptions and bias definitions, which other papers would tabulate, are prose subsections in Methods.

# Captions
- Structure: bold title sentence, then a short plain-text description in the same paragraph. Positional panel cues are inline: "(Left)", "(Pink)", "*Left*." in italics in Fig. 4.
- Length: about 17 to 75 words; typical about 35 to 45. Fig. 3 is shortest (title plus one claim sentence), Fig. 4 longest.
- Tone: titles are mostly descriptive labels ("Running language agents in AgentClinic.", "Specialist, multilingual, and tool usage."). Two captions add a declarative finding: Fig. 3 states MedQA accuracy does not predict AgentClinic accuracy, and Fig. 4 states GPT-4 was not susceptible to bias while Mixtral was.
- Content: panel roles and colour meaning (Fig. 4 green/orange, Fig. 6 pink/blue). Missing: n per condition, number of cases, definition of error bars or ± values, statistical method, data source details. Abbreviations (CoT, RAG, MIMIC-IV) are not redefined. Captions do not stand alone; the reader needs the text for numbers and setup.
- Example titles: "Accuracy of various doctor language models and human physicians on AgentClinic-MedQA"; "Comparison of accuracy of models on MedQA and AgentClinic-MedQA"; "Specialist, multilingual, and tool usage".
- No tables, so no table-title contrast.

# Order and organisation
Outline with approximate words (total main text about 7,500):
1. Abstract, unstructured (about 185; under 3%).
2. Introduction, unheaded (about 650; 9%), ending in a numbered list of three key contributions.
3. Results (about 3,300; 44%):
   - AgentClinic: a multimodal benchmark for tool-using clinical AI agents (system, biases, datasets, languages; effectively methods)
   - Comparison of models
   - Comparing tools from the Agent Toolbox
   - How does bias affect the diagnostic accuracy of the doctor agent?
   - Bias and patient agent perception
   - Specialist and multilingual cases
   - Human dialogue ratings
   - Diagnostic accuracy in a multimodal environment
   - How does limited time affect diagnostic accuracy?
   - Does the patient language model affect accuracy?
   - Coverage of MedQA versus AgentClinic-MedQA (closes with a numbered-style set of recommendations)
4. Discussion, unheaded subsections (about 1,550; 21%).
5. Methods (about 1,700; 23%): Agent details; Patient perception metrics; Diagnostic accuracy in a multimodal environment; Bias details; Model details; Tool descriptions.
6. Data availability, Code availability, references (52), acknowledgements, contributions, competing interests.

Methods last: the first Results subsection carries the system description, dataset construction, bias seeding and language conversion, so Results opens as a methods section. Later subsections each restate their own setup (N = 20 turns, 120 NEJM cases, rating questions as a numbered list). Methods then partly duplicates this; one Methods subheading repeats a Results heading verbatim.

Results ordering logic: system description, main comparison, tools, bias (accuracy then perception), subgroups (specialty, language), human realism ratings, multimodal extension, ablations (interaction time, patient model), then a mechanistic coverage analysis ending in recommendations. Ordering is roughly by dataset variant, not by importance; the tools subsection cites Fig. 5, which is placed after Fig. 4. Headings are a mix of labels and questions ("How does limited time affect diagnostic accuracy?"); none are claims.

Figure distribution: about one figure per two subsections. Fig. 2 feeds two subsections (model comparison and patient model); Fig. 5 feeds tools and specialty/language subsections; Fig. 4 feeds both bias subsections. Three subsections (human ratings, time, coverage) have no figure and report numbers in prose only.

Discussion sequence: recap of what was built and main findings; a long run of limitations (simplified environment, LLM moderator, rater sample N = 3, data leakage, same-model self-preference, tool abstraction) each paired with future work; comparison with prior benchmarks (AMIE, CRAFT-MD, MedAgents) near the end; one-sentence closing call for dialogue-driven benchmarks.

Supplementary: none; never referenced. Code and data via GitHub under MIT licence.
Boxes, key points, graphical abstract: none. The numbered contribution list in the Introduction plays the highlights role.

Ease of reading: Fig. 1 orients well and question headings make each ablation easy to locate. Hard parts are numbers buried in prose lists with inconsistent formats, figures without values, non-sequential figure citation, and a Results section that mixes setup and findings.

# Checklist candidates
- Make Figure 1 the system or study overview, pairing a workflow schematic with one worked example case. [strong]
- For a benchmark paper, give each dataset variant or ablation its own Results subsection with a short setup recap when Methods comes last. [strong]
- Label every panel with a letter (a, b, c) and cite panels as "Fig. 2b" rather than by position words. [strong; supported by the paper's lack of it]
- Put numeric values (or a table) beside any figure whose numbers the text lists; do not leave long inline number lists as the only source. [strong]
- When reporting more than about five models by more than one metric, use a table with models as rows rather than prose. [strong]
- Define error bars and ± values (SD, SE, 95% CI; bootstrap or not) and n per condition in every caption. [strong]
- Cite figures in numerical order in the text. [strong]
- Keep one fixed colour per model across all figures. [weak]
- End a caption title or the caption with the single takeaway when the figure carries one main finding. [weak]
- Phrase ablation subsection headings as questions only when the subsection answers one question. [weak]
- Close a benchmark Results section with explicit evaluation recommendations derived from the analyses. [weak]
- Report benchmark versus static-exam comparisons as a paired bar chart with consistent fill for each condition. [weak]

# Notable deviations
- No tables at all in a paper reporting 11 models across many conditions; all values are prose lists, which a JAMIA or Lancet Digital Health reviewer would likely flag.
- No supplementary material despite heavy content (prompts, per-case results, rater details).
- Unlettered panels and positional captions, unusual for a Nature-portfolio journal.
- Figures show no numbers and no uncertainty except Fig. 6, whose error bars are undefined.
- Fig. 4 cited before Figs. 2 and 3.
- Inconsistent headline numbers across sections: the abstract and introduction give a 92% relative gain for Llama 3 with the notebook, the Results tools section a 9.4% average gain, and the Discussion 19.7%.
- Results opens with a methods subsection, and a Methods subheading duplicates a Results heading.
- Methods "Model details" reads as vendor description with promotional claims rather than versioned specifications.
