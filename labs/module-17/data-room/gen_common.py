"""Shared helpers and constants for the Vantage Logistics data-room generator (standard library only).

Every file is written with LF line endings and UTF-8 (no BOM), so `python generate.py` rebuilds the
data room byte for byte on any machine.
"""
from __future__ import annotations

import csv
import io
import random
from datetime import date, datetime, timedelta
from pathlib import Path

SEED = 20270606
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


def write_md(rel: str, text: str) -> int:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    body = text.strip("\n") + "\n"
    path.write_bytes(body.encode("utf-8"))
    return 1


def days(start: date, end: date):
    d = start
    while d <= end:
        yield d
        d += timedelta(days=1)


def is_workday(d: date) -> bool:
    """Israeli operations run Sunday to Thursday, with a short Friday (Python: Monday=0 ... Sunday=6)."""
    return d.weekday() in (6, 0, 1, 2, 3)


def ts(d: date, minutes: int) -> str:
    """'2027-05-03 08:14' from a date and minutes after midnight."""
    return (datetime(d.year, d.month, d.day) + timedelta(minutes=minutes)).strftime("%Y-%m-%d %H:%M")


# Regions and depots. Europe runs Monday-Friday.
DEPOTS = [
    ("North", "HFA", "Haifa Port"), ("North", "KRM", "Karmiel"), ("North", "KSH", "Kiryat Shmona"),
    ("Centre", "MOD", "Modi'in DC"), ("Centre", "APL", "Airport Logistics Park"), ("Centre", "PTK", "Petah Tikva"),
    ("South", "ASH", "Ashdod Port"), ("South", "BSV", "Be'er Sheva"), ("South", "NTV", "Netivot"),
    ("Europe", "RTM", "Rotterdam"),
]

# Key dates of the story.
ROUTE_NORTH_LIVE = date(2026, 11, 8)
ROUTE_ALL_REGIONS = date(2027, 1, 10)
SOUTH_PULLED_BACK = date(2027, 2, 25)
CENTRE_PLANNER_ONLY = date(2027, 3, 14)
MABAT_FEED_BROKEN = date(2026, 11, 14)
DOCS_V42 = date(2027, 5, 2)
DOCS_V421 = date(2027, 5, 21)
INCIDENT_OPENED = date(2027, 5, 18)
ASSIST_DOCS_ON = date(2027, 4, 20)
ASSIST_DOCS_OFF = date(2027, 5, 19)

# Importers whose documents and declarations appear in the customs and portal exports.
# (code, short name, type). All fictional.
CUSTOMERS = [
    ("C1007", "Gefen Medical Distribution", "medical consumables"),
    ("C1022", "Shuk Online Imports", "B2C parcel consolidator"),
    ("C1031", "Narkis Home Textiles", "home textiles"),
    ("C1044", "Ofanim Cycle Parts", "bicycle parts"),
    ("C1052", "Tavlin Spice Traders", "food"),
    ("C1060", "Kav Yashar Hardware", "hardware"),
    ("C1068", "Zohar Lighting Supply", "lighting"),
    ("C1073", "Migdal Office Furnishing", "furniture"),
    ("C1081", "Shaked Baby Goods", "baby products"),
    ("C1095", "Tamar Kitchenware", "kitchenware"),
    ("C1102", "Even Ceramics Import", "ceramics"),
    ("C1117", "Nahal Garden Tools", "garden"),
    ("C1123", "Peleg Auto Spares", "auto parts"),
    ("C1136", "Rakia Toys", "toys"),
    ("C1141", "Sapir Cosmetics Import", "cosmetics"),
    ("C1158", "Yarden Pet Supplies", "pet supplies"),
    ("C1164", "Arava Solar Components", "solar"),
    ("C1172", "Hermon Sports Gear", "sports"),
    ("C1189", "Dekel Electronics Trade", "electronics"),
    ("C1193", "Neta Lab Supplies", "lab supplies"),
    ("C1204", "Galim Marine Equipment", "marine"),
    ("C1218", "Orot Packaging", "packaging"),
    ("C1225", "Brosh Building Materials", "building materials"),
    ("C1237", "Lahav Kitchen Appliances", "appliances"),
]

# Suppliers' invoice prefixes. Two consolidators in Shenzhen and Ningbo share a numeric series:
# that is where Tzir Docs 4.2's normaliser collides.
SUPPLIER_PREFIXES = ["SZX", "NGB", "SHA", "QDO", "XMN", "IST", "MUM", "HCM", "RTM", "BRE", "GDZ", "TJN"]

LANG_MIX = ["he", "he", "he", "he", "ar", "ru", "en", "en", "am"]
