# The SciFi protocol: actors, files, handshakes

This is the one document every component is written against. Skills and agents point here instead of restating it.

## 1. Actors

| Actor | Who | Owns | Reads |
|---|---|---|---|
| Human | you | `Manuscript/`, `Literature/`; every gate decision | anything |
| Master | the session model running the `scifi` skill (Opus or Fable, whichever you chose) | `Thinking-space/` and `.claude/` in the workspace; the only writer of shared files | `STATE.json` first, then only the files the current stage needs |
| Sub-agents | `agents/*.md`, each in an isolated context | only their own envelope and the unit files their brief names | only the paths their brief lists |

The system never edits `Manuscript/`, `Literature/library.json` or `Literature/fulltext/`. The literature stages write their own outputs to `Literature/notes/`, `Literature/ontology.yaml` and `Literature/labels/` and nowhere else. Drafts live in `Thinking-space/units/`, and the human copies an accepted draft into `Manuscript/` (or asks the master to, which the master does only on an explicit instruction, writing a `.bak` copy first).

## 2. The workspace

```
<your-paper>/
  Manuscript/               your sections as markdown, pandoc citations [@citekey]
  Literature/               library.json (Better CSL JSON) and fulltext/<citekey>.pdf|.md
  Thinking-space/           everything the system makes
    STATE.json              where we are, mode, journal, next action, pointer
    spine.json              central claim, gap, results R1.., implications I1.., threads T1..
    skeleton.json           per section, per unit: id, takeaway, does, thread, keep/defer
    figures.json            display-item plan with captions
    units/<id>.logic.json   claims, evidence, steps of one unit
    units/<id>.draft.md     the current draft; older versions below a "---- previous" marker
    figures/                generate_figures.py and rendered figures when data exist
    briefs/<task>.json      what the master dispatched
    handshakes/<task>.json  what the agent returned; <unit>.synthesis.r<n>.json is the master's resolution
    comments/<id>.json      review comments in the same finding format
    log/decisions.jsonl     append-only
    scratch/                option exploration, stress tests
  .claude/                  memory spine (see project-memory)
    STATUS.md  Project-log.jsonl  LESSONS.jsonl
```

Section files for a unit: `sections/<section>.md`, where `limitations` and `conclusion` units use `discussion.md` and `caption` units use `captions.md`. Unit ids: `t01` title, `a01` abstract, `i01..` introduction, `m01..` methods, `r01..` results, `d01..` discussion, `c01..` captions. Task ids: `<unit>.<agent>.r<round>`, for example `d03.flow-checker.r1`. Literature batch work (notes, labels) uses `lit-<nnn>.<role>.r1` where the role is `notes` or `labels` and the agent is a general sonnet subagent briefed by `scifi-literature`.

## 3. The brief (master to agent)

Every dispatch writes `briefs/<task>.json` (schema `brief`) and passes the same content as the agent's prompt. Eight content fields, always, plus `task_id`, `agent` and `dispatched_at`; `unit_text` whenever the unit has text:

| Field | Content |
|---|---|
| objective | one sentence naming the outcome |
| context | 2 to 5 facts the agent cannot see (the central claim, the unit's takeaway, the journal, the mode) |
| inputs | exact absolute paths. Plugin files are given as `${CLAUDE_PLUGIN_ROOT}/...` resolved by the master to an absolute path, because agents run in the workspace and cannot resolve plugin-relative paths. The unit text is also pasted in `unit_text` so the agent never depends on locating it |
| constraints | tools not to use, files not to touch, the standards file to read if any |
| output_contract | the envelope path; artifact paths if the agent writes a unit file |
| done_criteria | checks the master can run |
| non_goals | what this agent does not judge (the other axes) |
| escalation | "If blocked, or a source is missing, return status blocked or a NEED in `needs`; never guess." |

## 4. The envelope (agent to master)

Every agent replies with the envelope JSON and nothing else; the master writes it verbatim to `handshakes/<task>.json` (schema `envelope`), where the hook validates it. Agents that have Write may also write it themselves. Required: `task_id`, `agent_id`, `status` (done, partial, blocked), `result` (one readable paragraph), `evidence` (what was read or run). Findings carry `id`, `axis`, `severity` (blocker, major, minor, nit), `issue`, `solution`, `location` (`d04:s3` or a quote of at most 12 words), and `rule` (the standards item). Gate agents add `verdict` (PASS or RETURN) and, at manuscript scope, `manuscript_verdict` (accept, minor, major, reject). Sources missing become entries in `needs`, never a guess. The reply text in the conversation is the envelope and nothing else, so the master parses one thing.

The `validate-json` hook rejects a malformed brief, envelope, synthesis, logic, spine, skeleton, figures, comments or STATE file on write, with the schema error returned to the writer.

## 5. The synthesis (master decision)

After reading the envelopes of one round the master writes `handshakes/<unit>.synthesis.r<n>.json` (schema `synthesis`): the de-duplicated findings with a response each (accept, reject, defer), `decided_by` (human, master, both) and `next` (draft, redraft, gate, human, accept, blocked). Deferred findings become `defer` notes on the skeleton unit they belong to. `scifi-review` writes the same findings, with the human's responses, as `comments/<id>.json` (schema `comments`), which the improver reads.

## 6. Control modes

| Mode | Where the human decides |
|---|---|
| co-thinker (default) | at every gate: the master shows 2 or 3 stress-tested options with one pick and proceeds on agreement; fixes are shown as diffs to approve |
| human-on-the-loop | the master resolves findings itself, then confirms with the human at the end of every stage before the next one starts |
| human-in-the-loop | the human writes every draft; the system maps, checks and proposes; the human edits |
| fully-automated | end to end; stops only on a blocker or an unresolved NEED |

A decision that cannot be undone (overwriting a human-edited draft, changing the central claim after units are accepted) is a human gate in every mode.

## 7. Model routing and effort

| Agent | Model | Effort | Why |
|---|---|---|---|
| logic-mapper, flow-checker, local-aligner, global-aligner, evidence-checker, figure-brainstormer | sonnet | medium | independent, parallel, structured output; judgement is bounded by one axis |
| style-checker, literature-scout | sonnet | low | script-backed or lookup work |
| drafter, standards-gate, improver | inherit | inherit | prose quality and the final judgement stay with the model you chose for the session |
| master | your session | your session | holds the decisions and the human conversation |

## 8. Active memory rules

- The master never reads the whole Thinking-space. Per unit: `STATE.json`, the unit's `logic.json`, the five envelopes, the skeleton entry. Envelopes carry findings and a one-paragraph result, never the text.
- An agent reads only its listed inputs. The full standards are read by `style-checker`, `drafter`, `standards-gate` and `figure-brainstormer`; the four alignment agents get the one or two rules they enforce quoted in their brief.
- A skill body stays under about 150 lines. Depth lives in reference files loaded by the one agent that needs it.
- Long shared context (the spine, the skeleton) is a file every agent reads from a path, never prose duplicated into prompts.

## 9. Session count

The master runs `python3 scripts/state.py session` once at the start of every session; the ritual runs `state.py ritual` when it completes. The session-start hook uses the count to suggest the ritual after three sessions without one.

## 10. Resume

Read `Thinking-space/STATE.json`, then the last five lines of `log/decisions.jsonl`, then the current unit's files named in `STATE.json`. Continue from `next_action`. Accepted units are not redrafted. A unit whose `status` is `human-edited` is re-mapped before anything else happens to it.

## 11. Honesty

Failures come with their output. Skipped steps are named. "Done" means the gate passed and the envelope says so. A missing envelope is never counted as a pass; the master re-dispatches once and then asks the human. A mistake is logged in `Project-log.jsonl` (type `mistake`) and, when it could recur, as a `LESSONS.jsonl` row with a prevention that a script or a hook can check.
