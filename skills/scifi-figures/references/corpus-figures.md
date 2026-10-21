# Corpus figures (corpus mode)

Figures and a dashboard from a labelled literature corpus, the CrystaLit library adapted to the SciFi workspace. Rendering rules are in `figure-standards.md` (corpus mode column of section 9). Use this for a review, a scoping review, or the related-work figure of an original paper.

## 1. Inputs

| File | Content |
|---|---|
| `Literature/labels/all_papers.json` | list of papers, each `{"paper_id", "title", "<Theme>": {"<Subtheme>": [concepts]}, "_comments": [...]}`. An object keyed by paper id is also accepted |
| `Literature/ontology.yaml` | `themes > subthemes > groups > concepts`, each level with a `description` |
| `Literature/library.json` | Better CSL JSON, for years and venues when the labels lack them; join on `paper_id` = citekey |

Both label files are read only (protocol section 1). If either is missing, stop and say which. The labelling pipeline that produces them is not part of SciFi (CrystaLit, archived, does it).

Outputs go to `Thinking-space/figures/corpus/`: `generate_figures.py`, `<name>.pdf` and `<name>.png` per figure, `dashboard/index.html`. Corpus figures that enter the manuscript get an entry in `figures.json` like any other item (role `taxonomy` or `evidence-map`).

Before writing code, compute and show the human: papers, themes, subthemes, concepts, concepts used by no paper, concepts used by over 80% of papers, papers with fewer than one concept per theme. These flag ontology problems that no figure can fix.

## 2. The figure library

Ten types. In corpus mode make each type that fits the data, one design each, with a variation only when the human asks (section 9 of figure-standards.md).

| # | Type | Shows | Data | Notes |
|---|---|---|---|---|
| 1 | Horizontal bar | concept frequency within one subtheme | counts per concept | sorted descending, values on bars, zero bars for unused ontology concepts |
| 2 | Stacked bar | composition by period or study type | concept by year bin | at most 8 stack colours, "Other" for the rest |
| 3 | Heat map | concept co-occurrence | concept by concept counts | sequential map, counts in cells up to 12 by 12, sorted by frequency |
| 4 | Treemap | theme, subtheme, concept hierarchy | ontology plus counts | `squarify`, labels only above 3% area |
| 5 | Network | co-occurrence network | edges above a stated threshold | `networkx`, circular layout, edge width for strength |
| 6 | Timeline or scatter | year against method or modality | year from labels or library.json | jitter stated in caption |
| 7 | Radar | profile of a few papers or groups | normalised counts per subtheme | at most 8 axes, values printed, not for a manuscript main figure |
| 8 | Grouped bar | concept frequency compared across themes or periods | counts per group | same order and colours across groups |
| 9 | Bubble | three variables (e.g. year, n, modality) | per paper | size legend with real values |
| 10 | Sankey or alluvial | flow between categories (task to metric to validation design) | paired label counts | `plotly` export to static PDF, or a hand-drawn flow in matplotlib |

For an evidence map in a review, the grid figure in `skills/scientific-writing/references/figures.md` (section 2, inventory row) is usually the main figure. Build it as type 3 with papers as columns, concepts as rows, a symbol per cell and a count column.

## 3. generate_figures.py structure

Start from `references/generate_figures_template.py`, copied to `Thinking-space/figures/corpus/generate_figures.py`. Keep this shape:

1. **Docstring** with usage, inputs, outputs, exit codes.
2. **Constants** at the top: `DPI`, widths in cm, font sizes, `CATEGORICAL`, `ABBREV_MAP` (built from the ontology's concept names), `MAXLEN`, thresholds (co-occurrence minimum, treemap label area).
3. **Loaders**: `load_labels()`, `load_ontology_concepts()`, and counting helpers (`concept_counts()`, a co-occurrence counter). The YAML import is guarded, so a missing PyYAML skips ontology-dependent figures with a message.
4. **One function per figure**, named `fig_<type>_<subject>()`, taking the data and the output folder, returning the saved paths or `None` with a printed reason when the data cannot support it.
5. **`save_fig(fig, name, out)`** saving PDF and PNG with fixed metadata.
6. **`main()`** that runs every figure function, prints progress, and exits non-zero if nothing was written.

Run it, and record the command and the output folder in `log/decisions.jsonl`.

## 4. The dashboard

`Thinking-space/figures/corpus/dashboard/index.html`, one self-contained file:

- Data embedded as a JSON block in the page (no server, no fetch).
- One charting library from a CDN at a pinned version (Chart.js or Plotly.js).
- Filters for theme, subtheme and paper. A paper table with title, year, citekey and its concepts, searchable.
- The same colours and abbreviations as the static figures.
- Opens offline from disk. It is a browsing aid for the authors and is not a manuscript display item.

## 5. QA pass

After every run, view each PNG at print size (open it at 100% on the target width) and check:

| Check | Fix |
|---|---|
| Truncated or overlapping labels | extend `ABBREV_MAP`, lower `MAXLEN`, switch to horizontal bars |
| Text under 8 pt at print size | enlarge the figure height, not the fonts beyond the scale |
| Empty or near-empty figure | drop it, or merge with a neighbour, and say so |
| Legend over data | move it (figure-standards.md section 9) |
| Colours not in the palette, or the same concept in two colours | use the constants |
| Counts that disagree with the summary from section 1 | fix the counting, never the figure by hand |
| Greyscale unreadable | add hatching or markers |

Regenerate until every figure passes. Report the list with pass or the fix made, and show all figures to the human at the HITL checkpoint before any enters `figures.json`.
