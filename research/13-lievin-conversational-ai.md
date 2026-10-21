# Paper

Lievin V, Palepu A, Weng WH, Saab K, Stutz D, Cheng Y, Kulkarni K, Mahdavi SS, Barral J, Webster DR, Chou K, Hassidim A, Matias Y, Manyika J, Tanno R, Natarajan V, Rodman A, Tu T, Karthikesalingam A, Schaekermann M. Towards conversational artificial intelligence for disease management. Nature. 2026;655:1292-1299. doi:10.1038/s41586-026-10764-5.

- Journal: Nature (Vol 655, 30 July 2026; received 17 March 2025, accepted 4 June 2026, open access).
- Article type: original research ("Article"), randomized blinded virtual OSCE study plus a new benchmark (RxQA).
- Word count estimate: abstract about 265; main text about 4,300; Methods about 3,300; legends about 1,200; 52 references.
- Source used: local PDF (28 pages, text extracted with pypdf and checked against page images); Supplementary Information not included in the PDF.

# Global patterns

**Sentence length.** Sample of 20 sentences across sections: range 7 to about 70 words, typical 20 to 35. Short punch sentences appear at turning points ("There were no domains in which PCPs outperformed AMIE", 9 words; "Our contributions are summarized in Figs. 1 to 3", 7). The longest are Results sentences packed with three visit-level comparisons in parentheses (about 70 tokens) and the first Introduction sentence (about 60 words, a "not only... but" construction). Paragraphs: Introduction 3 to 4 sentences (100 to 130 words); Results 3 to 5 (90 to 160 words); Discussion 6 to 12 (150 to 320 words).

**Voice and person.** "We" is frequent in the Introduction contributions, Methods and Discussion ("we developed", "we acknowledge", "We encourage future work"). Results are mostly third person with the system or physicians as grammatical subject ("AMIE scored significantly higher than PCPs"). Passive appears in study description ("AMIE was compared to 21 primary care physicians") and in captions.

**Tense.** Abstract mixes present perfect for the field and own work ("have remained underexplored", "We have advanced"), past for the study, present for the closing claim. Introduction: present perfect for field progress, present for the problem. Methods: present for the system's architecture ("The dialogue agent has two roles"), past for what was done. Results: past throughout. Discussion: past for findings, present and conditional for implications ("could eventually provide continuity").

**Hedging.** Graded vocabulary: "indicate", "suggest", "seem to", "probably", "we suspect", "might". Strong verbs ("demonstrate", "showed", "outperformed") are reserved for numbers in Results or summary sentences. Implication sentences carry double hedges and conditionals ("If such systems could be developed and tested with care..."). Yet promotional framing coexists: "a significant step", "milestone", "crucial unmet need", "durable contributions", "art-of-the-possible demonstration". Readiness disclaimers are explicit and repeated (Discussion and Conclusion: not ready for clinical care).

**Punctuation.** Semicolons are used freely: between independent clauses, and to separate visit-level results inside parentheses ("95% versus 72%, P < 0.001, for visit 1; 96% versus..."). Colons introduce numbered lists and run-in definitions. Parentheses are very heavy, mostly pointers to Supplementary Information sections, figures and examples ("(for example, compounding errors)"). No dashes in prose. Lists inside sentences are serial without an Oxford comma in British style, and Methods use numbered run-in lists "(1) ... (2) ...", each item a full sentence or clause ending with semicolons or periods.

**Abbreviations.** About 15 (LLM, AI, AMIE, PCP, OSCE, NICE, BNF, Mx, MXEKF, RxQA, PACES, DDx, GMCPQ, COPD, FDR, CI). AMIE and PCP are defined in the abstract and again in the Introduction. OSCE is spelled out in the abstract as "Objective Structured Clinical Examination" but in the Introduction as "...Clinical Evaluation" (an inconsistency). NICE is spelled out without abbreviation in the abstract, abbreviated in the Introduction. Mx is first defined in the Fig. 1 caption. MXEKF is defined in a Results heading paragraph. RxQA is never expanded. FDR, GMCPQ and PACES are redefined in each caption. COPD appears unexpanded in a caption.

**Numbers and statistics.** OSCE results: integer percentages, paired as "AMIE% versus PCP%", P to three decimals or "P < 0.001", visit label after; no counts, no effect sizes, no CIs. Preference results: "median tie rate of 49% (95% CI: 37% to 62%; n = 51), with an en dash range in the original". RxQA: one decimal ("50.6% versus 41.5%, P = 0.013"). Capital italic P in main text, lower-case p in Extended Data captions. Tests named only in Methods and captions (McNemar, FDR correction). n given for subsets ("lower-difficulty (n = 282)").

**Citations.** Superscript numerals at clause or sentence end, usually 1 to 3 per claim, sometimes mid-sentence after the noun they support ("Gemini4", "AMIE1 to 3" as a superscript range). "ref. 1" used as a noun in Methods. Guidelines cited by URL. Supplementary Information is cited by section number dozens of times, functioning as a second citation layer. No reporting guideline (CONSORT, TRIPOD-LLM, etc.) is named; only the Nature Portfolio Reporting Summary.

**Transitions.** Paragraphs open with topic sentences that state the point ("There were important differences between the management plans..."). Linkers: "Although" (very frequent), "However", "By contrast", "Similarly", "In addition", "Nonetheless". Known to unknown to aim is compressed into three Introduction paragraphs.

**Word choice.** Moderate jargon, mostly plain verbs, but with nominalisations ("preciseness", "grounding", "alignment", "translation"). Technical terms (agentic, posttraining, long-context) go undefined.

# Local patterns by section

**Title.** Descriptive phrase, 7 words, "Towards X for Y". Names neither design nor population; it echoes the predecessor paper's title (series branding).

**Abstract.** Unstructured single paragraph, about 265 words. Moves: concessive "Although" field promise plus gap; what we built; how it is grounded; design with numbers (21 PCPs, 100 scenarios); headline result; second contribution (RxQA); its result; hedged but promotional close ("marks a significant step towards"). No P values or percentages in the abstract; only sample sizes.

**Introduction.** No heading; 3 prose paragraphs plus a bulleted contribution list. Funnel: rapid LLM advances in diagnosis; diagnosis is "necessary but not sufficient"; management reasoning defined and why it is hard (context specificity); evaluation gap (static non-conversational settings). Aim paragraph opens "In this paper, we detail our progress towards...". Then a one-line pointer to Figs. 1 to 3 and three bullets: system, study, results. Results are fully previewed in the third bullet.

**Methods (after references).** Order: system overview (two agents, dual-process analogy), Dialogue agent (posttraining, chain of reasoning, agent state), Mx agent (design optimization, long-context reasoning, coarse retrieval, structured generation), Evaluation (multivisit OSCE: scenarios, clinical guidelines, participants, evaluation measures), RxQA benchmark (numbered build steps), Statistical analysis (short, two paragraphs plus one sentence), Reporting summary. Run-in bold subheads ("Posttraining.", "Coarse retrieval."). Design rationale is argued in prose against alternatives. No ethics approval or consent statement appears in the PDF.

**Results.** Three H2 headings (Management plan quality; Management Reasoning Empirical Key Features; Medication reasoning accuracy). Each opens with a short paragraph on what was measured and which figure shows it, then run-in bold claim headings that state the finding as a sentence fragment ("AMIE had more precise recommendations.", "External knowledge helps PCPs and AMIE."). No cohort description section. Comparisons phrased "scored significantly higher than", "marginally though not significantly higher". Interpretation largely avoided, though evaluative words slip in ("A key strength of AMIE was its level of preciseness").

**Discussion.** Opens with a one-sentence principal-finding paragraph ("In this study, we showed that AMIE performed consistently well..."). Then one paragraph per finding: longitudinal care; preciseness with a concrete example (generic antibiotic advice versus named drug, dose, route); guideline alignment with a counterpoint; MXEKF; ablations (candidly noting scaffolding added little to newer base models); RxQA. Limitations open with "Despite these promising results, our study had several limitations" and run five paragraphs (about 700 words, roughly a quarter of the Discussion), each followed by mitigation or future work ("We encourage future work to..."). A separate RxQA limitations paragraph closes the Discussion. Conclusion heading: 4 sentences; restates the claim, explicitly denies clinical readiness, names next steps, then ends on "milestone".

**Back matter.** Order: Online content statement; References; Methods; Data availability; Code availability; Methods references; Acknowledgements; Author contributions; Funding; Competing interests; Additional information (Supplementary information, Correspondence, Peer review information, Reprints). Data availability: partial and controlled; open datasets named, scenarios and AMIE output shared in Supplementary Information, OpenFDA portion on GitHub, BNF portion only via contacting BNF owing to licensing. Code availability: model and weights not released, justified by safety of unmonitored medical use. Author contributions grouped by activity (conception, data curation, technical implementation, evaluation), CRediT-like but not CRediT vocabulary. Funding: one sentence (Alphabet). Competing interests: employment and stock listed by initials.

**Figures and captions.** Bold title as a short noun phrase ("Overview of randomized study design."), then 3 to 8 explanatory sentences; panel letters bold with comma ("a, Target structure..."). Captions repeat statistical details (test, correction, n, error bar meaning, significance asterisk key). Abbreviations largely not re-expanded in main figures; Extended Data captions do re-expand. Fig. 1 summarizes system, design and headline result in one panel set.

# Checklist candidates

- End the Introduction with an explicit aim sentence followed by a bulleted list of contributions that maps to figures. [strong]
- Write Results run-in subheadings as one-line claims that state the finding. [strong]
- Open every Results subsection with what was measured, by whom, and which figure shows it, before giving numbers. [strong]
- Report each comparison as "X% versus Y%, P = 0.xxx" with the subgroup named in the same parenthesis. [strong]
- Give P values to three decimals and use "P < 0.001" below that threshold. [strong]
- State n and the 95% CI for summary rates. [weak] (done for preference rates, absent for OSCE proportions)
- Open the Discussion with a single sentence restating the principal finding. [strong]
- Devote one Discussion paragraph to each main finding, ending with its practical implication. [strong]
- Pair each limitation with its mitigation or a concrete future study. [strong]
- State explicitly that the system is not ready for clinical use, in both Discussion and Conclusion. [strong]
- Use graded hedges ("indicate", "suggest", "could") for implications and keep "demonstrate" for measured results. [weak] (promotional phrases undercut this)
- Define an abbreviation at first use in the abstract and again at first use in the main text. [weak] (AMIE and PCP yes; NICE, RxQA not)
- Keep the expansion of each abbreviation identical everywhere. [weak] (OSCE expanded two ways)
- Put the statistical test and multiple-comparison correction in the figure caption as well as Methods. [strong]
- Justify withheld code or data in the availability statement with a specific reason (safety, licensing) and an access route. [strong]
- Include an illustrative concrete example to explain why a metric matters clinically. [strong]

# Notable deviations

- No ethics approval, consent or IRB statement anywhere in the PDF, despite human participants; no CONSORT-style or TRIPOD-LLM reporting guideline named.
- Semicolons and long parenthetical chains carry multiple results per sentence, producing sentences of 60 to 70 tokens.
- Promotional wording ("significant step", "milestone", "durable contributions", "art-of-the-possible") alongside cautious hedging; acceptable at Nature for an industry lab, risky for JAMIA or Lancet Digital Health.
- Results flagged on percentage differences without CIs, effect sizes or raw counts for the main OSCE comparisons.
- Introduction has no heading and previews all results in bullets; Methods sit after the main references (Nature format).
- More than 30 Supplementary Information pointers shift detail out of the paper.
- Surface errors survived editing (stray periods, "to allows", inconsistent OSCE expansion, mixed British and American spelling, P versus p).
- "Although" as a sentence opener is heavily repeated, including three times in the abstract.
