You are analysing ONE published paper to extract its scientific-writing patterns. The findings will be merged with eight other analyses into a reusable "scientific writing" skill for a clinical-AI researcher who publishes in npj Digital Medicine, JAMIA, Nature and The Lancet Digital Health. Work at medium reasoning effort: careful, but do not over-deliberate.

PAPER
{PAPER}

STEP 1: GET THE FULL TEXT
- Fetch the paper with WebFetch. The preferred source is PubMed Central (pmc.ncbi.nlm.nih.gov) because it serves clean full text. If the URL given fails, use WebSearch with the title plus "PMC" or "full text", and try europepmc.org, the publisher page, or an institutional repository (nih.gov, par.nsf.gov). Do not use curl or Python for downloads; the shell has no web access.
- WebFetch answers a prompt against the page with a small model, so ONE fetch will not give you the whole paper. Make SEVERAL WebFetch calls on the same URL, each with a prompt that asks for the complete, verbatim text of one part: (1) title, abstract and keywords; (2) introduction; (3) methods (or the equivalent section, wherever it sits in the paper); (4) results; (5) discussion and conclusion; (6) back matter: data availability, code availability, author contributions, competing interests, acknowledgements, funding, ethics, reporting summary; (7) figure and table captions. Ask each time for the verbatim text with paragraph breaks preserved, no summary. If a section is long, split the request (first half, second half).
- Read everything before analysing. If you truly cannot reach the full text after trying at least three sources, write an analysis file that says so clearly at the top and analyse what you could get.

STEP 2: ANALYSE
Extract patterns at two levels.

GLOBAL (the whole scientific register of this paper):
- Sentence length: estimate the typical range and the longest sentence (count words on a sample of 20 sentences from different sections). Paragraph length in sentences and approximate words.
- Voice and person: active vs passive, "we" usage, where each appears.
- Tense by section (present, past, present perfect) and what each tense is used for.
- Hedging and certainty vocabulary: which verbs and adverbs carry claims (suggest, demonstrate, show, indicate, may, could, likely). How strong claims are tied to evidence (a citation, a figure, a table, a number) in the same sentence.
- Punctuation habits: use or avoidance of colons, semicolons, parentheses, dashes; how lists inside sentences are built.
- Abbreviations: how they are introduced (at first use in abstract and again in main text?), how many are used, whether every defined abbreviation is reused, whether any are defined but used once.
- Numbers and statistics: how results are stated (point estimate, CI, p value, n), decimal places, units, how percentages and counts appear together.
- Citation placement: mid-sentence vs end, how many per claim, citation of guidelines, reporting checklists (TRIPOD, CONSORT, STROBE, PRISMA, CLAIM, etc.).
- Transitions and flow: how paragraphs open (topic sentence style), the words that link paragraphs, how the paper moves from known to unknown to what-we-did.
- Tone: any emotional, promotional or blog-style wording (revolutionary, groundbreaking, unlock, exciting). Note whether the paper avoids or uses it.
- Word choice: nominalisations, jargon density, whether plain words are preferred.

LOCAL (per section), note the structure, moves, length, and 1 to 3 example sentences each (quote at most 12 words per example, paraphrase longer passages):
- Title: form (declarative claim vs descriptive phrase vs colon subtitle), length, whether it names the method, population, design (multicentre, randomised, observational).
- Abstract: structured or not, word count, the move sequence (background, gap, aim, methods, key numbers, conclusion), which numbers appear.
- Introduction: number of paragraphs, the funnel (field, problem, prior work and its limits, gap, this study's aim and contribution), whether the last paragraph states the aim and design explicitly, whether results are previewed.
- Methods: ordering of subsections, level of detail, ethics and consent statement placement, data sources, model description, evaluation metrics, statistics paragraph, reporting guideline named.
- Results: ordering (cohort description first?), how each paragraph maps to a figure or table, how comparisons are phrased, whether interpretation is avoided.
- Discussion: first paragraph (summary of principal findings?), comparison with prior work, mechanisms or explanations, clinical or practical implications, limitations paragraph (position, length, how limitations are mitigated), future work, conclusion paragraph (how it restates the claim at the strength the evidence supports).
- Back matter: exact headings present and their order, the standard phrasing used for data availability (and whether access is controlled), code availability, author contributions (CRediT style?), competing interests, funding, ethics, acknowledgements, reporting summary.
- Figures and tables: caption style (one-sentence title then detail?), how abbreviations are handled in captions.
- For a REVIEW or PERSPECTIVE paper, map the equivalent sections (e.g. framework, taxonomy, challenges, recommendations, boxes) and describe how the argument is organised and how evidence is marshalled without original results.

STEP 3: WRITE THE ANALYSIS FILE
Write your analysis to {OUTFILE} in Markdown with exactly these top-level headings:
# Paper
(citation in this exact style: surname then initials with no periods, comma separated, then a period; full title; then journal and year. Then journal, article type (original research / review / perspective), word count estimate, source URL used.)
# Global patterns
# Local patterns by section
# Checklist candidates
(a bullet list of concrete, checkable rules this paper supports, each phrased as an instruction, e.g. "Define an abbreviation at first use in the abstract and again at first use in the main text." Mark each with [strong] if the paper consistently follows it or [weak] if only partly.)
# Notable deviations
(anything this paper does that contradicts common advice, e.g. uses semicolons freely, very long sentences, so the merger knows which rules are journal-specific.)

Constraints: never quote more than 12 consecutive words from the paper; prefer paraphrase. Do not use em dashes or en dashes anywhere in your file. Keep the file under about 1800 words. When finished, reply with a 5 line summary of the most distinctive patterns you found and confirm the file path.
