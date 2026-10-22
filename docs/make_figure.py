#!/usr/bin/env python3
"""Draw docs/scifi-system.svg, the system visual used in the README.

Usage: python3 docs/make_figure.py            (writes docs/scifi-system.svg)
Render check: node docs/render_figure.js       (writes docs/scifi-system.png with headless Chromium)

The content comes from docs/anatomy_data.py (shared with make_anatomy.py, the clickable page);
when a skill, agent, hook or workspace file changes, change it there and re-run both. Stdlib only.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from anatomy_data import LOCAL, plain  # noqa: E402

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
text(40, 44, LOCAL["title"], 24, "bold")
text(40, 68, plain(LOCAL["subtitle"]), 12.5, fill=SLATE)

# ------------------------------------------------------------------ left: repo
LX, LY, LW, LH = 40, 92, 520, 1040
box(LX, LY, LW, LH)
text(LX + 16, LY + 26, plain(LOCAL["repo_title"]), 14.5, "bold")
repo = [(ind, plain(n), plain(d)) for ind, n, d in LOCAL["repo"]]
y = LY + 54
for ind, name, desc in repo:
    text(LX + 16, y, ind + name, 12, "bold" if not ind else "normal", mono=True)
    if desc:
        text(LX + (200 if ind else 160), y, desc, 11, fill=SLATE)
    y += 27

# ------------------------------------------------------------------ middle: lanes
MX, MW = 600, 560
L = LOCAL["lanes"]
lanes = [(L["human"]["title"], 110, HUMAN_BG, HUMAN), (L["master"]["title"], 380, MASTER_BG, MASTER),
         (L["agents"]["title"], 690, AGENT_BG, AGENT)]
for name, ly, fill, stroke in lanes:
    box(MX, ly, MW, 245, fill, stroke, 10, 1.5)
    text(MX + 14, ly + 22, name, 12.5, "bold", stroke)

hy = 110
text(MX + 14, hy + 46, L["human"]["heading"], 11.5, "bold")
cmds = [(plain(c), plain(d)) for c, d in LOCAL["lanes"]["human"]["items"]]
for i, (c, d) in enumerate(cmds):
    text(MX + 22, hy + 62 + i * 16, c, 10.5, mono=True)
    text(MX + 290, hy + 62 + i * 16, d, 10.2, fill=SLATE)
for i, n in enumerate(LOCAL["lanes"]["human"]["notes"]):
    text(MX + 14, hy + 196 + i * 17, plain(n), 11, fill="#7a4b00")

my = 380
steps = [(n, plain(name), plain(d)) for n, name, d in LOCAL["lanes"]["master"]["steps"]]
for i, (n, name, desc) in enumerate(steps):
    yy = my + 50 + i * 24
    parts.append(f'<circle cx="{MX + 26}" cy="{yy - 4}" r="9" fill="{MASTER}"/>')
    text(MX + 26, yy, n, 10, "bold", "#fff", "middle")
    text(MX + 44, yy, name, 12, "bold")
    text(MX + 175, yy, desc, 10.8, fill="#333")
for i, n in enumerate(LOCAL["lanes"]["master"]["notes"]):
    text(MX + 14, my + 222 + i * 15, plain(n), 10.8, fill="#1b4b9c")

sy = 690
text(MX + 14, sy + 44, L["agents"]["heading"], 11.5, "bold")
rows = [(plain(a), plain(d)) for a, d in L["agents"]["rows"]]
for i, (a, d) in enumerate(rows):
    yy = sy + 65 + i * 18
    text(MX + 22, yy, a, 11, "bold", mono=True)
    text(MX + 170, yy, d, 10.5, fill="#333")
px = MX + 22
for label, color in L["agents"]["pills"]:
    px += pill(px, sy + 222, label, color) + 8
text(MX + 290, sy + 222, plain(L["agents"]["note"]), 10.3, fill="#1d6b3a")

# arrows between lanes
line(MX + MW / 2 + 60, 355, MX + MW / 2 + 60, 380, HUMAN)
text(MX + MW / 2 + 68, 371, plain(LOCAL["arrows"]["human_to_master"]), 10, fill="#7a4b00")
line(MX + 70, 380, MX + 70, 355, MASTER, dash="4 3")
text(MX + 78, 371, plain(LOCAL["arrows"]["master_to_human"]), 10, fill="#1b4b9c")
line(MX + MW / 2 - 110, 625, MX + MW / 2 - 110, 690, MASTER)
text(MX + MW / 2 - 102, 660, plain(LOCAL["arrows"]["master_to_agents"]), 10, fill="#1b4b9c")
line(MX + MW / 2 + 110, 690, MX + MW / 2 + 110, 625, AGENT)
text(MX + MW / 2 + 118, 660, plain(LOCAL["arrows"]["agents_to_master"]), 10, fill="#1d6b3a")

# ------------------------------------------------------------------ right: workspace
RX, RY, RW = 1200, 92, 460
box(RX, RY, RW, 1030)
text(RX + 16, RY + 26, plain(LOCAL["ws_title"]), 14.5, "bold")
ws = [(ind, plain(n), plain(d)) for ind, n, d in LOCAL["ws"]]
y = RY + 54
for ind, name, desc in ws:
    text(RX + 16, y, ind + name, 11.5, "bold" if not ind else "normal", mono=True)
    if desc:
        text(RX + (262 if ind else 130), y, desc, 10.3, fill=SLATE)
    y += 26
box(RX + 16, RY + 760, RW - 32, 250, "#ffffff", RULE, 6)
text(RX + 28, RY + 782, LOCAL["rules_title"], 12, "bold")
rules = [plain(r) for r in LOCAL["rules"]]
for i, s in enumerate(rules):
    text(RX + 28, RY + 802 + i * 17, s, 10.3, fill="#333")

# lane to column arrows
curve(LX + LW, 320, MX, 230, SLATE, "3 3")
curve(LX + LW, 580, MX, 500, SLATE, "3 3")
curve(LX + LW, 860, MX, 810, SLATE, "3 3")
curve(MX + MW, 200, RX, 150, HUMAN)
text(MX + MW - 8, 194, plain(LOCAL["arrows"]["human_to_ws"]), 9.5, fill="#7a4b00", anchor="end")
curve(MX + MW, 500, RX, 400, MASTER)
text(MX + MW - 8, 494, plain(LOCAL["arrows"]["master_to_ws"]), 9.5, fill="#1b4b9c", anchor="end")
curve(MX + MW, 810, RX, 560, AGENT)
text(MX + MW - 8, 804, plain(LOCAL["arrows"]["agents_to_ws"]), 9.5, fill="#1d6b3a", anchor="end")

text(40, 1155, plain(LOCAL["footer"]), 10.8, fill=SLATE)
parts.append("</svg>")
OUT.write_text("\n".join(parts), encoding="utf8")
print(f"wrote {OUT}")
