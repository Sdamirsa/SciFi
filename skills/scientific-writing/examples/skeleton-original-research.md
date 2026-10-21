# Skeleton: original research (balanced default, Methods before Results)

Fill each bracket. Every bracket that stays unfilled at delivery is listed back to the user. Word targets in parentheses. Delete this preamble and all guidance lines marked ">" before delivery.

Target: [journal or "default"]

---

# [Method or system] for [task or outcome] in [population or data]: [design]
> 10 to 16 words, no abbreviations, no claim verb.

## Abstract (250 words)

**Background** [One sentence: clinical problem with a number.] [One sentence: limitation of current practice or prior work.]

**Methods** [Design.] [Data source, sites, period, n development and n test.] [Reference standard.] [Method and comparator.] [Primary metric or outcome.]

**Results** [Headline value with 95% CI.] [Comparison as X versus Y with CI and p.] [One secondary number.] [One efficiency number if relevant.]

**Conclusions** [Claim at design strength.] [Condition for use or next validation step.]

> Define every abbreviation here; no citations; every number must reappear identically in Results.

## Introduction (300 to 550 words, 4 to 6 paragraphs)

[P1: the clinical stake with a number and citation. No "we".]

[P2: what is currently done and why it falls short, present perfect for the literature.]

[P3: the enabling idea, glossed for a clinical reader; define any coined term once with an example.]

[P4: the gap in one sentence, contrasting what prior work covers and what it does not.]

[P5: "We aimed to [verb] [method] for [task] using [data, n] against [comparator] with [primary outcome]." Then one sentence on the contribution.]

> No results preview. Aim sentence under 40 words.

## Methods

### Study design and ethics
[Design in one sentence.] [Committee name and number; consent or waiver and reason; Declaration of Helsinki; data use agreement.] [Reporting guideline followed; checklist in Supplementary [X].]

### Data source and population
[Sites, period, inclusion and exclusion with Figure 1 (flow).] [Development, validation and test sets with n; period or site separation.]

### Reference standard
[Who labelled, how many, qualifications, independence, consensus, label set, agreement with 95% CI.]

### [Model or intervention]
[Architecture or base model with exact version; parameters; temperature; max tokens; seeds; runs; hardware; software versions.] [Prompt anatomy in one line; full prompts in Supplementary [X].] [One sentence justifying the choice.]

### Outcomes and metrics
[Each metric with numerator, denominator, unit of analysis, tie rules.] [Primary metric named.]

### Evaluation design
[Comparators and baselines.] [Subgroups, sensitivity analyses, ablations.] [Human evaluation: raters, cases, blinding, scale.]

### Statistical analysis (100 to 200 words)
[Summary statistics by variable type.] [Tests by variable type.] [Model and adjustment set.] [CI method and resamples.] [Correction, sidedness, alpha.] [Missing data.] [Sample size rationale or statement that none was made.] [Software and version.]

> Lancet: add "Role of the funding source" here. Nature-portfolio: add "Statistics and reproducibility".

## Results

### Study population
[First sentence: n with the flow figure.] [Key characteristics with Table 1.]

### [Primary analysis label matching Methods]
[Figure 2 shows ... .] [Headline value (95% CI), p.] [X versus Y comparison.] [Exception or null result.] [One descriptive closing sentence.]

### [Secondary analysis label]
[Table 2 / Figure 3 ... .]

### Subgroup and sensitivity analyses
[Forest plot or summary table in main text; Supplementary Tables [X] for the rest.]

### [Human or clinician evaluation]
[Sample: cases and raters.] [One paragraph per axis.]

### Error analysis
[Named failure types with counts; Table 3 for examples.]

> Results paragraphs 60 to 130 words, no mechanism, no implication, no evaluative adverbs.

## Discussion (20 to 30% of text, 6 to 9 paragraphs)

[P1: "In this study, we ..." Principal findings with numbers, citation-free.]

[P2 to P4: one paragraph per main finding: the finding, the closest prior study with its numbers and the specific difference, one concrete clinical example of what the difference means.]

[P5: mechanism, hedged, tied to a result or citation; rival explanation named and checked.]

[P6: implications and conditions for use; regulatory status if high risk.]

[P7: "This study has several limitations. The most important is [X], which means [consequence]. [Mitigation or future study.] Second, ... .]

[P8: "In conclusion, ..." 60 to 120 words; claim at design strength; condition for use; stop.]

## Back matter (in journal order)

**Data availability** [Public: repository, accession, licence. Controlled: reason, route, data use agreement, re-identification prohibition. Derived resources: location.]

**Code availability** [URL, licence, version or DOI; third-party code; reason if withheld and what is offered instead.]

**Author contributions** [Journal format; guarantor; approval sentence.]

**Funding** [Grants with initials; no-role sentence.]

**Competing interests** [Per author; closing sentence.]

**Acknowledgements** [Named help; AI-use disclosure naming tool, version and task.]

## Display items plan

| Item | Type | Cited from | Content |
|---|---|---|---|
| Figure 1 | Flow diagram or design overview | Methods or first Results sentence | n per step |
| Table 1 | Baseline characteristics | First Results paragraph | median (IQR), n (%), stratified by [X] |
| Figure 2 | Primary result, multi-panel | Primary Results subsection | values on plot, CIs, n |
| Table 2 | Primary results with CIs | Primary Results subsection | models or exposures as rows, metrics as columns |
| Figure 3 | Secondary or subgroup | Secondary subsection | forest plot or calibration |
| Table 3 | Error taxonomy with examples | Error analysis | type, count, example |
| Supplementary | prompts, hyperparameters, extended tables, per-dataset curves | by number | |
