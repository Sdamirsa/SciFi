# Paper

Gaber F, Shaik M, Allega F, Bilecz AJ, Busch F, Goon K, Franke V, Akalin A. Evaluating large language model workflows in clinical decision support for triage and referral and diagnosis. npj Digital Medicine, 2025.

- Journal: npj Digital Medicine
- Article type: original research (LLM benchmarking on 2000 retrospective MIMIC-IV emergency department cases, plus a clinician reader study)
- Word count estimate: about 5000 to 5500 words of main text; 46 references; 8 figures, 6 tables
- Source: open-access PDF in the MDC Berlin repository (https://edoc.mdc-berlin.de/id/eprint/25329/1/25329oa.pdf). PMC (PMC12064692) only returned paraphrases or a reCAPTCHA page, and nature.com failed. The fetch tool would not return verbatim text, so this analysis rests on structural measurements (counts, openers, short quotes) taken from the PDF. Paragraph boundaries are approximate.

# Global patterns

**Sentence and paragraph length.** Most sentences run 13 to 40 words; the median is about 22 to 25. The longest are in the Introduction (the aim sentence, about 54 words) and in Results and Discussion (39 to 41 words). Methods sentences are shorter (7 to 16 words). Paragraphs are uneven: 2 to 8 sentences and 30 to 210 words. Results paragraphs are often short (30 to 60 words). Discussion paragraphs average about 100 words (16 paragraphs, about 1640 words).

**Voice and person.** The authors write as "we" throughout: "We created a curated dataset", "we evaluated", "we mapped". Passive voice appears for procedures and outcomes ("were assessed", "were rated"). The Methods sections mostly use "we", with some descriptive sentences about the models.

**Tense.** Past tense for actions in Methods and Results. Present tense for what tables and figures show ("Table 4 show[s]", "Figure 4 presents") and for interpretation ("results suggest"). The Discussion opens in present progressive ("are beginning to reshape").

**Hedging and certainty.** Results freely use interpretive verbs (show, suggest, demonstrate, indicate, highlight, underline). Some claims go beyond the evidence, such as RAG knowledge "has enhanced its diagnostic skills" with no statistical test behind it. The Discussion contains about 14 hedges (may, might, could, suggest, likely) across 16 paragraphs. The authors also use intensifiers: "a significant 81.5%" (not meaning statistical significance), "exceptionally low at just 2.63%", "crucial finding". Strong claims point to a table or figure, never to a confidence interval.

**Punctuation.** No semicolons in the Discussion and almost none elsewhere. Colons are rare in prose but are used in titles of captions and subsection-like constructions ("Triage level accuracy: exact match vs. range evaluation"). There is one em dash and a couple of spaced hyphens in the Discussion. Parentheses carry abbreviation definitions, conditions ("with additional patient vitals data") and legal articles. Lists within sentences use commas.

**Abbreviations.** LLM and RAG are defined in both the abstract and the main text. ED is defined twice (Introduction and Results). AI, AWS, HPI and HIV are never defined, and captions never expand abbreviations. Handling is loose.

**Numbers and statistics.** Results are given as percentages only. Decimals are inconsistent (95.62%, 81.5%, 76%). Counts are written without a thousands separator ("2000 cases"). There are no confidence intervals, p values, kappa or variance estimates, and all values come from a single run. Inter-rater agreement is raw percent agreement. Comparisons are verbal ("minimal", "similar accuracy", "outperformed").

**Citations.** Superscript numerals placed mainly mid-sentence, directly after the claim or name, with ranges (8 to 14, 15 to 18) when citing groups of studies. The Introduction has about 13 citation markers and the Discussion 17. Many Discussion paragraphs have none. No reporting checklist is cited (no TRIPOD-LLM, STARD or TRIPOD). The EU AI Act is cited by article number.

**Transitions.** Most paragraphs open with a noun phrase ("The ...", over 25 times). Connectives are rare (While 3, However 1 to 2, Moreover, Finally, Nevertheless 1 each). Results subsections often open with a purpose clause ("To evaluate the accuracy and reliability of the...").

**Tone.** Mostly plain, with mild promotional wording: "promising results", "promise", "empowers", "highly needed", "reshape". There is no "groundbreaking", "revolutionary" or "novel".

**Word choice.** Moderate nominalisation ("the evaluation of") and jargon limited to the domain.

# Local patterns by section

**Title.** A descriptive phrase of 15 words with no colon. It names the method (LLM workflows), the setting (clinical decision support) and three tasks. It does not name the dataset, the design (retrospective) or the models. The phrase "triage and referral and diagnosis" uses a double "and" (the preprint used a colon list).

**Abstract.** Unstructured, a single paragraph of 142 words in 7 sentences (10 to 34 words each). The moves are: importance (1 sentence), patient problem (1), clinician problem (1), LLM opportunity (1), "In this study, we benchmark..." method (1, the only number: 2000 cases), qualitative findings (1: "Our findings show that these LLMs are capable..."), and implication with "may" (1). No performance figures appear. This is a weak model for a skill that should require numbers in the abstract.

**Introduction.** Six or seven paragraphs, about 740 words and 28 sentences. P1: decision-making is complex and the ED is error-prone. P2: LLM performance on exams and vignettes. P3: under- and over-triage rates with numbers (5% and 35% targets, 14 to 34% observed). P4: patients as a second user group. P5: the gap ("While the scope of current LLM research...", which notes single-disease and multiple-choice formats). P6: the aim ("In this study, we aimed to benchmark multiple LLM workflows...") with data, models and tasks, plus a qualitative preview of "promising results". A short contribution statement follows.

**Results** (before Methods, as at npj). Eight descriptive subsections: dataset, model selection and RAG (Fig. 1 workflow), one per task, inter-model agreement, then two clinician validations. Each task subsection restates the clinical rationale ("In the context of emergency care, triage..."), defines the metric, then reports Tables 1 and 2 and figures. Interpretation is not avoided. Paragraphs end with sentences such as "These results suggest that LLMs perform well in..." and "This is a crucial finding, as it indicates...".

**Discussion.** 16 unheaded paragraphs. P1 sets out field context, not findings. P2 gives the main finding ("Our results suggest that LLMs and the RAG-assisted LLM can support...") and has the most citations. P3 to P8 cover mechanisms (why RAG gains from vitals), weaknesses (severe levels, numeric guidelines), a data bias and how it was mitigated, and future work. P9 and P10 cover prompting and model complementarity. P11 to P13 cover the EU AI Act and "leaky deployment". P14 covers generalisability beyond Claude. P15 and P16 conclude that the results are "primarily of academic interest", that LLMs cannot replace clinicians, and that education and screening are plausible roles. Limitations are spread across paragraphs with no dedicated one.

**Methods.** Ten subsections: data preprocessing (about 650 words, exact inclusion thresholds), prompts (temperature 0, prompts in the Supplement), model selection, RAG-assisted LLM (30 million PubMed abstracts, no top-k or embedding model), one evaluation framework per task (three), LLM judge, reader study (400 cases, four clinicians), and intra-model agreement. Short "we" sentences. There is no statistics subsection, no ethics statement, no reporting guideline and no model version strings.

**Back matter.** The order is Data availability, Code availability, References, Acknowledgements, Author contributions, Funding, Competing interests, Additional information, Open Access licence. Data availability is a one-line pointer to PhysioNet ("Core data is available at..."). Access is credentialed through PhysioNet but the text does not say so. Code availability points to GitHub. Author contributions use initials in prose ("F.G. and M.S. jointly executed..."), not CRediT. Funding states that the work received no specific funding and that Open Access was paid by Projekt DEAL. Competing interests use the standard sentence "The authors declare no competing interests."

**Figures and tables.** Each caption starts with a short title phrase (5 to 11 words, no verb) that often has a colon and "vs." ("Specialty prediction accuracy: matched vs. at least one..."). The detail runs 40 to 90 words. Abbreviations (LLM, RAG, MIMIC-IV-ED) are never expanded in captions. There are two workflow schematics (Figs. 1 and 8) and a preprocessing flow diagram (Fig. 7).

# Checklist candidates

- Open the aim paragraph with "In this study, we..." and name the data source, models and tasks in the same sentence. [strong]
- Ground the clinical gap in concrete numbers from the literature, such as error-rate targets and observed rates, before introducing AI. [strong]
- State the research gap by contrasting prior evaluation formats (multiple-choice, single disease) with the real task. [strong]
- Write in the first person plural for design decisions and use passive voice only for routine procedures. [strong]
- Use past tense for what was done and present tense for what tables and figures show. [strong]
- Give each Results subsection a descriptive heading that names the task, and keep one task per subsection. [strong]
- In npj format, when Results precede Methods, briefly restate the dataset and metric definitions at the start of Results. [strong]
- Report temperature and put the full prompts in the Supplement. [strong]
- Define each evaluation metric (exact match, range or tolerance accuracy, at-least-one match) in its own Methods subsection. [strong]
- Validate LLM-generated ground truth or LLM-judge outputs with a clinician reader study, and report the number of cases and raters. [strong]
- Discuss regulatory status (for example the EU AI Act risk class) and the risk of informal deployment when the task is high-risk. [strong]
- End the Discussion with a claim weaker than "replace clinicians" and name realistic roles such as education or background screening. [strong]
- Use a single line for each Data availability and Code availability statement, with repository URLs. [strong]
- Begin each caption with a verbless title phrase of 12 words or fewer, then the detail. [strong]
- Put at least one key quantitative result in the abstract. [weak, this paper does not]
- Report confidence intervals or a significance test for every model comparison, and use kappa for agreement. [weak, absent here]
- Define every abbreviation at first use in the abstract and again in the main text, and expand abbreviations in captions. [weak]
- Use the same number of decimal places for all percentages. [weak]
- Include an explicit limitations paragraph. [weak, limitations are scattered]
- Name a reporting guideline (for example TRIPOD-LLM) and include an ethics statement even for public de-identified data. [weak, absent]

# Notable deviations

- The abstract has no performance numbers. Its findings sentence is qualitative ("capable of...").
- No inferential statistics anywhere: no confidence intervals, p values or kappa, and single-run percentages only. Yet the authors use "a significant 81.5%" in its everyday sense, which reviewers in JAMIA or Lancet Digital Health would flag.
- Intensifiers and evaluative adverbs appear in Results ("exceptionally low at just", "crucial finding"), and Results interpret findings freely, including causal language about RAG.
- The Discussion opens with context, not with the principal findings, and has no limitations heading or paragraph.
- No ethics statement and no reporting guideline, which is acceptable at npj for public MIMIC data but would not be elsewhere.
- Author contributions use initials in prose rather than CRediT.
- Copy-editing slips survived into print ("Additionally to", "based once on", a leftover drafting note in the reader study). The "Intra-model agreement" heading describes inter-model agreement. Use this paper for structure, not for polish or statistics.
- The title chains three tasks with "and ... and" instead of using a colon or a comma list.
