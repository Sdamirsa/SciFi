# Paper
Mahmoudi E, et al. Privacy-preserving LLMs for echocardiography report analysis. JAMIA 2025;32:1120-1129; original research; source: medRxiv preprint full text (10.1101/2024.12.19.24319181v1), because PMC showed a reCAPTCHA, OUP is paywalled and Europe PMC was rate limited. Figure and table findings may differ from the typeset JAMIA version.

# Figures
**Main text: 4 figures. Supplementary: 6 (S2 to S7; no S1 is listed).**

| No. | Type | Panels | Role |
|---|---|---|---|
| 1 | Schematic of the prompt (base prompt in the centre, condition instructions without CoT on the left, with CoT on the right) | 3 columns, unlettered | Orientation: method illustration, cited in Methods |
| 2 | Labelled "schematic view of study workflow" but holds a sunburst plot (severity class distribution) and a radar plot (model accuracy across 9 categories) | 2, described as left and right | Data description plus a first look at the main result |
| 3 | Heat maps of predicted vs actual labels, 5 models x 4 regurgitant lesions | Multiple, unlettered | Main result (confusion structure) |
| 4 | Composite of processing time per report, accuracy and MSE, with vs without CoT, across 8 VHD categories, 4 prosthetic locations and "all diseases" | Multiple, not described individually | Main result plus efficiency trade-off |

- **Figure 1 is the prompt design**, not a study overview or cohort flow; the contribution is a prompting pipeline, so the prompt leads. The 200/1,000 dataset split appears only in prose.
- **Numbers on figures:** heat maps presumably carry counts per cell and Figure 4 carries values per bar, but captions do not say so, and no captions mention CIs, error bars or p values. The paper reports no CIs or p values anywhere.
- **Panel referencing:** no panel letters at all. The text cites whole figures ("Figure 3 and 4"); left and right appear only inside the Figure 2 caption. "Figure" is always spelled out.
- **Encoding:** the main contrast is with vs without CoT and model by model; colour legends are not explained in captions.
- **Supplementary figures** hold per-metric matrices (accuracy, sensitivity, specificity, NPV, PPV; S2 to S6) and stenotic lesion heat maps (S7) mirroring Figure 3: prevalent regurgitant lesions in the main text, rare stenotic ones in the supplement. None is cited in the main text.

# Tables
**Main text: 3 tables. Supplementary: S1, S2 titled, plus untitled image tables per model.**

| No. | Content | Position |
|---|---|---|
| 1 | Models (parameter size, context window, token limit) combined with study population characteristics | Cited in Methods (model selection) and again in Results (demographics) |
| 2 | Ambiguous report excerpts with each model's predicted labels in right-hand columns; wrong labels in red | Results, failure analysis |
| 3 | Same caption as Table 2, different abbreviation key; responses of each model to ambiguous reports | Results, cited as holding every model's response |

- **Table 1 convention is hybrid:** a model specification table merged with a baseline characteristics table. This is efficient for a methods comparison paper but mixes two kinds of row.
- **Tables 2 and 3 are qualitative example tables** (text excerpts as rows, models as columns, colour for errors). Using colour (red) as the only error marker is a print and accessibility risk.
- **Formatting seen in prose and supplement:** counts as n/N ("509/1000"), percentages with one decimal, MSE with two decimals, median (IQR) with a hyphenated range, mean plus or minus SD. Accuracy values sometimes appear without the % sign.
- **Supplementary S1** (prevalence) and **S2** (per-category accuracy) carry the quantitative detail; there is no main-text performance table.
- **Repetition:** Results restates all five models' means in one run of numbers, then MSE with "respectively", so displayed values are both pointed to and repeated in the prose.

# Captions
- **Structure:** two patterns. (a) A phrase ending in a colon, then the description (Figures 1, 2). (b) A single descriptive sentence (Figures 3, 4; Tables 2, 3). Table 1 is a bare label. No bold title sentence is visible in the preprint.
- **Length:** figures 15 to 53 words (typical about 30 to 35); tables 7 to 41 words. Table titles are either very short labels or long sentences with an abbreviation key.
- **Tone:** entirely descriptive; no caption states a finding.
- **Content:** Figure captions describe the layout (left/right, columns) and what is plotted; they do not define colour scales, cell values, n, or statistics. Table captions for Tables 2 and 3 define lesion abbreviations (AR, MR, PS or PR, TR) and the red error convention. Figure captions largely avoid abbreviations by spelling terms out ("mean squared error", "chain of thought").
- **Stand-alone:** partly. Figure 2 and Table 2 can be read alone; Figure 3 (15 words) cannot, since it names neither the colour scale nor the dataset.
- **Example titles:** "The prompt structure for prosthetic aortic valve classification"; "Heatmaps presenting five models' predicted labels versus actual labels"; "Proposed Language models and study population characteristics."

# Order and organisation
**Outline (approx. words, share of about 3,570 including abstract):**
- Abstract, structured Background/Methods/Results/Conclusions: 280 (8%)
- Introduction, 4 paragraphs, no subheads, ends with aim: 450 (13%)
- Methods: 670 (19%)
  - Data collection 190
  - Prompts structure 200 (Figure 1)
  - Model selection, and deployment 130 (Table 1)
  - Prompt optimization and model evaluation 150
- Results: 1,000 (28%)
  - Data characteristics 250 (Table 1, Figure 2, Supp Table 1)
  - Prompt Optimization 80 (Supp Table 2)
  - Evaluation 200 (Figures 3 and 4)
  - Unheaded continuation: failure types and ambiguous reports 250 (Figure 4, Tables 2, 3, Supp Section 2)
- Discussion, 9 paragraphs, no subheads: 900 (25%)
- Conclusion, 1 paragraph: 190 (5%)
- Data availability, 22 references; supplement in 3 sections (Methods: schema, full prompt, inference parameters; Results: per-model subsections; figures and tables).

**Methods before Results** (standard JAMIA IMRaD), so Results re-explains little, but it restates split sizes, the more-than-10-reports rule for metrics, and introduces the four error categories (an analytic scheme) inside Results.

**Results ordering:** data description, then prompt optimisation on the development set, then held-out evaluation with and without CoT, then error taxonomy, then ambiguous cases. This mirrors the pipeline (develop, test, inspect failures). Subsection headings are labels, not claims, and the most interesting qualitative material sits after the last heading with no heading of its own.

**Figure and table distribution:** one figure per Methods or Results subsection for the first three units, then the Evaluation subsection carries two figures and the unheaded tail carries two tables. Figure 4 serves two subsections.

**Discussion sequence:** (1) summary and headline performance without fine-tuning; (2) clinical uses (registries, severity tracking, alerts); (3) comparison with prior LLM and echo reporting studies; (4) why classification metrics beat generation metrics; (5) comparison with traditional NLP; (6) reasons for performance (pretraining, instruction tuning); (7) limitations: hallucination, model size; (8) mid-size model weakness on prosthetic valves; (9) CoT accuracy vs efficiency trade-off and low stenosis prevalence. Limitations are scattered across paragraphs 7 to 9 rather than in a labelled block.

**Supplement pointers:** about five, phrased generically ("provided in the supplementary material", "summarized in Supplementary Table 1", "described in the supplementary material Section 2"). Supplementary figures are never cited.

**Boxes:** none in the preprint (no key points, highlights or graphical abstract). JAMIA's typeset version may add a structured abstract only.

**Ease of reading:** the pipeline order and the prompt as Figure 1 help; the defects listed under Notable deviations hurt.

# Checklist candidates
- When the method is a prompt or pipeline, make Figure 1 an annotated schematic of that prompt or pipeline. [strong]
- Add a data flow figure or panel giving the development and evaluation split with n. [strong]
- Letter every panel (a, b, c) and cite panels in the text, never "left" or "right". [strong]
- Make every caption name what is plotted, the dataset and n, what colour encodes, and what cell or bar values mean. [strong]
- Check that every caption matches its figure type and the text claims that cite it (no "schematic" for data plots). [strong]
- Give every table its own caption; never duplicate captions, and check that counts in captions match the text. [strong]
- Cite every supplementary figure and table at least once in the main text, by number. [strong]
- Mark errors in example tables with a symbol or bold as well as colour. [strong]
- Report CIs (for example bootstrap) for headline metrics in tables or figures. [strong]
- Keep model specification and patient characteristics in separate tables, or label the two blocks clearly. [weak]
- Put the rare-class or secondary lesion analyses in the supplement, mirroring the main figure, and say so in the text. [weak]
- Give the error analysis its own Results heading and define its taxonomy in Methods. [weak]
- Use numbers from the same source across text, figures and supplement; cross-check before submission. [strong]
- Use descriptive figure captions of about 30 to 50 words, with abbreviations spelled out or defined. [weak]

# Notable deviations
- No study flow diagram, despite a development and evaluation split; Figure 1 is the prompt.
- No CIs or p values anywhere, unusual for a JAMIA model comparison.
- No main-text quantitative performance table; performance lives in Figure 4, the prose and the supplement.
- Consistency defects (duplicated table captions, six vs seven cases, mislabelled Figure 2, a Figure 4 citation that does not match its caption, a 99.0 vs 99.6 mismatch, uncited S2 to S7, missing S1). These may be fixed in the typeset version but show what copyediting must catch.
- Hybrid Table 1 combining model specifications with demographics.
