# Paper
Ferber D, et al. Nature Cancer 2025;6:1337 to 1349; original research Article; source: local PDF (13 article pages, Extended Data Fig. 1, Reporting Summary), all pages read.

# Figures
Five main figures, one Extended Data figure, no supplementary figures cited. Supplementary material is text and tables only (Supplementary Notes 1 to 4, Supplementary Tables 1 to 7).

- **Fig. 1, pipeline schematic (orientation).** One unlettered panel in two zones: knowledge database on the left, agent loop with colour-coded tool tiles on the right. Steps carry circled numbers 1 to 5, and the caption walks through them as (1) to (5) instead of panel letters. It sits on page 2, inside the Introduction, and is cited in the last Introduction paragraph as the overview of the whole pipeline. Figure 1 is the system architecture, not a study flow or cohort diagram.
- **Fig. 2, main result (two panels).** Panel a: three example outputs side by side, GPT-4 alone in red speech bubbles above, GPT-4 with tools and RAG in green below, with wrong or generic phrases highlighted red and correct ones green. Panel b: two-bar chart of completeness; each bar carries the percentage in bold plus n/N (30.3%, 33/109 vs 87.2%, 95/109). The x-axis legend uses tick and cross marks for Tools and RAG.
- **Fig. 3, worked example (three stages).** One simulated case: context and question at top, then Stage 1 (strategy and tool calls with images and outputs) and Stage 2 (RAG and the answer, tool-derived sentences highlighted purple). Stages carry circled letters A, B, C on the figure while the caption uses lowercase a, b, c.
- **Fig. 4, main quantitative result (five bar panels).** Tool use, correctness, completeness, helpfulness, citation. Panels are headed by the circled stage letters from Fig. 3, linking metric to pipeline step. Every bar is labelled with percentage and n/N. Encoding: blue for success or correct, purple for failure or wrong, light grey for not required or irrelevant. One bar reads "2/-" because no denominator exists.
- **Fig. 5, comparison with open-weight models (two panels).** Panel a: example tool-call outputs (failures red, GPT-4 success green). Panel b: grouped bars for three models (percent with n/N) plus a right-hand counts subpanel for superfluous failed calls. Models are three shades of blue.
- **Extended Data Fig. 1, robustness and population (four panels).** A sex bar chart, B age histogram, C ethnicity pie, D twenty small heatmaps of tool usage per patient across 15 demographic permutations. Plain matplotlib styling, visibly different from the designed main figures. Caption is on a separate page.

Text refers to panels as "Fig. 2a", "Fig. 2b", "Fig. 5a", "Extended Data Fig. 1a to 1d", and once by metric name ("Fig. 4, 'tool use'"). Uppercase panel letters in the Extended Data figure conflict with lowercase citations in text. No error bars, CIs or p values appear on any figure; numbers on bars are always percentage plus count.

# Tables
No main or Extended Data tables. All tabular content is pushed to Supplementary Tables 1 to 7 (per-tool, per-patient, per-observer and baseline results). There is therefore no Table 1 and no baseline-characteristics table; the case population is shown graphically in Extended Data Fig. 1. Results that live in supplementary tables are only pointed to ("provided in Supplementary Table 4 for review"), while results shown in figures are fully repeated in prose with percent and n/N.

# Captions
- **Structure:** bold title sentence, then a running paragraph with bold lowercase panel letters inline (main figures). The Extended Data caption uses bold uppercase letters in parentheses.
- **Length:** about 95 to 250 words; typical about 180. Fig. 2 is shortest, Fig. 4 longest.
- **Tone of titles:** mostly descriptive labels; one declarative claim. Examples: "Tool use and RAG improves LLM performance" (claim); "High-level overview of the LLM agent framework" (label); "Performance of the agent's pipeline in patient case evaluation" (label).
- **Content:** Fig. 1 caption narrates the pipeline step by step. Fig. 4 caption defines every metric with its numerator and denominator, states that four experts rated, and gives the aggregation rule (majority vote, least favourable answer on ties). Fig. 5 caption interprets results and quotes percentages, essentially a mini Results paragraph. Fig. 3 caption explains a simplification (pre-extracted features) marked by a symbol on the figure.
- **Abbreviations:** inconsistently handled. RAG, MSI, MSS, KRAS and BRAF appear undefined in captions; Llama and Mixtral are spelled out in the Fig. 5 title. Captions mostly stand alone for metric meaning (Fig. 4) but not for acronyms.
- **No statistics section in captions** because no inferential statistics are used; the caption reports counts only.
- Figure titles for Fig. 3 and Fig. 4 are nearly identical ("Details of" vs "Performance of" the agent's pipeline), which weakens scanability.

# Order and organisation
Outline with approximate words (main text plus Methods about 6,700):
1. Abstract, unstructured single paragraph, about 150 (2%).
2. Introduction, unheaded, about 900 (13%), ending with an overview paragraph citing Fig. 1 and the Methods.
3. Results, about 1,500 (22%), four claim headings:
   - Tool use and retrieval improve LLM responses (Fig. 2)
   - GPT-4 handles complex chains of tool use (Figs. 3, 4, 5; Extended Data Fig. 1)
   - Radiology tools improve GPT-4's treatment accuracy (Fig. 3 again)
   - Evaluations show accurate, helpful and reliable responses (Fig. 4)
4. Discussion, unheaded subsections, about 1,700 (25%).
5. Methods, about 2,500 (37%): data collection, PDF curation, RAG, embeddings, tools, response generation, open-model benchmarking, model specifications, case generation, human evaluation, statistics and reproducibility, reporting summary.
6. Data availability, Code availability, References (54), Acknowledgements (includes LLM-use disclosure), Author contributions, Competing interests.

**Methods last.** The Introduction's final paragraph does the bridging work: it summarises case construction, the two-stage agent process, the blinded four-expert evaluation and the three evaluation areas, then points to Fig. 1 and the Methods. Results subsections re-explain each metric briefly before reporting it (for example how statements were segmented before correctness counts).

**Results ordering.** Headline comparison first (agent vs GPT-4 alone), then a worked example, then sequential metrics signposted "First", "Second", "Thirdly", "Fourth" that cut across subsection boundaries. Robustness (demographic permutations) and the open-weight model comparison are tucked inside the second subsection rather than given their own headings. Headings are claims throughout. Each subsection ends with an "In summary" or "Overall" sentence.

**Figure distribution.** One figure feeds several subsections: Fig. 3 serves subsections 2 and 3; Fig. 4 serves 2 and 4. Fig. 1 lives in the Introduction.

**Discussion sequence.** Main finding framed as LLMs being reasoning engines; advantages of the modular tool approach over a generalist foundation model (updatability, regulation, hallucination control via citations); small sample as main limitation and proof-of-concept framing; about ten mixed limitation and future-work paragraphs (tool validation, imaging, architecture, data protection, retrieval, orchestrators); a "To summarize" vision paragraph; closing paragraph on deployment barriers. No Conclusion heading.

**Supplementary pointers.** Frequent, about 15 pointers, phrased plainly ("provided in Supplementary Table 1", "shown in Supplementary Note 1", "highlighted in red in Supplementary Note 2"). Supplementary Notes carry full case texts, raw outputs and pseudocode.

**Boxes and extras.** None: no key points, research in context or graphical abstract. A Nature Portfolio Reporting Summary is appended.

**Ease of reading.** Easy: Fig. 1 early, claim headings, numbers on bars match prose. Hard: the First to Fourth sequence spans headings, model comparison is buried, and limitations are diffuse across about ten paragraphs.

# Checklist candidates
- Make Figure 1 the system or pipeline schematic for a methods-type AI paper and cite it at the end of the Introduction. [strong]
- Place Figure 1 physically near the Introduction so readers see the architecture before Results. [weak]
- Pair a qualitative example panel (outputs side by side, errors highlighted) with the quantitative bar panel in the headline figure. [strong]
- Print percentage and n/N on every bar for small-sample human evaluations. [strong]
- Keep one colour logic across all result panels (success, failure, not applicable) and state it once. [strong]
- Include one worked end-to-end example figure that traces a single case through every tool and output. [strong]
- Reuse stage markers from the pipeline figure as panel headers in the metrics figure. [weak]
- Define each evaluation metric's numerator, denominator and aggregation rule in the caption. [strong]
- Use the same panel-letter case in the figure, caption and text. [strong]
- Give each figure a distinct caption title; avoid near-duplicate titles. [strong]
- Define every abbreviation in each caption so it stands alone. [strong]
- Keep result interpretation in Results, not in captions. [weak]
- Use claim-style Results subheadings, each closed with a one-sentence summary. [strong]
- When Methods come last, end the Introduction with a paragraph summarising data, evaluation design and outcome metrics. [strong]
- Give robustness analyses and baseline comparisons their own Results subsection. [weak]
- Gather limitations into one or two paragraphs rather than scattering them. [weak]

# Notable deviations
- No tables at all, even for per-model results; everything tabular is supplementary.
- No CIs, error bars or tests anywhere; the Statistics section states none were used, unusual for npj Digital Medicine or Lancet Digital Health.
- Fig. 1 uses circled numerals instead of panel letters; Fig. 3 uses circled uppercase letters on the art and lowercase in the caption.
- Fig. 2 caption title is a claim; the other titles are labels.
- Fig. 5b mixes a percentage axis and a separate counts axis in one panel.
- Extended Data figure styling (default matplotlib, uppercase letters) differs from main figures.
- Captions repeat numerical results that also appear in prose.
