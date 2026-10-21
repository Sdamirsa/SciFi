# Paper

Scherbakov D, Hubig N, Jansari V, Bakumenko A, Lenert LA. The emergence of large language models as tools in literature reviews: a large language model-assisted systematic review. Journal of the American Medical Informatics Association, 2025.

- Journal: JAMIA
- Article type: review (systematic review, PRISMA 2020, OSF registered)
- Word count estimate: about 3,700 to 4,000 words main text (Introduction about 1,100, Methods about 1,075); abstract about 250 to 280 words
- Source URL used: https://pmc.ncbi.nlm.nih.gov/articles/PMC12089777/
- Access note: PMC was reachable but the fetch tool refused long verbatim passages; analysis rests on targeted structural passes, so counts are estimates.

# Global patterns

**Sentence length.** Sample of about 23 sentences across sections: typical range 14 to 32 words, median near 24. Short anchor sentences exist (5 to 10 words, e.g. pointers to supplementary tables). Longest: a 68 word Methods sentence describing the screening vote procedure; Introduction peaks at 42, Discussion at 46. Results sentences are shorter (9 to 30).

**Paragraph length.** Typical paragraph is 3 to 6 sentences, 60 to 130 words. Outliers: one Introduction paragraph about 295 words, one Methods paragraph about 240. Results paragraphs are short (2 to 5 sentences); the 4 Discussion paragraphs are long.

**Voice and person.** Passive dominates Introduction, Methods and Results ("were identified", "were excluded", "was used as"). "We" appears only in the final Introduction paragraph (aims), sparingly in Methods ("our team"), never in Results, freely in Discussion and Limitations ("we do not have information", "We used calibrated LLMs"), and not at all in Conclusion.

**Tense.** Introduction: present for field state, present perfect for trends, past for cited findings. Methods: past throughout. Results: past for findings, present for exhibit pointers ("Figure 2 outlines", "Figure 4A and Table 2 show"); occasional present for descriptive summaries ("is the most frequently mentioned"). Discussion: past for own findings, present for general claims, future and modals for predictions ("will probably", "will require"). Conclusion: present for the general claim, past for what was found.

**Hedging.** Modest and mostly modal: might, could, probably, likely, appears, seemed to. "May" is absent from the Discussion and Conclusion. Hedges cluster around predictions about the future of reviews, not around the paper's own counts. Strong findings carry a number in the same sentence (count plus percentage, or mean plus SD). Predictive claims ("will probably eventually change") carry no evidence anchor.

**Punctuation.** Abstract and Results: no semicolons, colons or dashes; parentheses used for statistics. Introduction: 1 semicolon, no colons, one pair of dashes. Methods: about 15 semicolons, almost all as list separators, a few colons introducing lists. Lists in sentences are built with commas and "and"; longer enumerations become formatted bulleted lists (exclusion criteria, 12 item charting form). Aims are an inline numbered list.

**Abbreviations.** LLM defined in the abstract and again in the Introduction. Introduction defines NLP, AI, ML, NICE, PICO, SVM; Methods defines OSF and IQR. Several used without definition (HIPAA, GPT, BERT, GPT-4o). Some defined terms appear rarely (NICE, PICO, SVM appear essentially once in context). Total distinct abbreviations about 15.

**Numbers and statistics.** Descriptive only, no p values or CIs. Counts with percentages: "79 (45.9%)" in prose or "(n = 60, 34.9%)" in parentheses. Percentages to one decimal, occasionally two (8.14%). Means as "M = 83.07, SD = 10.43" (APA style, two decimals). Abstract rounds to one decimal (83.0%, 86.0%). Numerals used for small counts ("3 most common", "2 reviewers").

**Citations.** Numbered markers at sentence end, after punctuation. One per claim usually, clusters of 2 to 4 as ranges for broader claims. Introduction is citation dense (about 34 markers); Methods cites tools and the PRISMA checklist (about 8). PRISMA 2020 named in Methods, with a PRISMA flow diagram as Figure 2.

**Transitions and flow.** Paragraphs open with topic sentences naming the subject outright, often an exhibit ("Figure 3 shows..."). Few explicit connectives; flow comes from strict topical sequence.

**Tone.** Methods and Results are neutral and procedural. Introduction and Discussion use promotional intensifiers: significant (non-statistical, repeated), remarkable, powerful, notable advancement, exponential rise, overwhelming, democratization, "an obvious choice".

**Word choice.** Plain, low nominalisation, moderate jargon (mostly tool and model names).

# Local patterns by section

**Title.** Descriptive phrase plus colon subtitle naming the design (about 19 words). Main clause frames the topic ("the emergence of..."); subtitle states design and the reflexive method, an LLM-assisted systematic review. No population or claim.

**Abstract.** Structured with JAMIA headings: Objectives, Materials and Methods, Results, Discussion and Conclusion. Moves: aim, methods (databases, month and year, Covidence plus GPT-4o add-on, other AI tools disclosed), results (retrieved and included counts, dominant architecture, true reviews, most automated stages, mean precision and recall by model family), conclusion (numeric extraction limitation, forecast of change). Numbers: 3,788 retrieved, 172 included, 73.2%, 26 (15.1%), 83.0%, 86.0%. No gap sentence; the conclusion is a forecast rather than a restated finding.

**Introduction.** 10 paragraphs, no subheadings, about 1,100 words. Funnel: growth of reviews (with counts from cited bibliometrics), resource burden, existing platforms, human screening error, earlier ML and rule-based automation, limits of those methods, LLMs as the advance, aims. Final paragraph opens with an aim statement ("The review aims to") and lists three numbered aims (summarise current automation, which review types and stages, performance). Design is named; results are not previewed. Example: opening sentence frames abundance of reviews in 18 words.

**Methods.** About 13 paragraphs, no subheadings, ordered: protocol registration and reporting checklist, eligibility (with a bulleted exclusion list), search (databases, fields, date, single reviewer), Covidence plus LLM add-on (three runs, majority vote), human calibration on 100 abstracts and 30 full texts, extraction quality control (threshold of 80% precision triggers manual correction), charting form (12 item bulleted list), disclosure of other AI tools, analysis (frequencies, plots, means and SD), time savings pointer to supplement. Example: "The results are reported using the checklist provided by" PRISMA. Explicit statement that no risk of bias assessment was done. No ethics statement (none needed). Prompts and benchmarks pushed to supplementary tables with short pointer sentences ("Three prompts per phase are detailed in Table S1").

**Results.** No subheadings; 10 short paragraphs; cohort (PRISMA flow) first, then geography, review types, stages, model types, metrics, publication types, pointer to full extraction table. Almost every paragraph opens by naming its exhibit (Figure 2, Figure 3, Figure 4A and Table 2, Figure 4B and Table 2, Figure 5, Figure 6, Table S5). Comparisons use "higher", "lower", "better", "compared to", never "outperformed". Mild interpretation leaks in ("showing its widespread use"). No "we".

**Discussion.** 4 paragraphs, no subheadings. P1 restates the principal finding with "Our LLM-assisted systematic review revealed". P2 states strengths (scale, number of records). P3 compares model families and cites prior work including the authors' own previous review. P4 discusses the absence of journal restrictions on LLM use and perceived publication barriers, with predictive modals ("could eventually be replaced").

**Limitations.** Separate top level section between Discussion and Conclusion, 2 paragraphs, about 200 words. Opens with "We used calibrated LLMs as reviewers", acknowledges possible missed publications and reliance on reported metrics, mitigates through calibration, and advises caution in interpretation.

**Conclusion.** 2 paragraphs, impersonal. First states growth of LLM use in review automation; second contrasts early success with few true LLM-assisted systematic reviews, judges trustworthy AI meta-analysis as hard, and places scoping reviews "well within the capabilities of current or near-future AI". Strength matches a descriptive review: forecasts are hedged with "likely" and "appears".

**Back matter (order).** Author contributions (CRediT roles per author, e.g. "Writing, original draft"), Supplementary material, Funding (grant numbers plus NIH disclaimer that content is the authors' responsibility), Conflicts of interest ("The authors have no competing interests to declare."), Data availability (data in the article, supplementary files and OSF record; open, not controlled), Acknowledgments. The AI use disclosure sits in Acknowledgments and names each tool with the section it drafted (Scite.ai for parts of introduction and discussion, ChatGPT for abstract and results). No code availability heading, though prompts are in the supplement. No ethics heading.

**Figures and tables.** Short noun phrase titles ("Flow diagram of the systematic review process.", "Types of automated review.") followed, when needed, by a sentence on panels (A), (B) and inclusion rules (only models in 2 or more studies). Abbreviations handled unevenly: Table 2 has a full legend; Figure 5 and Figure 6 use LLM, GPT, BERT without expansion. Table 1 holds the full Boolean search string. Figure 1 is a workflow diagram of the authors' own tool.

**Review-specific mapping.** A descriptive census: who (country), what (review type, stage), how (model), how well (metrics), one plot per question plus a master summary table. The review is itself LLM-assisted, so Methods doubles as a case study.

# Checklist candidates

- Use the journal's structured abstract headings exactly (for JAMIA: Objectives, Materials and Methods, Results, Discussion and Conclusion). [strong]
- State the database list and the search month and year in the abstract methods. [strong]
- Give retrieved and included counts in the first abstract result sentence. [strong]
- Report counts with percentages together, as "79 (45.9%)" or "(n = 60, 34.9%)". [strong]
- Use one decimal place for percentages throughout. [weak]
- Report means with SD in a consistent format and decimal precision. [strong]
- Name the reporting guideline and registration in the first Methods paragraph. [strong]
- Include a PRISMA flow diagram as the first Results figure and open Results with it. [strong]
- Open each Results paragraph by naming the figure or table it describes. [strong]
- Use present tense for exhibit pointers and past tense for findings. [strong]
- Avoid "we" in Results; reserve first person for aims, Discussion and Limitations. [strong]
- End the Introduction with an explicit, numbered list of aims. [strong]
- State explicitly when a standard step was not done (for example, no risk of bias assessment). [strong]
- Move prompts, benchmarks and full extraction tables to supplementary material with one line pointers. [strong]
- Disclose every generative AI tool used, naming the tool and the section or task it served. [strong]
- Put Limitations in its own section before the Conclusion. [strong]
- Open the Discussion with a one sentence restatement of the principal finding. [strong]
- Hedge forecasts with "likely", "could" or "probably"; keep counts unhedged. [strong]
- Define every abbreviation at first use and define it again in the main text after the abstract. [weak]
- Expand abbreviations in every figure and table caption or legend. [weak]
- Use CRediT roles for author contributions. [strong]
- Use bulleted lists for eligibility exclusions and charting form items rather than long sentences. [strong]

# Notable deviations

- Promotional wording in Introduction and Discussion ("remarkable", "powerful", "notable advancement", "democratization"), and non-statistical use of "significant", which most clinical journals discourage.
- A 68 word Methods sentence and a 295 word Introduction paragraph; well beyond common limits.
- Several abbreviations used without definition (GPT, BERT, HIPAA) and others defined but used about once (NICE, PICO, SVM).
- Inconsistent decimal precision (one decimal mostly, two in places, and abstract rounding to 83.0% versus M = 83.07 in text).
- Mild interpretation inside Results.
- Abstract conclusion is a forecast rather than a restatement of the main finding.
- Many semicolons in Methods (used as list separators) while other sections avoid them, so semicolon rules here are section dependent.
- AI use disclosure placed in Acknowledgments rather than a dedicated heading; no code availability statement despite a custom tool.
- Statistics written APA style (M =, SD =), unusual for clinical journals that prefer "mean (SD)".
