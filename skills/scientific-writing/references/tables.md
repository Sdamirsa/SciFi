# Tables

Nine of the 14 papers had no main-text tables at all, including no baseline characteristics table. That is a Nature-portfolio and machine-learning habit; clinical reviewers at JAMIA, Lancet Digital Health and EHJ expect tables, and a paper with 11 models by three metrics written as prose lists is harder to review than the same data in one table. This file sets the clinical expectation.

## 1. Which tables to make

| Table | Content | Where cited | Needed when |
|---|---|---|---|
| Table 1, baseline characteristics | Rows: demographics, clinical variables, exposures or body composition measures. Columns: overall, then the stratification the paper reports differences on (by sex, by outcome, by development versus test set), then p. Continuous as median (IQR) or mean (SD), categorical as n (%). Tests named in Methods, not in the table | First Results paragraph | Any patient cohort. For benchmarks, a dataset summary table (datasets as rows; source, size, task format, domain as columns) plays this role |
| Model or system specification | Models as rows; parameter count, context window, version string, licence, hardware as columns | Methods | More than two models compared. Keep separate from Table 1; one corpus paper merged model specs with patient demographics |
| Primary results | Models or exposures as rows (grouped by setting if there are two conditions); metrics as grouped columns; an Average column where it is meaningful; cells as estimate (95% CI) | Primary Results subsection | Always, alongside the primary figure |
| Comparison of two methods per model | Each model as a block of sub-rows (method A, method B, difference) with the difference flagged for significance | Secondary Results | Paired comparison across many items |
| Delta table | Signed change between two conditions, sign convention in the footnote | Secondary Results | Two input conditions |
| Agreement or validation | Raters as rows, agreement categories as columns, average row | Human evaluation | Any rater study |
| Error taxonomy with examples | Failure type, count, one example per type (text excerpt as a row, model outputs as columns, errors marked with a symbol and colour) | Error analysis | Any model that produces free text |
| Search string | The full Boolean string in one cell | Methods or supplement | Systematic reviews (this is their Table 1) |
| Taxonomy or framework | Domains or classes as rows, target question and focus as columns | Framework section | Guidance and perspective papers (their Table 1) |
| Assessment matrix | Items as rows grouped by domain, criteria as columns, symbols (++, +, minus) or Yes/No, a verdict column; the tally matches the abstract | Body of a guidance paper | Reviews that score items against criteria |
| Recommendation summary | Item, categorical verdict (Recommended, Inadvisable, two hedged grades), one-line reason, abbreviation footnote as glossary | Discussion | Guidance papers |
| Evaluation rubric | Item, question, scale, options, who rated | Methods or extended data | Rater studies |

Supplement takes: extended HR tables (an extended twin of the main effect table, named in the text), subgroup tables, per-category metrics, hyperparameters, feature definitions, full extraction tables, per-patient results.

## 2. Layout rules

- Rows are the things compared (models, exposures, subgroups); columns are the quantities (metrics, outcomes). Readers scan down a column to compare.
- Group columns under spanning headers per task or dataset.
- Keep model or group order identical across all tables and figures and in the prose.
- Units in column headers in parentheses or brackets ("Accuracy (%)", "Time per report (s)"), never repeated in every cell.
- Consistent decimals within a column: one for percentages, two for AUROC and similar, three for p (or "<0.001"). Tables may carry one more decimal than the prose, but the prose value must round from the table value.
- Cells for an effect: "2.39 (1.92 to 2.96)"; p in its own column. State "95% CI" once in the column header.
- Mean ± SD only with the dispersion named in a footnote; prefer "mean (SD)".
- Reference category stated in the title or footnote for any table of ratios.
- No empty cells without a footnote; use "NA" or a dash defined in the footnote.
- Bold for the best value per column and underline for second best, with both explained in the footnote and the scope of the comparison stated ("within each user setting"). Italics for worst is unusual; avoid.
- Colour as the only marker of an error or a category fails in print; add a symbol.
- Check that every estimate lies inside its own CI and that no interval is reversed (both errors passed review in the corpus).

## 3. Titles and footnotes

- Title: one descriptive noun phrase, 5 to 14 words, no claim, no verb ("Baseline characteristics stratified by sex", "Model performance across tasks and evaluation methods"). Methodological notes ("lower values serve as the reference") go in the footnote, not the title.
- Footnotes carry: abbreviation key (every abbreviation used in the table, alphabetised), formatting conventions (bold, underline, asterisk), statistical notes (test, correction, what follows ±), exclusions, data source. Never reuse one letter for two meanings in the key.
- Every table has its own unique title; duplicated captions across two tables survived review in one corpus paper.

## 4. Prose and tables

- The text points to the table and restates only the headline values and the exceptions. It does not walk through every cell.
- The text never names a column or statistic absent from the table (a P-value column that is in fact an asterisk, a mean when the figure shows medians).
- Numbers in text, table, figure and abstract come from one source file and agree to the stated precision.

## 5. In a review

- Table 1 is the search string (systematic review) or the taxonomy (guidance, perspective).
- A citation summary table that groups references by codes with no counts summarises nothing; add count columns or replace it with a grid figure.
- The assessment matrix and the recommendation table carry the main contribution of a guidance paper; their tallies must match the abstract and the Discussion.
