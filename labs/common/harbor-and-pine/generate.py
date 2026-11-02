"""Harbor & Pine data room generator.

Rebuilds every generated file in this folder, byte for byte, from a fixed seed:

    python generate.py                      # rewrite the data files
    python generate.py --answer-key DIR     # also write the ground truth (for course writers) to DIR

Python 3.12+, standard library only. Files are UTF-8 (no BOM) with LF line endings; timestamps are
Israel local time with their UTC offset (+03:00 in summer, +02:00 after 25 October 2026), except the
phone system, which exports UTC like many cloud phone systems do.

How the simulation works, in one paragraph: we build the staff, the product catalogue and the
containers each supplier ships (with real-world style delays). Customer orders are allocated to
containers; the web store promises a delivery date from a fixed lead time per supplier country.
Customers then write to support when they need something: when a promised date passes, when an
item arrives damaged, when they want an invoice, and so on. Support agents reply during business
hours, mark the ticket "resolved" when they reply, and some customers write again. Everything else
(phone calls, claims, time sheets, IT logs, the pilot's usage export) is built around that story.

Hand-written documents (policies, vendor papers, persona files) are not touched by this script;
the few documents that quote numbers from the data (org chart, KPI report, the AI-drafted memo,
the logistics sheet) are generated so their numbers always match.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import math
import random
import statistics
from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from pathlib import Path

import sys

sys.dont_write_bytecode = True   # keep the data room folder clean (no __pycache__)
import textbank as tb  # noqa: E402  (multilingual text fragments, in this folder)

SEED = 20261102
ROOT = Path(__file__).resolve().parent

DATA_START = datetime(2026, 5, 1)             # tickets, emails, calls start here
EXPORT_AT = datetime(2026, 10, 31, 23, 59, 59)  # the exports were pulled at the end of October
ORDERS_FROM = date(2026, 3, 15)               # orders placed from mid-March deliver from May
CATEGORY_CHANGE = datetime(2026, 7, 1)        # helpdesk categories were redefined on this day

COUNTRIES = {"VN": "Vietnam", "CN": "China", "TR": "Turkey", "IT": "Italy"}
# The web store's lead-time table (days from order to promised delivery). Set in 2023, never changed.
LEAD_DAYS = {"VN": 42, "CN": 38, "TR": 21, "IT": 28}


def rng_for(name: str) -> random.Random:
    """One independent random stream per part, so changing one part never shifts another."""
    return random.Random(f"{SEED}:{name}")


# =============================================================================================
# Time helpers: Israel time, business hours
# =============================================================================================
# Israel daylight saving time: from the Friday before the last Sunday of March, 02:00, to the last
# Sunday of October, 02:00 (UTC+3 in summer, UTC+2 in winter).
DST = {
    2025: (datetime(2025, 3, 28, 2), datetime(2025, 10, 26, 2)),
    2026: (datetime(2026, 3, 27, 2), datetime(2026, 10, 25, 2)),
    2027: (datetime(2027, 3, 26, 2), datetime(2027, 10, 31, 2)),
}


def utc_offset(local: datetime) -> int:
    start, end = DST[local.year]
    return 3 if start <= local < end else 2


def iso(local: datetime | None) -> str:
    """'2026-07-14 09:12:44+03:00' (blank for None)."""
    if local is None:
        return ""
    return local.strftime("%Y-%m-%d %H:%M:%S") + f"+0{utc_offset(local)}:00"


def iso_utc(local: datetime) -> str:
    return (local - timedelta(hours=utc_offset(local))).strftime("%Y-%m-%dT%H:%M:%SZ")


def to_utc(local: datetime) -> datetime:
    return local - timedelta(hours=utc_offset(local))


def hours_between(a: datetime, b: datetime) -> float:
    return (to_utc(b) - to_utc(a)).total_seconds() / 3600


ISRAELI_WORKDAYS = (6, 0, 1, 2, 3)  # Python weekday(): Sunday=6, Monday=0 ... Thursday=3
# The support team works in shifts: Sunday-Thursday 08:00-18:00 and a skeleton crew on Friday
# 08:30-12:30. (The KPI report counts only Sunday-Thursday 08:00-17:00: see kpi_numbers.)
SUPPORT_OPEN, SUPPORT_CLOSE = time(8, 0), time(18, 0)
FRIDAY_OPEN, FRIDAY_CLOSE = time(8, 30), time(12, 30)
# Days the support team did not work (Rosh Hashana, Yom Kippur 2026) and a half day (eve of YK).
SUPPORT_CLOSED = (date(2026, 9, 13), date(2026, 9, 21))
SUPPORT_HALF_DAYS = {date(2026, 9, 20): time(13, 0)}


def support_window(d: date) -> tuple[datetime, datetime] | None:
    if d in SUPPORT_CLOSED or d.weekday() == 5:
        return None
    if d.weekday() == 4:
        return datetime.combine(d, FRIDAY_OPEN), datetime.combine(d, FRIDAY_CLOSE)
    close = SUPPORT_HALF_DAYS.get(d, SUPPORT_CLOSE)
    return datetime.combine(d, SUPPORT_OPEN), datetime.combine(d, close)


def add_support_hours(start: datetime, hours: float) -> datetime:
    """The moment `hours` of support opening time have passed after `start`."""
    remaining = hours * 3600
    t = start
    while True:
        window = support_window(t.date())
        if window and t < window[1]:
            s = max(t, window[0])
            available = (window[1] - s).total_seconds()
            if remaining <= available:
                return s + timedelta(seconds=round(remaining))
            remaining -= available
        t = datetime.combine(t.date() + timedelta(days=1), time(0))


def working_hours(a: datetime, b: datetime) -> float:
    """Sunday-Thursday 08:00-17:00 hours between a and b (the KPI report's definition; no holidays)."""
    total, day = 0.0, a.date()
    while day <= b.date():
        if day.weekday() in ISRAELI_WORKDAYS:
            s = max(a, datetime.combine(day, time(8)))
            e = min(b, datetime.combine(day, time(17)))
            total += max(0.0, (e - s).total_seconds() / 3600)
        day += timedelta(days=1)
    return total


def next_workday(d: date) -> date:
    while d.weekday() not in ISRAELI_WORKDAYS:
        d += timedelta(days=1)
    return d


def days(start: date, end: date):
    d = start
    while d <= end:
        yield d
        d += timedelta(days=1)


def poisson(r: random.Random, lam: float) -> int:
    limit, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= r.random()
        if p < limit:
            return k
        k += 1


# Customers write at all hours, more in the late morning and the evening.
CUSTOMER_HOUR_WEIGHTS = [.8, .4, .2, .1, .1, .3, .8, 2.5, 5, 7, 7.5, 7.5, 7, 7, 7, 6.5, 6, 5, 4,
                         3.8, 4, 3.6, 2.8, 1.6]


def random_moment(r: random.Random, d: date, weights=CUSTOMER_HOUR_WEIGHTS) -> datetime:
    hour = r.choices(range(24), weights)[0]
    return datetime.combine(d, time(hour, r.randrange(60), r.randrange(60)))


def contact_moment(r: random.Random, d: date) -> datetime:
    """When a customer gets round to writing: fewer messages on Friday and Shabbat, more on Sunday."""
    if d.weekday() == 5 and r.random() < 0.55:
        d += timedelta(days=1)
    elif d.weekday() == 4 and r.random() < 0.3:
        d += timedelta(days=2)
    return random_moment(r, d)


# =============================================================================================
# Output helpers
# =============================================================================================
def write_csv(rel: str, header: list[str], rows: list[list], root: Path = ROOT) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def write_text(rel: str, text: str, root: Path = ROOT) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def money(x: float) -> str:
    return f"{x:,.0f}"


# =============================================================================================
# 1. Staff (about 120 people)
# =============================================================================================
@dataclass
class Person:
    emp_id: str
    first: str
    last: str
    role: str
    team: str
    site: str
    manager_id: str
    start: date
    band: str
    fte: float = 1.0
    langs: str = "Hebrew"
    has_pc: bool = True

    @property
    def name(self) -> str:
        return f"{self.first} {self.last}"

    @property
    def email(self) -> str:
        last = self.last.lower().replace("-", "").replace(" ", "")
        return f"{self.first.lower()}.{last}@harborpine.co.il"


HQ = "Rishon LeZion (HQ & warehouse)"
TLV, HFA = "Tel Aviv showroom", "Haifa showroom"

# The people the story needs, by name. (first, last, role, team, site, band, start, languages, manager)
NAMED_STAFF = [
    ("Yoav", "Ben-Ami", "Chief Executive Officer", "Management", HQ, "₪60k+", "2014-01-01", "Hebrew, English", None),
    ("Michal", "Peretz", "Chief Operating Officer", "Management", HQ, "₪45–60k", "2019-04-01", "Hebrew, English", "Yoav Ben-Ami"),
    ("Ronit", "Avraham", "Chief Financial Officer", "Finance", HQ, "₪45–60k", "2017-09-01", "Hebrew, English", "Yoav Ben-Ami"),
    ("Samir", "Haddad", "Customer Service Manager", "Customer Service", HQ, "₪28–35k", "2015-03-01", "Arabic, Hebrew, English", "Michal Peretz"),
    ("Olga", "Petrenko", "Senior Support Agent (team lead)", "Customer Service", HQ, "₪23–28k", "2016-09-01", "Russian, Hebrew, Ukrainian, English", "Samir Haddad"),
    ("Rina", "Azoulay", "Claims & Returns Coordinator", "Customer Service", HQ, "₪16–19k", "2012-05-01", "Hebrew, French", "Samir Haddad"),
    ("Yana", "Kogan", "Support Agent", "Customer Service", HQ, "₪16–19k", "2019-02-01", "Russian, Hebrew", "Samir Haddad"),
    ("Sergei", "Novikov", "Support Agent", "Customer Service", HQ, "₪16–19k", "2023-06-01", "Russian, Hebrew", "Samir Haddad"),
    ("Lina", "Khoury", "Support Agent", "Customer Service", HQ, "₪16–19k", "2020-01-01", "Arabic, Hebrew, English", "Samir Haddad"),
    ("Rami", "Nasser", "Support Agent", "Customer Service", HQ, "₪16–19k", "2022-03-01", "Arabic, Hebrew", "Samir Haddad"),
    ("Ahmad", "Jabareen", "Support Agent", "Customer Service", HQ, "₪16–19k", "2024-05-01", "Arabic, Hebrew", "Samir Haddad"),
    ("Hila", "Dahan", "Support Agent", "Customer Service", HQ, "₪16–19k", "2018-07-01", "Hebrew, English", "Samir Haddad"),
    ("Moran", "Biton", "Support Agent", "Customer Service", HQ, "₪16–19k", "2021-10-01", "Hebrew", "Samir Haddad"),
    ("Adi", "Golan", "Support Agent", "Customer Service", HQ, "₪16–19k", "2025-01-01", "Hebrew, English", "Samir Haddad"),
    ("Shani", "Ohayon", "Support Agent", "Customer Service", HQ, "₪16–19k", "2022-08-01", "Hebrew, English", "Samir Haddad"),
    ("Tigist", "Mekonen", "Support Agent", "Customer Service", HQ, "₪16–19k", "2023-02-01", "Hebrew, Amharic", "Samir Haddad"),
    ("Daniel", "Shaw", "Support Agent", "Customer Service", HQ, "₪16–19k", "2021-04-01", "English, Hebrew", "Samir Haddad"),
    ("Tamar", "Shalev", "Logistics Manager", "Logistics & Warehouse", HQ, "₪28–35k", "2013-11-01", "Hebrew, English", "Michal Peretz"),
    ("Avi", "Mizrahi", "IT Manager", "IT", HQ, "₪28–35k", "2018-01-01", "Hebrew, English", "Ronit Avraham"),
    ("Noa", "Levi", "Marketing Director", "Marketing & E-commerce", HQ, "₪35–45k", "2020-06-01", "Hebrew, English", "Yoav Ben-Ami"),
    ("Shir", "Barak", "Content Manager", "Marketing & E-commerce", HQ, "₪19–23k", "2022-01-01", "Hebrew, English", "Noa Levi"),
    ("Dana", "Katz", "HR Manager", "HR", HQ, "₪28–35k", "2016-02-01", "Hebrew, English", "Michal Peretz"),
    ("Eyal", "Navon", "Head of Purchasing", "Purchasing", HQ, "₪35–45k", "2014-06-01", "Hebrew, English", "Michal Peretz"),
    ("Igor", "Volkov", "Buyer (Asia)", "Purchasing", HQ, "₪23–28k", "2020-09-01", "Russian, Hebrew, English", "Eyal Navon"),
    ("Yaniv", "Carmi", "Head of B2B Sales", "B2B Sales", HQ, "₪35–45k", "2018-03-01", "Hebrew, English", "Yoav Ben-Ami"),
    ("Natalia", "Gurevich", "Financial Controller", "Finance", HQ, "₪28–35k", "2019-11-01", "Russian, Hebrew, English", "Ronit Avraham"),
]

# Everyone else, generated: (team, site, role, count, band, manager, has_pc)
FILLER_STAFF = [
    ("Management", HQ, "Executive Assistant", 1, "₪16–19k", "Yoav Ben-Ami", True),
    ("Logistics & Warehouse", HQ, "Import Coordinator", 3, "₪16–19k", "Tamar Shalev", True),
    ("Logistics & Warehouse", HQ, "Delivery Coordinator", 3, "₪14–16k", "Tamar Shalev", True),
    ("Logistics & Warehouse", HQ, "Warehouse Supervisor", 1, "₪19–23k", "Tamar Shalev", True),
    ("Logistics & Warehouse", HQ, "Warehouse Worker", 30, "₪11–14k", "Tamar Shalev", False),
    ("Logistics & Warehouse", HQ, "Assembly Technician", 6, "₪14–16k", "Tamar Shalev", False),
    ("Purchasing", HQ, "Buyer", 2, "₪19–23k", "Eyal Navon", True),
    ("Purchasing", HQ, "Purchasing Assistant", 1, "₪14–16k", "Eyal Navon", True),
    ("Sales – Showroom Tel Aviv", TLV, "Showroom Manager", 1, "₪23–28k", "Yoav Ben-Ami", True),
    ("Sales – Showroom Tel Aviv", TLV, "Sales Consultant", 13, "₪14–16k", "@Sales – Showroom Tel Aviv", True),
    ("Sales – Showroom Haifa", HFA, "Showroom Manager", 1, "₪23–28k", "Yoav Ben-Ami", True),
    ("Sales – Showroom Haifa", HFA, "Sales Consultant", 8, "₪14–16k", "@Sales – Showroom Haifa", True),
    ("B2B Sales", HQ, "Account Manager", 6, "₪23–28k", "Yaniv Carmi", True),
    ("Marketing & E-commerce", HQ, "E-commerce Manager", 1, "₪23–28k", "Noa Levi", True),
    ("Marketing & E-commerce", HQ, "Performance Marketing Specialist", 1, "₪19–23k", "Noa Levi", True),
    ("Marketing & E-commerce", HQ, "Graphic Designer", 1, "₪16–19k", "Noa Levi", True),
    ("Marketing & E-commerce", HQ, "Social Media Coordinator", 1, "₪14–16k", "Noa Levi", True),
    ("Marketing & E-commerce", HQ, "Web Content Editor", 1, "₪14–16k", "Noa Levi", True),
    ("Finance", HQ, "Accountant", 2, "₪19–23k", "Natalia Gurevich", True),
    ("Finance", HQ, "Accounts Payable Clerk", 1, "₪14–16k", "Natalia Gurevich", True),
    ("Finance", HQ, "Accounts Receivable Clerk", 1, "₪14–16k", "Natalia Gurevich", True),
    ("Finance", HQ, "Payroll Specialist", 1, "₪16–19k", "Natalia Gurevich", True),
    ("HR", HQ, "HR Generalist", 1, "₪16–19k", "Dana Katz", True),
    ("HR", HQ, "Recruiter", 1, "₪16–19k", "Dana Katz", True),
    ("Merchandising", HQ, "Head of Merchandising", 1, "₪28–35k", "Michal Peretz", True),
    ("Merchandising", HQ, "Merchandiser", 3, "₪16–19k", "@Merchandising", True),
    ("Facilities", HQ, "Office & Facilities Coordinator", 1, "₪14–16k", "Michal Peretz", True),
    ("Facilities", HQ, "Maintenance Technician", 1, "₪14–16k", "Michal Peretz", False),
]


def build_staff() -> list[Person]:
    r = rng_for("staff")
    staff: list[Person] = []
    taken: set[str] = set()
    by_name: dict[str, Person] = {}
    for i, (first, last, role, team, site, band, start, langs, mgr) in enumerate(NAMED_STAFF):
        p = Person(f"HP-{1001 + i}", first, last, role, team, site, "", date.fromisoformat(start), band,
                   langs=langs)
        p.manager_id = mgr or ""   # resolved below
        staff.append(p)
        by_name[p.name] = p
        taken.add(p.name)

    origin_weights = [("he", 55), ("ar", 17), ("ru", 18), ("am", 5), ("en", 5)]
    am_first = [("Abebe", "m"), ("Tigist", "f"), ("Worku", "m"), ("Almaz", "f"), ("Desta", "m"),
                ("Malkam", "f"), ("Yitayish", "f"), ("Getachew", "m")]
    am_last = ["Tesfaye", "Wondimu", "Belay", "Alemu", "Negash", "Mengistu"]

    def new_name() -> tuple[str, str, str]:
        while True:
            origin = r.choices([o for o, _ in origin_weights], [w for _, w in origin_weights])[0]
            if origin == "he":
                f, _, _ = r.choice(tb.HE_FIRST)
                l = r.choice(tb.HE_LAST)[0]
                langs = "Hebrew"
            elif origin == "ar":
                f, _, _ = r.choice(tb.AR_FIRST)
                l = r.choice(tb.AR_LAST)[0]
                langs = "Arabic, Hebrew"
            elif origin == "ru":
                f, _, g = r.choice(tb.RU_FIRST)
                l, _, fem = r.choice(tb.RU_LAST)
                if g == "f" and fem:
                    l += "a"
                langs = "Russian, Hebrew"
            elif origin == "am":
                f, _ = r.choice(am_first)
                l = r.choice(am_last)
                langs = "Hebrew, Amharic"
            else:
                f, _ = r.choice(tb.EN_FIRST)
                l = r.choice(tb.EN_LAST)
                langs = "English, Hebrew"
            if f"{f} {l}" not in taken:
                taken.add(f"{f} {l}")
                return f, l, langs

    n = len(staff)
    team_heads: dict[str, Person] = {}
    for team, site, role, count, band, mgr, has_pc in FILLER_STAFF:
        for _ in range(count):
            f, l, langs = new_name()
            start = date(r.randint(2010, 2025), r.randint(1, 12), 1)
            fte = 1.0 if r.random() > 0.08 else 0.5
            p = Person(f"HP-{1001 + n}", f, l, role, team, site, mgr, start, band, fte, langs, has_pc)
            n += 1
            staff.append(p)
            by_name[p.name] = p
            if role in ("Showroom Manager", "Head of Merchandising"):
                team_heads[team] = p
    for p in staff:
        if p.manager_id.startswith("@"):
            p.manager_id = team_heads[p.manager_id[1:]].emp_id
        elif p.manager_id:
            p.manager_id = by_name[p.manager_id].emp_id
    return staff


def person(staff: list[Person], name: str) -> Person:
    return next(p for p in staff if p.name == name)


CS_AGENTS_BY_LANG = {
    # Who picks up tickets in each language (weights). Rina handles damage claims herself.
    "ru": [("Olga Petrenko", 45), ("Yana Kogan", 35), ("Sergei Novikov", 20)],
    "ar": [("Lina Khoury", 40), ("Rami Nasser", 30), ("Ahmad Jabareen", 25), ("Samir Haddad", 5)],
    "en": [("Daniel Shaw", 60), ("Olga Petrenko", 12), ("Adi Golan", 13), ("Shani Ohayon", 15)],
    "he": [("Hila Dahan", 16), ("Moran Biton", 16), ("Adi Golan", 15), ("Shani Ohayon", 15),
           ("Tigist Mekonen", 14), ("Daniel Shaw", 6), ("Ahmad Jabareen", 7), ("Yana Kogan", 4),
           ("Olga Petrenko", 4), ("Sergei Novikov", 3)],
}
# Agents who use the helpdesk's time-tracking timer (the others leave it blank).
TIMER_USERS = ("Olga Petrenko", "Yana Kogan", "Lina Khoury", "Rami Nasser", "Hila Dahan", "Adi Golan",
               "Daniel Shaw", "Rina Azoulay", "Samir Haddad")


# =============================================================================================
# 2. Product catalogue (current) and the stale 2023 copy
# =============================================================================================
PRODUCT_TYPES = [
    # code, English, Hebrew, Russian, Arabic, countries, price range (ILS)
    ("SOF", "3-seat sofa", "ספה תלת מושבית", "диван", "كنبة", ("TR", "CN", "IT"), (3200, 9800)),
    ("SEC", "corner sofa", "פינת ישיבה", "угловой диван", "كنبة زاوية", ("TR", "CN", "IT"), (5900, 14900)),
    ("ARM", "armchair", "כורסה", "кресло", "كرسي استرخاء", ("TR", "CN", "IT"), (1400, 4900)),
    ("DTB", "dining table", "שולחן אוכל", "обеденный стол", "طاولة سفرة", ("VN", "IT", "CN"), (2400, 8900)),
    ("DCH", "dining chair", "כיסא אוכל", "стул", "كرسي سفرة", ("VN", "CN", "IT"), (390, 1490)),
    ("BED", "double bed", "מיטה זוגית", "кровать", "تخت", ("VN", "CN", "TR"), (2900, 8900)),
    ("WRD", "wardrobe", "ארון בגדים", "шкаф", "خزانة", ("CN", "VN", "TR"), (2600, 9900)),
    ("DRS", "dresser", "שידה", "комод", "شوفونيرة", ("VN", "CN"), (1200, 3900)),
    ("CTB", "coffee table", "שולחן סלון", "журнальный столик", "طاولة صالون", ("VN", "IT", "CN"), (690, 3200)),
    ("OUT", "outdoor lounge set", "פינת ישיבה לגינה", "садовый комплект", "طقم حديقة", ("VN",), (3900, 12900)),
    ("LMP", "pendant lamp", "מנורה תלויה", "светильник", "ثريا", ("CN", "IT"), (290, 2400)),
    ("RUG", "rug 200x290", "שטיח 200x290", "ковёр", "سجادة", ("TR",), (890, 4900)),
    ("OCH", "office chair", "כיסא משרדי", "офисное кресло", "كرسي مكتب", ("CN",), (590, 2900)),
    ("DSK", "desk", "שולחן עבודה", "письменный стол", "مكتب", ("VN", "CN"), (990, 3900)),
    ("SHL", "bookcase", "כוננית", "стеллаж", "مكتبة", ("VN", "CN"), (690, 2900)),
]
COLLECTIONS = {  # collection -> supplier country
    "Oslo": "TR", "Bergen": "VN", "Lisbon": "CN", "Kyoto": "VN", "Carmel": "VN", "Arbel": "CN",
    "Tavor": "CN", "Negev": "VN", "Milano": "IT", "Verona": "IT", "Ankara": "TR", "Izmir": "TR",
    "Hoi An": "VN", "Da Nang": "VN", "Palermo": "IT", "Como": "IT", "Bodrum": "TR", "Galil": "CN",
    "Yarden": "VN", "Malmo": "CN", "Aarhus": "CN", "Porto": "TR", "Sevilla": "CN", "Ningbo": "CN",
}
COLORS = [("grey", "אפור"), ("oak", "אלון"), ("walnut", "אגוז"), ("black", "שחור"), ("white", "לבן"),
          ("beige", "בז'"), ("navy", "כחול נייבי"), ("olive", "ירוק זית"), ("natural teak", "טיק טבעי"),
          ("terracotta", "טרקוטה")]
SUPPLIERS = {
    "VN": ["Saigon Woodcraft Co.", "Binh Duong Furniture JSC", "Hanoi Teak Works"],
    "CN": ["Foshan Comfort Furniture Ltd", "Ningbo Brightlight Co.", "Shenzhen Home Living Ltd"],
    "TR": ["Inegol Mobilya A.S.", "Kayseri Textiles Ltd"],
    "IT": ["Brianza Design srl", "Murano Luce srl"],
}


def price_round(x: float) -> int:
    return int(round(x / 100.0)) * 100 - 10   # 4,990 style


def build_products() -> list[dict]:
    r = rng_for("products")
    products, seq = [], 1000
    for coll, country in COLLECTIONS.items():
        types = [t for t in PRODUCT_TYPES if country in t[5]]
        chosen = r.sample(types, k=min(len(types), r.randint(4, 7)))
        anchor = {"Oslo": "SOF", "Bergen": "DTB"}.get(coll)   # the two items the vendor demo quotes
        if anchor and all(t[0] != anchor for t in chosen):
            chosen.append(next(t for t in types if t[0] == anchor))
        for t in chosen:
            for color, color_he in r.sample(COLORS, k=r.randint(1, 3)):
                seq += r.randint(1, 9)
                code, en, he, ru, ar, _, (lo, hi) = t
                price = price_round(r.uniform(lo, hi))
                launched = date(r.randint(2018, 2026), r.randint(1, 12), 1)
                if launched > date(2026, 6, 1):
                    launched = date(2026, r.randint(1, 5), 1)
                products.append({
                    "sku": f"HP-{code}-{seq}", "type": code, "collection": coll, "country": country,
                    "name_en": f"{coll} {en}, {color}", "name_he": f"{he} {coll} {color_he}",
                    "word_ru": ru, "word_ar": ar, "color": color,
                    "supplier": r.choice(SUPPLIERS[country]), "price": price,
                    "price_2023": price_round(price / r.uniform(1.06, 1.22)),
                    "launched": launched, "discontinued": None,
                    "assembly": "Y" if code in ("BED", "WRD", "DRS", "DSK", "SHL", "OCH", "DTB") else "N",
                    "weight": round(r.uniform(4, 95), 1),
                })
    # About 12% of items were discontinued after 2023 (still sold until then).
    for p in products:
        if p["launched"] < date(2023, 1, 1) and r.random() < 0.18:
            p["discontinued"] = date(r.randint(2024, 2026), r.randint(1, 12), 1)
            if p["discontinued"] > date(2026, 4, 1):
                p["discontinued"] = date(2026, r.randint(1, 3), 1)
    # Two anchor products quoted in the vendor demo (see vendors/chatnest-sales-deck.md).
    oslo = next(p for p in products if p["collection"] == "Oslo" and p["type"] == "SOF")
    oslo.update(name_en="Oslo 3-seat sofa, grey", name_he="ספה תלת מושבית Oslo אפור", color="grey",
                price=4990, price_2023=4290, launched=date(2021, 3, 1), discontinued=None)
    bergen = next(p for p in products if p["collection"] == "Bergen" and p["type"] == "DTB")
    bergen.update(name_en="Bergen dining table 180, oak", name_he="שולחן אוכל Bergen 180 אלון", color="oak",
                  price=3990, price_2023=3450, launched=date(2020, 5, 1), discontinued=date(2025, 8, 1))
    return products


def sellable(products: list[dict], on: date) -> list[dict]:
    return [p for p in products if p["launched"] <= on and (p["discontinued"] is None or p["discontinued"] > on)]


# =============================================================================================
# 3. Containers (shipments) and their delays
# =============================================================================================
SCHEDULE = {  # first original ETA, days between containers, sea transit days, origin ports
    "VN": (date(2026, 3, 30), 7, 31, ["Ho Chi Minh City (Cat Lai)", "Haiphong"]),
    "CN": (date(2026, 4, 2), 7, 28, ["Ningbo", "Shenzhen (Yantian)", "Shanghai"]),
    "TR": (date(2026, 3, 22), 14, 5, ["Mersin", "Istanbul (Ambarli)"]),
    "IT": (date(2026, 3, 29), 14, 8, ["Genoa", "La Spezia"]),
}
CARRIERS = [("Oriental Lines", "ORLU"), ("MedStar Shipping", "MSTU"), ("Levant Container Line", "LCLU"),
            ("Adriatic Feeder Co.", "ADFU")]
VESSELS = ["Pacific Meridian", "Jade Horizon", "Cape Orchid", "Golden Lotus", "Aegean Star",
           "Liguria Express", "Bosphorus Bridge", "Coral Pioneer", "Silver Monsoon", "Harbor Lark"]
ETA_NOTES_HE = ["שינוי מסלול - הקפת אפריקה", "עומס בנמל המעבר", "החמצת חיבור בנמל שילוח", "עיכוב בהטענה אצל הספק",
                "עומס בנמל אשדוד", "הספק אישר", "ממתין לאישור משלוח", ""]


def build_shipments() -> list[dict]:
    r = rng_for("shipments")
    shipments, seq = [], 1
    for country, (first_eta, step, transit, ports) in SCHEDULE.items():
        eta = first_eta
        while eta <= date(2026, 12, 20):
            carrier, prefix = r.choice(CARRIERS)
            if country in ("VN", "CN"):
                if eta < date(2026, 5, 28):
                    delay = r.choice([-1, 0, 0, 0, 1, 1, 2, 3])
                elif eta < date(2026, 6, 12):
                    delay = max(2, round(r.gauss(8, 3)))
                else:
                    delay = min(30, max(5, round(r.gauss(15.6, 4.5))))
            else:
                delay = r.choice([-1, 0, 0, 1, 1, 2, 2, 3, 4, 6])
            actual = eta + timedelta(days=delay)
            s = {
                "ref": f"HP-IMP-26-{seq:03d}", "container": f"{prefix}{r.randint(1000000, 9999999)}",
                "country": country, "supplier": r.choice(SUPPLIERS[country]), "origin_port": r.choice(ports),
                "dest_port": r.choice(["Haifa", "Ashdod", "Ashdod"]), "carrier": carrier,
                "vessel": r.choice(VESSELS), "voyage": f"{r.randint(100, 999)}{r.choice('EWNS')}",
                "etd": eta - timedelta(days=transit), "eta": eta, "delay": delay, "actual": actual,
                "revisions": [], "note": "",
            }
            # Revised ETAs: the forwarder announces a delay in two or three steps.
            if delay >= 3:
                steps = [(eta - timedelta(days=12), eta + timedelta(days=round(delay * 0.4))),
                         (eta - timedelta(days=3), eta + timedelta(days=round(delay * 0.8)))]
                if delay >= 9:
                    steps.append((eta + timedelta(days=round(delay * 0.5)), actual))
                s["revisions"] = [(announced, new) for announced, new in steps if new != eta]
                s["note"] = r.choice(ETA_NOTES_HE[:5])
            s["customs"] = actual + timedelta(days=r.randint(1, 3))
            s["warehouse"] = s["customs"] + timedelta(days=r.randint(1, 2))
            shipments.append(s)
            seq += 1
            eta += timedelta(days=step)
    shipments.sort(key=lambda s: (s["eta"], s["ref"]))
    return shipments


def shipment_status(s: dict, at: date) -> str:
    if s["warehouse"] <= at:
        return "Delivered to warehouse"
    if s["actual"] <= at:
        return "Customs clearance"
    if s["etd"] <= at:
        return "At sea"
    return "Booked"


# =============================================================================================
# 4. Customers and orders
# =============================================================================================
CITIES = [  # city, weight, language mix (he, ar, ru, en)
    ("Tel Aviv-Yafo", 13, (70, 4, 10, 16)), ("Rishon LeZion", 8, (74, 2, 18, 6)),
    ("Haifa", 9, (52, 24, 19, 5)), ("Jerusalem", 7, (78, 6, 6, 10)), ("Petah Tikva", 5, (80, 1, 13, 6)),
    ("Holon", 4, (80, 1, 15, 4)), ("Netanya", 5, (63, 1, 20, 16)), ("Ashdod", 5, (55, 1, 40, 4)),
    ("Be'er Sheva", 4, (62, 6, 30, 2)), ("Ramat Gan", 4, (80, 2, 10, 8)), ("Herzliya", 3, (72, 1, 7, 20)),
    ("Kfar Saba", 3, (85, 2, 6, 7)), ("Nazareth", 3, (12, 86, 1, 1)), ("Umm al-Fahm", 2, (8, 92, 0, 0)),
    ("Shefa-'Amr", 2, (12, 88, 0, 0)), ("Tayibe", 2, (15, 85, 0, 0)), ("Karmiel", 2, (50, 12, 36, 2)),
    ("Bat Yam", 2, (52, 2, 44, 2)), ("Modi'in", 3, (82, 1, 5, 12)), ("Rehovot", 3, (80, 2, 12, 6)),
    ("Ashkelon", 2, (60, 1, 37, 2)), ("Acre", 1, (40, 45, 14, 1)), ("Eilat", 1, (65, 3, 22, 10)),
    ("Kiryat Ata", 2, (60, 10, 29, 1)), ("Ra'anana", 2, (62, 1, 5, 32)),
]
B2B_ACCOUNTS = [
    "Kinneret Shores Hotel", "Shikmona Boutique Hotel", "Galil Business Park", "Netanya Beach Suites",
    "Space9 Co-Working Ramat Gan", "Nof Carmel Hotel", "Eilat Coral Inn", "Herzliya Tech Offices Ltd",
    "Arava Desert Lodge", "Old Jaffa Port Hotel", "BlueGate Insurance (offices)", "Modi'in Medical Center (admin)",
    "Ramat Hanadiv Guest House", "Sea of Galilee Resort", "Jerusalem Garden Hotel", "Ayalon Law Offices",
]
LANGS = ("he", "ar", "ru", "en")


@dataclass
class Customer:
    cid: str
    first: str
    last: str
    native_first: str
    native_last: str
    lang: str          # the language they write in
    city: str
    phone: str
    email: str
    b2b: str = ""      # account name for business customers

    @property
    def native_name(self) -> str:
        return f"{self.native_first} {self.native_last}"

    @property
    def name(self) -> str:
        return f"{self.first} {self.last}"


def make_customer(r: random.Random, cid: str, city: str | None = None, lang: str | None = None) -> Customer:
    if city is None:
        city = r.choices([c[0] for c in CITIES], [c[1] for c in CITIES])[0]
    mix = next(c[2] for c in CITIES if c[0] == city)
    if lang is None:
        lang = r.choices(LANGS, mix)[0]
    # The name follows the person's background; some Russian and Arabic speakers write in Hebrew.
    origin = lang
    if lang == "he":
        origin = r.choices(["he", "ru", "ar"], [86, 9, 5])[0]
    if origin == "he":
        f, nf, g = r.choice(tb.HE_FIRST)
        l, nl = r.choice(tb.HE_LAST)
    elif origin == "ar":
        f, nf, g = r.choice(tb.AR_FIRST)
        l, nl = r.choice(tb.AR_LAST)
    elif origin == "ru":
        f, nf, g = r.choice(tb.RU_FIRST)
        l, nl, fem = r.choice(tb.RU_LAST)
        if g == "f" and fem:
            l, nl = l + "a", nl + "а"
    else:
        f, g = r.choice(tb.EN_FIRST)
        l = r.choice(tb.EN_LAST)
        nf, nl = f, l
    if lang == "he" and origin != "he":
        nf, nl = f, l   # writes Hebrew, signs with a Latin-letter name
    phone = f"05{r.choice('0234578')}-{r.randint(1000000, 9999999)}"
    domain = r.choices(["gmail.com", "walla.co.il", "hotmail.com", "yahoo.com", "bezeqint.net", "012.net.il",
                        "mail.ru"], [58, 10, 9, 5, 6, 4, 8 if lang == "ru" else 0])[0]
    handle = f"{f.lower()}{r.choice(['.', '', '_'])}{l.lower().replace('-', '')}{r.choice(['', str(r.randint(1, 99)), str(r.randint(70, 99))])}"
    return Customer(cid, f, l, nf, nl, lang, city, phone, f"{handle}@{domain}")


@dataclass
class Order:
    oid: str
    placed: datetime
    channel: str
    customer: Customer
    product: dict
    qty: int
    total: int
    promised: date
    shipment: dict
    delivered: datetime          # when it reached (or will reach) the customer
    container_shown: str         # what the ERP shows (sometimes blank)
    cancelled: bool = False

    @property
    def lag(self) -> int:
        return (self.delivered.date() - self.promised).days


def build_orders(products: list[dict], shipments: list[dict]) -> tuple[list[Order], list[Customer]]:
    r = rng_for("orders")
    month_factor = {3: .9, 4: 1.0, 5: .9, 6: .95, 7: 1.0, 8: 1.15, 9: 1.2, 10: 1.05}
    dow_factor = {6: 1.0, 0: 1.05, 1: 1.05, 2: 1.0, 3: 1.1, 4: .8, 5: .55}
    b2b_customers = [Customer(f"C2{100 + i:04d}", "", "", "", "", "he" if i % 4 else "en", "", "", "", acc)
                     for i, acc in enumerate(B2B_ACCOUNTS)]
    for c in b2b_customers:
        contact = make_customer(r, c.cid, lang=c.lang)
        c.first, c.last, c.native_first, c.native_last = contact.first, contact.last, contact.native_first, contact.native_last
        c.city, c.phone = contact.city, contact.phone
        c.email = f"{contact.first.lower()}@{c.b2b.split()[0].lower().replace(chr(39), '')}.co.il"
    customers: list[Customer] = list(b2b_customers)
    orders: list[Order] = []
    by_country: dict[str, list[dict]] = {}
    for s in shipments:
        by_country.setdefault(s["country"], []).append(s)
    seq, cust_seq = 4100, 104000
    for d in days(ORDERS_FROM, EXPORT_AT.date()):
        for _ in range(poisson(r, 14.0 * month_factor[d.month] * dow_factor[d.weekday()])):
            channel = r.choices(["web", "showroom_tlv", "showroom_haifa", "b2b"], [52, 22, 14, 12])[0]
            if d.weekday() == 5:
                channel = "web"   # showrooms are closed on Saturday
            if channel == "b2b":
                cust = r.choice(b2b_customers)
            elif customers and r.random() < 0.05:
                cust = r.choice(customers)
            else:
                city = None
                if channel == "showroom_haifa":
                    city = r.choice(["Haifa", "Haifa", "Kiryat Ata", "Nazareth", "Shefa-'Amr", "Karmiel", "Acre"])
                cust_seq += r.randint(1, 4)
                cust = make_customer(r, f"C{cust_seq}", city)
                customers.append(cust)
            hours = CUSTOMER_HOUR_WEIGHTS if channel == "web" else [0] * 10 + [5] * 10 + [0] * 4
            placed = random_moment(r, d, hours)
            prod = r.choice(sellable(products, d))
            if channel == "b2b":
                qty = r.randint(10, 80) if prod["type"] in ("DCH", "OCH") else r.randint(2, 20)
                total = round(qty * prod["price"] * 0.82)
            else:
                qty = r.choice([4, 6, 6, 8]) if prod["type"] == "DCH" else 1
                total = qty * prod["price"] + r.choice([0, 0, 0, 290, 390, 590])   # delivery / add-ons
            promised = d + timedelta(days=LEAD_DAYS[prod["country"]])
            # Purchasing allocates the order to the container planned to land 7-13 days (Turkey and
            # Italy: 7-20 days) before the promised date, which leaves time for customs and delivery.
            window = 13 if prod["country"] in ("VN", "CN") else 20
            fits = [s for s in by_country[prod["country"]]
                    if promised - timedelta(days=window) <= s["eta"] <= promised - timedelta(days=7)]
            ship = fits[-1]
            ready = ship["warehouse"] + timedelta(days=r.randint(1, 4))
            delivered = random_moment(r, next_workday(ready), [0] * 8 + [5] * 9 + [0] * 7)
            seq += r.randint(1, 3)
            orders.append(Order(f"SO26{seq:06d}", placed, channel, cust, prod, qty, total, promised, ship,
                                delivered, "" if r.random() < 0.03 else ship["container"]))
    return orders, customers


# =============================================================================================
# 5. Support tickets
# =============================================================================================
@dataclass
class Ticket:
    created: datetime
    cat: str                 # TRUE category (answer key)
    lang: str                # TRUE language of the message
    customer: Customer
    order: Order | None
    variant: str = ""        # "", "early" (before the promised date), "followup"
    kind: str = "new"        # new / followup / duplicate
    parent: "Ticket | None" = None
    org: str = ""            # for B2B quotes from prospects
    # filled by the simulation
    tid: int = 0
    channel: str = ""
    subject: str = ""
    webform_reason: str = ""
    first_response: datetime | None = None
    resolved: datetime | None = None
    status: str = ""
    agent: str = ""
    category: str = ""
    detected_lang: str = ""
    order_ref: str = ""
    tags: list[str] = field(default_factory=list)
    used_macro: bool = False
    work_min: str = ""
    csat: str = ""
    priority: str = "normal"
    merged: bool = False
    claim_no: str = ""
    template_seed: int = 0


def order_events(r: random.Random, orders: list[Order]) -> list[Ticket]:
    """Tickets that customers open about an order."""
    out = []
    for o in orders:
        c, lag, deliv = o.customer, o.lag, o.delivered
        # A few anxious customers ask before the promised date.
        if r.random() < 0.05:
            t = contact_moment(r, o.promised - timedelta(days=r.randint(2, 12)))
            if t < deliv:
                out.append(Ticket(t, "wismo", c.lang, c, o, "early"))
        # When the promised date passes, the chance of a "where is my order?" grows with the delay.
        if lag > 0 and r.random() < min(0.66, 0.14 + 0.036 * lag):
            t = contact_moment(r, o.promised + timedelta(days=r.randint(0, min(lag - 1, 4))))
            if t < deliv:
                out.append(Ticket(t, "wismo", c.lang, c, o))
        if 0 <= lag <= 2 and r.random() < 0.04:   # the delivery company calls to book a slot
            out.append(Ticket(contact_moment(r, deliv.date() - timedelta(days=r.randint(1, 3))), "reschedule", c.lang, c, o))
        elif r.random() < 0.025:
            out.append(Ticket(contact_moment(r, deliv.date() - timedelta(days=r.randint(1, 4))), "reschedule", c.lang, c, o))
        after = deliv.date()
        for cat, p, lo, hi in (("damage", .066, 0, 2), ("assembly", .05, 0, 6), ("returns", .034, 1, 12),
                               ("complaint", .022, 0, 1)):
            if r.random() < p:
                out.append(Ticket(contact_moment(r, after + timedelta(days=r.randint(lo, hi))), cat, c.lang, c, o))
        if r.random() < (0.12 if c.b2b else 0.03):
            out.append(Ticket(contact_moment(r, o.placed.date() + timedelta(days=r.randint(2, 40))), "invoice", c.lang, c, o))
    return out


def other_events(r: random.Random, customers: list[Customer]) -> list[Ticket]:
    """Tickets that are not about a specific order: pre-sale questions, quotes, spam, other."""
    out, req = [], 30000
    prospects = ["Dead Sea View Hotel", "Ramat Aviv Dental Clinics", "Kiryat Shmona College", "Hadera Seniors Home",
                 "Startup Nation Hub", "Tiberias Lakeside Hotel", "Holon Municipality (procurement)",
                 "Beit Lessin Offices", "Rosh Pina Boutique Inn", "Ashkelon Marina Hotel"]
    for d in days(DATA_START.date(), EXPORT_AT.date()):
        for cat, lam in (("product_question", 1.6), ("b2b_quote", .5), ("other", 1.15), ("spam", .8),
                         ("complaint", .1)):
            for _ in range(poisson(r, lam)):
                req += r.randint(1, 7)
                if cat == "spam":
                    lang = r.choices(["en", "he"], [85, 15])[0]
                    c = Customer(f"REQ-{req}", "", "", "", "", lang, "", "", r.choice(
                        ["info@seo-rank-pro.net", "sales@foshan-chairs.cn", "admin@mail-verify-center.com",
                         "partners@growthly.io", "billing@invoices-online.biz", "deals@loans-now.co.il"]))
                    out.append(Ticket(contact_moment(r, d), "spam", lang, c, None))
                    continue
                if cat == "b2b_quote":
                    if r.random() < 0.4:
                        c = r.choice([x for x in customers if x.b2b])
                        org = c.b2b
                    else:
                        c = make_customer(r, f"REQ-{req}", lang=r.choices(LANGS, [70, 6, 4, 20])[0])
                        org = r.choice(prospects)
                    out.append(Ticket(contact_moment(r, d), cat, c.lang, c, None, org=org))
                    continue
                c = make_customer(r, f"REQ-{req}")
                out.append(Ticket(contact_moment(r, d), cat, c.lang, c, None))
    return out


def helpdesk_category(r: random.Random, t: Ticket) -> str:
    """What the agent picks in the helpdesk's category field (often 'Other/כללי')."""
    new = t.created >= CATEGORY_CHANGE
    other = "Other/כללי"
    table = {
        "wismo": [("Delivery status" if new else "Delivery", 55), (other, 33), ("Complaint", 6), ("Product info", 3), ("Returns & refunds", 3)],
        "reschedule": [("Delivery status" if new else "Delivery", 65), (other, 35)],
        "damage": ([("Delivery damage", 72), ("Returns & refunds", 8), ("Complaint", 6), (other, 14)] if new else
                   [("Delivery", 50), ("Returns & refunds", 17), ("Complaint", 11), (other, 22)]),
        "assembly": [("Assembly", 82), (other, 18)],
        "returns": [("Returns & refunds", 84), (other, 16)],
        "invoice": [("Invoice & payment", 85), (other, 15)],
        "b2b_quote": [("B2B", 90), (other, 10)],
        "product_question": [("Product info", 70), (other, 30)],
        "complaint": [("Complaint", 78), (other, 22)],
        "other": [(other, 72), ("Product info", 18), ("Complaint", 10)],
        "spam": [("Spam", 92), (other, 8)],
    }[t.cat]
    if r.random() < 0.03:
        return ""   # left blank
    return r.choices([c for c, _ in table], [w for _, w in table])[0]


WEBFORM_REASON = {  # true category -> what customers pick in the web form's dropdown
    "wismo": [("status", 80), ("other", 20)], "reschedule": [("status", 60), ("other", 40)],
    "damage": [("damage", 75), ("returns", 10), ("other", 15)], "assembly": [("assembly", 70), ("other", 30)],
    "returns": [("returns", 75), ("other", 25)], "invoice": [("invoice", 70), ("other", 30)],
    "b2b_quote": [("b2b", 75), ("other", 25)], "product_question": [("other", 85), ("status", 15)],
    "complaint": [("other", 70), ("status", 20), ("damage", 10)], "other": [("other", 90), ("status", 10)],
}

AGENT_MINUTES = {  # median handling minutes (time-tracking timer) per true category
    "wismo": 7, "damage": 14, "assembly": 8, "returns": 11, "invoice": 6, "b2b_quote": 22,
    "product_question": 6, "complaint": 15, "reschedule": 5, "other": 5, "spam": 1,
}


def fmt_date(d: date, lang: str) -> str:
    if lang == "en":
        return d.strftime("%d %b").lstrip("0")
    if lang == "ru":
        return d.strftime("%d.%m")
    return f"{d.day}/{d.month}"


def product_in(lang: str, p: dict) -> str:
    return {"he": p["name_he"], "en": p["name_en"], "ru": f"{p['word_ru']} {p['collection']}",
            "ar": f"{p['word_ar']} {p['collection']}"}[lang]


def order_ref(r: random.Random, oid: str) -> str:
    """How the order number appears in the ticket: usually clean, sometimes typed by hand."""
    x = r.random()
    if x < 0.94:
        return oid
    return r.choice([oid.lower(), f"SO-{oid[2:]}", oid[2:], f"#{oid[4:]}", f"SO {oid[2:]}"])


def detected(r: random.Random, lang: str) -> str:
    """The helpdesk's automatic language detection (wrong now and then, blank on short texts)."""
    if r.random() < 0.92:
        return lang
    return r.choice({"he": ["", "yi", ""], "ar": ["fa", "ur", ""], "ru": ["uk", "bg", ""],
                     "en": ["", "nl", "de"]}[lang])


def build_tickets(orders: list[Order], customers: list[Customer], staff: list[Person]) -> list[Ticket]:
    r = rng_for("tickets")
    events = order_events(r, orders) + other_events(r, customers)
    base = sorted([t for t in events if DATA_START <= t.created <= EXPORT_AT],
                  key=lambda t: (t.created, t.customer.cid))
    # Queue pressure: in busy weeks agents answer later.
    week_counts: dict[date, int] = {}
    for t in base:
        wk = t.created.date() - timedelta(days=(t.created.weekday() + 1) % 7)
        week_counts[wk] = week_counts.get(wk, 0) + 1
    typical = statistics.median(week_counts.values())

    def load(t: datetime) -> float:
        wk = t.date() - timedelta(days=(t.weekday() + 1) % 7)
        return min(1.6, max(0.75, (week_counts.get(wk, typical) / typical) ** 0.6))

    def respond(t: Ticket) -> None:
        t.template_seed = r.randrange(10 ** 6)
        if not t.channel:
            t.channel = "email" if r.random() < 0.68 else "web_form"
        if t.cat == "spam":
            t.channel = "email"
        t.detected_lang = detected(r, t.lang)
        t.category = helpdesk_category(r, t)
        if t.order:
            keep = {"wismo": .86, "damage": .9, "assembly": .8, "returns": .85, "invoice": .92,
                    "complaint": .7, "reschedule": .9}.get(t.cat, .8)
            t.order_ref = order_ref(r, t.order.oid) if r.random() < keep else ""
        if t.cat == "spam":
            t.status, t.category = "closed", t.category or "Spam"
            return
        if t.cat == "damage" and t.kind != "duplicate" and r.random() < 0.6:
            t.agent = "Rina Azoulay"
        elif t.cat == "complaint" and r.random() < 0.3:
            t.agent = "Samir Haddad"
        else:
            pool = CS_AGENTS_BY_LANG[t.lang]
            t.agent = r.choices([a for a, _ in pool], [w for _, w in pool])[0]
        if t.channel == "email":
            wait = r.lognormvariate(math.log(1.1), 1.0) * load(t.created)
        else:   # the web-form queue is checked a few times a day
            wait = r.lognormvariate(math.log(2.0), 0.85) * load(t.created)
        fr = add_support_hours(t.created, wait)
        if fr > EXPORT_AT:
            t.status = "open"
            return
        t.first_response = fr
        # Agents set "resolved" when they send the reply. A minority wait for the customer first.
        if r.random() < 0.8:
            t.resolved = fr + timedelta(seconds=r.randint(5, 240))
            t.status = "resolved"
        else:
            later = add_support_hours(fr, r.uniform(9, 45))
            if later <= EXPORT_AT:
                t.resolved, t.status = later, "resolved"
            else:
                t.status = "pending"
        t.used_macro = t.cat == "wismo" and r.random() < 0.85 or t.cat == "reschedule" and r.random() < 0.1
        if t.agent in TIMER_USERS and r.random() < 0.9:
            minutes = r.lognormvariate(math.log(AGENT_MINUTES[t.cat]), 0.5)
            if t.lang in ("ru", "ar"):
                minutes *= 1.45   # writing a careful reply in Russian or Arabic takes longer
            t.work_min = str(max(1, round(minutes)))
        if t.resolved and r.random() < 0.2:
            bad = {"wismo": .5, "damage": .4, "complaint": .6}.get(t.cat, .12)
            if t.kind == "followup":
                bad = .7
            t.csat = "bad" if r.random() < bad else "good"

    for t in base:
        respond(t)

    # Follow-ups: the customer writes again within two weeks of a "resolved" reply (a new ticket).
    follow_p = {"damage": .25, "assembly": .17, "returns": .19, "invoice": .1, "complaint": .14,
                "reschedule": .05}
    all_tickets = list(base)
    queue = [t for t in base]
    while queue:
        t = queue.pop(0)
        if t.status != "resolved" or not t.order or t.cat in ("spam",):
            continue
        if t.cat == "wismo":
            still_waiting = t.order.delivered > t.resolved + timedelta(days=4)
            p = 0.21 if still_waiting else 0.04
        else:
            p = follow_p.get(t.cat, 0.03)
        if t.kind == "followup":
            p *= 0.6
        if r.random() >= p:
            continue
        gap = timedelta(hours=r.uniform(12, 24 * 13.5))
        when = t.resolved + gap
        if t.cat == "wismo":
            when = min(when, t.order.delivered - timedelta(hours=6))
            if when <= t.resolved + timedelta(hours=6):
                continue
        if when > EXPORT_AT:
            continue
        f = Ticket(when, t.cat, t.lang, t.customer, t.order, "followup", "followup", t)
        if r.random() < 0.5:
            f.channel = t.channel
        respond(f)
        all_tickets.append(f)
        queue.append(f)

    # Duplicates: the same customer sends the same message again within the hour (6% of tickets).
    candidates = sorted([t for t in all_tickets if t.cat != "spam"], key=lambda t: (t.created, t.customer.cid))
    n_dup = round(0.0638 * len(all_tickets))
    for t in r.sample(candidates, n_dup):
        when = t.created + timedelta(minutes=r.randint(2, 58), seconds=r.randint(0, 59))
        if when > EXPORT_AT:
            continue
        d = Ticket(when, t.cat, t.lang, t.customer, t.order, t.variant, "duplicate", t, t.org)
        d.channel = r.choice(["email", "web_form"])
        if r.random() < 0.35:   # an agent noticed and merged it
            d.template_seed = r.randrange(10 ** 6)
            d.merged, d.status = True, "closed"
            d.detected_lang = detected(r, d.lang)
            d.category = helpdesk_category(r, d)
            d.order_ref = order_ref(r, t.order.oid) if t.order and t.order_ref else ""
            d.tags = ["duplicate", "merged"]
        else:
            respond(d)
        all_tickets.append(d)

    all_tickets.sort(key=lambda t: (t.created, t.customer.cid, t.kind))
    tid = 31840
    for t in all_tickets:
        tid += r.choice([1, 1, 1, 2, 3])   # gaps: tickets deleted by the spam filter
        t.tid = tid
        build_subject_and_tags(r, t)
    return all_tickets


def build_subject_and_tags(r: random.Random, t: Ticket) -> None:
    o = t.order
    fill = {"order": t.order_ref or (o.oid if o else ""), "org": t.org}
    if t.channel == "web_form" and t.cat != "spam":
        site_lang = t.lang if t.lang in ("he", "en") else r.choices(["he", "en"], [70, 30])[0]
        pool = WEBFORM_REASON[t.cat]
        reason = r.choices([x for x, _ in pool], [w for _, w in pool])[0]
        t.webform_reason = reason
        t.subject = tb.WEBFORM_SUBJECT[site_lang].format(reason=tb.WEBFORM_REASONS[site_lang][reason])
    else:
        lang = t.lang if t.lang in tb.SUBJECTS[t.cat] else "en"
        subject = r.choice(tb.SUBJECTS[t.cat][lang])
        if not fill["order"] and "{order}" in subject:
            subject = subject.replace(" {order}", "").replace("{order}", "")
        t.subject = subject.format(**fill)
        if t.kind == "followup" and r.random() < 0.4 and t.parent and t.parent.subject:
            t.subject = "Re: " + t.parent.subject
        if t.kind == "duplicate" and t.parent and r.random() < 0.5:
            t.subject = t.parent.subject if t.parent.channel == "email" else t.subject
    if t.merged:
        return
    tags = []
    if t.used_macro:
        tags.append("macro_order_status")
        if t.created >= datetime(2026, 8, 15) and r.random() < 0.12:
            tags.append("עיכוב_מכולה")
    if t.cat == "damage" and t.first_response and r.random() < 0.7:
        tags.append("macro_damage_photos")
    if t.cat == "returns" and t.first_response and r.random() < 0.6:
        tags.append("macro_returns_policy")
    if t.customer.b2b or t.cat == "b2b_quote":
        tags.append("b2b")
        t.priority = "high"
    if t.cat == "complaint" and r.random() < 0.3:
        tags.append("escalated")
        t.priority = "high"
    if t.kind == "followup" and r.random() < 0.08:
        tags.append("2nd_contact")
    if t.lang in ("ru", "ar") and r.random() < 0.2:
        tags.append({"ru": "russian", "ar": "arabic"}[t.lang])
    if t.cat == "spam" and r.random() < 0.5:
        tags.append("spam")
    t.tags = tags


# =============================================================================================
# 6. Emails (a sample of 600 tickets with the full text)
# =============================================================================================
def email_text(t: Ticket, staff: list[Person]) -> tuple[str, str, str]:
    """(customer body, agent reply, attachments) for one ticket, reproducible from its seed."""
    r = random.Random(f"{SEED}:email:{t.tid}")
    c, o, lang = t.customer, t.order, t.lang
    key = t.cat
    if t.cat == "wismo" and t.variant == "early":
        key = "wismo_early"
    elif t.kind == "followup" and f"{t.cat}_followup" in tb.BODIES:
        key = f"{t.cat}_followup"
    bank = tb.BODIES[key]
    lang_for_text = lang if lang in bank else "en"
    street = r.choice(tb.STREETS_HE) if lang != "en" else r.choice(tb.STREETS_EN)
    city = c.city or "Tel Aviv-Yafo"
    fill = {
        "first": c.native_first or c.first, "name": c.name, "native_name": c.native_name.strip() or c.name,
        "order": t.order_ref or (o.oid if o else ""), "phone": c.phone,
        "order_date": fmt_date(o.placed.date(), lang) if o else "", "promised": fmt_date(o.promised, lang) if o else "",
        "product": product_in(lang_for_text, o.product) if o else product_in(
            lang_for_text, PRODUCTS_BY_SEED[t.tid % len(PRODUCTS_BY_SEED)]),
        "detail": r.choice(tb.DAMAGE_DETAILS.get(lang, tb.DAMAGE_DETAILS["en"])),
        "address": f"{street} {r.randint(1, 120)}, {city}", "org": t.org or c.b2b,
        "n": r.choice([24, 40, 60, 80, 120]), "m": r.choice([6, 10, 15, 20]),
        "date2": fmt_date(t.created.date() + timedelta(days=r.randint(45, 120)), lang),
    }
    body = r.choice(bank[lang_for_text]).format(**fill)
    if t.cat != "spam":
        body += r.choice(tb.SIGNATURES[lang_for_text]).format(**fill)
    if t.kind == "duplicate":
        body = r.choice(tb.RESEND_PREFIX[lang_for_text]) + body
    attachments = ""
    if t.cat == "damage" and t.kind != "followup":
        attachments = "; ".join(f"IMG_{r.randint(1000, 9999)}.jpg" for _ in range(r.randint(1, 4)))
    elif t.cat == "spam" and r.random() < 0.4:
        attachments = r.choice(["catalog_2026.pdf", "INV-88213.pdf.html", "audit.zip"])
    reply = ""
    if t.first_response and not t.merged:
        agent = next(p for p in staff if p.name == t.agent)
        reply_lang = t.lang
        if agent.name == "Rina Azoulay" or (t.lang == "ru" and "Russian" not in agent.langs) or (
                t.lang == "ar" and "Arabic" not in agent.langs):
            reply_lang = "he"   # agents who don't speak the language answer in Hebrew
        rkey = t.cat
        if t.cat == "wismo":
            rkey = "wismo_macro" if t.used_macro else "wismo_checked"
        if rkey not in tb.REPLIES:
            rkey = "other"
        eta = o.shipment["actual"] if o else t.created.date()
        rfill = dict(fill, first=(c.native_first or c.first) if reply_lang == lang else c.first,
                     agent=agent.first, claim=t.claim_no or "DC-26-0xx",
                     promised=fmt_date(o.promised, reply_lang) if o else "", eta=fmt_date(eta, reply_lang))
        rfill["agent"] = tb.AGENT_SIGN.get(agent.name, {}).get(reply_lang, agent.first)
        reply = tb.REPLIES[rkey][reply_lang].format(**rfill)
    return body, reply, attachments


PRODUCTS_BY_SEED: list[dict] = []   # set in main(): products for messages that name no order


def build_emails(tickets: list[Ticket], staff: list[Person]) -> tuple[list[list], list[dict]]:
    r = rng_for("emails")
    sample = sorted(r.sample(tickets, 600), key=lambda t: t.tid)
    rows, truth = [], []
    # Five replies where the agent pasted a chatbot's answer without cleaning it (shadow AI).
    ai_plan = [("Olga Petrenko", "ru", "preamble"), ("Olga Petrenko", "ru", "preamble"),
               ("Olga Petrenko", "ru", "placeholder"), ("Lina Khoury", "ar", "preamble"),
               ("Yana Kogan", "ru", "placeholder"), ("Daniel Shaw", "en", "preamble")]
    planted: dict[int, str] = {}
    for agent, lang, kind in ai_plan:
        options = [t for t in sample if t.agent == agent and t.lang == lang and t.first_response
                   and not t.merged and t.tid not in planted and t.cat != "spam"]
        if options:
            planted[r.choice(options).tid] = kind
    for t in sample:
        body, reply, attachments = email_text(t, staff)
        ai = planted.get(t.tid, "")
        if ai and reply:
            rr = random.Random(f"{SEED}:ai:{t.tid}")
            reply_lang = t.lang
            if ai == "preamble":
                reply = rr.choice(tb.AI_PREAMBLES[reply_lang]) + reply
            else:
                first = t.customer.native_first or t.customer.first
                reply = reply.replace(first, tb.AI_PLACEHOLDER_NAME[reply_lang], 1)
        c = t.customer
        from_name = c.b2b and f"{c.name} ({c.b2b})" or (c.native_name.strip() or c.email.split("@")[0])
        if t.channel == "web_form":
            to_addr = "webform@harborpine.co.il"
        else:
            to_addr = "service@harborpine.co.il" if r.random() < 0.85 else "info@harborpine.co.il"
        rows.append([f"EM-{t.tid}", t.tid, iso(t.created), from_name, c.email, to_addr, t.subject, body,
                     attachments, iso(t.first_response) if reply else "", t.agent if reply else "", reply])
        truth.append({"email_id": f"EM-{t.tid}", "ticket_id": t.tid, "true_category": t.cat,
                      "true_language": t.lang, "kind": t.kind, "ai_artifact_in_reply": ai if reply else ""})
    return rows, truth


# =============================================================================================
# 7. Phone system log (inbound calls, UTC)
# =============================================================================================
def build_calls(staff: list[Person]) -> list[list]:
    r = rng_for("calls")
    rows, seq = [], 880000
    agents_by_queue = {
        "he": ["Hila Dahan", "Moran Biton", "Adi Golan", "Shani Ohayon", "Tigist Mekonen", "Daniel Shaw", "Ahmad Jabareen"],
        "ar": ["Lina Khoury", "Rami Nasser", "Ahmad Jabareen"], "ru": ["Olga Petrenko", "Yana Kogan", "Sergei Novikov"],
        "en": ["Daniel Shaw", "Shani Ohayon"],
    }
    ext = {name: 200 + i for i, name in enumerate(sorted({a for v in agents_by_queue.values() for a in v}))}
    for d in days(DATA_START.date(), EXPORT_AT.date()):
        busy = 1.0 + (0.35 if d >= date(2026, 7, 15) else 0) + (0.2 if d.month in (9, 10) else 0)
        n = poisson(r, (18 if d.weekday() in ISRAELI_WORKDAYS else 4) * busy)
        for _ in range(n):
            start = random_moment(r, d, [0] * 7 + [2, 6, 7, 7, 6, 6, 6, 5, 5, 4, 2, 2, 1, 1, 0, 0, 0])
            lang = r.choices(LANGS, [64, 14, 16, 6])[0]
            option = r.choices(["1", "2", "3", "4"], [42, 18, 7, 33])[0]
            queue = "B2B" if option == "3" else {"he": "Hebrew", "ar": "Arabic", "ru": "Russian", "en": "English"}[lang]
            window = support_window(d)
            open_now = window and window[0] + timedelta(minutes=30) <= start < window[1]
            seq += 1
            caller = f"+972-5{r.randint(0, 8)}-XXX-{r.randint(1000, 9999)}"
            if not open_now:
                rows.append([seq, iso_utc(start), caller, lang, option, queue, "after_hours", "", "", "", ""])
                continue
            wait = r.lognormvariate(math.log(70), 0.75) * busy
            patience = r.lognormvariate(math.log(260), 0.6)
            if wait > patience:
                rows.append([seq, iso_utc(start), caller, lang, option, queue, "abandoned", round(patience), "", "", ""])
                continue
            agent = r.choice(agents_by_queue[lang] if queue != "B2B" else ["Daniel Shaw", "Hila Dahan"])
            talk = round(r.lognormvariate(math.log(260 if option == "1" else 340), 0.5))
            rows.append([seq, iso_utc(start), caller, lang, option, queue, "answered", round(wait), talk,
                         ext[agent], agent])
    rows.sort(key=lambda x: (x[1], x[0]))   # the phone system numbers calls in time order
    for i, row in enumerate(rows):
        row[0] = 880001 + i
    return rows


# =============================================================================================
# 8. Damage claims log (kept by hand by the claims coordinator)
# =============================================================================================
def build_claims(tickets: list[Ticket]) -> tuple[list[list], list[dict]]:
    r = rng_for("claims")
    rows, truth, seq = [], [], 0
    damage = [t for t in tickets if t.cat == "damage" and t.kind == "new" and t.first_response]
    for t in damage:
        if r.random() > 0.9:
            continue   # never logged
        seq += 1
        claim = f"DC-26-{seq:03d}"
        t.claim_no = claim
        if "claim_opened" not in t.tags and r.random() < 0.5:
            t.tags.append("claim_opened")
        o = t.order
        opened = t.first_response.date()
        value = round(o.product["price"] * min(o.qty, r.choice([1, 1, 2])) * r.uniform(0.15, 1.0), -1)
        recorded = r.random() >= 0.38
        decision = decision_date = compensation = chargeback = ""
        if recorded:
            decision = r.choices(["אושר", "אושר חלקית", "נדחה"], [62, 23, 15])[0]
            decided = opened + timedelta(days=round(r.lognormvariate(math.log(8), 0.6)))
            decision_date = decided.strftime("%d/%m/%Y")
            compensation = {"אושר": r.choice(["החלפה", "החלפה", "זיכוי", "תיקון"]),
                            "אושר חלקית": r.choice(["זיכוי חלקי", "תיקון"]), "נדחה": ""}[decision]
            chargeback = r.choice(["כן", "לא", "", "בבדיקה"]) if decision != "נדחה" else "לא"
        notes = r.choice(["", "", "", "חיכיתי לתמונות", "סמיר אישר בטלפון", "להעביר לספק", "לקוח לחוץ",
                          "נזק מהובלה?", "תמונות לא ברורות", "ביקש פיצוי כספי", "דיברתי עם תמר - מכולה הגיעה רטובה"])
        if not recorded and r.random() < 0.3:
            notes = r.choice(["לבדוק מול הספק", "ממתין", "?"])
        c = t.customer
        rows.append([claim, opened.strftime("%d/%m/%Y"), t.tid if r.random() > 0.08 else "", o.oid,
                     c.name, c.phone, o.product["sku"], o.product["name_he"],
                     r.choice(["שבר", "שריטה", "קרע בבד", "זכוכית שבורה", "חסר חלק", "רטיבות", "עיוות"]),
                     r.choice(["כן", "כן", "כן", "לא"]), o.product["supplier"], o.shipment["container"],
                     money(value), decision, decision_date, compensation, chargeback, notes])
        truth.append({"claim_no": claim, "ticket_id": t.tid, "outcome_recorded": recorded})
    return rows, truth


# =============================================================================================
# 9. People: headcount, time sheets
# =============================================================================================
def build_timesheets(staff: list[Person]) -> list[list]:
    r = rng_for("timesheets")
    cs = [p for p in staff if p.team == "Customer Service"]
    rows = []
    week = date(2025, 11, 2)   # a Sunday
    while week <= date(2026, 10, 25):
        peak = week <= date(2026, 1, 25)
        for p in cs:
            if r.random() < 0.03:
                continue   # time sheet not submitted that week
            contracted = 42.0 * p.fte
            absence = r.choices([0, 0, 0, 0, 0, 8.5, 8.5, 17, 42], k=1)[0] if not peak else r.choice([0, 0, 0, 0, 8.5])
            absence = min(absence, contracted)
            available = contracted - absence
            util = r.gauss(0.925 if peak else 0.81, 0.03)
            if week >= date(2026, 7, 12) and not peak:
                util += 0.04   # the delay-driven WISMO wave
            logged = round(available * min(util, 1.0) * 2) / 2
            if p.name == "Samir Haddad":
                email, phone = logged * 0.3, logged * 0.1
            elif p.name == "Rina Azoulay":
                email, phone = logged * 0.55, logged * 0.15
            else:
                email = logged * r.gauss(0.72, 0.04)
                phone = logged * r.gauss(0.19, 0.03)
            email, phone = round(email * 2) / 2, round(phone * 2) / 2
            other = max(0.0, logged - email - phone)
            note = ""
            if r.random() < 0.04:
                note = r.choice(["שבוע עמוס - עיכובי מכולות", "הדרכה", "כולל שעות נוספות", "חסר יום - מילואים",
                                 "busy week", "סגירת חודש"])
            rows.append([week.isoformat(), p.emp_id, p.name, p.role, f"{contracted:.1f}", f"{absence:.1f}",
                         f"{email:.1f}", f"{phone:.1f}", f"{other:.1f}", f"{logged:.1f}", note])
        week += timedelta(days=7)
    return rows


def build_whatsapp_tally(staff: list[Person]) -> list[list]:
    """One week of WhatsApp Business conversations, tallied by hand by the agents (no export exists).

    Most customers write to the four shared WhatsApp phones, not to the helpdesk. Samir asked the team
    to note every conversation for one week in October; this is that sheet, typed up as people typed it.
    """
    r = rng_for("whatsapp-tally")
    agents = [p for p in staff if p.team == "Customer Service" and p.name not in ("Samir Haddad", "Rina Azoulay")]
    # (share, how agents wrote the topic, minutes range)
    topics = [
        (0.46, ["איפה ההזמנה", "מתי מגיע", "בירור מועד אספקה", "where is my order", "где заказ", "وين الطلبية",
                "עיכוב באספקה", "לקוח שואל על משלוח", "איפה הספה", "מועד משלוח"], (5, 15)),
        (0.15, ["תיאום הובלה", "תיאום משלוח", "לשנות תאריך הובלה", "delivery booking", "תיאום מועד"], (5, 15)),
        (0.12, ["נזק", "שריטה", "פגם במוצר", "damage", "רגל שבורה", "תמונות נזק", "повреждение"], (10, 30)),
        (0.08, ["הרכבה", "שאלה על הרכבה", "חסרים ברגים", "assembly", "сборка", "تركيب"], (5, 20)),
        (0.07, ["החזרה", "ביטול הזמנה", "החזר כספי", "return", "возврат"], (10, 20)),
        (0.04, ["הצעת מחיר", "לקוח עסקי", "B2B", "מלון - הזמנה גדולה"], (10, 30)),
        (0.08, ["שאלה על מוצר", "מלאי", "מבצע", "חשבונית", "אחר", "", "שאלה כללית"], (5, 10)),
    ]
    langs = [("עברית", 0.55), ("רוסית", 0.17), ("ערבית", 0.14), ("אנגלית", 0.06), ("en", 0.03), ("ru", 0.03), ("", 0.02)]
    rows = []
    for d in days(date(2026, 10, 18), date(2026, 10, 22)):   # Sunday to Thursday
        for agent in agents:
            if r.random() < 0.08:
                continue   # forgot to fill the sheet that day
            for _ in range(poisson(r, 11.5)):
                share = r.random()
                acc = 0.0
                for weight, words, (lo, hi) in topics:
                    acc += weight
                    if share <= acc:
                        break
                topic = r.choice(words)
                minutes = r.choice([m for m in (5, 10, 15, 20, 30) if lo <= m <= hi])
                lang = r.choices([l for l, _ in langs], weights=[w for _, w in langs], k=1)[0]
                hour = r.choice(["בוקר", "צהריים", "אחה\"צ", f"{r.randint(8, 16)}:{r.choice(['00', '15', '30', '45'])}"])
                order_no = f"HP-{r.randint(118000, 121400)}" if r.random() < 0.38 else ""
                called = r.choices(["כן", "לא", ""], weights=[0.18, 0.5, 0.32], k=1)[0]
                note = r.choice(["", "", "", "", "", "לקוח עצבני", "שלח תמונות", "העברתי לרינה", "חוזר שוב", "ביקש מנהל"])
                rows.append([d.strftime(r.choice(["%d/%m", "%d/%m/%Y", "%d.%m"])), agent.name, hour, lang, topic,
                             order_no, minutes, called, note])
    return rows


# =============================================================================================
# 10. IT: SaaS list, proxy log, browser extensions, expenses
# =============================================================================================
def pseudonym(email: str) -> str:
    return "u_" + hashlib.sha256(f"hp-proxy-salt:{email}".encode()).hexdigest()[:8]


SAAS = [
    # name, vendor, category, owner, users, plan, annual ILS, renewal, SSO, data, AI features, AI enabled, DPA, notes
    ("Priority ERP", "Priority Software (via local integrator)", "ERP", "Ronit Avraham", 64, "Cloud Pro", 312000, "2027-12-31", "N", "customers, orders, stock, suppliers, finance", "", "N/A", "Y", ""),
    ("SmartStock AI (ERP add-on)", "Optimo Systems Ltd", "Inventory replenishment", "Eyal Navon", 6, "Module", 38000, "2027-03-31", "N", "stock levels, purchase orders", "AI-powered smart reorder suggestions", "Yes", "N", "Bought 2024 as 'AI'. See it/smartstock-reorder-config.md"),
    ("AutoRecon (accounting add-on)", "Optimo Systems Ltd", "Bank reconciliation", "Natalia Gurevich", 4, "Module", 14000, "2027-03-31", "N", "bank transactions", "Intelligent auto-match", "Yes", "N", ""),
    ("Deskly", "Deskly Inc.", "Helpdesk (email, web form)", "Samir Haddad", 15, "Growth", 61000, "2027-01-31", "Y", "customer names, emails, phones, addresses, order details", "Deskly AI Assist add-on (triage, drafts) available, not purchased", "No", "Y", "AI add-on terms received Oct 2026"),
    ("CloudVoice PBX", "CloudVoice Ltd", "Phone system", "Samir Haddad", 18, "Contact center", 48000, "2026-12-31", "N", "caller numbers, call recordings (30 days)", "Call transcription & summary", "No", "Y", ""),
    ("StoreHub", "StoreHub Commerce", "Web store", "Noa Levi", 7, "Advanced", 54000, "2027-06-30", "N", "customers, orders, payments (tokenised)", "AI product descriptions", "Yes", "Y", "Lead-time table set by marketing"),
    ("Google Workspace", "Google", "Email, docs, drive", "Avi Mizrahi", 92, "Business Standard", 101000, "2027-02-28", "Y", "everything", "Gemini features", "Unknown", "Y", "Admin console not reviewed since 2024"),
    ("PeopleWise", "PeopleWise HR Ltd", "HR, payroll, recruiting", "Dana Katz", 5, "Business", 46000, "2027-08-31", "N", "employee and candidate personal data, salaries", "", "No", "Y", ""),
    ("MailPost", "MailPost", "Email marketing", "Noa Levi", 3, "Pro", 21000, "2027-01-31", "N", "customer emails, purchase history", "AI subject lines, send-time optimisation", "Yes", "Y", ""),
    ("Canva", "Canva", "Design", "Noa Levi", 4, "Teams", 6200, "2027-05-31", "N", "marketing images", "Magic Write / AI image tools", "Yes", "N", ""),
    ("Zoom", "Zoom", "Video meetings", "Avi Mizrahi", 25, "Business", 9800, "2027-04-30", "N", "meeting content", "AI Companion (meeting summaries)", "Unknown", "N", ""),
    ("Monday.com", "monday.com", "Projects (marketing, B2B)", "Yaniv Carmi", 12, "Standard", 13000, "2026-12-31", "N", "B2B leads, contacts", "AI assistant", "Unknown", "N", ""),
    ("RouteMaster", "RouteMaster Ltd", "Delivery route planning", "Tamar Shalev", 4, "Fleet", 26000, "2027-02-28", "N", "customer addresses, phone numbers", "Route optimisation", "N/A", "Y", "Algorithmic optimisation, not ML (per vendor)"),
    ("Gal-Ship Portal", "Gal-Ship Forwarding Ltd", "Freight forwarder portal", "Tamar Shalev", 4, "Free with service", 0, "", "N", "shipments, containers", "", "N/A", "N", "Export to CSV weekly; ETA changes also come by email"),
    ("SignNow IL", "SignNow IL", "E-signature", "Ronit Avraham", 6, "Business", 4800, "2027-09-30", "N", "contracts", "", "No", "Y", ""),
    ("Bitdefender GravityZone", "Bitdefender", "Endpoint security", "Avi Mizrahi", 88, "Business", 17500, "2027-01-31", "N", "device telemetry", "ML-based threat detection", "Yes", "Y", "Managed by MSP"),
    ("NetGuard Web Proxy", "NetGuard", "Web proxy / filtering", "Avi Mizrahi", 88, "Cloud", 12000, "2027-01-31", "N", "browsing logs", "URL categorisation", "Yes", "Y", "Logs kept 90 days"),
    ("Kaltura-like LMS (LearnBox)", "LearnBox", "Training", "Dana Katz", 120, "Basic", 8000, "2027-03-31", "N", "training records", "", "No", "N", "Barely used"),
    ("Hilan-style attendance (ClockIn)", "ClockIn", "Attendance", "Dana Katz", 120, "Standard", 15000, "2027-12-31", "N", "attendance", "", "No", "Y", ""),
    ("Waze for Business", "Google", "Driver navigation", "Tamar Shalev", 8, "Free", 0, "", "N", "locations", "", "N/A", "N", ""),
]


def build_proxy(staff: list[Person]) -> list[list]:
    r = rng_for("proxy")
    users = [p for p in staff if p.has_pc]
    work_domains = {
        "*": [("mail.google.com", "Webmail", 18), ("docs.google.com", "Business", 10), ("drive.google.com", "Business", 6),
              ("www.google.com", "Search Engines", 12), ("harborpine.priority-cloud.co.il", "Business", 8),
              ("www.ynet.co.il", "News", 4), ("www.facebook.com", "Social Networking", 3), ("web.whatsapp.com", "Instant Messaging", 6),
              ("www.youtube.com", "Streaming Media", 3), ("www.linkedin.com", "Social Networking", 2), ("translate.google.com", "Translation", 2)],
        "Customer Service": [("harborpine.deskly.com", "Business", 30), ("app.cloudvoice.co.il", "Business", 6),
                             ("harborpine.storehub.app", "Business", 6), ("www.deepl.com", "Translation", 2)],
        "Logistics & Warehouse": [("portal.galship.co.il", "Business", 14), ("www.routemaster.co.il", "Business", 8),
                                  ("www.gov.il", "Government", 3)],
        "Marketing & E-commerce": [("harborpine.storehub.app", "Business", 14), ("www.canva.com", "Business", 8),
                                   ("app.mailpost.io", "Business", 6), ("business.facebook.com", "Social Networking", 6),
                                   ("ads.google.com", "Business", 5)],
        "Finance": [("www.bankhapoalim.co.il", "Financial Services", 4), ("www.leumi.co.il", "Financial Services", 4),
                    ("www.misim.gov.il", "Government", 3)],
        "HR": [("harborpine.peoplewise.com", "Business", 14), ("www.alljobs.co.il", "Job Search", 4),
               ("match-ai.peoplewise.io", "Business", 3)],
        "Purchasing": [("www.alibaba.com", "Shopping", 6), ("portal.galship.co.il", "Business", 4)],
        "B2B Sales": [("harborpine.monday.com", "Business", 10)],
    }
    # Who uses which AI or translation tool, and how often per day (mean). Matches expenses and extensions.
    ai_use = {
        "Olga Petrenko": [("chatgpt.com", "Generative AI", 7, (2500, 14000)), ("api.linguaflow.ai", "Uncategorized", 5, (300, 2500))],
        "Yana Kogan": [("chatgpt.com", "Generative AI", 4, (1500, 9000)), ("api.linguaflow.ai", "Uncategorized", 4, (300, 2500))],
        "Lina Khoury": [("chatgpt.com", "Generative AI", 3, (1500, 9000)), ("api.linguaflow.ai", "Uncategorized", 3, (300, 2500))],
        "Rami Nasser": [("chat.openai.com", "Generative AI", 1, (1000, 6000)), ("api.linguaflow.ai", "Uncategorized", 2, (300, 2500))],
        "Daniel Shaw": [("gemini.google.com", "Generative AI", 1.2, (800, 5000)), ("capi.grammarly.com", "Business", 6, (200, 1500))],
        "Sergei Novikov": [("www.deepl.com", "Translation", 3, (500, 4000)), ("api.linguaflow.ai", "Uncategorized", 2, (300, 2500))],
        "Ahmad Jabareen": [("api.linguaflow.ai", "Uncategorized", 2, (300, 2500))],
        "Noa Levi": [("app.copygenie.io", "Uncategorized", 3, (800, 6000)), ("chatgpt.com", "Generative AI", 1, (500, 3000)),
                     ("capi.grammarly.com", "Business", 4, (200, 1500))],
        "Shir Barak": [("chatgpt.com", "Generative AI", 4, (800, 7000)), ("app.copygenie.io", "Uncategorized", 2, (800, 6000)),
                       ("capi.grammarly.com", "Business", 5, (200, 1500))],
        "Igor Volkov": [("chatgpt.com", "Generative AI", 2, (600, 5000)), ("www.deepl.com", "Translation", 1, (500, 3000)),
                        ("api.linguaflow.ai", "Uncategorized", 1, (300, 2500))],
        "Natalia Gurevich": [("claude.ai", "Generative AI", 0.25, (2000, 20000))],
        "Yaniv Carmi": [("capi.grammarly.com", "Business", 3, (200, 1500)), ("gemini.google.com", "Generative AI", 0.4, (500, 3000))],
    }
    extra_linguaflow = [p for p in users if p.team.startswith("Sales – Showroom")][:2] + \
                       [p for p in users if p.role == "Import Coordinator"][:1]
    rows = []
    for d in days(date(2026, 10, 11), date(2026, 10, 22)):
        if d.weekday() not in ISRAELI_WORKDAYS:
            continue
        for p in users:
            dept = p.team if not p.team.startswith("Sales – Showroom") else "Showroom Sales"
            pool = work_domains["*"] + work_domains.get(p.team, [])
            entries = []
            for _ in range(poisson(r, 2.6)):
                dom, cat, _ = r.choices(pool, [w for _, _, w in pool])[0]
                entries.append((dom, cat, r.randint(300, 4000)))
            plan = list(ai_use.get(p.name, []))
            if p in extra_linguaflow:
                plan.append(("api.linguaflow.ai", "Uncategorized", 1.5, (300, 2500)))
            for dom, cat, mean, (lo, hi) in plan:
                for _ in range(poisson(r, mean)):
                    entries.append((dom, cat, r.randint(lo, hi)))
            for dom, cat, bytes_out in entries:
                t = random_moment(r, d, [0] * 8 + [4, 6, 6, 6, 4, 6, 6, 5, 4, 2, 1, 1, 0, 0, 0, 0])
                rows.append([iso(t), pseudonym(p.email), dept, f"10.20.{r.randint(1, 4)}.{r.randint(10, 250)}", dom, cat,
                             r.choice(["GET", "POST"]) if cat != "Generative AI" else "POST", 200, bytes_out,
                             r.randint(2000, 180000), "allowed"])
    rows.sort(key=lambda x: (x[0], x[1]))
    return rows


def build_extensions(staff: list[Person]) -> list[list]:
    r = rng_for("extensions")
    users = [p for p in staff if p.has_pc]
    rows = []
    linguaflow = ["Olga Petrenko", "Yana Kogan", "Lina Khoury", "Rami Nasser", "Sergei Novikov", "Ahmad Jabareen",
                  "Igor Volkov"] + [p.name for p in users if p.team.startswith("Sales – Showroom")][:1] + \
                 [p.name for p in users if p.role == "Import Coordinator"][:1]
    grammarly = ["Daniel Shaw", "Noa Levi", "Shir Barak", "Yaniv Carmi", "Michal Peretz", "Hila Dahan"]
    sidebar = ["Shir Barak", "Igor Volkov"]
    for i, p in enumerate(users):
        device = f"HP-{'LT' if r.random() < 0.6 else 'PC'}-{i + 101:03d}"
        exts = [("Google Docs Offline", "ghbmnnjooekpmoecnnnilnnbdlolhkhi", "1.88.1", "Force-installed (policy)", "Storage")]
        if p.team == "Customer Service":
            exts.append(("Deskly Agent Toolbar", "pdkdmblkcfmnhhdagfjjjpljmlmcolbh", "4.2.0", "Force-installed (policy)",
                         "Read and change data on harborpine.deskly.com"))
        if p.name in linguaflow:
            exts.append(("LinguaFlow – AI Translate & Rewrite", "lgfnnkpcmoapejcbkoahjhebbcbjmhgk", "3.7.2", "Chrome Web Store",
                         "Read and change all your data on all websites; clipboard"))
        if p.name in grammarly:
            exts.append(("Grammarly: AI Writing Assistant", "kbfnbcaeplbcioakkpcpgfkobkghlhen", "14.1189.0", "Chrome Web Store",
                         "Read and change all your data on all websites"))
        if p.name in sidebar:
            exts.append(("ChatGPT Sidebar – AI Assistant for Any Page", "difoiogjjojoaoomphldepapgpbgkhkb", "6.2.4",
                         "Chrome Web Store", "Read and change all your data on all websites; tabs; clipboard"))
        if r.random() < 0.35:
            exts.append(("uBlock Origin", "cjpalhdlnbpafiamejdnhcphjbkeiagm", "1.60.0", "Chrome Web Store", "Read and change all your data on all websites"))
        if r.random() < 0.25:
            exts.append(("Zoom Scheduler", "kgjfgplpablkjnlkjmjdecgdpfankdle", "2.1.6", "Chrome Web Store", "Calendar"))
        if r.random() < 0.15:
            exts.append(("Google Translate", "aapbdbdomjkkjkaonfhkkikfgjllcleb", "2.0.16", "Chrome Web Store", "Read data on all websites"))
        for name, ext_id, ver, source, perms in exts:
            installed = date(2026, r.randint(1, 10), r.randint(1, 28))
            if "LinguaFlow" in name:
                installed = date(2026, r.randint(3, 9), r.randint(1, 28))
            rows.append([device, p.email, p.team, "Windows 11" if r.random() < 0.9 else "macOS 15", name, ext_id, ver,
                         installed.isoformat(), source, perms, "2026-10-28"])
    return rows


def build_expenses(staff: list[Person]) -> list[list]:
    r = rng_for("expenses")
    rows, seq = [], 5200
    usd = 3.70   # rate the finance team uses for reimbursements in 2026
    monthly_ai = [  # name, merchant, description, USD, first month, card
        ("Noa Levi", "COPYGENIE.IO", "CopyGenie Pro - monthly", 39.0, 2, "Personal card - reimbursement"),
        ("Shir Barak", "OPENAI *CHATGPT SUBSCR", "ChatGPT Plus", 20.0, 4, "Personal card - reimbursement"),
        ("Igor Volkov", "OPENAI *CHATGPT SUBSCR", "chatgpt plus", 20.0, 6, "Personal card - reimbursement"),
    ]
    other_merchants = [
        ("GETT TAXI", "Taxi to client meeting", (45, 180), "Travel"), ("PANGO", "Parking", (12, 60), "Travel"),
        ("RAV-KAV", "Train", (15, 40), "Travel"), ("AROMA ESPRESSO BAR", "Meeting coffee", (30, 120), "Meals"),
        ("WOLT", "Team lunch", (90, 450), "Meals"), ("OFFICE DEPOT IL", "Office supplies", (40, 350), "Office"),
        ("ALIEXPRESS", "Samples", (60, 400), "Purchasing"), ("LINKEDIN PREMIUM", "LinkedIn Premium", (110, 110), "Software"),
        ("HOTEL HAIFA", "Overnight - Haifa showroom", (450, 700), "Travel"), ("DELEK", "Fuel", (150, 400), "Travel"),
        ("SHUTTERSTOCK", "Stock photos", (110, 300), "Marketing"), ("ZOOM.US", "Zoom Pro (personal)", (60, 60), "Software"),
    ]
    spenders = [p for p in staff if p.has_pc and p.team not in ("Logistics & Warehouse",)] + \
               [p for p in staff if p.role in ("Import Coordinator", "Logistics Manager")]
    for m in range(1, 11):
        for name, merchant, desc, amount, first_month, card in monthly_ai:
            if m >= first_month:
                p = person(staff, name)
                dt = date(2026, m, min(28, 3 + first_month))
                seq += 1
                rows.append([f"EXP-{seq}", p.emp_id, p.name, p.team, dt.isoformat(), merchant, desc, f"{amount:.2f}", "USD",
                             f"{amount * usd:.2f}", card, "Software" if r.random() < 0.7 else "Marketing tools",
                             p.manager_id and next(x.name for x in staff if x.emp_id == p.manager_id)])
        for _ in range(poisson(r, 30)):
            p = r.choice(spenders)
            merchant, desc, (lo, hi), cat = r.choice(other_merchants)
            amount = round(r.uniform(lo, hi), 2)
            dt = date(2026, m, r.randint(1, 28))
            seq += 1
            card = "Corporate card" if p.band.startswith(("₪28", "₪35", "₪45", "₪60")) and r.random() < 0.7 else "Personal card - reimbursement"
            rows.append([f"EXP-{seq}", p.emp_id, p.name, p.team, dt.isoformat(), merchant, desc, f"{amount:.2f}", "ILS",
                         f"{amount:.2f}", card, cat, p.manager_id and next(x.name for x in staff if x.emp_id == p.manager_id)])
    # One-off AI purchases
    for name, d, merchant, desc, amount in (("Shir Barak", date(2026, 5, 17), "MIDJOURNEY INC.", "image gen - campaign", 30.0),
                                            ("Natalia Gurevich", date(2026, 8, 9), "ANTHROPIC", "Claude Pro (1 month)", 20.0)):
        p = person(staff, name)
        seq += 1
        rows.append([f"EXP-{seq}", p.emp_id, p.name, p.team, d.isoformat(), merchant, desc, f"{amount:.2f}", "USD",
                     f"{amount * usd:.2f}", "Personal card - reimbursement", "Software",
                     next(x.name for x in staff if x.emp_id == p.manager_id)])
    rows.sort(key=lambda x: (x[4], x[0]))
    return rows


# =============================================================================================
# 11. Pilot usage export (8 weeks from 1 February 2027) and the HR roster to join it with
# =============================================================================================
PILOT_START = date(2027, 2, 1)


def build_usage(staff: list[Person]) -> tuple[list[list], list[list]]:
    r = rng_for("usage")
    cs = [p for p in staff if p.team == "Customer Service"]
    profiles = {  # daily mean of (drafts generated, drafts inserted, triage accepted, translate)
        "Olga Petrenko": "power", "Yana Kogan": "steady", "Lina Khoury": "steady", "Rami Nasser": "steady",
        "Daniel Shaw": "light", "Shani Ohayon": "steady", "Tigist Mekonen": "grower", "Adi Golan": "steady",
        "Sergei Novikov": "quitter", "Moran Biton": "quitter", "Ahmad Jabareen": "quitter",
        "Hila Dahan": "leave", "Rina Azoulay": "translate_only", "Samir Haddad": "manager",
    }
    leave_from = date(2027, 2, 21)      # Hila Dahan starts maternity leave
    resign_on = date(2027, 3, 4)        # Adi Golan's last day
    rows = []
    for d in days(PILOT_START, PILOT_START + timedelta(days=55)):
        if d.weekday() not in ISRAELI_WORKDAYS:
            continue
        week = (d - PILOT_START).days // 7 + 1
        for p in cs:
            prof = profiles[p.name]
            if prof == "leave" and d >= leave_from:
                continue
            if p.name == "Adi Golan" and d > resign_on:
                continue
            if r.random() < 0.06:
                continue   # sick day / day off
            ramp = min(1.0, 0.5 + 0.2 * week)
            opened = poisson(r, 24 if prof not in ("manager", "translate_only") else 6)
            gen = ins = tri = tr = 0
            if prof == "power":
                gen, ins, tri, tr = poisson(r, 22 * ramp), 0, poisson(r, 18), poisson(r, 9)
                ins = sum(1 for _ in range(gen) if r.random() < 0.85)
            elif prof in ("steady", "leave"):
                gen, tri, tr = poisson(r, 11 * ramp), poisson(r, 10), poisson(r, 3)
                ins = sum(1 for _ in range(gen) if r.random() < 0.7)
            elif prof == "grower":
                gen, tri = poisson(r, 2 + 1.6 * week), poisson(r, 4 + week)
                ins = sum(1 for _ in range(gen) if r.random() < 0.65)
            elif prof == "light":
                gen, tri = poisson(r, 3), poisson(r, 5)
                ins = sum(1 for _ in range(gen) if r.random() < 0.5)
            elif prof == "quitter":
                # Quiet non-adoption: real use in weeks 1-3, then only the panel that opens by itself.
                if week <= 3:
                    gen, tri = poisson(r, 9), poisson(r, 8)
                    ins = sum(1 for _ in range(gen) if r.random() < 0.6)
                elif week == 4:
                    gen, tri = poisson(r, 2), poisson(r, 2)
                    ins = sum(1 for _ in range(gen) if r.random() < 0.4)
                else:
                    gen = 1 if r.random() < 0.1 else 0
            elif prof == "translate_only":
                tr = poisson(r, 6)
            elif prof == "manager":
                gen = 1 if r.random() < 0.3 else 0
            for feature, n in (("panel_opened", opened), ("triage_suggestion_accepted", tri), ("draft_generated", gen),
                               ("draft_inserted", ins), ("translate_inbound", tr)):
                if n:
                    rows.append([d.isoformat(), p.email, feature, n])
        # Two marketing licences assigned "to try it" and never used beyond one login.
        if d == PILOT_START + timedelta(days=1):
            for name in ("Noa Levi", "Shir Barak"):
                rows.append([d.isoformat(), person(staff, name).email, "panel_opened", 1])
    roster = []
    licensed = [p for p in cs] + [person(staff, "Noa Levi"), person(staff, "Shir Barak")]
    for p in licensed:
        status, since = "active", ""
        if p.name == "Hila Dahan":
            status, since = "maternity leave", leave_from.isoformat()
        if p.name == "Adi Golan":
            status, since = "resigned", (resign_on + timedelta(days=1)).isoformat()
        wave = "" if p.team != "Customer Service" else "wave 1"
        mgr = next((x.name for x in staff if x.emp_id == p.manager_id), "")
        roster.append([p.emp_id, p.email, p.name, p.team, p.role, mgr, p.site, f"{p.fte:.1f}", status, since,
                       wave, "Y"])
    return rows, roster


# =============================================================================================
# 12. Generated documents
# =============================================================================================
def org_chart_md(staff: list[Person]) -> str:
    lines = ["# Harbor & Pine — organisation chart", "",
             "Exported from PeopleWise on 26 October 2026 (active employees). Reporting lines as recorded in HR; ",
             "the showroom managers report to the CEO for sales and to the COO for operations.", ""]
    by_id = {p.emp_id: p for p in staff}
    teams: dict[str, list[Person]] = {}
    for p in staff:
        teams.setdefault(p.team, []).append(p)
    lines += [f"Headcount: **{len(staff)}** ({sum(p.fte for p in staff):.1f} FTE).", "",
              "| Team | People | Head | Reports to |", "|---|---|---|---|"]
    order = ["Management", "Finance", "Customer Service", "Logistics & Warehouse", "Purchasing", "Merchandising",
             "Sales – Showroom Tel Aviv", "Sales – Showroom Haifa", "B2B Sales", "Marketing & E-commerce", "HR", "IT",
             "Facilities"]
    heads = {"Management": "Yoav Ben-Ami", "Finance": "Ronit Avraham", "Customer Service": "Samir Haddad",
             "Logistics & Warehouse": "Tamar Shalev", "Purchasing": "Eyal Navon", "B2B Sales": "Yaniv Carmi",
             "Marketing & E-commerce": "Noa Levi", "HR": "Dana Katz", "IT": "Avi Mizrahi"}
    for team in order:
        members = teams[team]
        head = heads.get(team) or next(p.name for p in members if p.role.startswith(("Showroom Manager", "Head of", "Office")))
        hp = person(staff, head)
        boss = by_id[hp.manager_id].name if hp.manager_id else "Board"
        lines.append(f"| {team} | {len(members)} | {head} | {boss} |")
    lines.append("")
    for team in order:
        lines += [f"## {team}", "", "| ID | Name | Role | Site | Manager | Since |", "|---|---|---|---|---|---|"]
        for p in sorted(teams[team], key=lambda x: (x.manager_id != "" and by_id.get(x.manager_id, x).team == team, x.role, x.last)):
            mgr = by_id[p.manager_id].name if p.manager_id else "—"
            part = " (50%)" if p.fte < 1 else ""
            lines.append(f"| {p.emp_id} | {p.name} | {p.role}{part} | {p.site} | {mgr} | {p.start:%Y-%m} |")
        lines.append("")
    return "\n".join(lines)


def kpi_numbers(tickets: list[Ticket], calls: list[list]) -> dict:
    q3 = [t for t in tickets if datetime(2026, 7, 1) <= t.created < datetime(2026, 10, 1)]
    email = [t for t in q3 if t.channel == "email" and t.created.weekday() in ISRAELI_WORKDAYS and t.first_response]
    frt = statistics.mean(working_hours(t.created, t.first_response) for t in email)
    non_spam = [t for t in q3 if t.cat != "spam" and not t.merged]
    resolved = sum(1 for t in non_spam if t.status == "resolved")
    csat = [t.csat for t in q3 if t.csat]
    q3_calls = [c for c in calls if "2026-07-01" <= c[1][:10] <= "2026-09-30"]
    in_hours = [c for c in q3_calls if c[6] != "after_hours"]
    answered = [c for c in in_hours if c[6] == "answered"]
    return {
        "tickets": len(q3), "email_tickets": sum(1 for t in q3 if t.channel == "email"), "frt": frt,
        "frt_n": len(email), "resolution": 100 * resolved / len(non_spam),
        "csat": 100 * csat.count("good") / len(csat), "calls": len(in_hours),
        "answered_pct": 100 * len(answered) / len(in_hours),
        "avg_wait": statistics.mean(c[7] for c in answered),
    }


def kpi_report_md(k: dict) -> str:
    def ok(met: bool) -> str:
        return "✅" if met else "⚠️"

    return f"""# Customer Service — Quarterly KPI Report, Q3 2026

Prepared by: Customer Service (Samir Haddad) with Finance BI · Distribution: CEO, COO, CFO · 6 October 2026

## Headline

Customer Service met its first-response target for the third quarter in a row.

| KPI | Q3 2026 | Target | Status |
|---|---|---|---|
| Average first response time¹ | **{k['frt']:.1f} hours** | ≤ 2 hours | {ok(k['frt'] <= 2.05)} |
| Tickets handled (email + web form) | {k['tickets']:,} | — | ↑ vs Q2 |
| Resolution rate² | {k['resolution']:.1f}% | ≥ 90% | {ok(k['resolution'] >= 90)} |
| Customer satisfaction (CSAT)³ | {k['csat']:.0f}% | ≥ 80% | {ok(k['csat'] >= 80)} |
| Calls offered (phone, opening hours) | {k['calls']:,} | — | ↑ vs Q2 |
| Calls answered | {k['answered_pct']:.0f}% | ≥ 85% | {ok(k['answered_pct'] >= 84.5)} |
| Average speed of answer (phone) | {k['avg_wait'] / 60:.1f} min | ≤ 2 min | {ok(k['avg_wait'] <= 120)} |

## Comments

- Volume rose in August and September with the holiday season and supplier delays. The team absorbed the
  increase without overtime beyond the usual peak-season budget.
- CSAT is below target. Most negative ratings come from customers unhappy about delivery dates, which are
  outside Customer Service's control.
- First response stayed at about **2 hours** thanks to the saved replies (macros) introduced in 2025.
- Recommendation: keep the current staffing for Q4; review again before the November–January peak.

---

¹ First response time: business hours (Sunday–Thursday, 08:00–17:00) between ticket creation and the first
agent reply, for tickets received by email on business days (n = {k['frt_n']:,}). Average.
² Resolution rate: tickets in status "resolved" ÷ tickets received, excluding spam and merged tickets.
³ CSAT: share of "good" ratings among customers who answered the one-question survey sent on resolution.
"""


def memo_numbers(tickets: list[Ticket]) -> dict:
    total = len(tickets)
    status = sum(1 for t in tickets if t.category == "Delivery status")
    langs: dict[str, int] = {}
    for t in tickets:
        langs[t.detected_lang or "unknown"] = langs.get(t.detected_lang or "unknown", 0) + 1
    other = sum(1 for t in tickets if t.category == "Other/כללי")
    return {"total": total, "wismo_pct": 100 * status / total, "he": 100 * langs.get("he", 0) / total,
            "ru": 100 * langs.get("ru", 0) / total, "ar": 100 * langs.get("ar", 0) / total,
            "en": 100 * langs.get("en", 0) / total, "other_pct": 100 * other / total}


def memo_md(m: dict, k: dict) -> str:
    return f"""# Findings memo — Customer Service AI opportunity (DRAFT v0.3)

*Drafted with an AI assistant from the helpdesk export and the Q3 KPI report. For internal review.*

To: Yoav Ben-Ami (CEO), Michal Peretz (COO) · From: Operations · Date: 19 October 2026

## Summary

Harbor & Pine's customer service is efficient but expensive. The team answers customers quickly (median first
response of 2 hours) and resolves {k['resolution']:.0f}% of tickets. The main opportunity is to automate repetitive
questions with an AI chatbot, which industry research shows can handle the majority of retail enquiries. We
recommend launching a chatbot in Q1 2027.

## Findings

1. **Volume.** The helpdesk received {m['total']:,} tickets between May and October 2026, plus phone calls.
2. **"Where is my order" is a minority of contacts.** Only {m['wismo_pct']:.0f}% of tickets are delivery-status
   questions (category "Delivery status"). Most tickets are spread across many smaller categories, which is
   typical for furniture retail.
3. **Response time is already good.** The median first response time is 2 hours, meeting the target, so speed is
   not the problem — cost is.
4. **Languages.** {m['he']:.0f}% of tickets are in Hebrew, {m['ru']:.0f}% Russian, {m['ar']:.0f}% Arabic and
   {m['en']:.0f}% English, based on the helpdesk's language field.
5. **Industry benchmark.** According to a Gartner 2025 study of 400 retailers, AI chatbots fully resolve 65–70% of
   customer service enquiries without human involvement, reducing service cost by up to 45%.
6. **Data quality is adequate.** Every ticket has a category; {m['other_pct']:.0f}% are "Other", which a chatbot
   can classify automatically.

## Recommendation

- Select a chatbot vendor (ChatNest has already given a demo built on our catalogue).
- Go live in Q1 2027 on the website and WhatsApp, in Hebrew first.
- Target: 40% support cost reduction within 12 months, in line with the CEO's commitment to the board.

## Sources

Helpdesk export (tickets.csv, May–October 2026); Customer Service KPI report Q3 2026; Gartner (2025),
*AI in Retail Customer Service*.
"""


def eta_sheet(shipments: list[dict]) -> list[list]:
    """Tamar's hand-kept tracking sheet: Hebrew headers, mixed date formats, notes, gaps."""
    r = rng_for("eta-sheet")
    header = ["מס' מכולה", "ספק", "ארץ", "נמל", "ETA מקורי", "ETA עדכני", "עודכן בתאריך", "הגיע?", "הערות", "סטטוס"]
    rows = [header]
    month_he = {4: "אפריל", 5: "מאי", 6: "יוני", 7: "יולי", 8: "אוגוסט", 9: "ספטמבר", 10: "אוקטובר", 11: "נובמבר", 12: "דצמבר"}
    current = None
    country_he = {"VN": "וייטנאם", "CN": "סין", "TR": "טורקיה", "IT": "איטליה"}

    def fmt(d: date) -> str:
        style = r.random()
        if style < 0.6:
            return d.strftime("%d/%m/%y")
        if style < 0.85:
            return f"{d.day}.{d.month}"
        return d.isoformat()

    export_day = EXPORT_AT.date()
    for s in shipments:
        if s["eta"] < date(2026, 4, 20) or s["etd"] > export_day + timedelta(days=10):
            continue
        if s["eta"].month != current:
            current = s["eta"].month
            rows.append([f"--- {month_he[current]} ---"] + [""] * 9)
        if r.random() < 0.04:
            continue   # never entered
        known = [(a, n) for a, n in s["revisions"] if a <= export_day]
        latest = known[-1] if known else None
        arrived = s["actual"] <= export_day
        status = "התקבל במחסן" if s["warehouse"] <= export_day else ("במכס" if arrived else ("בים" if s["etd"] <= export_day else "הוזמן"))
        rows.append([
            s["container"] if r.random() > 0.03 else s["container"][:4] + " " + s["container"][4:],
            s["supplier"].split()[0], country_he[s["country"]], s["dest_port"], fmt(s["eta"]),
            fmt(latest[1]) if latest else "", fmt(latest[0]) if latest and r.random() < 0.8 else "",
            ("כן " + fmt(s["actual"])) if arrived else "", s["note"] if known else "", status,
        ])
        if r.random() < 0.03:
            rows.append(rows[-1][:])   # copied twice by mistake
    delayed = sum(1 for s in shipments if s["delay"] >= 7 and s["eta"] <= export_day)
    rows.append([""] * 10)
    rows.append([f"סה\"כ מכולות עם עיכוב של שבוע ומעלה (מאז אפריל): {delayed}"] + [""] * 9)
    rows.append(["לא לשנות את הקובץ בלי לדבר איתי - תמר"] + [""] * 9)
    return rows


# =============================================================================================
# 13. Main: build everything and write the files
# =============================================================================================
def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--answer-key", metavar="DIR", help="also write the ground truth to DIR (course writers only)")
    args = parser.parse_args()

    staff = build_staff()
    products = build_products()
    PRODUCTS_BY_SEED.extend(p for p in products if p["discontinued"] is None)
    shipments = build_shipments()
    orders, customers = build_orders(products, shipments)
    tickets = build_tickets(orders, customers, staff)
    claims, claims_truth = build_claims(tickets)   # adds claim numbers and tags to tickets
    emails, emails_truth = build_emails(tickets, staff)
    calls = build_calls(staff)

    # ---- company/
    write_text("company/org-chart.md", org_chart_md(staff))
    k = kpi_numbers(tickets, calls)
    write_text("company/kpi-report-2026-q3.md", kpi_report_md(k))
    write_csv("company/finance-summary.csv", ["line", "fy2024_ils", "fy2025_ils", "h1_2026_ils", "note"], FINANCE_ROWS)

    # ---- support/
    write_csv("support/tickets.csv",
              ["ticket_id", "created_at", "channel", "requester_id", "order_id", "language", "category", "subject",
               "priority", "status", "first_response_at", "resolved_at", "agent", "tags", "time_spent_min", "csat"],
              [[t.tid, iso(t.created), t.channel, t.customer.cid, t.order_ref, t.detected_lang, t.category, t.subject,
                t.priority, t.status, iso(t.first_response), iso(t.resolved), t.agent, " ".join(t.tags), t.work_min, t.csat]
               for t in tickets])
    write_csv("support/whatsapp-week-tally.csv",
              ["date", "agent", "time", "customer_language", "topic", "order_no", "minutes", "also_called", "note"],
              build_whatsapp_tally(staff))
    write_csv("support/emails.csv",
              ["email_id", "ticket_id", "received_at", "from_name", "from_address", "to_address", "subject", "body",
               "attachments", "reply_sent_at", "reply_agent", "reply_body"], emails)
    write_csv("support/phone-log.csv",
              ["call_id", "started_at", "caller", "ivr_language", "ivr_option", "queue", "result", "wait_seconds",
               "talk_seconds", "agent_ext", "agent_name"], calls)

    # ---- orders/
    write_csv("orders/orders.csv",
              ["order_id", "order_created_at", "sales_channel", "customer_id", "customer_type", "ship_to_city", "sku",
               "item_description", "supplier_country", "qty", "order_total_ils", "promised_delivery_date",
               "container_no", "delivery_status", "actual_delivery_date"],
              [order_row(o) for o in orders])
    write_csv("orders/shipments.csv",
              ["shipment_ref", "container_no", "supplier", "origin_country", "origin_port", "dest_port", "carrier",
               "vessel", "voyage", "etd_date", "eta_original_date", "eta_rev1_date", "eta_rev2_date", "eta_latest_date",
               "arrival_date", "customs_release_date", "warehouse_in_date", "status"],
              [shipment_row(s) for s in shipments if s["etd"] <= EXPORT_AT.date() + timedelta(days=21)])
    sheet = eta_sheet(shipments)
    write_csv("orders/logistics-eta-tracking.csv", sheet[0], sheet[1:])
    write_csv("orders/storehub-delivery-settings.csv",
              ["setting", "supplier_country", "value_days", "applies_to", "last_modified_at", "modified_by"],
              [["promised_delivery_lead_time", COUNTRIES[c], LEAD_DAYS[c], "all SKUs from this country",
                "2023-02-14 11:02:37+02:00", "noa.levi"] for c in COUNTRIES] +
              [["in_stock_lead_time", "(warehouse stock)", 7, "SKUs flagged in stock", "2023-02-14 11:03:10+02:00", "noa.levi"]])

    # ---- catalog/
    write_csv("catalog/products.csv",
              ["sku", "name_en", "name_he", "collection", "color", "supplier", "supplier_country", "list_price_ils",
               "assembly_required", "weight_kg", "launched", "status", "discontinued_on"],
              [[p["sku"], p["name_en"], p["name_he"], p["collection"], p["color"], p["supplier"], COUNTRIES[p["country"]],
                p["price"], p["assembly"], p["weight"], p["launched"].isoformat(),
                "discontinued" if p["discontinued"] else "active", p["discontinued"].isoformat() if p["discontinued"] else ""]
               for p in products])
    old = [p for p in products if p["launched"] < date(2023, 4, 1)]
    write_csv("catalog/products-2023-shared-drive-copy.csv",
              ["מק\"ט", "שם מוצר", "Product name", "ספק", "מחיר לצרכן", "מחיר B2B", "הרכבה", "הערות"],
              [[p["sku"], p["name_he"], p["name_en"], p["supplier"], p["price_2023"], round(p["price_2023"] * 0.82),
                "כן" if p["assembly"] == "Y" else "לא", "" if i % 17 else "מבצע קיץ"] for i, p in enumerate(old)])

    # ---- claims/
    write_csv("claims/damage-claims-log.csv",
              ["מס' תביעה", "תאריך פתיחה", "טיקט", "הזמנה", "שם לקוח", "טלפון", "מק\"ט", "פריט", "סוג נזק", "תמונות",
               "ספק", "מכולה", "סכום תביעה", "החלטה", "תאריך החלטה", "פיצוי", "חיוב ספק", "הערות"], claims)

    # ---- people/
    write_csv("people/headcount.csv",
              ["employee_id", "full_name", "role", "team", "site", "manager_id", "start_date", "fte",
               "loaded_monthly_cost_band"],
              [[p.emp_id, p.name, p.role, p.team, p.site, p.manager_id, p.start.isoformat(), f"{p.fte:.1f}", p.band]
               for p in staff])
    write_csv("people/timesheets.csv",
              ["week_start_date", "employee_id", "employee_name", "role", "contracted_hours", "absence_hours",
               "email_hours", "phone_hours", "other_hours", "total_logged_hours", "notes"], build_timesheets(staff))

    # ---- it/
    write_csv("it/saas-list.csv",
              ["application", "vendor", "category", "business_owner", "users", "plan", "annual_cost_ils", "renewal_date",
               "sso", "data_held", "ai_features", "ai_enabled", "dpa_signed", "notes"], [list(x) for x in SAAS])
    write_csv("it/proxy-log.csv",
              ["timestamp", "user_id", "department", "client_ip", "dest_host", "url_category", "method", "status",
               "bytes_out", "bytes_in", "action"], build_proxy(staff))
    write_csv("it/browser-extensions.csv",
              ["device", "user", "department", "os", "extension_name", "extension_id", "version", "installed_date",
               "install_source", "permissions", "inventory_date"], build_extensions(staff))
    write_csv("it/expenses.csv",
              ["expense_id", "employee_id", "employee_name", "department", "expense_date", "merchant", "description",
               "amount", "currency", "amount_ils", "payment_method", "category", "approved_by"], build_expenses(staff))

    # ---- usage/
    usage, roster = build_usage(staff)
    write_csv("usage/ai-usage-export.csv", ["date", "user_email", "feature", "events"], usage)
    write_csv("usage/hr-roster.csv",
              ["employee_id", "email", "full_name", "team", "role", "manager", "site", "fte", "employment_status",
               "status_since_date", "pilot_wave", "ai_assist_licence"], roster)

    # ---- documents/
    write_text("documents/findings-memo-ai-draft.md", memo_md(memo_numbers(tickets), k))

    if args.answer_key:
        write_answer_key(Path(args.answer_key), tickets, orders, shipments, emails_truth, claims_truth, k)


def order_row(o: Order) -> list:
    at = EXPORT_AT
    delivered = o.delivered <= at
    if delivered:
        status = "Delivered"
    elif o.shipment["warehouse"] <= at.date():
        status = "Scheduled"
    elif o.shipment["actual"] <= at.date():
        status = "At port / customs"
    else:
        status = "Awaiting container"
    return [o.oid, iso(o.placed), o.channel, o.customer.cid, "B2B" if o.customer.b2b else "B2C", o.customer.city,
            o.product["sku"], o.product["name_en"], COUNTRIES[o.product["country"]], o.qty, o.total,
            o.promised.isoformat(), o.container_shown, status, o.delivered.date().isoformat() if delivered else ""]


def shipment_row(s: dict) -> list:
    at = EXPORT_AT.date()
    known = [(a, n) for a, n in s["revisions"] if a <= at]
    rev = [n.isoformat() for _, n in known[:2]] + ["", ""]
    latest = known[-1][1] if known else s["eta"]
    arrived = s["actual"] <= at
    return [s["ref"], s["container"], s["supplier"], COUNTRIES[s["country"]], s["origin_port"], s["dest_port"],
            s["carrier"], s["vessel"], s["voyage"], s["etd"].isoformat(), s["eta"].isoformat(), rev[0], rev[1],
            latest.isoformat(), s["actual"].isoformat() if arrived else "",
            s["customs"].isoformat() if s["customs"] <= at else "",
            s["warehouse"].isoformat() if s["warehouse"] <= at else "", shipment_status(s, at)]


# Finance summary (ILS). Static numbers, kept here so the CSV and the markdown summary agree.
FINANCE_ROWS = [
    ["Revenue — B2C (web + showrooms)", 63_400_000, 67_100_000, 34_900_000, ""],
    ["Revenue — B2B (hotels, offices)", 26_800_000, 28_900_000, 14_600_000, ""],
    ["Total revenue", 90_200_000, 96_000_000, 49_500_000, ""],
    ["Cost of goods sold (landed)", -52_300_000, -55_700_000, -29_200_000, "incl. freight and duties"],
    ["Gross profit", 37_900_000, 40_300_000, 20_300_000, ""],
    ["Personnel — sales & showrooms", -9_100_000, -9_600_000, -4_900_000, ""],
    ["Personnel — logistics & warehouse", -8_700_000, -9_200_000, -4_800_000, ""],
    ["Customer service (fully loaded)", -3_250_000, -3_400_000, -1_760_000, "salaries, benefits, tools, space"],
    ["Personnel — management, finance, HR, IT, other", -5_600_000, -5_900_000, -3_000_000, ""],
    ["Last-mile delivery & assembly (outsourced)", -3_900_000, -4_200_000, -2_300_000, ""],
    ["Marketing", -2_600_000, -2_900_000, -1_500_000, ""],
    ["Rent & facilities", -2_400_000, -2_500_000, -1_300_000, ""],
    ["IT & software", -800_000, -880_000, -470_000, ""],
    ["Damage & returns write-offs", -610_000, -690_000, -420_000, ""],
    ["Write-off of capitalised software", 0, 0, 0, "FY2023: -860,000"],
    ["EBITDA", 940_000, 1_030_000, -150_000, "H1 is seasonally weak"],
]


def write_answer_key(out: Path, tickets: list[Ticket], orders: list[Order], shipments: list[dict],
                     emails_truth: list[dict], claims_truth: list[dict], k: dict) -> None:
    write_csv("tickets-truth.csv",
              ["ticket_id", "true_category", "true_language", "kind", "parent_ticket_id", "order_id", "is_wismo",
               "used_order_status_macro", "planted_findings"],
              [[t.tid, t.cat, t.lang, t.kind, t.parent.tid if t.parent else "", t.order.oid if t.order else "",
                "Y" if t.cat == "wismo" else "", "Y" if t.used_macro else "",
                " ".join(x for x in (
                    "F1" if t.cat == "wismo" else "", "F4" if t.kind == "followup" else "",
                    "F6" if t.kind == "duplicate" else "",
                    "F5" if t.category == "Other/כללי" else "") if x)]
               for t in tickets], out)
    write_csv("emails-truth.csv", list(emails_truth[0].keys()), [list(x.values()) for x in emails_truth], out)
    write_csv("orders-truth.csv", ["order_id", "supplier_country", "promised", "delivered", "lag_days",
                                   "container", "container_delay_days"],
              [[o.oid, o.product["country"], o.promised.isoformat(), o.delivered.date().isoformat(), o.lag,
                o.shipment["container"], o.shipment["delay"]] for o in orders], out)
    write_csv("claims-truth.csv", ["claim_no", "ticket_id", "outcome_recorded"],
              [[c["claim_no"], c["ticket_id"], "Y" if c["outcome_recorded"] else "N"] for c in claims_truth], out)
    n = len(tickets)
    wismo = sum(1 for t in tickets if t.cat == "wismo")
    lines = ["# Harbor & Pine — ground truth (generated)", "",
             f"- Tickets: {n}; true WISMO: {wismo} ({100 * wismo / n:.1f}%)",
             f"- Follow-ups (true): {sum(1 for t in tickets if t.kind == 'followup')}",
             f"- Duplicates (true): {sum(1 for t in tickets if t.kind == 'duplicate')} "
             f"({100 * sum(1 for t in tickets if t.kind == 'duplicate') / n:.1f}%)",
             f"- KPI first response (email, business days, business hours, Q3 mean): {k['frt']:.2f} h",
             "", "True category counts:", ""]
    cats: dict[str, int] = {}
    for t in tickets:
        cats[t.cat] = cats.get(t.cat, 0) + 1
    for c, v in sorted(cats.items(), key=lambda x: -x[1]):
        lines.append(f"- {c}: {v} ({100 * v / n:.1f}%)")
    write_text("README.md", "\n".join(lines) + "\n", out)


if __name__ == "__main__":
    main()
