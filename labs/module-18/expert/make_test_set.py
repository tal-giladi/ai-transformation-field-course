"""The expert's inquiry test set (240 items) and the portal's routing baseline on it.

    python make_test_set.py

Standard library only. Reads ../data-room/inquiries/student-inquiries-2025-26.csv, writes
test-set-240.csv next to this file and prints the baseline: how often the portal's category routing
sent the inquiry to the unit that resolved it. Seeded, so it rebuilds byte for byte.
"""
from __future__ import annotations

import csv
import random
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "data-room" / "inquiries" / "student-inquiries-2025-26.csv"
QUOTA = {"he": 90, "ar": 80, "ru": 40, "en": 30}
WINDOWS = [(date(2025, 12, 28), date(2026, 1, 11)), (date(2026, 5, 31), date(2026, 6, 14))]


def language(text: str) -> str:
    if any("؀" <= ch <= "ۿ" for ch in text):
        return "ar"
    if any("Ѐ" <= ch <= "ӿ" for ch in text):
        return "ru"
    if any("֐" <= ch <= "׿" for ch in text):
        return "he"
    return "en"


def urgent(row: dict) -> bool:
    d = datetime.fromisoformat(row["opened_at"]).date()
    return row["resolved_unit"] == "finance - collections" and any(a <= d <= b for a, b in WINDOWS)


def main() -> None:
    rows = list(csv.DictReader(open(SRC, encoding="utf-8", newline="")))
    by_lang = defaultdict(list)
    for r in rows:
        by_lang[language(r["text"])].append(r)
    rng = random.Random(20270409)
    picked = []
    for lang, n in QUOTA.items():
        picked += [(lang, r) for r in rng.sample(by_lang[lang], n)]
    picked.sort(key=lambda x: x[1]["inquiry_id"])
    out = []
    for i, (lang, r) in enumerate(picked):
        split = "dev" if i % 6 == 0 else "test"
        out.append([r["inquiry_id"], lang, r["category_selected"], r["text"], r["resolved_unit"],
                    "Y" if urgent(r) else "N", r["first_unit"], split])
    with open(HERE / "test-set-240.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["inquiry_id", "language", "category_selected", "text", "gold_unit", "urgent",
                    "portal_first_unit", "split"])
        w.writerows(out)
    test = [o for o in out if o[7] == "test"]
    print(f"test-set-240.csv: {len(out)} items, {len(test)} in the test split")
    stats = defaultdict(lambda: [0, 0])
    for o in test:
        for key in ("all", o[1], "finance" if o[4] == "finance - collections" else None,
                    "urgent" if o[5] == "Y" else None):
            if key:
                stats[key][0] += 1
                stats[key][1] += o[6] == o[4]
    for key, (n, ok) in stats.items():
        print(f"  portal routing correct, {key}: {ok}/{n} = {100 * ok / n:.1f}%")


if __name__ == "__main__":
    main()
