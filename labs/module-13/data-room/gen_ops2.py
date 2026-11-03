"""The Plant G maintenance log, the night-call log and the KPI figures the December deck shows.

Reading this spoils the engagement: finish module 13 first.
"""
from __future__ import annotations

from datetime import datetime, timedelta
from statistics import mean, median

from gen_common import ROOM, TECHS_G, dmy, hm, machines, rng, write_csv
from textbank import CAUSES, G_PROBLEM_PREFIX, G_STATUS, NIGHT_TOPICS, VAGUE_ACTIONS


def _g_name(r, hall: int, maker: str) -> str:
    x = r.random()
    if x < 0.55:
        return f"מכונה {hall}"
    if x < 0.8:
        return f"M{hall}"
    return f"{'מורנדי' if maker == 'Morandi' else 'הייוויי'} {hall}"


def write_plant_g_log(events: list[dict]) -> dict:
    """Plant G keeps maintenance in Excel: DD/MM/YYYY, local time, hall numbers, 'ready' = tech done."""
    r = rng(4)
    rows = []
    for e in [x for x in events if x["plant"] == "G"]:
        g = e["group"]
        if not ((g == "machine" and r.random() < 0.9) or (g == "mould" and r.random() < 0.5)
                or (g == "material" and r.random() < 0.3)):
            continue
        texts = CAUSES[e["cause"]][2]
        problem = r.choice(G_PROBLEM_PREFIX) + r.choice(texts["he"] if r.random() < 0.8 else texts["ar"])
        action = r.choice(VAGUE_ACTIONS[:5]) if r.random() < 0.4 else r.choice(CAUSES[e["cause"]][3])
        status = r.choice(G_STATUS)
        done = e["tech_done"]
        ready = hm(done) if done.date() == e["start"].date() else done.strftime("%d/%m %H:%M")
        if status != "מוכן":
            ready = ""
        note = ""
        if e["needs_part"] and r.random() < 0.4:
            note = "חלק הוזמן מכנרת"
        rows.append((e["start"], [dmy(e["start"]), hm(e["start"]), _g_name(r, e["hall"], e["maker"]), problem,
                                  action, e["tech"], status if status != "מוכן" or ready else "מוכן", ready, note]))
    for m in [x for x in machines() if x["plant"] == "G"]:
        for month in range(1, 13):
            d = datetime(2026, month, r.randint(4, 24), r.choice([8, 9, 10]), r.choice([0, 15, 30]))
            if d.weekday() in (4, 5):
                d += timedelta(days=2)
            rows.append((d, [dmy(d), hm(d), _g_name(r, m["hall"], m["maker"]), "טיפול מונע חודשי",
                             "בוצע", r.choice([t[0] for t in TECHS_G]), "מוכן", hm(d + timedelta(hours=2)), ""]))
    rows.sort(key=lambda x: x[0])
    out = [[i] + row for i, (_, row) in enumerate(rows, 1)]
    n = write_csv(ROOM / "maintenance" / "maintenance-log-plant-g-2026.csv",
                  ["מס'", "תאריך", "שעת קריאה", "מכונה", "תקלה", "טיפול", "טכנאי", "סטטוס", "מוכן ב-", "הערות"],
                  out)
    return {"g_log_rows": n}


def write_night_calls(events: list[dict]) -> dict:
    """Shift supervisors' log of night calls to the maintenance manager (kept since 1 March 2026)."""
    r = rng(5)
    rows = []
    sups = ["Tigist W.", "Yaron A.", "Muhammad Z."]
    for e in events:
        c = e["call"]
        if not c:
            continue
        if e["cause"] in ("HR_HEATER", "HR_TC"):
            topic = r.choice([NIGHT_TOPICS[1], NIGHT_TOPICS[2]])
        elif e["needs_part"]:
            topic = r.choice([NIGHT_TOPICS[3], NIGHT_TOPICS[0]])
        elif e["cause"] == "DRIVE":
            topic = NIGHT_TOPICS[5]
        elif e["cause"] == "GATE":
            topic = NIGHT_TOPICS[7]
        elif e["maker"] == "Haiwei":
            topic = r.choice([NIGHT_TOPICS[9], NIGHT_TOPICS[0]])
        else:
            topic = r.choice(NIGHT_TOPICS[:8])
        call_t = e["start"] + timedelta(minutes=e["wait"] + r.randint(10, 40))
        waiting = c["reach"] + c["phone"] + (70 if c["came_in"] else 0) + r.randint(5, 25)
        rows.append([call_t.strftime("%Y-%m-%d"), r.choice(sups), e["mes"], e["tech"], topic, hm(call_t),
                     c["reach"], c["phone"], waiting, "כן" if c["by_phone"] else "לא",
                     "כן" if c["came_in"] else "לא"])
    rows.sort()
    n = write_csv(ROOM / "maintenance" / "night-calls-2026.csv",
                  ["date", "supervisor", "machine", "technician_id", "topic", "call_time",
                   "minutes_to_reach", "minutes_on_phone", "machine_waiting_min", "solved_by_phone",
                   "came_in"], rows)
    return {"night_calls": n}


def kpi_figures(events: list[dict]) -> dict:
    """What the December KPI deck computed: Plant K MTTR from MES (stop to restart), Plant G from the
    Excel log (call to 'ready'). Also the like-for-like numbers the learner can compute."""
    k = [e for e in events if e["plant"] == "K" and e["group"] in ("machine", "mould")]
    g = [e for e in events if e["plant"] == "G" and e["group"] in ("machine", "mould")]
    hours = lambda a, b: (b - a).total_seconds() / 3600
    return {
        "mttr_k_restart": round(mean(hours(e["start"], e["end"]) for e in k), 1),
        "mttr_g_ready": round(mean(hours(e["start"], e["tech_done"]) for e in g), 1),
        "mttr_g_restart": round(mean(hours(e["start"], e["end"]) for e in g), 1),
        "median_restart_gap_g": round(median(e["restart"] for e in g)),
    }
