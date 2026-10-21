---
name: scifi-export
description: >
  Export the manuscript to a Word file whose citations become live Zotero citation fields,
  and from there to Google Docs with the citations still live. Use when the user says
  "export to Word", "make the docx", "give me a Word file with Zotero citations", "send it
  to Google Docs with live citations", "I need the manuscript for coauthors in Word",
  "/scifi-export". Reads Manuscript/*.md with pandoc [@citekey] citations and the Zotero
  item keys from a Better BibTeX JSON export (Literature/library.bbt.json). Not for PDF or
  plain docx without citations; for those, convert with pandoc.
argument-hint: "[--out file.docx] [--library users/<id>|groups/<id>] [--sections ...]"
allowed-tools: Read, Bash(python3 *), Glob
---

# scifi-export

Zotero's Word plugin stores each citation as a field holding the item URI. Google Docs
cannot read Word fields, but Zotero can rewrite every field as a hyperlink that its Google
Docs connector recognises. The system therefore writes plain-text Scannable Cite markers
into a docx, Zotero's ODF/DOCX Scan turns them into fields, Word refreshes them, and one
menu action makes them Google Docs ready. The user does four short steps in Zotero, Word and
Google Docs; the full step list and the troubleshooting table are in
`${CLAUDE_PLUGIN_ROOT}/docs/zotero-guide.md`, section "Export to Word and Google Docs".

## Procedure

1. **Confirm the inputs.** `Manuscript/*.md` with `[@citekey]` citations, and a key source
   for the Zotero item keys: `Literature/library.bbt.json` (a Better BibTeX JSON export of
   the collection, kept updated, which carries `citekey`, `itemKey` and `uri` per item),
   or `--keys <file>`. Ask which library the items live in (synced personal library
   `users/<id>` or a group `groups/<id>`); the markers need the full `http://zotero.org/...`
   URI, never the short `zu:` or `zg:` form, and a local-only library URI will not resolve.
   If the user has no BBT JSON export yet, point them to the guide (two minutes in Zotero).
2. **Check keys first.** `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/bbt_check.py --workspace <ws>`
   so no cited key is missing from the library.
3. **Export.**
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/export_docx.py --workspace <ws> --out <ws>/export/<name>.docx --library users/<id> --report <ws>/export/<name>.report.json`
   The script writes a docx with headings, paragraphs, a scan note at the top, every
   citation group as one unbroken marker run (adjacent markers merge into one citation;
   ranges and multi-item citations become adjacent markers; a locator such as `p. 12` goes
   into the marker's locator field), a page break, a "References" heading and a placeholder
   line where the bibliography will be inserted. It never writes the reference list;
   Zotero generates it from the fields.
4. **Read the report.** `citations_written`, `items_in_markers`, `unmapped_citations` and
   `missing_keys`. Hand the file over only when `missing_keys` is empty; otherwise resolve
   the keys with the user (a missing key is never guessed) and export again. Tables are
   flattened to paragraphs and citations inside them must be inserted by hand in Word; the
   report says how many table blocks there were.
5. **Hand over** the docx plus the seven user steps from the guide, verbatim, in order.
   Step 4 (Switch to a Different Word Processor) is the one users skip, and skipping it
   leaves dead text in Google Docs; say so.

## What the script does not do

- It does not create Word field codes itself and does not need python-docx.
- It does not format to a journal template; that happens in Word after the scan, with the
  journal's CSL style chosen in Zotero's Document Preferences.
- It does not export figures. Figures are inserted in Word from `Thinking-space/figures/`
  or the user's files, after the scan.

## Without Zotero

For a reviewer copy with numeric citations and a reference list, use pandoc with the CSL
style and `Literature/library.json`:
`pandoc Manuscript/*.md --citeproc --bibliography Literature/library.json --csl <style>.csl -o draft.docx`.
That file has no live fields and is for reading, not for coauthoring in Zotero.
