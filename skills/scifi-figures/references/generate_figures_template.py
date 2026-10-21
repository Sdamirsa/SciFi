#!/usr/bin/env python3
"""Skeleton for a reproducible SciFi figure script (scifi-figures, both modes).

Copy this file to Thinking-space/figures/generate_figures.py and add one function per
figure in figures.json. Standards: references/figure-standards.md (same folder).

Usage:
    python3 generate_figures_template.py --demo [--out DIR]
    python3 generate_figures_template.py --labels Literature/labels/all_papers.json \
        [--ontology Literature/ontology.yaml] [--subtheme T1-S1_Algorithm] [--out DIR]
    python3 generate_figures_template.py --results Manuscript/figures/primary.json [--out DIR]

Inputs:
    --labels    CrystaLit labels: a list of paper objects (or an object keyed by paper id),
                each {"paper_id", "title", "<Theme>": {"<Subtheme>": [concepts]}}.
    --ontology  YAML ontology (themes > subthemes > groups > concepts). Optional; adds
                concepts no paper uses as zero bars. Needs PyYAML; skipped with a warning
                if PyYAML is missing.
    --results   JSON list of {"group", "arm", "estimate", "lo", "hi", "n", "N"} rows
                (estimate and CI bounds in the unit of the y axis, here percent).
    --demo      Ignore inputs and use a tiny synthetic dataset (all numbers invented).
    --out       Output folder (default: a new temporary folder, printed at the end).

Each figure is saved as <out>/<name>.pdf (vector) and <out>/<name>.png (300 dpi).
Running twice with the same inputs gives identical files (fixed metadata, no timestamps).
Exit 0 on success, 1 on bad arguments or unreadable input, 2 if no figure was written.

Path of this template:
    plugin:  ${CLAUDE_PLUGIN_ROOT}/skills/scifi-figures/references/generate_figures_template.py
    copied:  .claude/skills/scifi-figures/references/generate_figures_template.py
"""
import argparse
import json
import sys
import tempfile
from collections import Counter
from pathlib import Path

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
except ImportError:  # pragma: no cover
    sys.exit("matplotlib is required: pip install matplotlib")

try:
    import yaml  # optional, only for --ontology
except ImportError:
    yaml = None

# ---------------------------------------------------------------- constants
DPI = 300
CM = 1 / 2.54
WIDTH_SINGLE = 8.5 * CM      # single column
WIDTH_DOUBLE = 17.0 * CM     # double column (check the journal profile)
FONT = ["Arial", "Helvetica", "DejaVu Sans"]
SIZE_AXIS, SIZE_TICK, SIZE_LEGEND, SIZE_ANNOT = 9, 8, 8, 8
PANEL_CASE = "lower"         # "lower" (a, b: Nature, npj) or "upper" (A, B: Lancet, JAMIA, EHJ)
MAXLEN = 22                  # label truncation after abbreviation

# One fixed colour per arm across every figure in the paper (Okabe-Ito based).
ARM_COLOURS = {
    "Proposed": "#D55E00",   # the paper's own method: one warm colour
    "Comparator": "#0072B2", # the main comparator: one cool colour
    "Baseline": "#7F7F7F",   # other baselines: greys
}
CATEGORICAL = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7",
               "#56B4E9", "#F0E442", "#000000"]
NEUTRAL = "#4D4D4D"

# Long ontology or variable names to the abbreviations defined in the caption.
ABBREV_MAP = {
    "Large_Language_Model": "LLM",
    "Retrieval_Augmented_Generation": "RAG",
    "Rule_Based_System": "Rule-based",
    "Named_Entity_Recognition": "NER",
}

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": FONT,
    "font.size": SIZE_TICK,
    "axes.labelsize": SIZE_AXIS,
    "xtick.labelsize": SIZE_TICK,
    "ytick.labelsize": SIZE_TICK,
    "legend.fontsize": SIZE_LEGEND,
    "legend.frameon": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": False,
    "pdf.fonttype": 42,          # editable text in the PDF
    "svg.hashsalt": "scifi",
    "savefig.dpi": DPI,
})


# ---------------------------------------------------------------- helpers
def label(name, maxlen=MAXLEN):
    """Abbreviate, replace underscores, then truncate with an ellipsis."""
    text = ABBREV_MAP.get(name, name).replace("_", " ")
    return text if len(text) <= maxlen else text[: maxlen - 1] + "…"


def panel_letter(ax, index):
    """Bold panel letter in the journal's case, top left outside the axes."""
    letter = "abcdefghij"[index]
    letter = letter.upper() if PANEL_CASE == "upper" else letter
    ax.text(-0.12, 1.04, letter, transform=ax.transAxes, fontsize=SIZE_AXIS + 1,
            fontweight="bold", va="bottom", ha="left")


def save_fig(fig, name, out):
    """Save one figure as vector PDF and 300 dpi PNG; return both paths."""
    out.mkdir(parents=True, exist_ok=True)
    paths = []
    for ext, meta in (("pdf", {"CreationDate": None, "ModDate": None}), ("png", {"Software": None})):
        path = out / f"{name}.{ext}"
        fig.savefig(path, bbox_inches="tight", pad_inches=0.02, metadata=meta)
        paths.append(path)
    plt.close(fig)
    print(f"  wrote {paths[0].name} and {paths[1].name}")
    return paths


# ---------------------------------------------------------------- loaders
def load_labels(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = [data] if "paper_id" in data else list(data.values())
    papers = [p for p in data if isinstance(p, dict)]
    if not papers:
        raise ValueError(f"{path} holds no paper objects")
    return papers


def load_ontology_concepts(path):
    """Return {subtheme: [concepts]} from the ontology, or {} if unavailable."""
    if not path:
        return {}
    if yaml is None:
        print("  warning: PyYAML missing, ontology skipped (pip install pyyaml)", file=sys.stderr)
        return {}
    onto = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    out = {}
    for theme in (onto.get("themes") or {}).values():
        for sub_name, sub in (theme.get("subthemes") or {}).items():
            concepts = []
            for group in (sub.get("groups") or {}).values():
                concepts.extend(group.get("concepts") or [])
            concepts.extend(sub.get("concepts") or [])
            out[sub_name] = concepts
    return out


def concept_counts(papers, subtheme=None):
    """Count papers per concept, within one subtheme or across all."""
    counts = Counter()
    for paper in papers:
        for key, theme in paper.items():
            if not isinstance(theme, dict):
                continue
            for sub_name, concepts in theme.items():
                if subtheme and sub_name != subtheme:
                    continue
                if isinstance(concepts, list):
                    counts.update(set(concepts))
    return counts


def demo_labels():
    """Six invented papers in the CrystaLit label format."""
    algos = [["Large_Language_Model"], ["Large_Language_Model", "Retrieval_Augmented_Generation"],
             ["Rule_Based_System"], ["Large_Language_Model"], ["Named_Entity_Recognition"],
             ["Large_Language_Model", "Rule_Based_System"]]
    return [{"paper_id": f"Demo_{i}", "title": f"Invented paper {i}",
             "T1_Methods": {"T1-S1_Algorithm": a}} for i, a in enumerate(algos, 1)]


def demo_results():
    """Invented accuracy (%) with 95% CI for two arms at two centres."""
    return [
        {"group": "Centre A", "arm": "Proposed", "estimate": 96.8, "lo": 95.3, "hi": 97.9, "n": 581, "N": 600},
        {"group": "Centre A", "arm": "Comparator", "estimate": 89.5, "lo": 86.8, "hi": 91.8, "n": 537, "N": 600},
        {"group": "Centre B", "arm": "Proposed", "estimate": 95.8, "lo": 94.0, "hi": 97.2, "n": 575, "N": 600},
        {"group": "Centre B", "arm": "Comparator", "estimate": 87.8, "lo": 85.0, "hi": 90.3, "n": 527, "N": 600},
    ]


# ---------------------------------------------------------------- figures
def fig_concept_frequency(papers, out, subtheme=None, ontology=None, top=15):
    """Horizontal bar of papers per concept, sorted descending, values on bars."""
    counts = concept_counts(papers, subtheme)
    for concept in (ontology or {}).get(subtheme, []):
        counts.setdefault(concept, 0)          # unused concepts show as zero
    if not counts:
        print(f"  skipped concept frequency: no concepts for {subtheme or 'any subtheme'}")
        return None
    items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:top]
    names = [label(k) for k, _ in items][::-1]
    values = [v for _, v in items][::-1]
    fig, ax = plt.subplots(figsize=(WIDTH_SINGLE, 0.45 * CM * len(items) + 1.5 * CM))
    bars = ax.barh(names, values, color=CATEGORICAL[0], height=0.7)
    for bar, value in zip(bars, values):
        ax.text(bar.get_width() + max(values) * 0.01, bar.get_y() + bar.get_height() / 2,
                f"{value}", va="center", fontsize=SIZE_ANNOT)
    ax.set_xlabel(f"Papers (n of {len(papers)})")
    ax.set_xlim(0, max(max(values), 1) * 1.15)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    slug = (subtheme or "all").lower().replace("-", "_")
    return save_fig(fig, f"corpus_concepts_{slug}", out)


def fig_grouped_bar_ci(rows, out, ylabel="Accuracy (%)", name="primary_grouped_bar"):
    """Grouped bars per group and arm, 95% CI error bars, estimate and n/N printed."""
    groups = list(dict.fromkeys(r["group"] for r in rows))
    arms = list(dict.fromkeys(r["arm"] for r in rows))
    width = 0.8 / len(arms)
    fig, ax = plt.subplots(figsize=(WIDTH_SINGLE, 6.5 * CM))
    for j, arm in enumerate(arms):
        sub = {r["group"]: r for r in rows if r["arm"] == arm}
        xs = [i + (j - (len(arms) - 1) / 2) * width for i in range(len(groups))]
        est = [sub[g]["estimate"] for g in groups]
        err = [[sub[g]["estimate"] - sub[g]["lo"] for g in groups],
               [sub[g]["hi"] - sub[g]["estimate"] for g in groups]]
        colour = ARM_COLOURS.get(arm, CATEGORICAL[j % len(CATEGORICAL)])
        ax.bar(xs, est, width * 0.92, color=colour, label=label(arm),
               yerr=err, capsize=2, error_kw={"elinewidth": 0.8, "ecolor": NEUTRAL})
        for x, g in zip(xs, groups):
            r = sub[g]
            text = f"{r['estimate']:.1f}"
            if "n" in r and "N" in r:
                text += f"\n{r['n']}/{r['N']}"
            ax.text(x, 2, text, ha="center", va="bottom", fontsize=SIZE_ANNOT - 1, color="white")
    ax.set_xticks(range(len(groups)), groups)
    ax.set_ylabel(ylabel)
    ax.set_ylim(0, 105)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.12), ncol=len(arms))
    panel_letter(ax, 0)
    return save_fig(fig, name, out)


# ---------------------------------------------------------------- main
def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--labels")
    p.add_argument("--ontology")
    p.add_argument("--subtheme")
    p.add_argument("--results")
    p.add_argument("--demo", action="store_true")
    p.add_argument("--out")
    args = p.parse_args(argv)

    out = Path(args.out) if args.out else Path(tempfile.mkdtemp(prefix="scifi_figures_"))
    written = []
    try:
        if args.demo or not (args.labels or args.results):
            if not args.demo:
                print("No input given, using the invented demo dataset.")
            papers, rows, subtheme = demo_labels(), demo_results(), "T1-S1_Algorithm"
            ontology = {}
        else:
            papers = load_labels(args.labels) if args.labels else []
            rows = json.loads(Path(args.results).read_text(encoding="utf-8")) if args.results else []
            subtheme = args.subtheme
            ontology = load_ontology_concepts(args.ontology)
    except (OSError, ValueError) as exc:
        print(f"error: cannot read input: {exc}", file=sys.stderr)
        return 1

    print(f"Writing figures to {out}")
    if papers:
        written.append(fig_concept_frequency(papers, out, subtheme, ontology))
    if rows:
        written.append(fig_grouped_bar_ci(rows, out))
    written = [w for w in written if w]
    if not written:
        print("error: no figure written", file=sys.stderr)
        return 2
    print(f"Done: {len(written)} figures, {2 * len(written)} files in {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
