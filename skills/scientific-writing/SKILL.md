---
name: scientific-writing
description: Write, revise, outline or audit biomedical and clinical-AI manuscripts (original research, reviews, perspectives) in the register of npj Digital Medicine, JAMIA, Nature-portfolio journals, The Lancet Digital Health and European Heart Journal. Use this skill whenever the user asks for a title, abstract, introduction, methods, results, discussion, limitations, figure or table caption, back matter (data availability, author contributions), a cover letter to a journal, a response to reviewers, or any "make it sound like a paper", "tighten", "check my manuscript", "is this ready for submission", "write the methods section", "draft the abstract" request, even if they do not say "scientific writing". Also use it when the user pastes manuscript text and asks for feedback, or wants a manuscript checked for abbreviations, claims without evidence, sentence length, or promotional wording.
---

# Scientific writing

This skill encodes the writing conventions learned from 14 published papers (3 npj Digital Medicine, 2 JAMIA, 3 Nature, 1 Nature Cancer, 1 Nature Communications, 2 Lancet Digital Health, 1 European Heart Journal, plus their figures and tables), merged with the house rules of the researcher who uses it. The global rules below apply to every sentence of every section. The per-section files in `references/` apply to one part of a manuscript at a time. Read only what the task needs.

## 1. Decide the mode and the target

Work out two things from the request before writing anything.

**Mode**
- **Draft**: write new text for a section or a whole manuscript. Gather the material first (results, numbers, figures, prior work the user gives you), then read the section file, then write.
- **Revise**: the user gives existing text. Make the smallest set of changes that fixes real problems, keep their structure and voice, and list what you changed and why. Do not rewrite a paragraph that only needs one sentence fixed. The user prefers reviewing proposed changes before they are merged, so present edits as a change list or a marked-up version rather than silently replacing the text.
- **Review**: audit a manuscript or section against `references/checklist.md`, run `scripts/check_manuscript.py`, and report findings grouped by severity with line references. Do not rewrite unless asked.
- **Plan**: produce an outline, word budget and display-item plan from `references/organization.md` before any prose exists.

**Target journal**
Look for a journal name in the request, in a header line of the manuscript (for example "Target: Lancet Digital Health"), or in the file name. If one is named, read its entry in `references/journal-profiles.md` and apply it. If none is named, use the balanced default described in section 3 and say in one line that you used the default and which choices a journal would change (Results tone, Methods position, abstract format). Never block the task to ask for the journal; the default is designed to be safe for all five families.

## 2. Global rules (the whole scientific register)

These are what the 14 papers agree on, tightened where the user's house rules are stricter. Each rule carries its reason so you can apply it with judgement rather than mechanically.

**Sentences and paragraphs**
- Sentences run 15 to 30 words, hard ceiling 40. Published medians sit at 22 to 25, and every sentence above 40 words in the corpus was either a list that belonged in a table or two sentences fused by a semicolon.
- No sentence under about 8 words in running prose, except a deliberate claim sentence that opens a Discussion or Conclusion. Fragments and one-line verdicts read as blog style.
- Paragraphs run 80 to 150 words, 4 to 7 sentences, one idea each. The first sentence states the point of the paragraph (topic sentence). The last sentence does not introduce a new idea.
- Within a paragraph, order sentences from known to new: a claim, its evidence, its qualification, then the bridge to the next paragraph. Across paragraphs, the funnel runs from the field to the problem to the gap to what was done.

**Voice, person and tense**
- Use "we" for the aim, design decisions, interpretations, limitations and conclusions. Use impersonal or passive constructions for routine procedures ("Reports were labelled by a cardiologist") and for definitions ("A foundation model is..."). Background paragraphs of the Introduction carry no "we".
- Past tense for what was done and what was found. Present tense for established facts, for what a figure or table shows ("Figure 3 shows"), and for interpretation and implications. Present perfect for the state of the literature ("have been proposed"). Do not switch tense inside a paragraph without a reason.

**Claims and evidence**
- Every claim carries its evidence in the same sentence or the one before it: a number with its uncertainty, a figure or table pointer, a citation, or an explicit logical step from something already established. A sentence with none of these is an opinion and must be cut or hedged.
- Match verb strength to evidence. "Demonstrate" and "show" belong to measured results with uncertainty. "Suggest", "indicate" and "may" belong to mechanisms, explanations and implications. "Confirm" needs an independent dataset. Counts and measured values are never hedged.
- Report an unfavourable or null result as plainly as a favourable one, then give one explicitly hedged explanation.
- Keep claim strength identical across title, abstract, Results and conclusion. The corpus shows abstracts that promise "a robust foundation" while the Discussion calls the same work a proof of concept; reviewers notice.

**Abbreviations**
- Define an abbreviation at first use in the abstract and again at first use in the main text, in the form "full term (ABBR)". After that use only the abbreviation. Never redefine it later in the main text.
- Introduce an abbreviation only if it is used at least three more times. A term used once or twice is written out. This single rule removes most of the clutter seen in the corpus (RAG, IRB, GPU defined and then abandoned).
- One term for one concept: do not alternate EHR and EMR, AUC and C-statistic, or two expansions of the same acronym.
- Figure and table captions and the Research in context panel define their abbreviations again so they stand alone.
- Do not abbreviate in the title. Keep abbreviations out of subsection headings where possible.

**Numbers and statistics**
- Counts with percentages: "223 (91.0%)" or "91.0% (223/245)" when the denominator varies.
- Effects with uncertainty and the test result in one parenthesis after the claim: "adjusted HR 2.39 (95% CI 1.92 to 2.96), p<0.0001". Spell out "95% CI" at first use, then drop it. Use "to" for ranges in text, never a hyphen or comma, so ranges and negative numbers cannot be confused.
- One decimal place for percentages, two for AUROC and similar metrics, three for p values, "p<0.001" below that. Keep the same precision for the same quantity in abstract, text, tables and figures.
- Give a confidence interval for every headline metric, however the result was obtained (bootstrap for AUROC and accuracy, exact binomial for proportions). Eight of the fourteen papers reported none; that is a weakness of the corpus, not a licence.
- Say whether a difference is absolute (percentage points) or relative, and pair any normalised or relative figure with the absolute values in parentheses.
- Use "significant" only for a comparison that has a reported test and p value or CI. Everyday senses ("a significant 81.5%") are banned.
- Thousands separator from 10,000 upwards; spell out numbers below ten unless they carry a unit, a percentage or sit in a list of measured values.

**Citations**
- Place the citation directly after the claim it supports. When one sentence lists several named methods or studies, cite each one where it is named, not all at the end.
- One or two citations per claim; cite a range for a field-level statement. Do not cite in the abstract (Nature allows it; nobody else does).
- Name the reporting guideline followed (TRIPOD+AI for prediction models, TRIPOD-LLM for LLM studies, STARD for diagnostic accuracy, PRISMA 2020 for reviews, CONSORT-AI for trials, CLAIM for imaging) in the first Methods paragraph. None of the fourteen papers did; all should have.

**Punctuation and format**
- No colons and no semicolons in running prose. Replace a colon with a sentence break or "such as"; replace a semicolon with a full stop or a comma plus conjunction. Colons remain acceptable only inside captions after a panel letter, in structured abstract headings and in time or ratio notation.
- No em dashes and no en dashes anywhere. Use commas, parentheses, "to" for ranges and a sentence break.
- Parentheses carry abbreviations, pointers "(Figure 2b)", statistics and brief glosses. One parenthesis per sentence; nested brackets are a sign the sentence should be a table row.
- Lists inside a sentence use commas and "and". A list of more than four items, or any list whose items contain commas, becomes a numbered list in Methods, a table in Results or is cut.
- Cite display items as "Figure 2b" and "Table 1" (journal profiles say when "Fig." is required). Letter every panel; never refer to "left" or "right".

**Tone and word choice**
- No promotional, emotional or blog-style wording. Banned: novel, groundbreaking, revolutionary, remarkable, remarkably, striking, strikingly, exceptional, unprecedented, paradigm shift, cutting-edge, state-of-the-art (as praise), milestone, immense, drastically, dramatically, tremendous, exciting, powerful, unlock, leverage, game-changing, holistic, seamless. Treat with suspicion: robust, crucial, vital, importantly, interestingly, surprisingly, notably, promising, first (as a priority claim without "to our knowledge"). The corpus uses many of these; every instance would be cut by a Lancet or JAMIA editor and most were followed by a caveat in the next sentence, which is the sign the author knew.
- Prefer the plain verb: use, show, find, measure, compare, improve. Avoid utilise, leverage, delineate, encompass, synergise, and nominalisations where a verb will do ("we segmented" not "segmentation was performed by us").
- Clinical readers need technical terms glossed once in parentheses at first use (embedding, retrieval-augmented generation, in-context learning). Technical readers need clinical terms glossed the same way.
- British or American spelling follows the journal; be consistent within the manuscript. Nature-portfolio uses British spelling with -ize endings and no serial comma; Lancet uses British with -ise; JAMIA and EHJ accept either but EHJ is British.

**Flow and self-consistency**
- Every number that appears more than once (abstract, Results, Discussion, captions) must be identical. The corpus contains a paper giving the same improvement as 92%, 9.4% and 19.7%.
- Every figure, table and supplementary item is cited in the text at least once, in numerical order of first citation.
- Every Methods subsection has a matching Results paragraph and vice versa; every Results finding is picked up in the Discussion at least once.

## 3. The balanced default for Results and structure

When no journal is named, write as follows. This sits between the Nature-portfolio style (claim headings, interpretation inside Results) and the Lancet and JAMIA style (label headings, Results strictly descriptive), and either family can be reached from it with the small adjustments listed in `references/journal-profiles.md`.

- Section order: Introduction, Methods, Results, Discussion, with Methods first. A Nature-portfolio target moves Methods to the end and adds a design recap sentence at the top of each Results subsection.
- Results subheadings are descriptive labels that name the analysis ("Prognostic value of body composition measures"). A Nature-portfolio target may turn them into claim sentences.
- Results paragraphs describe; interpretation is limited to one closing sentence per subsection stating what the numbers mean, without mechanism or implication. Mechanisms and implications go to the Discussion.
- Structured abstract (Background, Methods, Results, Conclusions) of 250 words; unstructured 150 to 200 words for Nature-portfolio.
- Limitations are one paragraph, second to last in the Discussion, opening with "This study has several limitations", each limitation paired with its consequence and its mitigation.

## 4. Workflow

1. Identify mode, section(s) and target journal (section 1). If the request is ambiguous about scope, ask one question; otherwise proceed.
2. Read the relevant references: `references/organization.md` for a plan or a whole manuscript; the matching `references/sections/*.md` for a section; `references/figures.md`, `references/tables.md` and `references/captions.md` for display items; `references/journal-profiles.md` when a journal is named. For a review or perspective, each section file has an "In a review" block; use it.
3. Draft or revise. While writing, keep the global rules of section 2 open in mind; they override anything in the section files if the two ever conflict.
4. Run the checker on the result when the output is more than a few paragraphs: `python3 scripts/check_manuscript.py <file> --journal <name>`. Fix what it flags or explain in one line why a flag is a false positive (for example a colon inside a caption).
5. Self-review against `references/checklist.md`, section by section. Report remaining deviations to the user as a short list rather than silently leaving them.
6. For a Revise or Review task, present changes as a list (location, what changed, why), not as a silent rewrite. For a Draft task, deliver the text, then a short list of decisions you made that the user may want to change (journal defaults applied, numbers you did not have, claims that need a citation).

## 5. Where to look

| Task | Read |
|---|---|
| Outline, word budget, what goes in the supplement, Methods before or after Results | `references/organization.md` |
| Title | `references/sections/title.md` |
| Abstract, summary, Research in context, Translational perspective | `references/sections/abstract.md` |
| Introduction | `references/sections/introduction.md` |
| Methods, ethics, statistics paragraph, model reporting | `references/sections/methods.md` |
| Results | `references/sections/results.md` |
| Discussion, limitations, conclusion | `references/sections/discussion.md` |
| Data availability, code, contributions, funding, competing interests, acknowledgements, AI-use disclosure, reference format | `references/sections/back-matter.md` |
| Which figures to make, Figure 1 conventions, panels, colour | `references/figures.md` |
| Which tables to make, Table 1, cell formats, footnotes | `references/tables.md` |
| Caption titles, length, what a caption must contain | `references/captions.md` |
| Full audit list | `references/checklist.md` |
| npj Digital Medicine, JAMIA, Nature-portfolio, Lancet Digital Health, EHJ specifics | `references/journal-profiles.md` |
| What each source paper contributed and its known weaknesses | `references/sources.md` |
| Fill-in skeletons | `examples/skeleton-original-research.md`, `examples/skeleton-review.md`, `examples/abstract-variants.md` |
| Automated checks | `scripts/check_manuscript.py` |

## 6. Things this skill will not do

- It will not invent numbers, confidence intervals, sample sizes or citations. Where the user has not supplied a value, leave a bracketed placeholder "[n=?]" or "[REF]" and list it at the end.
- It will not soften a limitation the user names, and it will not raise a claim above what the design supports, even when asked to "make it stronger". It will say what evidence would justify the stronger claim.
- It will not reproduce text from the source papers. The references describe patterns, not wording.
