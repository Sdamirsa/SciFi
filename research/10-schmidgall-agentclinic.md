# Paper

Schmidgall S, Ziaei R, Harris C, Kim JW, Pontes Reis E, Jopling J, Moor M. AgentClinic: a multimodal benchmark for tool-using clinical AI agents. npj Digital Medicine 2026;9:499. doi:10.1038/s41746-026-02674-7.

- Journal: npj Digital Medicine (Nature portfolio, published in partnership with Seoul National University Bundang Hospital). Received 19 April 2025, accepted 14 April 2026 (about one year in review).
- Article type: original research ("Article"), benchmark/resource paper. No tables; six multi-panel figures.
- Word count estimate: abstract about 185 words; main text (intro, results, discussion, methods) about 7,500 words; 52 references.
- Source used: local PDF (12 pages), text extracted with pypdf and read in full.

# Global patterns

**Sentence length.** Sample of 20 sentences across sections: range 9 to 55 words, typical 18 to 32, median about 25. Longest sentences are in the contribution list and in explanatory hedged passages (for example the GPT-4 "over-aligned" explanation, about 55 words). Paragraphs run 4 to 9 sentences, roughly 100 to 220 words; Methods model paragraphs are shorter (3 to 5 sentences).

**Voice and person.** Heavy first-person active "we": "Here, we introduce", "We find", "We evaluate", "we recommend". "We find" opens many results sentences. Passive appears mainly in Methods descriptions of agents and data construction ("are converted ... and then manually corrected by native speakers") and in the patient perception metrics subsection, which reads as reviewer-response text.

**Tense.** Present for framing, benchmark description and most findings ("We find that ... is considerably more challenging"). Past for specific numbers and model behaviour ("Claude 3.5 achieved", "GPT-3.5 experienced decreased performance"). Tense switches within single paragraphs (present "find" next to past "showed"). Present perfect for prior literature ("Previous work has indicated", "have demonstrated").

**Hedging and certainty.** Explanations are hedged with stacked modals: "likely due to", "possibly due to", "may suggest", "might be due to", "plausibly", "We suspect". Claims of effect use "find", "show", "reveal", "demonstrate". The word "significantly" is used repeatedly with no statistical test reported, so "significant" is descriptive, not inferential. Strong claims are usually tied to a figure callout in the same sentence ("(Fig. 5)"), less often to a number with uncertainty.

**Punctuation.** Parentheses are very frequent: examples ("e.g., temperature, blood pressure, EKG"), absolute values beside normalised ones, model version strings. Colons introduce lists and long inline enumerations of model results. Semicolons are rare but present. Em dashes appear a handful of times for appositive definitions (coverage, StatPearls). Inline lists use serial (Oxford) commas. Numbered lists are used inside Introduction, Results and Methods (contributions, patient questions, rating axes, experiential learning steps).

**Abbreviations.** LLM defined in the abstract and again in the first introduction paragraph. Many are defined but used once or twice (OSCE, SMoE, DPO, WBC, PE). RAG is used in Results and Introduction but formally expanded only in the Discussion and again in Methods. CoT is expanded in a Results subsection list. Several are never expanded (MIMIC-IV, EKG, MRI, CT, NEJM before first full use, CBC, Hct). Density is high: about 25 distinct abbreviations, plus many model names.

**Numbers and statistics.** Accuracy given as percentage with "±" (for example "62.1% ± 3.3") but the dispersion measure is never named and the % sign is applied inconsistently in the same sentence. Decimal places vary from 0 to 2 (52%, 42.9%, 11.21%). No confidence intervals, no p values, no denominators beside most percentages. Human raters described with "N = 20" and "N = 3". Normalised accuracy reported with the absolute change in parentheses, a useful pairing. Relative improvement ("up to 92%") headlines the abstract while the Discussion reports 19.7% for the same model, an internal inconsistency.

**Citations.** Numeric superscripts, usually one per claim, placed at clause end or directly after a named dataset or benchmark (MIMIC-IV, AMIE, SAPS). Up to three grouped for LLM-as-judge validity. Many preprints and conference papers. No reporting guideline cited (no TRIPOD-LLM, no CLAIM), no ethics or IRB statement despite MIMIC-IV data and clinician raters.

**Transitions and flow.** Paragraphs open with a topic sentence, often signposting: "Here, we discuss", "In this section we describe", "We now focus on", "We also explore". Linking words are simple: "However", "Additionally", "Furthermore", "In contrast", "Overall", "Notably". The known to unknown to what-we-did funnel is compressed into two paragraphs before "In this work, we introduce".

**Tone.** Mildly promotional and narrative. Uses "Strikingly" in the abstract, "stark differences", "Interestingly", "profound effect", "state-of-the-art", "exceptional performance", and claims the work "advances the field". Model descriptions in Methods repeat vendor-style claims ("superior performance"). Not blog-like overall, but more evaluative than Lancet or JAMIA style.

**Word choice.** Computer-science register: "leverage", "backbone", "seeding biases", "emergent", "cross-model communication". Moderate nominalisation. Clinical terms are plain. Some typos and duplications survive (a model listed twice, "the the", "nine specialties" followed by a list of eight).

# Local patterns by section

**Title.** Colon form: coined benchmark name, then descriptive phrase naming the object (benchmark), modality (multimodal) and target (tool-using clinical AI agents). 10 words. No design or population terms.

**Abstract.** Unstructured, single paragraph, about 185 words, no subheadings. Moves: importance ("is crucial to assessing their potential clinical utility"), gap (static question-answering "does not accurately depict" sequential decisions), aim with "Here, we introduce", scope (nine specialties, seven languages), three findings each opened by "We find", "we observe", "we see", one headline number ("up to 92% relative improvements"), and a closing sentence listing extra analyses instead of a conclusion. No sample sizes, no uncertainty.

**Introduction.** No heading (npj format). Three prose paragraphs, then a numbered list of three contributions. Funnel: grand aim of AI, LLM exam progress with dated numbers, access argument; then "However" limitations of static multiple-choice; then "In this work, we introduce". Contributions preview results ("We find that doctor and patient agent biases can lower diagnostic accuracy"), so results are fully previewed.

**Results.** Placed before Methods. Opens with a subsection describing the benchmark design and data construction (methods content inside Results). Ten subsections, several titled as questions ("How does bias affect the diagnostic accuracy of the doctor agent?", "Does the patient language model affect accuracy?"). Each subsection maps to a figure panel; there are no tables, so long strings of model results are listed inline after a colon. Interpretation is mixed into Results freely ("likely because the patient is less willing to share information"), qualitative dialogue snippets are quoted as evidence, and the section ends with explicit recommendations ("First, performance should not be assessed against a single patient agent model").

**Discussion.** Paragraph 1 summarises principal findings with counts (215 agents, 260 specialty cases, 749 multilingual cases, 23 biases). Paragraphs 2 to 4 (about half the Discussion) are limitations: LLM moderator (mitigated by citing over 80% LLM-human agreement), LLM measurement agent hallucination, small clinician sample, data leakage (argued away by the interactive format), self-preference between same-model agents, untested moderator sensitivity, abstraction of tool commands ("this simplification limits ecological validity"). Future work is woven into each limitation. Comparison with prior benchmarks (AMIE, SAPS, CRAFT-MD, MedAgents) comes late, framed as what others "lack". Closing paragraph uses "we believe" and "we take a step towards", a modest restatement.

**Methods.** Order: agent details, patient perception metrics, multimodal diagnostic accuracy, bias details, model details, tool descriptions. Agent prompts are quoted verbatim (moderator instruction). Model versions given for OpenAI models only (for example gpt-4-0613); no temperature, seeds, number of runs or hardware. No statistics subsection; how "±" was computed is not stated. The patient perception subsection openly states no semantic anchors and no reliability analysis were done, and directs readers to relative rather than absolute values. No ethics, consent or reporting-guideline statement.

**Back matter.** Order: Data availability, Code availability, Received/Accepted dates, References, Acknowledgements (contains funding grant number plus a standard funder-role disclaimer), Author contributions (initials, free text, not CRediT), Competing interests ("The authors declare no competing interests."), Additional information (correspondence), Open Access licence. Data availability: benchmark open under MIT licence on GitHub; MIMIC-IV-derived data available on request after PhysioNet training (controlled access). Code availability: code, prompts and evaluation scripts under MIT licence. No separate Funding or Ethics heading.

**Figures and tables.** Caption form "Fig. n | Bold title." followed by panel descriptions keyed by position in parentheses ((Left), (Middle), (Right), (Top), (Bottom)) or colour ((Pink), (Blue)). Some captions state a finding ("GPT-4 accuracy was not susceptible to biases"). Abbreviations and the meaning of error bars are not defined in captions.

# Checklist candidates

- Use a colon title: coined resource name, then a descriptive phrase naming object and target use. [strong]
- Open the abstract with importance, then a one-sentence gap, then "Here, we introduce". [strong]
- Report each abstract finding in a sentence starting "We find" or "We observe". [strong]
- End the Introduction with a numbered list of contributions, each stating a finding. [strong]
- Define an abbreviation at first use in the abstract and again at first use in the main text. [weak]
- Define every abbreviation before its first use, not later in the Discussion or Methods. [weak]
- Pair a relative or normalised metric with the absolute values in parentheses. [strong]
- Attach a figure callout to every quantitative results sentence. [strong]
- Name the dispersion measure behind every "±" and use a consistent number of decimals. [weak]
- Reserve "significant" for results backed by a stated statistical test. [weak]
- Use question-form subheadings in Results when each subsection answers one experimental question. [strong]
- Open the Discussion with a one-paragraph summary of what was built and found, with counts. [strong]
- Pair each limitation with a mitigation argument or a concrete future-work item. [strong]
- State explicitly when a metric is simulated and should not be read as human perception. [strong]
- Quote key agent prompts verbatim in Methods so the evaluation is reproducible. [strong]
- Give exact model version strings for every evaluated model. [weak]
- Give a Data availability statement that names the licence and the controlled-access route for restricted source data. [strong]
- Release code, prompts and evaluation scripts under a named open licence. [strong]
- Include a funder-role disclaimer in the acknowledgements. [strong]
- Check that every number repeated across abstract, results and discussion matches. [weak]

# Notable deviations

- Results before Methods, with benchmark construction described inside Results: Nature-portfolio convention, not JAMIA or Lancet style.
- No statistical testing, no confidence intervals, no p values, and an undefined "±"; "significantly" used descriptively. Do not copy for clinical journals.
- No ethics or IRB statement and no reporting guideline (TRIPOD-LLM or similar) despite MIMIC-IV and clinician raters.
- Interpretation, speculation ("We suspect") and prescriptive recommendations appear in Results rather than the Discussion.
- Promotional adverbs and adjectives ("Strikingly", "profound", "exceptional", "state-of-the-art") that stricter clinical journals would cut.
- Internal inconsistencies (92% vs 19.7% improvement, nine specialties listing eight, six vs seven languages, a duplicated model) survived review; a cautionary example for consistency checks.
- Author contributions in free text rather than CRediT; funding sits inside Acknowledgements without its own heading.
- Occasional em dashes and long numeric run-on sentences listing a dozen model results after a colon instead of a table.
- Limitations occupy roughly half of the Discussion and are interleaved with future work, rather than a single bounded limitations paragraph.
