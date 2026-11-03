"""Shared helpers for the Atlas & Rowe generator (standard library only)."""
from __future__ import annotations

import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 20261115
ROOM = Path(__file__).resolve().parent          # labs/module-12/data-room
PILOT = ROOM.parent / "pilot"                   # labs/module-12/pilot

# Israeli holidays that fall on working days in the periods we generate (2026).
HOLIDAYS = {date(2026, 9, 13), date(2026, 9, 21)}   # Rosh Hashanah day 2, Yom Kippur
HALF_DAYS = {date(2026, 9, 20)} | {date(2026, 9, 27) + timedelta(d) for d in range(5)}  # eve of YK, Sukkot week


def rng(name: str) -> random.Random:
    """A separate, reproducible random stream per section, so editing one section never moves another."""
    return random.Random(f"{SEED}-{name}")


def workdays(start: date, end: date) -> list[date]:
    """Sunday-Thursday working days between start and end inclusive, without holidays."""
    out, d = [], start
    while d <= end:
        if d.weekday() in (6, 0, 1, 2, 3) and d not in HOLIDAYS:   # Sun=6, Mon=0 ... Thu=3
            out.append(d)
        d += timedelta(days=1)
    return out


def write_csv(path: Path, header: list[str], rows: list[list]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        for r in rows:
            w.writerow(["" if v is None else v for v in r])


def write_md(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = text.strip("\n") + "\n"
    path.write_bytes(text.encode("utf-8"))


def fill(template: str, values: dict) -> str:
    """Replace {{name}} placeholders; markdown braces elsewhere stay untouched."""
    for k, v in values.items():
        template = template.replace("{{" + k + "}}", str(v))
    if "{{" in template:
        raise ValueError("unfilled placeholder: " + template[template.index("{{"):][:40])
    return template


def ils(x: float) -> str:
    return f"₪{x:,.0f}"


def r10(x: float) -> int:
    return int(round(x / 10.0)) * 10
