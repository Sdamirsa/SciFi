# Paper

Moor M et al. Foundation models for generalist medical artificial intelligence. Nature 2023;616:259-265. Perspective (review-type, no original data). Source: NSF public-access copy, https://par.nsf.gov/servlets/purl/10471867, read through several targeted WebFetch calls (verbatim text not returned, so counts are approximate).

# Figures

- **Count and type.** Two main figures, both schematics. No extended data, no supplementary figures, no data plots of any kind. This fits a Perspective: figures carry concepts, not results.
- **Figure 1** (2 panels, a and b): a pipeline overview. Panel a shows one model trained by self-supervision on many data types, pairing images or EHR data with text or speech, drawing on knowledge sources (knowledge graphs, databases) and taking tasks specified in real time. Panel b shows the same model as a base under many clinical applications, each of which still needs validation and regulatory review. Purpose: orientation. It is the visual definition of the paper's central concept, so Figure 1 is the conceptual framework rather than a study overview.
- **Figure 2** (3 panels, a to c): worked examples of applications. a, bedside decision support; b, grounded radiology reports with clickable links per finding; c, classifying a never-seen phenomenon during an augmented procedure (vessel at duodenoscopy suggesting aortoduodenal fistula). Includes example queries, outputs and icons for input types (EHR, audio, text). Purpose: worked example that makes abstract capabilities concrete. Panel c reuses a published case image, credited in the caption with its licence.
- **Numbers on figures.** None; no n, values, p values or CIs, since there are no data.
- **Panel labelling and in-text referencing.** Lowercase letters (a, b, c) in captions. The text never cites a panel letter. Figure 1 is cited once, as "(Fig. 1)", at the end of the introduction where the three defining capabilities are announced. Figure 2 is cited twice, both in the Augmented procedures subsection, once with a positional phrase ("right panel") instead of "Fig. 2c". The Grounded radiology reports and Bedside decision support subsections, which panels b and a illustrate, do not cite the figure at all.
- **Panel order versus text order.** Figure 2 panels run bedside, radiology, procedures; the text sections run radiology, procedures, bedside. The figure and text order are not aligned.
- **Colour and encoding.** Captions say nothing about colour; no encoding legend is given.
- **Main versus supplementary.** Everything is in the main text; nothing is pushed out.

# Tables

None. The paper has no tables, no boxes and no glossary table, even though it lists many use cases and challenges that could have been tabulated. Lists of capabilities, use cases and challenges are carried by headed subsections instead.

# Captions

- **Structure.** Short title sentence, then a running paragraph with panel-by-panel sentences introduced by the bare panel letter and a comma. Bold title cannot be confirmed from the extracted text, but Nature house style sets it in bold after "Fig. N |".
- **Length.** Figure 1 about 145 words (7 sentences); Figure 2 about 90 words (7 sentences). Range about 80 to 145, typical about 110. Title sentences are 8 to 9 words.
- **Tone.** Titles are descriptive labels, not claims. Body sentences mix description with hedged potential ("could", "has the potential to"), with one mildly promotional phrase in Figure 1 about unlocking capabilities. No caption tells the reader what to notice.
- **Content.** Panel-by-panel description of what the schematic shows, plus image attribution and licence for reused material. No statistics, no data source beyond the case report, no colour legend.
- **Abbreviations.** GMAI and EHR are not redefined in captions; captions lean on the main text and do not fully stand alone.
- **Table titles.** Not applicable.
- **Example titles (paraphrase plus short quote).** "Overview of a GMAI model pipeline." "Illustration of three potential applications of GMAI."

# Order and organisation

Approximate main-text words about 5,000 (excluding references and back matter).

| Section | Words | Share |
|---|---|---|
| Summary (unlabelled) | 160 | 3% |
| Introduction (unlabelled) | 750 | 15% |
| The potential of generalist models in medical AI (intro 150; Flexible interactions 130 with Dynamic task specification 150 and Multimodal inputs and outputs 190; Medical domain knowledge 230) | 850 | 17% |
| Use cases of GMAI (intro 40; Grounded radiology reports 260; Augmented procedures 240; Bedside decision support 280; Interactive note-taking 170; Chatbots for patients 330; Text-to-protein generation 260) | 1,580 | 31% |
| Opportunities and challenges of GMAI: Paradigm shifts (Controllability 110, Adaptability 280, Applicability 200) | 645 | 13% |
| Challenges of GMAI (Validation 180, Verification 230, Social biases 170, Privacy 180, Scale 420) | 1,180 | 23% |
| Conclusion | 300 | 6% |

Back matter: acknowledgements, author contributions, competing interests, additional information, then about 1,450 words of references.

- **Methods.** None; a Perspective has no Methods or Results. The introduction does the orienting work: it defines the concept, points to Figure 1 for the three capabilities, and closes with a one-paragraph roadmap (strategies, high-impact applications, core challenges).
- **Body logic.** Define (what the concept can do) then show (six use cases) then weigh (paradigm shifts, then challenges) then conclude. The capability section uses up to three heading levels. Headings are short noun-phrase labels throughout (Validation, Privacy, Scale), never claims.
- **Use-case order.** Moves from clinician-facing imaging and procedures, to bedside and documentation, to patient-facing chatbots, to a research application (protein generation). Roughly clinician to patient to bench.
- **Challenges order.** Evaluation first (validation, verification), then ethics (bias, privacy), then practicalities (scale, the longest subsection).
- **Conclusion.** Three paragraphs: restate the promise and the three capabilities; restate the main hurdles (validation, cost, data); call to action for the AI and clinical communities, ending on concrete benefits for clinicians and patients.
- **Figure distribution.** Figure 1 serves the whole concept section and the intro; Figure 2 serves the use-case section but is cited from only one subsection.
- **Supplementary material.** None, and never mentioned.
- **Boxes, key points, graphical abstract.** None.
- **Ease of reading.** Easy to navigate thanks to parallel short headings and a clear roadmap. Weaker points: figure panels are not cited by letter, Figure 2 panel order does not match the section order, and the "Opportunities and challenges" section nests two very unequal halves.

# Checklist candidates

- In a perspective or review, make Figure 1 the conceptual framework that defines the central idea, cited from the introduction where that idea is introduced. [strong]
- Use a second figure of worked example cases (example input, query, output) to make abstract capabilities concrete. [strong]
- Credit any reused image in the caption with source reference and licence. [strong]
- Start each caption with a short descriptive title of under 10 words, then describe each panel in order with its letter. [strong]
- Keep perspective captions at about 80 to 150 words. [weak]
- Use parallel noun-phrase labels, not claims, for subsection headings in a perspective. [strong]
- End the introduction with a one-paragraph roadmap naming the main sections. [strong]
- Order a challenges section from evaluation, to ethics, to practical deployment. [weak]
- Close with a short conclusion of about 300 words: promise, hurdles, call to action. [strong]
- Cite every figure panel by letter (Fig. 2c) from the subsection it illustrates; do not use positional phrases such as "right panel". [strong; this paper falls short]
- Match panel order to the order in which the text discusses the examples. [strong; this paper falls short]
- Define abbreviations in captions so figures stand alone. [weak; this paper does not]
- A perspective can omit tables, boxes and supplementary material when headed subsections carry the lists. [weak]

# Notable deviations

- No tables, boxes, key points or supplementary material at all, unusual even for Nature Perspectives, which often use a box or summary table.
- Figure panels are never cited by letter; one citation uses "right panel", which conflicts with lettered panels.
- Figure 2 panel order (bedside, radiology, procedures) differs from the text order (radiology, procedures, bedside), and two of the three illustrated subsections never cite the figure.
- Captions use GMAI and EHR undefined, so they depend on the main text.
- Introduction and summary are unlabelled, as per Nature format, so the roadmap paragraph does the signposting a heading would.
