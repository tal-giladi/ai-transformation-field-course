"""Flag identifiers in case notes before any text goes into an AI tool (lesson 16.5). Optional Track B.

    python deid_check.py                                  # checks ../data-room/cases/case-notes-sample.csv
    python deid_check.py my-notes.csv --column text       # any CSV with a text column
    python deid_check.py --text "..."                     # one piece of text

Rule-based and offline: no LLM, no network. It cannot prove a text is anonymous; it catches the patterns
that leak most often (ID-like numbers, phone numbers, emails, full names in Latin script, schools,
hospitals, rare diagnoses, streets) so a person looks again. A note with no flag still gets a human read.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT = HERE.parent / "data-room" / "cases" / "case-notes-sample.csv"

RULES = [
    ("id_number", re.compile(r"\b\d{3}-?\d{3}-?\d{3}\b")),
    ("phone", re.compile(r"\b0\d{1,2}-?\d{3}-?\d{4}\b")),
    ("email", re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")),
    ("school", re.compile(r"\b(school|kindergarten)\b|בית ספר|בי\"ס|גן ילדים|مدرسة|школ", re.I)),
    ("hospital", re.compile(r"\b(hospital|Rambam|Bnei Zion|Carmel|clinic)\b|בית חולים|مستشفى|больниц", re.I)),
    ("diagnosis_named", re.compile(r"syndrome|תסמונת|متلازمة|синдром", re.I)),
    ("street", re.compile(r"\b(St\.|Street|Rd\.)|רחוב|شارع|улиц", re.I)),
    ("ethnic_or_unique", re.compile(r"\bthe only\b|היחיד|الوحيد|единствен", re.I)),
]
# Two capitalised Latin words in a row, minus known non-names. Hebrew/Arabic/Russian names need a person.
FULL_NAME = re.compile(r"\b[A-Z][a-z]+(?:[- ](?:Ben|Abu|Al|Bar|El)-?)?[ -][A-Z][a-z]{2,}\b")
NOT_NAMES = {"National Insurance", "Kiryat Bialik", "Kiryat Ata", "Kiryat Motzkin", "Kiryat Hadas", "Open Hands",
             "Home Visit", "Call Back"}


def flags(text: str) -> list[str]:
    found = [name for name, rx in RULES if rx.search(text)]
    names = [m.group(0) for m in FULL_NAME.finditer(text) if m.group(0) not in NOT_NAMES]
    if names:
        found.append("full_name:" + "|".join(names))
    if re.search(r"\[NAME\]\s+[A-Z][a-z]{3,}", text):
        found.append("surname_after_placeholder")
    return found


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?", default=str(DEFAULT))
    ap.add_argument("--column", default="text")
    ap.add_argument("--id-column", default="note_id")
    ap.add_argument("--text")
    a = ap.parse_args()
    if a.text:
        print(flags(a.text) or "no flags (still read it before pasting)")
        return
    with open(a.csv, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    hit = 0
    for r in sorted(rows, key=lambda x: x.get(a.id_column, "")):
        fl = flags(r[a.column])
        if fl:
            hit += 1
            print(f"{r.get(a.id_column, '?')}: {', '.join(fl)}")
    print(f"\n{hit} of {len(rows)} texts flagged. Flagged texts must be fixed by hand before any AI tool; "
          "unflagged texts still get a human read.")


if __name__ == "__main__":
    sys.exit(main())
