#!/usr/bin/env python3
"""Deterministic checks for a scientific manuscript.

Usage:
    python3 check_manuscript.py manuscript.md [--journal npj|jamia|nature|lancet|ehj|default]
                                              [--max-sentence 40] [--min-sentence 8]
                                              [--max-paragraph 150] [--min-paragraph 80]
                                              [--allow ABBR,ABBR2] [--json]

Accepts .md, .txt, .tex (treated as text) and .docx (paragraph text only).
Prints a Markdown report. Exit code is 0 always; the report is the product.

Checks:
  1. Sentence length (too long, too short)
  2. Paragraph length
  3. Colons and semicolons in prose; em and en dashes; spaced hyphens used as dashes
  4. Banned and caution words
  5. "significant" without a p value or CI in the same sentence
  6. Abbreviations: used before definition, defined but rarely reused, defined twice, never defined, competing terms
  7. Number formatting: mixed CI styles, mixed percentage precision, thousands separators, p-value style, P versus p
  8. Figure and table citation order, uncited items, positional panel references
  9. Section presence by journal profile
 10. Spelling variant mix (-ise / -ize), serial comma hints
 11. Self-consistency hints: repeated percentages that differ slightly, leftover drafting notes

Everything here is a heuristic. A flagged line is a prompt to look, not a verdict.
"""

import argparse
import json
import re
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

# ----------------------------------------------------------------------------
# Word lists
# ----------------------------------------------------------------------------

BANNED = [
    "novel", "groundbreaking", "ground-breaking", "revolutionary", "revolutionise", "revolutionize",
    "remarkable", "remarkably", "striking", "strikingly", "exceptional", "exceptionally",
    "unprecedented", "paradigm shift", "paradigm-shifting", "cutting-edge", "cutting edge",
    "state-of-the-art", "state of the art", "milestone", "immense", "drastically", "dramatically",
    "tremendous", "tremendously", "exciting", "excitingly", "powerful", "unlock", "unlocks",
    "unlocking", "leverage", "leverages", "leveraging", "leveraged", "game-changing", "game changing",
    "holistic", "seamless", "seamlessly", "breakthrough", "transformative", "unparalleled",
    "exceedingly", "profound", "profoundly", "utilize", "utilise", "utilized", "utilised",
    "utilizing", "utilising", "delineate", "delineates", "encompass", "encompasses", "synergize",
    "synergise", "synergistic", "delve", "delves", "delved", "delving",
]

CAUTION = [
    "robust", "crucial", "crucially", "vital", "importantly", "interestingly", "surprisingly",
    "notably", "promising", "clearly", "obviously", "of note", "it is worth noting", "note that",
    "superior", "superiority", "excellent", "impressive", "impressively", "essential",
    "key", "critical", "critically", "first", "innovative", "pioneering", "intriguing",
    "intriguingly", "highly", "extremely", "very", "indeed",
]

DRAFT_NOTES = [
    "todo", "tbd", "xxx", "fixme", "placeholder", "[ref]", "[cite]", "[n=?]", "lorem ipsum",
    "insert", "add citation", "check this",
]

COMPETING_TERMS = [
    ("EHR", "EMR"),
    ("AUC", "AUROC"),
    ("AUC", "C-statistic"),
    ("AUROC", "C-statistic"),
    ("CI", "confidence interval"),  # fine once, flagged if 'confidence interval' recurs after CI defined
    ("ML", "machine learning"),
]

# Abbreviations that need no definition in a clinical-AI manuscript.
DEFAULT_ALLOW = {
    "CT", "MRI", "PET", "ECG", "EKG", "DNA", "RNA", "USA", "UK", "EU", "US", "IQR", "SD", "SE",
    "CI", "HR", "OR", "RR", "AI", "ID", "PDF", "URL", "DOI", "ICU", "ED", "BMI", "HU", "ROC",
    "GPU", "CPU", "API", "HIV", "COVID", "IRB", "FDA", "CE", "ISO", "MIT", "XML", "JSON", "CSV",
    "IEEE", "ACM", "NHS", "WHO", "ESC", "AHA", "ACC", "NICE", "PRISMA", "TRIPOD", "STROBE",
    "CONSORT", "STARD", "CLAIM", "GPT", "LLM", "LLMs", "MIMIC", "III", "IV", "II", "VI",
    "RAM", "SSD", "FIG", "TABLE", "SI", "ANOVA", "RCT", "OSF", "NIH", "SNF", "SNSF", "ERC",
    "TODO", "TBD", "XXX", "REF", "NA", "AND", "OR", "NOT", "JAMIA", "EHJ", "BMJ", "JAMA", "NEJM",
}

SECTION_PROFILES = {
    "default": ["abstract", "introduction", "methods", "results", "discussion"],
    "jamia": ["abstract", "introduction", "methods", "results", "discussion", "conclusion"],
    "lancet": ["abstract", "research in context", "introduction", "methods", "statistical analysis",
               "role of the funding source", "results", "discussion", "contributors",
               "declaration of interests", "data sharing"],
    "nature": ["abstract", "results", "discussion", "methods", "data availability", "code availability",
               "author contributions", "competing interests"],
    "npj": ["abstract", "results", "discussion", "methods", "data availability", "code availability",
            "author contributions", "competing interests"],
    "ehj": ["abstract", "translational perspective", "introduction", "methods", "statistical analysis",
            "results", "discussion", "limitations", "conclusion", "funding", "conflict of interest"],
}

BACK_MATTER_HINTS = ["data availability", "code availability", "author contributions", "contributors",
                     "competing interests", "conflict of interest", "declaration of interests",
                     "funding", "acknowledg", "ethics", "data sharing", "reporting summary"]

# ----------------------------------------------------------------------------
# Input handling
# ----------------------------------------------------------------------------


def read_docx(path: Path) -> str:
    """Extract paragraph text from a .docx without external dependencies."""
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf8", errors="ignore")
    paras = re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S)
    out = []
    for p in paras:
        texts = re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, flags=re.S)
        line = "".join(texts)
        line = line.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        is_heading = "<w:pStyle w:val=\"Heading" in p or "w:pStyle w:val=\"Title" in p
        out.append(("# " if is_heading else "") + line)
    return "\n\n".join(out)


def load(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        return read_docx(path)
    return path.read_text(encoding="utf8", errors="ignore")


# ----------------------------------------------------------------------------
# Segmentation
# ----------------------------------------------------------------------------

HEADING_RE = re.compile(r"^\s{0,3}(#{1,6}\s+|\*\*[^*]+\*\*\s*$|[A-Z][A-Za-z &/-]{2,60}$)")
CAPTION_RE = re.compile(
    r"^\s*(\*\*)?(Fig\.?|Figure|Table|Supplementary (Fig\.?|Figure|Table)|Extended Data (Fig\.?|Figure|Table)|Panel|Box)"
    r"\s*S?\d+[a-zA-Z]?\s*(\*\*)?\s*[.:|]", re.I)
TABLE_ROW_RE = re.compile(r"^\s*\|")
REF_START_RE = re.compile(r"^\s*(#+\s*)?(references|bibliography)\s*$", re.I)
NUMBERED_REF_RE = re.compile(r"^\s*(\[\d+\]|\d+\.)\s+[A-Z][a-z]+ [A-Z]{1,3}[, ]")


def classify_lines(text: str):
    """Return a list of (line_no, kind, text). kind in heading, caption, table, ref, blank, prose."""
    lines = text.splitlines()
    kinds = []
    in_refs = False
    for i, raw in enumerate(lines, start=1):
        line = raw.rstrip()
        if not line.strip():
            kinds.append((i, "blank", line))
            continue
        if line.lstrip().startswith("<!--") or re.match(r"^\s*(Target|Journal|Keywords|Running head|Word count)\s*:", line, re.I):
            kinds.append((i, "meta", line))
            continue
        if REF_START_RE.match(line):
            in_refs = True
            kinds.append((i, "heading", line))
            continue
        if in_refs:
            # leave references if a new top-level heading appears that is not a reference entry
            if line.startswith("#") and not REF_START_RE.match(line):
                in_refs = False
                kinds.append((i, "heading", line))
                continue
            kinds.append((i, "ref", line))
            continue
        if TABLE_ROW_RE.match(line):
            kinds.append((i, "table", line))
        elif CAPTION_RE.match(line):
            kinds.append((i, "caption", line))
        elif line.startswith("#") or (len(line) < 80 and HEADING_RE.match(line) and not line.endswith(".")):
            kinds.append((i, "heading", line))
        elif NUMBERED_REF_RE.match(line):
            kinds.append((i, "ref", line))
        else:
            kinds.append((i, "prose", line))
    return kinds


def paragraphs(kinds):
    """Group consecutive prose lines into paragraphs: list of (start_line, text)."""
    paras = []
    buf = []
    start = None
    for ln, kind, text in kinds:
        if kind == "prose":
            if not buf:
                start = ln
            buf.append(text.strip())
        else:
            if buf:
                paras.append((start, " ".join(buf)))
                buf = []
    if buf:
        paras.append((start, " ".join(buf)))
    return paras


ABBREV_PROTECT = ["e.g.", "i.e.", "et al.", "vs.", "Fig.", "Figs.", "Dr.", "Prof.", "No.", "approx.", "ref.", "cf.", "Suppl."]


def split_sentences(para: str):
    t = para
    for a in ABBREV_PROTECT:
        t = t.replace(a, a.replace(".", "<DOT>"))
    # protect decimals
    t = re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", t)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(\[\"'*])", t)
    return [p.replace("<DOT>", ".").strip() for p in parts if p.strip()]


def word_count(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'%.\-]*", s))


# ----------------------------------------------------------------------------
# Checks
# ----------------------------------------------------------------------------


def check_lengths(paras, args, findings):
    for start, text in paras:
        wc = word_count(text)
        sents = split_sentences(text)
        if wc > args.max_paragraph:
            findings["paragraph_long"].append((start, f"{wc} words, {len(sents)} sentences"))
        elif wc < args.min_paragraph and len(sents) >= 2:
            findings["paragraph_short"].append((start, f"{wc} words"))
        for s in sents:
            swc = word_count(s)
            if swc > args.max_sentence:
                findings["sentence_long"].append((start, f"{swc} words: {s[:90]}..."))
            elif swc < args.min_sentence and swc >= 1 and not re.match(r"^(In conclusion|Figure|Table)", s):
                findings["sentence_short"].append((start, f"{swc} words: {s}"))


def check_punctuation(kinds, findings):
    for ln, kind, text in kinds:
        if "\u2014" in text or "\u2013" in text:
            findings["dash"].append((ln, text.strip()[:100]))
        if re.search(r"\s-\s", text):
            findings["spaced_hyphen"].append((ln, text.strip()[:100]))
        if kind != "prose":
            continue
        # colon: ignore times, ratios, URLs, "95% CI:" style in parentheses is still flagged
        stripped = re.sub(r"https?://\S+", "", text)
        stripped = re.sub(r"\b\d{1,2}:\d{2}\b", "", stripped)
        stripped = re.sub(r"\b\d+:\d+\b", "", stripped)
        if ":" in stripped:
            findings["colon"].append((ln, text.strip()[:100]))
        if ";" in text:
            findings["semicolon"].append((ln, text.strip()[:100]))
        # nested brackets
        if re.search(r"\([^()]*[\[(][^()\]]*[\])][^()]*\)", text):
            findings["nested_brackets"].append((ln, text.strip()[:100]))


def check_words(kinds, findings):
    for ln, kind, text in kinds:
        if kind in ("ref", "table"):
            continue
        low = text.lower()
        for w in BANNED:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                findings["banned"].append((ln, f"'{w}': {text.strip()[:90]}"))
        for w in CAUTION:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                findings["caution"].append((ln, f"'{w}': {text.strip()[:90]}"))
        for w in DRAFT_NOTES:
            if w in low:
                findings["draft_note"].append((ln, f"'{w}': {text.strip()[:90]}"))
        if re.search(r"\b(don't|can't|won't|isn't|aren't|didn't|doesn't|it's|we're|they're)\b", low):
            findings["contraction"].append((ln, text.strip()[:90]))


def check_significant(paras, findings):
    for start, text in paras:
        for s in split_sentences(text):
            if re.search(r"\bsignificant(ly)?\b", s, re.I) and not re.search(r"\bnot\s+significant", s, re.I):
                if not re.search(r"(\bp\s*[<=>]|\bP\s*[<=>]|\bCI\b|confidence interval|95%)", s):
                    findings["significant_no_stat"].append((start, s[:110]))


ABBR_TOKEN = re.compile(r"\b[A-Z][A-Z0-9]{1,7}s?\b")
DEF_RE = re.compile(r"\(([A-Z][A-Za-z0-9\-]{0,8}[A-Z0-9])s?\)")


def expansion_before(text: str, end: int, abbr: str) -> str:
    """Return the words immediately before position `end` that plausibly expand `abbr`."""
    before = text[:end].rstrip()
    words = re.findall(r"[A-Za-z][A-Za-z\-]*", before)
    if not words:
        return ""
    n_caps = max(1, min(8, sum(1 for c in abbr if c.isupper() or c.isdigit())))
    # try windows from n_caps up to n_caps+2 words and pick the one whose initials match best
    best, best_score = words[-n_caps:], -1
    target = abbr.upper()
    for k in range(max(1, n_caps - 1), min(len(words), n_caps + 3) + 1):
        window = words[-k:]
        initials = "".join(w[0].upper() for w in window)
        score = sum(1 for c in target if c in initials)
        if score > best_score or (score == best_score and k == n_caps):
            best, best_score = window, score
    return " ".join(best)


def check_abbreviations(kinds, allow, findings):
    prose_lines = [(ln, t) for ln, k, t in kinds if k in ("prose", "caption", "heading")]
    defs = defaultdict(list)  # abbr -> [(line, expansion)]
    uses = defaultdict(list)  # abbr -> [lines]
    # find the abstract region to allow a second definition in the main text
    abstract_end = None
    seen_abstract = False
    for ln, k, t in kinds:
        if k == "heading" and re.search(r"abstract|summary", t, re.I):
            seen_abstract = True
            continue
        if seen_abstract and k == "heading" and not re.search(r"background|methods|results|conclusion|objective|findings|interpretation|funding|materials|discussion", t, re.I):
            abstract_end = ln
            break
    for ln, t in prose_lines:
        for m in DEF_RE.finditer(t):
            ab = m.group(1)
            if ab.upper() in allow or len(ab) < 2:
                continue
            exp = expansion_before(t, m.start(), ab)
            if not exp:
                continue
            # a definition needs at least one initial in common, or a multi-word expansion
            initials = "".join(w[0] for w in exp.split()).upper()
            if any(c in initials for c in ab.upper()) or len(exp.split()) >= 2:
                defs[ab].append((ln, exp))
        for m in ABBR_TOKEN.finditer(t):
            tok = m.group(0)
            base = tok.rstrip("s") if tok.endswith("s") and len(tok) > 2 else tok
            if base in allow or base.upper() in allow or re.fullmatch(r"[IVX]+", base):
                continue
            if len(base) < 2:
                continue
            uses[base].append(ln)

    for ab, dlist in defs.items():
        first_def = dlist[0][0]
        use_lines = [u for u in uses.get(ab, []) if u != first_def]
        # defined twice: allowed once in abstract and once in main text
        main_defs = [d for d in dlist if abstract_end is None or d[0] >= abstract_end]
        if len(main_defs) > 1:
            findings["abbr_redefined"].append((main_defs[1][0], f"{ab} defined again (first at line {main_defs[0][0]})"))
        later_uses = [u for u in use_lines if u > first_def]
        if len(later_uses) < 3:
            findings["abbr_rarely_used"].append((first_def, f"{ab} defined but used {len(later_uses)} more time(s)"))
        before = [u for u in use_lines if u < first_def]
        if before:
            findings["abbr_used_before_def"].append((before[0], f"{ab} used before definition at line {first_def}"))
        expansions = {d[1].lower() for d in dlist}
        if len(expansions) > 1:
            findings["abbr_expansion_varies"].append((first_def, f"{ab}: {sorted(expansions)}"))
    for ab, ulines in uses.items():
        if ab not in defs and len(ulines) >= 1 and len(ab) >= 2 and not ab.isdigit():
            # skip model-name-like tokens with digits only if short
            findings["abbr_undefined"].append((ulines[0], f"{ab} used {len(ulines)} time(s), never defined"))
    # competing terms
    full = "\n".join(t for _, t in prose_lines)
    for a, b in COMPETING_TERMS:
        if re.search(r"\b" + re.escape(a) + r"\b", full) and re.search(r"\b" + re.escape(b) + r"\b", full, re.I):
            ca = len(re.findall(r"\b" + re.escape(a) + r"\b", full))
            cb = len(re.findall(r"\b" + re.escape(b) + r"\b", full, re.I))
            if a == "CI" and cb <= 1:
                continue
            findings["competing_terms"].append((0, f"both '{a}' ({ca}) and '{b}' ({cb}) appear"))


def check_numbers(kinds, findings):
    prose = [(ln, t) for ln, k, t in kinds if k in ("prose", "caption")]
    full = "\n".join(t for _, t in prose)
    # CI styles
    styles = Counter()
    if re.search(r"\d\s+to\s+\d", full):
        styles["to"] += len(re.findall(r"\d\s+to\s+\d", full))
    if re.search(r"\d\s*[\u2013-]\s*\d", full):
        styles["hyphen"] += len(re.findall(r"\d\s*[\u2013-]\s*\d", full))
    if re.search(r"\[\s*\d[\d.]*,\s*\d", full):
        styles["bracket-comma"] += len(re.findall(r"\[\s*\d[\d.]*,\s*\d", full))
    if re.search(r"\(\s*\d[\d.]*,\s*\d[\d.]*\)", full):
        styles["paren-comma"] += len(re.findall(r"\(\s*\d[\d.]*,\s*\d[\d.]*\)", full))
    if len([k for k, v in styles.items() if v > 0]) > 1:
        findings["ci_style_mixed"].append((0, f"range styles: {dict(styles)} (use 'lower to upper')"))
    # percentage precision
    pcts = re.findall(r"(\d+(?:\.\d+)?)\s?%(?!\s*(CI|confidence))", full)
    decimals = Counter(len(p.split(".")[1]) if "." in p else 0 for p in pcts)
    if len(decimals) > 1 and sum(decimals.values()) >= 4:
        findings["pct_precision_mixed"].append((0, f"percentages with decimals {dict(decimals)}"))
    # p-value style
    pstyles = Counter()
    for m in re.finditer(r"\b([pP])\s*([<=>])\s*(0?\.\d+)", full):
        pstyles[m.group(1)] += 1
        dec = len(m.group(3).split(".")[1])
        pstyles[f"dec{dec}"] += 1
    if pstyles.get("p", 0) and pstyles.get("P", 0):
        findings["p_case_mixed"].append((0, f"both 'p' ({pstyles['p']}) and 'P' ({pstyles['P']})"))
    decs = {k: v for k, v in pstyles.items() if k.startswith("dec")}
    if len(decs) > 2:
        findings["p_precision_mixed"].append((0, f"p-value decimals {decs}"))
    if re.search(r"\bp\s*[<=]\s*0?\.0+1\b", full) and re.search(r"\bp\s*[<=]\s*0?\.0001\b", full):
        findings["p_precision_mixed"].append((0, "both p<0.001 and p<0.0001 used"))
    # thousands separators
    with_sep = re.findall(r"\b\d{1,3}(?:,\d{3})+\b", full)
    without = [n for n in re.findall(r"\b\d{5,}\b", full) if not re.match(r"(19|20)\d{2}", n)]
    if with_sep and without:
        findings["thousands_mixed"].append((0, f"with separator: {with_sep[:3]}; without: {without[:3]}"))
    # ± without definition hint
    if "±" in full or "+/-" in full:
        if not re.search(r"(standard deviation|\bSD\b|standard error|\bSE\b)", full):
            findings["pm_undefined"].append((0, "'±' used but SD/SE never named"))
    # proportions vs percentages for the same quantity hint
    if re.search(r"\b0\.\d{3}\b", full) and re.search(r"\d\.\d%", full):
        if re.search(r"\b(accuracy|AUROC|AUC|F1)\b", full):
            findings["proportion_pct_mixed"].append((0, "both 0.xxx proportions and x.x% percentages appear; check the same metric is not given both ways"))
    # repeated percentages that differ slightly (e.g. 83.0 vs 83.07)
    vals = defaultdict(set)
    for p in pcts:
        if "." in p:
            vals[p.split(".")[0]].add(p)
    for base, s in vals.items():
        if len(s) > 1 and any(len(x.split(".")[1]) != len(y.split(".")[1]) for x in s for y in s):
            findings["pct_variants"].append((0, f"{sorted(s)}% (same value at different precision?)"))
    # 'significant' numbers without CI anywhere
    if not re.search(r"(95%\s*CI|confidence interval)", full) and re.search(r"\b(accuracy|AUROC|AUC|hazard ratio|odds ratio|sensitivity)\b", full, re.I):
        findings["no_ci_anywhere"].append((0, "performance metrics reported but no '95% CI' found in the text"))


FIG_RE = re.compile(r"\b(Fig\.?|Figure|Figs\.?|Figures)\s*(\d+)([a-zA-Z])?", re.I)
TAB_RE = re.compile(r"\bTable\s*(\d+)", re.I)
SUPP_RE = re.compile(r"\b(Supplementary|Extended Data)\s+(Fig\.?|Figure|Table|Figs\.?|Figures|Tables|Note)s?\s*(S?\d+)", re.I)


def check_display_items(kinds, findings):
    first_cite = {}
    captioned_figs, captioned_tabs = set(), set()
    positional = re.compile(r"\b(left|right|top|bottom|middle|upper|lower)\s+(panel|half|plot)|\(\s*(left|right|top|bottom|middle)\s*\)", re.I)
    order = []
    for ln, kind, text in kinds:
        if kind == "caption":
            m = re.match(r"\s*(\*\*)?(Fig\.?|Figure)\s*(\d+)", text, re.I)
            if m:
                captioned_figs.add(int(m.group(3)))
            m = re.match(r"\s*(\*\*)?Table\s*(\d+)", text, re.I)
            if m:
                captioned_tabs.add(int(m.group(2)))
            continue
        if kind != "prose":
            continue
        for m in FIG_RE.finditer(text):
            n = int(m.group(2))
            if ("F", n) not in first_cite:
                first_cite[("F", n)] = ln
                order.append(("Figure", n, ln))
        for m in TAB_RE.finditer(text):
            n = int(m.group(1))
            if ("T", n) not in first_cite:
                first_cite[("T", n)] = ln
                order.append(("Table", n, ln))
        if positional.search(text) and FIG_RE.search(text):
            findings["positional_panel"].append((ln, text.strip()[:100]))
    for label in ("Figure", "Table"):
        seq = [(n, ln) for lab, n, ln in order if lab == label]
        for i in range(1, len(seq)):
            if seq[i][0] < max(s[0] for s in seq[:i]):
                findings["citation_order"].append((seq[i][1], f"{label} {seq[i][0]} first cited after {label} {max(s[0] for s in seq[:i])}"))
        nums = {n for n, _ in seq}
        if nums:
            for k in range(1, max(nums) + 1):
                if k not in nums:
                    findings["uncited_item"].append((0, f"{label} {k} never cited in prose"))
    for f in captioned_figs:
        if ("F", f) not in first_cite:
            findings["uncited_item"].append((0, f"Figure {f} has a caption but no citation"))
    for t in captioned_tabs:
        if ("T", t) not in first_cite:
            findings["uncited_item"].append((0, f"Table {t} has a caption but no citation"))
    # supplementary pointers without numbers
    for ln, kind, text in kinds:
        if kind == "prose" and re.search(r"\bsupplementary (material|information|data|file)s?\b", text, re.I) and not SUPP_RE.search(text) and not re.search(r"section\s+\d", text, re.I):
            findings["supp_pointer_vague"].append((ln, text.strip()[:100]))


def check_sections(kinds, journal, findings):
    headings = [t.lower().lstrip("# ").strip("* ") for _, k, t in kinds if k == "heading"]
    joined = "\n".join(headings)
    wanted = SECTION_PROFILES.get(journal, SECTION_PROFILES["default"])
    for w in wanted:
        if w not in joined:
            findings["section_missing"].append((0, f"'{w}' heading not found (profile: {journal})"))
    if not re.search(r"limitation", "\n".join(t for _, k, t in kinds if k == "prose"), re.I):
        findings["section_missing"].append((0, "no sentence mentions limitations"))
    prose = "\n".join(t for _, k, t in kinds if k == "prose")
    if not re.search(r"\b(TRIPOD|STARD|PRISMA|CONSORT|STROBE|CLAIM|CHEERS|SPIRIT|DECIDE-AI|MI-CLAIM|CLEAR)\b", prose):
        findings["section_missing"].append((0, "no reporting guideline named (TRIPOD, STARD, PRISMA, ...)"))
    if not re.search(r"\b(ethic|institutional review board|IRB|Helsinki|consent)\b", prose, re.I):
        findings["section_missing"].append((0, "no ethics or consent statement found"))


def check_spelling_variant(kinds, findings):
    prose = "\n".join(t for _, k, t in kinds if k == "prose")
    ise = len(re.findall(r"\b\w+is(e|ed|ing|ation)\b", prose))
    ize = len(re.findall(r"\b\w+iz(e|ed|ing|ation)\b", prose))
    if ise >= 3 and ize >= 3:
        findings["spelling_mixed"].append((0, f"-ise forms: {ise}, -ize forms: {ize}"))
    us = len(re.findall(r"\b(color|center|analyze|modeling|labeled|behavior)\b", prose))
    uk = len(re.findall(r"\b(colour|centre|analyse|modelling|labelled|behaviour)\b", prose))
    if us and uk:
        findings["spelling_mixed"].append((0, f"US forms: {us}, UK forms: {uk}"))


def check_consistency(kinds, findings):
    prose = [(ln, t) for ln, k, t in kinds if k == "prose"]
    # duplicated sentences
    seen = {}
    for ln, t in prose:
        for s in split_sentences(t):
            key = re.sub(r"\W+", " ", s.lower()).strip()
            if len(key) > 40:
                if key in seen:
                    findings["duplicate_sentence"].append((ln, f"same as line {seen[key]}: {s[:80]}"))
                else:
                    seen[key] = ln
    # "N items" followed by a list hint: 'three X: a, b' handled loosely
    full = "\n".join(t for _, t in prose)
    for m in re.finditer(r"\b(two|three|four|five|six|seven|eight|nine|\d+)\s+((?:\w+\s+){0,2}\w+)\s*\(([^)]{10,200})\)", full):
        words = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        n = words.get(m.group(1).lower()) or (int(m.group(1)) if m.group(1).isdigit() else None)
        items = [x for x in re.split(r",\s*|\s+and\s+", m.group(3)) if x.strip()]
        if n and 2 <= n <= 9 and len(items) >= 2 and len(items) != n and abs(len(items) - n) == 1:
            findings["count_list_mismatch"].append((0, f"'{m.group(1)} {m.group(2)}' followed by {len(items)} items: {m.group(3)[:60]}"))


# ----------------------------------------------------------------------------
# Report
# ----------------------------------------------------------------------------

LABELS = {
    "sentence_long": ("Sentences over the limit", "high"),
    "sentence_short": ("Sentences under the minimum", "low"),
    "paragraph_long": ("Paragraphs over the limit", "medium"),
    "paragraph_short": ("Paragraphs under the minimum", "low"),
    "colon": ("Colons in prose", "high"),
    "semicolon": ("Semicolons in prose", "high"),
    "dash": ("Em or en dashes", "high"),
    "spaced_hyphen": ("Spaced hyphens used as dashes", "medium"),
    "nested_brackets": ("Nested brackets", "medium"),
    "banned": ("Banned words", "high"),
    "caution": ("Caution words (justify or cut)", "low"),
    "draft_note": ("Leftover drafting notes or placeholders", "high"),
    "contraction": ("Contractions", "medium"),
    "significant_no_stat": ("'significant' without p value or CI in the sentence", "high"),
    "abbr_used_before_def": ("Abbreviation used before definition", "high"),
    "abbr_rarely_used": ("Abbreviation defined but used fewer than 3 more times", "medium"),
    "abbr_redefined": ("Abbreviation defined again in the main text", "medium"),
    "abbr_undefined": ("Abbreviation never defined", "medium"),
    "abbr_expansion_varies": ("Abbreviation expanded in different ways", "high"),
    "competing_terms": ("Two terms for one concept", "medium"),
    "ci_style_mixed": ("Mixed range or CI styles", "medium"),
    "pct_precision_mixed": ("Mixed percentage precision", "medium"),
    "p_case_mixed": ("Mixed 'p' and 'P'", "low"),
    "p_precision_mixed": ("Mixed p-value precision", "low"),
    "thousands_mixed": ("Mixed thousands separators", "low"),
    "pm_undefined": ("'±' without SD or SE named", "medium"),
    "proportion_pct_mixed": ("Proportions and percentages both used", "low"),
    "pct_variants": ("Same percentage at different precision", "medium"),
    "no_ci_anywhere": ("No confidence intervals in the text", "high"),
    "positional_panel": ("Positional panel references (left, right, top)", "medium"),
    "citation_order": ("Display items cited out of order", "medium"),
    "uncited_item": ("Display items never cited or without a caption", "medium"),
    "supp_pointer_vague": ("Vague supplementary pointers", "low"),
    "section_missing": ("Expected sections or statements missing", "medium"),
    "spelling_mixed": ("Mixed spelling variants", "low"),
    "duplicate_sentence": ("Duplicated sentences", "high"),
    "count_list_mismatch": ("Stated count does not match listed items", "medium"),
}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--journal", default="default", help="default, npj, jamia, nature, lancet, ehj")
    ap.add_argument("--max-sentence", type=int, default=40)
    ap.add_argument("--min-sentence", type=int, default=8)
    ap.add_argument("--max-paragraph", type=int, default=150)
    ap.add_argument("--min-paragraph", type=int, default=80)
    ap.add_argument("--allow", default="", help="comma-separated abbreviations that need no definition")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of Markdown")
    args = ap.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)
    text = load(path)
    journal = args.journal.lower()
    if journal in ("npj digital medicine", "npj dm"):
        journal = "npj"
    if journal.startswith("lancet"):
        journal = "lancet"
    if journal.startswith("nature"):
        journal = "nature"
    allow = set(DEFAULT_ALLOW) | {a.strip().upper() for a in args.allow.split(",") if a.strip()}

    kinds = classify_lines(text)
    paras = paragraphs(kinds)
    findings = defaultdict(list)

    check_lengths(paras, args, findings)
    check_punctuation(kinds, findings)
    check_words(kinds, findings)
    check_significant(paras, findings)
    check_abbreviations(kinds, allow, findings)
    check_numbers(kinds, findings)
    check_display_items(kinds, findings)
    check_sections(kinds, journal, findings)
    check_spelling_variant(kinds, findings)
    check_consistency(kinds, findings)

    total_words = sum(word_count(t) for _, t in paras)
    all_sents = [s for _, t in paras for s in split_sentences(t)]
    lens = sorted(word_count(s) for s in all_sents) or [0]
    median = lens[len(lens) // 2]

    if args.json:
        print(json.dumps({k: v for k, v in findings.items()}, indent=1))
        return

    out = []
    out.append(f"# Manuscript check: {path.name}")
    out.append("")
    out.append(f"Journal profile: {journal}. Prose words: {total_words}. Sentences: {len(all_sents)}. "
               f"Median sentence length: {median} words. Paragraphs: {len(paras)}.")
    out.append("")
    sev_order = {"high": 0, "medium": 1, "low": 2}
    keys = sorted(findings.keys(), key=lambda k: (sev_order[LABELS.get(k, ("", "low"))[1]], k))
    if not keys:
        out.append("No issues flagged by the automated checks. Run the manual checklist next.")
    counts = Counter(LABELS.get(k, ("", "low"))[1] for k in keys for _ in findings[k])
    out.append(f"Flags: {counts.get('high', 0)} high, {counts.get('medium', 0)} medium, {counts.get('low', 0)} low.")
    out.append("")
    for k in keys:
        label, sev = LABELS.get(k, (k, "low"))
        items = findings[k]
        out.append(f"## [{sev}] {label} ({len(items)})")
        shown = items[:25]
        for ln, msg in shown:
            loc = f"line {ln}: " if ln else ""
            out.append(f"- {loc}{msg}")
        if len(items) > len(shown):
            out.append(f"- ... and {len(items) - len(shown)} more")
        out.append("")
    out.append("Heuristics only. Colons inside captions, structured-abstract headings and ratios are acceptable; "
               "abbreviation detection cannot see tables or figures; counts are approximate.")
    print("\n".join(out))


if __name__ == "__main__":
    main()
