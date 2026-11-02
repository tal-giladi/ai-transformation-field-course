"""Meridian Mutual: field-level eval and fairness slices for document extraction (lesson 09.5).

    python score_extraction.py data-room/extraction/smart_intake_output.csv   # the vendor's Smart Intake
    python score_extraction.py runs/rules-baseline.csv                        # the no-AI baseline
    python score_extraction.py runs/llm-<model>.csv                           # your pilot
    python score_extraction.py runs/llm-<model>.csv --split test              # only the test documents
    python score_extraction.py runs/llm-<model>.csv --docs D001,D002          # only some documents

A run file has the columns doc_id, field, value (one row per extracted field); the filled Track A
sheet (pilot/track-a-sheet.csv, column your_value) also works. The script compares
every value with the QA team's verified value (gold_fields.csv), after normalising formats, and
writes reports/<run name>.md. Fields the run returns that the gold does not ask for are listed as
"extra fields": for a medical document that is a data-minimisation finding, not a bonus.
"""
from __future__ import annotations

import argparse
import math
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
sys.stdout.reconfigure(encoding="utf-8")

import pandas as pd  # noqa: E402

from fieldkit.data import data_room  # noqa: E402

ROOM = data_room("module-09") / "extraction"
HERE = Path(__file__).resolve().parent
GROUPS = ["doc_language", "claimant_language", "region", "claimant_age_band", "capture_channel", "form_filled", "doc_type"]
MIN_N = 30          # a group with fewer scored fields than this is reported but not judged


def kind(field: str) -> str:
    if field.endswith("_date"):
        return "date"
    if field.endswith("_amount"):
        return "amount"
    if field == "currency":
        return "currency"
    return "identifier"


def norm(field: str, v) -> str:
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return ""
    s = str(v).strip()
    if s.lower() in ("", "null", "none", "nan", "n/a"):
        return ""
    k = kind(field)
    if k == "date":
        m = re.fullmatch(r"(\d{4})-(\d{1,2})-(\d{1,2})", s)
        if m:
            try:
                return date(int(m.group(1)), int(m.group(2)), int(m.group(3))).isoformat()
            except ValueError:
                return s
        return s
    if k == "amount":
        t = s.replace("₪", "").replace(" ", "").replace(",", "")
        try:
            return f"{float(t):.2f}"
        except ValueError:
            return s
    return re.sub(r"\s+", "", s).upper()


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - m) / d, (c + m) / d)


def score(run_path: Path, docs: list[str] | None = None):
    gold = pd.read_csv(ROOM / "gold_fields.csv", dtype=str, keep_default_na=False)
    idx = pd.read_csv(ROOM / "documents_index.csv", dtype=str, keep_default_na=False)
    run = pd.read_csv(run_path, dtype=str, keep_default_na=False)
    if "your_value" in run.columns:            # the Track A sheet, filled in
        run = run[["doc_id", "field", "your_value"]].rename(columns={"your_value": "value"})
        run = run[run.value != ""]
    if docs:
        gold, idx, run = gold[gold.doc_id.isin(docs)], idx[idx.doc_id.isin(docs)], run[run.doc_id.isin(docs)]
    run = run.drop_duplicates(["doc_id", "field"], keep="last")
    x = gold.merge(run[["doc_id", "field", "value"]], on=["doc_id", "field"], how="left", suffixes=("_gold", "_run"))
    x["gold_n"] = [norm(f, v) for f, v in zip(x.field, x.value_gold)]
    x["run_n"] = [norm(f, v) for f, v in zip(x.field, x.value_run)]
    x["correct"] = x.gold_n == x.run_n
    x["error"] = ["" if c else ("blank" if r == "" else "wrong") for c, r in zip(x.correct, x.run_n)]
    x["kind"] = x.field.map(kind)
    x = x.merge(idx, on="doc_id")
    extra = run.merge(gold[["doc_id", "field"]], on=["doc_id", "field"], how="left", indicator=True)
    extra = extra[extra["_merge"] == "left_only"].drop(columns="_merge")
    return x, extra, idx


def table(x: pd.DataFrame, col: str) -> tuple[list[str], float | None]:
    rows, best = [], None
    g = x.groupby(col).correct.agg(["sum", "size"])
    judged = g[g["size"] >= MIN_N]
    if len(judged):
        best = (judged["sum"] / judged["size"]).max()
    for val, r in g.iterrows():
        k, n = int(r["sum"]), int(r["size"])
        lo, hi = wilson(k, n)
        ratio = f"{(k / n) / best:.2f}" if best and n >= MIN_N else "n<30"
        rows.append(f"| {val} | {n} | {k / n * 100:.1f}% | {lo * 100:.1f}–{hi * 100:.1f}% | {ratio} |")
    return rows, best


def report(run_path: Path, docs: list[str] | None) -> str:
    x, extra, idx = score(run_path, docs)
    name = run_path.stem
    n, k = len(x), int(x.correct.sum())
    lo, hi = wilson(k, n)
    per_doc = x.groupby("doc_id").correct.all()
    crit = x[x.kind.isin(["date", "amount", "currency"])]
    out = [f"# Extraction eval — {name}", "",
           f"Documents: {x.doc_id.nunique()} · fields scored: {n} · run file: `{run_path.as_posix()}`", "",
           "## Headline", "",
           f"- Field accuracy: **{k / n * 100:.1f}%** ({k} of {n}; 95% interval {lo * 100:.1f}–{hi * 100:.1f}%)",
           f"- Critical fields (dates, amounts, currency): **{crit.correct.mean() * 100:.1f}%** of {len(crit)}",
           f"- Documents with every field right (no correction needed): **{per_doc.mean() * 100:.1f}%** of {len(per_doc)}",
           f"- Errors: {int((x.error == 'blank').sum())} blank, {int((x.error == 'wrong').sum())} wrong value "
           "(a wrong value is worse: it looks filled in)",
           f"- Extra fields returned that were not asked for: {len(extra)}"
           + (f" (fields: {', '.join(sorted(extra.field.unique()))})" if len(extra) else ""), "",
           "## By field type", "", "| Type | Fields | Accuracy |", "|---|---|---|"]
    for kd, g in x.groupby("kind"):
        out.append(f"| {kd} | {len(g)} | {g.correct.mean() * 100:.1f}% |")
    out += ["", "## Fairness slices", "",
            f"Accuracy per group with a 95% interval. *Ratio* = the group's accuracy divided by the best group's "
            f"(groups with at least {MIN_N} scored fields). Read a low ratio together with its interval and the "
            "stratified table below before you call it a language effect.", ""]
    for col in GROUPS:
        rows, _ = table(x, col)
        out += [f"### {col}", "", "| Group | Fields | Accuracy | 95% interval | Ratio to best |", "|---|---|---|---|---|"]
        out += rows + [""]
    out += ["## Stratified: document language × capture channel", "",
            "| Language | Capture | Fields | Accuracy |", "|---|---|---|---|"]
    for (lang, cap), g in x.groupby(["doc_language", "capture_channel"]):
        out.append(f"| {lang} | {cap} | {len(g)} | {g.correct.mean() * 100:.1f}% |")
    out += ["", "## Errors (first 40)", "", "| doc | type | lang | capture | field | gold | run |", "|---|---|---|---|---|---|---|"]
    for _, r in x[~x.correct].head(40).iterrows():
        out.append(f"| {r.doc_id} | {r.doc_type} | {r.doc_language} | {r.capture_channel} | {r.field} | {r.gold_n} | {r.run_n or '(blank)'} |")
    if len(extra):
        out += ["", "## Extra fields (data minimisation)", "", "| doc | field | value |", "|---|---|---|"]
        for _, r in extra.head(30).iterrows():
            out.append(f"| {r.doc_id} | {r.field} | {str(r.value)[:60]} |")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("run", type=Path)
    ap.add_argument("--docs", default="", help="comma-separated doc ids to score only those")
    ap.add_argument("--split", choices=["dev", "test", "track-a"], help="score only one split of pilot/splits.csv")
    a = ap.parse_args()
    docs = [d.strip() for d in a.docs.split(",") if d.strip()] or None
    suffix = "-subset" if docs else ""
    if a.split == "track-a":
        docs = sorted(set(pd.read_csv(HERE / "pilot" / "track-a-sheet.csv", dtype=str).doc_id))
        suffix = "-track-a"
    elif a.split:
        sp = pd.read_csv(HERE / "pilot" / "splits.csv", dtype=str)
        docs = list(sp[sp.split == a.split].doc_id)
        suffix = f"-{a.split}"
    text = report(a.run, docs)
    out = HERE / "reports" / f"{a.run.stem}{suffix}.md"
    out.parent.mkdir(exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(text[: text.index("## Fairness slices")])
    print(f"Full report: {out.relative_to(HERE).as_posix()}")
