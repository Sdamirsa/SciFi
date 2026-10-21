#!/usr/bin/env python3
"""statectl for the SciFi master: the one way to change Thinking-space/STATE.json and append
to log/decisions.jsonl. Stdlib only. Every write is validated against state.schema.json first
(via validate_json.py in this folder) and refreshes updated_at; an invalid result is refused.

Usage:
    python3 state.py [--workspace DIR] show
    python3 state.py [--workspace DIR] next "<action>"
    python3 state.py [--workspace DIR] pointer "<text>"          ("" clears it)
    python3 state.py [--workspace DIR] unit <id> <status>        (also sets current_unit)
    python3 state.py [--workspace DIR] stage <stage>
    python3 state.py [--workspace DIR] decision --stage S --decision D --by human|master|both --why W
                                                [--unit U] [--options A B ...] [--artifacts P ...]
    python3 state.py [--workspace DIR] need add|clear "<text>"
    python3 state.py [--workspace DIR] session                   (count one session; for the master)
    python3 state.py [--workspace DIR] ritual                    (record a /project-memory run)

As a plugin:  python3 "${CLAUDE_PLUGIN_ROOT}/scripts/state.py" ...
Copied:       python3 .claude/scripts/state.py ...

--workspace defaults to the current directory (or the one child folder holding
Thinking-space/STATE.json). Exit 0 on success, 1 on usage error or missing workspace, 2 when
the change would make STATE.json invalid.
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _scifi  # noqa: E402

STAGES = ["init", "spine", "skeleton", "figures", "paragraphs", "review", "done"]
UNIT_STATUSES = ["planned", "mapped", "drafted", "reviewed", "accepted", "human-edited", "blocked"]


def build_parser():
    ap = argparse.ArgumentParser(prog="state.py", description="Change SciFi STATE.json safely.")
    ap.add_argument("--workspace", default=None, help="workspace folder (default: cwd)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("show")
    p = sub.add_parser("next"); p.add_argument("action")
    p = sub.add_parser("pointer"); p.add_argument("text")
    p = sub.add_parser("unit"); p.add_argument("id"); p.add_argument("status", choices=UNIT_STATUSES)
    p = sub.add_parser("stage"); p.add_argument("stage", choices=STAGES)
    p = sub.add_parser("decision")
    p.add_argument("--stage", required=True, choices=STAGES)
    p.add_argument("--unit", default="")
    p.add_argument("--decision", required=True)
    p.add_argument("--by", required=True, choices=["human", "master", "both"])
    p.add_argument("--why", required=True)
    p.add_argument("--options", nargs="*", default=[])
    p.add_argument("--artifacts", nargs="*", default=[])
    p = sub.add_parser("need"); p.add_argument("op", choices=["add", "clear"]); p.add_argument("text")
    sub.add_parser("session")
    sub.add_parser("ritual")
    return ap


def main(argv=None):
    import sys as _sys
    argv = list(_sys.argv[1:] if argv is None else argv)
    # accept --workspace before or after the subcommand
    ws = None
    if "--workspace" in argv:
        i = argv.index("--workspace")
        ws = argv[i + 1]
        del argv[i:i + 2]
    args = build_parser().parse_args(argv)
    if ws is not None:
        args.workspace = ws
    ws = _scifi.find_workspace(args.workspace or Path.cwd())
    if ws is None:
        print(f"no Thinking-space/STATE.json at {args.workspace or Path.cwd()}; run init_workspace.py first",
              file=sys.stderr)
        return 1
    try:
        st = _scifi.load_state(ws)
    except Exception as exc:
        print(f"cannot read STATE.json: {exc}", file=sys.stderr)
        return 1

    if args.cmd == "show":
        print(json.dumps(st, indent=2, ensure_ascii=False))
        return 0

    if args.cmd == "decision":
        row = {"ts": _scifi.now_iso(), "stage": args.stage, "unit": args.unit, "decision": args.decision,
               "decided_by": args.by, "options": args.options, "why": args.why, "artifacts": args.artifacts}
        _scifi.append_jsonl(ws / _scifi.DECISIONS_REL, row)
        try:
            _scifi.write_state(ws, st)  # refresh updated_at
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2
        print(f"decision logged: {args.stage} {args.unit or '-'} {args.decision}")
        return 0

    if args.cmd == "next":
        st["next_action"] = args.action
    elif args.cmd == "pointer":
        st["pointer"] = args.text
        if args.text:
            st["pointer_at"] = _scifi.now_iso()
        else:
            st.pop("pointer_at", None)
    elif args.cmd == "unit":
        units = st.get("units")
        if not isinstance(units, dict):
            units = {}
        units[args.id] = args.status
        st["units"] = units
        st["current_unit"] = args.id
    elif args.cmd == "stage":
        st["stage"] = args.stage
    elif args.cmd == "need":
        needs = [n for n in (st.get("open_needs") or []) if isinstance(n, str)]
        if args.op == "add":
            if args.text not in needs:
                needs.append(args.text)
        else:
            if args.text not in needs:
                print(f"no open NEED equal to {args.text!r}; open: {needs}", file=sys.stderr)
                return 1
            needs.remove(args.text)
        st["open_needs"] = needs
    elif args.cmd == "session":
        sc = st.get("session_count")
        st["session_count"] = (sc if isinstance(sc, int) and not isinstance(sc, bool) else 0) + 1
    elif args.cmd == "ritual":
        st["last_ritual"] = _scifi.now_iso()
        st["session_count"] = 0

    try:
        _scifi.write_state(ws, st)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(f"STATE.json updated ({args.cmd})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
