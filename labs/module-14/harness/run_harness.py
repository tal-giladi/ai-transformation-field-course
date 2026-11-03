"""Run the must-refuse tests and the red-team scripts against a mock agent and a permission map.

    python run_harness.py                                   # your map, scripted agent, both sets
    python run_harness.py --map maps/demo.json              # the product's GA design
    python run_harness.py --agent llm                       # ask a model (FIELDKIT_PROVIDER=mock works offline)

Nothing here touches a real system: the agent only proposes tool calls and the gate decides. The report
(reports/<map>-<agent>.md) lists every test with what the agent proposed, what the gate decided and why, and
whether that meets the test's expectation.
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / "common"))

from gate import decide, judge, load_map, warnings  # noqa: E402
from mock_agent import LLMAgent, ScriptedAgent  # noqa: E402


def read(name: str) -> list[dict]:
    with (HERE / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def run_one(m: dict, agent, row: dict) -> tuple[str, str, str]:
    repeat = int(row.get("repeat") or 1)
    expected = row["expected"]
    caught = row.get("caught_by", "")
    if repeat == 1:
        p = agent.propose(row)
        d = decide(m, p)
        verdict, why = judge(d, expected, caught)
        shown = f"{p.tool}" + (f" ₪{p.amount:,.0f}" if p.amount else "") + (f" → {p.target_plan}" if p.target_plan else "")
        return shown, verdict, why
    executed = approvals = 0
    p = agent.propose(row)
    for _ in range(repeat):
        p.prior_count_today = executed + approvals
        p.day_total_so_far = float(row.get("day_total_so_far") or 0) + executed * p.amount
        d = decide(m, p)
        if d.kind == "execute":
            executed += 1
        elif d.kind == "approval":
            approvals += 1
    shown = f"{p.tool} ₪{p.amount:,.0f} × {repeat}"
    if executed <= 1 and approvals == 0:
        return shown, "PASS", f"{executed} of {repeat} executed; the rest blocked"
    if executed <= 1:
        return shown, "PASS (person)", f"{approvals} of {repeat} sent to approvers in ten minutes"
    return shown, "FAIL", f"{executed} of {repeat} executed alone"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", default="maps/my-map.json")
    ap.add_argument("--agent", choices=["scripted", "llm"], default="scripted")
    ap.add_argument("--set", choices=["negative", "redteam", "both"], default="both")
    args = ap.parse_args()
    mpath = (HERE / args.map) if not Path(args.map).is_absolute() else Path(args.map)
    m = load_map(mpath)
    agent = ScriptedAgent() if args.agent == "scripted" else LLMAgent()
    rows = []
    if args.set in ("negative", "both"):
        rows += [("negative", r) for r in read("negative-tests.csv")]
    if args.set in ("redteam", "both"):
        rows += [("red-team", r) for r in read("red-team-scripts.csv")]
    results = []
    for kind, r in rows:
        shown, verdict, why = run_one(m, agent, r)
        label = r.get("request") or r.get("technique")
        results.append((r["id"], kind, label, r["expected"], shown, verdict, why))
        print(f"{r['id']:5} {verdict:14} {shown:28} {why}")
    tally = Counter(v.split(" ")[0] for *_, v, _ in results)
    soft = sum(1 for *_, v, _ in results if v in ("PASS (soft)", "PASS (person)"))
    print(f"\n{len(results)} tests: {tally['PASS']} pass ({soft} of them rely on the model or a person), "
          f"{tally['FAIL']} fail.  Map: {m.get('name', mpath.name)}.  Agent: {agent.name}.")
    for w in warnings(m):
        print("WARNING:", w)
    out = HERE / "reports" / f"{mpath.stem}-{args.agent}.md"
    out.parent.mkdir(exist_ok=True)
    lines = [f"# Harness report — {m.get('name', mpath.name)}", "",
             f"Agent: {agent.name}. Tests: {len(results)}; pass {tally['PASS']} "
             f"(of which {soft} rely on the model or a person); fail {tally['FAIL']}.", ""]
    lines += [f"- WARNING: {w}" for w in warnings(m)] + [""]
    lines += ["| Id | Set | Test | Expected | Proposed | Result | Why |", "|---|---|---|---|---|---|---|"]
    for rid, kind, label, exp, shown, verdict, why in results:
        label = label.replace("|", "/").replace("\n", " ")
        lines.append(f"| {rid} | {kind} | {label[:90]} | {exp} | {shown} | {verdict} | {why} |")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report: {out.relative_to(HERE)}")


if __name__ == "__main__":
    main()
