<!-- This file is invented for illustration and describes a fictional study. -->

# Full texts

One file per cited source, named by its citation key: `<citekey>.pdf` or `<citekey>.md`. The evidence-checker reads only the keys a unit cites, and only their methods and results.

This example holds two invented full texts as Markdown, `mahmoudi2025echo.md` and `lindqvist2022rules.md`. The other six references in `../library.json` would sit here as PDFs in a real workspace. They are left out on purpose. When a unit cites one of them, the evidence-checker cannot verify the claim and returns a NEED (see `Thinking-space/handshakes/d03.evidence-checker.r1.json`, which asks for `vandermeer2024external`).

With Zotero and Better BibTeX, an automatic export keeps `library.json` current and you copy the PDFs here by citation key. With the Zotero MCP route, this folder can stay empty. See `docs/zotero-guide.md` in the SciFi repository.
