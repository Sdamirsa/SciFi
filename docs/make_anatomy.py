#!/usr/bin/env python3
"""Write docs/index.html, the clickable anatomy of SciFi (served by GitHub Pages).

Usage: python3 docs/make_anatomy.py            (writes docs/index.html)
Check: python3 docs/make_anatomy.py --check    (also verifies every link target exists in the repo)

Same layout and content as docs/scifi-system.svg (both read docs/anatomy_data.py), with a toggle
between the Claude Code view and the claude.ai view. Every name opens its file or folder on
GitHub; every description opens the rule, schema or document behind it. Stdlib only. Exits 1
when --check finds a link whose target is missing.
"""
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from anatomy_data import GITHUB, VIEWS, all_hrefs, plain  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "docs" / "index.html"
VERSION = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text())["version"]


def gh(href):
    path, _, anchor = href.partition("#")
    if path == "":
        url = GITHUB
    elif (REPO / path).is_dir():
        url = f"{GITHUB}/tree/main/{path}"
    else:
        url = f"{GITHUB}/blob/main/{path}"
    return url + (f"#{anchor}" if anchor else "")


def spans(sp, cls=""):
    out = []
    for text, href in sp:
        t = html.escape(text)
        if href is None:
            out.append(t)
        else:
            c = f' class="{cls}"' if cls else ""
            out.append(f'<a href="{gh(href)}"{c} target="_blank" rel="noopener">{t}</a>')
    return "".join(out)


def rows(items, name_cls="name", desc_cls="desc"):
    out = []
    for ind, name, desc in items:
        lvl = len(ind) // 2
        d = f'<span class="{desc_cls}">{spans(desc)}</span>' if plain(desc) else ""
        out.append(f'<div class="row lvl{lvl}"><span class="{name_cls}">{spans(name)}</span>{d}</div>')
    return "\n".join(out)


def check_links():
    missing = []
    for href in all_hrefs():
        path, _, anchor = href.partition("#")
        target = REPO / path if path else REPO
        if not target.exists():
            missing.append(href)
            continue
        if anchor:
            text = target.read_text(encoding="utf8", errors="replace")
            slugs = set()
            for line in text.splitlines():
                m = re.match(r"#{1,6}\s+(.*)", line)
                if m:
                    s = m.group(1).strip().lower()
                    s = re.sub(r"[^\w\- ]", "", s).replace(" ", "-")
                    slugs.add(s)
            if anchor not in slugs:
                missing.append(href)
    return missing


def view_html(v):
    L = v["lanes"]
    k = v["key"]
    human_items = "\n".join(
        f'<div class="cmd"><span class="mono">{spans(c)}</span><span class="desc">{spans(d)}</span></div>'
        for c, d in L["human"]["items"])
    human_notes = "\n".join(f'<p class="note human-note">{spans(n)}</p>' for n in L["human"]["notes"])
    steps = "\n".join(
        f'<div class="step"><span class="num">{n}</span><span class="step-name">{spans(name)}</span>'
        f'<span class="desc dark">{spans(d)}</span></div>' for n, name, d in L["master"]["steps"])
    master_notes = "\n".join(f'<p class="note master-note">{spans(n)}</p>' for n in L["master"]["notes"])
    agent_rows = "\n".join(
        f'<div class="agent"><span class="mono bold">{spans(a)}</span><span class="desc dark">{spans(d)}</span></div>'
        for a, d in L["agents"]["rows"])
    pills = "".join(f'<a class="pill" style="background:{c}" href="{gh(L["agents"]["pills_href"])}" target="_blank" rel="noopener">{html.escape(t)}</a>'
                    for t, c in L["agents"]["pills"])
    A = v["arrows"]
    rules = "\n".join(f"<li>{spans(r)}</li>" for r in v["rules"])
    return f'''
<section class="view" id="view-{k}" data-view="{k}">
  <p class="subtitle">{spans(v["subtitle"])}</p>
  <div class="cols">
    <div class="col box">
      <h2 class="col-title">{spans(v["repo_title"])}</h2>
      <div class="rows">
{rows(v["repo"])}
      </div>
      <p class="col-foot">&#8594; {spans(A["repo_to_lanes"])}</p>
    </div>

    <div class="col lanes">
      <div class="lane human">
        <div class="lane-head"><h2>{html.escape(L["human"]["title"])}</h2><span class="to-ws human-ink">{spans(A["human_to_ws"])} &#8594;</span></div>
        <h3>{html.escape(L["human"]["heading"])}</h3>
        <div class="cmds">
{human_items}
        </div>
{human_notes}
      </div>
      <div class="between">
        <span class="master-ink dashed">&#8593; {spans(A["master_to_human"])}</span>
        <span class="human-ink">{spans(A["human_to_master"])} &#8595;</span>
      </div>
      <div class="lane master">
        <div class="lane-head"><h2>{html.escape(L["master"]["title"])}</h2><span class="to-ws master-ink">{spans(A["master_to_ws"])} &#8594;</span></div>
        <div class="steps">
{steps}
        </div>
{master_notes}
      </div>
      <div class="between">
        <span class="master-ink">{spans(A["master_to_agents"])} &#8595;</span>
        <span class="agent-ink">&#8593; {spans(A["agents_to_master"])}</span>
      </div>
      <div class="lane agents">
        <div class="lane-head"><h2>{html.escape(L["agents"]["title"])}</h2><span class="to-ws agent-ink">{spans(A["agents_to_ws"])} &#8594;</span></div>
        <h3>{html.escape(L["agents"]["heading"])}</h3>
        <div class="agent-rows">
{agent_rows}
        </div>
        <p class="pills">{pills}<span class="agent-ink pill-note">{spans(L["agents"]["note"])}</span></p>
      </div>
    </div>

    <div class="col box">
      <h2 class="col-title">{spans(v["ws_title"])}</h2>
      <div class="rows ws">
{rows(v["ws"])}
      </div>
      <div class="rules">
        <h3>{html.escape(v["rules_title"])}</h3>
        <ul>
{rules}
        </ul>
      </div>
    </div>
  </div>
  <p class="footer">{spans(v["footer"])}</p>
</section>'''


def page():
    tabs = "".join(
        f'<button type="button" role="tab" id="tab-{v["key"]}" data-view="{v["key"]}" aria-selected="{"true" if i == 0 else "false"}" '
        f'aria-controls="view-{v["key"]}">{html.escape(v["label"])}</button>' for i, v in enumerate(VIEWS))
    views = "\n".join(view_html(v) for v in VIEWS)
    return f'''<title>SciFi Anatomy</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="The anatomy of SciFi: repo, actors and workspace, every node linked to its file. Toggle between the Claude Code plugin and the claude.ai skills.">
<style>
/* Layout: the system figure as three columns (repo, three actor lanes, workspace); stacks to one column on phones. */
:root {{
  --bg: #ffffff; --fg: #1c2330; --slate: #5a6472; --rule: #c9d1d9; --panel: #fbfcfe; --dark-text: #333333;
  --human: #b8732a; --human-bg: #fff5e8; --human-ink: #7a4b00;
  --master: #1f5fbf; --master-bg: #eaf1fd; --master-ink: #1b4b9c;
  --agent: #2a8a56; --agent-bg: #eaf6ee; --agent-ink: #1d6b3a;
  --link-line: rgba(28, 35, 48, 0.28); --focus: #1f5fbf; --tab-bg: #f0f3f7;
  --mono: Menlo, Consolas, "DejaVu Sans Mono", ui-monospace, monospace;
  --sans: Helvetica, Arial, "DejaVu Sans", system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #0f141b; --fg: #e6ebf0; --slate: #9aa6b4; --rule: #2b3542; --panel: #141b24; --dark-text: #cfd6de;
  --human: #d4924a; --human-bg: #2a2015; --human-ink: #f0c68a;
  --master: #5b8fe6; --master-bg: #141f33; --master-ink: #a9c4f5;
  --agent: #4fb27c; --agent-bg: #132619; --agent-ink: #9fdcb8;
  --link-line: rgba(230, 235, 240, 0.3); --focus: #8fb4f0; --tab-bg: #1a222c; color-scheme: dark;
}} }}
:root[data-theme="dark"] {{
  --bg: #0f141b; --fg: #e6ebf0; --slate: #9aa6b4; --rule: #2b3542; --panel: #141b24; --dark-text: #cfd6de;
  --human: #d4924a; --human-bg: #2a2015; --human-ink: #f0c68a;
  --master: #5b8fe6; --master-bg: #141f33; --master-ink: #a9c4f5;
  --agent: #4fb27c; --agent-bg: #132619; --agent-ink: #9fdcb8;
  --link-line: rgba(230, 235, 240, 0.3); --focus: #8fb4f0; --tab-bg: #1a222c; color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ background: var(--bg); color: var(--fg); font-family: var(--sans); font-size: 13px; line-height: 1.45;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 20px 28px; }}
a {{ color: inherit; text-decoration: underline; text-decoration-color: var(--link-line); text-decoration-thickness: 1px; text-underline-offset: 2px; }}
a:hover {{ text-decoration-color: currentColor; }}
a:focus-visible, button:focus-visible {{ outline: 2px solid var(--focus); outline-offset: 2px; border-radius: 3px; }}
.wrap {{ max-width: 1660px; margin: 0 auto; }}
header {{ display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px 16px; margin-bottom: 4px; }}
h1 {{ font-size: 24px; margin: 0; font-weight: 700; letter-spacing: -0.01em; text-wrap: balance; }}
.version {{ font-family: var(--mono); font-size: 11.5px; color: var(--slate); }}
.tabs {{ margin-left: auto; display: inline-flex; border: 1px solid var(--rule); border-radius: 8px; overflow: hidden; background: var(--tab-bg); }}
.tabs button {{ font: inherit; font-size: 12px; font-weight: 600; color: var(--slate); background: transparent; border: 0; padding: 7px 12px; cursor: pointer; }}
.tabs button[aria-selected="true"] {{ background: var(--bg); color: var(--fg); box-shadow: inset 0 0 0 1px var(--rule); }}
.subtitle {{ color: var(--slate); font-size: 12.5px; margin: 0 0 14px; max-width: 1100px; }}
.cols {{ display: grid; grid-template-columns: minmax(0, 10fr) minmax(0, 11fr) minmax(0, 9fr); gap: 18px; align-items: start; }}
.col {{ min-width: 0; }}
.box {{ background: var(--panel); border: 1px solid var(--rule); border-radius: 8px; padding: 14px 16px 12px; }}
.col-title {{ font-size: 14.5px; font-weight: 700; margin: 0 0 12px; font-family: var(--mono); }}
.col-title a {{ font-family: var(--mono); }}
.rows {{ display: flex; flex-direction: column; gap: 5px; }}
.row {{ display: grid; grid-template-columns: minmax(118px, max-content) minmax(0, 1fr); column-gap: 12px; align-items: baseline; }}
.rows.ws .row {{ grid-template-columns: minmax(150px, max-content) minmax(0, 1fr); }}
.row.lvl1 {{ padding-left: 14px; }}
.row.lvl2 {{ padding-left: 28px; }}
.name {{ font-family: var(--mono); font-size: 12px; font-weight: 700; white-space: nowrap; }}
.lvl1 .name, .lvl2 .name {{ font-weight: 400; }}
.desc {{ color: var(--slate); font-size: 11px; min-width: 0; white-space: pre-wrap; }}
.desc.dark {{ color: var(--dark-text); }}
.mono {{ font-family: var(--mono); font-size: 11px; }}
.bold {{ font-weight: 700; }}
.col-foot {{ color: var(--slate); font-size: 11px; margin: 14px 0 0; border-top: 1px dashed var(--rule); padding-top: 8px; }}
.lanes {{ display: flex; flex-direction: column; gap: 0; }}
.lane {{ border-radius: 10px; border: 1.5px solid; padding: 12px 14px 12px; }}
.lane.human {{ background: var(--human-bg); border-color: var(--human); }}
.lane.master {{ background: var(--master-bg); border-color: var(--master); }}
.lane.agents {{ background: var(--agent-bg); border-color: var(--agent); }}
.lane-head {{ display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: 4px 12px; margin-bottom: 10px; }}
.lane h2 {{ font-size: 12.5px; margin: 0; font-weight: 700; }}
.human h2 {{ color: var(--human); }} .master h2 {{ color: var(--master); }} .agents h2 {{ color: var(--agent); }}
.lane h3 {{ font-size: 11.5px; font-weight: 700; margin: 0 0 6px; }}
.to-ws {{ font-size: 10px; white-space: nowrap; }}
.human-ink {{ color: var(--human-ink); }} .master-ink {{ color: var(--master-ink); }} .agent-ink {{ color: var(--agent-ink); }}
.cmds, .steps, .agent-rows {{ display: flex; flex-direction: column; gap: 4px; margin-bottom: 10px; }}
.cmd, .agent {{ display: grid; grid-template-columns: minmax(130px, max-content) minmax(0, 1fr); column-gap: 12px; align-items: baseline; }}
.cmd .desc {{ font-size: 10.5px; }}
.step {{ display: grid; grid-template-columns: 18px minmax(96px, max-content) minmax(0, 1fr); column-gap: 8px; align-items: baseline; }}
.num {{ display: inline-flex; width: 18px; height: 18px; border-radius: 50%; background: var(--master); color: #fff; font-size: 10px; font-weight: 700; align-items: center; justify-content: center; align-self: center; }}
.step-name {{ font-weight: 700; font-size: 12px; }}
.step .desc {{ font-size: 10.8px; }}
.agent .desc {{ font-size: 10.5px; }}
.note {{ font-size: 11px; margin: 3px 0 0; }}
.master-note {{ font-size: 10.8px; }}
.between {{ display: flex; justify-content: space-between; flex-wrap: wrap; gap: 4px 16px; font-size: 10px; padding: 7px 18px; }}
.dashed {{ opacity: 0.9; }}
.pills {{ display: flex; flex-wrap: wrap; align-items: center; gap: 6px 8px; margin: 2px 0 0; }}
.pill {{ color: #fff; font-size: 9.5px; font-weight: 700; padding: 2px 8px; border-radius: 8px; text-decoration: none; line-height: 1.3; }}
.pill:hover {{ text-decoration: underline; }}
.pill-note {{ font-size: 10.3px; margin-left: 4px; }}
.rules {{ background: var(--bg); border: 1px solid var(--rule); border-radius: 6px; padding: 10px 12px 8px; margin-top: 16px; }}
.rules h3 {{ font-size: 12px; margin: 0 0 6px; }}
.rules ul {{ margin: 0; padding-left: 16px; font-size: 10.5px; color: var(--dark-text); }}
.rules li {{ margin: 2px 0; }}
.footer {{ color: var(--slate); font-size: 11px; margin: 16px 0 0; }}
@media (max-width: 1100px) {{
  .cols {{ grid-template-columns: 1fr; }}
  .name, .to-ws {{ white-space: normal; }}
}}
@media (max-width: 560px) {{
  .row, .cmd, .agent {{ grid-template-columns: 1fr; row-gap: 1px; }}
  .step {{ grid-template-columns: 18px minmax(0, 1fr); }}
  .step .desc {{ grid-column: 2; }}
  .rows.ws .row {{ grid-template-columns: 1fr; }}
  .tabs {{ margin-left: 0; }}
  h1 {{ font-size: 20px; }}
}}
@media (prefers-reduced-motion: no-preference) {{ .tabs button {{ transition: background 0.15s; }} }}
</style>
<div class="wrap">
  <header>
    <h1 id="page-title">{html.escape(VIEWS[0]["title"])}</h1>
    <a class="version" href="{GITHUB}/releases/tag/v{VERSION}" target="_blank" rel="noopener">v{VERSION}</a>
    <div class="tabs" role="tablist" aria-label="Where SciFi runs">{tabs}</div>
  </header>
{views}
</div>
<script>
(function () {{
  var titles = {json.dumps({v["key"]: v["title"] for v in VIEWS})};
  var keys = Object.keys(titles);
  var hashFor = {{ local: 'local', ai: 'claude-ai' }};
  function show(key) {{
    keys.forEach(function (k) {{
      var sec = document.getElementById('view-' + k);
      var tab = document.getElementById('tab-' + k);
      sec.hidden = (k !== key);
      tab.setAttribute('aria-selected', k === key ? 'true' : 'false');
    }});
    document.getElementById('page-title').textContent = titles[key];
    try {{ localStorage.setItem('scifi-anatomy-view', key); }} catch (e) {{}}
  }}
  var initial = keys[0];
  var h = (location.hash || '').replace('#', '');
  keys.forEach(function (k) {{ if (hashFor[k] === h) initial = k; }});
  if (!h) {{ try {{ var s = localStorage.getItem('scifi-anatomy-view'); if (s && titles[s]) initial = s; }} catch (e) {{}} }}
  show(initial);
  document.querySelectorAll('.tabs button').forEach(function (b) {{
    b.addEventListener('click', function () {{ show(b.dataset.view); }});
  }});
  window.addEventListener('hashchange', function () {{
    var h = (location.hash || '').replace('#', '');
    keys.forEach(function (k) {{ if (hashFor[k] === h) show(k); }});
  }});
}})();
</script>
'''


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if "--check" in argv:
        missing = check_links()
        if missing:
            print("missing link targets:\n  " + "\n  ".join(missing), file=sys.stderr)
            return 1
        print(f"all {len(all_hrefs())} link targets exist")
    OUT.write_text(page(), encoding="utf8")
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
