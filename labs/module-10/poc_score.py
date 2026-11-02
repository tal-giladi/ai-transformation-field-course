"""Lessons 10.4 and 10.5 (Track B): score the proof of concept and the vendors, the same way every time.

    python poc_score.py                      # PoC results per vendor and language, with 95% intervals
    python poc_score.py --scores my.csv      # also weight your own 1-5 scores (columns: vendor,criterion,score)

Reads ../module-10/poc/review-sheet.csv and rfp-responses.csv. Prints:
  - word error rate per language, omissions and invented findings per 100 notes with Wilson 95% intervals,
    minutes to correct, omissions inside passages marked unsure;
  - must-have contract terms each vendor accepts or refuses;
  - weighted scores (weights 2/3/3/2/1/2) from a scores file, if you give one.
No network, no API key. Standard library plus pandas.
"""
import argparse
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))

import pandas as pd

from fieldkit.data import load

POC = HERE / "poc"
WEIGHTS = {"evidence": 2, "safety": 3, "privacy": 3, "languages": 2, "integration": 1, "contract": 2}


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """95% interval for a proportion k/n (Wilson score); returned per 100."""
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (100 * max(0, centre - half), 100 * min(1, centre + half))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scores", help="CSV with columns vendor,criterion,score (1-5)")
    args = ap.parse_args()

    s = load(POC / "review-sheet.csv")
    scored = s[s["status"] == "scored"]

    print("== Word error rate, % (mean of notes)")
    print(scored.pivot_table(index="vendor", columns="language", values="wer_pct", aggfunc="mean").round(1).to_string())
    print("\n== Minutes to correct a note (mean)")
    print(scored.pivot_table(index="vendor", columns="language", values="minutes_to_correct", aggfunc="mean").round(1).to_string())

    print("\n== Notes with no output")
    print(s[s["status"] == "no_output"].groupby(["vendor", "language"]).size().to_string())

    print("\n== Per 100 notes, with Wilson 95% intervals (counts are events / notes produced)")
    rows = []
    for vendor, g in scored.groupby("vendor"):
        n = len(g)
        om, inv = int(g["omitted_relevant"].sum()), int(g["invented"].sum())
        lo, hi = wilson(om, n)
        ilo, ihi = wilson(inv, n)
        rows.append([vendor, n, om, round(100 * om / n, 1), f"{lo:.1f}-{hi:.1f}", inv, round(100 * inv / n, 1),
                     f"{ilo:.1f}-{ihi:.1f}", int(g["omissions_flagged"].sum()), round(g["minutes_to_correct"].mean(), 2)])
    print(pd.DataFrame(rows, columns=["vendor", "notes", "omitted", "per100", "95% CI", "invented", "per100 ",
                                      "95% CI ", "omissions flagged unsure", "min to correct"]).to_string(index=False))
    print("(Each event is counted per note; a note with two omissions counts twice, so the interval is approximate.)")

    print("\n== Omissions by language (count / notes)")
    t = scored.groupby(["vendor", "language"]).agg(omitted=("omitted_relevant", "sum"), notes=("run", "size"))
    print(t.to_string())

    print("\n== Visits with a relative present vs alone: omissions per 100 notes")
    vis = load(POC / "visits-90.csv")[["poc_visit_id", "relative_present"]]
    j = scored.merge(vis, on="poc_visit_id")
    print((j.groupby(["vendor", "relative_present"])["omitted_relevant"].mean() * 100).round(1).unstack().to_string())

    r = load(POC / "rfp-responses.csv")
    must = r[r["must_have"] == "must"]
    print("\n== Must-have contract terms refused")
    for vendor, g in must.groupby("vendor"):
        refused = g[g["reply"] == "refuses"]["term_id"].tolist()
        print(f"{vendor}: {'none, accepts all ' + str(len(g)) if not refused else ', '.join(refused)}")

    if args.scores:
        sc = pd.read_csv(args.scores)
        sc["w"] = sc["criterion"].map(WEIGHTS)
        tot = sc.assign(x=sc["score"] * sc["w"]).groupby("vendor")["x"].sum() / sum(WEIGHTS.values())
        print("\n== Weighted scores from", args.scores)
        print(tot.round(2).sort_values(ascending=False).to_string())


if __name__ == "__main__":
    main()
