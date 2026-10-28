# Changelog

## 0.1.0 (2026-10-21)

Initial release.

- Master skill `scifi` with six stages: spine, skeleton, figures, paragraph loop, review, ritual.
- Stage skills `scifi-spine`, `scifi-skeleton`, `scifi-figures`, `scifi-paragraph`, `scifi-review`, `scifi-literature`.
- Sub-agents for the logic map, five check axes, drafting, the standards gate, improvement, figure brainstorming, literature lookup and design review.
- JSON schemas for briefs, envelopes, syntheses, logic maps, spine, skeleton, figures, comments and state, with a validation hook.
- Session-start resume and stop-pointer hooks.
- `project-memory` end-of-session ritual (STATUS, Project-log, LESSONS).
- `scientific-writing` standards from 14 published papers, with `check_manuscript.py`.
- `scifi-lite` and `scientific-writing` packages for claude.ai.
- Example workspace with an invented study.

## 0.1.1 (2026-10-22)
- `scifi-stats` skill: method selection from question, data type and design via a method map, a complexity guard against paper-specific methods, reporting rules and an analysis-plan template.
- `scifi-export` skill and `scripts/export_docx.py`: Word export with Scannable Cite markers that Zotero's ODF/DOCX Scan turns into live citation fields, with the Google Docs handoff steps in the Zotero guide.
- Anatomy page `docs/index.html` (GitHub Pages): the system figure as a clickable page with a Claude Code view and a claude.ai view; every node opens its file, folder, schema or document. Content for the figure and the page now comes from `docs/anatomy_data.py`.
- `scripts/release.py`: version check, bump, tag and GitHub release with the dist files attached.
- `scifi-lite` writes `handshakes/<id>.synthesis.r<n>.json`, the plugin's name, so a workspace moves between the two without renaming.

## 0.2.0 (2026-10-22)
- Dynamic workflows for the two batch fan-outs: `workflows/review-all.js` (logic map and five checks on every unit in parallel, then the manuscript pass) and `workflows/literature-all.js` (one noter or labeler per paper). They write the same briefs and envelopes as a dispatch, validated by the runtime against the envelope schema and stored by a scribe stage, and return counts rather than content. Protocol section 12.
- Agents `noter` and `labeler` for the literature stages, which previously had no agent file to dispatch, and `scribe` (Write and the validator only) for the workflow stages that store files.
- `scripts/build_workflows.py` builds the scripts from `scripts/workflow_templates/` with the envelope schema inlined; `scripts/tests/_workflow_harness.js` runs them end to end with mock agents in the tests.
- `install_local.sh` and the `.claude/` zip carry `workflows/` with the agent prefix removed.

## 0.2.1

- `scifi-export` writes live Zotero citation fields directly (`ADDIN ZOTERO_ITEM CSL_CITATION` with the item URI and CSL data, as Zotero's Word plugin and Better BibTeX's pandoc filter write them). The author picks a style, presses Refresh and inserts the bibliography; no ODF/DOCX Scan add-on is needed.
- `export_docx.py --convert` turns an existing .docx with Scannable Cite markers into fields. It edits document text only, so pictures, tables, comments and tracked changes stay intact, and it takes item data from Zotero desktop's local API.
- `--markers` keeps the old Scannable Cite output. The Zotero guide now warns that the ODF/DOCX Scan corrupts any .docx with pictures: it matches raw XML and takes the `{GUID}` in picture markup for a marker.
- Tests for field export, `--markers` and conversion next to a picture.

## Planned

- Detect hand edits to accepted drafts by storing a hash of each draft in STATE.json and comparing on resume (sets the unit to human-edited).
- Schemas for Literature/ontology.yaml and Literature/labels/*.json so the validate-json hook covers the literature stages.
- Round-aware synthesis files are in place (d03.synthesis.r1.json); a merge view across rounds is not.
