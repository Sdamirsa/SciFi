# Building the library (stage 0)

The library is the foundation of the paper. What is not in it cannot be cited, checked or
argued against. This stage is a conversation between the master and the human, guided like a
research librarian and methodologist would guide it. The output is a search plan in
`Thinking-space/scratch/search-plan.md` and an organised Zotero collection connected to the
workspace by one of the two routes in `docs/zotero-guide.md`.

## What AI cannot do here

Be honest with the human about this. No AI tool currently does paper discovery reliably.
Claude, ChatGPT, Scispace and similar tools cannot consistently find full-text PDFs,
distinguish original results from speculation, cover the full breadth of a niche field, or
replace the mental map built by reading abstracts. Citation-network tools such as Litmap (with
Zotero sync) are the best specialised help as of 2026, because they map who cites whom rather
than guess. The system helps plan, organise, check coverage and read what the human has
collected. The human finds and reads.

## Step 1: define the search scope

Write the field hierarchy with the human:

```
Broad context:     the broad discipline
Adjacent fields:   a neighbouring methodology or application area
Specific topic:    the specific problem or sub-field
Your niche:        the precise contribution of this paper
```

Each level needs at least one good review. When `spine.json` exists, the niche is its central
claim and the specific topic is its gap.

## Step 2: reviews first (one or two per level)

PubMed with the Article Type filter (Review, Systematic Review), Google Scholar with "review"
or "systematic review", the reference lists of known papers, citation-network clusters.

## Step 3: original articles

Forward and backward citation tracking from the reviews and the key papers, keyword searches
across PubMed, Google Scholar, IEEE Xplore and arXiv, reference lists of the reviews,
citation-network maps. Import each paper into Zotero with its full-text PDF.

## Step 4: two or three role model papers

Papers that guide tone, structure, figure design and presentation. A good role model is
published in the target journal (or one of similar standing), asks a similar type of
question, has clear figures, and is recent enough to reflect current reporting standards. The
journal profile in `skills/scientific-writing/references/journal-profiles.md` says what the
target journal expects. Role models inform `scifi-skeleton` and `scifi-figures`.

## Step 5: organise the Zotero collection

One collection per paper, with these subcollections:

```
<Paper> Collection/
  Original        all relevant original research articles
  Reviews         reviews and perspectives (one or two per field level)
  Role Models     two or three papers guiding this paper's design
  Logic           papers holding a logical statement the paper needs to cite
  Interesting     papers with an interesting angle
  Maybe           uncertain relevance, kept for now
```

Tags: `solid`, `role-model`, `full-text-not-found`, plus domain tags the human chooses.
`full-text-not-found` is the list the lookup role will turn into NEEDs.

Export the parent collection (it includes the subcollections) so `library.json` holds every
key the manuscript might cite.

## Step 6: read and build the mental map

Reading order: reviews (the landscape), role models (design), originals (detail). Rough notes
per paper on contribution and gaps. Stage 1 turns these into structured notes, but the human's
own reading comes first.

## Checkpoint

Before stage 1, confirm with the human:

- search scope written for all four levels, with reviews at each
- role models chosen and representative of the target journal
- PDFs attached, or the paper tagged `full-text-not-found`
- collection organised as above
- one route connected and checked (`bbt_check.py` on the export route, a test search on the
  MCP route)

## What the system can help with

Refine search terms and synonyms, suggest which levels lack a review, judge collection
completeness against the spine's threads (each thread needs sources for its opening and
closing), organise the Zotero structure, find coverage gaps, and draft a search protocol
(databases, strings, dates, inclusion rules) for the Methods when the paper needs one.
