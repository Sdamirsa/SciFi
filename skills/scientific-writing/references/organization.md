# Organisation of a manuscript

How the 14 source papers order their content, what share each section takes, and how display items are distributed. Use this file for a Plan task, for a whole-manuscript Draft, and whenever a Review finds a structural problem (a Results section that is half Methods, limitations scattered across ten paragraphs, a Figure 1 that is cited after Figure 4).

## 1. Section order by journal family

| Family | Order | Where ethics sits | Where the design recap sits |
|---|---|---|---|
| Balanced default, JAMIA, Lancet Digital Health, EHJ | Abstract, Introduction, Methods, Results, Discussion, (Conclusion), back matter | First Methods subsection | Not needed; Methods precedes Results |
| Nature, Nature Cancer, Nature Communications, npj Digital Medicine | Abstract, unheaded Introduction, Results, Discussion, Methods, back matter | First Methods subsection ("Ethics" or "Compliance statement") | Last Introduction paragraph names data, design, raters and outcome; each Results subsection opens with one or two sentences restating the condition, metric or n it reports |

When Methods comes last, three things prevent the Results from turning into a Methods section (a failure seen in two npj papers): (1) the contributions paragraph at the end of the Introduction names every dataset, model and evaluation; (2) each Results subsection gets a one to two sentence setup, no more; (3) anything longer than that moves to Methods with a pointer.

## 2. Word budgets

Approximate shares of the main text (excluding abstract, captions and references) that the corpus converges on, with the user's preference for concision applied.

| Section | Original research, Methods first | Original research, Methods last | Review or perspective |
|---|---|---|---|
| Introduction | 10 to 15% (300 to 550 words, 4 to 6 paragraphs) | 10 to 13% | 15% including aims and roadmap |
| Methods | 30 to 35% | 25 to 40% (engineering detail inflates it; push prompts and hyperparameters to the supplement) | A short scope and search paragraph, or a dedicated case-study section |
| Results | 20 to 30% | 30 to 45% | Body sections 50 to 65% |
| Discussion | 20 to 30% (including one limitations paragraph of 150 to 250 words and a conclusion of 60 to 120 words) | 20 to 25% | 10 to 15% plus a 200 to 300 word conclusion |

Typical totals: 3,000 to 4,500 words for JAMIA, Lancet Digital Health and EHJ original research; 4,000 to 7,500 for Nature-portfolio with Methods; 4,500 to 8,000 for a review. The two shortest papers in the corpus (about 2,500 and 3,000 words) were a Lancet prognostic study and a JAMIA model comparison; neither felt thin because tables and figures carried the detail.

## 3. The spine of an original research paper

Each item below is a "move". A move is one or two paragraphs. Section files give the moves in detail; this is the map.

1. Title: what was done, to what, with what design.
2. Abstract: background, gap, aim, design with n, headline numbers with uncertainty, conclusion at design strength.
3. Introduction: field, clinical problem with numbers, prior work and its limit, gap in one sentence, aim with design in one sentence. No results preview unless the journal profile asks for one.
4. Methods: design and ethics, population and data, intervention or model, reference standard, outcomes and metrics, statistics, reporting guideline, role of funder (Lancet).
5. Results: cohort or data description with flow figure and Table 1, primary analysis, secondary analyses, subgroups or robustness, human or clinician evaluation, error analysis.
6. Discussion: principal findings in one paragraph, comparison with prior work, mechanism, implications, limitations paragraph, conclusion.
7. Back matter in journal order.

Mirror principle: Methods subsections and Results subsections share the same sequence and, where possible, the same headings. A reader who finds "Subgroup analyses" in Methods expects "Subgroup analyses" in Results.

## 4. The spine of a review or perspective

Reviews in the corpus (two narrative perspectives, one guidance review, one systematic review) share a structure that has nothing to do with IMRaD.

1. Summary or abstract: context, what is proposed or asked, how the paper proceeds, implication.
2. Introduction: define the central concept, state the gap, state the aims as a numbered list, give a one-paragraph roadmap of the sections.
3. Framework before evidence: define the taxonomy, the criteria or the organising list first (Table 1 or Figure 1 is this framework). Every later section is scored against it.
4. Body: parallel sections, each with the same internal template. The three templates seen: (a) scenario, how it works, "a solution needs to", prior evidence; (b) definition, interpretation, critique against the criteria, worked value, verdict; (c) one subsection per item of the organising list, alternating the two classes being compared.
5. Challenges and opportunities, each challenge paired with a mitigation. This section doubles as the limitations.
6. Discussion: what was done with counts, the core recommendation, a rebuttal of a common belief, scope limitations, conclusion. A recommendation table is introduced here.
7. Systematic reviews: PRISMA 2020, registration, eligibility with a bulleted exclusion list, Table 1 as the search string, PRISMA flow diagram as the first Results figure, one paragraph per figure in Results, a separate Limitations section, a two-paragraph conclusion.

The device that made the strongest reviews coherent was one organising list (six benefits, five domains, three capabilities) repeated as the structure of the framework, the evidence, the figures and the recommendations.

## 5. What goes in the supplement

Main text keeps: the design overview figure, the flow diagram, Table 1, the primary result figure and table, one worked example, the error analysis table.

Supplement takes: full prompts and hyperparameters, per-dataset or per-model curves when one representative panel is in the main text, rater instruments and interfaces, extended HR tables, subgroup tables, stability and ablation plots, full search strings when Table 1 is used for something else, raw outputs and case texts, formulas.

Pointer phrasing: parenthetical and specific, at the end of the sentence the item supports, "(Supplementary Table 6)" or "(Supplementary Figures 3 to 5)". Never "see supplementary material" without a number. Cite every supplementary item at least once in the main text; the corpus has papers with six uncited supplementary figures.

## 6. Display item distribution

- One figure or table per Results subsection is the ideal; two subsections sharing one six-panel figure is acceptable when the panels are parallel.
- Figures are numbered in order of first citation. If the first figure cited is the dataset description, that is Figure 1, unless the design overview is cited from the Introduction or Methods, in which case the overview is Figure 1. Three corpus papers broke this rule and their readers meet Figure 3 or Figure 4 before Figure 1.
- Headline result: in a figure with values printed on it, and in a table with CIs. Not only in prose lists (one paper reports 11 models by several metrics entirely in sentences), and not only in a table (one paper has no figure of its main result).
- Methods-only figures (preprocessing flow, prompt anatomy, RAG pipeline) go to the supplement unless the pipeline is the contribution.
- Total display items in the main text: 4 to 7 for a 3,500 word paper. One corpus paper has 14, which is too many for npj.

## 7. Structural failure modes seen in the corpus, in order of frequency

1. Limitations scattered across many Discussion paragraphs with no heading or opening sentence (five papers).
2. Results subsections that describe the method, dataset construction or metric definitions at length (three papers with Methods last).
3. Figures cited out of numerical order (three papers).
4. No cohort or dataset characteristics table (nine papers; acceptable for benchmarks, not for patient cohorts).
5. Captions that do not stand alone: no n, no test, no abbreviations (nine papers).
6. The same number given differently in abstract, Results and Discussion (three papers).
7. Introduction longer than Results (one systematic review).
8. A Discussion that opens with field context instead of the principal finding (one paper).
