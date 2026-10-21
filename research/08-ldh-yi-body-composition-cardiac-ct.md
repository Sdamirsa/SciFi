# Paper

Yi J, Marcinkiewicz AM, Shanbhag A, et al, Slomka PJ. AI-based volumetric six-tissue body composition quantification from CT cardiac attenuation scans for mortality prediction: a multicentre study. The Lancet Digital Health, 2025.

- Journal: The Lancet Digital Health, 2025;7(5):100862, DOI 10.1016/j.landig.2025.02.002
- Article type: original research (retrospective multicentre prognostic study, AI imaging biomarker)
- Word count estimate: main text about 2400 to 2600 words; structured abstract about 270 words; 2 tables, 5 figures, about 25 references, 12 supplementary tables
- Source used: medRxiv preprint, https://www.medrxiv.org/content/10.1101/2024.07.30.24311224.full.pdf and https://medrxiv.org/node/844751

**Source caveat.** The published version could not be read: thelancet.com failed, ScienceDirect and europepmc.org block robots, PubMed and the Europe PMC API were rate limited, and no PMC record was found. This analysis uses the preprint, which already follows the Lancet structure (structured abstract, Research in context panel, Lancet back matter). Copyediting will have standardised some statistics formatting, so treat the numeric formatting notes as preprint habits.

# Global patterns

**Sentence length.** In a sample of about 20 sentences, Results sentences run 9 to 18 words and Introduction and Discussion sentences run 18 to 30. The outliers are the 58-word aim sentence and a 49-word Discussion sentence. Paragraphs have 4 to 6 sentences (70 to 150 words). Results paragraphs are shorter, except one subgroup paragraph of about 185 words of chained HRs.

**Voice and person.** Methods use mostly passive voice ("was segmented", "were summarized as median"). "We" appears at key decision points: the aim ("We aimed to evaluate"), the analytic choice ("We evaluated the prognostic value of"), the Discussion opener ("We developed"), the limitations ("We did not manually annotate"), and the conclusion ("we demonstrated"). "Our" marks the group's own prior tool ("our previously validated EAT segmentation model").

**Tense.** The Introduction uses present tense for established facts and current practice ("are routinely obtained", "remains scarce"). Present perfect is used for the state of the literature ("have shown", "have not been evaluated"), and simple past for single prior studies. Methods and Results are in past tense. References to figures use present tense ("are shown in Figure 3"). The Discussion uses past tense for own findings ("We showed") and present for interpretation and implications.

**Hedging and certainty.** The paper leans assertive. Results contain no hedges, and association language ("was associated with an increased ACM risk") sits next to quasi-causal verbs ("significantly increased death risk"). Discussion certainty verbs (showed, demonstrated, reveals) outnumber modals. Hedges cluster in implications and feasibility ("could potentially provide additive prognostic value", "may be important", "can be performed automatically"). "Suggest" and "likely" are absent. Strong claims are anchored by a number in the same sentence in the abstract and Results (adjusted HR with interval and p). In the Discussion, claims are anchored by citation clusters rather than numbers.

**Punctuation.** Colons are almost absent from the prose. Semicolons appear only once or twice in the whole paper (both in "; however," style). There are no dashes. Hyphens carry compounds and ranges ("T5-T11", "end-to-end"). Parentheses are heavy and hold abbreviations, HU thresholds, units and statistics. In-sentence lists are comma series with "and", often long (five tissue names in one noun phrase).

**Abbreviations.** Density is high (about 17, for example CTAC, ACM, EAT, VAT, SAT, IMAT, HU, TPD). They are defined as "full term (ABBR)" at first use in the abstract and again in the Introduction. Several tissue abbreviations are not re-expanded in Methods, and CAC and the vertebral labels are used without expansion. Nearly all defined abbreviations are reused many times. Figure captions act as abbreviation keys.

**Numbers and statistics.** The pattern is "adjusted HR 2.39 [1.92, 2.96], p<0.0001", with the interval in square brackets, a comma separator, and often no "95% CI" label after first use. The abstract labels the first interval "95% CI". p values are given to four decimals or as p<0.0001. Counts are "610 (6.2%)", with the percentage precision varying (55% vs 6.2%). Medians appear as "65 (57-73) years" in one place and with square brackets in another. Thousands have no separators (9918). Runtime is given as mean±SD seconds.

**Citation placement.** Numbered superscript or bracketed references. They are mostly at sentence end, but sit mid-sentence after a list item when each item has its own source. Discussion context paragraphs cluster 8 to 13 citations. No reporting guideline (TRIPOD, STROBE, CLAIM) is cited. The Declaration of Helsinki is cited.

**Transitions.** Paragraphs open with a topic sentence naming the subject. Connectives are few ("Importantly,", "Similarly,", "Lastly,", "In conclusion,").

**Tone.** Mostly sober, with mild promotional drift: "first comprehensive volumetric", "simple", "robust", "holistic", "easily", "vital", "alarmingly". There is no "novel", "groundbreaking" or "unlock".

**Word choice.** Technical, noun-heavy and jargon-dense, but plainly structured. "Opportunistic" is the framing keyword for reusing existing scans.

# Local patterns by section

**Title.** A descriptive noun phrase plus a colon subtitle naming the design ("a multicentre study"). At about 20 words, it is long. It names the method (AI-based volumetric), the scope (six-tissue), the data (CT cardiac attenuation scans), the outcome (mortality prediction) and the design. It is not a declarative claim. The preprint title carried a claim verb ("enhances"), and the published title is neutralised to "for".

**Abstract.** Background, Methods, Findings, Interpretation (plus Funding), about 270 words. Background states the scan's current narrow use ("only utilized for attenuation correction and visual calcium estimation") and the aim. Methods give the registry, anatomical range, tissues and adjustment set. Findings give runtime, then n, sex, follow-up, deaths, then five adjusted HRs with intervals and p. Interpretation is one sentence: routine scans "contain important volumetric body composition biomarkers".

**Research in context panel.** Evidence before this study is about 176 words. It names the databases (PubMed, Google Scholar), the search terms and the search date, gives the hit count (34 articles), and states the gap (three or fewer tissues, no CTAC, no EAT). Added value is three sentences, about 107 words. Implications is two sentences, about 48 words, and is clinically oriented ("at the point of care").

**Introduction.** Four paragraphs, about 310 words, a tight funnel:
1. A routine scan is underused (2 citations).
2. Body composition matters clinically, and the gap is that CTAC-derived measures have not been studied.
3. Prior AI work covered few tissues and single slices, so the predictive value "remains unexplored" (9 citations).
4. A single 58-word sentence states the aim and the approach ("We aimed to evaluate CTAC's value for patient risk assessment").

No results are previewed.

**Methods.** Six subsections: Study population; CTAC image acquisition parameters; Clinical data and existing risk factors; Body composition segmentation and quantification; Statistical analysis; Role of funding source. Ethics (IRB at each site, Declaration of Helsinki) sits in Study population, with no consent sentence. The model is TotalSegmentator plus HU thresholds plus the group's prior EAT model, with details in the supplement. Evaluation is purely prognostic (Cox, Youden cutoffs, Kaplan-Meier). The statistics paragraph (about 150 words) gives tests per variable type, two-sided p<0.05, summary statistics and software version. No reporting guideline is named.

**Results.** Three subsections in fixed order: cohort (flowchart figure, Table 1 baseline characteristics), whole-cohort predictors (Table 2, Figure 3 forest plot, Kaplan-Meier figures), and subgroups (supplementary tables). Each paragraph points to a figure or table. Comparisons are written as "high X was associated with increased/lower risk (adjusted HR ..., p...)". Example: "Patients with high bone attenuation were at lower risk". There is no interpretation or hedging. Runtime is reported as a result.

**Discussion.** Five paragraphs plus "In conclusion,":
1. Citation-free summary of findings and feasibility ("We developed AI-based volumetric CTAC-body composition segmentation").
2. Clinical context (obesity, sarcopenia), 13 citations.
3. Prior work and the priority claim ("To our knowledge", "first").
4. Mechanism (EAT, visceral obesity), opened by "Importantly,".
5. Limitations (about 150 words, second to last), opened by "Our study has several limitations." Six first-person items ("We did not..."). Two are mitigated. Retrospective design is not named. Future work is folded into the last item.

The two-sentence conclusion is assertive ("we demonstrated the utility of performing opportunistic volumetric..."). Modals attach only to feasibility.

**Back matter.** Order: Contributors; Declaration of interests; Data sharing; Supporting information. "Role of the funding source" ends Methods (Lancet convention, boilerplate wording). Contributors are narrative with initials ("JY developed the algorithms"). Interests are listed per author, closing with a statement that the others declared none. Data sharing makes code "available upon reasonable written request", lists software versions, and is silent on patient data.

**Figures and tables.** Captions give a short title phrase, then panel-by-panel detail with cutoffs, and double as abbreviation keys (HR, adjusted vs unadjusted models defined).

# Checklist candidates

- Title the paper as a descriptive phrase naming method, data, outcome, then a colon and the design ("a multicentre study"). [strong]
- Avoid claim verbs in the title. Prefer "for mortality prediction" over "enhances". [weak] (changed only at publication)
- Use the Lancet structured abstract (Background, Methods, Findings, Interpretation, Funding) and give n, follow-up, events and adjusted effect sizes with intervals in Findings. [strong]
- In the Research in context panel, name the databases, search terms, search date and hit count, then state the gap in one sentence. [strong]
- Keep the Introduction to about four paragraphs that funnel from an underused resource, to clinical relevance, to the limits of prior work, to the aim. [strong]
- End the Introduction with an explicit "We aimed to..." sentence and do not preview results. [strong]
- Place IRB approval and the Declaration of Helsinki in the first Methods subsection. [strong]
- State the consent or waiver of consent explicitly. [weak] (missing)
- Write a Statistical analysis paragraph naming each test by variable type, the sidedness, the alpha, the summary statistics and the software with version. [strong]
- Name a reporting guideline (TRIPOD for prognostic models). [weak] (absent; add it)
- Put "Role of the funding source" as the last Methods subsection. [strong]
- Order Results as cohort and flowchart, then the main analysis, then subgroups, each paragraph pointing to a figure or table. [strong]
- Report every effect as point estimate, interval and p value in one parenthesis after the claim. [strong]
- Use one bracket and range style for intervals and IQRs throughout. [weak] (mixed brackets and hyphens)
- Keep Results free of interpretation and hedges. [strong]
- Open the Discussion with a citation-free summary paragraph beginning "We developed/We showed". [strong]
- Write limitations as one paragraph, second to last, opened by "Our study has several limitations", each item in the first person. [strong]
- Pair each limitation with a mitigation. [weak] (two of six)
- Open the conclusion with "In conclusion," and restate the main claim with feasibility. [strong]
- Avoid colons and semicolons in running prose. [strong]
- Define abbreviations at first use in the abstract and again in the main text. [weak] (several not re-expanded in Methods)
- Use captions as abbreviation keys. [strong]

# Notable deviations

- Effect sizes are stated with association and quasi-causal verbs ("increased death risk") and no hedging, which is stronger than typical observational-study advice.
- The conclusion claims added prognostic value without qualification. Hedges attach only to feasibility.
- Mild promotional words ("first", "holistic", "robust", "vital", "alarmingly") appear despite Lancet sobriety norms.
- No reporting guideline is cited for a prognostic model study.
- No segmentation accuracy evaluation is reported. Absence of manual annotation is justified by cohort size.
- The aim is a single 58-word sentence, and one Discussion sentence reaches 49 words.
- Statistical formatting is inconsistent (brackets vs parentheses vs hyphen ranges, 0 vs 1 decimal percentages). Do not imitate this.
- Code is available only on request, which is weaker than npj Digital Medicine expectations. Contributors are narrative, not CRediT.
