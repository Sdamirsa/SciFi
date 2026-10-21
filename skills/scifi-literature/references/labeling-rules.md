# Labelling rules (stage 3)

Read by the subagent that labels one paper. Labels are the data layer for corpus figures and
any count the paper reports about the literature. A wrong label propagates into figures and
text, and a missing label makes a paper's contribution invisible, so precision comes before
speed.

## Inputs and output

Inputs: `Literature/ontology.yaml` (status agreed), `Literature/notes/<key>.md`, and the full
text when the note is ambiguous. Output: `Literature/labels/<key>.json`, nothing else.

```json
{
  "paper_id": "smith2023deep",
  "title": "Full title of the paper",
  "ontology_version": 1,
  "T1_Theme_Name": {
    "T1-S1_Subtheme_Name": ["Concept_One", "Concept_Two"],
    "T1-S2_Another_Subtheme": ["Concept_Three"]
  },
  "T2_Another_Theme": {
    "T2-S1_Subtheme": []
  },
  "_comments": "Optional. Ambiguities and the conservative choice made."
}
```

`paper_id` is the citekey. Every theme and every subtheme in the ontology appears, even when
empty (`[]`), so the files aggregate without special cases. Concepts are copied exactly as
spelled in the ontology. A concept that is not in the ontology is never invented; propose it
in `_comments` and in the envelope's `result`.

## General principles

**Source sections.** Label from methods and results only. Introductions and discussions hold
claims about other work and speculation that must not be attributed to this paper. Exception:
the note's Gaps section may hold author-acknowledged limitations from the discussion. These
may inform labels of validation scope or study design, treated as self-reported, not
independently verified.

**Inclusion threshold.** Apply a concept if the paper uses, evaluates or directly contributes
to it in its methods or results. Do not label mentions, citations of others' work or future
work.

**Multi-label is expected.** Papers usually map to several concepts per subtheme.

**Granularity.** Label at the most specific concept. A paper using nnU-Net is labelled
`nnU-Net`, not only `Deep_Learning` or `3D_CNN`. The hierarchy is for organisation, not for
labelling.

**Absence versus not determinable.** `[]` means "this paper uses or contributes to no concept
in this subtheme". It does not mean "could not tell". For genuine ambiguity, check the full
text, then apply the most conservative label and explain in `_comments`.

## Domain rules

**Algorithms.** Label the index model (the main contribution) and every comparison model
evaluated. An unmodified architecture gets its specific name. A modified one ("attention U-Net
with squeeze-and-excitation blocks") gets both the base and the modification.

**Data.**
- Population size categories follow the thresholds the ontology defines (for example small
  under 200, medium 200 to 1000, large over 1000), counted as unique subjects across all
  splits.
- Multi-centre or single-centre follows the data used, not the authors' affiliations.
- Imaging modality is the one used in the study, not one mentioned as context.

**Evaluation.**
- Reference standard is what the paper actually compared against, not what could serve.
- Validation type. Internal is a held-out split from the same institution. External is data
  from an institution not seen in training. Cross-validation is its own category.

**Clinical application.** Label the demonstrated application, not the intended one. A paper
that proposes a clinical tool but validates only segmentation accuracy is labelled
segmentation. Put the intended application in `_comments`.

**Anatomy.** Label every structure the method explicitly segments, quantifies or analyses.

## Edge cases

**Foundation models.** Applied unmodified, label the model name. Fine-tuned, label the model
and the fine-tuning strategy.

**Reviews in the collection.** Label only the review's own methodological contribution (for
example a new taxonomy), not the papers it reviews.

**Multi-task papers.** Label every task that has methods and results. Not tasks mentioned only
as extensions.

## Procedure per paper

1. Open the note. Map the data extract to ontology concepts.
2. Cross-check with the note's theme summary.
3. For each theme and subtheme, decide which concepts apply.
4. Open the full text for anything uncertain.
5. Write the JSON with every subtheme present. Reload it with `python3 -c "import json,sys;
   json.load(open(sys.argv[1]))" <file>` to confirm it parses.

## Aggregation and quality checks (master)

Aggregate every `labels/<key>.json` into `labels/all_papers.json` (a JSON array of the paper
objects, in citekey order). Report:

- papers per concept, unused concepts, papers with unusually few labels
- **completeness**: every paper has at least one concept in every theme unless genuinely not
  applicable
- **distribution**: a concept on more than 80 percent of papers may be too broad, one on zero
  papers too narrow
- **consistency**: spot-check two or three pairs of similar papers for similar patterns

## When the ontology changes

If the ontology is updated after labelling has begun, the `changes` entry in `ontology.yaml`
names the concepts that changed and the papers to relabel. The master re-dispatches those
papers only, and each new label file carries the new `ontology_version`.
