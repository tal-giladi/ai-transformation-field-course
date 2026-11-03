"""Rebuild the Kinneret Plastics data room (module 13) byte for byte.

    python generate.py

Python 3.12+, standard library only. Writes every file in this folder's subfolders and the pilot's
inputs in ../pilot/. Reading the generator spoils the engagement: finish module 13 first.
"""
from __future__ import annotations

import csv
import sys

sys.dont_write_bytecode = True
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gen_common import ROOM  # noqa: E402
import gen_docs  # noqa: E402
import gen_docs2  # noqa: E402
import gen_manuals  # noqa: E402
import gen_ops  # noqa: E402
import gen_ops2  # noqa: E402
import gen_pilot  # noqa: E402
import gen_records  # noqa: E402
import gen_signals  # noqa: E402


def _read(rel: str) -> list[dict]:
    with open(ROOM / rel, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def deck_figures() -> dict:
    """The figures the December KPI deck shows, computed the way the deck computed them."""
    dt = _read("production/downtime-events-2026.csv")
    maint = ("MECH", "ELEC", "HYD", "MOULD", "WAIT_TECH")
    k = [int(x["duration_min"]) for x in dt if x["plant"] == "K" and x["reason_code"] in maint]
    unplanned = {}
    for x in dt:
        if x["reason_code"] not in ("PM", "SETUP", "NO_ORDER"):
            key = (x["plant"], x["reason_code"])
            unplanned[key] = unplanned.get(key, 0) + int(x["duration_min"])
    g_log = _read("maintenance/maintenance-log-plant-g-2026.csv")
    g = []
    for x in g_log:
        if x["תקלה"] == "טיפול מונע חודשי" or x["סטטוס"] != "מוכן" or not x["מוכן ב-"]:
            continue
        call = datetime.strptime(x["תאריך"] + " " + x["שעת קריאה"], "%d/%m/%Y %H:%M")
        ready_s = x["מוכן ב-"]
        if " " in ready_s:
            d, t = ready_s.split(" ")
            ready = datetime.strptime(f"{d}/{call.year} {t}", "%d/%m/%Y %H:%M")
            if ready < call:
                ready = ready.replace(year=call.year + 1)
        else:
            ready = datetime.strptime(x["תאריך"] + " " + ready_s, "%d/%m/%Y %H:%M")
        g.append((ready - call).total_seconds() / 3600)
    wo = _read("maintenance/work-orders-plant-k-2026.csv")
    pm = [x for x in wo if x["wo_type"] == "PM"]
    pm_closed = sum(1 for x in pm if x["status"] == "סגור")
    return {
        "mttr_k": round(sum(k) / len(k) / 60, 1), "mttr_g": round(sum(g) / len(g), 1),
        "pm_total": len(pm), "pm_closed": pm_closed, "pm_compliance": round(100 * pm_closed / len(pm)),
        "unplanned_hours": {f"{p}:{c}": round(v / 60) for (p, c), v in sorted(unplanned.items())},
    }


def main() -> None:
    stats = {}
    catalogue, by_cause = gen_records.parts()
    events = gen_ops.simulate(by_cause)
    stats.update(gen_records.write_parts(catalogue))
    stats.update(gen_records.write_assets())
    stats.update(gen_records.write_exam_register())
    stats.update(gen_ops.write_downtime(events))
    stats.update(gen_ops.write_work_orders_k(events, by_cause))
    stats.update(gen_ops2.write_plant_g_log(events))
    stats.update(gen_ops2.write_night_calls(events))
    stats.update(gen_records.write_scrap(events))
    stats.update(gen_signals.write_sensors(events))
    stats.update(gen_signals.write_alarms(events))
    drive = gen_manuals.write_drive()
    files = drive.pop("_files")
    stats.update(drive)
    stats.update(gen_manuals.write_drive_listing(files))
    stats.update(gen_manuals.write_pack())
    stats.update(gen_pilot.write_pilot())
    figures = deck_figures()
    gen_docs.write_all(figures)
    gen_docs2.write_all()
    stats["deck"] = figures
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
