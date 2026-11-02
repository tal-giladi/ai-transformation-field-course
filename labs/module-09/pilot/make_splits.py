"""Builds pilot/splits.csv (40 development + 200 test documents) and pilot/track-a-sheet.csv.

    python pilot/make_splits.py

Stratified by document language and type, seeded, so everyone gets the same split. The Track A
sheet holds 60 test documents (15 per language) with one row per field: the verified value, the
vendor's Smart Intake value and the rules baseline's value, and an empty column for yours.
"""
from __future__ import annotations

import csv
import random
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXT = HERE.parent / "data-room" / "extraction"


def read(path: Path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    r = random.Random(909)
    docs = read(EXT / "documents_index.csv")
    strata = defaultdict(list)
    for d in docs:
        strata[(d["doc_language"], d["doc_type"])].append(d["doc_id"])
    dev = set()
    for key in sorted(strata):
        ids = sorted(strata[key])
        r.shuffle(ids)
        dev.update(ids[: max(1, round(len(ids) / 6))])
    dev = set(sorted(dev)[:40]) if len(dev) > 40 else dev
    with open(HERE / "splits.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["doc_id", "split"])
        for d in docs:
            w.writerow([d["doc_id"], "dev" if d["doc_id"] in dev else "test"])
    # Track A: 15 test documents per language
    by_lang = defaultdict(list)
    for d in docs:
        if d["doc_id"] not in dev:
            by_lang[d["doc_language"]].append(d)
    chosen = []
    for lang in ("he", "ar", "ru", "en"):
        pool = sorted(by_lang[lang], key=lambda d: d["doc_id"])
        r.shuffle(pool)
        chosen += sorted(pool[:15], key=lambda d: d["doc_id"])
    gold = defaultdict(dict)
    for g in read(EXT / "gold_fields.csv"):
        gold[g["doc_id"]][g["field"]] = g["value"]
    vend = defaultdict(dict)
    for v in read(EXT / "smart_intake_output.csv"):
        vend[v["doc_id"]][v["field"]] = v["value"]
    rules = defaultdict(dict)
    rp = HERE.parent / "runs" / "rules-baseline.csv"
    if rp.exists():
        for v in read(rp):
            rules[v["doc_id"]][v["field"]] = v["value"]
    with open(HERE / "track-a-sheet.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["doc_id", "file", "doc_type", "doc_language", "capture_channel", "region", "claimant_age_band",
                    "field", "verified_value", "smart_intake_value", "rules_value", "your_value"])
        for d in sorted(chosen, key=lambda d: d["doc_id"]):
            for field in sorted(gold[d["doc_id"]]):
                w.writerow([d["doc_id"], "data-room/extraction/" + d["file"], d["doc_type"], d["doc_language"],
                            d["capture_channel"], d["region"], d["claimant_age_band"], field, gold[d["doc_id"]][field],
                            vend[d["doc_id"]].get(field, ""), rules[d["doc_id"]].get(field, ""), ""])
    print(f"dev {len(dev)}, test {len(docs) - len(dev)}, Track A documents {len(chosen)}")


if __name__ == "__main__":
    main()
