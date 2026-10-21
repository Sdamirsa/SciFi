---
name: panel-discussion
description: "This skill should be used when the user says 'panel discussion,' 'expert deliberation,' 'let's debate this,' 'what would experts think,' 'simulate a discussion,' or wants to name something, choose between approaches, debate framing, or make strategic research decisions. Simulates a multi-round expert panel deliberation with diverse perspectives."
version: 1.0.0
---

# Panel Discussion

A facilitator running structured multi-round expert deliberation. This technique produces higher-quality decisions than individual reasoning by forcing diverse perspectives to confront each other, vote independently, and converge through argumentation rather than authority.

## When to Use

Any decision where multiple expert lenses would help: naming decisions, methodology choices, framing debates, strategic choices, design decisions.

## Setup

### Step 1: Understand the Decision

What decision? What constraints? Who is the audience? Any candidates already?

### Step 2: Configure the Panel (5-7 panelists)

Default for scientific/research decisions:

```
1. Journal Editor-in-Chief    -- Publication standards, searchability, field norms
2. Domain Pioneer             -- Historical context, scientific rigor, nomenclature
3. AI/Tech Visionary          -- Technical accuracy, future-proofing, adoption
4. Pragmatic Engineer         -- Simplicity, memorability, practical deployment
5. Clinical End-User          -- Real-world relevance, patient impact, workflow
6. Senior Mentor/Director     -- Institutional perspective, career, strategy
7. Claude (AI Perspective)    -- Synthesis, pattern recognition, contrarian analysis
```

Adapt to domain. Always include at least one contrarian and one end-user voice.

### Step 3: Context Brief

3-5 sentences all panelists share: what the thing is, what it does, who it serves, non-negotiable constraints.

## The Deliberation Protocol

### Round 1: Proposals (divergent)

Each panelist proposes 3-5 candidates with one-sentence rationale. Goal: breadth. Expect 20-35 proposals.

### Round 2: Discussion (convergent)

Each panelist reviews all Round 1 proposals, comments on 3-5. Argues from expertise. Surface the 5-8 strongest candidates.

### Round 3: Independent Voting

Each panelist ranks top 3 (3pts, 2pts, 1pt). Voting must be independent. Present a scoreboard.

### Round 4: Responsive Discussion (if needed)

If the user pushes back or adds constraints, run a focused round addressing the specific concern.

### Round 5: Final Convergence (if needed)

One more vote on the refined shortlist. Present: primary choice, alternative, simple/informal variant.

## Key Principles

**Independence matters.** Each panelist votes on own reasoning. If everyone agrees with the loudest voice, the result is worse than thinking alone.

**Respect user constraints.** When the user introduces new information, pivot the discussion.

**Diversity of perspective.** Each panelist brings a viewpoint that would genuinely change the decision. Remove overlapping perspectives.

**Real personality.** Distinct voices surface distinct concerns.

**Convergence is not forced.** A split decision with clear reasoning is more useful than false consensus.

## Output Format

```markdown
# [Decision Topic] -- Panel Discussion

## Context / ## Panelists
---
## Round 1: Proposals
## Round 2: Discussion
## Round 3: Independent Voting (scoreboard)
## Round 4: [If triggered] / ## Round 5: Final Vote
---
## Final Recommendation
**Primary:** ... / **Alternative:** ... / **Simple variant:** ...
```

## Integration

Standalone skill invocable by the user, by `scifi` or `scifi-literature`, or by any skill facing a decision that benefits from diverse reasoning.
