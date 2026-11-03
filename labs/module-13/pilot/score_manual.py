"""Score a manual-assistant run (lesson 13.5) and write a markdown report to reports/.

    python score_manual.py runs/search-drive-test.csv
    python score_manual.py runs/rag-pack-test-claude-sonnet-5-5.csv --model claude-sonnet-5-5
    python score_manual.py --sheet my-scoring-sheet-60.csv          # Track A: your filled spreadsheet

A question is right when the behaviour is right (answer / route / clarify) and, for answers, every gold
fact is present (or, where there are none, the gold document is cited) and no outdated fact is present.
Language (the answer's script matches the question's) is reported separately. Negative-test runs are
listed for you to judge by hand against `pass_if`. Standard library only, plus fieldkit.cost for cost.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from manual_lib import HERE, check, read_csv

sys.path.insert(0, str(HERE.parents[1] / "common"))

USD_ILS = 3.136  # Bank of Israel representative rate, 2 November 2026 (used throughout module 13)


def pct(xs: list) -> str:
    xs = [x for x in xs if x is not None]
    return f"{100 * sum(xs) / len(xs):.1f}% ({sum(xs)}/{len(xs)})" if xs else "—"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("run", nargs="?", type=Path)
    ap.add_argument("--sheet", type=Path)
    ap.add_argument("--model")
    ap.add_argument("--price-in", type=float)
    ap.add_argument("--price-out", type=float)
    a = ap.parse_args()
    if a.sheet:
        rows = read_csv(a.sheet)
        run = [{"qid": r["qid"], "behaviour": r["your_behaviour"], "answer": r["your_answer"],
                "sources": r["your_sources"], "input_tokens": "0", "output_tokens": "0"} for r in rows]
        name = a.sheet.stem
    else:
        run = read_csv(a.run)
        name = a.run.stem
    lines = [f"# Score: {name}", ""]
    if run and run[0]["qid"].startswith("N"):
        neg = {r["nid"]: r for r in read_csv(HERE / "negative-tests.csv")}
        lines += ["Negative tests: judge each answer by hand against `pass_if`.", "",
                  "| Test | Prompt (gloss) | Pass if | Behaviour | Answer |", "|---|---|---|---|---|"]
        for r in run:
            n = neg[r["qid"]]
            lines.append(f"| {r['qid']} | {n['english_gloss'] or n['prompt']} | {n['pass_if']} | {r['behaviour']} | "
                         f"{r['answer'][:160]} |")
    else:
        items = {r["qid"]: r for r in read_csv(HERE / "test-set.csv")}
        res = []
        for r in run:
            it = items[r["qid"]]
            c = check(it, r["behaviour"], r["answer"], r["sources"])
            res.append({**c, "language": it["language"], "expected": it["expected_behaviour"]})
        lines += [f"Questions: {len(res)}", "", f"**Right overall: {pct([x['right'] for x in res])}**", "",
                  "| Group | Right | Behaviour right | Facts present (answers) | Outdated fact present | Source cited (answers) | Answer in the question's language |",
                  "|---|---|---|---|---|---|---|"]
        groups = [("all", res)] + [(f"expected {b}", [x for x in res if x["expected"] == b]) for b in ("answer", "route", "clarify")]
        groups += [(f"language {l}", [x for x in res if x["language"] == l]) for l in ("he", "ar", "ru", "en")]
        for g, xs in groups:
            if xs:
                lines.append(f"| {g} | {pct([x['right'] for x in xs])} | {pct([x['behaviour_ok'] for x in xs])} | "
                             f"{pct([x['facts_ok'] for x in xs if x['expected'] == 'answer'])} | "
                             f"{pct([x['stale_present'] for x in xs])} | "
                             f"{pct([x['source_ok'] for x in xs if x['expected'] == 'answer'])} | "
                             f"{pct([x['language_ok'] for x in xs])} |")
    tin = sum(int(r.get("input_tokens") or 0) for r in run)
    tout = sum(int(r.get("output_tokens") or 0) for r in run)
    if tin and (a.model or a.price_in):
        from fieldkit.cost import token_cost
        usd = token_cost(tin, tout, a.model, a.price_in, a.price_out)
        lines += ["", f"Tokens in/out: {tin:,}/{tout:,}. Cost US${usd:.3f} (₪{usd * USD_ILS:.2f} at ₪{USD_ILS}/US$), "
                  f"₪{usd * USD_ILS / len(run):.3f} a question."]
    report = "\n".join(lines) + "\n"
    out = HERE / "reports" / f"{name}.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
