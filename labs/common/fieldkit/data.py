"""Find and load data-room files.

    from fieldkit.data import data_room, load
    room = data_room("harbor-and-pine")            # labs/common/harbor-and-pine
    tickets = load(room / "support/tickets.csv")   # a pandas DataFrame, dates parsed
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

LABS = Path(__file__).resolve().parents[2]  # .../labs


def data_room(name: str) -> Path:
    """Path of a data room: 'harbor-and-pine' (shared) or a module folder like 'module-08'."""
    for candidate in (LABS / "common" / name, LABS / name / "data-room"):
        if candidate.is_dir():
            return candidate
    raise FileNotFoundError(f"No data room called {name!r} under {LABS}")


def load(path: str | Path, **kwargs) -> pd.DataFrame:
    """Read a CSV: parse *_at / *_date columns as Israel time, make all-number columns numeric."""
    path = Path(path)
    df = pd.read_csv(path, dtype=str, keep_default_na=False, na_values=[""], encoding="utf-8", **kwargs)
    for col in df.columns:
        if col.endswith(("_at", "_date")) or col in ("date", "timestamp"):
            df[col] = pd.to_datetime(df[col], errors="coerce", utc=True).dt.tz_convert("Asia/Jerusalem")
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            continue
        converted = pd.to_numeric(df[col], errors="coerce")
        if df[col].notna().any() and converted.notna().sum() == df[col].notna().sum():
            df[col] = converted
    return df
