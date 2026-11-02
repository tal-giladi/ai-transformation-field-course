"""Profile a table before you trust it: is it complete, unique, current, labelled?

    from fieldkit.profile import profile, duplicates
    print(profile(tickets))                          # one row per column
    dups = duplicates(tickets, ["customer_id", "subject"], within="1h", time_col="created_at")
"""
from __future__ import annotations

import pandas as pd


def profile(df: pd.DataFrame, top: int = 3) -> pd.DataFrame:
    """One row per column: type, % filled, distinct values, range and the most common values."""
    rows = []
    for col in df.columns:
        s = df[col]
        filled = s.notna() & (s.astype(str).str.strip() != "")
        row = {
            "column": col,
            "type": str(s.dtype),
            "filled_%": round(100 * filled.mean(), 1),
            "distinct": s.nunique(dropna=True),
            "min": s.min() if filled.any() and s.dtype != object else "",
            "max": s.max() if filled.any() and s.dtype != object else "",
            "top_values": "; ".join(f"{v} ({n})" for v, n in s[filled].value_counts().head(top).items()),
        }
        rows.append(row)
    return pd.DataFrame(rows).set_index("column")


def duplicates(df: pd.DataFrame, keys: list[str], within: str | None = None,
               time_col: str | None = None) -> pd.DataFrame:
    """Rows that repeat on `keys`; with `within` (e.g. '1h'), only repeats close in time."""
    if within is None:
        return df[df.duplicated(keys, keep="first")]
    ordered = df.sort_values(time_col)
    gap = ordered.groupby(keys)[time_col].diff()
    return ordered[gap.notna() & (gap <= pd.Timedelta(within))]


def share(series: pd.Series, normalize: bool = True) -> pd.Series:
    """Value shares in % (or counts), largest first, blanks shown as '(blank)'."""
    counts = series.fillna("(blank)").replace("", "(blank)").value_counts()
    return (100 * counts / counts.sum()).round(1) if normalize else counts
