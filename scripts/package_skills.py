#!/usr/bin/env python3
"""Build the SciFi distribution files into dist/. Stdlib only.

Usage:
    python3 scripts/package_skills.py [--out DIR]

Builds:
    dist/scientific-writing.skill   zip, folder scientific-writing/ at the top level (claude.ai upload)
    dist/scifi-lite.skill           zip, folder scifi-lite/ at the top level (claude.ai upload)
    dist/SciFi-dotclaude.zip        .claude/{skills,agents,hooks,scripts,docs/protocol.md} for a
                                    manual copy into a project (then wire hooks with install_local.sh
                                    or by hand: ${CLAUDE_PLUGIN_ROOT} becomes "$CLAUDE_PROJECT_DIR"/.claude)

__pycache__ folders and *.pyc files are skipped. Prints each file's size. Exits 1 when a
source folder is missing (the other files are still built).
"""
import argparse
import os
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"__pycache__", ".git", ".DS_Store"}


def iter_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for f in sorted(filenames):
            if f.endswith(".pyc") or f == ".DS_Store":
                continue
            yield Path(dirpath) / f


def add_tree(zf: zipfile.ZipFile, src: Path, arc_prefix: str, skip=None):
    n = 0
    for f in iter_files(src):
        if skip and any(part in skip for part in f.relative_to(src).parts):
            continue
        arc = f"{arc_prefix}/{f.relative_to(src).as_posix()}"
        info = zipfile.ZipInfo.from_file(f, arc)
        info.compress_type = zipfile.ZIP_DEFLATED
        with open(f, "rb") as fh:
            zf.writestr(info, fh.read())
        n += 1
    return n


def human(size):
    return f"{size / 1024:.1f} KB" if size < 1024 * 1024 else f"{size / 1024 / 1024:.2f} MB"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build dist/*.skill and dist/SciFi-dotclaude.zip")
    ap.add_argument("--out", default=str(REPO / "dist"))
    args = ap.parse_args(argv)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    missing = []
    built = []

    for skill in ["scientific-writing", "scifi-lite"]:
        src = REPO / "skills" / skill
        if not (src / "SKILL.md").is_file():
            missing.append(f"skills/{skill}/SKILL.md")
            continue
        target = out / f"{skill}.skill"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
            n = add_tree(zf, src, skill)
            if skill == "scifi-lite":
                # scifi-lite runs without the rest of the plugin, so it carries its own copy of
                # the standards, the schemas and the protocol under references/.
                std = REPO / "skills" / "scientific-writing"
                n += add_tree(zf, std / "references", f"{skill}/references/standards")
                n += add_tree(zf, std / "examples", f"{skill}/references/standards/examples")
                zf.write(std / "scripts" / "check_manuscript.py", f"{skill}/scripts/check_manuscript.py")
                zf.write(REPO / "scripts" / "validate_json.py", f"{skill}/scripts/validate_json.py")
                n += add_tree(zf, REPO / "scripts" / "schemas", f"{skill}/scripts/schemas")
                zf.write(REPO / "docs" / "protocol.md", f"{skill}/references/protocol.md")
                # global rules: section 2 of the standards SKILL.md
                text = (std / "SKILL.md").read_text(encoding="utf8")
                start = text.find("## 2. Global rules")
                end = text.find("## 3.", start)
                zf.writestr(f"{skill}/references/standards/global-rules.md", "# Global rules (from the scientific-writing skill)\n\n" + text[start:end])
                n += 5
        built.append((target, n))

    target = out / "SciFi-dotclaude.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
        n = 0
        for d in ["skills", "agents", "hooks", "scripts"]:
            src = REPO / d
            if src.is_dir():
                n += add_tree(zf, src, f".claude/{d}", skip={"scifi-lite"})
            else:
                missing.append(d + "/")
        proto = REPO / "docs" / "protocol.md"
        if proto.is_file():
            zf.write(proto, ".claude/docs/protocol.md")
            n += 1
    built.append((target, n))

    for path, n in built:
        print(f"{path}: {human(path.stat().st_size)} ({n} files)")
    if missing:
        print("missing, not packaged: " + ", ".join(missing), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
