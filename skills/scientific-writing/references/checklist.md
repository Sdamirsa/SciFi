# Checklist

Use this for a Review task and as a self-check after a Draft. Work through it section by section. Report each failed item with its location and a one-line fix. Items marked (script) are also tested by `scripts/check_manuscript.py`; the rest need reading.

## A. Global: language

- [ ] Sentences 15 to 30 words, none above 40 (script).
- [ ] No sentence under 8 words in running prose except a deliberate opening claim (script).
- [ ] Paragraphs 80 to 150 words, 4 to 7 sentences, one idea, topic sentence first (script for length).
- [ ] No colons or semicolons in running prose; colons only in captions after panel letters, in structured abstract headings and in ratio or time notation (script).
- [ ] No em dashes or en dashes anywhere; ranges use "to" (script).
- [ ] At most one parenthesis per sentence; no nested brackets.
- [ ] Lists of more than four items, or items containing commas, are numbered lists or tables, not sentences.
- [ ] Banned promotional words absent; caution words justified (script).
- [ ] No everyday "significant"; every "significant" sits beside a p value or CI (script).
- [ ] Plain verbs; no utilise, leverage, delineate, encompass, synergise (script).
- [ ] Technical terms glossed in parentheses at first use for the other audience.
- [ ] Consistent spelling variant for the journal (script flags mixed -ise and -ize).
- [ ] No contractions, no rhetorical questions, no "note that" or "it is worth noting".

## B. Global: voice, tense, claims

- [ ] "We" only for aims, design decisions, interpretations, limitations and conclusions; none in background paragraphs.
- [ ] Past tense for what was done and found; present for established facts, figure pointers and interpretation; no tense switch within a paragraph without reason.
- [ ] Every claim has its evidence in the same sentence or the one before: a number with uncertainty, a figure or table pointer, a citation, or an explicit logical step from an established point.
- [ ] Verb strength matches evidence: demonstrate and show for measured results with CI; suggest, indicate and may for mechanisms and implications; confirm only with an independent dataset.
- [ ] Counts and measured values are not hedged; forecasts and mechanisms are.
- [ ] Unfavourable and null results reported plainly with one hedged explanation.
- [ ] Claim strength identical in title, abstract, Results, Discussion and conclusion.
- [ ] Association language for observational data; no causal verbs.
- [ ] "To our knowledge, this is the first" only after a search, and only in the Discussion.

## C. Global: abbreviations

- [ ] Each abbreviation defined at first use in the abstract and again at first use in the main text, as "full term (ABBR)" (script).
- [ ] No abbreviation defined that is used fewer than three further times (script).
- [ ] No abbreviation used before its definition (script).
- [ ] No abbreviation redefined later in the main text (script).
- [ ] One term per concept (EHR not EMR, AUROC not AUC and C-statistic) (script flags pairs).
- [ ] Captions, the Research in context panel and table footnotes define their abbreviations again.
- [ ] No abbreviations in the title; few in headings.
- [ ] The same expansion wording everywhere.

## D. Global: numbers, statistics, citations

- [ ] Counts as "n (x.x%)"; proportions from small samples as "x.x% (n/N)".
- [ ] Effects as "estimate (95% CI lower to upper), p=0.xxx"; "95% CI" spelled once (script flags mixed CI formats).
- [ ] One decimal for percentages, two for AUROC-type metrics, three for p or "p<0.001"; same precision for the same quantity everywhere (script flags mixed precision).
- [ ] A CI for every headline metric, with the method in Methods and the caption.
- [ ] Differences labelled absolute or relative; relative figures paired with absolute values.
- [ ] Thousands separator from 10,000; numbers under ten spelled out unless with a unit (script flags inconsistent separators).
- [ ] Citations placed after the claim they support, each named item cited where named; no citations in the abstract outside Nature.
- [ ] Reporting guideline named in the first Methods paragraph with the checklist supplied.
- [ ] Every number appearing more than once is identical everywhere (script flags repeated percentages that differ slightly; manual check needed).

## E. Title and abstract

- [ ] Title names method, task or outcome, and design where relevant; 10 to 16 words; no abbreviations, no claim verb outside Nature, no "novel".
- [ ] Abstract in the journal's format and length; headings verbatim.
- [ ] Background, aim, methods with n, headline results with uncertainty, conclusion at design strength.
- [ ] At least one head-to-head number as "X versus Y" with the same metric and decimals.
- [ ] No numbers absent from the main text; no citations; abbreviations defined.
- [ ] Companion panel (Research in context, Translational perspective, Key points) present where the journal asks.

## F. Introduction

- [ ] Four to six paragraphs, 300 to 550 words (longer only for Nature-portfolio).
- [ ] Opens on the clinical problem with a number, not on AI.
- [ ] Prior work and its limit; the enabling idea glossed; the gap in one sentence contrasting what prior work covers and what it does not.
- [ ] Aim sentence under 40 words naming data, method, comparator and primary outcome; design named.
- [ ] No results preview unless Nature-portfolio; there, a contributions list mapped to figures.
- [ ] Coined concepts defined once with an example and used by the same name throughout.
- [ ] No "we" before the aim paragraph; no promotional framing; no regulatory commentary.

## G. Methods

- [ ] Subheadings present, in data-flow order, mirrored in Results.
- [ ] Ethics committee and number, consent or waiver with reason, data use agreement, Declaration of Helsinki in the first subsection.
- [ ] Reporting guideline named.
- [ ] Data: sites, period, inclusion and exclusion, split sizes with n, period or site separation of test data, "external validation" used correctly.
- [ ] Reference standard: who, how many, qualification, independence, consensus, agreement with CI; LLM labels validated by humans.
- [ ] Model: exact version string, parameters, temperature, max tokens, seeds, runs, hardware, software versions, prompts in supplement, choice justified.
- [ ] Metrics defined with numerator, denominator, unit of analysis, tie rules, recoding.
- [ ] Statistical analysis paragraph: summary statistics, tests by variable type, model and adjustment set, CI method, correction, sidedness, alpha, missing data, sample size rationale, software version; Nature-portfolio reproducibility items.
- [ ] Role of the funding source (Lancet) as the last subsection.
- [ ] What was not done stated with the reason.
- [ ] No sentence over 40 words; covariate lists in tables or supplement.

## H. Results

- [ ] Opens with n and the flow figure, then Table 1; or with a data quality check for benchmarks.
- [ ] Order: cohort, primary, secondary, subgroups and robustness, human evaluation, error analysis.
- [ ] Each paragraph opens by naming the display item; when Methods comes last, one setup sentence first.
- [ ] Headline value with uncertainty; comparisons as "X versus Y" with fixed group order.
- [ ] No interpretation beyond one descriptive closing sentence; no mechanism or implication; no evaluative adverbs.
- [ ] Only headline values restated from tables; no prose-only number lists; no reference to absent columns.
- [ ] Every figure and table cited, in numerical order, by panel where relevant.
- [ ] Subheadings match Methods subheadings (labels) or state a clean finding (Nature-portfolio).
- [ ] Error analysis with a named taxonomy and counts.

## I. Discussion

- [ ] Opens with a citation-free principal findings paragraph starting "In this study, we".
- [ ] One paragraph per main finding with a named prior study and its numbers, and a concrete clinical example.
- [ ] Mechanism hedged and tied to a result or citation; rival explanation named and checked.
- [ ] Implications limited to what results support; next validation step named; regulatory status where high risk.
- [ ] Limitations in one paragraph, second to last, opening "This study has several limitations", most important first with its consequence, each paired with a mitigation or a concrete future study; covers design, reference standard, validation, generalisability, measurement.
- [ ] Conclusion of 60 to 120 words opening "In conclusion,"; claim at design strength; condition for use named; no new data or numbers.
- [ ] Discussion 20 to 30% of the text; no more than nine paragraphs; subheadings only where the journal uses them.

## J. Back matter

- [ ] Every heading the journal requires is present, in its order.
- [ ] Data availability distinguishes public, controlled and unavailable data with the route for each; licence named; controlled-access wording includes the data use agreement and re-identification prohibition.
- [ ] Code availability with URL, licence, version or DOI; reason given if withheld and what is offered instead; third-party code listed.
- [ ] Author contributions in the journal's format with a guarantor and the approval sentence.
- [ ] Funding with grant numbers and the no-role sentence.
- [ ] Competing interests per author including patents and spin-outs; closing sentence for the rest.
- [ ] AI-use disclosure naming each tool, version and task.
- [ ] Reporting summary or checklist supplied.
- [ ] References in the journal's style; house style used for drafts.

## K. Figures

- [ ] Figure 1 is the overview (design or pipeline, optionally with a worked example), cited from the Introduction or first Methods subsection.
- [ ] Flow diagram with n per step on the figure, cited from the first Results sentence.
- [ ] Primary result in one multi-panel figure with identical panel layout, values printed, CI error bars or bands, number-at-risk tables under survival curves.
- [ ] One representative panel in the main text with the full set in the supplement.
- [ ] Every panel lettered in the journal's case; the same case on art, caption and text; no positional references.
- [ ] Panel order matches text order; figures cited in numerical order of first citation.
- [ ] One fixed colour per arm or model across all figures; success, failure, not applicable in the same three colours; reference lines present; no colour as the only error marker.
- [ ] Every error bar defined; n per group on the figure or in the caption; exact p values only where they survive correction.
- [ ] Methods-only figures in the supplement; four to six main figures for a 3,500 word paper.
- [ ] Supplementary figures styled like main ones and each cited by number.

## L. Tables

- [ ] Table 1 (baseline characteristics or dataset summary) present for any cohort or multi-dataset study, stratified by the variable the paper reports differences on, with median (IQR) or mean (SD) and n (%).
- [ ] Primary results table with estimate (95% CI) cells alongside the primary figure.
- [ ] Rows are the things compared, columns the quantities; group order identical across tables, figures and prose.
- [ ] Units in headers; consistent decimals per column; prose values round from table values.
- [ ] Reference category stated for ratio tables; sign convention stated for delta tables; every ± and asterisk explained.
- [ ] Bold and underline conventions explained with their scope; no colour-only markers; no empty cells without a footnote.
- [ ] Every estimate inside its own CI; no reversed intervals.
- [ ] Unique titles; abbreviation key under every table; no letter reused for two meanings.
- [ ] Model specifications and patient characteristics in separate tables.
- [ ] Error taxonomy table with counts and examples where free text is produced.

## M. Captions

- [ ] Four parts: descriptive title of 3 to 12 words; panel descriptions in order; reading notes (n, what marks and error bars mean, test and correction, cut-offs, adjustment set, sort order, legend); abbreviations and credits.
- [ ] Length within the ranges (40 to 120 schematic, 40 to 80 single-panel, 80 to 200 multi-panel; table titles 5 to 14 words).
- [ ] Title is a label, not a claim (Nature-portfolio may add one plain finding sentence in the body).
- [ ] Stand-alone test passed.
- [ ] Caption matches figure type and the text that cites it; numbers in captions match the text; medians versus means aligned.
- [ ] Journal lead-in and panel-letter format applied.

## N. Organisation and consistency

- [ ] Section order and word shares per `organization.md` and the journal profile.
- [ ] Every Methods subsection has a Results counterpart and vice versa; every Results finding appears in the Discussion.
- [ ] Limitations are not scattered; the Discussion does not open with context.
- [ ] Results does not contain Methods material beyond one setup sentence per subsection.
- [ ] Supplementary items all cited by number with specific pointers.
- [ ] Total display items in main text within 4 to 7 (up to 8 for npj and Nature).
- [ ] No leftover drafting notes, duplicated sentences, duplicated captions, stray reference markers, or "nine specialties" followed by a list of eight (script flags some).
- [ ] Companion items present where required: Research in context, Translational perspective, Statistics and reproducibility paragraph, Reporting summary, Role of the funding source.
