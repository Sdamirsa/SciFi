# Paper

Ferber D, El Nahhas OSM, Wolflein G, Wiest IC, Clusmann J, Lessmann ME, Foersch S, Lammert J, Tschochohei M, Jager D, Salto-Tellez M, Schultz N, Truhn D, Kather JN. Development and validation of an autonomous artificial intelligence agent for clinical decision-making in oncology. Nature Cancer 2025.

- Journal: Nature Cancer 6, 1337 to 1349 (August 2025); doi:10.1038/s43018-025-00991-6; open access, CC BY 4.0.
- Article type: original research (Article).
- Word count estimate: abstract about 150 words; main text (introduction, results, discussion) about 4,000; Methods about 2,700; 54 references; 5 main figures, 1 Extended Data figure, no main tables.
- Source: local PDF (13 article pages, Extended Data Fig. 1, 3 page Reporting Summary).

# Global patterns

**Sentence length.** Sample of 20 sentences across sections: range 5 to about 60 words, typical 20 to 35. Shortest: "Our work has several limitations." (5). Longest: the final Discussion sentence listing deployment challenges (interoperability, GDPR and HIPAA, liability, regulatory approval, validation) at about 60 words. Paragraphs: 3 to 8 sentences, about 80 to 200 words in Results and Discussion; Methods paragraphs reach about 250 words.

**Voice and person.** Heavily active with "we" throughout ("we compiled", "we show that", "we decided to only focus on GPT-4"). "Our agent", "our pipeline", "our approach" are frequent and possessive. Passive appears mainly in Methods data handling and the Statistics paragraph ("No data were excluded in the analysis").

**Tense.** Introduction mixes present for the field ("the future of medical AI is multimodal") and present for the study's own actions ("we build and evaluate", "we devise a benchmark strategy"), then slips to past ("we designed a blinded manual evaluation"). Results use past for procedures and observations, present for reporting verbs ("We show that GPT-4 alone only provided 30.3%"). Methods use past for what was done and present for how the system works ("GPT-4 can send the HUGO symbol"). Discussion is present and future ("we anticipate", "we envision").

**Hedging and certainty.** Claims are strong. Verbs: demonstrate, show, enable, establish, address. Adverbs and intensifiers: drastically, substantially, greatly, highly, remarkably, far superior, immense potential. Hedges are reserved for future work (may, might, could, potential). Strong claims are usually anchored to a number or figure in the same sentence (87.2% versus 30.3%, "(Fig. 2b)"), but summary sentences ("Overall, our results demonstrate...") restate them without the number. The abstract's "establishing a robust foundation for deploying" exceeds what n = 20 supports, and the limitations paragraph later calls it a proof of concept.

**Punctuation.** Parentheses are the dominant device: abbreviation definitions, figure pointers, counts, glosses ("(so-termed hallucinations)", "(providing examples to the model)"). Colons are rare in main text; semicolons rare (mainly before "thus" or "however"). No dashes in prose. In-sentence lists use "A, B and C" with no serial comma (Nature house style). Single quotation marks flag coined metric names ('tool use', 'completeness', 'reasoning engines').

**Abbreviations.** About 30 defined. AI is defined in the abstract and again in the introduction. LLM, RAG, MSI, MSS, API, MRI, CT, TCGA, 3D are defined at first main text use. GPT-4V is defined in Results and again in Methods. Some are never expanded (KRAS, BRAF, RECIST, GDPR, HIPAA, NSCLC, HUGO, FOLFOX), and GMAI appears in the Discussion without definition. Figure captions reuse abbreviations without redefinition. TEI and GROBID are defined once and barely reused.

**Numbers and statistics.** Results are proportions only: count over denominator with one decimal percentage, e.g. "223 (91.0%) of these to be factually correct". Figures show "87.5% 56/64". No confidence intervals, no p values, no inter-rater agreement statistic. Majority vote of four raters, ties resolved to the worst category. Thousands take commas; small counts are spelled out ("four human experts"). A grammatical slip appears ("a 87.2% success rate").

**Citations.** Nature superscripts, placed directly after the named entity mid-sentence (MedSAM, OncoKB, "Zakka et al.") or at sentence end before the period. When a citation follows a number or model version the form "(ref. 2)" is used. Usually one reference per claim, rarely two. No reporting guideline (TRIPOD, TRIPOD-LLM, CONSORT-AI) is named; the Nature Portfolio Reporting Summary stands in.

**Transitions.** Paragraphs open with a topic sentence, often signposted by connectives: However, Additionally, Moreover, Furthermore, Similarly, Next, Lastly, Overall, In summary. Results subsections are ordered by ordinals (First, Second, Thirdly, Fourth: inconsistent form). Most Results subsections close with an "In summary," or "Overall," sentence restating the claim. The introduction moves known (LLM capability) to limitation (generalist models, regulation) to prior fix (RAG, agents) to gap (single task benchmarks) to what we did.

**Tone.** Noticeably promotional for a Nature title: "remarkable advancements", "drastically improved", "Remarkably,", "far superior explainability", "immense potential", "within reach", "demonstrate the superiority".

**Word choice.** Moderate nominalisation in Methods ("the conversion of raw text data", "the deployment of these tools"). Jargon density is high but most technical terms get a parenthetical gloss for a clinical readership (embeddings, dense retrieval, hybrid search, few-shot prompting). Inflated verbs recur (delineate, encompass, leverage, synergize).

# Local patterns by section

**Title.** Descriptive phrase, 14 words, no colon. Pattern "Development and validation of [system] for [task] in [domain]". Names the method (autonomous AI agent) and domain (oncology); does not name design, sample, or that cases are simulated.

**Abstract.** Unstructured single paragraph, about 150 words, 6 sentences. Moves: context in one sentence (complexity of oncology decisions), what we built (GPT-4 plus named tools), evaluation set (20 multimodal cases), three headline percentages, comparison against baseline (30.3% to 87.2%), broad conclusion. No explicit gap sentence. Example: "Evaluated on 20 realistic multimodal patient cases" opens the results sentence.

**Introduction.** No heading (Nature style). About 7 paragraphs. Funnel: LLM capability and USMLE pass; multimodality as the future; doubts that generalist models suffice plus a regulatory argument (single purpose devices); RAG and fine-tuning as partial fixes, then agents outside medicine; "In this study, we build and evaluate an AI agent" with a full tool inventory; benchmark gap (single task, text only, closed Q and A); final paragraph states dataset (20 cases), two-stage process, blinded evaluation by four experts on three areas, and points to Fig. 1 and Methods. Results are not previewed numerically.

**Results.** Four subsections with declarative claim headings ("Tool use and retrieval improve LLM responses", "Radiology tools improve GPT-4's treatment accuracy"). Opens with the baseline comparison rather than a cohort description. Each paragraph maps to a figure or Supplementary Note; qualitative worked examples (patients G, W, X) interleave with counts. Interpretation is not avoided: evaluative phrases ("These findings are promising") and design decisions ("we decided to only focus on GPT-4") sit inside Results. Comparison phrasing: "Compared to GPT-4 alone" and "only provided 30.3%... However, our agent's responses achieved".

**Methods.** Ethics statement first (no confidential data, Declaration of Helsinki, local committee number). Then: data sources; PDF extraction; RAG indexing; tools; retrieval and generation; open-weights benchmarking; model specifications (model identifiers, temperatures); case generation; human evaluation definitions; "Statistics and reproducibility" paragraph in Nature template language (no sample size calculation, no randomisation, blinding status, n = 1 run per case, model deprecation as reproducibility threat). Engineering detail is high; statistics thin.

**Discussion.** First paragraph opens "Our results demonstrate that combining..." and restates the GPT-4 alone deficit, then argues advantages of a tool-based design over a generalist foundation model (updating, regulation, hallucination). Limitations begin in paragraph two: "Our work has several limitations. The most notable is the small sample size", mitigated by a feasibility reason and reframed as proof of concept. Limitations and future work then run across about 10 short paragraphs chained by Moreover, Additionally, Next, Lastly. Closes with a visionary "To summarize, in the near future, we envision" paragraph and a deployment challenges paragraph that ends on clinicians keeping final authority. No separate Conclusion heading.

**Back matter.** Order inside Methods: Statistics and reproducibility, Reporting summary ("Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article."), Data availability, Code availability. Then References, Acknowledgements (funding by author initials with grant numbers, NHS disclaimer, and an AI-use disclosure citing the COPE position, GPT-4 for spelling and grammar), Author contributions (narrative by initials, not CRediT), Competing interests (named companies per author, closing "The remaining authors declare no competing interests."), Additional information. Data availability is open: images available from URLs in the Supplementary Information, TCGA cited, "Source data are provided with this paper." Code on GitHub with README pointer.

**Figures.** Caption starts with a bold title (descriptive, or a claim as in "Tool use and RAG improves LLM performance"), then panel letters in bold lower case with descriptions. Captions are long (about 200 words) and carry metric definitions and interpretation. Numbers in figures show both percentage and n/N. Abbreviations are not redefined in captions.

# Checklist candidates

- Report every proportion as count over denominator with a one decimal percentage, in text and on the figure. [strong]
- Give each Results subsection a declarative heading that states the finding. [strong]
- Tie each headline claim to a figure panel or supplementary item in the same sentence. [strong]
- Place the ethics approval statement, with committee name and number, as the first paragraph of Methods. [strong]
- State exact model identifiers, API endpoints, temperature and other hyperparameters in a dedicated model specifications subsection. [strong]
- Define each evaluation category (correct, wrong, harmful; citation correct, irrelevant, wrong) operationally in Methods, including the unit of analysis and the tie rule. [strong]
- Include a Statistics and reproducibility paragraph covering sample size rationale, randomisation, blinding, exclusions and repeated runs. [strong]
- Report how often proprietary model refusals occurred and how they were handled. [weak]
- Gloss technical AI terms in parentheses at first use for a clinical audience. [strong]
- End the introduction with the study design: dataset, process, raters, outcome domains, and a pointer to the overview figure. [strong]
- Open the limitations with the most important limitation named explicitly, then state its consequence for interpretation. [strong]
- Disclose any AI use in writing in the Acknowledgements, citing the journal or COPE policy. [strong]
- Define an abbreviation at first use in the abstract and again at first main text use. [weak]
- Expand every gene, regulation and criteria acronym at first use (RECIST, GDPR, HIPAA, NSCLC). [weak, paper fails this]
- Provide uncertainty (confidence intervals) and inter-rater agreement for rater based outcomes. [weak, paper omits]
- Name the applicable reporting guideline (e.g. TRIPOD-LLM) in Methods. [weak, paper omits]
- Keep the abstract conclusion at the strength of the design (proof of concept for n = 20 simulated cases). [weak, paper overclaims]

# Notable deviations

- Promotional and intensified vocabulary (drastically, remarkably, immense potential, far superior, within reach) in a Nature journal; do not treat this as a model for npj Digital Medicine or Lancet Digital Health.
- Abstract conclusion claims a "robust foundation for deploying" while the Discussion calls the work a proof of concept; mismatch in claim strength between sections.
- No confidence intervals, p values, or inter-rater agreement despite four raters; Statistics paragraph asserts normality was assumed without any test being used.
- No reporting guideline named; relies on the Nature Portfolio Reporting Summary instead.
- Interpretation and design decisions appear inside Results; evaluative sentences ("These findings are promising") and "In summary" closers in each Results subsection.
- Figure captions contain results interpretation and value judgments, not only description.
- Inconsistent ordinals (First, Second, Thirdly, Fourth) and non-idiomatic wording ("Contrarily", "answered sophistically").
- Limitations are spread across many short paragraphs that merge with future work rather than one consolidated limitations paragraph.
