# Paper
Singhal K et al. Large language models encode clinical knowledge. Nature 2023;620:172-180; Article (original research); source: Europe PMC full-text XML and NCBI BioC XML for main text and figure captions (PMC page gave a reCAPTCHA, nature.com failed), arXiv preprint 2212.13138 to infer Extended Data table layouts.

# Figures
- **Main text: 6 figures. Extended Data: 2 figures** (ED Fig. 1, overview of instruction prompt tuning for Med-PaLM, cited in Methods; ED Fig. 2, MMLU clinical topic results, cited in Results). No supplementary figures were seen; Supplementary Information holds sections and tables instead.
- **Fig. 1, overview of contributions.** An unlettered schematic summarising the whole paper: the MultiMedQA benchmark, PaLM and Flan-PaLM evaluated on it, the headline accuracy gain, and Med-PaLM compared with clinicians. Its job is orientation plus headline result. It sits in Main and is cited once there, whole. Figure 1 works like a graphical abstract, not a methods pipeline.
- **Fig. 2, comparison with prior state of the art.** Single-panel bar chart, Flan-PaLM 540B against the best earlier model on MedQA, MedMCQA and PubMedQA. Accuracy values are printed above each bar. Main result for the automated benchmarks.
- **Fig. 3, selective prediction.** Single panel, accuracy against deferral fraction (a curve, inferred). Secondary or exploratory result.
- **Fig. 4, clinician evaluation.** Six panels (a to f), one per rating axis: consensus, incorrect content, omitted content, extent of harm, likelihood of harm, bias. Three answer sources compared: Flan-PaLM, Med-PaLM, clinicians. Main human evaluation result; one figure feeds five Results subsections.
- **Fig. 5, comprehension, recall and reasoning.** Two panels (a, correct; b, incorrect evidence of each capability). Secondary human evaluation.
- **Fig. 6, lay user assessment.** Two panels (a, addresses intent; b, helpfulness). Secondary human evaluation.
- **Encoding.** The same three-source comparison (base model, tuned model, human expert) repeats across Figs. 4 to 6. No caption states colours; the in-image legend carries them.
- **Numbers on figures.** Only Fig. 2 puts values on bars. Figs. 4 to 6 show 95% bootstrap intervals; exact percentages appear in the prose.
- **Panel citation.** Captions use lower-case bold letters (a, b). The text cites only whole figures ("Fig. 4", "Figs. 4 to 6" style ranges), never "Fig. 4b", even when a subsection discusses one panel.
- **Pushed out of the main text.** MMLU breakdown, prompt tuning schematic, ablation tables and qualitative examples go to Extended Data; scaling, CoT and self-consistency numbers to Supplementary Information.

# Tables
- **No main-text tables.** All tabular content is Extended Data (8 tables) or Supplementary tables. There is no baseline characteristics Table 1, because there are no participants; the benchmark summary (ED Table 1) fills that descriptive role.
- **Extended Data tables (layouts inferred from the preprint):** ED Table 1, dataset summary (datasets as rows; format, size dev/test, domain as columns). ED Tables 2 and 3, rater instrument (numbered axis rows with the exact question asked). ED Table 4, MedQA leaderboard (models as rows with parameter count and "(ours)"; accuracy in percent, one decimal). ED Table 5, instruction tuning (datasets as rows with shot count in the label, model by size as columns). ED Tables 6 to 8, qualitative question and answer examples, one column per answer source.
- **Cell conventions.** Percent accuracy with one decimal, no intervals in benchmark tables, no p values anywhere. Citation numbers sit inside row labels for prior models. Bold for best values could not be confirmed.
- **Prose and tables.** Headline benchmark numbers (67.6%, 57.6%, 79.0%) are repeated in the text; ablation tables are pointed to with only the key delta repeated. Qualitative example tables are only pointed to.

# Captions
- **Structure.** Bold title sentence ending with a full stop, then a running paragraph. Panel letters appear inline within that paragraph for multi-panel figures.
- **Length.** Titles 3 to 10 words (typical 4 or 5). Whole captions about 40 to 230 words; single-panel figures run 40 to 55 words, multi-panel human evaluation figures 85 to 230. The longest (Fig. 4) carries the statistical method.
- **Tone.** Titles are descriptive labels ("Selective prediction analysis."). The body then states the result as a claim, for example that Med-PaLM narrows the gap with clinicians. So: label title, claim body.
- **Content.** Panel by panel description; n (140 questions, one rater per question); interval method (non-parametric bootstrap, 1,000 replicas, 95% percentile intervals), restated in every human evaluation caption; names of prior models compared. Colour legends are not described. Some abbreviations are defined (USMLE, SOTA) while dataset and model names are not, so captions are nearly but not fully standalone.
- **Tables vs figures.** ED table captions are shorter (about 10 to 30 words, the rater instrument table longer) and purely descriptive; figure captions carry claims and statistics.
- **Example titles.** "Overview of our contributions."; "Comparison of our method and prior state of the art."; "Lay user assessment of answers."

# Order and organisation
- **Outline with approximate words (body about 10,000):**
  - Main: about 750 (8%), followed by a "Key contributions" block of about 350 (3%)
  - Results (no "Results" heading; two top-level blocks): about 3,600 (35%)
    - Model development and evaluation of performance: about 440 (MedQA; MedMCQA and PubMedQA; MMLU)
    - Ablations: about 960 (instruction tuning, scaling, CoT, self-consistency, uncertainty)
    - Human evaluation results: about 1,800 (intro, then consensus; comprehension, retrieval and reasoning; incorrect or missing content; harm; bias; lay users)
  - Discussion: about 475 (5%)
  - Limitations: about 1,300 (13%), five subsections (benchmark expansion, key capabilities, human evaluation, fairness and equity, ethics)
  - Conclusion: about 100 (1%)
  - Methods: about 3,800 (36%): Datasets (eight dataset subsections), Framework for human evaluation, Modelling (PaLM, Flan-PaLM, prompting, instruction prompt tuning, Med-PaLM), Related work.
- **Methods last.** The Key contributions block in Main names every dataset, model and evaluation in advance, and each Results subsection opens with one or two setup sentences (what MedQA is, how many decodes, how many raters) before the number. The Human evaluation intro restates the 140 question sample and bootstrap approach.
- **Results ordering.** Headline benchmark result, then ablations explaining it, then uncertainty, then human evaluation by clinicians axis by axis, then lay users. Automated before human, expert before lay.
- **Heading style.** Mixed. Some headings are claims ("Instruction tuning improves performance", "Self-consistency improves multiple-choice performance", "Scaling improves performance on medical question answering"); others are labels ("Bias for medical demographics", "Lay user assessment"). Claims are used for ablations with a clean positive finding; labels where results were mixed.
- **Figure distribution.** Figures map to result blocks, not subsections: Fig. 2 to benchmarks, Fig. 3 to uncertainty, Fig. 4 to four human subsections, Fig. 5 and Fig. 6 to one each. Ablation subsections have no main figure and lean on Extended Data and Supplementary tables.
- **Discussion sequence.** Emergent ability from scale plus instruction tuning; consistency of gains across sizes and datasets; data contamination check (with supplement pointer); comparison with domain-specific models; human evaluation shows scale is insufficient and alignment matters. Very short; the weight of interpretation moves to Limitations.
- **Supplementary pointers.** About 10 or more in the visible text, mostly in ablation subsections, phrased as "detailed in Supplementary Information, section N" or "reported in Supplementary Information, section N". Numbered sections make pointers precise.
- **Boxes.** None; no key points or graphical abstract. Fig. 1 serves the graphical abstract role.
- **Ease of following.** Fig. 1 plus Key contributions give a map. Harder: ablations sit between headline results and human evaluation, and six thin human evaluation subsections share one six-panel figure.

# Checklist candidates
- Make Figure 1 a one-panel overview of benchmark, models and headline results when the paper has no participant flow. [strong]
- Print the key values on bars in the headline comparison figure. [strong]
- Use one figure with one panel per evaluation axis, and keep the same comparator order and encoding across all human evaluation figures. [strong]
- State n, rater count per item and the interval method (bootstrap replicas, percentile CI) in every caption that shows intervals, even if repeated. [strong]
- Write caption titles as short descriptive labels (3 to 10 words) and put the claim in the caption body. [strong]
- Keep captions for single-panel figures under about 60 words and multi-panel ones under about 230. [weak]
- Define every abbreviation in captions, including dataset and model names, so they stand alone (this paper only partly does). [weak]
- When Methods comes last, add a contributions list in the introduction and open each Results subsection with one setup sentence. [strong]
- Order Results as headline result, ablations, uncertainty, expert human evaluation, lay evaluation. [weak]
- Use claim headings only for subsections with an unambiguous finding; use label headings for mixed results. [weak]
- Move dataset summaries, rater instruments, ablation tables and qualitative examples to Extended Data; keep main text for figures. [weak]
- Point to supplementary material by numbered section ("Supplementary Information, section N"). [strong]
- Report benchmark accuracies as percent with one decimal and mark the authors' model as "(ours)" in comparison tables. [weak]

# Notable deviations
- No main-text tables at all, and no Table 1 of characteristics; unusual for clinical journals, normal for Nature machine learning papers.
- No explicit "Results" heading; Results is split into two top-level blocks plus a separate top-level Limitations section with five subsections, longer than the Discussion.
- Related work is placed inside Methods.
- Extended Data captions and table formatting (bold, footnotes) could not be read directly from the Nature version; table descriptions rest on the arXiv preprint.
