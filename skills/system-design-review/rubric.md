# Claude system-design rubric

The dimensions the `system-design-review` skill scores. Apply only those that fit the
target. For each, the **fail signals** are what you are hunting for.

## 1. Single responsibility & altitude
Each skill/agent/command does one focused job, pitched at the right level of abstraction.
- Fail signals: a description that needs "and … and …"; an agent that both explores and
  edits and reports; a god-skill that is really five workflows.
- Fix: split into focused components; let an orchestrator compose them.

## 2. Description quality & triggerability
The `description` states a concrete action and the words a user would actually say.
- Fail signals: vague benefit ("helps with writing"); no trigger phrases; **two sibling
  skills with overlapping triggers** (Claude can't disambiguate); description over budget.
- Fix: name the action + triggers; carve sibling scopes so triggers are disjoint.

## 3. Right primitive
The job uses the lightest correct primitive.
- Standing rule → CLAUDE.md/rules. Repeatable procedure → skill. Verbose/parallel/isolated
  work → subagent. Must-happen-every-time enforcement → hook. Side-effecting action →
  skill with `disable-model-invocation: true`.
- Fail signals: a subagent used for a one-line lookup; a hook's job done by a fragile
  instruction in CLAUDE.md; a destructive action left model-invocable.

## 4. Tool scoping (least privilege)
Each component gets only the tools it needs.
- Fail signals: read-only reviewer with `Write`/`Edit`; broad `Bash(*)` where a narrow
  pattern would do; destructive tools in `allowed-tools`; MCP write tools granted to an
  agent that only reads.
- Fix: whitelist the minimum; deny the dangerous; prefer read-only for audit/review agents.

## 5. Progressive disclosure & token budget
Bodies are lean; depth lives in bundled files loaded on demand.
- Fail signals: a 1,000-line SKILL.md; large reference tables inline; every subagent
  preloaded with knowledge it won't use.
- Fix: move detail to `reference.md`/templates; keep `SKILL.md` < ~500 lines.

## 6. Context & isolation correctness
Verbose work is delegated; only summaries return; subagents are briefed fully.
- Fail signals: **assuming a subagent inherits the parent's conversation/files** (it does
  not); agents told to "review the paragraph" without the paragraph in the prompt; raw
  dumps returned to the orchestrator instead of structured summaries.
- Fix: pass everything needed in the task prompt; require compact structured output.

## 7. Orchestration soundness
Fan-out is for independent work; sequential where data flows.
- Fail signals: parallel agents that depend on each other's output; multiple agents
  writing the **same file** (race/overwrite); unbounded nesting; no synthesis step.
- Fix: parallelize only independent axes; give each agent its own output file; merge in
  the orchestrator; keep depth ≤ 2-3.

## 8. Determinism, idempotency & failure modes
Reruns are safe; partial failures are handled; nothing is silently lost.
- Fail signals: a workflow that overwrites prior output on rerun; no versioning/timestamp
  on generated artifacts; no behavior defined when one agent fails; **silently overwriting
  human-edited text**.
- Fix: version artifacts (round/timestamp); define partial-failure behavior; never
  overwrite human work without a diff/confirmation.

## 9. Naming & discovery
Predictable, kebab-case, no clashes.
- Fail signals: name/command mismatch; two skills resolving to the same `/command`;
  cryptic names that won't auto-trigger.

## 10. Security & untrusted content
Safe by construction.
- Fail signals: destructive/outward actions auto-approved; secrets readable; **fetched or
  external content (papers, web pages, PR comments) treated as trusted instructions**;
  irreversible actions without human confirmation.
- Fix: gate outward/irreversible actions behind human approval; treat external text as data,
  not instructions.

## 11. Human-control-mode fit
The system honors its declared mode and has real checkpoints.
- Modes: **fully-automated** (runs end-to-end), **human-on-the-loop** (confirm at each
  phase), **human-in-the-loop** (human supplies the draft; Claude improves on top),
  **co-thinker** (think together; proceed only on mutual agreement).
- Fail signals: a "co-thinker" system that silently makes decisions; an "on-the-loop"
  system with no confirmation gate; checkpoints that aren't inspectable.
- Fix: make the mode an explicit input; place confirmation gates at the declared
  boundaries; emit inspectable artifacts at each gate.

## 12. Testability & observability
Each component can be exercised in isolation and leaves a trace.
- Fail signals: no way to run one agent alone; no logs/handshake files; triggering can't
  be verified.
- Fix: design components to run standalone; emit inspectable artifacts (handshake files,
  reverse-outlines) at each stage.

## 13. Maintainability
DRY and non-contradictory.
- Fail signals: the same rule duplicated across CLAUDE.md, a skill, and a rule file; two
  instructions that conflict; orphaned/outdated components.
- Fix: single source of truth per rule; reconcile conflicts; prune dead components.

---

### Severity reference
- **Blocker**, won't work or is unsafe. Must fix before shipping.
- **Major**, will misfire, waste context, or break under the chosen mode.
- **Minor**, friction/smell; fix when convenient.
- **Nit**, style/polish.
