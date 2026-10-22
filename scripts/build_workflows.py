#!/usr/bin/env python3
"""Build workflows/*.js from scripts/workflow_templates/*.js, inlining the envelope schema.

Usage:
    python3 scripts/build_workflows.py            write workflows/<name>.js for every template
    python3 scripts/build_workflows.py --check    exit 1 if any built file differs from its
                                                  template, or fails a JavaScript syntax check

Why: a dynamic workflow script cannot read files, so the JSON schema it hands to agent({schema})
must be inlined. The template holds the placeholder __ENVELOPE_SCHEMA__ and this script puts
scripts/schemas/envelope.schema.json there (without $schema and title, which the runtime does
not need), so the schema stays single-sourced. Stdlib only; the syntax check uses node when it
is on PATH and is skipped otherwise.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEMPLATES = REPO / "scripts" / "workflow_templates"
OUT = REPO / "workflows"
SCHEMA = REPO / "scripts" / "schemas" / "envelope.schema.json"


def envelope_schema_js():
    schema = json.loads(SCHEMA.read_text(encoding="utf8"))
    schema = {k: v for k, v in schema.items() if k not in ("$schema", "title")}
    return json.dumps(schema, indent=2)


def render(template: Path) -> str:
    text = template.read_text(encoding="utf8")
    if "__ENVELOPE_SCHEMA__" not in text:
        raise SystemExit(f"{template.name}: no __ENVELOPE_SCHEMA__ placeholder")
    return text.replace("__ENVELOPE_SCHEMA__", envelope_schema_js(), 1)


def syntax_ok(js: str) -> str:
    """Return '' when node accepts the script wrapped the way the runtime runs it, else the error."""
    node = shutil.which("node")
    if not node:
        return ""
    body = re.sub(r"^export const meta", "const meta", js, count=1, flags=re.M)
    wrapped = "async function __scifi_workflow(args, agent, pipeline, parallel, phase, log, budget, workflow) {\n" + body + "\n}\n"
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf8") as fh:
        fh.write(wrapped)
        path = fh.name
    try:
        r = subprocess.run([node, "--check", path], capture_output=True, text=True)
        return "" if r.returncode == 0 else r.stderr.strip()
    finally:
        Path(path).unlink(missing_ok=True)


def meta_ok(js: str, name: str) -> str:
    m = re.search(r"^export const meta = \{(.*?)^\}", js, re.S | re.M)
    if not m:
        return "meta block missing or not first"
    if f"name: '{name}'" not in m.group(1):
        return f"meta.name is not '{name}' (must equal the file name)"
    if "${" in m.group(1):
        return "meta must be a pure literal (no template interpolation)"
    return ""


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    check = "--check" in argv
    templates = sorted(TEMPLATES.glob("*.js"))
    if not templates:
        raise SystemExit(f"no templates in {TEMPLATES}")
    OUT.mkdir(exist_ok=True)
    problems = []
    for t in templates:
        js = render(t)
        name = t.stem
        err = meta_ok(js, name) or syntax_ok(js)
        if err:
            problems.append(f"{t.name}: {err}")
            continue
        target = OUT / t.name
        if check:
            if not target.exists() or target.read_text(encoding="utf8") != js:
                problems.append(f"{target.relative_to(REPO)} is stale; run python3 scripts/build_workflows.py")
        else:
            target.write_text(js, encoding="utf8")
            print(f"wrote {target.relative_to(REPO)} ({len(js) // 1024} KB)")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    if check:
        print(f"workflows in sync: {', '.join(t.stem for t in templates)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
