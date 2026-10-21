# Paper
Oikonomou EK et al., Eur Heart J 2019;40:3529-3543 (doi:10.1093/eurheartj/ehz592), original research (FastTrack Clinical Research, translational, three linked studies); source: local publisher PDF, all 15 pages read.

# Figures
Seven numbered main figures plus a "Take home figure" (a central illustration). All sit in shaded boxes with a coloured bold "Figure N" label.

- **Figure 1, workflow diagram (1 panel, orientation).** Three colour-coded columns (Study 1 blue, Study 2 orange, Study 3 green) crossed by three rows labelled AIM, COHORT, ANALYSES. Cohort sizes are in the boxes (167 biopsies; 101 MACE plus 101 controls; 1,575 SCOT-HEART; 44 AMI plus 44 stable CAD). It leads because three studies need a map; Methods cites it first.
- **Figure 2, Study 1 main result (5 panels, A to E).** A to C are Manhattan plots of -log10 P per radiomic feature against gene expression (TNFA, COL1A1, CD31), with first-order features in green, texture features in red, a dashed Bonferroni line, and the top features labelled with arrows. D is a 3D principal component scatter. E is a stacked bar panel of F statistics for three nested regression models per gene, with P for F change printed above brackets and small tissue cartoons on the left.
- **Figure 3, data description (3 panels).** A shows CT images of RCA and LCA with colour-coded PVAT segmentation and a HU colour bar; B a clustered correlation heatmap of 1,391 features; C a Z-score heatmap of features by patients.
- **Figure 4, model development schematic (1 panel).** Pictogram people (highlighted cases versus controls) flow from the 5,487 scan pool through 1:1 matching, an 80/20 split, threefold repeated 5-fold cross-validation, external validation, then cohort-wide testing in SCOT-HEART.
- **Figure 5, model result (3 panels).** A Manhattan-type plot of univariable discrimination with three dashed P thresholds (0.05, 0.01, 0.001) and labelled top features; B external validation ROC with the AUC and 95% CI printed inside the plot; C a lollipop variable-importance chart of the top 20 features, alternately shaded rows, beside a small grid of plus signs coding association strength with inflammation, fibrosis and vascularity.
- **Figure 6, prognostic result (6 panels).** Kaplan-Meier curves (A, B, D, E, F) with adjusted HR, 95% CI and P printed on the plot, group n in the legend, and number-at-risk tables beneath; C is a time-dependent ROC comparing traditional model (black) with model plus FRP (red), with delta AUC and P printed.
- **Figure 7, Study 3 result (4 panels).** Tukey box plot (A), paired spaghetti plots with dual y axes for FRP and FAI (B, D), and a line plot along the culprit lesion with shaded areas labelled AUC1 and AUC2 (C). P values sit at the top of each panel.
- **Take home figure.** Cartoon of a vessel in three states (healthy, early, chronic inflammation) above two colour gradient bars showing FAI and FRP from low to high, with biological descriptors between them.

Panel labels are bold capitals A to F. The text cites panels in italics as "Figure 2A", "Figure 2B, C", "Figure 6E, F"; supplementary figures as "Supplementary material online, Figure S3". Encoding: red for the new model or high-risk group, black for baseline, teal for low FRP; red for AMI versus green for stable CAD. Numbers on figures: effect sizes, CIs and P values are drawn directly on the plots, so many result sentences are verifiable from the figure alone.

Supplementary: figures S1 to S5 (feature counts, stability analysis, recursive feature elimination, internal validation, cut-off selection). Method checks, tuning and threshold derivation go there.

# Tables
No main-text tables. All tabular content (demographics S1 to S4, radiomic feature definitions S5 to S12) is in the Supplement. Baseline characteristics, the usual Table 1, are referenced in the first Methods sentence and again in Results for matching ("Supplementary material online, Table S2"). Results that would normally sit in a performance table (HRs, AUCs) are printed on the Kaplan-Meier and ROC panels and repeated in the prose.

# Captions
- **Structure:** bold coloured label, then a short descriptive title sentence, then a panel-by-panel paragraph with lettered panels in parentheses, then a block of abbreviation definitions. Figure 7 ends with the statistical test used for each panel.
- **Length:** about 85 to 190 words; typical about 120. Figure 1 and Figure 6 are the longest; Figure 3 the shortest.
- **Tone:** descriptive labels, not claims. Examples: "Workflow diagram."; "Radiomic phenotyping to detect biological hallmarks of dysfunctional adipose tissue."; "Prognostic value of the pericoronary fat radiomic profile." The Take home figure caption is the exception: it narrates the biological model and ends with a value statement.
- **Content:** what each panel plots, n per group, the significance threshold (Bonferroni alpha), model specifications (covariates of nested models listed in full), the housekeeping gene in a footnote marker, legend of plus-sign codes, and test names. Colours are explained in words only in Figure 2.
- **Abbreviations:** redefined in every caption, alphabetised, separated by semicolons. Captions stand alone.
- **Tables:** none in main text, so no contrast available.

# Order and organisation
Approximate word counts (main text about 4,300 words, excluding abstract and references):
1. Structured abstract (Background, Methods and results, Conclusion, Keywords) about 330
2. Translational perspectives box about 110
3. Introduction about 550 (13%)
4. Methods about 1,500 (35%): Study design (Study 1, Study 2, Study 3); CCTA protocol, data collection and definitions; Radiomic analysis (Image transfer and segmentation; Radiomic characterization); Adipose tissue collection, RNA isolation and gene expression; Statistical analysis
5. Results about 1,000 (23%): four subsections, one per study arm
6. Discussion about 1,100 (26%): unheaded opening paragraph, then four headed subsections including Limitations
7. Conclusions about 150 (3%)
8. Supplementary material, Acknowledgements, Funding, Conflict of interest, References (39)

Methods precede Results, so Results re-explains little; it restates only cohort sizes and the split, because each Results subsection opens by naming its study.

Results ordering follows the study chain rather than a data, main, secondary, robustness sequence: biology discovery (Study 1), signature derivation (Study 2a), prognostic test (Study 2b), acute event behaviour (Study 3). Subsection headings are labels with the study tagged in parentheses, e.g. "(Study 2a)"; only the first edges toward a claim. Figures map neatly: Figure 2 to Study 1; Figures 3, 4, 5 to Study 2a; Figure 6 to Study 2b; Figure 7 to Study 3. Figure 4 is cited from both Methods and Results.

Discussion sequence: opening paragraph summarising all findings and pointing to the Take home figure; PVAT biology background and the gap FAI leaves; radiotranscriptomic discovery interpreted against oncology radiomics; FRP development and incremental value; FRP in AMI, contrasting patient-level versus lesion-level indices; Limitations (event count, compute time, left circumflex exclusion, ongoing validation study). Conclusions repeats the FAI versus FRP contrast.

Supplement is pointed to very often (over 20 times) with the fixed EHJ phrase "Supplementary material online", sometimes alone as a parenthetical and sometimes with a specific table or figure. Boxes: structured abstract, "Translational perspectives" (five sentences: known mechanism, new signature, what it detects, incremental value, FAI versus FRP contrast), and the Take home figure as graphical summary.

Ease of reading: shared Study 1/2/3 labels across Figure 1, Methods, Results and figures make it easy to follow; dense abbreviations (FAI, FRP, PVAT, HRP, CCS) make it harder.

# Checklist candidates
- When a paper combines several studies, make Figure 1 a grid of studies by aim, cohort (with n) and analysis, and reuse those study labels in Methods, Results headings and captions. [strong]
- Tag each Results subheading with the study or cohort it reports, e.g. "(Study 2b)". [strong]
- Assign each Results subsection its own figure, in reading order. [strong]
- Print the headline statistic (HR with 95% CI and P, or AUC with 95% CI) inside the plot area of KM and ROC panels. [strong]
- Put number-at-risk tables under every Kaplan-Meier panel and group n in the legend. [strong]
- Use one consistent colour for the proposed model or high-risk group and a neutral colour for the baseline across all figures. [strong]
- Include a schematic figure for the train, internal validation, external validation and cohort testing split, with percentages. [strong]
- Write figure captions as: short descriptive title; panel-by-panel description; tests and thresholds; alphabetised abbreviations. [strong]
- Redefine all abbreviations in every caption so it stands alone. [strong]
- State in the caption the statistical test behind each panel's P value. [weak]
- Keep captions descriptive; reserve claim-style wording for a central illustration caption. [weak]
- Move demographics and feature definition tables to the Supplement when the main text is figure-driven, and cite them by number. [weak]
- Close the Discussion opening paragraph with a pointer to the central illustration. [weak]
- Add a short translational box of about five sentences moving from known mechanism to new tool to clinical implication. [weak]
- Put Limitations as the last headed Discussion subsection, followed by a separate short Conclusions section. [weak]

# Notable deviations
- No main-text tables at all; even baseline characteristics live in the Supplement, unusual for a clinical cohort paper.
- Discussion is nearly as long as Methods and contains headed subsections, a journal-specific EHJ style.
- Captions are descriptive labels, unlike claim-style titles common in Nature-portfolio journals.
- Study 2 is split into 2a and 2b only in Results, not in Figure 1 or Methods.
- Figure 7 uses dual y axes and a broken y axis, both choices many style guides discourage.
- The Take home figure is a conceptual cartoon of biology, not a summary of data.
