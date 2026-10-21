# Brainstorming display items (manuscript mode)

Read by `figure-brainstormer` (candidates) and by the master (choice). The figure and table types themselves are defined in `skills/scientific-writing/references/figures.md` (sections 1 and 2) and `tables.md` (section 1). This file is the procedure that applies them to one paper.

## 1. Inputs

- `Thinking-space/spine.json`: the results R1..Rn with numbers, their `display` hints, the threads.
- `Thinking-space/skeleton.json`: the Results units r01.. and the result ids each carries, the Methods units they mirror, the journal.
- The journal profile entry (figure limit, panel letter case, whether Table 1 is expected).
- `Manuscript/figures/` listing, if any: which data exist, so a design that needs absent data is flagged as a NEED, never assumed.

## 2. Per Results unit, the candidates

For each Results unit, write two or three candidates. Each candidate states:

| Field | Content |
|---|---|
| kind and type | figure, table or supplementary, and the type from figures.md section 2 |
| panels | letter, what it shows, n |
| numbers printed | the exact values that go on the art (from the spine, never new ones) |
| encoding | arm colours, reference lines, sort order |
| proves | the one sentence the item lets a reader verify without the text |
| reviewer expects | what a clinical reviewer looks for here and whether this design gives it |
| journal fit | whether the journal family uses this form (section 4) |
| cost | data needed, whether it exists, main-text slot it uses |

Then choose with three questions, in this order:

1. **What does each design prove?** Prefer the design whose "proves" sentence is the unit's takeaway. A design that proves something else belongs to another unit or the supplement.
2. **What does a reviewer expect?** A discrimination claim without a ROC with CI, a survival claim without number at risk, a comparison of many models by many metrics without a table, all draw a request. Meet the expectation first, then improve on it.
3. **What does the journal family prefer?** Use section 4. When the choice is still open, take the design with fewer panels.

Record the losers in `alternatives_considered` on the chosen item, one line each with why.

## 3. Designs by kind of result

| Result shape | Candidate A | Candidate B | Candidate C |
|---|---|---|---|
| One metric, two to four arms | grouped bar with values, n/N and 95% CI | table, estimate (95% CI) | dot plot with CI (many groups) |
| Many models by many metrics | table with spanning headers, best in bold | heat map of metrics with values in cells | small multiples, one bar panel per metric |
| Per-class or per-severity performance | confusion matrix with counts | per-class bar with CI | table of sensitivity and PPV per class |
| Subgroups or sites | forest plot with the overall diamond | grouped bar per site | table in the supplement |
| Discrimination | ROC with AUC (95% CI) | PR curve when the outcome is rare | both as two panels |
| Agreement with a reference | Bland-Altman | scatter with identity line and r | table of kappa per rater pair |
| Errors | error taxonomy table with one example per type | annotated example figure | stacked bar of error types per arm |
| Efficiency | bar of time or cost per report with CI | table | text only if one number |

## 4. Journal family preferences

| Family | Leans towards | Watch |
|---|---|---|
| Nature-portfolio, npj | multi-panel figures, overview with a result teaser, extended data | tables still expected for many-by-many comparisons, lower-case letters |
| Lancet Digital Health | Table 1, primary results table, flow diagram, fewer main figures | upper-case letters in parentheses, every abbreviation redefined |
| JAMIA | tables for model comparisons, error taxonomy, rubric tables | figures count against a limit, check the profile |
| EHJ | central illustration, structured multi-panel figures with tests per panel | bold A to F, alphabetised abbreviation list |

## 5. The fixed set for a clinical-AI paper

Every clinical-AI original research paper is checked for these, and the brainstormer names the skeleton unit that cites each (figures.md section 1, tables.md section 1):

1. Figure 1 overview (pipeline or study design), cited from the end of the Introduction or the first Methods unit per journal.
2. Flow diagram with n at every step, cited from the first Results sentence.
3. Table 1, baseline characteristics or the dataset summary, cited from the first Results unit.
4. Primary result figure with values and CIs on the art, plus the primary results table when more than two arms or metrics.
5. Error analysis (confusion matrix or error taxonomy table).
6. Model or system specification table when more than two models are compared.

A missing member is either justified in `rejected` (for example no patient cohort, so Table 1 is the dataset summary) or added.

## 6. What goes to the supplement

- Per-site, per-class or per-subgroup repeats when one representative panel is in the main text.
- Prompts, preprocessing flows, hyperparameters, annotation guides, rater interfaces.
- Sensitivity and stability analyses that do not change the claim.
- Full extraction or per-patient tables.
- Anything over the journal's main display limit, lowest-priority first (worked example, then secondary robustness).

Each supplementary item is still cited by number from a named skeleton unit.

## 7. Rejected by default

Dual axes, pie charts, radar charts without printed values, colour-only error marks, a figure that duplicates a table, a figure whose "proves" sentence no unit needs (an orphan display). Each rejection goes in `rejected` with a one-line reason.

## 8. Worked example (invented study)

All numbers below are invented for illustration. Study: an open-weight LLM extracts aortic, mitral and tricuspid valve disease severity (none, mild, moderate, severe) from 1,200 transthoracic echocardiography reports, 600 at Centre A and 600 at Centre B, against a cardiologist reference, compared with a rule-based system. Journal: npj Digital Medicine.

Spine results (invented):
- R1 report-level accuracy (all three valves graded correctly) 96.3% (95% CI 95.1 to 97.2) for the LLM versus 88.7% (86.8 to 90.4) for the rule-based system.
- R2 accuracy by centre, LLM 96.8% (A) and 95.8% (B), rule-based 89.5% and 87.8%.
- R3 most LLM errors are moderate versus severe confusions in reports with mixed grading language.
- R4 median processing time 2.1 s per report on one GPU.

Unit r02 carries R1 and R2. Candidates:

| | A, grouped bar | B, table | C, forest plot |
|---|---|---|---|
| type | grouped bar, two arms by two centres plus pooled | table, arms as rows, centres and pooled as columns, estimate (95% CI) | difference in accuracy LLM minus rule-based, per centre and pooled |
| panels | a, accuracy per centre and pooled with n/N | none | a, difference with 95% CI, null line at 0 |
| numbers printed | 96.8, 95.8, 96.3 and 89.5, 87.8, 88.7 with n/N | same, plus sensitivity per severity | +7.3, +8.0, +7.6 points |
| proves | the LLM is higher at both centres | exact values for meta-analysis | the gap is consistent across centres |
| reviewer expects | values and CI on bars, definition of CI | a table for exact numbers | the paired test named |
| journal fit | npj favours a figure for the headline | supplement in npj | fits as panel b |

Choice: A as Figure 3a with C as Figure 3b (the takeaway is "higher at both centres, by a similar margin"), B to Supplementary Table 2. `alternatives_considered` on F3 records B and a single pooled bar.

Unit r03 carries R3: confusion matrix per valve (Figure 4, counts in cells, rows sorted by reference severity) against an error taxonomy table with one example per type (Table 3). Chosen both, since the matrix shows where and the table shows why. Unit r04: one number, stays in text, no display item (recorded in `rejected`).

Fixed set: Figure 1 pipeline (report, prompt, structured output, severity grade) cited from i05. Figure 2 flow diagram (reports screened, excluded with reasons, 600 per centre). Table 1 dataset summary per centre (reports, patients, valves graded, severity distribution). Table 2 system specification (model, version, parameters, licence, hardware, rule-based version).

The resulting `figures.json` entry for the primary figure:

```json
{
  "id": "F3", "kind": "figure", "role": "primary", "type": "grouped bar and forest",
  "shows": "Accuracy of the LLM and the rule-based system per centre and pooled, and their difference",
  "results": ["R1", "R2"],
  "panels": [
    {"letter": "a", "shows": "Accuracy per centre and pooled, values and n/N on bars", "n": "600 + 600 reports", "stat": "95% CI, Wilson"},
    {"letter": "b", "shows": "Difference LLM minus rule-based per centre and pooled", "n": "600 + 600 reports", "stat": "95% CI, paired bootstrap 2,000 resamples"}
  ],
  "cited_from": "r02",
  "data_source": "Manuscript/figures/accuracy_by_centre.json",
  "encoding": "LLM vermilion, rule-based blue, null line at 0 in b",
  "numbers_on_figure": "96.8, 95.8, 96.3 and 89.5, 87.8, 88.7 (%), n/N per bar",
  "caption": "c03",
  "alternatives_considered": ["Table of accuracy per centre (moved to Supplementary Table 2)", "Single pooled bar (hides the centre consistency)"],
  "status": "chosen"
}
```
