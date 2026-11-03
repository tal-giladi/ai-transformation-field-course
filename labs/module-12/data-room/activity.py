"""Time entries for Q3 2026 (Litigation, Tech & IP, International desk) and 2026 hours for everyone."""
from __future__ import annotations

from datetime import date

import textbank as tb
from common import HALF_DAYS, ROOM, rng, workdays, write_csv

RESEARCH_TOPICS = {
    "Litigation": ["agreed-compensation", "force-majeure", "liability-cap", "non-compete"],
    "Tech & IP": ["data-processing", "liability-cap", "non-compete"],
    "Corporate": ["negotiation-good-faith", "liability-cap", "data-processing"],
}
OTHER_TOPICS = {"he": ["חוזה הפצה", "הסכם בעלי מניות", "תביעת עובד", "רישוי תוכנה", "הסכם השקעה"],
                "en": ["distribution agreement", "shareholders' agreement", "licensing", "investment round", "SPA"]}
TASKS_ASSOC = {"research": 0.24, "DRF": 0.29, "REV": 0.17, "COR": 0.12, "MTG": 0.09, "X": 0.09}
TASKS_PARTNER = {"research": 0.05, "DRF": 0.14, "REV": 0.28, "COR": 0.21, "MTG": 0.20, "X": 0.12}


def in_extract(l) -> bool:
    return l["group"] in ("Litigation", "Tech & IP") or l["desk"] == "International"


def build_time_entries(lawyers, matters) -> list[list]:
    r = rng("time")
    days = workdays(date(2026, 7, 1), date(2026, 9, 30))
    topic_names = {t["key"]: (t["he_name"], t["en_name"]) for t in tb.TOPICS}
    rows, n = [], 0
    for l in [x for x in lawyers if in_extract(x)]:
        pool_group = "Corporate" if l["desk"] == "International" else l["group"]
        pool = [m for m in matters if m["group"] == pool_group and m["has26"]
                and (pool_group != "Corporate" or m["desk"] == "International")]
        if l["role"] != "associate":
            mine = [m for m in pool if m["partner"] == l["id"]]
            pool_l = mine + r.sample(pool, min(4, len(pool)))
        else:
            pool_l = r.sample(pool, min(r.randint(5, 9), len(pool)))
            shm = [m for m in pool if m["partner"] == "L002"]
            if l["group"] == "Litigation" and shm:
                pool_l += r.sample(shm, min(2, len(shm)))
        vacation = set(r.sample([d for d in days if d.month in (7, 8)], r.randint(5, 9)))
        daily = l["h2025"] * 0.955 / 224
        tasks = TASKS_ASSOC if l["role"] == "associate" else TASKS_PARTNER
        lang_he = 0.1 if l["desk"] == "International" else 0.8
        total = 0.0
        for d in days:
            if d in vacation:
                continue
            h = max(0.5, min(11.5, r.gauss(daily, 1.1))) * (0.6 if d in HALF_DAYS else 1.0)
            k = r.choices([1, 2, 3, 4], [2, 4, 3, 1])[0]
            cuts = sorted(r.random() for _ in range(k - 1))
            parts = [b - a for a, b in zip([0] + cuts, cuts + [1])]
            for p in parts:
                hours = round(max(0.2, h * p), 1)
                m = r.choice(pool_l)
                lang = "he" if r.random() < lang_he else "en"
                task = r.choices(list(tasks), list(tasks.values()))[0]
                if task == "research":
                    topic = topic_names[r.choice(RESEARCH_TOPICS[pool_group])][0 if lang == "he" else 1]
                    if l["role"] == "associate":
                        code = r.choices(["RES", "DRF_R", "REV_R"], [0.25, 0.55, 0.20])[0]
                    else:
                        code = r.choices(["RES", "REV_R"], [0.7, 0.3])[0]
                    narr = r.choice(tb.NARR[(code, lang)]).format(t=topic)
                else:
                    code = task if task != "X" else ("CRT" if l["group"] == "Litigation" else "NEG")
                    narr = r.choice(tb.NARR[(code, lang)])
                    if code in ("DRF", "REV") and r.random() < 0.4:
                        narr += f" - {r.choice(OTHER_TOPICS[lang])}"
                act = {"DRF_R": "DRF", "REV_R": "REV"}.get(code, code)
                billed, wo, reason = hours, 0.0, ""
                if m["type"] == "fixed":
                    billed, wo, reason = None, None, "fixed-fee matter"
                else:
                    if code == "RES":
                        p_wo = 0.75 if m["partner"] == "L002" else 0.42
                        if r.random() < p_wo:
                            wo, reason = hours, "research - junior time" if l["role"] == "associate" else "partner discretion"
                    elif code in ("DRF_R", "REV_R"):
                        if r.random() < 0.15:
                            wo, reason = round(hours * r.uniform(0.5, 1.0), 1), "partner discretion"
                    elif r.random() < 0.04:
                        wo, reason = round(hours * r.uniform(0.3, 1.0), 1), "partner discretion"
                    if m["type"] == "capped" and d.month == 9 and r.random() < 0.25:
                        wo, reason = hours, "over cap"
                    if m["type"] == "retainer" and reason != "over cap":
                        wo, reason = (0.0, "") if r.random() < 0.97 else (wo, reason)
                    billed = round(hours - wo, 1)
                n += 1
                rows.append([f"E-{n:06d}", d.isoformat(), l["id"], l["role"], l["group"], m["id"], m["type"],
                             act, hours, narr, l["rate"], billed, wo, reason])
                total += hours
        l["q3"] = round(total, 1)
    return rows


def set_2026_hours(lawyers) -> None:
    r = rng("h2026")
    for l in lawyers:
        if "q3" in l:
            l["h2026"] = round(l["q3"] * r.uniform(3.0, 3.15))
        else:
            l["h2026"] = round(l["h2025"] * 0.955 * 0.75 * r.uniform(0.95, 1.05))


def write_time(rows) -> None:
    write_csv(ROOM / "billing" / "time-entries-2026-q3.csv",
              ["entry_id", "work_date", "lawyer_id", "role", "practice_group", "matter_id", "billing_type",
               "activity_code", "hours", "narrative", "rate_ils", "billed_hours", "written_off_hours",
               "writeoff_reason"], rows)
