# The note template (stage 1)

Read by the subagent that writes one note. The reader of the note is a later agent or the
human who has not opened the PDF, so accuracy and grounding matter more than coverage.

## The cardinal rule

Extract only what is grounded in the paper's **methods and results**. Introductions and
discussions hold claims about other work, speculation and framing that may not reflect what
the paper did. A finding in the note must come from what the authors did and measured, not
from what they said others did or what they hope their work implies.

One exception. The Gaps section may include limitations the authors acknowledge in their
discussion, marked `(author-acknowledged)` so they are not mistaken for evidence-based gaps.

## File

`Literature/notes/<citekey>.md`, the key exactly as in `Literature/library.json` (or as the
Zotero MCP returns it). One paper per file. Write nothing else.

## Template

```markdown
# <First author> <Year>, <Short title> [@<citekey>]

## Relevance to the central claim

<2 to 3 sentences. How this paper bears on the central claim in
Thinking-space/spine.json: which thread (T1..) or result (R1..) it supports, contrasts with,
or sets up, and whether it belongs where the thread opens (Introduction) or closes
(Discussion). If spine.json does not exist yet, write "Spine not agreed" and one sentence on
the paper's relation to the human's stated topic. The master refreshes this banner once the
spine and the ontology are agreed.>

## 1 Data extract

* **Aim of study:** "<quoted or closely paraphrased from the paper>"

* **Task approach:** <setting; input data type; what the method or model does; what it
  outputs. Be specific about the pipeline: preprocessing, model, postprocessing, output.>

* **Dataset size:** <number of centres; devices or scanners; total subjects with
  demographics; train, validation and test split if reported; notable inclusion and
  exclusion criteria>

* **Models:** <index model(s) with version or architecture; comparison models; key
  hyperparameters if reported>

* **Evaluation and gold standard:** <metrics with values and intervals; reference standard;
  statistical methods; inter- or intra-observer variability if reported>

* **Preprocessing steps:** <all preprocessing, such as resampling, windowing, cropping,
  augmentation, normalisation, gating, reconstruction parameters>

* **Postprocessing and XAI steps:** <postprocessing such as CRF, shape regularisation,
  connected components; explainability such as saliency maps, attention, SHAP>

## 2 Gaps

<Bullets, one sentence each. Methodological gaps (what they should have done and did not),
validation gaps (what evidence is missing), applicability gaps (what limits real-world use).
Mark discussion-sourced items "(author-acknowledged)".>

## 3 Interesting application and usable rationale

<2 to 4 paragraphs, each with a bold title. Reusable ideas such as an evaluation framework,
a data strategy, a workflow insight or a transferable method, and why each matters beyond
this paper.>

---

## Theme summary for the ontology

<Structured summary by anticipated theme: model types, data characteristics, evaluation
approaches, applications, anatomical or domain targets, notable methodological choices.
Stage 2 reads this section first.>
```

The data extract fields above suit imaging and clinical AI papers. For another field, the
master adapts the field names in the brief at the stage 1 checkpoint (for example design,
population, intervention, comparator, outcomes for a trial) and keeps the four sections.

## Procedure

1. Read the full paper, not just the abstract. The methods hold the real information.
2. Fill the data extract field by field. If something is not reported, write "Not reported".
3. Gaps: what would a rigorous reviewer want that is missing?
4. Interesting application: what idea here could be reused elsewhere?
5. Theme summary: scan the data extract and map it to broad categories.
6. Check the note against the template. Every section present, no section empty.

## Quality standards

- **Specific over vague.** "Random-forest classifier with 200 trees, trained on 5,000 labelled
  records", not "a machine learning model trained on the dataset".
- **Numbers.** Sample sizes, metric values, confidence intervals and p values when reported,
  copied exactly.
- **The paper's own terms** for models, metrics and methods.
- **Flag uncertainty.** If something is ambiguous, say so in the note rather than choosing.
- **Self-contained.** Someone who reads only the note knows what the paper did, found, missed
  and offers.

## When to stop

A PDF that is unreadable (scanned without OCR, corrupt, password protected) or a paper that is
not original research (a review, an editorial) is reported in the envelope, not silently
skipped. Unreadable: `status: blocked`, `NEED: readable full text of @key`. A review: write
the note with the data extract fields marked "Not applicable (review)" and the review's own
contribution (its taxonomy, its search) under section 3, and say so in `result`.
