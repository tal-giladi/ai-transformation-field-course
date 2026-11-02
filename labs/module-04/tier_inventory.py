"""Lesson 04.4 (Track B): apply the risk-tier rule and the DPIA triggers to the AI inventory.

Run from this folder:  python tier_inventory.py [path/to/inventory.csv]
Default input: ai-inventory-tiering.csv (next to this script). Standard library only.

The rule is written as checkable conditions so that anyone re-running it next quarter gets the same
tier for the same facts. A person may override a tier, but only with a written reason in the register.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCALE = 1000  # people or contacts a month above which personal data counts as "at scale"


def yes(value: str) -> bool:
    return value.strip().lower() in {"y", "yes", "true", "1"}


def volume(row: dict) -> int | None:
    raw = row.get("people_or_contacts_per_month", "").strip()
    return int(raw) if raw.isdigit() else None


def tier(row: dict) -> tuple[str, list[str]]:
    """Return (tier, reasons). High if any H condition holds, else Medium if any M, else Low."""
    data = row["max_data_class"].strip().upper()
    harm = row["harm_if_wrong"].strip().lower()
    vol = volume(row)
    high = []
    if yes(row["decides_about_people"]):
        high.append("H1 decides about or ranks people")
    if yes(row["acts_without_person"]) and harm in {"money", "rights", "safety"}:
        high.append(f"H2 acts without a person; a wrong output costs {harm}")
    if data == "S":
        high.append("H3 highly sensitive data (class S)")
    if data == "D" and vol is not None and vol > SCALE and yes(row["new_recipients"]):
        high.append(f"H4 personal data of {vol:,} people or contacts a month, sent to new recipients")
    if high:
        return "High", high
    medium = []
    if data == "D":
        medium.append("M1 personal data (class D)")
    if yes(row["reaches_outside"]):
        medium.append("M2 output reaches customers or the public")
    if data == "B" and yes(row["new_recipients"]):
        medium.append("M3 confidential business data in an outside tool")
    if medium:
        return "Medium", medium
    return "Low", ["no condition met"]


def dpia_triggers(row: dict) -> list[str]:
    """DPIA triggers (lesson 04.4). Any one means: write a DPIA before the use starts or continues."""
    data = row["max_data_class"].strip().upper()
    vol = volume(row)
    out = []
    if yes(row["decides_about_people"]):
        out.append("decisions about people")
    if data == "S":
        out.append("highly sensitive data")
    if data == "D" and vol is not None and vol > SCALE:
        out.append("new technology on personal data at scale")
    if data in {"D", "S"} and yes(row["new_recipients"]) and vol is not None and vol > SCALE:
        out.append("personal data to new recipients, including abroad")
    if data == "D" and vol is None:
        out.append("volume unknown: find out before deciding")
    return out


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "ai-inventory-tiering.csv"
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    counts = {"High": 0, "Medium": 0, "Low": 0}
    for row in rows:
        t, reasons = tier(row)
        counts[t] += 1
        triggers = dpia_triggers(row)
        print(f"{row['id']:6} {t:6} {row['tool_or_use']}")
        print(f"       why: {'; '.join(reasons)}")
        if triggers:
            print(f"       DPIA: {'; '.join(triggers)}")
    print(f"\n{len(rows)} rows: {counts['High']} High, {counts['Medium']} Medium, {counts['Low']} Low")


if __name__ == "__main__":
    sys.stdout.reconfigure(errors="replace")
    main()
