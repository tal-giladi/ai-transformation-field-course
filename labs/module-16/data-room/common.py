"""Shared helpers for the Open Hands generator (standard library only)."""
from __future__ import annotations

import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 20261115
ROOM = Path(__file__).resolve().parent          # labs/module-16/data-room
DOMAIN = "openhands-amuta.org.il"               # fictional
EXPORT_DAY = date(2026, 11, 12)                 # case register and Drive audit exported
LINK_SHARED_ON = date(2024, 8, 14)         # Respite folder opened to "anyone with the link"
USD_ILS_OCT = 3.139                             # rate used on the October card statement (synthetic)


def rng(name: str) -> random.Random:
    """A separate, reproducible random stream per section, so editing one section never moves another."""
    return random.Random(f"{SEED}-{name}")


def pick(r: random.Random, weights: dict):
    keys = list(weights)
    return r.choices(keys, weights=[weights[k] for k in keys])[0]


def rand_date(r: random.Random, start: date, end: date) -> date:
    return start + timedelta(days=r.randint(0, (end - start).days))


def workday(d: date) -> bool:
    """Sunday-Thursday."""
    return d.weekday() in (6, 0, 1, 2, 3)


def write_csv(path: Path, header: list[str], rows: list[list]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        for row in rows:
            w.writerow(["" if v is None else v for v in row])


def write_md(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = text.strip("\n") + "\n"
    path.write_bytes(text.encode("utf-8"))


def fill(template: str, values: dict) -> str:
    """Replace {{name}} placeholders; other braces stay untouched."""
    for k, v in values.items():
        template = template.replace("{{" + k + "}}", str(v))
    if "{{" in template:
        raise ValueError("unfilled placeholder: " + template[template.index("{{"):][:40])
    return template


def ils(x: float) -> str:
    return f"₪{x:,.0f}"


def pct(a: float, b: float) -> str:
    return f"{100.0 * a / b:.1f}%" if b else "n/a"
