# SciFi: contributor notes

This repo is the SciFi plugin itself, not a manuscript workspace. It ships skills, agents,
hooks, scripts and schemas for writing and evaluating scientific manuscripts, plus the
packages for claude.ai in `dist/`. User docs start at `README.md`.

## Read first

- `docs/protocol.md`: the one contract. Every skill and agent is written against it.
- `docs/architecture.md`: why the design is what it is.
- `skills/scientific-writing/`: the standards. Change "good" here and nowhere else.

## Conventions

- One route per task. If the protocol or a skill already covers something, point to it.
  Never restate or re-implement it in a second place.
- No em dashes or en dashes anywhere. Avoid colons and semicolons in running prose (fine in
  headings, tables and code). No promotional words.
- A `SKILL.md` body stays under about 150 lines; depth goes in files it points to.
  Frontmatter `name` equals the folder name; the description carries concrete trigger phrases.
- Scripts and hooks are bash plus python3 standard library. Each has a usage docstring and
  exits non-zero on failure. Paths resolve via `${CLAUDE_PLUGIN_ROOT}` and, when copied,
  relative to `.claude/`; document both.
- A schema change updates `scripts/schemas/`, `docs/protocol.md` and every writer of that
  file in the same change.
- Every JSON under `example-workspace/` must pass `python3 scripts/validate_json.py <file>`.
- No real manuscript, patient or unpublished data in the repo. The example study is invented.
- `dist/*.skill` is committed. Rebuild it when `skills/scientific-writing/` or
  `skills/scifi-lite/` changes.
- The system figure and the anatomy page share `docs/anatomy_data.py`. When a skill, agent,
  hook, script or workspace file is added, renamed or removed, change it there and run
  `python3 docs/make_figure.py && node docs/render_figure.js && python3 docs/make_anatomy.py --check`.

## Test

```bash
python3 -m unittest discover -s scripts/tests -v
for f in $(find example-workspace -name '*.json'); do python3 scripts/validate_json.py "$f" || exit 1; done
```

## After changing skills, agents or hooks

Run the `design-reviewer` agent with a brief listing the changed files. It audits them
against `skills/system-design-review/rubric.md` and returns findings. Resolve every FAIL
before merging, and record notable changes in `CHANGELOG.md`.

## Release

The version lives in `.claude-plugin/plugin.json` and `scripts/release.py` keeps everything
else in step. `bump <patch|minor|major>` sets it, opens the CHANGELOG heading and rebuilds
`docs/` and `dist/`; `check` verifies versions, changelog, tests, example JSON, page links and
a clean tree; `tag` makes `v<version>`; `publish` pushes and creates the GitHub release with
the three dist files attached. Users on claude.ai download from the release page.
