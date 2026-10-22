"""The content of the SciFi system figure and the anatomy page, in one place.

`make_figure.py` draws docs/scifi-system.svg from the LOCAL view. `make_anatomy.py` writes
docs/index.html (the clickable anatomy page) from both views. Change a skill, agent, hook or
workspace file here, then re-run both scripts.

Every text item is a list of spans, each span `(text, href)` where href is None, a path in
the repo (file or folder, with an optional #anchor), or a full https URL. The page turns paths into GitHub links;
the figure prints the text only. Stdlib only.
"""

GITHUB = "https://github.com/Sdamirsa/SciFi"


def span(text, href=None):
    return [(text, href)]


def S(*parts):
    """Join spans: S("a ", ("b", "path"), " c")."""
    out = []
    for p in parts:
        out.append(p if isinstance(p, tuple) else (p, None))
    return out


def plain(spans):
    return "".join(t for t, _ in spans)


# A column row: (indent, name_spans, desc_spans). indent is "" or "  ".
# Convention on the page: the name opens the file or folder itself; the description opens
# the rule, schema or document behind it.

# ------------------------------------------------------------------ LOCAL (plugin or .claude/)
LOCAL = {
    "key": "local",
    "label": "Claude Code (plugin or .claude/)",
    "title": "SciFi: scientific manuscripts from findings to inference",
    "subtitle": S("One repo, three ways to run it (Claude Code plugin, copied .claude/ folder, claude.ai skills). "
                  "Three actors. Every handoff is a JSON file in the workspace, validated on write."),
    "repo_title": S(("SciFi/", ""), "  (the repo, github.com/Sdamirsa/SciFi)"),
    "repo": [
        ("", S((".claude-plugin/", ".claude-plugin")), S(("plugin.json", ".claude-plugin/plugin.json"), ", ", ("marketplace.json", ".claude-plugin/marketplace.json"))),
        ("", S(("skills/", "skills")), S()),
        ("  ", S(("scifi/", "skills/scifi/SKILL.md")), S("master orchestrator, entry /scifi, ", ("stages.md", "skills/scifi/stages.md"))),
        ("  ", S(("scientific-writing/", "skills/scientific-writing/SKILL.md")), S("the standards from 14 papers, ", ("checker", "skills/scientific-writing/scripts/check_manuscript.py"), ", ", ("checklist", "skills/scientific-writing/references/checklist.md"), ", ", ("journals", "skills/scientific-writing/references/journal-profiles.md"))),
        ("  ", S(("scifi-spine/", "skills/scifi-spine/SKILL.md")), S("central claim, gap, results, threads of evidence")),
        ("  ", S(("scifi-skeleton/", "skills/scifi-skeleton/SKILL.md")), S("reverse outline per section from the threads")),
        ("  ", S(("scifi-paragraph/", "skills/scifi-paragraph/SKILL.md")), S("the paragraph loop: map, 5 checks, draft, gate (", ("loop.md", "skills/scifi-paragraph/loop.md"), ")")),
        ("  ", S(("scifi-figures/", "skills/scifi-figures/SKILL.md")), S("figure and table ", ("brainstorm", "skills/scifi-figures/references/brainstorm.md"), ", captions, ", ("corpus figures", "skills/scifi-figures/references/corpus-figures.md"))),
        ("  ", S(("scifi-literature/", "skills/scifi-literature/SKILL.md")), S("scout, ", ("notes", "skills/scifi-literature/references/note-template.md"), ", ", ("ontology", "skills/scifi-literature/references/ontology.md"), ", ", ("labels", "skills/scifi-literature/references/labeling-rules.md"), ", ", ("evidence lookup", "skills/scifi-literature/references/lookup.md"))),
        ("  ", S(("scifi-review/", "skills/scifi-review/SKILL.md")), S("evaluation, ", ("comments.json", "scripts/schemas/comments.schema.json"), ", improvements")),
        ("  ", S(("scifi-export/", "skills/scifi-export/SKILL.md")), S("Word with live Zotero citations, then Google Docs (", ("guide", "docs/zotero-guide.md"), ")")),
        ("  ", S(("scifi-stats/", "skills/scifi-stats/SKILL.md")), S("which biostatistical method, with a ", ("complexity guard", "skills/scifi-stats/references/complexity-guard.md"))),
        ("  ", S(("scifi-lite/", "skills/scifi-lite/SKILL.md")), S("single-session version for claude.ai")),
        ("  ", S(("project-memory/", "skills/project-memory/SKILL.md")), S("the ritual: ", ("STATUS", "skills/project-memory/STATUS.template.md"), ", Project-log, LESSONS")),
        ("  ", S(("panel-discussion/", "skills/panel-discussion/SKILL.md")), S("decision utility")),
        ("  ", S(("system-design-review/", "skills/system-design-review/SKILL.md")), S("maintainer ", ("rubric", "skills/system-design-review/rubric.md"))),
        ("", S(("agents/", "agents")), S("15 sub-agents")),
        ("  ", S(("logic-mapper", "agents/logic-mapper.md")), S("sonnet, medium")),
        ("  ", S(("flow-checker", "agents/flow-checker.md")), S("sonnet, medium   internal alignment")),
        ("  ", S(("local-aligner", "agents/local-aligner.md")), S("sonnet, medium   previous and next unit")),
        ("  ", S(("global-aligner", "agents/global-aligner.md")), S("sonnet, medium   spine, results, skeleton")),
        ("  ", S(("evidence-checker", "agents/evidence-checker.md")), S("sonnet, medium   claims vs sources and results")),
        ("  ", S(("style-checker", "agents/style-checker.md")), S("sonnet, low      length, standards, script")),
        ("  ", S(("literature-scout", "agents/literature-scout.md")), S("sonnet, low      read-only lookup")),
        ("  ", S(("figure-brainstormer", "agents/figure-brainstormer.md")), S("sonnet, medium   display-item candidates")),
        ("  ", S(("noter", "agents/noter.md"), ", ", ("labeler", "agents/labeler.md")), S("sonnet, medium   one paper each")),
        ("  ", S(("scribe", "agents/scribe.md")), S("sonnet, low      workflow stage: stores files")),
        ("  ", S(("drafter", "agents/drafter.md")), S("inherit: your session model")),
        ("  ", S(("standards-gate", "agents/standards-gate.md")), S("inherit: one pass, PASS or RETURN")),
        ("  ", S(("improver", "agents/improver.md")), S("inherit: accepted comments as diffs")),
        ("  ", S(("design-reviewer", "agents/design-reviewer.md")), S("inherit: audits SciFi itself")),
        ("", S(("hooks/", "hooks/hooks.json")), S(("session-start", "hooks/session-start.sh"), ", ", ("validate-json", "hooks/validate-json.sh"), ", ", ("stop-pointer", "hooks/stop-pointer.sh"))),
        ("", S(("workflows/", "workflows")), S(("review-all", "workflows/review-all.js"), ", ", ("literature-all", "workflows/literature-all.js"), ": batch fan-outs, no gate inside")),
        ("", S(("scripts/", "scripts")), S(("validate_json", "scripts/validate_json.py"), ", ", ("state", "scripts/state.py"), ", ", ("init_workspace", "scripts/init_workspace.py"), ", ", ("export_docx", "scripts/export_docx.py"), ", ", ("release", "scripts/release.py"), ", ", ("schemas/", "scripts/schemas"))),
        ("", S(("example-workspace/", "example-workspace")), S("the invented echo study, every JSON valid")),
        ("", S(("docs/", "docs")), S(("protocol", "docs/protocol.md"), ", ", ("workflows", "docs/workflows.md"), ", ", ("architecture", "docs/architecture.md"), ", ", ("zotero-guide", "docs/zotero-guide.md"), ", ", ("this figure", "docs/make_figure.py"), ", ", ("this page", "docs/make_anatomy.py"))),
        ("", S(("dist/", "dist")), S(("scientific-writing.skill", "dist/scientific-writing.skill"), ", ", ("scifi-lite.skill", "dist/scifi-lite.skill"), ", ", ("SciFi-dotclaude.zip (release asset)", "https://github.com/Sdamirsa/SciFi/releases/latest"))),
        ("", S(("research/", "research")), S("the 28 paper analyses behind the standards")),
    ],
    "lanes": {
        "human": {
            "title": "HUMAN",
            "heading": "Types a command or a phrase",
            "items": [  # (command spans, desc spans)
                (S(("/scifi <workspace> [mode] [journal]", "skills/scifi/SKILL.md")), S("full pipeline, or resume from ", ("STATE.json", "example-workspace/Thinking-space/STATE.json"))),
                (S(("/scifi-paragraph d03", "skills/scifi-paragraph/SKILL.md")), S("one paragraph through the loop")),
                (S(("/scifi-review [file]", "skills/scifi-review/SKILL.md")), S("evaluate, comment, optionally improve")),
                (S(("/scifi-figures", "skills/scifi-figures/SKILL.md")), S("brainstorm figures and tables")),
                (S(("/scifi-literature", "skills/scifi-literature/SKILL.md")), S("library, notes, ontology, labels")),
                (S(("/scifi-export --library users/<id>", "skills/scifi-export/SKILL.md")), S("docx with live Zotero citations")),
                (S(("/scifi-stats", "skills/scifi-stats/SKILL.md")), S("analysis plan: the standard method for the question")),
                (S(("/project-memory", "skills/project-memory/SKILL.md")), S("end-of-session ritual, user only")),
            ],
            "notes": [
                S(("Decides at gates: picks one option, approves diffs, answers NEED requests.", "docs/protocol.md#6-control-modes")),
                S(("Owns Manuscript/ and Literature/. The system reads them and never edits them.", "docs/protocol.md#1-actors")),
                S(("Modes: co-thinker (default), human-on-the-loop, human-in-the-loop, fully-automated.", "docs/workflows.md#control-modes")),
            ],
        },
        "master": {
            "title": "MASTER  (your session model: Opus or Fable)",
            "steps": [  # (number, name spans, desc spans)
                ("0", S(("resume", "hooks/session-start.sh")), S(("state.py session", "scripts/state.py"), "; read STATE.json and the last decisions")),
                ("1", S(("spine", "skills/scifi-spine/SKILL.md")), S("claim, gap, results R1.., threads T1..  ", ("spine.json", "scripts/schemas/spine.schema.json"))),
                ("2", S(("skeleton", "skills/scifi-skeleton/SKILL.md")), S("units with takeaway and thread  ", ("skeleton.json", "scripts/schemas/skeleton.schema.json"))),
                ("3", S(("figures", "skills/scifi-figures/SKILL.md")), S("display-item plan, caption units  ", ("figures.json", "scripts/schemas/figures.schema.json"))),
                ("4", S(("paragraph loop", "skills/scifi-paragraph/loop.md")), S(("brief", "scripts/schemas/brief.schema.json"), ", store envelopes, ", ("synthesis", "scripts/schemas/synthesis.schema.json"), ", draft, gate")),
                ("5", S(("review", "skills/scifi-review/SKILL.md")), S("all units via ", ("review-all", "workflows/review-all.js"), ", gates, ", ("comments/*.json", "scripts/schemas/comments.schema.json"))),
                ("6", S(("ritual and export", "skills/scifi/stages.md")), S(("/project-memory", "skills/project-memory/SKILL.md"), " (user), ", ("/scifi-export", "skills/scifi-export/SKILL.md"))),
            ],
            "notes": [
                S(("Only writer of STATE.json, spine, skeleton, figures, syntheses and the decisions log,", "docs/protocol.md#1-actors")),
                S("through ", ("state.py", "scripts/state.py"), ". Reads one unit, its logic.json and five envelopes at a time."),
            ],
        },
        "agents": {
            "title": "SUB-AGENTS  (isolated, one JSON brief in, one JSON envelope out)",
            "heading": "The paragraph loop for one unit",
            "rows": [
                (S(("logic-mapper", "agents/logic-mapper.md")), S("claims, evidence, steps of the text  ", ("units/<id>.logic.json", "scripts/schemas/logic.schema.json"))),
                (S(("flow-checker", "agents/flow-checker.md")), S("internal: one point, context first, takeaway last, old to new")),
                (S(("local-aligner", "agents/local-aligner.md")), S("neighbours: redundancy, pre-emption, bridge, single home")),
                (S(("global-aligner", "agents/global-aligner.md")), S("spine and results: serves the claim, same gap, no new data")),
                (S(("evidence-checker", "agents/evidence-checker.md")), S("each claim vs cited source, our results, or a logical step")),
                (S(("style-checker", "agents/style-checker.md")), S("runs ", ("check_manuscript.py", "skills/scientific-writing/scripts/check_manuscript.py"), ", then the ", ("section standards", "skills/scientific-writing/references/sections"))),
                (S(("drafter", "agents/drafter.md")), S("redrafts from logic.json and the accepted findings  ", ("units/<id>.draft.md", "example-workspace/Thinking-space/units/d03.draft.md"))),
                (S(("standards-gate", "agents/standards-gate.md")), S("one pass: PASS, or RETURN with three blockers")),
            ],
            "pills": [("sonnet medium", "#5a8f6a"), ("sonnet low", "#7a9d85"), ("inherit", "#2a8a56")],
            "pills_href": "docs/protocol.md#7-model-routing-and-effort",
            "note": S("five checks in parallel; the two inherit agents after"),
        },
    },
    "arrows": {
        "human_to_master": S(("command, mode, journal", "docs/workflows.md#commands-and-phrases")),
        "master_to_human": S(("options with one pick at each gate", "docs/protocol.md#6-control-modes")),
        "master_to_agents": S(("briefs/<task>.json", "scripts/schemas/brief.schema.json")),
        "agents_to_master": S(("envelope JSON, stored in handshakes/", "scripts/schemas/envelope.schema.json")),
        "repo_to_lanes": S(("loaded as skills, agents, hooks and workflows", "docs/installation.md")),
        "human_to_ws": S(("manuscript, papers", "docs/protocol.md#2-the-workspace")),
        "master_to_ws": S(("reads and writes", "docs/protocol.md#8-active-memory-rules")),
        "agents_to_ws": S(("envelopes, unit files", "docs/protocol.md#4-the-envelope-agent-to-master")),
    },
    "ws_title": S(("<your-paper>/", "example-workspace"), "  (the workspace)"),
    "ws": [
        ("", S(("Manuscript/", "example-workspace/Manuscript")), S("YOU write here, pandoc [@citekey]")),
        ("  ", S(("title.md", "example-workspace/Manuscript/title.md"), "  ", ("abstract.md", "example-workspace/Manuscript/abstract.md"), "  ", ("introduction.md", "example-workspace/Manuscript/introduction.md")), S()),
        ("  ", S(("methods.md", "example-workspace/Manuscript/methods.md"), "  ", ("results.md", "example-workspace/Manuscript/results.md"), "  ", ("discussion.md", "example-workspace/Manuscript/discussion.md")), S()),
        ("  ", S(("figures/", "example-workspace/Manuscript/figures"), "  ", ("tables/", "example-workspace/Manuscript/tables")), S("your drafts, data, images")),
        ("", S(("Literature/", "example-workspace/Literature")), S("YOU provide")),
        ("  ", S(("library.json", "example-workspace/Literature/library.json")), S(("Better CSL JSON (citation keys)", "docs/zotero-guide.md"))),
        ("  ", S(("library.bbt.json", "docs/zotero-guide.md#export-to-word-and-google-docs-with-live-citations")), S("Better BibTeX JSON (item keys)")),
        ("  ", S(("fulltext/<citekey>.pdf|.md", "example-workspace/Literature/fulltext")), S("the cited papers")),
        ("  ", S(("notes/  ontology.yaml  labels/", "skills/scifi-literature/SKILL.md")), S("written by scifi-literature only")),
        ("", S(("Thinking-space/", "example-workspace/Thinking-space")), S(("SYSTEM owns, all validated JSON", "hooks/validate-json.sh"))),
        ("  ", S(("STATE.json", "example-workspace/Thinking-space/STATE.json")), S(("stage, mode, journal, next action", "scripts/schemas/state.schema.json"))),
        ("  ", S(("analysis-plan.md", "skills/scifi-stats/references/reporting.md")), S("question, data, method, what is reported")),
        ("  ", S(("spine.json", "example-workspace/Thinking-space/spine.json")), S(("claim, gap, results, implications, threads", "scripts/schemas/spine.schema.json"))),
        ("  ", S(("skeleton.json", "example-workspace/Thinking-space/skeleton.json")), S(("units per section, takeaway, thread", "scripts/schemas/skeleton.schema.json"))),
        ("  ", S(("figures.json", "example-workspace/Thinking-space/figures.json")), S(("display-item plan and captions", "scripts/schemas/figures.schema.json"))),
        ("  ", S(("units/<id>.logic.json, .draft.md", "example-workspace/Thinking-space/units")), S(("one unit's logic and drafts", "scripts/schemas/logic.schema.json"))),
        ("  ", S(("briefs/<task>.json", "example-workspace/Thinking-space/briefs")), S(("what the master sent", "scripts/schemas/brief.schema.json"))),
        ("  ", S(("handshakes/<task>.json", "example-workspace/Thinking-space/handshakes")), S(("what the agent returned", "scripts/schemas/envelope.schema.json"))),
        ("  ", S(("handshakes/<id>.synthesis.r<n>.json", "example-workspace/Thinking-space/handshakes/d03.synthesis.r1.json")), S(("the master's decisions", "scripts/schemas/synthesis.schema.json"))),
        ("  ", S(("comments/<id>.json", "example-workspace/Thinking-space/comments/d02.json")), S(("review comments with severity and fix", "scripts/schemas/comments.schema.json"))),
        ("  ", S(("log/decisions.jsonl", "example-workspace/Thinking-space/log/decisions.jsonl")), S("append-only: who decided what, why")),
        ("  ", S(("scratch/", "example-workspace/Thinking-space/scratch")), S("option exploration, inspectable")),
        ("", S(("export/", "skills/scifi-export/SKILL.md")), S("docx with Zotero markers, report")),
        ("", S((".claude/", "example-workspace/.claude")), S(("memory spine (minimal dot-claude-iff)", "skills/project-memory/SKILL.md"))),
        ("  ", S(("STATUS.md", "example-workspace/.claude/STATUS.md")), S("read first; rewritten by the ritual")),
        ("  ", S(("Project-log.jsonl", "example-workspace/.claude/Project-log.jsonl")), S("one line per real thing")),
        ("  ", S(("LESSONS.jsonl", "example-workspace/.claude/LESSONS.jsonl")), S("mistakes with a checkable prevention")),
    ],
    "rules_title": "Rules that hold everywhere",
    "rules": [
        S(("Human owns Manuscript/ and Literature/; the system never edits them.", "docs/protocol.md#1-actors")),
        S(("Master owns Thinking-space/ and is the only writer of shared files.", "docs/protocol.md#1-actors")),
        S(("Sub-agents read only the paths in their brief and return one envelope.", "docs/protocol.md#3-the-brief-master-to-agent")),
        S(("validate-json rejects any malformed JSON on write (exit 2).", "hooks/validate-json.sh")),
        S(("No number that is not in results.md; no source that is not in the library.", "docs/protocol.md#11-honesty")),
        S(("A missing source is a NEED, never a guess. A missing envelope is not a pass.", "docs/protocol.md#11-honesty")),
        S(("Resume = STATE.json, then the tail of log/decisions.jsonl.", "docs/protocol.md#10-resume")),
        S(("Accepted units are never redrafted; human edits are never overwritten.", "docs/protocol.md#8-active-memory-rules")),
        S(("Standards: sentences 15 to 30 words, no colons, semicolons or dashes,", "skills/scientific-writing/SKILL.md")),
        S(("no promotional words, every claim with its evidence in the same sentence.", "skills/scientific-writing/references/checklist.md")),
    ],
    "footer": S("Run it: ", ("/plugin marketplace add Sdamirsa/SciFi, then /plugin install scifi@scifi", "docs/installation.md#a-plugin-from-the-marketplace"),
                " (Claude Code); ", ("scripts/install_local.sh <project>", "scripts/install_local.sh"), " to copy into .claude/; ",
                ("dist/scifi-lite.skill", "dist/scifi-lite.skill"), " and ", ("dist/scientific-writing.skill", "dist/scientific-writing.skill"),
                " for claude.ai."),
}

# ------------------------------------------------------------------ CLAUDE.AI (two .skill uploads)
CLAUDE_AI = {
    "key": "ai",
    "label": "claude.ai (two .skill files)",
    "title": "SciFi on claude.ai: the same files, one Claude playing every role",
    "subtitle": S("Two skills uploaded to claude.ai. No subagents, no hooks, no model routing. The roles below run in sequence in one "
                  "context, each writing its output before the next role's rules are read. The workspace files are the plugin's, so a "
                  "paper started here continues in Claude Code. ", ("What works and what does not", "docs/claude-ai.md")),
    "repo_title": S(("dist/", "dist"), "  (what you upload, built by ", ("package_skills.py", "scripts/package_skills.py"), ")"),
    "repo": [
        ("", S(("scifi-lite.skill", "dist/scifi-lite.skill")), S("the loop in one session; unpacks to the files below")),
        ("  ", S(("SKILL.md", "skills/scifi-lite/SKILL.md")), S("spine, skeleton, the loop, evaluation only, limits")),
        ("  ", S(("references/standards/", "skills/scientific-writing/references")), S("copy of the scientific-writing references")),
        ("    ", S(("global-rules.md", "skills/scientific-writing/SKILL.md")), S("section 2 of the standards skill")),
        ("    ", S(("sections/<section>.md", "skills/scientific-writing/references/sections")), S("title to back matter, original and review")),
        ("    ", S(("checklist.md", "skills/scientific-writing/references/checklist.md")), S("sections A to H, cited by every finding")),
        ("    ", S(("journal-profiles.md", "skills/scientific-writing/references/journal-profiles.md")), S("npj, jamia, nature, lancet, ehj, default")),
        ("    ", S(("figures.md  tables.md  captions.md", "skills/scientific-writing/references/figures.md")), S("display items")),
        ("    ", S(("examples/", "skills/scientific-writing/examples")), S("skeletons and abstract variants")),
        ("  ", S(("references/protocol.md", "docs/protocol.md")), S("workspace layout, finding format, synthesis")),
        ("  ", S(("scripts/check_manuscript.py", "skills/scientific-writing/scripts/check_manuscript.py")), S("style checker, needs code execution")),
        ("  ", S(("scripts/validate_json.py", "scripts/validate_json.py")), S("schema check, needs code execution")),
        ("  ", S(("scripts/schemas/", "scripts/schemas")), S("the nine JSON schemas")),
        ("", S(("scientific-writing.skill", "dist/scientific-writing.skill")), S("the standards alone, without the loop")),
        ("  ", S(("SKILL.md", "skills/scientific-writing/SKILL.md")), S("draft, revise, plan or audit one section")),
        ("  ", S(("references/", "skills/scientific-writing/references")), S("same references as above")),
        ("  ", S(("examples/", "skills/scientific-writing/examples")), S("")),
        ("  ", S(("scripts/check_manuscript.py", "skills/scientific-writing/scripts/check_manuscript.py")), S("")),
        ("", S(("Not shipped here", "docs/claude-ai.md")), S("")),
        ("  ", S(("agents/", "agents")), S("no subagents on claude.ai; the roles run in sequence")),
        ("  ", S(("hooks/", "hooks")), S("no hooks; validation only with code execution")),
        ("  ", S(("workflows/", "workflows")), S("no dynamic workflows; one unit at a time")),
        ("  ", S(("scifi-export, scifi-stats, scifi-literature", "skills")), S("plugin only")),
        ("  ", S(("project-memory", "skills/project-memory/SKILL.md")), S("no ritual; save STATE.json yourself")),
        ("", S(("Install", "docs/installation.md#d-claudeai")), S("Settings, Skills, upload both .skill files; turn code execution on")),
    ],
    "lanes": {
        "human": {
            "title": "HUMAN",
            "heading": "Uploads the paper, then types a phrase",
            "items": [
                (S(("\"check paragraph 2 of my discussion with SciFi, journal lancet\"", "skills/scifi-lite/SKILL.md")), S("one unit through the loop")),
                (S(("\"evaluate this manuscript for JAMIA\"", "skills/scifi-lite/SKILL.md")), S("comments with severity, location, rule, fix; a verdict")),
                (S(("\"extract the spine and skeleton of this paper\"", "skills/scifi-lite/SKILL.md")), S("claim, threads, reverse outline")),
                (S(("\"tighten this abstract for npj Digital Medicine\"", "skills/scientific-writing/SKILL.md")), S("standards skill alone, one section")),
                (S(("\"check this methods section\"", "skills/scientific-writing/SKILL.md")), S("standards audit, checker if code execution is on")),
                (S(("upload STATE.json to resume", "docs/claude-ai.md")), S("resume is manual here")),
            ],
            "notes": [
                S(("Decides at gates: picks one option, agrees to the synthesis, answers NEED requests.", "docs/protocol.md#6-control-modes")),
                S(("Uploads the sections, results.md and the full texts of cited papers; without full texts, evidence findings are NEEDs.", "docs/claude-ai.md")),
                S(("Modes as in the plugin: co-thinker (default), human-on-the-loop, human-in-the-loop, fully-automated.", "docs/protocol.md#6-control-modes")),
            ],
        },
        "master": {
            "title": "ONE CLAUDE  (the session model plays master and every role)",
            "steps": [
                ("0", S(("resume", "skills/scifi-lite/SKILL.md")), S("read the uploaded STATE.json; no session-start hook")),
                ("1", S(("spine", "skills/scifi-lite/SKILL.md")), S("results R1.., gap, 2 or 3 claims with one pick, threads  ", ("spine.json", "scripts/schemas/spine.schema.json"))),
                ("2", S(("skeleton", "skills/scifi-lite/SKILL.md")), S("units with takeaway and thread, reverse-outline test  ", ("skeleton.json", "scripts/schemas/skeleton.schema.json"))),
                ("3", S(("figures", "docs/claude-ai.md")), S("brainstorm only; the generation script needs code execution")),
                ("4", S(("the loop", "skills/scifi-lite/SKILL.md")), S("map, five checks, ", ("synthesis", "scripts/schemas/synthesis.schema.json"), ", draft, gate, as separate written passes")),
                ("5", S(("evaluation only", "skills/scifi-lite/SKILL.md")), S("spine, skeleton, steps 1 to 3 per unit, no draft, ", ("comments/<id>.json", "scripts/schemas/comments.schema.json"))),
                ("6", S(("state", "scripts/schemas/state.schema.json")), S("update STATE.json and append to log/decisions.jsonl; no ritual")),
            ],
            "notes": [
                S(("Writes each role's output before reading the next role's rules; that is the only isolation here.", "docs/claude-ai.md")),
                S(("Every JSON follows the plugin schemas; validated with validate_json.py when code execution is on.", "scripts/validate_json.py")),
            ],
        },
        "agents": {
            "title": "ROLES  (played in sequence, one envelope each, same schemas)",
            "heading": "The loop for one unit",
            "rows": [
                (S(("logic-mapper", "skills/scifi-lite/SKILL.md")), S("claims, evidence, steps of the text  ", ("units/<id>.logic.json", "scripts/schemas/logic.schema.json"))),
                (S(("flow", "skills/scifi-lite/SKILL.md")), S("internal: one point, context first, takeaway last, old to new")),
                (S(("local", "skills/scifi-lite/SKILL.md")), S("neighbours: redundancy, pre-emption, bridge, single home")),
                (S(("global", "skills/scifi-lite/SKILL.md")), S("spine and results: serves the claim, same gap, no new data")),
                (S(("evidence", "skills/scifi-lite/SKILL.md")), S("each claim vs the sources the user supplied, the results, or a step")),
                (S(("style", "skills/scifi-lite/SKILL.md")), S(("checklist", "skills/scientific-writing/references/checklist.md"), " A, C, D and the section's letter, plus the section file")),
                (S(("drafter", "skills/scifi-lite/SKILL.md")), S("rewrites from logic.json and the accepted findings  ", ("units/<id>.draft.md", "example-workspace/Thinking-space/units/d03.draft.md"))),
                (S(("standards-gate", "skills/scifi-lite/SKILL.md")), S("one pass: PASS, or RETURN with three blockers")),
            ],
            "pills": [("one model", "#5a8f6a"), ("in sequence", "#7a9d85"), ("same envelope", "#2a8a56")],
            "pills_href": "docs/claude-ai.md",
            "note": S("no model routing; the checks share one context, so treat findings as a strong first pass"),
        },
    },
    "arrows": {
        "human_to_master": S(("phrase, journal, mode", "docs/claude-ai.md#using-scifi-lite")),
        "master_to_human": S(("findings and picks, wait for agreement", "docs/protocol.md#6-control-modes")),
        "master_to_agents": S(("the role's rules and inputs", "skills/scifi-lite/SKILL.md")),
        "agents_to_master": S(("envelope JSON, written before the next role", "scripts/schemas/envelope.schema.json")),
        "repo_to_lanes": S(("two .skill uploads", "docs/installation.md#d-claudeai")),
        "human_to_ws": S(("uploads", "docs/claude-ai.md")),
        "master_to_ws": S(("files or JSON blocks", "skills/scifi-lite/SKILL.md")),
        "agents_to_ws": S(("one envelope per role", "docs/protocol.md#4-the-envelope-agent-to-master")),
    },
    "ws_title": S(("<your-paper>/", "example-workspace"), "  (a project or an uploaded folder; same layout)"),
    "ws": [
        ("", S(("Manuscript/", "example-workspace/Manuscript")), S("YOU upload, pandoc [@citekey]")),
        ("  ", S(("title.md", "example-workspace/Manuscript/title.md"), "  ", ("abstract.md", "example-workspace/Manuscript/abstract.md"), "  ", ("introduction.md", "example-workspace/Manuscript/introduction.md")), S()),
        ("  ", S(("methods.md", "example-workspace/Manuscript/methods.md"), "  ", ("results.md", "example-workspace/Manuscript/results.md"), "  ", ("discussion.md", "example-workspace/Manuscript/discussion.md")), S()),
        ("", S(("Literature/", "example-workspace/Literature")), S("YOU upload")),
        ("  ", S(("library.json", "example-workspace/Literature/library.json")), S(("Better CSL JSON (citation keys)", "docs/zotero-guide.md"))),
        ("  ", S(("fulltext/<citekey>.pdf|.md", "example-workspace/Literature/fulltext")), S("the cited papers; without them evidence is a NEED")),
        ("", S(("Thinking-space/", "example-workspace/Thinking-space")), S(("written as files, or shown as JSON blocks", "skills/scifi-lite/SKILL.md"))),
        ("  ", S(("STATE.json", "example-workspace/Thinking-space/STATE.json")), S(("stage, mode, journal, next action; upload it to resume", "scripts/schemas/state.schema.json"))),
        ("  ", S(("spine.json", "example-workspace/Thinking-space/spine.json")), S(("claim, gap, results, implications, threads", "scripts/schemas/spine.schema.json"))),
        ("  ", S(("skeleton.json", "example-workspace/Thinking-space/skeleton.json")), S(("units per section, takeaway, thread", "scripts/schemas/skeleton.schema.json"))),
        ("  ", S(("units/<id>.logic.json, .draft.md", "example-workspace/Thinking-space/units")), S(("one unit's logic and drafts", "scripts/schemas/logic.schema.json"))),
        ("  ", S(("handshakes/<id>.<role>.r<n>.json", "example-workspace/Thinking-space/handshakes")), S(("one envelope per role", "scripts/schemas/envelope.schema.json"))),
        ("  ", S(("handshakes/<id>.synthesis.r<n>.json", "example-workspace/Thinking-space/handshakes/d03.synthesis.r1.json")), S(("the decisions on the findings", "scripts/schemas/synthesis.schema.json"))),
        ("  ", S(("comments/<id>.json", "example-workspace/Thinking-space/comments/d02.json")), S(("evaluation comments and the verdict", "scripts/schemas/comments.schema.json"))),
        ("  ", S(("log/decisions.jsonl", "example-workspace/Thinking-space/log/decisions.jsonl")), S("append-only: who decided what, why")),
        ("", S(("Carry on in Claude Code", "docs/claude-ai.md")), S("copy the folder into a workspace; the plugin resumes from STATE.json")),
    ],
    "rules_title": "Rules that hold here too",
    "rules": [
        S(("Your text is never changed in place; drafts are proposals next to it.", "skills/scifi-lite/SKILL.md")),
        S(("Each role's output is written before the next role's rules are read.", "skills/scifi-lite/SKILL.md")),
        S(("A finding without a location and a rule is not reported.", "docs/protocol.md#4-the-envelope-agent-to-master")),
        S(("No number that is not in the results; no source that was not supplied.", "docs/protocol.md#11-honesty")),
        S(("Unverifiable is never reported as supported; it is a NEED.", "docs/protocol.md#11-honesty")),
        S(("No artifact is skipped because there is nowhere to write it.", "skills/scifi-lite/SKILL.md")),
        S(("The checks share one context; use the plugin when a paper is near submission.", "docs/claude-ai.md")),
        S(("Standards: sentences 15 to 30 words, no colons, semicolons or dashes,", "skills/scientific-writing/SKILL.md")),
        S(("no promotional words, every claim with its evidence in the same sentence.", "skills/scientific-writing/references/checklist.md")),
    ],
    "footer": S("Run it: upload ", ("dist/scifi-lite.skill", "dist/scifi-lite.skill"), " and ", ("dist/scientific-writing.skill", "dist/scientific-writing.skill"),
                " in claude.ai (", ("installation D", "docs/installation.md#d-claudeai"), "), turn code execution on, upload your sections and papers, then say what to check."),
}

VIEWS = [LOCAL, CLAUDE_AI]


def all_hrefs():
    """Every repo path referenced by either view, for the link check."""
    seen = []

    def walk(x):
        if isinstance(x, tuple) and len(x) == 2 and (x[1] is None or isinstance(x[1], str)) and isinstance(x[0], str):
            if x[1] is not None and x[1] not in seen:
                seen.append(x[1])
            return
        if isinstance(x, dict):
            for k, v in x.items():
                if k != "pills":
                    walk(v)
        elif isinstance(x, (list, tuple)):
            for v in x:
                walk(v)
    for v in VIEWS:
        walk(v)
        if v["lanes"]["agents"].get("pills_href"):
            seen.append(v["lanes"]["agents"]["pills_href"])
    return seen
