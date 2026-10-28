#!/usr/bin/env python3
"""Export a SciFi manuscript to a .docx whose citations become live Zotero fields.

Usage:
    python3 export_docx.py --workspace <ws> --out <file.docx> [--sections title,abstract,...]
                           [--library users/12345 | groups/6789] [--keys <library.bbt.json>]
                           [--report <report.json>] [--markers]
    python3 export_docx.py --convert <with-markers.docx> --out <file.docx> [--no-item-data]

Reads Manuscript/*.md (pandoc citations such as [@smith2024; @lee2023, p. 12]) and writes a
Word file in which every citation is already a live Zotero citation field, the same field the
Word plugin writes (ADDIN ZOTERO_ITEM CSL_CITATION with the item URI and, from
Literature/library.json, its CSL data). In Word the author picks a style in Document
Preferences, presses Refresh and inserts the bibliography. No Zotero add-on is needed.

--markers writes Scannable Cite markers instead, for Zotero's ODF/DOCX Scan:

    {prefix|Surname, (Year)|locator|suffix|http://zotero.org/users/USERID/items/ITEMKEY}

The scan pattern-matches raw XML and mistakes the {GUID} inside Word's picture markup for a
marker, so it corrupts any .docx with pictures. --convert does the same job safely on the text
of an existing .docx (for example one built elsewhere with markers): it reads w:t text only,
turns each marker group into a field, and asks Zotero desktop's local API for the item data
unless --no-item-data is given. Steps and the Google Docs handoff are in docs/zotero-guide.md.

Where the Zotero item key comes from, in order:
  1. --keys <file>: a Better BibTeX JSON export (it carries itemKey, libraryID and uri per item)
     or any JSON list of {citekey, itemKey, uri} objects. Default: Literature/library.bbt.json.
  2. Literature/library.json entries with an "itemKey" or "zotero-key" field.
If no key is found for a citation, no field or marker is written. The citation stays as plain
text [@key] and is listed in the report. The script never guesses a key.

The URI is taken from the keys file's "uri" when it is a zotero.org URI, otherwise built from
--library (users/<id> or groups/<id>) and the item key. Local-only libraries
(uri containing /users/local/) need --library with the synced user id.

An existing output file is never overwritten without --force, and the file is written to a
temporary name first and moved into place only when complete.

Exit codes: 0 all citations mapped, 2 some citations unmapped or markers left (file still
written), 1 usage error, missing input or a failed write. Stdlib only. The docx is minimal
(headings, paragraphs, bold, italic, page break).
"""
import argparse
import hashlib
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
import xml.dom.minidom
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

SECTION_ORDER = ["title", "abstract", "introduction", "methods", "results", "discussion"]
HEADING_FOR = {"abstract": "Abstract", "introduction": "Introduction", "methods": "Methods",
               "results": "Results", "discussion": "Discussion"}
CITE_RE = re.compile(r"\[([^\[\]]*@[^\[\]]*)\]")
BARE_RE = re.compile(r"(?<![\w@])@([A-Za-z0-9_:.\-]+)")
LOCATOR_RE = re.compile(r"^\s*(p{1,2}\.?|pages?|chap(?:ter)?\.?|sec(?:tion)?\.?|fig(?:ure)?\.?|table)\s*([\w\-\u2013,. ]+)$", re.I)
LOCATOR_LABEL = {"p": "page", "pp": "page", "page": "page", "pages": "page", "chap": "chapter",
                 "chapter": "chapter", "sec": "section", "section": "section", "fig": "figure",
                 "figure": "figure", "table": "table"}
SCHEMA = "https://github.com/citation-style-language/schema/raw/master/csl-citation.json"
MARKER_RE = re.compile(r"\{([^|{}]*)\|([^|{}]*)\|([^|{}]*)\|([^|{}]*)\|(http://zotero\.org/[^|{}]+)\}")
GROUP_RE = re.compile(r"(?:\{[^|{}]*\|[^|{}]*\|[^|{}]*\|[^|{}]*\|http://zotero\.org/[^|{}]+\})+")
T_RE = re.compile(r"<w:t(?:\s[^>]*)?>([^<]*)</w:t>")


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


def resolve(items, keymap, labels, missing):
    """[(prefix, key, locator, suffix)] -> [(prefix, label, locator, suffix, uri)], or None if any key is unmapped."""
    out = []
    for prefix, key, locator, suffix in items:
        km = keymap.get(key)
        if not km or not km[1]:
            missing.add(key)
            return None
        out.append((prefix, labels.get(key, key), locator, suffix, km[1]))
    return out


def marker_text(resolved):
    """Adjacent Scannable Cite markers, one string, for a single run."""
    return "".join("{" + "|".join(r) + "}" for r in resolved)


def public_csl(entry, uri):
    """CSL data safe to embed in a shared document: abstract and note (private Zotero extra) dropped."""
    return {k: v for k, v in dict(entry, id=uri).items() if k not in ("abstract", "note")}


def citation_field(resolved, item_data=None, rpr="", index=0):
    """Runs for one live Zotero citation, the field the Word plugin writes itself. Its visible
    text equals plainCitation, so Refresh replaces it without asking about manual edits."""
    plain = "(" + "; ".join(re.sub(r",\s*\(([^()]*)\)\s*$", r" \1", r[1].strip()) for r in resolved) + ")"
    items = []
    for prefix, _, locator, suffix, uri in resolved:
        ci = {"id": uri, "uris": [uri]}
        data = (item_data or {}).get(uri)
        if data:
            ci["itemData"] = public_csl(data, uri)
        lm = LOCATOR_RE.match(locator) if locator else None
        if lm:
            ci["label"] = LOCATOR_LABEL.get(lm.group(1).lower().rstrip("."), "page")
            ci["locator"] = lm.group(2).strip()
        elif locator:
            ci["locator"] = locator
        if prefix:
            ci["prefix"] = prefix
        if suffix:
            ci["suffix"] = suffix
        items.append(ci)
    seed = json.dumps([index, [[r[4], r[2]] for r in resolved]])  # same input, same bytes
    code = {"citationID": hashlib.sha1(seed.encode("utf8")).hexdigest()[:8],
            "properties": {"formattedCitation": plain, "plainCitation": plain, "noteIndex": 0},
            "citationItems": items, "schema": SCHEMA}
    instr = " ADDIN ZOTERO_ITEM CSL_CITATION " + json.dumps(code, ensure_ascii=False) + " "
    parts = ['<w:fldChar w:fldCharType="begin"/>', f'<w:instrText xml:space="preserve">{escape(instr)}</w:instrText>',
             '<w:fldChar w:fldCharType="separate"/>', f'<w:t xml:space="preserve">{escape(plain)}</w:t>',
             '<w:fldChar w:fldCharType="end"/>']
    return "".join(f"<w:r>{rpr}{p}</w:r>" for p in parts)


LOCAL_API = "http://127.0.0.1:23119/api"
_NO_PROXY = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # loopback only, never a proxy
_api_down = []


def zotero_item_data(uri):
    """CSL JSON for a zotero.org item URI from Zotero desktop's local API, or None. After the first
    connection failure the API is not asked again (Zotero closed, or local API not allowed)."""
    m = re.match(r"http://zotero\.org/(users|groups)/(\d+)/items/(\w+)$", uri)
    if not m or _api_down:
        return None
    libs = [f"{m.group(1)}/{m.group(2)}"] + (["users/0"] if m.group(1) == "users" else [])
    for lib in libs:
        try:
            with _NO_PROXY.open(f"{LOCAL_API}/{lib}/items/{m.group(3)}?format=csljson", timeout=10) as r:
                data = json.loads(r.read().decode("utf8"))
        except urllib.error.HTTPError:
            continue
        except OSError:
            _api_down.append(True)
            return None
        item = data[0] if isinstance(data, list) and data else (data.get("items") or [None])[0] if isinstance(data, dict) else None
        if item:
            return item
    return None


def run_properties(xml_text, open_end):
    """The w:rPr that starts at open_end, matched to its balanced end tag, without w:rPrChange
    (tracked-formatting history belongs to the original run, not to new field runs)."""
    if xml_text.startswith("<w:rPr/>", open_end):
        return "<w:rPr/>"
    if not xml_text.startswith("<w:rPr>", open_end) and not xml_text.startswith("<w:rPr ", open_end):
        return ""
    depth, pos = 0, open_end
    for t in re.finditer(r"<(/?)w:rPr(?=[\s>/])[^>]*?(/?)>", xml_text[open_end:]):
        if t.group(2):
            continue
        depth += -1 if t.group(1) else 1
        if depth == 0:
            pos = open_end + t.end()
            break
    return re.sub(r"<w:rPrChange\b.*?</w:rPrChange>", "", xml_text[open_end:pos], flags=re.S)


def convert_part(xml_text, data_for, stats):
    """Replace marker groups inside w:t text with fields. Markup is never matched, so the {GUID}
    attributes in picture XML stay intact. A run holding a marker is closed before the field and
    reopened after it with the same run properties."""
    def repl(m):
        text = html.unescape(m.group(1))
        if not GROUP_RE.search(text):
            return m.group(0)
        start = max(xml_text.rfind("<w:r>", 0, m.start()), xml_text.rfind("<w:r ", 0, m.start()))
        if start < 0:
            return m.group(0)  # no enclosing run: leave it, it is counted in markers_left
        rpr = run_properties(xml_text, xml_text.index(">", start) + 1)
        out, pos = [], 0
        for g in GROUP_RE.finditer(text):
            resolved = [mm.groups() for mm in MARKER_RE.finditer(g.group(0))]
            out.append(f'<w:t xml:space="preserve">{escape(text[pos:g.start()])}</w:t></w:r>')
            out.append(citation_field(resolved, {r[4]: data_for(r[4]) for r in resolved}, rpr, stats["citations"]))
            out.append(f"<w:r>{rpr}")
            stats["citations"] += 1
            stats["items"] += len(resolved)
            pos = g.end()
        out.append(f'<w:t xml:space="preserve">{escape(text[pos:])}</w:t>')
        return "".join(out)
    return T_RE.sub(repl, xml_text)


def convert_docx(src, out, item_data=True):
    """Turn the Scannable Cite markers of an existing .docx into live Zotero fields."""
    cache, stats = {}, {"citations": 0, "items": 0}

    def data_for(uri):
        if uri not in cache:
            cache[uri] = zotero_item_data(uri) if item_data else None
        return cache[uri]

    parts = ("word/document.xml", "word/footnotes.xml", "word/endnotes.xml")
    left = 0
    with zipfile.ZipFile(src) as zin:
        files = []
        for info in zin.infolist():
            data = zin.read(info.filename)
            if info.filename in parts:
                new = convert_part(data.decode("utf8"), data_for, stats)
                try:
                    xml.dom.minidom.parseString(new.encode("utf8"))
                except Exception as e:
                    raise SystemExit(f"{info.filename} would not be well-formed after conversion ({e}); nothing written")
                left += sum(len(GROUP_RE.findall(html.unescape(t))) for t in T_RE.findall(new))
                data = new.encode("utf8")
            files.append((info, data))
    write_zip(out, files)
    if item_data and cache and not any(cache.values()):
        print("No item data came from Zotero desktop. Is Zotero running, with Settings, Advanced, "
              "'Allow other applications on this computer to communicate with Zotero' ticked? "
              "The fields still work, Zotero resolves the URIs on Refresh.", file=sys.stderr)
    return {"out": str(out), "citations_written": stats["citations"], "items_in_fields": stats["items"],
            "item_data_embedded": sum(1 for v in cache.values() if v), "distinct_items": len(cache),
            "markers_left": left}


def write_zip(out, files):
    """Write [(name or ZipInfo, bytes)] to a temp file next to out, then move it into place."""
    tmp = Path(str(out) + ".tmp")
    try:
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
            for name, data in files:
                z.writestr(name, data)
        os.replace(tmp, out)
    finally:
        if tmp.exists():
            tmp.unlink()


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


def convert_paragraph(text, keymap, labels, missing, stats, render):
    """Markdown paragraph -> runs; each citation becomes render(resolved items), a field or a marker run."""
    pieces = []
    pos = 0
    for m in CITE_RE.finditer(text):
        pieces.append(("text", text[pos:m.start()]))
        items = parse_citation(m.group(1))
        if items:
            resolved = resolve(items, keymap, labels, missing)
            if resolved is None:
                pieces.append(("raw", m.group(0)))
                stats["unmapped"] += 1
            else:
                pieces.append(("cite", render(resolved)))
                stats["citations"] += 1
                stats["items"] += len(items)
        else:
            pieces.append(("text", m.group(0)))
        pos = m.end()
    pieces.append(("text", text[pos:]))
    xml = []
    for kind, s in pieces:
        if kind == "cite":
            xml.append(s)
        elif kind == "raw":
            xml.append(run(s))
        else:
            # bare @key outside brackets
            idx = 0
            for bm in BARE_RE.finditer(s):
                xml.append(inline_runs(s[idx:bm.start()]))
                key = bm.group(1).rstrip(".")
                resolved = resolve([("", key, "", "")], keymap, labels, missing)
                if resolved is None:
                    xml.append(run(bm.group(0)))
                    stats["unmapped"] += 1
                else:
                    xml.append(render(resolved))
                    stats["citations"] += 1
                    stats["items"] += 1
                idx = bm.end()
            xml.append(inline_runs(s[idx:]))
    return "".join(xml)


def md_to_body(md, keymap, labels, missing, stats, section, render):
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
            # tables are flattened to paragraphs; their citations stay [@key] text
            for line in b.splitlines():
                if re.match(r"^\|\s*-", line):
                    continue
                cells = [c.strip() for c in line.strip("|").split("|")]
                body.append(paragraph(inline_runs("   ".join(cells)), "TableText"))
            stats["table_blocks"] += 1
            continue
        text = " ".join(l.strip() for l in b.splitlines())
        body.append(paragraph(convert_paragraph(text, keymap, labels, missing, stats, render)))
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
    write_zip(path, [("[Content_Types].xml", CONTENT_TYPES), ("_rels/.rels", RELS),
                     ("word/_rels/document.xml.rels", DOC_RELS), ("word/document.xml", doc), ("word/styles.xml", STYLES)])


class Parser(argparse.ArgumentParser):
    def error(self, message):  # usage errors exit 1, so 2 always means unmapped citations
        self.print_usage(sys.stderr)
        print(f"{self.prog}: error: {message}", file=sys.stderr)
        sys.exit(1)


def fail(message):
    print(message, file=sys.stderr)
    sys.exit(1)


def main():
    ap = Parser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workspace", default=".")
    ap.add_argument("--out", required=True)
    ap.add_argument("--sections", default=",".join(SECTION_ORDER))
    ap.add_argument("--library", default="", help="users/<id> or groups/<id> for building URIs")
    ap.add_argument("--keys", default="", help="Better BibTeX JSON export (default Literature/library.bbt.json)")
    ap.add_argument("--report", default="")
    ap.add_argument("--markers", action="store_true",
                    help="write Scannable Cite markers for the ODF/DOCX Scan instead of fields (files without pictures only)")
    ap.add_argument("--convert", default="", help="existing .docx with Scannable Cite markers to turn into live Zotero fields")
    ap.add_argument("--no-item-data", action="store_true",
                    help="with --convert, do not ask Zotero desktop for item data (Zotero resolves the URIs on Refresh)")
    ap.add_argument("--force", action="store_true", help="overwrite --out if it exists (it may hold the author's Word edits)")
    args = ap.parse_args()

    out = Path(args.out)
    if args.convert and args.markers:
        ap.error("--markers cannot be combined with --convert")
    if args.convert and not Path(args.convert).is_file():
        fail(f"{args.convert} does not exist")
    if args.convert and out.resolve() == Path(args.convert).resolve():
        fail("--out must differ from the --convert input; the input is never overwritten")
    if out.exists() and not args.force:
        fail(f"{out} exists and may hold edits made in Word (style, Refresh, bibliography). "
             "Choose another --out, or pass --force to replace it.")

    if args.convert:
        out.parent.mkdir(parents=True, exist_ok=True)
        report = convert_docx(args.convert, out, item_data=not args.no_item_data)
        if args.report:
            Path(args.report).write_text(json.dumps(report, indent=1), encoding="utf8")
        print(json.dumps(report, indent=1))
        if report["markers_left"]:
            print("Some markers are split across runs or formatting and were not converted; "
                  "retype them as one plain run and convert again.", file=sys.stderr)
        sys.exit(2 if report["markers_left"] else 0)

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

    sections = [s.strip() for s in args.sections.split(",") if s.strip()]
    if not any((ws / "Manuscript" / f"{sec}.md").exists() for sec in sections):
        fail(f"No Manuscript/<section>.md found in {ws} for sections {', '.join(sections)}")
    missing, stats = set(), {"citations": 0, "items": 0, "unmapped": 0, "table_blocks": 0}
    if args.markers:
        render = lambda resolved: run(marker_text(resolved))
        note = ("Note for the author. In Zotero run Tools, ODF/DOCX Scan on this file (markers to citations), "
                "open the result in Word, press Refresh on the Zotero tab, then delete this note.")
        placeholder = "Place the cursor here and use the Zotero plugin to insert the bibliography after the scan."
    else:
        csl = {keymap[ck][1]: e for e in lib for ck in [e.get("id") or e.get("citation-key")] if ck in keymap and keymap[ck][1]}
        render = lambda resolved: citation_field(resolved, csl, index=stats["citations"])
        note = ("Note for the author. In Word open the Zotero tab, choose Document Preferences and the journal style, "
                "then press Refresh. Put the cursor on the line under References and click Add/Edit Bibliography. "
                "Then delete this note.")
        placeholder = "Place the cursor here and click Add/Edit Bibliography on the Zotero tab."

    body = [paragraph(run(note), "Note")]
    for sec in sections:
        f = ws / "Manuscript" / f"{sec}.md"
        if not f.exists():
            continue
        md = f.read_text(encoding="utf8")
        if sec in HEADING_FOR and not re.search(r"^#\s", md, re.M):
            body.append(paragraph(run(HEADING_FOR[sec]), "Heading1"))
        body.extend(md_to_body(md, keymap, labels, missing, stats, sec, render))
    body.append(page_break())
    body.append(paragraph(run("References"), "Heading1"))
    body.append(paragraph(run(placeholder), "Note"))

    out.parent.mkdir(parents=True, exist_ok=True)
    write_docx(out, "".join(body))

    report = {"out": str(out), "mode": "markers" if args.markers else "fields",
              "citations_written": stats["citations"], "items_cited": stats["items"],
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
