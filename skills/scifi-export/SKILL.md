---
name: scifi-export
description: >
  Export the manuscript to a Word file whose citations are already live Zotero citation fields,
  and from there to Google Docs with the citations still live. Use when the user says
  "export to Word", "make the docx", "give me a Word file with Zotero citations", "send it
  to Google Docs with live citations", "I need the manuscript for coauthors in Word",
  "turn these citation markers into Zotero citations", "/scifi-export". Reads Manuscript/*.md
  with pandoc [@citekey] citations and the Zotero item keys from a Better BibTeX JSON export
  (Literature/library.bbt.json), or converts an existing .docx that carries Scannable Cite
  markers. Not for PDF or a docx without citations, which pandoc converts directly.
argument-hint: "[--out file.docx] [--library users/<id>|groups/<id>] [--sections ...] [--convert in.docx] [--force]"
allowed-tools: Read, Bash(python3 *), Glob
---

# scifi-export

Zotero's Word plugin stores each citation as a field, `ADDIN ZOTERO_ITEM CSL_CITATION {…}`,
holding the item URI and its CSL data. `export_docx.py` writes exactly that field for every
citation, as Better BibTeX's pandoc filter does, so the author only picks a style, presses
Refresh and inserts the bibliography. No Zotero add-on and no scan step are involved. Google
Docs cannot read Word fields, so for Google Docs one more menu action in Word rewrites them as
links its Zotero connector recognises. The full step list and the troubleshooting table are in
`${CLAUDE_PLUGIN_ROOT}/docs/zotero-guide.md` (relative to `.claude/` when copied), section
"Export to Word and Google Docs".

## Procedure

1. **Confirm the inputs.** `Manuscript/*.md` with `[@citekey]` citations, and a key source
   for the Zotero item keys: `Literature/library.bbt.json` (a Better BibTeX JSON export of
   the collection, kept updated, which carries `citekey`, `itemKey` and `uri` per item),
   or `--keys <file>`. Ask which library the items live in (synced personal library
   `users/<id>` or a group `groups/<id>`). The fields need the full `http://zotero.org/...`
   URI, never the short `zu:` or `zg:` form, and a local-only library URI will not resolve.
   If the user has no BBT JSON export yet, point them to the guide (two minutes in Zotero).
2. **Check keys first.** `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/bbt_check.py --workspace <ws>`
   so no cited key is missing from the library.
3. **Export.**
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/export_docx.py --workspace <ws> --out <ws>/export/<name>.docx --library users/<id> --report <ws>/export/<name>.report.json`
   The script writes a docx with headings, paragraphs, a short note to the author at the top,
   every citation group as one live Zotero field (CSL data from `Literature/library.json`,
   locators such as `p. 12` as CSL locators), a page break, a "References" heading and a
   placeholder line where the bibliography goes. It never writes the reference list itself, and
   it never replaces an existing file (the author may have edited it in Word) unless given `--force`.
4. **Already have a .docx with Scannable Cite markers** (`{prefix|Surname, (Year)|locator|suffix|uri}`,
   for example a document relinked by hand)? Convert it instead of exporting:
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/export_docx.py --convert <in.docx> --out <out.docx>`.
   It reads `w:t` text only, so pictures, tables and comments are left untouched, and it asks
   Zotero desktop for each item's data (add `--no-item-data` when Zotero is closed). A marker
   group split across formatting runs is reported in `markers_left`. Fix it and run again.
5. **Read the report.** `citations_written`, `items_cited`, `unmapped_citations` and
   `missing_keys` (or `markers_left` for `--convert`). Hand the file over only when
   `missing_keys` is empty and `markers_left` is 0. Otherwise resolve the keys with the user
   (a missing key is never guessed) and export again. Tables are flattened to paragraphs and
   their citations stay as `[@key]` text. The report says how many table blocks there were.
6. **Hand over** the docx with these steps, in order:
   1. Open the file in Word desktop with the Zotero plugin (Word Online does not work).
   2. Zotero tab, **Document Preferences**, choose the journal's style, OK.
   3. Zotero tab, **Refresh**. Every citation renders in the style. A "missing item" message
      means the library is not synced. Sync it in Zotero and press Refresh again.
   4. Put the cursor on the placeholder line under **References**, delete it, and click
      **Add/Edit Bibliography**. Delete the note at the top. Save.
   5. Only for Google Docs, Document Preferences, **Switch to a Different Word Processor**,
      save, upload, *Save as Google Docs*, then Zotero menu, Refresh. Say that skipping the
      switch leaves dead text in Google Docs.

Do not offer Zotero's ODF/DOCX Scan for a file with pictures. It corrupts such files, as the
guide explains under "The ODF/DOCX Scan route".

## What the script does not do

- It does not need python-docx or Zotero add-ons.
- It does not format to a journal template; the style is chosen in Document Preferences.
- It does not export figures. Figures are inserted in Word from `Thinking-space/figures/`
  or the user's files.

## Without Zotero

For a reviewer copy with numeric citations and a reference list, use pandoc with the CSL
style and `Literature/library.json`:
`pandoc Manuscript/*.md --citeproc --bibliography Literature/library.json --csl <style>.csl -o draft.docx`.
That file has no live fields and is for reading, not for coauthoring in Zotero.
