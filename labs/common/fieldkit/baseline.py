"""Measure a baseline from timestamps: elapsed hours and working hours (Israeli week).

    from fieldkit.baseline import elapsed_hours, working_hours, summarize
    tickets["wait_h"] = elapsed_hours(tickets["created_at"], tickets["first_response_at"])
    tickets["wait_wh"] = working_hours(tickets["created_at"], tickets["first_response_at"])
    print(summarize(tickets["wait_wh"]))

The Israeli working week is Sunday to Thursday; set your own days and hours if the organization
differs (many retailers also work Friday mornings).
"""
from __future__ import annotations

from datetime import time, timedelta

import pandas as pd

ISRAEL_WORKDAYS = (6, 0, 1, 2, 3)  # Python weekday numbers: Sunday=6, Monday=0 ... Thursday=3


def elapsed_hours(start: pd.Series, end: pd.Series) -> pd.Series:
    """Clock hours between two timestamp columns (blank where either is missing)."""
    return (end - start).dt.total_seconds() / 3600


def working_hours(start: pd.Series, end: pd.Series, days=ISRAEL_WORKDAYS,
                  opens: time = time(8, 0), closes: time = time(17, 0)) -> pd.Series:
    """Hours between start and end that fall inside working hours on working days."""
    return pd.Series([_working(s, e, days, opens, closes) for s, e in zip(start, end)], index=start.index)


def _working(s, e, days, opens, closes):
    if pd.isna(s) or pd.isna(e) or e < s:
        return float("nan")
    total = 0.0
    day = s.normalize()
    while day <= e:
        if day.weekday() in days:
            window_start = max(s, day + timedelta(hours=opens.hour, minutes=opens.minute))
            window_end = min(e, day + timedelta(hours=closes.hour, minutes=closes.minute))
            total += max(0.0, (window_end - window_start).total_seconds() / 3600)
        day += timedelta(days=1)
    return total


def summarize(values: pd.Series) -> dict:
    """The numbers a baseline needs: count, median, p75, p90 and mean, rounded."""
    v = values.dropna()
    return {
        "n": int(v.size),
        "median": round(float(v.median()), 2),
        "p75": round(float(v.quantile(0.75)), 2),
        "p90": round(float(v.quantile(0.90)), 2),
        "mean": round(float(v.mean()), 2),
    }


def sample(df: pd.DataFrame, n: int, by: str | None = None, seed: int = 7) -> pd.DataFrame:
    """A reproducible random sample, optionally stratified (same share per value of `by`)."""
    if by is None:
        return df.sample(n=min(n, len(df)), random_state=seed)
    frac = min(1.0, n / len(df))
    return df.groupby(by, group_keys=False).sample(frac=frac, random_state=seed)


