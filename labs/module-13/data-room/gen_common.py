"""Shared helpers for the Kinneret Plastics data room generator (standard library only).

Reading this spoils the engagement: finish module 13 first.
"""
from __future__ import annotations

import csv
import io
import random
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

SEED = 20270110
ROOM = Path(__file__).resolve().parent
PILOT = ROOM.parent / "pilot"

YEAR_START = datetime(2026, 1, 1)
YEAR_END = datetime(2027, 1, 1)
# Israel daylight saving time 2026: from Friday 27 March 02:00 to Sunday 25 October 02:00 (local).
DST_START = datetime(2026, 3, 27, 2, 0)
DST_END = datetime(2026, 10, 25, 2, 0)

SHIFT_STARTS = (6 * 60 + 45, 14 * 60 + 45, 22 * 60 + 45)  # minutes after midnight


def rng(stream: int) -> random.Random:
    """An independent random stream per section, so one section never shifts another."""
    return random.Random(SEED * 100 + stream)


def il_offset(local: datetime) -> timedelta:
    return timedelta(hours=3) if DST_START <= local < DST_END else timedelta(hours=2)


def iso_local(local: datetime) -> str:
    """2026-07-14T03:12:00+03:00 — how MaintPro and ProdTrack export."""
    off = il_offset(local)
    sign = "+" if off >= timedelta(0) else "-"
    hours = int(off.total_seconds() // 3600)
    return local.strftime("%Y-%m-%dT%H:%M:%S") + f"{sign}{hours:02d}:00"


def to_utc(local: datetime) -> datetime:
    return local - il_offset(local)


def us_utc(local: datetime) -> str:
    """Plant G SCADA: MM/DD/YYYY HH:MM:SS in UTC, no marker."""
    return to_utc(local).strftime("%m/%d/%Y %H:%M:%S")


def dmy(d: datetime | date) -> str:
    return d.strftime("%d/%m/%Y")


def hm(d: datetime) -> str:
    return d.strftime("%H:%M")


def shift_of(local: datetime) -> str:
    """Morning (06:45-14:45), evening (14:45-22:45), night (22:45-06:45)."""
    m = local.hour * 60 + local.minute
    if SHIFT_STARTS[0] <= m < SHIFT_STARTS[1]:
        return "morning"
    if SHIFT_STARTS[1] <= m < SHIFT_STARTS[2]:
        return "evening"
    return "night"


def shift_end(local: datetime) -> datetime:
    m = local.hour * 60 + local.minute
    day = datetime(local.year, local.month, local.day)
    if SHIFT_STARTS[0] <= m < SHIFT_STARTS[1]:
        return day + timedelta(minutes=SHIFT_STARTS[1])
    if SHIFT_STARTS[1] <= m < SHIFT_STARTS[2]:
        return day + timedelta(minutes=SHIFT_STARTS[2])
    if m >= SHIFT_STARTS[2]:
        return day + timedelta(days=1, minutes=SHIFT_STARTS[0])
    return day + timedelta(minutes=SHIFT_STARTS[0])


def is_working_time(local: datetime) -> bool:
    """Production runs Sunday 06:45 to Friday 06:45."""
    wd = local.weekday()  # Monday 0 ... Sunday 6
    m = local.hour * 60 + local.minute
    if wd == 4:  # Friday
        return m < SHIFT_STARTS[0]
    if wd == 5:  # Saturday
        return False
    if wd == 6:  # Sunday
        return m >= SHIFT_STARTS[0]
    return True


def random_working_time(r: random.Random, start: datetime, end: datetime) -> datetime:
    span = int((end - start).total_seconds() // 60)
    while True:
        t = start + timedelta(minutes=r.randrange(span))
        if is_working_time(t):
            return t


def write_csv(path: Path, header: list[str], rows: list[list]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    for row in rows:
        w.writerow(["" if v is None else v for v in row])
    path.write_text(buf.getvalue(), encoding="utf-8", newline="")
    return len(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8", newline="")


def lognormal_minutes(r: random.Random, median: float, spread: float = 0.6, lo: int = 5) -> int:
    import math
    return max(lo, int(round(median * math.exp(r.gauss(0, spread)))))


# ---------------------------------------------------------------- machines
# Plant G: the MES numbers machines by purchase order, the hall (Excel log, SCADA) by position.
# Since the 2025 rearrangement four positions differ.
G_HALL_OF_MES = {3: 5, 5: 3, 9: 12, 12: 9}


def machines() -> list[dict]:
    out = []
    for n in range(1, 27):
        if n <= 8:
            maker, model, year, ton = "Haiwei", "HW-%d" % (160 + 40 * (n % 4)), 1999 + n, 160 + 40 * (n % 4)
            age = 3
        elif n <= 20:
            ton = (250, 350, 450, 550, 650)[n % 5]
            maker, model, year, age = "Kessler", f"KX {ton}", 2008 + (n - 8), 2
        elif n <= 23:
            ton = (450, 550, 650)[n - 21]
            maker, model, year, age = "Kessler", f"KX-e {ton}", 2024, 1
        else:
            ton = (220, 280, 320)[n - 24]
            maker, model, year, age = "Haiwei", f"HW-3 {ton}", 2016, 2
        out.append({
            "plant": "K", "mes": f"K{n:02d}", "cmms": f"KN-IM-{n:02d}", "maker": maker, "model": model,
            "year": year, "tonnage": ton, "age": age, "accumulator": maker == "Kessler" and ton >= 450,
            "cm": n in (21, 22, 23), "hall": n,
        })
    for n in range(1, 15):
        if n <= 9:
            ton = (300, 400, 500)[n % 3]
            maker, model, year, age = "Morandi", f"MP {ton}", 2002 + n, 3
        else:
            ton = (220, 280, 320, 380, 220)[n - 10]
            maker, model, year, age = "Haiwei", f"HW-3 {ton}", 2017 + (n - 10) // 2, 2
        out.append({
            "plant": "G", "mes": f"G{n:02d}", "cmms": "", "maker": maker, "model": model, "year": year,
            "tonnage": ton, "age": age, "accumulator": maker == "Morandi", "cm": False,
            "hall": G_HALL_OF_MES.get(n, n),
        })
    for i, m in enumerate(out):
        m["serial"] = f"{m['maker'][:2].upper()}{m['year']}-{(i * 7919 + 4111) % 9000 + 1000}"
    return out


# Six Plant K machines whose Q3 preventive maintenance was deferred and bulk-closed on 30 September.
DEFERRED_PM = ("K03", "K05", "K07", "K11", "K14", "K24")

TECHS_K = [  # id, first language, years
    ("T101", "ru", 31), ("T102", "ru", 27), ("T103", "ru", 22), ("T104", "ru", 19),
    ("T105", "ar", 14), ("T106", "ar", 9), ("T107", "ar", 6), ("T108", "ar", 4), ("T109", "ar", 2),
    ("T110", "he", 11), ("T111", "he", 3),
]
TECHS_G = [("ש.ב", "he"), ("מ.ח", "ar"), ("א.ס", "ar"), ("ד.ל", "ru"), ("ע.ג", "ar"), ("י.מ", "he")]
NIGHT_TECHS_K = ("T105", "T107", "T108", "T109", "T103", "T111")
