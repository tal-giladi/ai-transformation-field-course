"""Score a permit-FAQ run (lesson 11.5) and write a markdown report to reports/.

    python score_faq.py runs/search-site-test.csv --today       # + Moked 106 today (mystery shopper)
    python score_faq.py runs/rag-pack-test-claude-sonnet-5-5.csv --model claude-sonnet-5-5
    python score_faq.py runs/rag-pack-negative-<model>.csv
    python score_faq.py --sheet my-scoring-sheet-80.csv          # Track A: your filled spreadsheet

A question counts as right when the behaviour is right (answer / clarify / route) and, for answers,
every gold fact is present, no outdated fact is present and a source on the right topic is cited.
Language is scored separately. Needs pandas and tabulate (labs/common/requirements.txt).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

from faq_lib import HERE, ROOM, check_answer, read_csv

sys.path.insert(0, str(HERE.parents[1] / "common"))
from fieldkit.cost import token_cost  # noqa: E402
from fieldkit.evals import by_group  # noqa: E402

USD_ILS = 3.136  # Bank of Israel representative rate, 2 November 2026


def pct(s: pd.Series) -> str:
    s = s.dropna()
    return f"{100 * s.mean():.1f}% (n = {len(s)})" if len(s) else "—"


def load_items(run_ids: set[str]) -> dict:
    items = {r["question_id"]: r for r in read_csv(HERE / "test-set.csv")}
    for r in read_csv(HERE / "negative-tests.csv"):
        r["question_id"] = r["test_id"]
        items[r["question_id"]] = r
    return {k: v for k, v in items.items() if k in run_ids}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("run", nargs="?", type=Path)
    ap.add_argument("--sheet", type=Path, help="a filled copy of scoring-sheet-80.csv (Track A)")
    ap.add_argument("--today", action="store_true", help="compare with the mystery-shopper calls")
    ap.add_argument("--model", help="model id in fieldkit.cost.PRICES, for cost per question")
    ap.add_argument("--price-in", type=float)
    ap.add_argument("--price-out", type=float)
    args = ap.parse_args()
    if args.sheet:
        sheet = pd.read_csv(args.sheet, dtype=str, keep_default_na=False)
        run = sheet.rename(columns={"your_behaviour": "behaviour", "your_answer": "answer", "your_sources": "sources"})
        name = args.sheet.stem
    else:
        run = pd.read_csv(args.run, dtype=str, keep_default_na=False)
        name = args.run.stem
    items = load_items(set(run["question_id"]))
    rows = []
    for rec in run.to_dict("records"):
        it = items[rec["question_id"]]
        res = check_answer(it, rec)
        rows.append({"question_id": rec["question_id"], "language": it["language"],
                     "expected": it["expected_behaviour"], "predicted": rec.get("behaviour", ""),
                     "intent": it.get("intent", it.get("test_id", "")), "changed_2026": it.get("changed_2026", ""),
                     "tokens_in": int(rec.get("tokens_in") or 0), "tokens_out": int(rec.get("tokens_out") or 0),
                     "sources": rec.get("sources", ""), **res})
    df = pd.DataFrame(rows)
    ans = df[df.expected == "answer"]
    lines = [f"# Permit-FAQ eval: {name}", "",
             f"Questions: {len(df)} (answer {len(ans)}, route {(df.expected == 'route').sum()}, "
             f"clarify {(df.expected == 'clarify').sum()}).", "",
             "| Measure | Result |", "|---|---|",
             f"| **Right (behaviour, facts, no outdated fact, source)** | **{pct(df.correct)}** |",
             f"| Behaviour right | {pct(df.behaviour_ok)} |",
             f"| Answer questions: right | {pct(ans.correct)} |",
             f"| Answer questions: gold facts present | {pct(ans.facts_ok.astype('float'))} |",
             f"| Answer questions: outdated fact present | {pct(ans.stale_present.astype('float'))} |",
             f"| Answer questions: source on the right topic | {pct(ans.source_ok.astype('float'))} |",
             f"| Route questions: routed | {pct(df[df.expected == 'route'].behaviour_ok)} |",
             f"| Clarify questions: clarified | {pct(df[df.expected == 'clarify'].behaviour_ok)} |",
             f"| Reply in the question's language (he, ar, ru, en) | {pct(df.language_ok.dropna().astype('float'))} |", ""]
    lines += ["## Right, by language", "", by_group(df, "language").to_markdown(), ""]
    if len(ans) and ans.changed_2026.ne("").any():
        lines += ["## Answer questions, by whether the rule changed in 2026", "",
                  by_group(ans, "changed_2026").to_markdown(), ""]
    lines += ["## Behaviour: expected (rows) vs given (columns)", "",
              pd.crosstab(df.expected, df.predicted.replace("", "(none)"), margins=True,
                          margins_name="total").to_markdown(), ""]
    stale = ans[ans.stale_present.astype(bool)]
    if len(stale):
        lines += [f"## Answers that carry an outdated fact ({len(stale)})", "",
                  stale.groupby(["intent", "language"]).size().rename("n").reset_index().to_markdown(index=False), ""]
    if df.tokens_in.sum():
        model_cost = [token_cost(a, b, model=args.model, price_in=args.price_in, price_out=args.price_out)
                      for a, b in zip(df.tokens_in, df.tokens_out)] if (args.model or args.price_in) else None
        lines += ["## Tokens and cost", "", f"Mean tokens per question: {df.tokens_in.mean():.0f} in, "
                  f"{df.tokens_out.mean():.0f} out."]
        if model_cost:
            per_q = sum(model_cost) / len(model_cost)
            lines += [f"Cost per question: US${per_q:.5f} ≈ ₪{per_q * USD_ILS:.4f} (₪{USD_ILS} per US$, 2 Nov 2026)."]
        lines += [""]
    if args.today:
        ms = pd.read_csv(ROOM / "service" / "mystery-shopper-2026.csv", dtype=str, keep_default_na=False)
        ms = ms[ms.question_id.isin(df.question_id)]
        if len(ms):
            m = ms.merge(df[["question_id", "correct", "expected", "changed_2026"]], on="question_id")
            m["today_correct"] = m.result_code.eq("correct")
            m["served_own"] = m.served_language.eq(m.language_asked)
            lines += ["## Today: Moked 106 mystery-shopper calls on the same questions", "",
                      f"Calls: {len(m)} (August–September 2026). Right today: {pct(m.today_correct)}; "
                      f"this run on the same questions: {pct(m.correct)}.", "",
                      "| Language asked | Calls | Right today | Served in that language | This run right |",
                      "|---|---|---|---|---|"]
            for lang, g in m.groupby("language_asked"):
                lines.append(f"| {lang} | {len(g)} | {100 * g.today_correct.mean():.0f}% | "
                             f"{100 * g.served_own.mean():.0f}% | {100 * g.correct.mean():.0f}% |")
            ch = m[m.expected == "answer"]
            lines += ["", f"Answer questions whose rule changed in 2026: right today "
                      f"{pct(ch[ch.changed_2026 == 'y'].today_correct)}, outdated answer given "
                      f"{(ch[ch.changed_2026 == 'y'].result_code == 'wrong_outdated').sum()} times; unchanged rules: right today "
                      f"{pct(ch[ch.changed_2026 == 'n'].today_correct)}.", ""]
    fails = df[~df.correct].head(20)
    if len(fails):
        lines += ["## First failures", "", fails[["question_id", "language", "intent", "expected", "predicted",
                                                  "facts_ok", "stale_present", "source_ok", "sources"]].to_markdown(index=False), ""]
    out = HERE / "reports" / f"{name}.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print("\n".join(lines[:16]))
    print(f"\nReport: {out.relative_to(HERE)}")


if __name__ == "__main__":
    main()
