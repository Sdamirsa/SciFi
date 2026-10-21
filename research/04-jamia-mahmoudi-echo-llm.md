# Paper

Mahmoudi E, Vahdati S, Chao CJ, Khosravi B, Misra A, Lopez-Jimenez F, Erickson BJ. A comparative analysis of privacy-preserving large language models for automated echocardiography report analysis. Journal of the American Medical Informatics Association, 2025.

- Journal: JAMIA (2025;32(7):1120-1129; DOI 10.1093/jamia/ocaf056)
- Article type: original research
- Word count estimate: about 3,000 words of main text (abstract about 250, introduction about 420, methods about 700, results about 650, discussion and conclusion about 1,000), 3 figures plus 1 workflow figure, 3 tables, 22 references.
- Source used: medRxiv full text, https://www.medrxiv.org/content/10.1101/2024.12.19.24319181v1.full (abstract of the published version checked at https://academic.oup.com/jamia/article-abstract/32/7/1120/8126598).

**Source caveat.** The published full text was unreachable (PMC12257941 served a reCAPTCHA page, OUP is paywalled, Europe PMC was rate limited), so this analysis uses the medRxiv preprint. The published abstract matches it in content, but JAMIA editing likely changed back matter and some typos. Treat back-matter and polish findings as preprint-specific.

# Global patterns

**Sentence length.** Sample of 20 sentences: range 7 to 97 words, median about 22, mean about 26. Introduction is moderate (mean about 19). Methods has two sentences over 60 words chained by semicolons. Results holds the longest (97 words, a failure taxonomy as one inline enumeration). Discussion has several 45 to 75 word sentences. Very short sentences (7 to 8 words) serve as figure pointers.

**Paragraph length.** Introduction 4 paragraphs of 4 to 6 sentences (74 to 146 words). Methods paragraphs about 105 to 145 words. Discussion 9 short paragraphs of 1 to 6 sentences.

**Voice and person.** "We" appears only in the Introduction aim paragraph and the Discussion opening. Methods is almost fully passive ("Reports were manually labeled by a cardiologist"). Results uses models as subjects ("All five LLMs generated valid labels").

**Tense.** Introduction: present perfect for field state ("has shown promise"), present for the aim. Methods and Results: past, with present only for pointers to figures or supplement. Discussion: present for claims, past for actions. Conclusion: present and future ("will be essential").

**Hedging and certainty.** Mostly unhedged: "demonstrates", "achieved exceptional", "enables". Hedges ("may", "A possible explanation is", "likely") appear only for mechanisms and future use. Strong claims usually carry a number in the same sentence, but some Discussion numbers are absent from main-text Results. The abstract conclusion ("near-perfect performance") is stronger than the Discussion.

**Punctuation.** Introduction uses only commas, periods and parentheses. Methods and Results use colons to open category lists and semicolons to chain clauses. Parentheses carry abbreviations, parameter counts, n values. Inline lists use commas plus "respectively".

**Abbreviations.** About 13 defined. Core ones (LLM, VHD, CoT, MSE) defined in the abstract and again in the main text, then used heavily. IRB defined and never reused. MR, PS, TR, PR defined only in table captions and barely reused. GPU, AS and AI used undefined.

**Numbers and statistics.** Point estimates only: no CIs, p values or tests. Counts use "n=" and slash ratios ("91/200"). Percentages mix whole numbers and one decimal; accuracy sometimes lacks a % sign. MSE to two decimals. Median ranges and ± values are unlabelled.

**Citations.** Numeric, bracketed, at sentence end, usually one per claim; model citations sit mid-sentence after each model name. No reporting guideline named in the text. Only 22 references.

**Transitions and flow.** Topic-sentence openings. Linkers: "However", "On the other hand", "Traditionally", "Notably", "In conclusion". Classic funnel: task importance, manual burden, NLP history, LLMs, size versus compute, fine-tuning versus prompting, privacy and open-source models, sparse echo evidence, aim.

**Tone.** "Has revolutionized" in the Introduction; Discussion and Conclusion lean promotional ("exceptional", "significant advancement", "great promise"). The Conclusion closes with a safety sentence (support, not replacement; ongoing validation).

**Word choice.** Moderate nominalisation ("Content extraction", "the creation of"); "utilized" preferred over "used". Clinical terms are not explained; informatics terms are defined. Some grammar slips.

# Local patterns by section

**Title.** Descriptive noun phrase, no colon, 14 words. Names the design type ("comparative analysis"), the method class with its selling attribute ("privacy-preserving large language models"), and the task and data ("echocardiography report analysis"). No population, site or sample size.

**Abstract.** Structured: Background, Methods, Results, Conclusions; about 250 words. Moves: rationale and what was tested; data split by year, five models, two tasks, reference standard, metrics; best accuracies (one decimal) and MSE, smaller-model ranges, CoT effect, seconds per report, error sources; a strong claim plus a practical trade-off. Results take the largest share (about 93 words).

**Introduction.** Four paragraphs, about 420 words. P1 frames task importance and manual burden; P2 introduces LLMs and the size versus compute trade-off; P3 contrasts fine-tuning with prompting and adds privacy as the motivation for open-source, on-premise models; P4 states sparse prior evidence ("evidence on the performance of LLMs ... is limited", paraphrased), then the aim with "we aim to develop an automated pipeline", the method summary, and a closing contribution sentence. No results are previewed. Example openers: "Content extraction from echocardiography reports is crucial for case retrieval"; "However, the trade-off between model size, performance, and computational resources".

**Methods.** Subsections in order: Data collection; Prompts structure; Model selection and deployment; Prompt optimization and model evaluation. The IRB statement with protocol number is the first sentence of Data collection ("In this Institutional Review Board (IRB) approved study"). Consent and waiver are not in Methods (only in preprint declarations). Data: consecutive single-centre reports, impression section excluded. Reference standard: one certified cardiologist, with quoted label values. Prompt anatomy (system, user, assistant roles) in Figure 1, full prompt in supplement. Models named with parameter counts and citations; hardware and Python version named; inference parameters in supplement. Optimization: expert error review, per-model "hint" edits until no improvement, then a later-year held-out test set. Metrics listed without formulas; MSE defined via explicit ordinal recoding. No statistics paragraph, no named reporting guideline.

**Results.** Order: Data characteristics (cohort and prevalence, Table 1, Figure 2), Prompt Optimization (development-set metrics), Evaluation (test-set metrics with and without CoT, Figures 3 and 4), then error analysis and ambiguous-report cases (Tables 2 and 3). Each paragraph points to one display item ("Patients' characteristics are summarized in Table 1"). Comparisons use ordered lists plus "respectively" and contrastive openers ("Without CoT-guided prompting, accuracies were generally lower"). Interpretation leaks in ("Notably", "superior performance"). Error analysis turns CoT reasoning traces into a four-type failure taxonomy.

**Discussion.** Nine paragraphs plus a separate Conclusion. P1 summarises principal findings, naming the best models and noting that size correlated with but did not fully determine performance. P2 gives registry and alerting implications. P3 and P4 compare with prior echo and radiology LLM work, mostly qualitatively, and argue fixed output labels enable objective metrics. P5 offers a mechanism in one 75-word sentence. P6 to P8 frame limitations as "challenges": hallucination, intermediate-size behaviour ("A possible explanation is that intermediate-sized models"), and CoT latency with untested mitigations. P9 notes low stenosis prevalence. No dedicated limitations paragraph; single centre, single labeller and external validity are not discussed. Conclusion (6 sentences) opens "In conclusion, our study demonstrates" and ends on validation and monitoring.

**Back matter (preprint).** Competing Interest and Funding statements after the abstract (medRxiv format), then Author Declarations (IRB number, consent). After the Conclusion: Data Availability ("available upon reasonable request to the authors"). No code availability, author contributions or acknowledgements. JAMIA headings not verified.

**Figures and tables.** Captions open with a noun phrase title, often with a colon then panel detail ("A schematic view of study workflow:" followed by left and right panel descriptions). Most are one sentence of 14 to 50 words. Abbreviations are mostly not expanded in main captions; Tables 2 and 3 end with an abbreviation key; supplementary captions expand NPV and PPV. Supplementary figures are a repeated template ("Classification matrix presenting [metric] of five models").

# Checklist candidates

- Use a descriptive noun-phrase title that names the design type, the method class and the clinical task. [strong]
- Use a four-part structured abstract (Background, Methods, Results, Conclusions) of about 250 words, with the Results as the longest part. [strong]
- Report in the abstract the sample sizes of development and test sets, the best point estimates, and an efficiency number (time per case). [strong]
- Define each abbreviation at first use in the abstract and again at first use in the main text. [strong for core terms, weak overall]
- Do not define an abbreviation you will not reuse; define those used only in a table in that table's footnote. [weak]
- Keep "we" for the aim paragraph and Discussion opening; write Methods procedures in past passive. [strong]
- End the Introduction with an explicit aim sentence ("In this study, we aim to...") followed by a one-sentence method summary and a contribution statement, without previewing results. [strong]
- State IRB approval with protocol number in the first sentence of the Methods data subsection. [strong]
- Order Methods as data, input design (prompts), models and deployment, optimization and evaluation. [strong]
- Separate a development set for prompt optimization from a held-out evaluation set, ideally from a different period, and say so in the abstract. [strong]
- Name hardware, software version and quantisation, and put inference parameters and full prompts in the supplement. [strong]
- Define any composite or recoded metric (e.g. an ordinal recoding for MSE) explicitly in Methods. [strong]
- Report uncertainty (confidence intervals) for every headline metric. [the paper does not; add this as a corrective rule]
- Name the reporting guideline (e.g. TRIPOD-LLM) in Methods. [the paper does not; corrective rule]
- Open each Results paragraph by pointing to its display item. [strong]
- Use "respectively" to map ordered value lists onto ordered model lists, keeping model order fixed throughout. [strong]
- Include an error analysis that classifies failures into named types with examples in a table. [strong]
- Open the Discussion with a summary of principal findings that names the best models and the key nuance. [strong]
- Give limitations their own clearly labelled paragraph covering single-centre data, reference-standard quality and external validity. [weak; the paper scatters limitations as "challenges"]
- Close the Conclusion by pairing the main claim with a statement that the tool supports rather than replaces clinicians and needs ongoing validation. [strong]
- Keep the abstract conclusion no stronger than the Discussion. [weak]

# Notable deviations

- No confidence intervals, p values or significance tests anywhere; comparisons between models rest on point estimates alone. JAMIA accepted this, but most clinical AI reviewers will ask for CIs.
- No named reporting guideline and no statistical analysis subsection.
- Promotional adjectives in Discussion and Conclusion ("exceptional", "significant advancement", "great promise") and "has revolutionized" in the Introduction; contrary to restrained-register advice.
- Very long sentences (60 to 97 words) built from semicolons and inline enumerations in Methods and Results, while the Introduction avoids semicolons entirely. Register is uneven across sections.
- Interpretive words ("Notably", "superior") inside Results.
- Limitations are not in a dedicated paragraph and omit major ones (single centre, single annotator, per-model prompt tuning, no external validation).
- Preprint inconsistencies (seven versus six ambiguous reports, varying model names and sizes, a CoT claim contradicted by one model's numbers) are warnings for consistency checks, not patterns to copy.
- Data availability uses weak "upon reasonable request" phrasing with no code statement; npj Digital Medicine and Nature journals require more.
