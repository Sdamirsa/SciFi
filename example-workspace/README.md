<!-- Everything in this folder is invented for illustration. The study, data, people, sources and DOIs are fictional. -->

# Example workspace

This folder shows a SciFi workspace partway through writing a paper. Open it to see where everything goes and what each file looks like before you set up your own.

The study is invented. An open-weight language model with 70 billion parameters extracts valvular heart disease severity from 1,200 echocardiography reports at two Swiss centres, compared with a rule-based system and labelled by two cardiologists. The target journal is The Lancet Digital Health. No number, person, reference or DOI here is real, and every file says so in its first line.

## What you put where

| Folder | Who writes it | What goes in |
|---|---|---|
| `Manuscript/` | you | one Markdown file per section, with `[@citekey]` citations, plus `figures/` (data files) and `tables/` |
| `Literature/` | you (or Zotero) | `library.json`, a Better CSL JSON export of the cited papers, and `fulltext/<citekey>.pdf` or `.md` |

The system never edits these two folders. It drafts in `Thinking-space/units/` and you copy an accepted draft into `Manuscript/` (or ask the master to, which it does only on your explicit instruction and after a `.bak` copy).

## What the system makes

| Folder | What it holds |
|---|---|
| `Thinking-space/` | the state, spine, skeleton, figure plan, unit maps and drafts, agent briefs and replies, review comments, the decisions log and scratch work |
| `.claude/` | the memory spine for the next session: `STATUS.md`, `Project-log.jsonl`, `LESSONS.jsonl` |

The file formats are defined in `docs/protocol.md` of the SciFi repository. Every JSON file here passes `scripts/validate_json.py`.

## How to start

Copy the folder so the original stays clean, open Claude Code in the parent folder and type the command.

```bash
cp -r /path/to/SciFi/example-workspace ~/scifi-demo/example-workspace
cd ~/scifi-demo && claude
```

```
/scifi example-workspace co-thinker lancet
```

The arguments are the workspace, the control mode and the journal. The master names the journal and the literature route, then states its plan in three lines.

## How to resume

Open Claude Code again in the same folder. The session-start hook prints where you stopped, read from `Thinking-space/STATE.json`. Type `/scifi` or say "resume my manuscript". The master reads `STATE.json`, the last five lines of `log/decisions.jsonl` and the files of the current unit, then continues from `next_action`. In this example that is copying the accepted d03 draft into the Discussion, answering the d02 comments and supplying one missing full text.

## A walk through the files

Open them in this order.

1. `Manuscript/title.md`. The title and the `Target: lancet` line the master reads for the journal.
2. `Manuscript/abstract.md`, `introduction.md`, `methods.md`, `results.md`, `discussion.md`. Your paper. The Discussion still holds two defects on purpose, a banned word in paragraph 2 and a wrong number (95.4% for 95.8%) in paragraph 3.
3. `Manuscript/tables/table1.md` and `Manuscript/figures/README.md`. A table and the list of planned figure data files.
4. `Literature/library.json` and `Literature/fulltext/`. Eight invented references, two of them with invented full texts.
5. `Thinking-space/STATE.json`. Where the work stands, the status of every unit and the next action.
6. `Thinking-space/scratch/claim-options.md`, then `spine.json`. Three candidate claims and the agreed spine with results R1 to R6, implications I1 to I4 and threads T1 to T4.
7. `Thinking-space/skeleton.json`. The reverse outline. Read the takeaway lines alone and they tell the story.
8. `Thinking-space/figures.json`. The display-item plan with captions.
9. `Thinking-space/units/d03.logic.json`. The claims, evidence and steps of Discussion paragraph 3, including the number that does not match the results.
10. `Thinking-space/briefs/d03.*.r1.json`, then `handshakes/d03.*.r1.json`. What the master sent to the five checkers and what each returned. The evidence-checker raises a NEED for a source without a full text.
11. `Thinking-space/handshakes/d03.synthesis.json`. How the master merged the findings and what was accepted, rejected and deferred.
12. `Thinking-space/briefs/d03.drafter.r1.json`, `handshakes/d03.drafter.r1.json`, then `units/d03.draft.md`. The redraft, with the original kept below `---- previous`.
13. `Thinking-space/handshakes/d03.standards-gate.r1.json`. The gate's PASS.
14. `Thinking-space/comments/d02.json`. Review mode on paragraph 2, which catches the banned word.
15. `Thinking-space/log/decisions.jsonl`. Every gate decision from setup to d03 accepted.
16. `.claude/STATUS.md`, `Project-log.jsonl`, `LESSONS.jsonl`. What the next session reads first, what happened and what not to repeat.

To see the script check that the style-checker runs, try this from the SciFi repository.

```bash
python3 skills/scientific-writing/scripts/check_manuscript.py example-workspace/Manuscript/discussion.md --journal lancet
```

It flags the banned word. It also lists Lancet headings missing from this one-section file, which you can ignore here. The wrong number is found by the global-aligner and the evidence-checker, not by the script, because the script cannot compare sections.
