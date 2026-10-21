# Paper

Scherbakov D et al. LLMs as tools in literature reviews: an LLM-assisted systematic review. JAMIA 2025;32(6):1071-1086; systematic review (PRISMA 2020); source https://pmc.ncbi.nlm.nih.gov/articles/PMC12089777/ (several WebFetch passes; counts are estimates).

# Figures

Six main figures, no supplementary figures. Descriptive bibliometric figures dominate; there are no ROC, forest or calibration plots.

| No. | Type | Panels | Purpose |
|---|---|---|---|
| 1 | Workflow schematic (Covidence plus LLM add-on for screening and extraction) | 1 | Orientation to the method |
| 2 | PRISMA flow diagram | 1 | Study selection |
| 3 | Map or bar chart by country (A) and by US state (B) | 2 | Descriptive (geography) |
| 4 | Frequency bar charts: review types (A), automated stages (B) | 2 | Main descriptive result |
| 5 | Bar chart of LLM families (only those named in 2 or more studies) | 1 | Main descriptive result |
| 6 | Boxplots of performance metrics for the 3 most common stages, GPT (A) vs BERT (B) | 2 | Secondary result (performance) |

- **Figure 1** is the method pipeline rather than the PRISMA flow, because the paper's novelty is its own LLM-assisted method. It is cited in Methods. The PRISMA diagram is pushed to Figure 2 and opens Results.
- **Figure order follows Results order** exactly: selection, geography, review type and stage, model family, performance.
- **Numbers on figures**: none can be confirmed from captions. The counts (n and %) are given in the prose instead. The Figure 6 caption flags a mismatch: boxes show medians while the text compares means.
- **Panel labels**: capital letters in parentheses inside captions, "(A) ... (B) ...". The text uses "Figure 4A" and "Figure 4B" for Figure 4 only; Figures 3 and 6 are cited as whole figures even when the prose reports one panel (US state data from 3B has no pointer).
- **Encoding**: Figure 6 contrasts two model families as separate panels, not as colours in one plot.
- **Unusual point**: Methods states that ChatGPT wrote the R code that generated Figures 3 to 5, so figure provenance is disclosed in the text.

# Tables

Two main tables and five supplementary tables (S1 to S5) plus two supplementary files.

- **Table 1, Search strategy** (Methods): one cell holding the full Boolean string, an LLM term block AND a review term block, with asterisk truncation. No headers, no footnote. So Table 1 here is not baseline characteristics; a review uses Table 1 for the reproducible search.
- **Table 2, Summary table of reviewed citations** (Results): about 58 rows, five columns: Citations (author, year plus reference number, separated by semicolons), Review stage, M/R (methods or review paper), LLM family, Review type. Rows are groupings of stage by paper type by model, not single studies; counts are implicit in the number of citations per cell. No numbers, decimals, units or bold.
- **Footnote** of Table 2 is an abbreviation key (R, M, Sys., Scop., N, model families). Weakness: "M" means both methods paper and meta-analysis, and "Other" and "Non-specific" are not defined.
- **Supplementary tables**: S1 prompts (three per phase), S2 to S4 benchmarks of the LLM screening and extraction, S5 the full extraction table for all 172 studies. File S1 holds time savings and compute cost; File S2 the PRISMA checklist.
- **Prose vs table**: Results prose gives the counts and percentages (n = 118, 68.6% and so on) and cites "Figure 4A and Table 2" together, so the table is pointed to and the numbers are carried by text plus figure, not by the table.

# Captions

- **Structure**: title only, a single sentence fragment ending with a full stop. Two panel captions list panels inline as "(A) X. (B) Y." Only Figure 6 adds a second sentence (median vs mean note).
- **Length**: tables 2 to 5 words; figures 7 to 30 words; typical about 10 to 12.
- **Tone**: purely descriptive labels, never a claim. Examples: "LLM workflow added into Covidence for screening and extraction"; "Flow diagram of the systematic review process"; "Summary table of reviewed citations".
- **Content**: no abbreviation definitions in figure captions (LLM, GPT, BERT assumed known), no n, no statistics except Figure 6's note, no data source, no colour legend, no "what to notice". Captions do not stand alone; the reader needs the text.
- **Table titles vs figure captions**: table titles are even shorter; tables carry their abbreviation key as a footnote, figures carry none.

# Order and organisation

Outline (main text about 3,900 words, abstract about 240):

| Section | Words | Share |
|---|---|---|
| Abstract (Objectives; Materials and Methods; Results; Discussion and Conclusion) | 240 | separate |
| Introduction (10 paragraphs, no subheads) | 1,000 | 26% |
| Methods (no subheads) | 1,200 | 31% |
| Results (9 paragraphs, no subheads) | 800 | 20% |
| Discussion (4 paragraphs) | 500 | 13% |
| Limitations (2 paragraphs, own heading) | 220 | 6% |
| Conclusion (2 paragraphs) | 200 | 5% |

Back matter: Supplementary Material, Acknowledgments, Author contributions, Funding, Conflicts of interest, Data availability, References.

- **Methods before Results** (IMRaD), so Results re-explains nothing; it opens directly on the PRISMA figure.
- **Methods flow** without headings: protocol and PRISMA, eligibility, search (Table 1), Covidence plus LLM workflow (Figure 1), prompts and calibration (S1, S2 to S4), charting form, analysis, disclosure of ChatGPT and Scite.ai use for drafting and figures, time savings (File S1).
- **Results logic**: selection numbers, then descriptive characterisation (country, review type, stage, model), then performance, then publication type, author stance and funding, ending with a pointer to the full table (S5). One paragraph per figure; Table 2 feeds two paragraphs (types and stages). No subsection headings, so neither claims nor labels.
- **Discussion sequence**: (1) many projects cover single stages, few the full cycle; journal policy as barrier; (2) strengths of this review and implications for workload and access; (3) GPT performance, strong in extraction, weak in searching due to hallucinated citations; (4) cost and local smaller models. Then a separate Limitations section (accuracy of LLM reviewers on some fields; reliance on self-disclosure of LLM use) and a Conclusion (rapid growth plus call for disclosure of prompts; meta-analysis still hard, scoping reviews feasible).
- **Supplementary pointers**: about five, all short parenthetical or standalone sentences of the form "detailed in Table S1", "provided in Tables S2-S4", "we report ... in Supplementary File S1". Four sit in Methods, one closes Results, none in Discussion.
- **Boxes**: no key points, highlights or graphical abstract in the PMC version.
- **Ease of reading**: figure sequence mirrors prose, which is easy to follow. Hard parts: no Methods or Results subheadings in a 1,200 word Methods; Introduction longer than Results; Table 2 is a citation dump with no counts; panel citations inconsistent.

# Checklist candidates

- In a review, make Table 1 the full reproducible search string, or move it to the supplement if space is tight. [strong]
- Place the PRISMA flow diagram as the first figure cited in Results. [strong]
- If the paper's novelty is a method or pipeline, use Figure 1 for the workflow schematic and cite it in Methods. [weak]
- Order figures so their numbering follows the Results narrative one paragraph per figure. [strong]
- Cite panels by letter (Figure 3B) whenever the sentence reports one panel's data. [strong]
- Label multi-panel captions inline with "(A) ... (B) ..." in the same order as the panels. [strong]
- When a plot shows medians but the text compares means, say so in the caption. [strong]
- State in Methods which tool generated figures and code if an LLM produced them. [strong]
- Put an abbreviation key under every table that uses coded labels, and never reuse one letter for two meanings. [strong]
- Give counts and percentages in the prose and point to the figure or table, rather than leaving numbers only in a graphic. [strong]
- Keep supplementary pointers short and specific (item number plus content), mostly in Methods. [strong]
- Give Limitations its own heading in JAMIA reviews and keep it to about 5 to 6% of the text. [weak]
- Use descriptive label captions; for JAMIA expand them with n and abbreviations so they stand alone. [weak]

# Notable deviations

- Captions are minimal titles that do not define abbreviations or give n, below the self-contained caption norm of Nature-portfolio and Lancet journals.
- Table 2 lists citations grouped by codes with no counts, so it summarises nothing numerically; a counts matrix would serve better.
- Inconsistent panel citation (only Figure 4 cited by panel).
- Figure 6 shows medians while the text reports means, a mismatch flagged only in the caption.
- Introduction (26%) is longer than Results (20%), and Methods has no subheadings despite being the largest section.
- On-figure values could not be checked from the HTML text; every quantity is restated in prose.
