---
name: system-design-review
description: >
  Maintainer skill for SciFi itself: audit the design of its skills, agents, hooks and
  scripts against the 13-dimension system-design rubric after any change to them. Use when
  a contributor says "review the system design", "audit the plugin", "run the design
  review", or after editing anything under skills/, agents/, hooks/ or scripts/. Not for
  manuscripts; that is scifi-review.
allowed-tools: Read, Glob, Grep, Agent
---

# system-design-review

The rubric is `rubric.md` in this folder. The work is done by the `design-reviewer` agent
(`agents/design-reviewer.md`, inherit model, medium effort); this skill only briefs it and
relays the result, so there is one route for the audit.

## Procedure

1. List the files that changed (from the user, or `git diff --name-only` when available),
   plus `docs/protocol.md`, which every component is written against.
2. Dispatch `design-reviewer` with a SciFi brief (protocol section 3): objective "audit the
   listed files against rubric.md", inputs as absolute paths, output contract the envelope
   path under the repo's `.claude/state/` or a temp folder, non-goals "do not edit".
3. Relay the findings grouped by dimension, FAIL first, each with file, line, fail signal
   and fix. Resolve every FAIL before merging; note the rest in `CHANGELOG.md`.

The rubric applies to any Claude Code skill and agent system, not only SciFi.
