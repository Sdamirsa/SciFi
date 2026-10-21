# The ontology (stage 2)

Master work. The ontology distils the notes into a shared vocabulary for labelling, corpus
figures and the paper's own framing of the field. It must capture every meaningful concept in
the corpus and still be clean enough that each concept earns its place.

## Structure

Four levels plus a cross-cutting list, in `Literature/ontology.yaml`:

```yaml
status: draft            # agreed after the human gate
version: 1               # bump on every change after agreement
built_from: 42           # number of notes read
themes:
  T1_Theme_Name:
    description: "What this theme covers"
    subthemes:
      T1-S1_Subtheme_Name:
        description: "What this subtheme covers"
        groups:
          Group_Name:
            description: "What this group covers"
            concepts:
              - Concept_One
              - Concept_Two

lateral_reasoning_pairs:
  - pair: ["Concept_A", "Concept_B"]
    rationale: "Why comparing these two concepts reveals something"
changes: []              # after agreement: {version, concept, change, papers_to_relabel}
```

| Level | Typical count | What it is |
|---|---|---|
| Themes | 5 to 8 | major dimensions of the research landscape |
| Subthemes | 3 to 6 per theme | distinct facets within a theme |
| Groups | 2 to 5 per subtheme | clusters of related concepts |
| Concepts | 3 to 15 per group | concrete items a labeller can answer yes or no for |
| Lateral reasoning pairs | 15 to 30 | cross-theme pairs whose juxtaposition yields an insight |

## Passes

**Pass 1, seed.** Read all notes' theme summaries (or a representative 15 to 20 notes in a
large corpus). Find the major dimensions of variation. Draft themes first, then expand down.
Question: if the field had to be explained to a newcomer in six categories, which six?

**Pass 2, populate.** Re-read every note and extract every concrete concept that appears in
two or more papers (or is important in one). Place each in a group, adding groups or
subthemes as needed. When a concept could live in two places, choose the most natural home
and note the tension as a candidate pair.

**Pass 3, refine.** Balance (no theme with three times the concepts of another unless the
literature skews that way), non-redundancy (merge synonyms), naming consistency, completeness
(is any paper under-represented?).

**Pass 4, lateral reasoning pairs.** Scan across themes for pairs whose comparison yields
insight: a method against a clinical concept, a data limitation against a model ambition, an
evaluation metric against a clinical outcome. Pairs that bear on a thread of the spine are
worth flagging to the human, since they may become a Discussion point.

## Naming

- `Title_Case_With_Underscores` for every concept.
- Abbreviation appended when the full name is long, `CT_Pulmonary_Angiography_CTPA`.
- Specific over general. `Dice_Similarity_Coefficient`, not `Overlap_Metric`.
  `Left_Ventricle`, not `Heart_Chamber`.
- Theme ids `T<n>_`, subtheme ids `T<n>-S<m>_`, stable once labelling starts.

## Quality tests

1. **Coverage.** Can every paper be labelled meaningfully with these concepts alone?
2. **Discrimination.** Do the concepts tell papers apart?
3. **Utility.** Would a figure built from these labels tell a story worth telling?
4. **Parsimony.** Can any concept be removed without losing labelling ability?

## Scale

For 30 to 60 papers in a well-defined subfield, expect 5 to 8 themes, 20 to 35 subthemes, 30
to 50 groups, 200 to 400 concepts and 15 to 30 pairs. Fewer than three themes or fewer than 50
concepts for 30 or more papers suggests under-extraction, so flag it and reread the notes. For
a research paper (not a review) a smaller ontology is normal, since it only needs to frame the
paper's threads.

## The gate

Present the YAML with the counts and a short narrative of what it says about the field. Ask
whether themes are well separated, concepts complete and the pairs worth comparing. The human
may edit the file directly. Set `status: agreed` only after the gate and log the decision.
After agreement, every change bumps `version` and adds a `changes` entry naming the papers to
relabel.
