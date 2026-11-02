"""The fixed split of the 2,000 written tickets (lesson 08.5). Not run on its own.

dev: 300 tickets to tune prompts on; test: the other 1,700, frozen; track-a: 200 test tickets
(100 Hebrew, 40 Arabic, 35 Russian, 25 English) for the spreadsheet track; negative: the 12
hand-written negative tests in negative-tests.csv (not part of the 2,000). The split depends only on
the ticket ids and a fixed seed, so it is the same on every machine.
"""
from __future__ import annotations

import csv
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
TICKETS = HERE.parent / "data-room" / "support" / "written-tickets-2000.csv"
LABELS = HERE / "labels-2000.csv"
NEGATIVE = HERE / "negative-tests.csv"
NEGATIVE_LABELS = HERE / "negative-labels.csv"
SEED = 20261218


def _read(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def split() -> dict[str, list[str]]:
    rows = _read(TICKETS)
    ids = sorted(r["ticket_id"] for r in rows)
    r = random.Random(SEED)
    r.shuffle(ids)
    dev, test = sorted(ids[:300]), sorted(ids[300:])
    lang = {x["ticket_id"]: x["language"] for x in _read(LABELS)}
    quota = {"he": 100, "ar": 40, "ru": 35, "en": 25}
    track_a = []
    for code, n in quota.items():
        pool = [t for t in test if lang[t] == code]
        track_a += random.Random(f"{SEED}-{code}").sample(pool, n)
    return {"dev": dev, "test": test, "track-a": sorted(track_a), "all": sorted(ids)}


def load_set(name: str) -> list[dict]:
    if name == "negative":
        return _read(NEGATIVE)
    wanted = set(split()[name])
    return [r for r in _read(TICKETS) if r["ticket_id"] in wanted]


def labels() -> dict[str, dict]:
    return {x["ticket_id"]: x for x in _read(LABELS) + _read(NEGATIVE_LABELS)}
