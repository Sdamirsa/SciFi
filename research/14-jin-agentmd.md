# Paper

Jin Q, Wang Z, Yang Y, Zhu Q, Wright D, Huang T, Khandekar N, Wan N, Ai X, Wilbur WJ, He Z, Taylor RA, Chen Q, Lu Z. AgentMD: Empowering language agents for risk prediction with large-scale clinical tool learning. Nature Communications 2025.

- Journal: Nature Communications 16:9377 (2025), doi:10.1038/s41467-025-64430-x.
- Article type: original research (Article).
- Word count estimate: abstract about 145 words; main text (intro, results, discussion) about 2,900 words; Methods about 2,000 words including verbatim prompts. 11 pages, 5 multi-panel figures, 36 references, no main tables.
- Source used: local PDF (all 11 pages read via pypdf text extraction); no supplementary pages in the file.

# Global patterns

**Sentence length.** Sample of 20 sentences across sections: range 9 to 52 words, typical 18 to 30, mean about 24. Longest sentences are in Methods (score definitions chained with semicolons, about 50 words) and the intro's architecture sentence (about 45 words with a parenthetical aside). Short sentences appear mainly in Statistics boilerplate.

**Paragraph length.** Intro paragraphs 2 to 6 sentences (60 to 130 words). Results paragraphs are long: 8 to 14 sentences, 150 to 280 words, each covering one experiment end to end. Discussion paragraphs 4 to 8 sentences.

**Voice and person.** Heavy "we" in all sections ("We introduce AgentMD", "we manually evaluate", "we screened"). The system is also a grammatical agent: "AgentMD first uses PubMed", "AgentMD selects", "AgentMD ranks". Passive is reserved for annotation and ethics procedure ("three annotators are employed", "approved by the Yale institutional review board").

**Tense.** Present for system behaviour, figure descriptions and claims ("Figure 2 displays", "AgentMD surpasses CoT"). Results mix present and past for the same kind of action within one paragraph ("We manually evaluate" then "We also evaluated"; "we used GPT-4"). Present perfect for prior work and validation status ("has been shown to benefit", "has been validated on two real-world patient cohorts"). Methods mostly past for what was done, present for how the pipeline works.

**Hedging and certainty.** Strong verbs dominate Results: "demonstrate", "clearly demonstrate", "confirm", "show", plus "significantly outperforms" in the abstract with no statistical test anywhere. Hedges appear in the population-level analysis and Discussion: "might improve", "may offer", "has the potential", "promising". Claims are tied to a number and a figure panel in the same sentence ("0.546 vs. 0.321 in accuracy, Fig. 3b"). Each Results subsection closes with a summarising verdict sentence ("In conclusion, these results demonstrate..."). Intro and Discussion both end with a safety caveat that more evaluation is needed before clinical use.

**Punctuation.** Parentheses are very frequent: figure pointers, numeric comparisons, inline definitions, counts. Colons introduce lists and roles ("two roles: as a tool maker..."). Semicolons separate list items when items contain commas (the three cohorts; the four ranking scores). Spaced dashes appear a few times for asides ("two peaks, the higher one close to 100"). Inline enumerations use (1), (2) and (a), (b), (c).

**Abbreviations.** About 25 abbreviations; none defined in the abstract (LLM-free abstract, only "GPT-4" and "AgentMD"). Main text defines LLMs, AI, CoT, ROC, AUC, CCR, NSTEMI, API, HIPAA, IRB, CI. Inconsistencies: AI defined but never reused; CoT defined twice (Results and Methods); IRB defined twice; HIPAA spelled out again after being abbreviated; AUC defined, then AUROC used undefined; "ED" and "USMLE" used without definition; MIMIC-III never expanded. Many system names (RiskCalcs, RiskQA, MedCPT) are coined terms rather than abbreviations.

**Numbers and statistics.** Percentages to one decimal; accuracy reported as proportions to three decimals in Results (0.877) but as percentages in the abstract (87.7%). Paired comparisons as "X vs. Y". Relative improvement stated as a percent ("surpasses CoT by 70.1%"). Counts paired with percentages as "8.4% (42/500)" or "14 out of 16, 87.5%". No p values anywhere; 95% CIs only for annotator agreement in Methods, with method stated (bootstrap, 10,000 resamples). Thousands separators inconsistent (2,164 and 2164; 9822).

**Citations.** Superscript numerals placed directly after the named entity (HEART score, MDCalc, MedCPT, Llama) or at clause end; usually one per claim, ranges for clusters (26 to 29). No reporting guideline (no TRIPOD or TRIPOD-LLM) cited.

**Transitions.** Intro paragraphs open with topic sentences and link with "Despite", "In addition", "Moreover", "Furthermore", "However". Results paragraphs open by stating what was evaluated and pointing to the figure. Ordinal markers ("First", "Second", "Finally") structure Discussion and Methods.

**Tone.** Mildly promotional: "Empowering" in the title, "novel" twice, "vital", "indispensable", "pressing challenges", "Surprisingly", "clearly demonstrate". No "revolutionary" or "unlock" register. Balanced by explicit caveats.

**Word choice.** Moderate jargon from NLP (tool learning, backbone LLM, zero-shot, dense retrieval) alongside clinical terms. Some nominalisation ("the utilization of GPT-4") and non-native phrasing ("computing logics").

# Local patterns by section

**Title.** Colon title: system name, then gerund phrase stating purpose and method ("Empowering language agents for risk prediction..."). 14 words. Names the method and task, not population or design.

**Abstract.** Unstructured, single paragraph, about 145 words, 8 sentences. Moves: field value plus barrier (1 sentence), "We introduce AgentMD, a novel language agent..." (aim), tool-maker result with numbers, tool-user role, headline comparison, real-world validation, population-level use, closing claim. Numbers: 2,164 calculators, over 85% quality accuracy, over 90% unit test pass rate, 87.7% vs. 40.9%, 698 notes. No dataset names, no CIs.

**Introduction (no heading, 5 paragraphs).** Funnel: (1) calculators are indispensable, with HEART as a concrete example; (2) barriers to adoption listed as a chain of problems; (3) language agents as the remedy, with the gap stated bluntly: existing agents address maths and coding, "with minimal exploration into healthcare"; (4) "We introduce AgentMD..." with two enumerated objectives, two roles (tool maker, tool user), and a pointer to Fig. 1; (5) evaluation design across three cohorts with sizes, then full results preview with numbers, ending on a caveat ("further and more comprehensive evaluation is required").

**Results (Nature Communications order: before Methods).** Four subsections with declarative claim headings ("RiskCalcs tools feature high quality and extensive coverage"; "AgentMD can accurately calculate individual risks from emergency department notes"). Order follows the paper's logic: tool curation, controlled benchmark, individual-level real data, population-level analytics. No cohort description table. Each subsection maps to one figure (Figs. 2 to 5). Interpretation is not avoided: paragraphs contain explanations ("due to incorrect assumptions on missing values") and end with a concluding verdict. Comparisons phrased as "outperforms", "surpasses ... by", "X vs. Y".

**Discussion (5 paragraphs).** P1 opens "In this study, we address two critical issues..." then recaps curation results with numbers and causes of error. P2 compares with concurrent systems (OpenMedCalc, Almanac), naming one weakness each. P3 recaps benchmark, ED and MIMIC findings in order. P4 limitations, opening with a concession ("Although our research highlights the potential..."), then First, Second, In addition; each limitation is paired with a future direction; about 170 words, placed near the end. P5 one-sentence conclusion calling AgentMD "a promising methodical approach", softer than the Results verbs.

**Methods.** Subsections: Compliance statement (ethics first, IRB number, consent waiver), Backbone LLMs (model names, version 0613, API version, temperature 0.0), Curating calculators (Boolean query, date window, funnel counts 339,952 to 33,033 to 24,190 to 2164), Evaluation as tool maker (annotators, consensus process, labels, date of citation retrieval), Applying calculators (pipeline), CoT baseline, Evaluation as tool user (RiskQA construction, ED cohort, MIMIC scores with definitions and validation with CIs), Statistics & reproducibility (journal boilerplate: no sample size calculation, no exclusions, not randomised, not blinded). Full prompts reproduced verbatim inline. No reporting guideline named.

**Back matter (order).** Data availability; Code availability; References; Acknowledgements (funding embedded, grant numbers with author initials); Author contributions (narrative with initials, not CRediT); Competing interests ("The authors declare no competing interests."); Additional information (supplementary, correspondence, peer review). Data availability: public sources with URLs; private ED notes under controlled access via a data use agreement that forbids re-identification, requests to the corresponding author; generated resources deposited on GitHub; "Source data are provided in this paper." Code availability lists third-party code and the authors' repository with a citable reference.

**Figures.** Caption form: "Fig. N | Short noun-phrase title." then bold panel letters, each a sentence fragment describing the panel. Abbreviations defined at the end of captions ("Logic: computing logics; Interp.: result interpretation"). Captions state N, define central lines and error bars, and end with "Source data are provided as a Source Data file."

# Checklist candidates

- Use a colon title: system name, then a purpose phrase naming task and method. [strong]
- Write the abstract as one unstructured paragraph that moves from value, to barrier, to "We introduce", to headline numbers, to a closing capability claim. [strong]
- Put at least one concrete head-to-head number ("X vs. Y") in the abstract. [strong]
- Ground the field claim in the intro with one named, cited example. [strong]
- State the gap as what existing systems cover and what they do not, in one sentence. [strong]
- In the final intro paragraph, state the aim, enumerate objectives with (1), (2), name cohorts with sizes, and preview key results. [strong]
- End the intro and the Discussion with an explicit caveat that further evaluation is needed before clinical use. [strong]
- Give Results subsections declarative headings that state the finding. [strong]
- Map each Results subsection to one figure and cite panels inline next to each number. [strong]
- Close each Results subsection with a one-sentence summary verdict. [strong]
- Use one numeric scale per metric throughout (do not switch between 0.877 and 87.7%). [weak; paper violates]
- Report CIs with the method stated (bootstrap, number of resamples). [weak; only in Methods]
- Open Methods with the ethics statement: IRB name, protocol number, consent waiver and reason. [strong]
- Report LLM name, version, API version and decoding temperature. [strong]
- Report the literature search query, date window and the count at each filtering step. [strong]
- Reproduce prompts verbatim in Methods or supplement. [strong]
- Describe annotation: number of annotators, independence, consensus procedure, label set. [strong]
- Open the Discussion with "In this study, we..." plus a recap of principal findings. [strong]
- Compare with concurrent systems by naming each and its specific weakness. [strong]
- Write limitations as a concession sentence, then First/Second/In addition, pairing each with a future direction. [strong]
- Make the conclusion sentence weaker than the Results verbs ("promising approach"). [strong]
- Use the caption pattern "Fig. N | Title." then panel letters, defining abbreviations and N at the end. [strong]
- Provide controlled-access wording for private clinical data: data use agreement, no re-identification, requests to corresponding author. [strong]

# Notable deviations

- "Significantly outperforms" in the abstract with no significance test or p value anywhere in the paper; reviewers in JAMIA or Lancet Digital Health would likely object.
- Interpretation and causal explanation inside Results, plus evaluative adverbs ("Surprisingly", "clearly demonstrate").
- Tense switches between present and past within the same Results paragraph.
- Abbreviation hygiene is loose: AI defined and unused, CoT and IRB defined twice, AUROC and ED and USMLE undefined, HIPAA re-expanded.
- Inconsistent number formatting (2,164 vs 2164; proportions vs percentages; stray spaces before %).
- Stray "(1)", "(2)", "(3)" reference markers in the Backbone LLMs paragraph, and a duplicated sentence on annotation labels; "respectively" misused with a single pair.
- No reporting guideline (TRIPOD-LLM would apply) and no cohort characteristics table; Statistics section is only Nature boilerplate.
- Results precede Methods and the intro has no heading: Nature Communications house format, not universal.
- Narrative author contributions (not CRediT) and funding inside Acknowledgements are journal-specific.
