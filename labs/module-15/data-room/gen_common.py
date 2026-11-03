"""Shared helpers for the Crescent Bank data-room generator (standard library only).

Every file is written with LF line endings and UTF-8 (no BOM), so `python generate.py` rebuilds the
data room byte for byte on any machine.
"""
from __future__ import annotations

import csv
import io
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 20270103
ROOT = Path(__file__).resolve().parent


def rng(salt: int) -> random.Random:
    """A separate, reproducible random stream per file."""
    return random.Random(SEED * 1000 + salt)


def write_csv(rel: str, header: list[str], rows: list[list]) -> int:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO(newline="")
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    for r in rows:
        w.writerow(["" if v is None else v for v in r])
    path.write_bytes(buf.getvalue().encode("utf-8"))
    return len(rows)


def write_md(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    body = text.strip("\n") + "\n"
    path.write_bytes(body.encode("utf-8"))


def days(start: date, end: date):
    d = start
    while d <= end:
        yield d
        d += timedelta(days=1)


def is_workday(d: date) -> bool:
    """Israeli banks work Sunday to Thursday (Python: Monday=0 ... Sunday=6)."""
    return d.weekday() in (6, 0, 1, 2, 3)


HE_MONTHS = ["ינואר", "פברואר", "מרץ", "אפריל", "מאי", "יוני", "יולי", "אוגוסט", "ספטמבר",
             "אוקטובר", "נובמבר", "דצמבר"]


def messy_date(d: date, style: int) -> str:
    """Dates as units typed them into the register."""
    if style == 0:
        return d.isoformat()
    if style == 1:
        return d.strftime("%d/%m/%Y")
    if style == 2:
        return f"{HE_MONTHS[d.month - 1]} {d.year}"
    return d.strftime("%d.%m.%y")


def money(v: int, style: int) -> str:
    """Shekel amounts as typed: plain, with a sign and commas, or in thousands."""
    if style == 0:
        return str(v)
    if style == 1:
        return f"₪{v:,}"
    return f"{round(v / 1000)}k"
