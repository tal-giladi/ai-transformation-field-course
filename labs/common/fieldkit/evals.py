"""Run a pilot over a fixed test set and score it, the same way every time.

    from fieldkit.evals import run_eval, report
    results = run_eval(test_set, predict=my_triage, id_col="email_id",
                       expected_col="expected_category", group_cols=["language"])
    print(report(results, title="Triage v1"))       # markdown you can paste into the eval report

`predict(row)` takes one test-set row (a dict) and returns the predicted label (a string) or a
dict with at least "label" (and anything else you want kept, e.g. "draft", "tokens_in").
"""
from __future__ import annotations

from collections.abc import Callable

import pandas as pd


def run_eval(test_set: pd.DataFrame, predict: Callable[[dict], str | dict], *, id_col: str,
             expected_col: str, group_cols: list[str] | None = None) -> pd.DataFrame:
    """Call `predict` on every row; return one row per item with expected, predicted and correct."""
    rows = []
    for record in test_set.to_dict("records"):
        try:
            out = predict(record)
        except Exception as exc:  # a crash is a result too: count it, don't stop the run
            out = {"label": "ERROR", "error": f"{type(exc).__name__}: {exc}"}
        out = out if isinstance(out, dict) else {"label": out}
        label = str(out.get("label", "")).strip().lower()
        expected = str(record[expected_col]).strip().lower()
        row = {id_col: record[id_col], "expected": expected, "predicted": label, "correct": label == expected}
        for col in group_cols or []:
            row[col] = record[col]
        row.update({k: v for k, v in out.items() if k != "label"})
        rows.append(row)
    return pd.DataFrame(rows)


def confusion(results: pd.DataFrame) -> pd.DataFrame:
    """Rows = expected label, columns = predicted label."""
    return pd.crosstab(results["expected"], results["predicted"], margins=True, margins_name="total")


def by_group(results: pd.DataFrame, col: str) -> pd.DataFrame:
    """Accuracy per value of `col` (e.g. language): the place averages hide failures."""
    g = results.groupby(col)["correct"].agg(["size", "mean"]).rename(columns={"size": "n", "mean": "accuracy"})
    g["accuracy"] = (100 * g["accuracy"]).round(1)
    return g.sort_values("accuracy")


def per_label(results: pd.DataFrame) -> pd.DataFrame:
    """Precision and recall per label."""
    out = []
    for label in sorted(set(results["expected"]) | set(results["predicted"])):
        tp = ((results["expected"] == label) & (results["predicted"] == label)).sum()
        predicted = (results["predicted"] == label).sum()
        actual = (results["expected"] == label).sum()
        out.append({"label": label, "n": int(actual),
                    "precision_%": round(100 * tp / predicted, 1) if predicted else None,
                    "recall_%": round(100 * tp / actual, 1) if actual else None})
    return pd.DataFrame(out).set_index("label")


def report(results: pd.DataFrame, title: str = "Eval", group_cols: list[str] | None = None,
           max_failures: int = 15) -> str:
    """A markdown summary: overall accuracy, per label, per group, and the first failures."""
    lines = [f"## {title}", "", f"Items: {len(results)}  ",
             f"Accuracy: {100 * results['correct'].mean():.1f}%", "",
             "### Per label", "", per_label(results).to_markdown(), ""]
    for col in group_cols or []:
        lines += [f"### By {col}", "", by_group(results, col).to_markdown(), ""]
    failures = results[~results["correct"]].head(max_failures)
    if len(failures):
        lines += ["### First failures", "", failures.to_markdown(index=False), ""]
    return "\n".join(lines)
