#!/usr/bin/env python3
"""Draw docs/scifi-system.svg, the system visual used in the README.

Usage: python3 docs/make_figure.py            (writes docs/scifi-system.svg)
Render check: node docs/render_figure.js       (writes docs/scifi-system.png with headless Chromium)

The content below is the single source of truth for the figure; when a skill, agent, hook or
workspace file changes, change it here and re-run. Stdlib only.
"""
from pathlib import Path

W, H = 1700, 1180
OUT = Path(__file__).resolve().parent / "scifi-system.svg"

INK, SLATE, RULE = "#1c2330", "#5a6472", "#c9d1d9"
HUMAN, MASTER, AGENT = "#b8732a", "#1f5fbf", "#2a8a56"
HUMAN_BG, MASTER_BG, AGENT_BG = "#fff5e8", "#eaf1fd", "#eaf6ee"
MONO = "Menlo, Consolas, 'DejaVu Sans Mono', monospace"
SANS = "Helvetica, Arial, 'DejaVu Sans', sans-serif"

parts = []


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=12, weight="normal", fill=INK, anchor="start", mono=False):
    fam = MONO if mono else SANS
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
                 f'text-anchor="{anchor}" font-family="{fam}">{esc(s)}</text>')


def box(x, y, w, h, fill="#fbfcfe", stroke=RULE, r=8, sw=1.2):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def line(x1, y1, x2, y2, color=SLATE, marker=True, dash="", sw=1.6):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#arr-{color.lstrip("#")})"' if marker else ""
    parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="{sw}" fill="none"{m}{d}/>')


def curve(x1, y1, x2, y2, color=SLATE, dash="", bend=40):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    parts.append(f'<path d="M{x1},{y1} C{x1 + bend},{y1} {x2 - bend},{y2} {x2},{y2}" stroke="{color}" '
                 f'stroke-width="1.6" fill="none" marker-end="url(#arr-{color.lstrip("#")})"{d}/>')


def pill(x, y, label, color):
    w = 7 * len(label) + 14
    parts.append(f'<rect x="{x}" y="{y - 11}" width="{w}" height="15" rx="7" fill="{color}"/>')
    text(x + w / 2, y, label, 9.5, "bold", "#fff", "middle")
    return w


# ------------------------------------------------------------------ header
parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
parts.append("<defs>" + "".join(
    f'<marker id="arr-{c.lstrip("#")}" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">'
    f'<path d="M0,0 L9,4.5 L0,9 z" fill="{c}"/></marker>' for c in (SLATE, HUMAN, MASTER, AGENT)) + "</defs>")
parts.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
text(40, 44, "SciFi: scientific manuscripts from findings to inference", 24, "bold")
text(40, 68, "One repo, three ways to run it (Claude Code plugin, copied .claude/ folder, claude.ai skills). "
             "Three actors. Every handoff is a JSON file in the workspace, validated on write.", 12.5, fill=SLATE)

# ------------------------------------------------------------------ left: repo
LX, LY, LW, LH = 40, 92, 520, 1040
box(LX, LY, LW, LH)
text(LX + 16, LY + 26, "SciFi/  (the repo, github.com/Sdamirsa/SciFi)", 14.5, "bold")
repo = [
    ("", ".claude-plugin/", "plugin.json, marketplace.json"),
    ("", "skills/", ""),
    ("  ", "scifi/", "master orchestrator, entry /scifi, stages.md"),
    ("  ", "scientific-writing/", "the standards from 14 papers, checker, checklist, journals"),
    ("  ", "scifi-spine/", "central claim, gap, results, threads of evidence"),
    ("  ", "scifi-skeleton/", "reverse outline per section from the threads"),
    ("  ", "scifi-paragraph/", "the paragraph loop: map, 5 checks, draft, gate (loop.md)"),
    ("  ", "scifi-figures/", "figure and table brainstorm, captions, corpus figures"),
    ("  ", "scifi-literature/", "scout, notes, ontology, labels, evidence lookup"),
    ("  ", "scifi-review/", "evaluation, comments.json, improvements"),
    ("  ", "scifi-export/", "Word with live Zotero citations, then Google Docs"),
    ("  ", "scifi-stats/", "which biostatistical method, with a complexity guard"),
    ("  ", "scifi-lite/", "single-session version for claude.ai"),
    ("  ", "project-memory/", "the ritual: STATUS, Project-log, LESSONS"),
    ("  ", "panel-discussion/", "decision utility"),
    ("  ", "system-design-review/", "maintainer rubric"),
    ("", "agents/", "12 sub-agents"),
    ("  ", "logic-mapper", "sonnet, medium"),
    ("  ", "flow-checker", "sonnet, medium   internal alignment"),
    ("  ", "local-aligner", "sonnet, medium   previous and next unit"),
    ("  ", "global-aligner", "sonnet, medium   spine, results, skeleton"),
    ("  ", "evidence-checker", "sonnet, medium   claims vs sources and results"),
    ("  ", "style-checker", "sonnet, low      length, standards, script"),
    ("  ", "literature-scout", "sonnet, low      read-only lookup"),
    ("  ", "figure-brainstormer", "sonnet, medium   display-item candidates"),
    ("  ", "drafter", "inherit: your session model"),
    ("  ", "standards-gate", "inherit: one pass, PASS or RETURN"),
    ("  ", "improver", "inherit: accepted comments as diffs"),
    ("  ", "design-reviewer", "inherit: audits SciFi itself"),
    ("", "hooks/", "session-start, validate-json, stop-pointer"),
    ("", "scripts/", "validate_json, state, init_workspace, bbt_check, export_docx, schemas/"),
    ("", "example-workspace/", "the invented echo study, every JSON valid"),
    ("", "docs/", "protocol, workflows, architecture, zotero-guide, this figure"),
    ("", "dist/", "scientific-writing.skill, scifi-lite.skill, SciFi-dotclaude.zip"),
    ("", "research/", "the 28 paper analyses behind the standards"),
]
y = LY + 54
for ind, name, desc in repo:
    text(LX + 16, y, ind + name, 12, "bold" if not ind else "normal", mono=True)
    if desc:
        text(LX + (200 if ind else 160), y, desc, 11, fill=SLATE)
    y += 27

# ------------------------------------------------------------------ middle: lanes
MX, MW = 600, 560
lanes = [("HUMAN", 110, HUMAN_BG, HUMAN), ("MASTER  (your session model: Opus or Fable)", 380, MASTER_BG, MASTER),
         ("SUB-AGENTS  (isolated, one JSON brief in, one JSON envelope out)", 690, AGENT_BG, AGENT)]
for name, ly, fill, stroke in lanes:
    box(MX, ly, MW, 245, fill, stroke, 10, 1.5)
    text(MX + 14, ly + 22, name, 12.5, "bold", stroke)

hy = 110
text(MX + 14, hy + 46, "Types a command or a phrase", 11.5, "bold")
cmds = [("/scifi <workspace> [mode] [journal]", "full pipeline, or resume from STATE.json"),
        ("/scifi-paragraph d03", "one paragraph through the loop"),
        ("/scifi-review [file]", "evaluate, comment, optionally improve"),
        ("/scifi-figures", "brainstorm figures and tables"),
        ("/scifi-literature", "library, notes, ontology, labels"),
        ("/scifi-export --library users/<id>", "docx with live Zotero citations"),
        ("/scifi-stats", "analysis plan: the standard method for the question"),
        ("/project-memory", "end-of-session ritual, user only")]
for i, (c, d) in enumerate(cmds):
    text(MX + 22, hy + 62 + i * 16, c, 10.5, mono=True)
    text(MX + 290, hy + 62 + i * 16, d, 10.2, fill=SLATE)
text(MX + 14, hy + 196, "Decides at gates: picks one option, approves diffs, answers NEED requests.", 11, fill="#7a4b00")
text(MX + 14, hy + 213, "Owns Manuscript/ and Literature/. The system reads them and never edits them.", 11, fill="#7a4b00")
text(MX + 14, hy + 230, "Modes: co-thinker (default), human-on-the-loop, human-in-the-loop, fully-automated.", 11, fill="#7a4b00")

my = 380
steps = [("0", "resume", "state.py session; read STATE.json and the last decisions"),
         ("1", "spine", "claim, gap, results R1.., threads T1..  spine.json"),
         ("2", "skeleton", "units with takeaway and thread  skeleton.json"),
         ("3", "figures", "display-item plan, caption units  figures.json"),
         ("4", "paragraph loop", "brief, store envelopes, synthesis, draft, gate"),
         ("5", "review", "section and manuscript gates, comments/*.json"),
         ("6", "ritual and export", "/project-memory (user), /scifi-export")]
for i, (n, name, desc) in enumerate(steps):
    yy = my + 50 + i * 24
    parts.append(f'<circle cx="{MX + 26}" cy="{yy - 4}" r="9" fill="{MASTER}"/>')
    text(MX + 26, yy, n, 10, "bold", "#fff", "middle")
    text(MX + 44, yy, name, 12, "bold")
    text(MX + 175, yy, desc, 10.8, fill="#333")
text(MX + 14, my + 222, "Only writer of STATE.json, spine, skeleton, figures, syntheses and the decisions log,", 10.8, fill="#1b4b9c")
text(MX + 14, my + 237, "through state.py. Reads one unit, its logic.json and five envelopes at a time.", 10.8, fill="#1b4b9c")

sy = 690
text(MX + 14, sy + 44, "The paragraph loop for one unit", 11.5, "bold")
rows = [("logic-mapper", "claims, evidence, steps of the text  units/<id>.logic.json"),
        ("flow-checker", "internal: one point, context first, takeaway last, old to new"),
        ("local-aligner", "neighbours: redundancy, pre-emption, bridge, single home"),
        ("global-aligner", "spine and results: serves the claim, same gap, no new data"),
        ("evidence-checker", "each claim vs cited source, our results, or a logical step"),
        ("style-checker", "runs check_manuscript.py, then the section standards"),
        ("drafter", "redrafts from logic.json and the accepted findings  units/<id>.draft.md"),
        ("standards-gate", "one pass: PASS, or RETURN with three blockers")]
for i, (a, d) in enumerate(rows):
    yy = sy + 65 + i * 18
    text(MX + 22, yy, a, 11, "bold", mono=True)
    text(MX + 170, yy, d, 10.5, fill="#333")
pill(MX + 22, sy + 222, "sonnet medium", "#5a8f6a"); pill(MX + 130, sy + 222, "sonnet low", "#7a9d85"); pill(MX + 215, sy + 222, "inherit", "#2a8a56")
text(MX + 290, sy + 222, "five checks run in parallel; the two inherit agents run after", 10.3, fill="#1d6b3a")

# arrows between lanes
line(MX + MW / 2 + 60, 355, MX + MW / 2 + 60, 380, HUMAN)
text(MX + MW / 2 + 68, 371, "command, mode, journal", 10, fill="#7a4b00")
line(MX + 70, 380, MX + 70, 355, MASTER, dash="4 3")
text(MX + 78, 371, "options with one pick at each gate", 10, fill="#1b4b9c")
line(MX + MW / 2 - 110, 625, MX + MW / 2 - 110, 690, MASTER)
text(MX + MW / 2 - 102, 660, "briefs/<task>.json", 10, fill="#1b4b9c")
line(MX + MW / 2 + 110, 690, MX + MW / 2 + 110, 625, AGENT)
text(MX + MW / 2 + 118, 660, "envelope JSON, stored in handshakes/", 10, fill="#1d6b3a")

# ------------------------------------------------------------------ right: workspace
RX, RY, RW = 1200, 92, 460
box(RX, RY, RW, 1030)
text(RX + 16, RY + 26, "<your-paper>/  (the workspace)", 14.5, "bold")
ws = [
    ("", "Manuscript/", "YOU write here, pandoc [@citekey]"),
    ("  ", "title.md  abstract.md  introduction.md", ""),
    ("  ", "methods.md  results.md  discussion.md", ""),
    ("  ", "figures/  tables/", "your drafts, data, images"),
    ("", "Literature/", "YOU provide"),
    ("  ", "library.json", "Better CSL JSON (citation keys)"),
    ("  ", "library.bbt.json", "Better BibTeX JSON (item keys)"),
    ("  ", "fulltext/<citekey>.pdf|.md", "the cited papers"),
    ("  ", "notes/  ontology.yaml  labels/", "written by scifi-literature only"),
    ("", "Thinking-space/", "SYSTEM owns, all validated JSON"),
    ("  ", "STATE.json", "stage, mode, journal, next action"),
    ("  ", "analysis-plan.md", "question, data, method, what is reported"),
    ("  ", "spine.json", "claim, gap, results, implications, threads"),
    ("  ", "skeleton.json", "units per section, takeaway, thread"),
    ("  ", "figures.json", "display-item plan and captions"),
    ("  ", "units/<id>.logic.json, .draft.md", "one unit's logic and drafts"),
    ("  ", "briefs/<task>.json", "what the master sent"),
    ("  ", "handshakes/<task>.json", "what the agent returned"),
    ("  ", "handshakes/<id>.synthesis.r<n>.json", "the master's decisions"),
    ("  ", "comments/<id>.json", "review comments with severity and fix"),
    ("  ", "log/decisions.jsonl", "append-only: who decided what, why"),
    ("  ", "scratch/", "option exploration, inspectable"),
    ("", "export/", "docx with Zotero markers, report"),
    ("", ".claude/", "memory spine (minimal dot-claude-iff)"),
    ("  ", "STATUS.md", "read first; rewritten by the ritual"),
    ("  ", "Project-log.jsonl", "one line per real thing"),
    ("  ", "LESSONS.jsonl", "mistakes with a checkable prevention"),
]
y = RY + 54
for ind, name, desc in ws:
    text(RX + 16, y, ind + name, 11.5, "bold" if not ind else "normal", mono=True)
    if desc:
        text(RX + (262 if ind else 130), y, desc, 10.3, fill=SLATE)
    y += 26
box(RX + 16, RY + 760, RW - 32, 250, "#ffffff", RULE, 6)
text(RX + 28, RY + 782, "Rules that hold everywhere", 12, "bold")
rules = ["Human owns Manuscript/ and Literature/; the system never edits them.",
         "Master owns Thinking-space/ and is the only writer of shared files.",
         "Sub-agents read only the paths in their brief and return one envelope.",
         "validate-json rejects any malformed JSON on write (exit 2).",
         "No number that is not in results.md; no source that is not in the library.",
         "A missing source is a NEED, never a guess. A missing envelope is not a pass.",
         "Resume = STATE.json, then the tail of log/decisions.jsonl.",
         "Accepted units are never redrafted; human edits are never overwritten.",
         "Standards: sentences 15 to 30 words, no colons, semicolons or dashes,",
         "no promotional words, every claim with its evidence in the same sentence."]
for i, s in enumerate(rules):
    text(RX + 28, RY + 802 + i * 17, s, 10.3, fill="#333")

# lane to column arrows
curve(LX + LW, 320, MX, 230, SLATE, "3 3")
curve(LX + LW, 580, MX, 500, SLATE, "3 3")
curve(LX + LW, 860, MX, 810, SLATE, "3 3")
curve(MX + MW, 200, RX, 150, HUMAN)
text(MX + MW - 8, 194, "manuscript, papers", 9.5, fill="#7a4b00", anchor="end")
curve(MX + MW, 500, RX, 400, MASTER)
text(MX + MW - 8, 494, "reads and writes", 9.5, fill="#1b4b9c", anchor="end")
curve(MX + MW, 810, RX, 560, AGENT)
text(MX + MW - 8, 804, "envelopes, unit files", 9.5, fill="#1d6b3a", anchor="end")

text(40, 1155, "Run it: /plugin marketplace add Sdamirsa/SciFi, then /plugin install scifi@scifi (Claude Code); scripts/install_local.sh <project> to copy into .claude/; "
               "dist/scifi-lite.skill and dist/scientific-writing.skill for claude.ai.", 10.8, fill=SLATE)
parts.append("</svg>")
OUT.write_text("\n".join(parts), encoding="utf8")
print(f"wrote {OUT}")
