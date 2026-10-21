# Paper

Gu B, Desai RJ, Lin KJ, Yang J. Probabilistic medical predictions of large language models. npj Digital Medicine. 2024.

- Journal: npj Digital Medicine, 2024;7:367. DOI 10.1038/s41746-024-01366-4. PMID 39702641.
- Article type: original research (computational benchmarking study).
- Word count estimate: about 3,100 words of main text (abstract about 118, introduction about 840, results about 1,270, discussion about 850, methods about 1,100), plus 3 figures and 3 tables.
- Source used: arXiv preprint https://arxiv.org/pdf/2408.11316 (same title, authors and section order as the npj article). Nature and doi.org failed to load, PubMed and PMC were blocked by robots rules, and Europe PMC and arXiv HTML were rate limited. Wording may differ slightly from the typeset version. The fetcher would not return long verbatim passages, so the analysis rests on section by section structural extraction (counts, opening words, punctuation and hedge inventories).

# Global patterns

**Sentence length.** Across a sample of about 20 sentences from all sections, typical sentences run 18 to 35 words. Abstract sentences are 15 to 28 words. Results sentences are longer, averaging about 27 words, with several between 38 and 56 words; the longest observed is about 74 words (introduction paragraph 4, a definition plus worked example). The contributions statement closing the introduction is a single sentence of about 77 words.

**Paragraph length.** Mostly 3 to 7 sentences and 70 to 240 words. Results paragraphs average about 125 words; discussion paragraphs 75 to 180 words. One introduction paragraph is a single sentence.

**Voice and person.** "We" is used freely but not densely. It is absent from the opening background paragraphs, then clusters where the authors state aims (introduction paragraph 5 uses "we" in all four sentences), make design choices in Methods ("we select", "we convert", "we swap"), and voice an interpretation in Results ("we find", "we observe", "we argue", "we propose"). Passive voice carries tool use and metric description ("are used as the evaluation metrics").

**Tense.** Present tense dominates everywhere, including Methods and Results ("This study is conducted on five datasets"; "The AUROCs of the large LLMs ... are"). Present perfect is used for the literature ("has been widely adopted", "Recent work has shown"). Past tense is rare: one stray "evaluated" in the aim paragraph and "We compared" in the abstract. This is unusual for a clinical journal.

**Hedging and certainty.** Light hedging with "can", "may", "could", "suggests", plus quantity qualifiers ("mostly", "largely", "generally", "for most LLMs", "in some cases"). Strong verbs ("demonstrate", "show", "underscores") appear in the discussion summary. Results contain a few absolutes ("always", "consistently") and evaluative words ("questionable", "overly"). Claims in Results are tied to a table or figure in the same sentence or paragraph, not to numbers in the prose.

**Punctuation.** Colons and semicolons are almost absent from prose (one semicolon in the introduction, none in Results or Discussion). Parentheses are the main device: abbreviation definitions, figure and table pointers, "e.g." and "i.e." clauses, and paired numbers such as "(85.2% VS 93.0%)". One em dash in the whole discussion. In-sentence lists use commas with "and"; the contributions are listed inside one long sentence rather than as bullets.

**Abbreviations.** Moderate density (about 15 defined terms: LLM, AI, CoT, RAG, AUROC, AUPRC, MMLU, USMLE, MCMLE, MGB, SDoH and dataset subsets). LLMs is defined in the abstract and again in introduction paragraph 2. RAG is defined and never reused; AUROC and AUPRC are defined in the aim paragraph and then used throughout without redefinition in Methods. Several are used without definition (APIs, EHR, IRB, GPU, COVID). Captions do not redefine abbreviations.

**Numbers and statistics.** The prose carries few numbers. Results state percentages ("less than 10%", "78.6%", "a 50% imbalance") and paired comparisons in parentheses; AUROC and AUPRC values appear only in tables as mean ± standard deviation across three temperature runs, with an asterisk footnote for one-sided paired t test p < 0.05. No confidence intervals or bootstrap anywhere. Small counts are spelled out in the abstract ("six", "five"); dataset sizes appear as digits with commas in Methods.

**Citations.** Superscript numeric, placed both mid-sentence (directly after the claim or term, e.g. after "rarely") and at sentence end, usually in groups of two or three. The introduction is heavily cited (paragraphs 1 to 3); the aim and contribution paragraphs carry none. Results cite only once. No reporting checklist (TRIPOD, TRIPOD-LLM, etc.) is named.

**Transitions.** Paragraphs open with a topic sentence naming the object of the paragraph ("Generative AI models, especially...", "Probabilities have been estimated in the literature..."). Explicit contrast connectors drive the funnel: "However" in the abstract, "On the other hand" to pivot between two families of methods, "In this study, we" to turn to the aim. Results paragraphs open with the metric or comparison being reported ("The AUROCs of the large LLMs and their...").

**Tone.** Mostly sober; no "revolutionary", "groundbreaking" or "unlock". Mild intensifiers occur ("extensively examine", "delved into", "crucial", "shown promise").

**Word choice.** Moderate nominalisation ("reliability", "discrepancy"). Jargon is dense, but the key concepts (explicit vs implicit probability) are coined once and reused consistently. Some non-native phrasing ("open-weighted", "VS" in capitals).

# Local patterns by section

**Title.** Descriptive noun phrase, 7 words, no colon, no claim, no design or population named. Names the concept (probabilistic predictions) and the model class.

**Abstract.** Unstructured, one paragraph, about 118 words, 6 sentences. Moves: background (LLMs "have shown promise"), problem opened with "However", limitation of the explicit approach, aim ("We compared explicit probabilities from text generation to..."), main result with scale ("Across six advanced open-source LLMs and five medical datasets"), then moderator plus call for caution. No numeric results, no metrics values.

**Introduction.** Six paragraphs, about 840 words. Funnel: (1) why calibrated probabilities matter clinically, discriminative models give them naturally; (2) LLMs are capable but generative outputs lack native probabilities, rarely evaluated in health care; (3) defines explicit probability with a prompt example and doubts its reliability; (4) "On the other hand" defines implicit probability, with its practical constraints (proprietary APIs, complex prompts); (5) aim and design ("In this study, we extensively examine the reliability"), metric choice, and a preview of the finding; (6) one-sentence contributions list ("The contributions of this work include a large-scale..."). Results are previewed twice.

**Methods.** Placed after Discussion (npj format). Subsections: Data Source; Experiment Setting; Prediction and Probability Extraction; Evaluation; Imbalanced Datasets Analysis; Sensitivity Analysis. The ethics statement (IRB protocol number, consent waived for an observational study) sits inside Data Source, not in its own subsection. Model names include exact versions and parameter sizes; hardware, max tokens, temperatures (0, 0.3, 0.7) and library functions are given. The statistics description is folded into Evaluation and Experiment Setting (mean and SD over three runs, one-sided paired t test). Prompts are pushed to a supplementary table. Each subsection opens with a purpose clause ("To ensure the robustness of our results, we...").

**Results.** An unheaded opening paragraph reports instruction-following and invalid output rates (a data quality check, akin to a cohort description). Then five headed subsections mirroring the Methods analyses. Each paragraph maps to a table or figure named in its first or second sentence. Comparisons are verbal ("much smaller", "consistently higher") with values left to tables. Interpretation is not avoided: most paragraphs end with a causal or mechanistic explanation ("can be explained by"), and one says "we argue" about overconfidence.

**Discussion.** Seven paragraphs, about 850 words, no subheadings. (1) Two-sentence summary ("This study investigates the probabilistic prediction of LLMs..."); (2) why probability estimation matters clinically; (3) findings linked to prior work and mechanism, heavily cited; (4) implications and future methods ("The flaw of the explicit probability underscores the need"); (5) recent work on inference internals, more future work; (6) a dedicated limitations paragraph opening "There are several limitations in our study", about 130 words, listing scope limits without mitigation; (7) conclusion restating findings at moderate strength, ending that the work "informs future studies" on trustworthiness.

**Back matter.** Order: Data availability; Code availability; Acknowledgements (carries funding); Author contributions; Competing interests. Data availability distinguishes public benchmarks from a controlled institutional dataset available on reasonable request with institutional permission. Code: a public GitHub URL. Funding sentence names the NIH grant number and states that funders had no role in design, collection, analysis, interpretation or publication. Author contributions are initials-based narrative, not CRediT, with "All authors reviewed and approved" and a named guarantor ("takes responsibility for the integrity of the work"). Competing interests: standard "The authors declare no competing interests." No reporting summary mentioned in the preprint.

**Figures and tables.** Captions begin with a short noun-phrase title ("AUROCs of the large and small LLMs."), then panel descriptions (a, b) and notes; 20 to 55 words. Table notes explain boldface and the significance asterisk. Abbreviations are not expanded in captions.

# Checklist candidates

- Coin a name for each competing approach (here explicit vs implicit probability), define it once with an example, and use the exact term everywhere after. [strong]
- Open the abstract's problem sentence with "However" after one background sentence, then state the aim with "We compared". [strong]
- End the introduction with an aim paragraph that names the number of models, datasets and the metrics. [strong]
- Keep background paragraphs free of "we"; switch to "we" for the aim, design choices and interpretations. [strong]
- Mirror Results subsections on Methods subsections, using identical headings. [strong]
- Name the figure or table in the first or second sentence of each Results paragraph. [strong]
- Report a data quality or validity check (invalid output rate) before the main results. [strong]
- Report model names with exact version strings, parameter counts, decoding temperature, max tokens and hardware. [strong]
- Place the IRB approval number and consent waiver in the data source subsection. [strong]
- Write a dedicated limitations paragraph near the end of the Discussion, opening with an explicit signpost sentence. [strong]
- Close the Discussion with a conclusion paragraph that restates the main finding and a forward-looking implication. [strong]
- In the funding statement, give the grant number and state that funders had no role in design, analysis, interpretation or publication. [strong]
- Name a guarantor in author contributions who takes responsibility for the integrity of the work. [strong]
- Separate public and access-controlled data in the data availability statement, giving the access route for the controlled data. [strong]
- Avoid colons and semicolons in prose; use commas and parentheses. [strong]
- Place citations directly after the specific claim, mid-sentence when the sentence contains several claims. [strong]
- Define each abbreviation at first use and use it again; do not define terms used only once. [weak] (RAG defined, never reused; several terms undefined)
- Define abbreviations in the abstract and again at first use in the main text. [weak] (done for LLMs only)
- Keep Results descriptive and move explanations to the Discussion. [weak] (Results interpret freely)
- Name the reporting guideline followed. [weak] (none named)

# Notable deviations

- Present tense used for Methods and Results throughout, rather than past tense; common in computer science, less so in clinical journals.
- Results carry substantial interpretation and causal explanation ("we argue", "can be explained by"), contrary to the usual clinical rule of keeping interpretation for the Discussion.
- Uncertainty reported as mean ± SD across three temperature runs with one-sided paired t tests; no confidence intervals or bootstrap. Clinical reviewers would usually ask for 95% CIs.
- Almost no numbers in the Results prose; all metric values live in tables.
- Unstructured abstract with no quantitative result.
- Contributions listed in one 77-word sentence; informal phrasing ("delved into", "VS") retained.
- No reporting guideline (e.g. TRIPOD-LLM) cited despite clinical data use.
- Author contributions in narrative initials style, not CRediT.
