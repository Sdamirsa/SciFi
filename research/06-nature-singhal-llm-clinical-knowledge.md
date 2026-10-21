# Paper

Singhal K, Azizi S, Tu T, et al. Large language models encode clinical knowledge. Nature, 2023.

- Journal: Nature (Article, 2023;620:172-180, DOI 10.1038/s41586-023-06291-2)
- Type: original research
- Word count estimate: abstract about 240 words; main text (Main, Results, Discussion) about 6,500 words; Methods about 4,500 words including a Related work subsection; about 11,000 words in total before references.
- Source: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10396962/fullTextXML (PMC returned a reCAPTCHA page), plus the NCBI BioC XML and the Nature PDF for the back matter. The fetch tool gave paragraph-level readouts (counts, functions, numbers, hedges), not verbatim text, so all counts are approximate. Extended Data captions could not be retrieved.

# Global patterns

**Sentence and paragraph length.** In a sample of 20 sentences across sections, lengths ran from 10 to 34 words, with a mean of about 22. The longest sentence seen was about 62 words, in the Fairness and equity limitation. Paragraphs are short in Main (2 to 5 sentences, 40 to 115 words) and longer in Results and Limitations (5 to 8 sentences, 120 to 210 words). The Discussion opens with a one-sentence paragraph.

**Voice and person.** "We" is used throughout, in the abstract (about five times), in every contribution paragraph, and to open most Results paragraphs ("We randomly selected", "We sought to understand", "We asked a panel"). Passive voice appears mainly in dataset descriptions in Methods and in caption detail.

**Tense.** Main and the abstract use the present tense for this paper's own actions and findings ("we curate", "we show", "Flan-PaLM achieves"). Results and Methods switch to the past tense for procedures and outcomes ("our model achieved", "we performed several ablations"). The Discussion uses present tense for interpretation ("Our results suggest") and past for observations ("We observed"). The present perfect appears for field background ("LLMs have demonstrated").

**Hedging and certainty.** Claims are carried by achieve, show, demonstrate and improve when backed by a number, and by suggest, may, likely, seem and appears when interpretive. Hedges cluster in the ablation and selective prediction subsections, which are labelled preliminary, and in Limitations (may, could, might, often). Strong benchmark claims almost always carry a number and a figure call in the same sentence or paragraph. An unfavourable result (Med-PaLM produced more incorrect content than Flan-PaLM) is reported plainly and given "one potential explanation".

**Punctuation.** Parentheses are very frequent (abbreviations, dataset glosses, figure calls). Colons are sparse and mostly used as labels in Methods ("Format:"). Semicolons are rare. Dashes are essentially absent. In-sentence lists use no serial comma ("MedQA, MedMCQA, PubMedQA and MMLU"). "For example" is preferred over "such as".

**Abbreviations.** The abstract defines LLMs, PaLM and MMLU, and Main defines AI, COT and USMLE. LLMs is not redefined in the main text. BLEU, MedQA and MedMCQA are never expanded. Coined names (MultiMedQA, Med-PaLM) work as proper nouns. "FLAN-PaLM" appears once against "Flan-PaLM" elsewhere.

**Numbers and statistics.** Percentages are given to one decimal place (67.6%, 92.9%, 5.9%). Thousands take a comma (3,173 questions). Margins over the prior state of the art are written as "by 17%" without saying whether these are percentage points or relative gains. The running text has no CIs or p values. The bootstrap (1,000 replicas, 95% percentile) is described in Results and the Fig. 4 to 6 captions, with the intervals given in the Supplementary Information. Some gains are lower bounds ("over 30%").

**Citations.** Superscript numbers placed right after the named term or claim, usually one per claim, with ranges for groups. Each dataset is cited where it is named. Methods sometimes use "ref. N". No reporting guideline (TRIPOD, CONSORT, etc.) is cited. Harm scales (AHRQ) are cited as instrument sources.

**Transitions.** Paragraphs open with a topic sentence, often an infinitive of purpose ("To evaluate how well LLMs...", "To address this, we curate...") or a contrastive connector (However, Despite, Although, By contrast, Similarly). The contributions run as an explicit enumeration: "Our first key contribution", "The second key contribution", "The next contribution", "Finally".

**Tone.** More promotional than typical clinical journals ("impressive capabilities", "exciting potential applications", "breakthrough performance", "a compelling opportunity"). A caveat nearly always follows in the same or the next sentence.

**Word choice.** The ML jargon is dense but defined in Methods. The evaluation axes use plain words (scientific consensus, extent of harm, bias). Spelling is British with -ize endings.

# Local patterns by section

**Title.** A six-word declarative claim with no colon. It names neither the model nor the design and states the finding as a general fact.

**Abstract.** One unstructured paragraph of about 240 words and 11 sentences, with six citations, which is unusual for an abstract. The moves are: capability and high bar ("the bar for clinical applications is high"), limits of current benchmarks, "Here, to address these limitations," with the benchmark and the human evaluation framework, the models, the headline number (67.6% on MedQA, 17% over prior SOTA), the gaps found by human evaluation, the method fix (instruction prompt tuning) and the result, then a hedged closing that the models still fall short of clinicians. A separate one-sentence web summary also exists.

**Introduction (Main plus Key contributions).** Thirteen paragraphs, about 1,000 words. The funnel runs: AI in medicine is narrow (P1), LLMs as foundation models (P2), the need for safety evaluation (P3), current benchmarks fall short (P4), "To address this, we curate MultiMedQA" (P5), headline result (P6), human evaluation gaps with numbers (P7), caveat (P8), then numbered contribution paragraphs and a limitations preview (P9 to P13). Results are previewed in full. Fig. 1 summarises the contributions.

**Results.** The section has 17 subheadings, many of them findings written as sentences ("Instruction tuning improves performance", "Scaling improves performance on medical question answering", "Self-consistency improves multiple-choice performance"). The order is: overview, one subsection per benchmark, ablations, uncertainty, the human evaluation setup, then one subsection per rating axis, and finally the lay users. There is no cohort table. The human evaluation block opens with its sample (140 questions, nine clinicians). Each paragraph cites a figure or a supplementary table. Comparisons are written as a triad (clinician, Flan-PaLM, Med-PaLM) with three percentages in one sentence. Results also interpret, with hedged explanations ("may be an inherent ceiling", "One potential explanation") and flagged limitations.

**Discussion.** The section has no subheadings. It opens with a single sentence ("Our results suggest that the strong performance...") that summarises and interprets in one move. Paragraphs 2 to 5 cover scale, a rival explanation (test contamination) checked against evidence, comparison with domain-specific models, and the gap shown by human evaluation. Limitations is its own titled section and the longest part (about 1,100 words), with five subheadings (dataset scope, LLM capabilities, human evaluation, fairness, ethics). Each limitation paragraph names a limit and then a direction for future work. The Conclusion has two paragraphs with no numbers. It frames the work as early ("a glimpse") and predicts it will spark wider conversation among stakeholders, so the closing claim is modest.

**Methods (after Discussion).** The order is: Datasets (one H3 per dataset, each giving format, size and a worked example question with its answer, and MMLU split into six H4 subtasks), Framework for human evaluation (clinician evaluation, lay user evaluation), Modelling (PaLM, Flan-PaLM, aligning to the medical domain, prompting strategies: few-shot, chain-of-thought, self-consistency, prompt tuning, instruction prompt tuning), "Putting it all together: Med-PaLM", then Related work. Raters are described by number, country and specialty. There is no statistics subsection (the bootstrap appears in Results and captions), no ethics or consent statement and no reporting guideline. Hyperparameters, prompts and the model card go to the Supplementary Information.

**Back matter.** In order: Online content boilerplate, Reporting summary, Data availability, Code availability, References, Acknowledgements, Author contributions, Competing interests, Additional information (correspondence, peer review information, reprints). Data availability states the six open datasets and releases HealthSearchQA as a supplementary file. Code availability declines to open-source Med-PaLM, citing the risks of unmonitored medical use, and promises work with partners and regulators. Author contributions are grouped by task using initials (conception and design, data, technical, evaluation, clinical input). This is not CRediT. Competing interests state that the funder is Alphabet and that the authors are employees who "may own stock as part of the standard compensation".

**Figures and captions.** Each caption opens with a short title phrase ("Clinician evaluation of answers."). Panel captions are lettered and say what each panel measures, followed by a one-line comparative finding. The Fig. 4 to 6 captions state n (140 questions, one rater per item) and the uncertainty method. Model names are not expanded. SOTA and USMLE are defined inline where they first appear in a caption.

# Checklist candidates

- Use a short declarative title that states the main finding as a claim. [strong]
- Write each of this paper's own actions in Main with "we" plus a present-tense verb, and switch to the past tense for procedures and results in Results and Methods. [strong]
- Open an introduction paragraph with an infinitive of purpose or a contrastive connector that links it to the previous gap. [strong]
- State the contributions as an explicitly enumerated list at the end of the introduction. [strong]
- Preview the key numerical results in the introduction for a Nature-style Main section. [strong]
- Write Results subheadings as finding sentences where the result is unambiguous. [weak]
- Report comparisons among arms in one sentence with all values side by side, to one decimal place. [strong]
- Tie each benchmark claim to a number and a figure or table call in the same sentence. [strong]
- State the human rater sample by number, country and specialty. [strong]
- Report unfavourable results plainly and offer an explicitly hedged explanation. [strong]
- Follow each enthusiastic phrase with a caveat in the same or the next sentence. [strong]
- Give each limitation a mitigation or a concrete future-work direction in the same paragraph. [strong]
- Restate the conclusion without numbers and at a strength no greater than the evidence supports. [strong]
- State whether margins are absolute percentage points or relative gains. [weak: the paper omits this, so it is a lesson rather than a model]
- Report confidence intervals in the text, not only in captions and supplements. [weak: the paper omits this]
- Describe the uncertainty method and n in every figure caption that shows rates. [strong]
- Explain why code or weights are withheld, give the specific risk, and say what alternative is offered. [strong]
- Define an abbreviation at first use in the abstract and again in the main text. [weak: the paper does not redefine LLMs]
- Avoid dashes and use parentheses or commas instead. [strong]

# Notable deviations

- Promotional vocabulary ("impressive", "breakthrough", "exciting", "remarkable", "glimpse") that npj Digital Medicine, JAMIA or Lancet Digital Health reviewers would likely cut. It is tolerated here because each instance is hedged.
- Citations inside the abstract (six of them).
- Results contain interpretation, explanations and limitation notes, against the common rule to keep Results neutral.
- No p values or tests in the text, no CIs in the prose, and margins of unclear unit.
- No ethics approval or rater consent statement and no reporting guideline, which clinical journals would require.
- Limitations is a separate titled section, longer than the Discussion itself, with its own subheadings.
- Methods sits after the Discussion and ends with a Related work subsection, which is specific to Nature and the ML literature.
- Abbreviations are not reset after the abstract, and several dataset acronyms are never expanded.
- No serial comma and British spelling with -ize endings (Nature house style).
