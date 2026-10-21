#!/usr/bin/env python3
"""Validate a SciFi JSON artifact against its schema. Stdlib only.

Usage:
    python3 validate_json.py <file.json> [--schema <name>] [--quiet]

The schema is inferred from the path when --schema is omitted:
    briefs/*.json            -> brief
    handshakes/*.json        -> envelope   (except *.synthesis.json -> synthesis)
    units/*.logic.json       -> logic
    spine.json               -> spine
    skeleton.json            -> skeleton
    figures.json             -> figures
    comments/*.json          -> comments
    STATE.json               -> state

Exit 0 when valid, 2 when invalid (the hook uses exit 2 to block the write), 1 on usage error.
Supports the subset of JSON Schema the SciFi schemas use: type, required, properties, items,
enum, pattern, description. Unknown keys are allowed unless additionalProperties is false.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCHEMA_DIR = HERE / "schemas"

TYPES = {"object": dict, "array": list, "string": str, "integer": int, "number": (int, float), "boolean": bool, "null": type(None)}


def infer_schema(path: Path):
    name = path.name
    parent = path.parent.name
    if ".synthesis." in name:
        return "synthesis"
    if name.endswith(".logic.json"):
        return "logic"
    if name == "STATE.json":
        return "state"
    if name in ("spine.json", "skeleton.json", "figures.json"):
        return name[:-5]
    if parent == "briefs":
        return "brief"
    if parent == "handshakes":
        return "envelope"
    if parent == "comments":
        return "comments"
    return None


def validate(instance, schema, path="$", errors=None):
    if errors is None:
        errors = []
    t = schema.get("type")
    if t:
        expected = TYPES.get(t)
        if expected is not None:
            if t == "integer" and isinstance(instance, bool):
                errors.append(f"{path}: expected integer, got boolean")
            elif not isinstance(instance, expected):
                errors.append(f"{path}: expected {t}, got {type(instance).__name__}")
                return errors
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} not in {schema['enum']}")
    if "pattern" in schema and isinstance(instance, str) and not re.search(schema["pattern"], instance):
        errors.append(f"{path}: {instance!r} does not match {schema['pattern']}")
    if isinstance(instance, dict):
        for req in schema.get("required", []):
            if req not in instance:
                errors.append(f"{path}: missing required key '{req}'")
        props = schema.get("properties", {})
        for k, v in instance.items():
            if k in props:
                validate(v, props[k], f"{path}.{k}", errors)
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}: unexpected key '{k}'")
    if isinstance(instance, list) and "items" in schema:
        for i, item in enumerate(instance):
            validate(item, schema["items"], f"{path}[{i}]", errors)
    return errors


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    quiet = "--quiet" in args
    schema_name = None
    if "--schema" in args:
        schema_name = args[args.index("--schema") + 1]
    files = [a for a in args if a.endswith(".json") and not a.startswith("--") and (schema_name is None or a != schema_name)]
    if not files:
        print("no json file given", file=sys.stderr)
        sys.exit(1)
    worst = 0
    for f in files:
        p = Path(f)
        name = schema_name or infer_schema(p)
        if name is None:
            if not quiet:
                print(f"{p}: no schema inferred, skipped")
            continue
        sp = SCHEMA_DIR / f"{name}.schema.json"
        if not sp.exists():
            print(f"{p}: schema '{name}' not found in {SCHEMA_DIR}", file=sys.stderr)
            worst = max(worst, 1)
            continue
        try:
            inst = json.loads(p.read_text(encoding="utf8"))
        except Exception as e:
            print(f"{p}: not valid JSON: {e}", file=sys.stderr)
            worst = 2
            continue
        errs = validate(inst, json.loads(sp.read_text(encoding="utf8")))
        if errs:
            print(f"{p}: INVALID against {name}.schema.json", file=sys.stderr)
            for e in errs[:20]:
                print(f"  - {e}", file=sys.stderr)
            worst = 2
        elif not quiet:
            print(f"{p}: valid ({name})")
    sys.exit(worst)


if __name__ == "__main__":
    main()
