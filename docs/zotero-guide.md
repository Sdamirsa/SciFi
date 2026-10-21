# Connecting Zotero to SciFi

SciFi reads your literature from one of two routes. Pick one per workspace. Both use the same
citation keys, so a manuscript written on one route works on the other.

| | Route A, Zotero MCP | Route B, Better BibTeX export |
|---|---|---|
| What the agents read | your live Zotero library, full texts and annotations | `Literature/library.json` and `Literature/fulltext/` |
| Setup | install one Python package, enable one MCP server | install one Zotero plugin, export once, copy PDFs |
| Works offline, in copies, on claude.ai uploads | needs Zotero running on the same machine | yes, the files travel with the workspace |
| Checked by `bbt_check.py` | only if you also export `library.json` | yes |

Recommendation: use Route B always (it makes the workspace self-contained and checkable) and
add Route A when you want the agents to search your whole library or read your highlights.

In both routes the manuscript cites with pandoc syntax, `[@smith2023deep]`, several as
`[@smith2023deep; @lee2021echo]`, narrative as `@smith2023deep showed`. The key is the Better
BibTeX citation key. At submission pandoc (or Zotero's Word plugin after conversion) turns the
keys into the journal's style. SciFi never edits `Literature/library.json` or
`Literature/fulltext/`. The stages that write notes, an ontology and labels into `Literature/`
are in `skills/scifi-literature/SKILL.md`. How agents resolve a key is in
`skills/scifi-literature/references/lookup.md`.

## Before either route: Better BibTeX and a key formula

Both routes need stable citation keys.

1. Install Zotero 7 from zotero.org.
2. Install Better BibTeX (BBT). Download the latest `.xpi` from
   retorquere.github.io/zotero-better-bibtex, then in Zotero open Tools, Plugins, the gear
   icon, "Install Plugin From File", choose the `.xpi`, restart Zotero.
3. Set the citation key formula. Zotero, Settings, Better BibTeX, Citation keys, "Citation key
   formula". Enter

   ```
   auth.lower + year + shorttitle(1,1).lower
   ```

   This builds the first author's family name in lower case, the four-digit year and the
   first meaningful word of the title in lower case, for example `smith2023deep` for Smith J,
   2023, "Deep learning for echocardiography". `shorttitle(1,1)` takes one word and skips
   stop words such as "a", "the" and "of". Keys are readable in the manuscript, unique in
   almost every library, and stable when you add papers. Collisions get a suffix (`a`, `b`)
   automatically. Pick the formula once, before the first citation, since changing it later
   renames unpinned keys.
4. Pin the keys. Select all items in the paper's collection, right-click, Better BibTeX, "Pin
   BibTeX key". A pinned key never changes, even if you later fix the title or author
   metadata. Pin new papers when you add them (or turn on automatic pinning in the BBT
   settings if your version offers it).

## Route A: Zotero MCP

SciFi recommends `zotero-mcp` by 54yyyu (MIT licence). In local mode it talks to the Zotero
desktop app on your machine, which reads your `zotero.sqlite` database, so it needs no API key
and sees full texts and PDF annotations.

1. Python 3.10 or newer. Install the server

   ```bash
   pip install zotero-mcp-server
   # or: uv tool install zotero-mcp-server
   zotero-mcp setup        # optional, writes a config for Claude Desktop
   ```

2. In Zotero, Settings, Advanced, enable "Allow other applications on this computer to
   communicate with Zotero" (the local API). Keep Zotero running while you work.
3. Add the server to your workspace. The template is
   `${CLAUDE_PLUGIN_ROOT}/templates/mcp.zotero.json` (when SciFi is copied into a project,
   `.claude/templates/mcp.zotero.json`). Merge its `mcpServers` entry into `.mcp.json` at
   the workspace root:

   ```json
   {
     "mcpServers": {
       "zotero": {
         "command": "zotero-mcp",
         "args": [],
         "env": { "ZOTERO_LOCAL": "true" }
       }
     }
   }
   ```

4. Start Claude Code in the workspace, approve the `zotero` server when asked, and run `/mcp`
   to see it connected. Ask "list my Zotero collections" as a test.
5. Tell SciFi. `/scifi` detects a Zotero tool and records the route as `zotero-mcp` in
   `STATE.json`.

How the agents use it. The master lists the Zotero tools in a brief only for
`literature-scout` and `evidence-checker`, never for drafting agents. They search by citekey,
DOI or title (`zotero_search_items`, `zotero_get_collection_items`), read metadata
(`zotero_get_item_metadata`), read the paper (`zotero_get_item_fulltext`) and, when you ask
for it, your highlights (`zotero_get_annotations`, `zotero_get_notes`). They never create or
change items. If Zotero is closed the call fails and the agent returns a NEED asking you to
start it, rather than guessing.

## Route B: no MCP, a Better BibTeX export

1. Complete "Before either route" above.
2. Organise the paper's collection (layout in
   `skills/scifi-literature/references/library-building.md`). Export the parent collection;
   its subcollections come with it.
3. Right-click the collection, "Export Collection...". Format "Better CSL JSON". Tick "Keep
   updated". Save as `<workspace>/Literature/library.json`.

   "Keep updated" makes BBT rewrite the file whenever the collection changes, so a paper you
   add in Zotero appears in `library.json` without another export. Manage or remove automatic
   exports in Settings, Better BibTeX, Automatic export. Each entry's `id` is the citation
   key (`citation-key` holds it too in recent BBT versions), and that is what `bbt_check.py`
   and the agents match.

4. Put the full texts in `Literature/fulltext/<citekey>.pdf`. Three ways.

   - **BBT file export.** Export the collection once more in the "Better BibTeX" format with
     "Export Files" ticked into a temporary folder. BBT copies each attachment into a
     subfolder and the `.bib` file records each entry's key and `file` path. Then rename by
     key (the script idea below). Use this for the first bulk copy.
   - **By hand.** In Zotero, right-click the PDF attachment, "Show File", copy it to
     `Literature/fulltext/` and rename it to the key (BBT, "Copy citation key" in the item's
     context menu puts the key on the clipboard). Fine for a handful of papers.
   - **A short script.** Read the `.bib` from the file export and copy each entry's first PDF
     to `fulltext/<key>.pdf`. For example, with `refs.bib` from the export:

     ```bash
     python3 -c "import re,shutil,sys;b=open(sys.argv[1]).read();[shutil.copy(f.split(';')[0].strip(),sys.argv[2]+'/'+k+'.pdf') for k,f in re.findall(r'@\w+\{([^,]+),.*?file\s*=\s*\{([^}]*\.pdf)',b,re.S)]" refs.bib Literature/fulltext
     ```

     The idea in one line. Match each entry's key with its `file` field and copy the file to
     `<key>.pdf`. Check the result with `bbt_check.py` (step 6).

5. Optional, extract text. Agents read Markdown or text faster and more reliably than PDF, and
   a `.md` next to the PDF is used first. With poppler installed,

   ```bash
   for f in Literature/fulltext/*.pdf; do pdftotext -layout "$f" "${f%.pdf}.md"; done
   ```

   A scanned PDF without a text layer gives an empty file. Run OCR first (for example
   `ocrmypdf in.pdf out.pdf`) or tag the item `full-text-not-found` in Zotero.

6. Check. From the workspace root

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/scripts/bbt_check.py          # as a plugin
   python3 .claude/scripts/bbt_check.py                         # copied into .claude/
   python3 /path/to/bbt_check.py --workspace ~/my-paper         # from anywhere
   ```

   It reads every `Manuscript/*.md`, finds each `[@key]` and `@key`, and reports keys missing
   from `library.json` (exit 2), cited keys with no file in `fulltext/`, library entries never
   cited, and duplicate keys. `--strict` also fails on missing full texts and duplicates. Run
   it after adding citations and before submission. Agents raise a NEED for every missing key
   or file it lists.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `bbt_check.py` says a key is missing but it is in Zotero | the paper is outside the exported collection, or the export is not "Keep updated"; add it to the collection |
| keys changed after a metadata fix | they were not pinned; pin them and update the manuscript once |
| duplicate keys | two Zotero items for the same paper; merge them (Zotero, Duplicate Items) |
| the MCP returns nothing | Zotero is closed or the local API is off (step A2) |
| an agent asks for a full text you have | the file name does not equal the key; rename it to `<key>.pdf` |
