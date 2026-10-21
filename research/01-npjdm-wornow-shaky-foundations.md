# Paper

Wornow M, Xu Y, Thapa R, Patel B, Steinberg E, Fleming S, Pfeffer MA, Fries J, Shah NH. The shaky foundations of large language models and foundation models for electronic health records. npj Digital Medicine, 2023.

- Journal: npj Digital Medicine (received 21 March 2023, accepted 13 July 2023)
- Article type: review (labelled Review Article; a narrative, non-systematic review with a perspective-style argument and recommendations)
- Word count estimate: about 5,500 to 6,500 words of main text excluding references and captions; abstract 143 words; 106 references; 4 figures, no tables
- Source used: https://www.nature.com/articles/s41746-023-00879-8 and its PDF (https://www.nature.com/articles/s41746-023-00879-8.pdf). PMC (PMC10387101) returned a captcha; Europe PMC was blocked or rate limited. Note on access: WebFetch would not return long verbatim passages, so the analysis rests on several section-by-section extractions (sentence counts, word counts, short quotes, punctuation and abbreviation inventories) from the full publisher text, not on a verbatim reading of every sentence. Counts are approximate.

# Global patterns

**Sentence length.** Sample of 10 sentences across sections: 13 to 37 words, median about 27. Introduction sentences measured 11 to 49 words; most fall in 18 to 36. Longest observed about 49 words (a sentence in the CLaM training-data subsection justifying why clinical text needs clinical training data). Definitional sentences are shorter (12 to 26).

**Paragraph length.** Introduction paragraphs: 3 to 5 sentences, about 80 to 125 words. Survey subsections: 1 to 2 paragraphs. Discussion: 4 paragraphs, the last short.

**Voice and person.** "We" is frequent and deliberate: in the introduction ("we reviewed", "we begin"), in the survey ("we reorganized", "we collected", "we see"), and especially in recommendations ("we propose", "we recommend", "we must explicitly define", "We invite"). Definitional sections are impersonal and mostly active ("CLaMs ingest", "FEMRs output"); passive appears for training procedures and term definitions ("is typically referred to"). "We" also appears as an inclusive field voice ("If we believe that FMs can help...", "we also lack").

**Tense.** Present simple for definitions, the state of the field, and claims about what models do. Past for the authors' own actions (we reviewed, we collected). Present perfect for field trends (the progress "has" prompted; approaches "have remained fairly separate"). Modal "must", "should" and "can" carry the argumentative intro.

**Hedging and certainty.** Strongly bimodal. Benefits are stated as flat declaratives ("Clinical FMs have better predictive performance."), backed by a citation. Critical findings use certainty words ("almost all", "virtually always", "substantial gaps"). Hedges cluster in the discussion and recommendations: "may", "remains an open question", "still unproven", "it remains unclear", "we believe". Quantitative critique is tied to counts in the same sentence (e.g. "roughly half of all CLaMs surveyed were not validated on clinical text") and pointed to Figs. 2 and 3.

**Punctuation.** Semicolons essentially absent. Colons rare in running prose; used to introduce the contribution list and as run-in labels in numbered items ("Less labeled data: ..."). Parentheses very frequent: abbreviation definitions, "e.g." and "i.e." asides, dataset sizes ("170 million patients"), figure pointers ("(Fig. 2a)"). Em dashes appear a few times for inserted definitions or lists of examples (this is journal-acceptable but conflicts with the user's no-dash rule). Scare quotes mark technical terms ("pre-training", "representation", "patient embedding"). In-sentence lists are comma series with "such as".

**Abbreviations.** About 11 defined. Core ones (FM, EMR, LLM, CLaM, FEMR) are defined in parentheses at first use and some are redefined in the first definitional section (FM, LLM, EMR), giving each major section a self-contained entry point. Two coined acronyms (CLaM, FEMR) carry the taxonomy and are used about 50 times each. Weaknesses: HAIM, FTE and MLOps defined and used once; AI, EHR, ICU, AUROC, AUPRC, USMLE, MIMIC used without expansion; EHR (in the title) and EMR (in the body) coexist without reconciliation. One abbreviation is introduced by appositive ("clinical language models, or CLaMs").

**Numbers.** No inferential statistics. Evidence is counts ("50 CLaMs and 34 FEMRs", "84 models"), dataset sizes in parentheses, and approximate proportions ("roughly half"). Large numbers use words for scale ("18.5 billion words", "170 million patients"). Date cut-off stated (published before 1 March 2023). No percentages with denominators.

**Citations.** Superscript numbers, placed both mid-sentence (directly after the named model or application) and at the end. Lists of example applications carry stacked citations, one per item (up to 6 in one sentence). Roughly 26 citations in a 6-paragraph introduction. No reporting guideline (no PRISMA), consistent with an openly non-systematic review.

**Transitions.** Paragraphs open with a topic sentence naming the logical step ("To clarify these challenges, we...", "Finally, to better quantify...", "Despite these challenges..."). Headings carry the movement between sections.

**Tone.** Mostly sober and critical, but with a few vivid, opinionated words: "breakneck progress", "alarming", "shaky" (title), "immense promise", "unfortunately", "particularly powerful". No "revolutionary", "groundbreaking" or "unlock". The critical vocabulary is the signature: "little", "limited", "sparse", "unclear", "overreliance", "poorer state".

**Word choice.** Plain verbs, jargon defined on first use, lay analogies (ChatGPT as an advanced autocomplete), moderate nominalisation.

# Local patterns by section

**Title.** Declarative-evaluative noun phrase with a metaphor ("The shaky foundations of..."), no colon, 15 words. Names the technology (LLMs and FMs) and data domain (EHRs), not the design.

**Abstract.** Unstructured, 5 sentences, 143 words. Moves: hook (success of ChatGPT and AlphaFold) then problem (hype obscures capability) then what we did (review 84 models, taxonomy) then key finding (narrow data, uninformative evaluations) then contribution (an improved evaluation framework tied to health-system value). One number only (84). Example opening: "The success of foundation models such as ChatGPT and AlphaFold has spurred..."

**Introduction.** 6 paragraphs plus a numbered contribution list. Funnel: (1) define FMs generally; (2) ChatGPT as popular example and rapid clinical uptake with stacked citations; (3) breakneck progress, health leaders lack guidance; (4) argumentative turn with "we" ("If we believe that FMs can help..."), naming the evaluation gap; (5) what we did, scope and exclusions in parentheses, ending "Our primary contributions are:"; numbered list of 3 contributions (largest review plus taxonomy; critique of evaluations; improved framework); (6) roadmap paragraph ("We begin with a brief overview of clinical FMs and..."). Aim and contributions explicit; main finding not previewed in numbers.

**Methods equivalent.** No Methods section. Selection is described in a few sentences at the start of the survey section: 84 models before 1 March 2023, found by following citations from representative recent work plus manual curation, with an explicit disclaimer that no claim of systematicity is made. Exclusions (imaging, genetics, wearables) are stated in the introduction.

**Framework / taxonomy section ("What are clinical FMs?").** Defines FM, then splits into two coined classes, each a subsection with 2 to 3 paragraphs, linked to Fig. 1a and 1b. Example sentence: "Clinical FMs are foundation models built specifically for electronic medical record data."

**Benefits section.** A numbered list of 6 value propositions, each opening with a one-line declarative claim then 2 to 10 explanatory sentences with citations. This list becomes the organising spine reused in the evaluation critique and in Fig. 4, which gives the paper its coherence.

**Results equivalent ("State of published clinical FMs").** Parallel subsections for CLaMs and FEMRs: training data, availability, evaluation on standard tasks, evaluation on FM benefits. Each is 1 to 2 paragraphs, reports counts and dataset sizes, and points to a figure panel. Interpretation is not avoided: evaluative verdicts sit in the same paragraph as the counts.

**Recommendations (Fig. 4 block).** Intro paragraph that frames the list as "by no means comprehensive", then 6 numbered items mirroring the 6 benefits, each with a run-in bold label and colon ("Less labeled data: ..."), proposing metrics, tasks and datasets. Heavy "we propose / we recommend".

**Discussion.** Unheaded in the extracted text, 4 paragraphs. P1 restates the principal finding with the counts ("Our review of 50 CLaMs and 34 FEMRs shows that...") and the recommendation. P2 scope caveat (general-purpose LLMs excluded) and open questions. P3 risks (privacy, interpretability, cost, regulation, bias, automation bias), impersonal and hedged with "may". P4 short call to action: "develop better evaluations to help realize their potential". No formal limitations paragraph about the review method.

**Back matter (order on the page).** Data availability (one sentence: no data beyond what the figures show), References, Acknowledgements (fellowship and institutional support named per author initials), Author contributions (narrative by initials: conceived and designed, extracted data, analysed and wrote, revised; all approved and accountable; not explicitly CRediT labelled), Competing interests (one author's stock compensation disclosed by initials, others declare none), Additional information (correspondence, publisher's note), CC BY 4.0 licence. No Code availability, no separate Funding heading (funding folded into Acknowledgements), no ethics statement (none needed).

**Figures.** Four figures do the evidential work of a results table. Caption style: short bold title sentence ("Overview of CLaMs."), then a summary sentence, then panel-by-panel description (a, b, c). Figs. 2 and 3 captions are long (about 340 to 360 words) and function as the data dictionary. Abbreviations are mostly not re-expanded in captions (only Fig. 1 expands CLaM and FEMR).

# Checklist candidates

- In a review, coin a small taxonomy with named classes and use those names consistently through text, figures and recommendations. [strong]
- Build the paper on one organising list (here 6 benefits) and reuse it as the structure of the critique and of the recommendations. [strong]
- End the introduction with an explicit numbered list of contributions followed by a one-paragraph roadmap. [strong]
- State the scope, cut-off date and exclusions of a narrative review, and say plainly if the search was not systematic. [strong]
- Tie each critical claim to a count, a dataset size or a figure panel in the same sentence or paragraph. [strong]
- Open the discussion by restating the principal finding with the key numbers, then scope caveats, then risks, then a short call to action. [strong]
- Use "we" for the authors' actions and recommendations, and impersonal present tense for definitions. [strong]
- Avoid semicolons; use parentheses for abbreviations, examples and dataset sizes. [strong]
- Write an unstructured review abstract of about 150 words in 5 moves: hook, problem, what we did, finding, contribution. [strong]
- Define each abbreviation at first use in the abstract and again at first use in the main text. [weak] (done for EMR, FM, LLM; AI, EHR, AUROC undefined)
- Do not define an abbreviation that is used only once. [weak] (HAIM, FTE, MLOps violate it)
- Use one term for one concept throughout (EHR vs EMR). [weak]
- Place citations directly after each named example when listing several applications in one sentence. [strong]
- Give figure captions a one-sentence title, then panel-by-panel detail. [strong]
- Include a Data availability statement even for a review with no data. [strong]
- Write a dedicated limitations paragraph for the review method. [weak] (absent; only a scope caveat)

# Notable deviations

- Evocative metaphor title ("shaky foundations") and some vivid wording ("breakneck", "alarming", "immense promise"); acceptable in an npj Digital Medicine review but riskier for JAMIA or Lancet Digital Health original research.
- No Methods section, no PRISMA, explicit disclaimer of systematicity; works for a narrative review but would not pass as a systematic review.
- No limitations paragraph about the review method.
- Em dashes used for insertions (journal accepts them; the user's house style forbids them).
- Flat benefit claims with one citation, although the thesis is that such benefits are under-evaluated.
- Very long figure captions (over 300 words) carry the survey data instead of tables.
- Funding sits inside Acknowledgements; no Code availability heading.
