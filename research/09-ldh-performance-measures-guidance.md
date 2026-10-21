> SOURCE NOTE: The publisher version could not be fetched (ScienceDirect, thelancet.com and the Utrecht PDF were all blocked), and it is not in PMC. This analysis uses the full text of the arXiv preprint v1 (2412.10288), which has the same authors and argument. Metadata were confirmed via EuropePMC. Lancet editing probably changed surface features (it uses "Panel" for "Box", unnumbered headings, and CIs written with "to"). Treat the punctuation and number findings as the authors' style, not house style.

# Paper

Van Calster B, Collins GS, Vickers AJ, Wynants L, Kerr KF, Barreñada L, Varoquaux G, Singh K, Moons KGM, Hernandez-Boussard T, Timmerman D, McLernon DJ, van Smeden M, Steyerberg EW. Evaluation of performance measures in predictive artificial intelligence models to support medical decisions: overview and guidance. The Lancet Digital Health 2025.

- Journal: The Lancet Digital Health, 7(12):100916 (Dec 2025). The byline also includes the STRATOS initiative Topic Group 6.
- Type: review, specifically a methodological guidance review (EuropePMC: Review). It includes a worked case study with real data.
- Length: about 7500 to 8500 words of main text, with 4 tables, 4 figures, 1 box, 148 references and a supplement.
- Source used: https://arxiv.org/html/2412.10288 (preprint full text). Metadata came from EuropePMC and https://researchinformation.umcutrecht.nl/en/publications/evaluation-of-performance-measures-in-predictive-artificial-intel/

# Global patterns

**Sentence and paragraph length.** In a sample of 20 sentences, most run 12 to 30 words (median about 22). Verdicts are short, 8 to 12 words ("The discrimination slope and MAPE are improper."). The longest run 36 to 40 words. Paragraphs vary: one-sentence paragraphs of 25 to 40 words for key points, a typical 5 to 8 sentences (120 to 200 words), and explanatory paragraphs of up to 12 sentences (about 340 words).

**Voice and person.** "We" is the authorial guide and judge. It appears when the paper states aims ("We present a taxonomy"), defines terms ("We define two key characteristics"), sets scope ("We do not discuss") and takes positions ("We argue", "we do not agree"). The background paragraphs have no "we". Passive voice is used for literature and for data provenance (e.g. a model "was developed", data "were recruited", measures "have been suggested").

**Tense.** Present tense is used for definitions, properties of measures and the argument ("AUROC is a semiproper measure"). Past tense is used for case-study facts and results ("ADNEX had an O:E ratio of 1.23"). The Discussion summary uses past tense for what the paper did ("We distinguished between five domains") and present tense for the claims. Present perfect is used for the state of the literature ("have been proposed", "has received a lot of attention").

**Certainty.** The paper is unusually assertive for a review. Mathematical properties are stated as flat facts: "is improper", "are not strictly proper", "There are no grounds to call AUROC misleading". It names practices "outdated" and calls a criterion "practically unachievable". The authors disagree openly with other guidance ("we do not agree with recommendations to use AUPRC"). Hedges are kept for empirical and contextual claims: "may", "can", "often", "tends to", "generally", "in our experience". Strong claims are anchored to a property defined in Section 4 (properness) or to a case-study number. Literature claims get citation ranges.

**Punctuation.** There are almost no semicolons. Colons are moderate: they introduce lists and the key recommendation ("in most circumstances: AUROC, calibration plot, ..."). Parentheses are very heavy and do several jobs: abbreviations, "(i.e., ...)" and "(e.g., ...)", cross-references "(Table 2)", "(Box 1)", case-study numbers with CIs, and even "(repeated)" inside a phrase. There are no em dashes in the prose. In-sentence lists use serial commas with "and", and are numbered "(1) ... and (2) ..." when two criteria are contrasted.

**Abbreviations.** There are many, about 25 (AUROC, AUPRC, ECE, ICI, NB, DOR, MCC, NRI and others). AI is defined in the abstract and again at its first use in the main text. AUROC appears undefined in the abstract and the introduction and is first expanded in Section 5.1, which is a lapse. Most abbreviations are defined in their own subsection and reused. Table 4 acts as a de facto glossary. ADNEX, transIOTA and "c.q." are never expanded.

**Numbers.** Point estimates in the text have two decimals with the CI in parentheses. The label "95% confidence interval" is spelled out at first use and dropped afterwards. Tables use three decimals. Counts are given with prevalence in parentheses: 894 women, 434 with malignancy (prevalence 49%). Thresholds are written both as percentages (10%) and as decimals (t = 0.10). Thresholds are translated into harm ratios ("up to 9 false positives per true positive", odds 1:19). The CI method is stated once (percentile bootstrap, 1000 resamples). There are no p values. The paper argues that CIs are inappropriate for clinical utility.

**Citations.** Numbered superscripts, mostly at the end of the clause or sentence. Ranges and lists are common (33 to 37, or 21,22), and density is high in technical sections (about 2 to 3 per 100 words). Background paragraphs have one citation per example. The paper's own argument paragraphs (aims, recommendations) carry none. Reporting guidelines are cited only in the Discussion: TRIPOD, TRIPOD+AI and TRIPOD-Cluster.

**Transitions.** Paragraphs open with a topic sentence that names the concept. Links are plain ("In contrast", "For instance", "Consequently", "Ultimately"). The arc runs from many models, to confusion over measures, to harm, and then to "the aims of this paper".

**Tone and word choice.** Sober and argumentative, with no promotional vocabulary ("abounds" and "myriad" are the only colour). Technical terms are first defined in a plain sentence and restated in lay terms. Nominalisations are moderate.

# Local patterns by section

**Title.** A descriptive phrase plus a colon subtitle ("overview and guidance"), 18 words. It names the object (performance measures), the model class (predictive AI) and the purpose (medical decisions), and labels the genre in the subtitle. The preprint title was shorter ("Performance evaluation of ..."). Editing made it longer and more explicit.

**Abstract.** Unstructured, about 240 words, three short paragraphs in the preprint. The moves are: abundance of measures; why the choice matters (harm, cost); aim; scope (binary outcome); the 32 measures in five domains; the two key characteristics as (1) and (2); the counted verdict (17 meet both, 14 one, 1 neither, the F1 measure); a blunt finding on classification measures; and the explicit list of recommended measures. The numbers are counts of measures, not data.

**Introduction.** Four paragraphs, about 440 words. P1 describes the field with two concrete example models, one regression and one deep learning, one citation each. P2 covers the problem (disagreement on measures, harm) and defines external versus internal validation. P3 is the aim ("The aims of this paper are to assess...") with a roadmap sentence of four verbs and the scope. P4 is a single sentence that previews the bottom-line recommendation. The conclusion is placed up front.

**Methods equivalent.** Section 2 is a one-paragraph case study. It covers the clinical question, the model, the development data, the validation cohort (n, prevalence), the CI method, and code and data on GitHub. Ethics approval is not mentioned here. It is in the back matter.

**Framework sections.** Section 3 is the taxonomy (Table 1 gives the domains as target questions). Box 1 gives worked threshold reasoning with harm ratios. Section 4 defines the evaluation criteria (properness: strict, semi, improper; and clarity of focus). It also explicitly drops interpretability as too subjective.

**Body (Sections 5 and 6).** Each measure follows a repeated unit: definition, interpretation, critique (properness, costs), the ADNEX result with CI, and a verdict. Formulas go to the supplement. Calibration is laddered (mean, weak, moderate, strong). Section 7 reruns every measure after recalibration, and the improper ones "worsened remarkably". This turns the argument into evidence.

**Discussion.** Seven unheaded paragraphs. P1 summarises what was done, with counts, in past tense with "We". P2 argues for the core domains. P3 gives the core set and its context. P4 rebuts the class-imbalance argument. P5 is a numbered list of side topics (sample size, heterogeneity, TRIPOD+AI reporting). P6 gives limitations as scope exclusions, each briefly justified. P7 is a two-sentence conclusion that restates the principles at full strength.

**Back matter (preprint order).** Contributors (CRediT roles, by initials), then "Data sharing and ethics approval", then Conflicts of Interest (one line: none), then Acknowledgments (funding, with NIHR and NIH disclaimers). Data access is controlled: the full dataset is held at KU Leuven and not shared for privacy reasons, while the risks, outcomes and code are on GitHub.

**Figures and tables.** Captions are mostly a one-phrase title with "(panel A)" markers. Figure 4 has a long, explanatory caption. Table 2 uses symbols (++, +, minus) with a footnote. Table 4 gives categorical verdicts ("Recommended", "Inadvisable") with a reason column. Abbreviations are not expanded in the captions.

# Checklist candidates

- Preview the bottom-line recommendation at the end of the introduction, in one sentence after a colon. [strong]
- State scope limits in the aim paragraph (e.g. binary outcomes only) and repeat them in the limitations. [strong]
- Define every evaluation criterion explicitly before judging items against it, then apply it uniformly. [strong]
- Give each item a repeated micro-structure: definition, interpretation, critique, worked number, verdict. [strong]
- Anchor a methodological claim with a worked example from real data, including n, prevalence and CI. [strong]
- Spell out "95% confidence interval" at first use and use bare parentheses afterwards. [strong]
- Report a point estimate and CI to two decimals in the text. Tables may carry three. [weak; text and table values diverge]
- Translate decision thresholds into an interpretable harm ratio (false positives tolerated per true positive). [strong]
- Use "we" for aims, definitions and positions, and the passive voice for data provenance and literature. [strong]
- Use the present tense for properties and claims and the past tense for case-study results. [strong]
- Avoid semicolons. Use colons only to introduce lists or the key recommendation. [strong]
- Put definitions, cross-references and estimates in parentheses rather than in subordinate clauses. [strong]
- Define an abbreviation at first use in the abstract and again in the main text. [weak; true for AI, not AUROC]
- Disagree with other guidance explicitly and give the reason in the same sentence. [strong]
- Make the Discussion open with a summary of what was done, including counts. [strong]
- End with a short conclusion paragraph (two sentences) that restates the principles and the recommended set. [strong]
- Cite the relevant reporting guideline (TRIPOD+AI) and recommend sharing code, protocol and data. [strong]
- Provide a summary guidance table with categorical verdicts and a reason column. [strong]
- Give CRediT roles by initials, and state controlled data access with the reason and what is shared instead. [strong]

# Notable deviations

- Very assertive, verdict-style language for a review ("improper", "outdated", "no grounds", "we do not agree"). This is justified by formal properties, not by empirical evidence. Do not transfer it to empirical original research.
- One-sentence paragraphs used for emphasis (the recommendation, the count of measures).
- The key recommendation appears in the abstract, at the end of the introduction, in the discussion and in the conclusion: deliberate four-fold repetition.
- Heavy use of parentheses, including "c.q." and "(repeated)" inside phrases. Abbreviations are dense and AUROC is used before it is defined.
- No limitations about the evidence base, only scope exclusions.
- There is a numbered list inside a Discussion paragraph, and funding sits under Acknowledgments (preprint only).
- The preprint has numeric inconsistencies (an ECE estimate outside its own CI, text versus table rounding). Cross-check every number between text and tables.
- Ranges are written with hyphens in the text and with commas in the tables. Lancet style uses "to", so do not copy the range format from this source.
