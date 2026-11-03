"""Shared helpers for the Lumen SaaS generator (standard library only)."""
from __future__ import annotations

import csv
import random
from datetime import date, datetime, timedelta
from pathlib import Path

SEED = 20261129
ROOM = Path(__file__).resolve().parent          # labs/module-14/data-room

BETA_START = date(2026, 10, 11)                 # Sunday: closed beta opens
BETA_END = date(2026, 11, 26)                   # Thursday: export cut-off
PLAN_TOOL_FROM = date(2026, 11, 1)              # change_plan added for Starter
STALE_FROM = datetime(2026, 11, 9, 16, 40)      # HC-214 replaced by the campaign draft
STALE_TO = datetime(2026, 11, 22, 14, 5)        # HC-214 restored
FLAG_OFF = datetime(2026, 11, 22, 13, 20)       # assist_enabled switched off
FLAG_ON = datetime(2026, 11, 22, 16, 0)
RESCUE_START = date(2026, 8, 2)

# Israeli holidays on working days in the generated periods (Rosh Hashanah, Yom Kippur, Sukkot 2026).
HOLIDAYS = {date(2026, 9, 12), date(2026, 9, 13), date(2026, 9, 21), date(2026, 9, 26), date(2026, 10, 3)}


def rng(name: str) -> random.Random:
    """A separate, reproducible random stream per section, so editing one section never moves another."""
    return random.Random(f"{SEED}-{name}")


def days(start: date, end: date) -> list[date]:
    out, d = [], start
    while d <= end:
        out.append(d)
        d += timedelta(days=1)
    return out


def workday(d: date) -> bool:
    """Sunday-Thursday, not a holiday."""
    return d.weekday() in (6, 0, 1, 2, 3) and d not in HOLIDAYS


def thursday_run(d: datetime) -> datetime:
    """The first weekly invoice run (Thursday 22:00) at or after d."""
    t = datetime(d.year, d.month, d.day, 22, 0)
    while t.weekday() != 3 or t < d:
        t = datetime(t.year, t.month, t.day, 22, 0) + timedelta(days=1)
    return t


def ts(x: datetime) -> str:
    return x.strftime("%Y-%m-%d %H:%M:%S")


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


def pct(a: float, b: float) -> str:
    return f"{100.0 * a / b:.1f}%" if b else "n/a"
