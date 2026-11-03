"""Stoppages, work orders, the Plant G log, MES downtime and night calls (2026).

One hidden simulation of what really happened on 40 machines drives every export, so the files
disagree with each other the way real exports do. Reading this spoils the engagement.
"""
from __future__ import annotations

from datetime import datetime, timedelta

from gen_common import (DEFERRED_PM, NIGHT_TECHS_K, ROOM, TECHS_G, TECHS_K, YEAR_END, YEAR_START,
                        dmy, hm, iso_local, is_working_time, lognormal_minutes, machines,
                        random_working_time, rng, shift_end, shift_of, write_csv)
from textbank import (CAUSE_MES, CAUSES, G_PROBLEM_PREFIX, G_STATUS, NIGHT_TOPICS, NOTEBOOK_ACTIONS,
                      OPERATOR_DETAIL, PART_NOT_FOUND, PM_TEXT, VAGUE_ACTIONS)

RATE_MACHINE = {1: 7, 2: 16, 3: 26}          # machine-caused stoppages a year by age class
RATE_MOULD, RATE_MATERIAL = 24, 9
REPAIR_MEDIAN = {
    "HYD_PUMP": 240, "HYD_VALVE": 120, "HYD_LEAK": 75, "OIL_TEMP": 60, "HEATER": 70, "TC": 45,
    "CONTACTOR": 50, "DRIVE": 90, "CHECK_RING": 300, "CLAMP": 150, "EJECTOR": 60, "GATE": 60,
    "ROBOT": 50, "HR_HEATER": 180, "HR_TC": 90, "COOLING_LEAK": 120, "EJ_PIN": 150,
    "MOULD_DAMAGE": 240, "DRYER": 90, "WET_MAT": 150,
}
MACHINE_CAUSES = [c for c, v in CAUSES.items() if v[0] == "machine"]
MOULD_CAUSES = [c for c, v in CAUSES.items() if v[0] == "mould"]
MATERIAL_CAUSES = [c for c, v in CAUSES.items() if v[0] == "material"]
MACHINE_WEIGHTS = [8, 6, 9, 4, 12, 7, 5, 4, 3, 4, 3, 7, 6]
MOULD_WEIGHTS = [9, 6, 8, 5, 3]


def _next_tooling_start(t: datetime) -> datetime:
    d = datetime(t.year, t.month, t.day, 7, 30)
    if d <= t:
        d += timedelta(days=1)
    while d.weekday() in (4, 5):  # tooling works Sunday-Thursday
        d += timedelta(days=1)
    return d


def simulate(parts_by_cause: dict) -> list[dict]:
    """The hidden truth: every unplanned stoppage of 2026 with its real cause and timings."""
    r = rng(1)
    events = []
    for m in machines():
        n_machine = RATE_MACHINE[m["age"]]
        plans = [("machine", n_machine), ("mould", RATE_MOULD + (4 if m["plant"] == "G" else 0)),
                 ("material", RATE_MATERIAL)]
        for group, rate in plans:
            n = max(0, int(round(r.gauss(rate, rate ** 0.5))))
            for _ in range(n):
                start = random_working_time(r, YEAR_START, YEAR_END - timedelta(days=1))
                cause = (r.choices(MACHINE_CAUSES, MACHINE_WEIGHTS)[0] if group == "machine" else
                         r.choices(MOULD_CAUSES, MOULD_WEIGHTS)[0] if group == "mould" else
                         r.choice(MATERIAL_CAUSES))
                events.append(_event(r, m, cause, start, parts_by_cause))
        if m["mes"] in DEFERRED_PM:  # deferred PMs: extra machine stoppages in Q4
            for _ in range(int(round(n_machine * 0.3))):
                start = random_working_time(r, datetime(2026, 10, 1), datetime(2026, 12, 31))
                cause = r.choices(MACHINE_CAUSES, MACHINE_WEIGHTS)[0]
                events.append(_event(r, m, cause, start, parts_by_cause))
    k22 = next(x for x in machines() if x["mes"] == "K22")
    events.append(_event(r, k22, "HYD_PUMP", datetime(2026, 12, 2, 3, 10), parts_by_cause, forced=True))
    events.sort(key=lambda e: (e["start"], e["mes"]))
    for i, e in enumerate(events):
        e["eid"] = i
    return events


def _event(r, m, cause, start, parts_by_cause, forced=False) -> dict:
    group = CAUSES[cause][0]
    night = shift_of(start) == "night"
    if m["plant"] == "K":
        tech = r.choice(NIGHT_TECHS_K) if night else r.choice([t[0] for t in TECHS_K])
    else:
        tech = r.choice([t[0] for t in TECHS_G])
    wait = lognormal_minutes(r, 38 if night else 12, 0.7, 2)
    repair = lognormal_minutes(r, REPAIR_MEDIAN[cause], 0.55, 10)
    if forced:
        wait, repair = 35, 410
    tooling_wait = 0
    if group == "mould" and night and r.random() < 0.6:
        ready = start + timedelta(minutes=wait + 30)
        tooling_wait = int((_next_tooling_start(ready) - ready).total_seconds() // 60)
    needs_part = group == "machine" and (r.random() < 0.35 or forced)
    bin_wrong = needs_part and m["plant"] == "K" and r.random() < 0.3
    parts_min = 0
    if needs_part:
        parts_min = lognormal_minutes(r, 20 if m["plant"] == "K" else 55, 0.6, 5) + (45 if bin_wrong else 0)
    call = None
    junior = m["plant"] == "K" and dict((t[0], t[2]) for t in TECHS_K).get(tech, 99) < 10
    if m["plant"] == "K" and night and group in ("machine", "mould") and start >= datetime(2026, 3, 1):
        p = 0.32 if junior else 0.12
        if cause in ("HR_HEATER", "HR_TC", "DRIVE", "HYD_VALVE"):
            p += 0.12
        if r.random() < p:
            phone = r.randint(4, 26)
            reach = r.choice([0, 0, 3, 8, 15, 25])
            came_in = r.random() < 0.1
            call = {"phone": phone, "reach": reach, "came_in": came_in, "by_phone": not came_in and r.random() < 0.75}
            repair += reach + phone + (70 if came_in else 0)
    restart = lognormal_minutes(r, 50, 0.5, 10)
    tech_done = start + timedelta(minutes=wait + tooling_wait + repair + parts_min)
    end = tech_done + timedelta(minutes=restart)
    part = ""
    if needs_part:
        options = parts_by_cause.get(cause, [])
        if options:
            part = r.choice(options)
    return {"plant": m["plant"], "mes": m["mes"], "cmms": m["cmms"], "hall": m["hall"], "maker": m["maker"],
            "cause": cause, "group": group, "start": start, "wait": wait, "tooling_wait": tooling_wait,
            "repair": repair, "parts_min": parts_min, "bin_wrong": bin_wrong, "needs_part": needs_part,
            "part": part, "restart": restart, "tech_done": tech_done, "end": end, "night": night,
            "call": call, "tech": tech, "forced": forced}


# ------------------------------------------------------------------ MES downtime (ProdTrack)
def write_downtime(events: list[dict]) -> dict:
    r = rng(2)
    rows = []
    for e in events:
        code = CAUSE_MES[e["cause"]]
        x = r.random()
        if e["night"] and e["wait"] + e["tooling_wait"] > 45 and x < 0.3:
            code = "WAIT_TECH"
        elif not e["night"] and e["wait"] > 25 and x < 0.15:
            code = "WAIT_TECH"
        elif e["group"] == "mould" and x < 0.1:
            code = "MECH"
        elif x > 0.93:
            code = "OTHER"
        rows.append([e["plant"], e["mes"], e["start"], e["end"], code, r.choice(OPERATOR_DETAIL[code]),
                     "supervisor" if r.random() < 0.3 else "operator", "unplanned"])
    for m in machines():  # planned stops
        for month in range(1, 13):
            if not (m["mes"] in DEFERRED_PM and month in (7, 8, 9)):
                s = random_working_time(r, datetime(2026, month, 2), datetime(2026, month, 26))
                rows.append([m["plant"], m["mes"], s, s + timedelta(minutes=lognormal_minutes(r, 150, 0.3, 60)),
                             "PM", r.choice(OPERATOR_DETAIL["PM"]), "supervisor", "planned"])
            for _ in range(2):
                s = random_working_time(r, datetime(2026, month, 1), datetime(2026, month, 28))
                rows.append([m["plant"], m["mes"], s, s + timedelta(minutes=lognormal_minutes(r, 95, 0.35, 30)),
                             "SETUP", r.choice(OPERATOR_DETAIL["SETUP"]), "supervisor", "planned"])
            if r.random() < 0.45:
                s = random_working_time(r, datetime(2026, month, 1), datetime(2026, month, 28))
                rows.append([m["plant"], m["mes"], s, s + timedelta(minutes=lognormal_minutes(r, 480, 0.6, 120)),
                             "NO_ORDER", r.choice(OPERATOR_DETAIL["NO_ORDER"]), "supervisor", "planned"])
            if r.random() < 0.5:
                s = random_working_time(r, datetime(2026, month, 1), datetime(2026, month, 28))
                rows.append([m["plant"], m["mes"], s, s + timedelta(minutes=lognormal_minutes(r, 70, 0.5, 20)),
                             "QA_HOLD", r.choice(OPERATOR_DETAIL["QA_HOLD"]), "supervisor", "unplanned"])
    rows.sort(key=lambda x: (x[2], x[1]))
    out = []
    for i, (plant, mes, s, en, code, det, role, kind) in enumerate(rows, 1):
        out.append([f"DT-26-{i:05d}", plant, mes, iso_local(s), iso_local(en),
                    int((en - s).total_seconds() // 60), code, det, shift_of(s), role])
    n = write_csv(ROOM / "production" / "downtime-events-2026.csv",
                  ["event_id", "plant", "machine", "start_at", "end_at", "duration_min", "reason_code",
                   "reason_note", "shift", "entered_by"], out)
    return {"downtime_rows": n}


# ------------------------------------------------------------------ Plant K work orders (MaintPro)
def write_work_orders_k(events: list[dict], parts_by_cause: dict) -> dict:
    r = rng(3)
    rows = []
    stats = {"bd": 0, "coded": 0, "code99": 0, "blank": 0}
    dryers = [f"KN-DR-{i:02d}" for i in range(1, 7)]
    for e in [x for x in events if x["plant"] == "K"]:
        g = e["group"]
        if not ((g == "machine" and r.random() < 0.95) or (g == "mould" and r.random() < 0.55)
                or (g == "material" and r.random() < 0.4)):
            continue
        asset = e["cmms"] if g != "material" or r.random() < 0.5 else r.choice(dryers)
        lang_of = {t[0]: t[1] for t in TECHS_K}
        lang = lang_of[e["tech"]]
        texts = CAUSES[e["cause"]][2]
        wl = lang if lang in texts and r.random() < 0.45 else ("he" if r.random() < 0.85 else "en")
        problem = r.choice(texts[wl])
        month = e["start"].month
        x = r.random()
        p_coded = 0.24 - 0.016 * (month - 1)
        if e["forced"]:
            code = "H01"
        elif x < p_coded:
            code = CAUSES[e["cause"]][1] if r.random() < 0.85 else r.choice(["H01", "E01", "M02", "S01", "99"])
        elif x < p_coded + 0.18:
            code = "99"
        else:
            code = ""
        stats["bd"] += 1
        stats["coded" if code not in ("", "99") else ("code99" if code == "99" else "blank")] += 1
        y = r.random()
        if e["forced"]:
            action = "הוחלף מיסב במנוע משאבה. ויברציה עלתה 3 שבועות (ראה היסטוריאן)"
        elif e["bin_wrong"] and r.random() < 0.6:
            action = r.choice(PART_NOT_FOUND)
        elif y < 0.45:
            action = r.choice(VAGUE_ACTIONS)
        elif y < 0.48:
            action = r.choice(NOTEBOOK_ACTIONS)
        else:
            action = r.choice(CAUSES[e["cause"]][3])
        z = r.random()
        if z < 0.25 or e["forced"]:
            completed, closed_by = e["tech_done"], e["tech"]
        elif z < 0.40:
            thu = e["tech_done"] + timedelta(days=(3 - e["tech_done"].weekday()) % 7)
            bulk = datetime(thu.year, thu.month, thu.day, 15, 30) + timedelta(minutes=r.randint(0, 60))
            completed, closed_by = (bulk, "svetlana.p") if bulk > e["tech_done"] else (e["tech_done"], e["tech"])
        else:
            completed = shift_end(e["tech_done"]) - timedelta(minutes=r.randint(0, 12))
            if completed < e["tech_done"]:
                completed = e["tech_done"]
            closed_by = e["tech"]
        started = "" if r.random() < 0.45 else iso_local(e["start"] + timedelta(minutes=e["wait"]))
        dt = r.random()
        dur = int((e["end"] - e["start"]).total_seconds() // 60)
        downtime = "" if dt < 0.5 else (0 if dt < 0.62 else int(round(dur * r.uniform(0.7, 1.3) / 15) * 15))
        labour = "" if r.random() < 0.3 else max(15, int(round(e["repair"] / 30) * 30))
        part = e["part"] if e["needs_part"] and r.random() < 0.7 else ""
        rows.append([iso_local(e["start"] + timedelta(minutes=r.randint(1, 6))), asset, "BD",
                     "1" if r.random() < 0.6 else "2", "מפעיל" if r.random() < 0.7 else "ראש משמרת",
                     shift_of(e["start"]), started, iso_local(completed), e["tech"], problem, action, code,
                     downtime, part, labour, "סגור", closed_by])
    rows += _pm_rows(r)
    rows += _cm_rows(r)
    rows.sort(key=lambda x: x[0])
    out = []
    for i, row in enumerate(rows, 1):
        desc = _asset_desc(row[1])
        out.append([f"WO-26-{i:05d}", row[1], desc, row[2], row[3], row[0]] + row[4:])
    n = write_csv(ROOM / "maintenance" / "work-orders-plant-k-2026.csv",
                  ["wo_number", "asset_id", "asset_description", "wo_type", "priority", "requested_at",
                   "requested_by", "shift", "started_at", "completed_at", "technician_id", "problem_text",
                   "action_text", "failure_code", "downtime_min", "parts_used", "labour_min", "status",
                   "closed_by"], out)
    stats["wo_rows"] = n
    return stats


def _asset_desc(asset: str) -> str:
    if asset.startswith("KN-IM-"):
        m = next(x for x in machines() if x["cmms"] == asset)
        return f"מכונת הזרקה {m['maker']} {m['model']}"
    if asset.startswith("KN-DR-"):
        return "מייבש DryMax DM-150"
    if asset.startswith("KN-CH-"):
        return "צ'ילר ArcticFlow AC-40"
    if asset.startswith("KN-CP-"):
        return "מדחס + מכל אוויר"
    if asset.startswith("KN-CR-"):
        return "עגורן גשר 10 טון"
    return asset


def _pm_rows(r) -> list[list]:
    rows = []
    stats_k = [m for m in machines() if m["plant"] == "K"]
    for m in stats_k:
        for month in range(1, 13):
            kind = "quarterly" if month in (3, 6, 9, 12) else "monthly"
            title, acts = PM_TEXT[kind]
            due = datetime(2026, month, 3, 7, 0)
            if m["mes"] in DEFERRED_PM and month in (7, 8, 9):
                done = datetime(2026, 9, 30, 15, 20) + timedelta(minutes=r.randint(0, 40))
                rows.append([iso_local(due), m["cmms"], "PM", "3", "מתוכנן", "morning", "",
                             iso_local(done), "", title, "בוצע", "", "", "", "", "סגור", "svetlana.p"])
                continue
            if r.random() < 0.065:
                rows.append([iso_local(due), m["cmms"], "PM", "3", "מתוכנן", "morning", "", "", "", title,
                             "", "", "", "", "", "פתוח", ""])
                continue
            s = random_working_time(r, datetime(2026, month, 3), datetime(2026, month, 25))
            lab = r.choice([90, 120, 120, 150, 180]) + (60 if kind == "quarterly" else 0)
            done = s + timedelta(minutes=lab + r.randint(0, 40))
            tech = r.choice([t[0] for t in TECHS_K])
            part = "FLT-HYD-10" if kind == "quarterly" and r.random() < 0.7 else ""
            rows.append([iso_local(due), m["cmms"], "PM", "3", "מתוכנן", shift_of(s), iso_local(s),
                         iso_local(done), tech, title, r.choice(acts), "", "", part, lab, "סגור", tech])
    for prefix, count, every in (("KN-DR-", 6, 1), ("KN-CH-", 3, 3), ("KN-CP-", 2, 1)):
        for i in range(1, count + 1):
            for month in range(1, 13, every):
                s = random_working_time(r, datetime(2026, month, 3), datetime(2026, month, 25))
                tech = r.choice([t[0] for t in TECHS_K])
                rows.append([iso_local(datetime(2026, month, 3, 7, 0)), f"{prefix}{i:02d}", "PM", "3", "מתוכנן",
                             shift_of(s), iso_local(s), iso_local(s + timedelta(minutes=60)), tech,
                             "טיפול מונע", "בוצע", "", "", "", 60, "סגור", tech])
    for asset, d in (("KN-CR-01", datetime(2026, 4, 14, 9)), ("KN-CR-02", datetime(2026, 4, 14, 11)),
                     ("KN-CP-01", datetime(2026, 2, 9, 9)), ("KN-CP-02", datetime(2026, 2, 9, 11))):
        rows.append([iso_local(d), asset, "INS", "2", "ממונה בטיחות", "morning", iso_local(d),
                     iso_local(d + timedelta(hours=2)), "", "בדיקת בודק מוסמך", "בוצע, תסקיר בתיק", "", "", "",
                     "", "סגור", "vladimir.k"])
    return rows


def _cm_rows(r) -> list[list]:
    texts = ["להחליף צינור בטיפול הבא", "לבדוק רעש בטוגל", "להזמין גוף חימום רזרבי", "לצבוע קווי בטיחות",
             "לתקן מגן צד", "להחליף נורת סימון", "רטיבות בלוח - לבדוק", "לכייל מד לחץ"]
    rows = []
    ks = [m for m in machines() if m["plant"] == "K"]
    for _ in range(190):
        m = r.choice(ks)
        s = random_working_time(r, YEAR_START, YEAR_END - timedelta(days=3))
        done = s + timedelta(days=r.randint(0, 20), minutes=r.randint(30, 240))
        tech = r.choice([t[0] for t in TECHS_K])
        rows.append([iso_local(s), m["cmms"], "CM", "3", "טכנאי", shift_of(s), "", iso_local(done), tech,
                     r.choice(texts), r.choice(VAGUE_ACTIONS + ["בוצע"]), "", "", "", "", "סגור", tech])
    return rows
