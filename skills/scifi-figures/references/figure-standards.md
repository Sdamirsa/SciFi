# Figure standards

How a SciFi figure is rendered: size, type, colour, layout, labels, libraries. What to draw and how to caption it is not here. That lives in the standards skill and is not repeated:

- which figures and panels, numbers on figures, supplement: `skills/scientific-writing/references/figures.md`
- which tables and their layout: `skills/scientific-writing/references/tables.md`
- caption structure, length, journal lead-ins: `skills/scientific-writing/references/captions.md`
- figure limits and formats per journal: `skills/scientific-writing/references/journal-profiles.md`

Absorbed from CrystaLit's vizmaker standards and adapted. Where CrystaLit's advice (written for literature-review corpus figures) differs from the clinical-journal advice, the table in section 9 says which wins in each mode.

## 1. Dimensions and output

| Property | Value | Notes |
|---|---|---|
| Single-column width | 8.5 to 9 cm | Most result panels |
| 1.5-column width | 11 to 12 cm | CrystaLit's "double column" range, used for wide corpus heat maps |
| Double-column width | 17 to 18 cm | Multi-panel main figures in a manuscript. Check the journal profile |
| Maximum height | 20 to 23 cm | Full page only, leave room for the caption |
| PNG | 300 dpi minimum, 600 for line art if the journal asks | |
| PDF | vector, fonts embedded as TrueType (`pdf.fonttype: 42`) so text stays editable | |
| Padding | `bbox_inches="tight"`, `pad_inches=0.02` in `savefig()` only, never in rcParams | |
| Files | every figure as `<name>.pdf` and `<name>.png` from one `save_fig()` | |
| Reproducibility | fixed seeds, no timestamps in metadata, running twice gives identical files | |

Set the figure size in centimetres at the final print width. Never scale a figure after rendering, since the font sizes below assume print size.

## 2. Typography

| Element | Size | Notes |
|---|---|---|
| Axis labels | 9 to 10 pt | with units in parentheses, "Accuracy (%)" |
| Tick labels | 8 to 9 pt | |
| Legend | 8 to 9 pt | match the ticks |
| Annotations, values on bars | 7 to 8 pt | 8 pt is the floor in corpus mode, 7 pt only inside bars in a manuscript when the journal allows |
| Panel letters | 10 to 12 pt bold | case per journal (section 6) |
| Title on the art | none in a manuscript | the caption title replaces it (section 9) |

Font family is sans-serif only: Arial, Helvetica, then DejaVu Sans as fallback. One font per paper.

## 3. Colour

**Arms and groups (manuscript mode).** One fixed colour per arm, model or group across every figure and table highlight in the paper. The proposed method takes one warm colour, the main comparator one cool colour, other baselines greys. Declare the map once as `ARM_COLOURS` at the top of `generate_figures.py` and never set a colour inline.

**Categorical, colour-vision safe (both modes).** Okabe-Ito:

```python
CATEGORICAL = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7",
               "#56B4E9", "#F0E442", "#000000"]
```

CrystaLit's original Material palette (`#2196F3, #FF9800, #4CAF50, #F44336, ...`) puts red next to green and is retired. Beyond eight categories, group the rest as "Other" or switch to small multiples.

**Sequential**: `viridis` or `cividis`. **Diverging** (correlations, signed deltas): `RdBu` or `coolwarm`, centred on zero with `TwoSlopeNorm`.

**Outcome states**: success, failure and not applicable keep the same three colours in every panel, and every error mark carries a symbol or bold as well as colour (figures.md section 4).

Check every figure in greyscale once. If two arms become indistinguishable, add hatching or markers.

## 4. Layout by chart type

**Bars.** Horizontal when labels are long (corpus concept frequencies), vertical for a few arms by a few groups. Sort descending unless the order is chronological or fixed by the paper's arm order. Axis from zero. Values on bars (section 5).

**Grouped bars.** Same arm order and colour in every group. Gap between groups wider than between bars.

**Heat maps.** Sequential map for counts, diverging for correlations. Always a labelled colour bar. Counts printed in cells when the matrix is at most about 12 by 12. Rows sorted, sort key stated in the caption. Prefer abbreviations to rotated labels, rotate 45 degrees only as a last resort.

**Forest plots.** Estimate as a square sized by weight or n, CI as a line, the null line (1 for ratios, 0 for differences) drawn, log scale for ratios, a text column with "estimate (95% CI)" and n.

**Kaplan-Meier.** Step curves, censor ticks, HR (95% CI) and p printed in the plot, number-at-risk table aligned under the x axis at the same tick positions, one row per arm in the arm colour.

**ROC and precision-recall.** Square axes, diagonal (ROC) or prevalence line (PR) as reference, AUC (95% CI) in the plot per curve.

**Calibration.** Grouped observed versus predicted points with CI, a smoother, the diagonal, a rug or histogram of predictions below.

**Network graphs (corpus).** Circular layout for dense networks, labels outside the circle, edge width for co-occurrence strength, related nodes grouped by angle.

**Treemaps (corpus).** Label only cells above 3% of the area. Theme cells use "Theme\nN subthemes\nM concepts". Text contrast checked against the fill.

**Radar charts (corpus only).** At most 8 to 10 axes, fill alpha 0.25, axis labels outside the rim, values printed. Not in a manuscript (section 9).

**Multi-panel figures.** Identical axis ranges, arm order and encoding across panels showing the same quantity. One shared legend. Panel order follows the text.

## 5. Numbers and uncertainty on the art (manuscript mode)

These implement figures.md section 5. Render, do not restate:

- **Values on bars.** Print the estimate on every bar of a headline comparison, with n/N for proportions from small samples. Inside the bar top in white when the bar is tall enough, above the error bar cap otherwise. Same decimals as the table.
- **CI error bars.** `yerr` as asymmetric `[estimate - lo, hi - estimate]`, never a symmetric SD posing as a CI. Caps 2 pt, line 0.8 pt, neutral dark grey. What the bar is (95% CI, bootstrap with N resamples, Wilson, exact binomial) is defined in the caption, never left as "±".
- **Number-at-risk tables.** Under every Kaplan-Meier panel, at the x tick positions, arm names in the arm colour.
- **Effect labels.** HR (95% CI) and p on KM panels, AUC (95% CI) on ROC panels, delta with p on incremental plots.
- **n per group** on the figure (axis tick "Centre A (n=600)") or in the caption.
- **p values** exact only for comparisons that survive the stated correction.

## 6. Panel letters

| Journal family | Letter on the art | Position |
|---|---|---|
| Nature, Nature Cancer, Nat Comms, npj | bold lower case a, b, c | top left, outside the axes |
| Lancet Digital Health, JAMIA | bold upper case A, B, C | top left |
| EHJ | bold upper case A to F | top left |

The case on the art, in the caption and in the text is the same (captions.md section 5). Set `PANEL_CASE` once at the top of the script from the journal in `STATE.json`.

## 7. Abbreviation map

Long names are mapped before rendering, then truncated at `MAXLEN` (default 20 to 22 characters) with an ellipsis as a fallback. Every abbreviation on the art is defined in the caption's abbreviation part, so the map doubles as the caption's glossary source.

```python
ABBREV_MAP = {
    # replace with the paper's or the corpus's terms
    "Large_Language_Model": "LLM",
    "Retrieval_Augmented_Generation": "RAG",
    "Left_Ventricular_Ejection_Fraction": "LVEF",
    "Dice_Similarity_Coefficient": "Dice",
    "Hausdorff_Distance": "HD",
}
```

In manuscript mode the map uses the abbreviations already defined in the manuscript, never new ones.

## 8. Anti-patterns

1. 3D charts. Never.
2. Pie and donut charts. Use a bar.
3. Dual y axes. Use side-by-side panels.
4. Default matplotlib style next to styled figures, including in the supplement.
5. Heavy gridlines. None, or alpha 0.15 on the value axis only.
6. Truncated value axes on bars.
7. Colour as the only carrier of meaning.
8. Rainbow or jet colour maps.
9. A legend that covers data.
10. Error bars without a definition.
11. "Left panel", "top right" instead of panel letters.
12. Text below 7 pt at print size.

## 9. Where CrystaLit and the clinical journals differ

| Rule | CrystaLit (corpus mode) | Clinical journals (manuscript mode) | Wins in manuscript mode |
|---|---|---|---|
| Legend placement | inside the axes, in the least busy quadrant, to keep size predictable | one shared legend above the panels or direct labels at line ends, never over data, identical across panels | clinical |
| Titles on the art | allowed at 10 to 11 pt | none, the caption title does the job | clinical |
| Width | 8 to 12 cm for everything | 8.5 to 9 cm single, 17 to 18 cm double | clinical |
| Palette | Material 10 colours | fixed arm colours plus Okabe-Ito | clinical (both modes) |
| Radar charts | one of the ten standard types | avoid unless every axis value is printed, prefer small multiples | clinical |
| Variations | 2 to 3 variations of every figure type | one design per display item, alternatives recorded in `figures.json` | clinical |
| Values on bars | "if space permits" | required on every headline comparison | clinical |
| Gridlines | none | none, or a faint value-axis grid if the journal style shows one | either |

In corpus mode CrystaLit's rules stand except the palette.

## 10. Libraries

```python
import matplotlib.pyplot as plt   # all figures
import numpy as np                # optional
import json                       # stdlib, labels and results
import yaml                       # PyYAML, ontology only, guard the import
import seaborn as sns             # optional, heat maps
import squarify                   # optional, treemaps
import networkx as nx             # optional, networks
import lifelines                  # optional, KM curves and at-risk tables
```

Install what a figure needs: `pip install matplotlib pyyaml` covers the template. Optional libraries are imported inside the function that needs them, so a missing one skips that figure with a message instead of failing the run. The runnable skeleton is `references/generate_figures_template.py`.
