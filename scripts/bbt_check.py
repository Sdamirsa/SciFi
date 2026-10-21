#!/usr/bin/env python3
"""Check manuscript citations against the Better BibTeX export. Stdlib only.

Usage:
    python3 ${CLAUDE_PLUGIN_ROOT}/scripts/bbt_check.py [--workspace <path>] [--strict]
    python3 .claude/scripts/bbt_check.py [--workspace <path>] [--strict]   (copied install)

Reads every Manuscript/*.md in the workspace (default: the current directory), finds every
pandoc citation ([@key], [@a; @b, p. 3], narrative @key, suppressed -@key), loads
Literature/library.json (a CSL JSON array, as Better BibTeX's "Better CSL JSON" export writes
it; keys are read from "id" and from "citation-key") and reports:

    MISSING     cited keys that are not in the library
    NO-FULLTEXT cited keys with no Literature/fulltext/<key>.pdf, .md or .txt
    UNCITED     library entries never cited in Manuscript/
    DUPLICATE   keys that occur on more than one library entry

pandoc-crossref labels (@fig:, @tbl:, @sec:, @eq:, @lst:) and text inside code spans or
fenced code blocks are ignored.

Exit codes:
    0  every cited key is in the library (other sections are warnings)
    1  usage or setup error (no Manuscript/, no or unreadable library.json)
    2  at least one cited key is missing from the library
       (with --strict, also any NO-FULLTEXT or DUPLICATE)
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

FULLTEXT_EXT = (".pdf", ".md", ".txt")
CROSSREF_PREFIXES = ("fig:", "tbl:", "sec:", "eq:", "lst:")
# pandoc citation key: starts with a letter, digit or underscore; may contain internal
# punctuation : . # $ % & - + ? < > ~ / ; trailing punctuation is stripped afterwards.
KEY = r"[A-Za-z0-9_][A-Za-z0-9_:.#$%&\-+?<>~/]*"
CITE_RE = re.compile(r"(?<![A-Za-z0-9_@.])-?@(" + KEY + r")")
FENCE_RE = re.compile(r"^(```|~~~).*?^\1", re.S | re.M)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def strip_code(text):
    text = FENCE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def find_citations(text):
    """Return a list of citation keys in order of appearance."""
    keys = []
    for m in CITE_RE.finditer(strip_code(text)):
        key = m.group(1).rstrip(".:#$%&-+?<>~/")
        if not key or key.lower().startswith(CROSSREF_PREFIXES):
            continue
        keys.append(key)
    return keys


def load_library(path):
    data = json.loads(path.read_text(encoding="utf8"))
    if isinstance(data, dict) and isinstance(data.get("items"), list):
        data = data["items"]
    if not isinstance(data, list):
        raise ValueError("expected a CSL JSON array")
    entry_keys = []  # one set of keys per entry
    for i, entry in enumerate(data):
        if not isinstance(entry, dict):
            raise ValueError(f"entry {i} is not an object")
        keys = {str(entry[f]) for f in ("id", "citation-key") if entry.get(f)}
        entry_keys.append(keys)
    return entry_keys


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--workspace", default=".", help="workspace root (default: current directory)")
    ap.add_argument("--strict", action="store_true", help="also fail on missing full texts and duplicate keys")
    args = ap.parse_args()

    ws = Path(args.workspace).resolve()
    ms_dir = ws / "Manuscript"
    lib_path = ws / "Literature" / "library.json"
    ft_dir = ws / "Literature" / "fulltext"

    if not ms_dir.is_dir():
        print(f"setup error: {ms_dir} not found (use --workspace)", file=sys.stderr)
        return 1
    if not lib_path.is_file():
        print(f"setup error: {lib_path} not found. Export the collection as Better CSL JSON "
              "(docs/zotero-guide.md, route B); on the Zotero MCP route keys are resolved by "
              "the agents instead.", file=sys.stderr)
        return 1
    try:
        entry_keys = load_library(lib_path)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"setup error: {lib_path} unreadable: {e}", file=sys.stderr)
        return 1

    cited = defaultdict(list)  # key -> ["file:line", ...]
    for md in sorted(ms_dir.glob("*.md")):
        for n, line in enumerate(strip_code(md.read_text(encoding="utf8")).splitlines(), 1):
            for key in find_citations(line):
                cited[key].append(f"{md.name}:{n}")

    count = Counter(k for keys in entry_keys for k in keys)
    lib_keys = set(count)
    duplicates = sorted(k for k, c in count.items() if c > 1)
    missing = sorted(k for k in cited if k not in lib_keys)
    no_fulltext = sorted(k for k in cited if k in lib_keys
                         and not any((ft_dir / f"{k}{ext}").is_file() for ext in FULLTEXT_EXT))
    uncited = sorted(min(keys) for keys in entry_keys if keys and not keys & set(cited))
    no_key = sum(1 for keys in entry_keys if not keys)

    print(f"workspace: {ws}")
    print(f"cited keys: {len(cited)}  library entries: {len(entry_keys)}")
    sections = [
        ("MISSING (cited, not in library.json)", missing, True),
        ("NO-FULLTEXT (cited, no file in Literature/fulltext/)", no_fulltext, False),
        ("UNCITED (in library.json, never cited)", uncited, False),
        ("DUPLICATE (key on more than one entry)", duplicates, False),
    ]
    for title, keys, show_where in sections:
        print(f"\n{title}: {len(keys)}")
        for k in keys:
            where = f"  ({', '.join(cited[k][:3])}{' ...' if len(cited[k]) > 3 else ''})" if show_where else ""
            print(f"  {k}{where}")
    if no_key:
        print(f"\nwarning: {no_key} library entries have neither 'id' nor 'citation-key'")

    if missing:
        return 2
    if args.strict and (no_fulltext or duplicates):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
