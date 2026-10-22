#!/usr/bin/env python3
"""Version and release SciFi. Stdlib only; git and gh must be on PATH for tag and publish.

Usage:
    python3 scripts/release.py check                 verify everything a release needs (no changes)
    python3 scripts/release.py bump <patch|minor|major|X.Y.Z>
                                                     set the version everywhere, open a CHANGELOG
                                                     heading, rebuild docs/ figures and dist/
    python3 scripts/release.py tag                   annotated tag v<version> from the CHANGELOG section
    python3 scripts/release.py publish               push main and the tag, create the GitHub release
                                                     with dist/* attached (needs gh auth)

The version lives in .claude-plugin/plugin.json; marketplace.json carries it twice and must
match. A release is the tag v<version> plus a GitHub release whose assets are the three dist
files, so claude.ai users download from the release page and plugin users install the tag.

check fails (exit 1) when: versions disagree; CHANGELOG.md has no "## <version>" heading;
the unit tests or the example-workspace validation fail; the anatomy page has a dead link;
dist/ or docs/ are not rebuilt from the current sources; the working tree is dirty; or the
tag already exists. bump refuses a version that is not greater than the current one.
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PLUGIN = REPO / ".claude-plugin" / "plugin.json"
MARKET = REPO / ".claude-plugin" / "marketplace.json"
CHANGELOG = REPO / "CHANGELOG.md"
DIST = ["dist/scientific-writing.skill", "dist/scifi-lite.skill", "dist/SciFi-dotclaude.zip"]


def run(cmd, check=True, capture=True):
    r = subprocess.run(cmd, cwd=REPO, text=True, capture_output=capture)
    if check and r.returncode != 0:
        raise SystemExit(f"failed: {' '.join(cmd)}\n{r.stdout if capture else ''}{r.stderr if capture else ''}")
    return r


def version():
    return json.loads(PLUGIN.read_text())["version"]


def versions_everywhere():
    m = json.loads(MARKET.read_text())
    return {"plugin.json": version(), "marketplace.metadata": m["metadata"]["version"],
            "marketplace.plugins[0]": m["plugins"][0]["version"]}


def changelog_section(v):
    text = CHANGELOG.read_text(encoding="utf8")
    m = re.search(rf"^## {re.escape(v)}\b[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else None


def rebuild():
    run([sys.executable, "docs/make_figure.py"])
    run([sys.executable, "docs/make_anatomy.py", "--check"])
    run([sys.executable, "scripts/package_skills.py"])


def check(args):
    problems = []
    vs = versions_everywhere()
    v = vs["plugin.json"]
    if len(set(vs.values())) != 1:
        problems.append("versions disagree: " + ", ".join(f"{k}={x}" for k, x in vs.items()))
    if not re.fullmatch(r"\d+\.\d+\.\d+", v):
        problems.append(f"version {v} is not X.Y.Z")
    sec = changelog_section(v)
    if sec is None:
        problems.append(f"CHANGELOG.md has no '## {v}' heading")
    elif not sec:
        problems.append(f"CHANGELOG.md section {v} is empty")
    r = run([sys.executable, "-m", "unittest", "discover", "-s", "scripts/tests"], check=False)
    if r.returncode != 0:
        problems.append("unit tests fail:\n" + r.stderr[-1500:])
    for f in sorted((REPO / "example-workspace").rglob("*.json")):
        r = run([sys.executable, "scripts/validate_json.py", str(f)], check=False)
        if r.returncode != 0:
            problems.append(f"invalid JSON: {f.relative_to(REPO)}: {r.stdout.strip()}{r.stderr.strip()}")
    r = run([sys.executable, "docs/make_anatomy.py", "--check"], check=False)
    if r.returncode != 0:
        problems.append("anatomy page: " + r.stderr.strip())
    if not args.no_rebuild:
        run([sys.executable, "docs/make_figure.py"])
        run([sys.executable, "scripts/package_skills.py"])
    dirty = run(["git", "status", "--porcelain"]).stdout.strip()
    if dirty:
        problems.append("working tree not clean (rebuild docs/ and dist/, then commit):\n" + dirty)
    if run(["git", "tag", "-l", f"v{v}"]).stdout.strip():
        problems.append(f"tag v{v} already exists")
    for d in DIST:
        if not (REPO / d).is_file():
            problems.append(f"missing {d}")
    if problems:
        print(f"release check for {v}: {len(problems)} problem(s)\n- " + "\n- ".join(problems))
        return 1
    print(f"release check for {v}: ok")
    return 0


def bump(args):
    cur = version()
    major, minor, patch = (int(x) for x in cur.split("."))
    if args.level == "patch":
        new = f"{major}.{minor}.{patch + 1}"
    elif args.level == "minor":
        new = f"{major}.{minor + 1}.0"
    elif args.level == "major":
        new = f"{major + 1}.0.0"
    elif re.fullmatch(r"\d+\.\d+\.\d+", args.level):
        new = args.level
    else:
        raise SystemExit("bump takes patch, minor, major or X.Y.Z")
    if tuple(int(x) for x in new.split(".")) <= (major, minor, patch):
        raise SystemExit(f"{new} is not greater than {cur}")
    for path in (PLUGIN, MARKET):
        text = path.read_text(encoding="utf8")
        text = text.replace(f'"version": "{cur}"', f'"version": "{new}"')
        path.write_text(text, encoding="utf8")
    today = dt.date.today().isoformat()
    text = CHANGELOG.read_text(encoding="utf8")
    if re.search(rf"^## {re.escape(new)}\b", text, re.M):
        text = re.sub(rf"^## {re.escape(new)}\s*$", f"## {new} ({today})", text, count=1, flags=re.M)
    else:
        text = text.replace("## Planned", f"## {new} ({today})\n\n- \n\n## Planned", 1)
    CHANGELOG.write_text(text, encoding="utf8")
    rebuild()
    print(f"{cur} -> {new}; edit the CHANGELOG section, commit, then run check and tag")
    return 0


def tag(args):
    if check(argparse.Namespace(no_rebuild=True)) != 0:
        return 1
    v = version()
    notes = f"SciFi {v}\n\n{changelog_section(v)}\n"
    run(["git", "tag", "-a", f"v{v}", "-m", notes])
    print(f"tagged v{v}; next: python3 scripts/release.py publish")
    return 0


def publish(args):
    v = version()
    if not run(["git", "tag", "-l", f"v{v}"]).stdout.strip():
        raise SystemExit(f"tag v{v} missing; run tag first")
    run(["git", "push", "origin", "main"], capture=False)
    run(["git", "push", "origin", f"v{v}"], capture=False)
    notes = REPO / "dist" / f"release-notes-{v}.md"
    notes.write_text(f"{changelog_section(v)}\n\nInstall: see README. Assets: the two claude.ai skills and the .claude/ zip.\n", encoding="utf8")
    try:
        exists = run(["gh", "release", "view", f"v{v}"], check=False).returncode == 0
        if exists:
            run(["gh", "release", "upload", "--clobber", f"v{v}", *DIST], capture=False)
        else:
            run(["gh", "release", "create", f"v{v}", *DIST, "--title", f"SciFi {v}", "--notes-file", str(notes)], capture=False)
    finally:
        notes.unlink(missing_ok=True)
    print(f"released v{v}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check"); c.add_argument("--no-rebuild", action="store_true", help="do not rebuild docs/ and dist/ before the clean-tree test")
    b = sub.add_parser("bump"); b.add_argument("level")
    sub.add_parser("tag")
    sub.add_parser("publish")
    args = ap.parse_args(argv)
    return {"check": check, "bump": bump, "tag": tag, "publish": publish}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
