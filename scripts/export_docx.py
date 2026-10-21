#!/usr/bin/env python3
"""Export a SciFi manuscript to a .docx whose citations become live Zotero fields.

Usage:
    python3 export_docx.py --workspace <ws> --out <file.docx> [--sections title,abstract,...]
                           [--library users/12345 | groups/6789] [--keys <library.bbt.json>]
                           [--report <report.json>]

Reads Manuscript/*.md (pandoc citations such as [@smith2024; @lee2023, p. 12]) and writes a
Word file in which every citation is a Scannable Cite marker:

    {prefix|Surname, (Year)|locator|suffix|http://zotero.org/users/USERID/items/ITEMKEY}

Zotero's ODF/DOCX Scan (Tools menu, from the Juris-M add-on) turns the markers into real
citation fields. After "Switch to a Different Word Processor" in Word, the file can be
uploaded to Google Docs and refreshed there. The steps are in docs/zotero-guide.md.

Where the Zotero item key comes from, in order:
  1. --keys <file>: a Better BibTeX JSON export (it carries itemKey, libraryID and uri per item)
     or any JSON list of {citekey, itemKey, uri} objects. Default: Literature/library.bbt.json.
  2. Literature/library.json entries with an "itemKey" or "zotero-key" field.
If no key is found for a citation the marker is not written; the citation stays as plain
text [@key] and is listed in the report. The script never guesses a key.

The URI is taken from the keys file's "uri" when it is a zotero.org URI, otherwise built from
--library (users/<id> or groups/<id>) and the item key. Local-only libraries
(uri containing /users/local/) need --library with the synced user id.

Exit codes: 0 all citations mapped, 2 some citations unmapped (file still written), 1 usage.
Stdlib only. The docx is minimal (headings, paragraphs, bold, italic, page break).
"""
import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

SECTION_ORDER = ["title", "abstract", "introduction", "methods", "results", "discussion"]
HEADING_FOR = {"abstract": "Abstract", "introduction": "Introduction", "methods": "Methods",
               "results": "Results", "discussion": "Discussion"}
CITE_RE = re.compile(r"\[([^\[\]]*@[^\[\]]*)\]")
BARE_RE = re.compile(r"(?<![\w@])@([A-Za-z0-9_:.\-]+)")
LOCATOR_RE = re.compile(r"^\s*(p{1,2}\.?|pages?|chap(?:ter)?\.?|sec(?:tion)?\.?|fig(?:ure)?\.?|table)\s*([\w\-–,. ]+)$", re.I)


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf8"))
    except FileNotFoundError:
        return None


def label_for(entry):
    """'Surname, (Year)' from a CSL JSON entry."""
    authors = entry.get("author") or entry.get("editor") or []
    if authors:
        a = authors[0]
        surname = a.get("family") or a.get("literal") or "Anon"
    else:
        surname = "Anon"
    year = "n.d."
    issued = entry.get("issued", {})
    parts = issued.get("date-parts") if isinstance(issued, dict) else None
    if parts and parts[0]:
        year = str(parts[0][0])
    elif isinstance(issued, dict) and issued.get("raw"):
        year = str(issued["raw"])[:4]
    return f"{surname}, ({year})"


def build_key_map(keys_path, library_json, library_arg):
    """citekey -> (itemKey, uri)"""
    out = {}
    data = load_json(keys_path) if keys_path else None
    items = []
    if isinstance(data, dict) and "items" in data:
        items = data["items"]          # Better BibTeX JSON
    elif isinstance(data, list):
        items = data
    for it in items:
        ck = it.get("citekey") or it.get("citationKey") or it.get("id")
        key = it.get("itemKey") or it.get("key")
        uri = it.get("uri", "")
        if ck and key:
            out[ck] = (key, uri)
    for e in library_json or []:
        ck = e.get("id") or e.get("citation-key")
        key = e.get("itemKey") or e.get("zotero-key")
        if ck and key and ck not in out:
            out[ck] = (key, e.get("uri", ""))
    # resolve uris
    resolved = {}
    for ck, (key, uri) in out.items():
        good = uri if (uri.startswith("http://zotero.org/") and "/users/local/" not in uri) else ""
        if not good and library_arg:
            good = f"http://zotero.org/{library_arg.strip('/')}/items/{key}"
        resolved[ck] = (key, good)
    return resolved


def parse_citation(inner):
    """Split a pandoc citation body into items: [(prefix, key, locator, suffix)]."""
    items = []
    for part in inner.split(";"):
        part = part.strip()
        m = re.search(r"@([A-Za-z0-9_:.\-]+)", part)
        if not m:
            continue
        key = m.group(1).rstrip(".")
        prefix = part[:m.start()].strip()
        rest = part[m.end():].strip().lstrip(",").strip()
        locator, suffix = "", ""
        if rest:
            lm = LOCATOR_RE.match(rest)
            if lm:
                locator = rest
            else:
                suffix = rest
        items.append((prefix, key, locator, suffix))
    return items


def markers_for(items, keymap, labels, missing):
    """Return a single-run string of adjacent markers, or None if any key is unmapped."""
    out = []
    for prefix, key, locator, suffix in items:
        km = keymap.get(key)
        if not km or not km[1]:
            missing.add(key)
            return None
        label = labels.get(key, key)
        out.append("{" + "|".join([prefix, label, locator, suffix, km[1]]) + "}")
    return "".join(out)


# ---------------------------------------------------------------- docx writing

def run(text, bold=False, italic=False):
    props = ""
    if bold or italic:
        props = "<w:rPr>" + ("<w:b/>" if bold else "") + ("<w:i/>" if italic else "") + "</w:rPr>"
    return f'<w:r>{props}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


INLINE_RE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")


def inline_runs(text):
    runs = []
    for seg in INLINE_RE.split(text):
        if not seg:
            continue
        if seg.startswith("**"):
            runs.append(run(seg[2:-2], bold=True))
        elif seg.startswith("*"):
            runs.append(run(seg[1:-1], italic=True))
        elif seg.startswith("`"):
            runs.append(run(seg[1:-1]))
        else:
            runs.append(run(seg))
    return "".join(runs)


def paragraph(runs_xml, style=None):
    ppr = f"<w:pPr><w:pStyle w:val=\"{style}\"/></w:pPr>" if style else ""
    return f"<w:p>{ppr}{runs_xml}</w:p>"


def page_break():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def convert_paragraph(text, keymap, labels, missing, stats):
    """Markdown paragraph -> runs; citations become single-run markers."""
    pieces = []
    pos = 0
    for m in CITE_RE.finditer(text):
        pieces.append(("text", text[pos:m.start()]))
        items = parse_citation(m.group(1))
        if items:
            marker = markers_for(items, keymap, labels, missing)
            if marker is None:
                pieces.append(("raw", m.group(0)))
                stats["unmapped"] += 1
            else:
                pieces.append(("marker", marker))
                stats["citations"] += 1
                stats["items"] += len(items)
        else:
            pieces.append(("text", m.group(0)))
        pos = m.end()
    pieces.append(("text", text[pos:]))
    xml = []
    for kind, s in pieces:
        if kind in ("marker", "raw"):
            xml.append(run(s))
        else:
            # bare @key outside brackets
            idx = 0
            for bm in BARE_RE.finditer(s):
                xml.append(inline_runs(s[idx:bm.start()]))
                key = bm.group(1).rstrip(".")
                marker = markers_for([("", key, "", "")], keymap, labels, missing)
                if marker is None:
                    xml.append(run(bm.group(0)))
                    stats["unmapped"] += 1
                else:
                    xml.append(run(marker))
                    stats["citations"] += 1
                    stats["items"] += 1
                idx = bm.end()
            xml.append(inline_runs(s[idx:]))
    return "".join(xml)


def md_to_body(md, keymap, labels, missing, stats, section):
    body = []
    blocks = re.split(r"\n\s*\n", md.strip())
    for block in blocks:
        b = block.strip()
        if not b or b.startswith("<!--") or re.match(r"^\s*(Target|Journal|Running head)\s*:", b, re.I):
            continue
        hm = re.match(r"^(#{1,3})\s+(.*)$", b)
        if hm and "\n" not in b:
            level = len(hm.group(1))
            title = hm.group(2).strip()
            if section == "title" and level == 1:
                body.append(paragraph(run(title), "Title"))
            else:
                body.append(paragraph(run(title), f"Heading{min(level + 1, 3)}"))
            continue
        if b.startswith("|"):
            # tables are flattened to paragraphs; markers in tables do not scan
            for line in b.splitlines():
                if re.match(r"^\|\s*-", line):
                    continue
                cells = [c.strip() for c in line.strip("|").split("|")]
                body.append(paragraph(inline_runs("   ".join(cells)), "TableText"))
            stats["table_blocks"] += 1
            continue
        text = " ".join(l.strip() for l in b.splitlines())
        body.append(paragraph(convert_paragraph(text, keymap, labels, missing, stats)))
    return body


STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="160" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="32"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="360"/></w:pPr><w:rPr><w:b/><w:sz w:val="28"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:before="240"/></w:pPr><w:rPr><w:b/><w:sz w:val="24"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/></w:pPr><w:rPr><w:b/><w:i/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Note"><w:name w:val="Note"/><w:basedOn w:val="Normal"/><w:rPr><w:i/><w:color w:val="7A4B00"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="TableText"><w:name w:val="Table text"/><w:basedOn w:val="Normal"/><w:rPr><w:sz w:val="18"/></w:rPr></w:style>
</w:styles>"""

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""


def write_docx(path, body_xml):
    doc = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
           f'<w:body>{body_xml}<w:sectPr/></w:body></w:document>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/document.xml", doc)
        z.writestr("word/styles.xml", STYLES)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workspace", default=".")
    ap.add_argument("--out", required=True)
    ap.add_argument("--sections", default=",".join(SECTION_ORDER))
    ap.add_argument("--library", default="", help="users/<id> or groups/<id> for building URIs")
    ap.add_argument("--keys", default="", help="Better BibTeX JSON export (default Literature/library.bbt.json)")
    ap.add_argument("--report", default="")
    args = ap.parse_args()

    ws = Path(args.workspace)
    lib = load_json(ws / "Literature" / "library.json") or []
    labels = {}
    for e in lib:
        ck = e.get("id") or e.get("citation-key")
        if ck:
            labels[ck] = label_for(e)
    keys_path = args.keys or str(ws / "Literature" / "library.bbt.json")
    keymap = build_key_map(keys_path, lib, args.library)
    if not keymap:
        print("No Zotero item keys found. Provide Literature/library.bbt.json (Better BibTeX JSON export) "
              "or --keys, and --library users/<id> or groups/<id>. See docs/zotero-guide.md.", file=sys.stderr)

    missing, stats = set(), {"citations": 0, "items": 0, "unmapped": 0, "table_blocks": 0}
    body = [paragraph(run("Note for the author: in Zotero run Tools, ODF/DOCX Scan on this file "
                          "(markers to citations), open the result in Word, press Refresh on the Zotero tab, "
                          "then delete this note."), "Note")]
    for sec in [s.strip() for s in args.sections.split(",") if s.strip()]:
        f = ws / "Manuscript" / f"{sec}.md"
        if not f.exists():
            continue
        md = f.read_text(encoding="utf8")
        if sec in HEADING_FOR and not re.search(r"^#\s", md, re.M):
            body.append(paragraph(run(HEADING_FOR[sec]), "Heading1"))
        body.extend(md_to_body(md, keymap, labels, missing, stats, sec))
    body.append(page_break())
    body.append(paragraph(run("References"), "Heading1"))
    body.append(paragraph(run("Place the cursor here and use the Zotero plugin to insert the bibliography after the scan."), "Note"))

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    write_docx(out, "".join(body))

    report = {"out": str(out), "citations_written": stats["citations"], "items_in_markers": stats["items"],
              "unmapped_citations": stats["unmapped"], "missing_keys": sorted(missing),
              "table_blocks_flattened": stats["table_blocks"], "keys_source": keys_path if keymap else None}
    if args.report:
        Path(args.report).write_text(json.dumps(report, indent=1), encoding="utf8")
    print(json.dumps(report, indent=1))
    if stats["table_blocks"]:
        print("Tables were flattened to paragraphs; citations inside tables must be inserted by hand in Word.", file=sys.stderr)
    sys.exit(2 if missing else 0)


if __name__ == "__main__":
    main()
