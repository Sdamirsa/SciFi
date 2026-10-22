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

## Planned

- Detect hand edits to accepted drafts by storing a hash of each draft in STATE.json and comparing on resume (sets the unit to human-edited).
- Schemas for Literature/ontology.yaml and Literature/labels/*.json so the validate-json hook covers the literature stages.
- Round-aware synthesis files are in place (d03.synthesis.r1.json); a merge view across rounds is not.
