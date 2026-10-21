# Discussion

## Paragraph sequence

1. **Principal findings.** One paragraph, citation-free, opening with "In this study, we..." or "We developed and validated...". Restate the two or three headline results with their numbers and the design in which they were obtained. Do not open with field context (one corpus paper did and buried its finding in paragraph two). A one-sentence summary paragraph is acceptable in Nature.
2. **One paragraph per main finding.** Each paragraph: the finding, the comparison with prior work (named studies, their numbers where comparable, and the specific way this study differs), and the practical meaning, often with one concrete clinical example (a generic recommendation versus a named drug with dose and route). Compare with concurrent systems by naming each and its specific weakness.
3. **Mechanism or explanation.** Why the result came out as it did, hedged ("A possible explanation is", "This may reflect"). Tie each explanation to a result or a citation. A rival explanation (test contamination, self-preference, data leakage) is named and checked against evidence.
4. **Implications.** Clinical use (registries, alerts, point-of-care), regulatory status (device class, EU AI Act risk tier) where the task is high risk, and deployment conditions. Keep to what the results support; "supports clinicians rather than replaces them" is the register, with the next validation step named.
5. **Limitations.** One paragraph, second to last, 150 to 250 words, opening with "This study has several limitations." Name the most important first and state its consequence for interpretation. Then the rest, each in the first person ("We did not..."), each paired with a mitigation already in the paper or with the concrete future study that would address it. Cover: design (retrospective, single centre, sample size), reference standard (single labeller, LLM-generated labels), validation (internal versus external, period), generalisability (one model family, one language, simulated versus real patients), measurement (no inter-rater agreement, no CIs where absent). A systematic review may use a separate "Limitations" heading; JAMIA accepts both.
6. **Conclusion.** One paragraph, 60 to 120 words, with or without a "Conclusion" heading depending on the journal. Open "In conclusion," restate the claim at the strength of the design, name the condition for use (external validation, prospective study, monitoring), and stop. No new data, no numbers, no "milestone". The strongest corpus closings state explicitly that the system is not ready for clinical use and what would make it so.

## Length and tone

- 20 to 30% of the main text. Six to nine paragraphs. The corpus extremes (16 unheaded paragraphs; a Limitations section longer than the Discussion) both hurt readability.
- Subheadings are unusual in Discussion for Lancet and Nature-portfolio; EHJ uses them; JAMIA accepts a "Limitations" subheading. Use them only when the journal does.
- Present tense for interpretation, past tense for what was found, "could" and "may" for implications. Verbs: suggest, indicate, support, is consistent with.
- The Discussion is the only place for "to our knowledge, this is the first" and it must be true after a search.
- Avoid regulatory or ethical sections longer than one paragraph unless the paper is about them.

## What reviewers look for and the corpus often lacked

- A direct comparison with the closest prior study's numbers.
- A limitation about the reference standard and about external validation.
- A statement of what the next step is (prospective trial, multicentre validation, monitoring).
- Consistency between the conclusion here, the abstract and the title.

## In a review

- Perspective: a challenges section where each challenge (validation, verification, bias, privacy, cost) is paired with a mitigation, then a conclusion of about 300 words that restates the promise in one short sentence, names the hurdles, and closes with a call to a named community.
- Guidance paper: summary of what was done with counts, the core recommendation, a rebuttal of a common belief with the reason, a numbered list of side topics, scope limitations only (what the paper did not cover and why), and a two sentence conclusion restating the criteria and the recommended set. A recommendation table is introduced here.
- Systematic review: principal finding with counts, strengths, comparison of findings by subgroup (model family), the field's barriers (journal policy, disclosure), a separate Limitations section (missed publications, reliance on self-reported metrics, the reviewers' own tooling), then a two paragraph conclusion hedged with "likely" and "appears" for forecasts.
