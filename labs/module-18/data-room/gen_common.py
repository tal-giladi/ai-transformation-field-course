"""Shared helpers for the Tzurim Academic College data room generator (standard library only).

Reading this spoils the capstone: submit your deliverables first.
"""
from __future__ import annotations

import csv
import io
import random
from datetime import date, datetime, timedelta
from pathlib import Path

SEED = 20270207
ROOM = Path(__file__).resolve().parent

# Israel daylight saving time: 2025-10-26 ends, 2026-03-27 to 2026-10-25 summer, 2027-03-26 starts.
DST = [
    (datetime(2025, 3, 28, 2), datetime(2025, 10, 26, 2)),
    (datetime(2026, 3, 27, 2), datetime(2026, 10, 25, 2)),
    (datetime(2027, 3, 26, 2), datetime(2027, 10, 31, 2)),
]

PROGRAMMES = [  # code, name, share, annual tuition 2025-26 (NIS), haredi track offered
    ("BA-BUS", "BA Business Administration", 0.30, 29400, True),
    ("BA-BEH", "BA Behavioural Sciences", 0.18, 29400, True),
    ("BSC-CS", "BSc Computer Science", 0.17, 33600, True),
    ("BSC-IEM", "BSc Industrial Engineering and Management", 0.10, 32400, False),
    ("BA-COM", "BA Communication", 0.10, 28200, False),
    ("LLB", "LLB Law", 0.15, 36800, True),
]
TUITION = {p[0]: p[3] for p in PROGRAMMES}
COHORTS = {2023: 2190, 2024: 2260, 2025: 2310}

# 2025-26 calendar (fictional, college's own)
SEM_A_BLOCK_CHECK = date(2026, 1, 4)
SEM_A_REG_CLOSE = date(2026, 1, 11)
SEM_A_EXAMS = (date(2026, 1, 18), date(2026, 2, 13))
SEM_A_GRADES = date(2026, 3, 1)
SEM_B_BLOCK_CHECK = date(2026, 6, 7)
SEM_B_REG_CLOSE = date(2026, 6, 14)
SEM_B_EXAMS = (date(2026, 6, 21), date(2026, 7, 17))
EI_SCORE_DATE = date(2026, 3, 15)

FIRST_HE = ["נועה", "איתי", "יעל", "עומר", "שירה", "דניאל", "מאיה", "אורי", "תמר", "יונתן", "הילה", "רועי",
            "אביגיל", "נתנאל", "מוריה", "אליה", "שקד", "עידו", "רחל", "יוסף"]
FIRST_AR = ["محمد", "رنا", "أحمد", "لين", "يوسف", "سلمى", "عمر", "نور", "خالد", "ريم", "سامي", "هبة",
            "علي", "مريم", "كريم", "دانا"]
FIRST_RU = ["Анна", "Илья", "Мария", "Дмитрий", "Екатерина", "Максим", "Ольга", "Артём", "Наталья", "Евгений"]
FIRST_AM = ["אבבה", "טיגיסט", "יוסף", "מזל", "דסטה", "אסתר", "ברהנו", "שמחה"]
FIRST_EN = ["Daniel", "Sarah", "Michael", "Rebecca", "Jonathan", "Hannah", "David", "Leah"]
LAST_HE = ["כהן", "לוי", "מזרחי", "פרץ", "ביטון", "אברהם", "פרידמן", "שושן", "אזולאי", "דהן", "גבאי", "רוזן"]
LAST_AR = ["حداد", "خوري", "عثمان", "ناصر", "صالح", "جبارين", "مصاروة", "زعبي", "عيسى", "بشارة"]
LAST_RU = ["Иванова", "Кузнецов", "Смирнова", "Попов", "Лебедева", "Козлов", "Новикова", "Морозов"]
LAST_AM = ["טקלה", "מלקו", "וורקנה", "אדמסו", "בלאי", "גטהון"]
LAST_EN = ["Cohen", "Miller", "Levine", "Klein", "Green", "Stern"]


def rng(stream: int) -> random.Random:
    """An independent random stream per section, so one section never shifts another."""
    return random.Random(SEED * 100 + stream)


def il_offset(local: datetime) -> timedelta:
    for a, b in DST:
        if a <= local < b:
            return timedelta(hours=3)
    return timedelta(hours=2)


def iso_local(local: datetime) -> str:
    """2026-01-07T09:14:00+02:00: how the inquiry portal and the SIS export."""
    hours = int(il_offset(local).total_seconds() // 3600)
    return local.strftime("%Y-%m-%dT%H:%M:%S") + f"+{hours:02d}:00"


def utc_z(local: datetime) -> str:
    """2026-01-07T07:14:00Z: how the LMS vendor exports."""
    return (local - il_offset(local)).strftime("%Y-%m-%dT%H:%M:%SZ")


def ymd(d: date | datetime | None) -> str:
    return d.strftime("%Y-%m-%d") if d else ""


def dmy(d: date | datetime | None) -> str:
    return d.strftime("%d/%m/%Y") if d else ""


def is_workday(d: date) -> bool:
    return d.weekday() not in (4, 5)  # Friday, Saturday


def add_workdays(d: date, n: int) -> date:
    cur = d
    while n > 0:
        cur += timedelta(days=1)
        if is_workday(cur):
            n -= 1
    return cur


def work_hour(r: random.Random, d: date) -> datetime:
    """A time during office hours on day d (moved to the next workday if needed)."""
    while not is_workday(d):
        d += timedelta(days=1)
    return datetime(d.year, d.month, d.day, r.randint(8, 16), r.choice((0, 5, 10, 15, 20, 30, 40, 45, 50)))


def any_hour(r: random.Random, d: date) -> datetime:
    """A time a student might write: any day, mostly evenings."""
    h = r.choice((7, 9, 10, 12, 13, 15, 17, 19, 20, 21, 22, 22, 23, 23, 0, 1))
    return datetime(d.year, d.month, d.day, h, r.randint(0, 59))


def pick_name(r: random.Random, lang: str) -> tuple[str, str]:
    table = {
        "he": (FIRST_HE, LAST_HE), "ar": (FIRST_AR, LAST_AR), "ru": (FIRST_RU, LAST_RU),
        "am": (FIRST_AM, LAST_AM), "en": (FIRST_EN, LAST_EN),
    }.get(lang, (FIRST_HE, LAST_HE))
    return r.choice(table[0]), r.choice(table[1])


def weighted(r: random.Random, pairs) -> str:
    total = sum(w for _, w in pairs)
    x = r.random() * total
    for value, w in pairs:
        x -= w
        if x <= 0:
            return value
    return pairs[-1][0]


def write_csv(rel: str, header: list[str], rows: list[list]) -> int:
    path = ROOM / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    for row in rows:
        w.writerow(["" if v is None else v for v in row])
    path.write_text(buf.getvalue(), encoding="utf-8", newline="\n")
    return len(rows)


def write_md(rel: str, text: str) -> None:
    path = ROOM / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip("\n") + "\n", encoding="utf-8", newline="\n")
