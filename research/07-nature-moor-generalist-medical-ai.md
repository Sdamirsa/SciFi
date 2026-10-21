# Paper

Moor M, Banerjee O, Abad ZSH, Krumholz HM, Leskovec J, Topol EJ, Rajpurkar P. Foundation models for generalist medical artificial intelligence. Nature, 2023.

- Journal: Nature (vol. 616, pp. 259 to 265; DOI 10.1038/s41586-023-05881-4)
- Article type: perspective (review-type, no original data)
- Word count estimate: about 4,500 words of main text, about 165-word summary, two multi-panel figures, no tables or boxes
- Source used: NSF public-access copy, https://par.nsf.gov/servlets/purl/10471867 (the nature.com page failed to fetch). Verbatim text was refused, so analysis rests on targeted structural fetches (counts, openings, short snippets).

# Global patterns

**Sentence length.** A sample of 20 sentences across sections ran from 8 to 41 words, median about 25. The shortest is the conclusion's opening claim (8 words); the longest body sentence is 41 words; 60+ word sentences occur only in back matter. Introduction paragraphs have 2 to 7 sentences (mean 4); body paragraphs run about 20 to 140 words.

**Voice and person.** Active voice dominates. "We" is concentrated in three places: the summary (4 uses in 3 of 7 sentences), the introduction's last three paragraphs (roadmap), and the conclusion's closing call to action. Body sections almost never use "we" (one "We anticipate"). Body sentences take the concept as subject ("GMAI enables").

**Tense.** Present simple for the state of the field and for what GMAI is. Present perfect for recent developments in the literature (prior work "has already shown"). Future and modal forms carry the vision: "will" for confident predictions, "can", "may", "could" for capabilities and use cases. "Would" is absent; "can" is used even for hypothetical systems, making the prose concrete.

**Hedging and certainty.** "Can" is the dominant modal (about 12 uses in the capabilities section, 16 in use cases), followed by "may" (13 in use cases) and "could" (6). "Will" is used for firm predictions about the field and for challenges ("will be uniquely difficult to validate"). "Probably" and "potentially" appear in the challenges. Strong empirical claims are tied to a superscript citation or a number in the same sentence (more than 500 FDA-approved models; PaLM at 540 billion parameters).

**Punctuation.** Semicolons: none observed. Colons: rare in prose (one in the introduction, introducing a named concept, "a new capability: in-context learning"), but used about six times in the capabilities section to introduce quoted example queries. Em dashes: about four in the whole paper, all as paired appositive interruptions. Parentheses: frequent in the introduction (8), for synonyms, figure pointers, labels for a just-described concept, and "for example" asides. In-sentence lists are built with commas and ordinal adverbs (First, Second, Third, Finally).

**Abbreviations.** Very few. AI and GMAI are defined in the summary and not redefined in the main text (Nature house style for perspectives). FDA is avoided entirely: "Food and Drug Administration" is spelled out because it is used once. Model names (GPT-3, PaLM, CheXzero) are never expanded. Captions use GMAI and EHRs without expansion.

**Numbers.** No statistics in the inferential sense (no CI, no p values). Numbers serve as rhetorical anchors: counts ("more than 300 apps"), scale ("540 billion parameters", "3,000 to 6,000 chips"), and approximate magnitudes ("hundreds of tons of CO2 equivalent", "millions of dollars").

**Citations.** Nature superscript numerals, mostly at sentence end before the period, sometimes mid-sentence directly after the term they support (five in one sentence listing techniques, one per technique). Ranges are compressed. Usually one citation per sentence. Density varies: text-to-protein is heavily cited (8 refs in 9 sentences), patient chatbots barely (1 in 14).

**Transitions and flow.** Paragraphs open with a topic sentence whose subject is the concept or the problem ("In stark contrast to a clinician, conventional medical AI ..."). Contrastive openers are common ("In current practice", "Compared to conventional AI models"). Ordinal adverbs (First, Third, Finally) structure enumerations. Macro movement: foundation models, why medical AI is narrow, what GMAI is, what it would do, what blocks it, call to action.

**Tone.** Mostly sober, but the paper permits measured visionary language at the boundaries: the conclusion opens by saying foundation models could transform healthcare and later speaks of unprecedented possibilities. In the body, promotional words are milder ("promises", "versatile", "indispensable", "markedly reducing"). No "groundbreaking", "unlock", "exciting".

**Word choice.** Plain verbs, moderate jargon (self-supervision, in-context learning, distribution shift are explained briefly at first use). Coined labels are introduced in parentheses, then reused as subsection headings.

# Local patterns by section

**Title.** Descriptive noun phrase, 8 words, no colon, no claim verb. Names the method class (foundation models) and the target concept (generalist medical AI).

**Summary (abstract).** Unstructured, one paragraph, about 164 words, 7 sentences, no citations, no numbers. Moves: (1) context, rapid development of flexible reusable models; (2) proposal, "We propose a new paradigm" and the coined term with acronym; (3 to 5) definition of the paradigm (self-supervised, multimodal inputs, flexible outputs); (6) "Here we identify" high-impact applications and technical capabilities; (7) implication, expected challenges to regulation, validation and dataset collection.

**Introduction (equivalent, unheaded).** 7 paragraphs (3, 5, 7, 2, 2, 6, 3 sentences). Funnel: P1 to P2 define foundation models and in-context learning; P3 states the gap (most FDA-approved models cover one or two tasks), opened concessively ("Although there have been early efforts"); P4 to P5 give the aim ("Here we outline"); P6 introduces three defining capabilities with a Fig. 1 pointer; P7 is a three-sentence roadmap ("We list concrete strategies", "Furthermore, we describe", "Finally, we point out").

**Framework section ("The potential of generalist models in medical AI").** Plays the role of methods. Two-paragraph lead-in, then four subsections: flexible interactions (3 paragraphs), dynamic task specification and multimodal inputs and outputs (each one long paragraph with run-in heading), medical domain knowledge (5 paragraphs). Each subsection contrasts current practice ("In current practice, AI models typically handle a narrow set") with the GMAI capability, then gives a concrete example query introduced by a colon. Evidence comes from named existing systems (GPT-3, PaLM, Gato) plus citations, not data.

**Use cases section (equivalent of results).** Two-sentence lead-in, six parallel subsections of 2 to 3 paragraphs and 8 to 14 sentences each. Template: (1) open with a scenario or category claim ("GMAI enables a new class of bedside clinical ..."); (2) describe how GMAI would work, often with a hypothetical patient vignette; (3) state requirements, frequently with the fixed formula "A solution needs to ..."; (4) point to prior work where available. This parallel template is the key device for presenting "results" without data.

**Opportunities and challenges (equivalent of discussion).** Split into paradigm shifts (controllability, adaptability, applicability: framed as benefits with brief caveats) and challenges (validation, verification, social biases, privacy, scale: framed as problem then mitigation). Each subsection opens with a topic claim naming the issue ("GMAI models will be uniquely difficult to validate"). Each risk is paired with a remedy (off-label warnings, uncertainty expression, deidentification, distillation, audits). This section doubles as the limitations; there is no separate limitations paragraph.

**Conclusion.** Two paragraphs, nine sentences. Paragraph 1 opens with a short, strong 8-word claim, then summarises the defining traits. Paragraph 2 opens with a concessive ("Despite their promise, ...") naming validation, compute cost and data access, then ends with a direct appeal to the AI community and a long (40-word) closing sentence listing benefits for patients and clinicians. The claim is restated at the level of potential, not demonstrated fact.

**Back matter.** Order: Acknowledgements (thanks to named colleagues, then funding by initials and grant numbers), Author contributions, Competing interests, then publisher sections (Additional information with correspondence line, Peer review information naming reviewers, Reprints and permissions, Publisher's note, rights line). No data or code availability statements (perspective). Author contributions are free text by initials, not CRediT: one sentence each for conception, design, synthesis and writing, illustrations, and a closing "all authors" feedback sentence. Competing interests list each conflicted author by initials and end with a standard sentence that the other authors declare none.

**Figures and tables.** Two figures, no tables, no boxes. Captions open with a short title sentence that is a noun phrase ("Overview of a GMAI model pipeline."), then panel descriptions led by bold lowercase letters ("a, ..."). Panel text runs 10 to 116 words. Abbreviations (GMAI, EHRs) are not expanded in captions. Reused third-party images carry a credit and licence line in the caption with a citation.

# Checklist candidates

- Title a perspective with a descriptive noun phrase that names the technology and the target concept, without a colon or claim verb. [strong]
- Write the summary as one unstructured paragraph that moves from context to "We propose" to definition to "Here we identify" to implication, with no citations. [strong]
- Coin at most one new acronym for the central concept, define it in the summary, and use it consistently throughout. [strong]
- Spell out an organisation or term used only once instead of abbreviating it. [strong]
- End the introduction with an explicit roadmap paragraph using ordinal signposts (We list, Furthermore we describe, Finally we point out). [strong]
- Restrict "we" to the summary, the aim or roadmap paragraph and the closing call to action; let the concept be the grammatical subject in body sections. [strong]
- Give each use case the same internal template (scenario, how the system works, "A solution needs to" requirements, prior evidence). [strong]
- Pair every challenge with a concrete mitigation in the same subsection. [strong]
- Anchor scale or impact claims with a specific number and a citation in the same sentence. [strong]
- Use present tense for the state of the field, present perfect for recent literature, and "can" or "will" for the proposed paradigm; avoid stacking hedges. [strong]
- Keep body sentences mostly between about 18 and 32 words; reserve very short sentences for key claims. [strong]
- Avoid semicolons; use colons only to introduce a named concept or an example query. [strong]
- Introduce a coined label in parentheses after describing it, then reuse it as a subsection heading. [strong]
- Place superscript citations directly after the specific term they support when a sentence lists several techniques. [strong]
- Open the conclusion with a short declarative claim and close it with a direct call to the community. [strong]
- Write figure captions as a short title phrase followed by lettered panel descriptions; credit reused images with licence and citation. [strong]
- Cite every illustrated panel in the main text. [weak] (Fig. 2a and 2b are not referenced in body text.)
- Write author contributions as short free-text sentences by initials grouped by role. [strong]

# Notable deviations

- Visionary wording is allowed at the edges: the conclusion says foundation models could transform healthcare and speaks of unprecedented possibilities, which stricter clinical journals would flag as promotional. Treat this as acceptable only for a Nature perspective.
- Em dashes are used (about four, as paired appositives, including in the first sentence). Our house style forbids them; replace with parentheses or commas.
- No introduction heading, limitations paragraph, or data and code statements (Nature perspective format); author contributions are not CRediT.
- Abbreviations are defined only in the summary and not redefined in the main text, contrary to the common rule of defining again at first main-text use.
- Abbreviations in figure captions are not expanded, unlike many clinical journals that require captions to stand alone.
- Hedging is light and modal-based ("can", "will") rather than verb-based ("suggest", "indicate"), appropriate for a position piece but too strong for original research.
- Fig. 2a and 2b are never cited in the body text.
- Use-case evidence is uneven (citation density from 1 in 14 to 8 in 9 sentences).
