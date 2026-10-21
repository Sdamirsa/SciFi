# SciFi on claude.ai

claude.ai has skills and, when enabled, code execution. It has no subagents and no hooks.
SciFi ships two skills for it. Install them as described in
[installation.md](installation.md#d-claudeai).

## What works and what does not

| Feature | Claude Code plugin | claude.ai |
|---|---|---|
| The standards and the checker script | yes | yes (`scientific-writing.skill`, checker needs code execution) |
| Spine and skeleton, extract mode | yes | yes (`scifi-lite`) |
| Paragraph loop: map, five checks, synthesis, draft, gate | yes, isolated agents in parallel | yes, one Claude playing each role in sequence |
| Same JSON files as the plugin | yes, validated on write by a hook | yes, written to files or shown inline; validated only with code execution |
| Model routing (sonnet checkers, your model drafting) | yes | no, one model does everything |
| Resume from `STATE.json` | automatic, session-start hook | manual, upload or paste `STATE.json` |
| Zotero MCP | yes, when configured | only if a Zotero connector is available |
| Figures stage and generation scripts | yes | brainstorm only, unless code execution can run the script |
| Whole-manuscript review | yes | yes, slower; one section per conversation works best |
| `/project-memory` ritual | yes | no |

The main loss is independence. In the plugin each check runs in its own context and cannot
see what the other checks concluded. In `scifi-lite` the roles share one context, so the
skill writes each role's output before reading the next role's rules. Treat its findings as
a strong first pass, and use the plugin when a paper is close to submission.

## Using scifi-lite

1. Start a project and upload your sections, `results.md` (or a results table) and the full
   texts of the papers you cite. Without full texts, evidence findings are NEEDs, not
   verdicts.
2. Say "check paragraph 2 of my discussion with SciFi, journal lancet". The skill asks for
   anything missing, extracts or asks for the spine and skeleton, then runs the loop.
3. Each artifact appears as a file (with code execution) or as a JSON block headed with its
   path. Save them in a `Thinking-space/` folder if you want to continue in Claude Code
   later; the formats are identical.
4. For a full review say "evaluate this manuscript for JAMIA". You get comments with
   severity, location, rule and fix, and a verdict.

The skill's procedure is in `skills/scifi-lite/SKILL.md`.

## Using the standards skill alone

`scientific-writing.skill` is the same standards the plugin uses, without the loop. It drafts,
revises, plans or audits one section at a time against the journal profiles, and runs
`check_manuscript.py` when code execution is on. Use it for quick work ("tighten this
abstract for npj Digital Medicine", "check this methods section"); use `scifi-lite` when the
paragraph's logic and its fit with the rest of the paper matter.
