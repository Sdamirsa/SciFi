"""export_docx.py writes live Zotero citation fields, keeps --markers, and converts marker files
without touching markup (the {GUID} in picture XML that breaks the ODF/DOCX Scan)."""
import json
import re
import subprocess
import sys
import tempfile
import unittest
import xml.dom.minidom
import zipfile
from pathlib import Path

from _helpers import SCRIPTS

EXPORT = SCRIPTS / "export_docx.py"
GUID = "{28A0092B-C50C-407E-A947-70E740481C1C}"
W_NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'


def run_export(*args):
    return subprocess.run([sys.executable, str(EXPORT), *args], capture_output=True, text=True)


def document_xml(path):
    with zipfile.ZipFile(path) as z:
        return z.read("word/document.xml").decode("utf8")


def fields(doc):
    """[(json code, visible result)] for every ZOTERO_ITEM field."""
    out = []
    for m in re.finditer(r'fldCharType="begin"/>.*?<w:instrText[^>]*>(.*?)</w:instrText>.*?fldCharType="separate"/>'
                         r'.*?<w:t[^>]*>(.*?)</w:t>.*?fldCharType="end"/>', doc, re.S):
        code = xml.dom.minidom.parseString(f"<x>{m.group(1)}</x>").documentElement.firstChild.data
        out.append((json.loads(code[code.index("{"):code.rindex("}") + 1]), m.group(2)))
    return out


class ExportFields(unittest.TestCase):
    def workspace(self, tmp):
        ws = Path(tmp)
        (ws / "Manuscript").mkdir()
        (ws / "Literature").mkdir()
        (ws / "Manuscript" / "introduction.md").write_text(
            "# Introduction\n\nScreening works [@smith2024, p. 12; @lee2023]. Later work agrees @lee2023.\n", encoding="utf8")
        lib = [{"id": "smith2024", "type": "article-journal", "title": "Screening", "itemKey": "AAAA1111",
                "note": "private extra", "abstract": "long text",
                "author": [{"family": "Smith", "given": "A"}], "issued": {"date-parts": [[2024]]}},
               {"id": "lee2023", "type": "article-journal", "title": "Agreement", "itemKey": "BBBB2222",
                "author": [{"family": "Lee", "given": "B"}], "issued": {"date-parts": [[2023]]}}]
        (ws / "Literature" / "library.json").write_text(json.dumps(lib), encoding="utf8")
        return ws

    def test_default_writes_live_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = self.workspace(tmp)
            out = ws / "export" / "m.docx"
            r = run_export("--workspace", str(ws), "--out", str(out), "--library", "groups/42")
            self.assertEqual(r.returncode, 0, r.stderr)
            doc = document_xml(out)
            xml.dom.minidom.parseString(doc.encode("utf8"))
            got = fields(doc)
            self.assertEqual(len(got), 2)
            first, text = got[0]
            self.assertEqual(text, "(Smith 2024; Lee 2023)")
            self.assertEqual(first["properties"]["plainCitation"], text)
            smith = first["citationItems"][0]
            self.assertEqual(smith["uris"], ["http://zotero.org/groups/42/items/AAAA1111"])
            self.assertEqual(smith["itemData"]["title"], "Screening")
            self.assertEqual((smith["label"], smith["locator"]), ("page", "12"))
            self.assertNotIn("note", smith["itemData"])
            self.assertNotIn("abstract", smith["itemData"])
            self.assertNotIn("{|", doc)
            self.assertIn("Add/Edit Bibliography", doc)

    def test_existing_output_needs_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = self.workspace(tmp)
            out = ws / "m.docx"
            self.assertEqual(run_export("--workspace", str(ws), "--out", str(out), "--library", "groups/42").returncode, 0)
            before = out.read_bytes()
            again = run_export("--workspace", str(ws), "--out", str(out), "--library", "groups/42")
            self.assertEqual(again.returncode, 1)
            self.assertEqual(out.read_bytes(), before)
            forced = run_export("--workspace", str(ws), "--out", str(out), "--library", "groups/42", "--force")
            self.assertEqual(forced.returncode, 0, forced.stderr)
            self.assertEqual(out.read_bytes(), before)  # deterministic citation IDs

    def test_markers_flag_keeps_scannable_cite(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = self.workspace(tmp)
            out = ws / "m.docx"
            r = run_export("--workspace", str(ws), "--out", str(out), "--library", "groups/42", "--markers")
            self.assertEqual(r.returncode, 0, r.stderr)
            doc = document_xml(out)
            self.assertIn("{|Smith, (2024)|p. 12||http://zotero.org/groups/42/items/AAAA1111}", doc)
            self.assertEqual(fields(doc), [])


class ConvertMarkers(unittest.TestCase):
    def make(self, tmp, body):
        src = Path(tmp) / "in.docx"
        doc = f'<?xml version="1.0" encoding="UTF-8"?><w:document {W_NS}><w:body>{body}</w:body></w:document>'
        with zipfile.ZipFile(src, "w") as z:
            z.writestr("word/document.xml", doc)
            z.writestr("[Content_Types].xml", "<Types/>")
        return src

    def test_input_is_never_the_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = self.make(tmp, "<w:p/>")
            before = src.read_bytes()
            r = run_export("--convert", str(src), "--out", str(src), "--no-item-data", "--force")
            self.assertEqual(r.returncode, 1)
            self.assertEqual(src.read_bytes(), before)

    def test_tracked_formatting_run(self):
        marker = "{|Lee, (2023)|||http://zotero.org/groups/42/items/BBBB2222}"
        rpr = '<w:rPr><w:i/><w:rPrChange w:id="1" w:author="A"><w:rPr><w:b/></w:rPr></w:rPrChange></w:rPr>'
        with tempfile.TemporaryDirectory() as tmp:
            src = self.make(tmp, f'<w:p><w:r>{rpr}<w:t>See {marker}.</w:t></w:r></w:p>')
            out = Path(tmp) / "out.docx"
            r = run_export("--convert", str(src), "--out", str(out), "--no-item-data")
            self.assertEqual(r.returncode, 0, r.stderr)
            new = document_xml(out)
            xml.dom.minidom.parseString(new.encode("utf8"))
            self.assertEqual(len(fields(new)), 1)
            self.assertEqual(new.count("<w:rPrChange"), 1)  # stays on the original run, never copied to new runs
            self.assertEqual(new.count("<w:i/>"), 7)  # the italic itself reaches the five field runs and the tail run

    def test_marker_next_to_picture_guid(self):
        marker = "{|Smith, (2024)|||http://zotero.org/groups/42/items/AAAA1111}"
        body = (f'<w:p><w:r><w:drawing><a:ext xmlns:a="urn:a" uri="{GUID}"/></w:drawing></w:r></w:p>'
                f'<w:p><w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">Before {marker} after.</w:t></w:r></w:p>')
        doc = f'<?xml version="1.0" encoding="UTF-8"?><w:document {W_NS}><w:body>{body}</w:body></w:document>'
        with tempfile.TemporaryDirectory() as tmp:
            src, out = Path(tmp) / "in.docx", Path(tmp) / "out.docx"
            with zipfile.ZipFile(src, "w") as z:
                z.writestr("word/document.xml", doc)
                z.writestr("[Content_Types].xml", "<Types/>")
            r = run_export("--convert", str(src), "--out", str(out), "--no-item-data")
            self.assertEqual(r.returncode, 0, r.stderr)
            new = document_xml(out)
            xml.dom.minidom.parseString(new.encode("utf8"))
            self.assertIn(f'uri="{GUID}"', new)
            got = fields(new)
            self.assertEqual(len(got), 1)
            self.assertEqual(got[0][1], "(Smith 2024)")
            self.assertEqual(got[0][0]["citationItems"][0]["uris"], ["http://zotero.org/groups/42/items/AAAA1111"])
            text = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", new))
            self.assertEqual(text, "Before (Smith 2024) after.")
            self.assertEqual(new.count("<w:b/>"), 7)  # before, five field runs, after
            self.assertEqual(json.loads(r.stdout)["markers_left"], 0)


if __name__ == "__main__":
    unittest.main()
