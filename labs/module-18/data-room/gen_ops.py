"""Inquiries, adviser contacts, LMS activity and risk scores (Tzurim Academic College data room).

Reading this spoils the capstone: submit your deliverables first.
"""
from __future__ import annotations

from datetime import date, timedelta

from gen_common import (EI_SCORE_DATE, SEM_A_GRADES, SEM_A_REG_CLOSE, SEM_B_REG_CLOSE, add_workdays,
                        any_hour, iso_local, pick_name, rng, weighted, work_hour, write_csv, ymd)
from textbank import ADVISER_NOTES, COURSES_EN, COURSES_HE, INQ

CATEGORY = {  # topic -> (category the student picks, weight) options
    "block": [("exams", 50), ("finance", 35), ("other", 15)],
    "block_debt": [("finance", 60), ("exams", 30), ("other", 10)],
    "followup": [("exams", 50), ("finance", 40), ("other", 10)],
    "payment_plan": [("finance", 90), ("other", 10)],
    "certificate": [("certificates", 92), ("other", 8)],
    "appeal": [("exams", 95), ("academic", 5)],
    "accommodation": [("accommodations", 70), ("exams", 30)],
    "reservist": [("reserve duty", 75), ("exams", 25)],
    "lms": [("technical", 90), ("other", 10)],
    "registration": [("academic", 85), ("other", 15)],
    "other": [("other", 100)],
}
FIRST_UNIT = {"exams": "exams office", "finance": "finance - collections", "certificates": "student administration",
              "accommodations": "accessibility unit", "reserve duty": "reservist desk", "technical": "IT helpdesk",
              "academic": "student administration", "other": "student administration"}
RESOLVER = {"block": "finance - collections", "block_debt": "finance - collections", "followup": "finance - collections",
            "payment_plan": "finance - collections", "certificate": "student administration", "appeal": "exams office",
            "accommodation": "accessibility unit", "reservist": "reservist desk", "lms": "IT helpdesk",
            "registration": "student administration", "other": "student administration"}
BASE_DAYS = {"student administration": (1, 3), "exams office": (2, 5), "finance - collections": (3, 9),
             "accessibility unit": (3, 8), "reservist desk": (1, 4), "IT helpdesk": (0, 2)}


def _text(r, topic: str, lang: str, block_close: date | None) -> str:
    lang = lang if lang in ("he", "ar", "en", "ru") else "he"
    tpl = r.choice(INQ[topic][lang])
    course = r.choice(COURSES_EN if lang == "en" else COURSES_HE)
    return tpl.format(course=course, date=(block_close or date(2026, 1, 11)).strftime("%d/%m"),
                      amount=r.randint(16, 90) * 100, days=r.randint(12, 60))


def _inquiry(r, s, topic, opened, rows, counter, unblock=None):
    cat = weighted(r, CATEGORY[topic])
    first = FIRST_UNIT[cat]
    resolver = RESOLVER[topic]
    reassign = 0 if first == resolver else (1 if r.random() < 0.8 else 2)
    lo, hi = BASE_DAYS[resolver]
    days = r.randint(lo, hi) + sum(r.randint(3, 8) for _ in range(reassign))
    lang = s["lang"] if s["lang"] in ("he", "ar", "en", "ru") else "he"
    if lang == "ar":
        days += r.randint(1, 3)
    reply_lang = "en" if lang == "en" else ("ar" if lang == "ar" and r.random() < 0.07 else "he")
    closed = work_hour(r, add_workdays(opened.date(), days))
    if unblock and topic in ("block", "block_debt", "followup") and r.random() < 0.7:
        closed = work_hour(r, max(unblock, opened.date() + timedelta(days=1)))
    reopen_p = {"ar": 0.27, "ru": 0.14}.get(lang, 0.07) + (0.1 if reassign else 0)
    counter[0] += 1
    status = "open" if closed.date() > date(2026, 9, 30) else "closed"
    rows.append([f"INQ-{2500000 + counter[0] * 7}", iso_local(opened), weighted(r, [("portal", 70), ("email", 22), ("whatsapp", 8)]),
                 s["no"], cat, _text(r, topic, lang, SEM_A_REG_CLOSE if opened.month < 3 else SEM_B_REG_CLOSE),
                 first, reassign, resolver, reply_lang, "" if status == "open" else iso_local(closed),
                 "Y" if r.random() < reopen_p else "N", status])


def inquiries(students: list[dict]) -> None:
    r = rng(10)
    rows, counter = [], [0]
    active = [s for s in students if s["fin"]]
    for s in active:
        for sem in ("A", "B"):
            f = s["fin"].get(sem)
            if not f or not f["blocked"] or r.random() > 0.55:
                continue
            topic = "block" if f["cause"] == "scholarship_not_posted" else "block_debt"
            opened = any_hour(r, f["block_date"] + timedelta(days=r.randint(1, 7)))
            _inquiry(r, s, topic, opened, rows, counter, f["unblock_date"])
            if r.random() < 0.22:
                _inquiry(r, s, "followup", opened + timedelta(days=r.randint(3, 6)), rows, counter, f["unblock_date"])
    topics = [("certificate", 26), ("appeal", 14), ("accommodation", 9), ("reservist", 12), ("lms", 10),
              ("registration", 15), ("payment_plan", 6), ("other", 8)]
    reservists = [s for s in active if s["reservist"]]
    for _ in range(1480):
        topic = weighted(r, topics)
        s = r.choice(reservists if topic == "reservist" else active)
        d = date(2025, 11, 2) + timedelta(days=r.randint(0, 255))
        _inquiry(r, s, topic, any_hour(r, d), rows, counter)
    rows.sort(key=lambda x: x[1])
    write_csv("inquiries/student-inquiries-2025-26.csv",
              ["inquiry_id", "opened_at", "channel", "student_no", "category_selected", "text", "first_unit",
               "reassignments", "resolved_unit", "reply_language", "closed_at", "reopened", "status"], rows)


def _accommodations(students):
    r = rng(11)
    for s in students:
        s["accom"] = r.random() < 0.09
        months = ["2025-11", "2025-12", "2026-01", "2026-02", "2026-03"]
        s["res_months"] = set(r.sample(months, r.choice((1, 2, 2, 3)))) if s["reservist"] else set()


def lms_and_scores(students: list[dict]) -> list[dict]:
    r = rng(12)
    _accommodations(students)
    first = [s for s in students if s["cohort"] == 2025]
    months = [("2025-11", date(2025, 11, 30)), ("2025-12", date(2025, 12, 31)), ("2026-01", date(2026, 1, 31)),
              ("2026-02", date(2026, 2, 28)), ("2026-03", date(2026, 3, 31))]
    rows, scored = [], []
    for s in first:
        leaver = s["cur"] in ("51", "52", "58")
        base = {"regular": 24, "evening": 16, "haredi": 7}[s["track"]]
        recs = []
        for m, end in months:
            if leaver and s["cur_date"] and end - timedelta(days=30) > s["cur_date"]:
                break
            mu = base * (0.25 if m in s["res_months"] else 1.0)
            if leaver and s["cur_date"] and (s["cur_date"] - end).days < 45:
                mu *= 0.6
            logins = max(0, int(r.gauss(mu, mu * 0.3)))
            due = r.randint(2, 5)
            on_time = sum(1 for _ in range(due) if r.random() < (0.55 if m in s["res_months"] else 0.85))
            recs.append((m, logins, on_time, due))
            rows.append([s["no"], m, logins, logins * r.randint(9, 25), due, on_time,
                         r.randint(0, 3) if s["track"] != "haredi" else r.randint(0, 1)])
        if s["cur_date"] and s["cur_date"] < EI_SCORE_DATE and leaver:
            continue
        jf = [x for x in recs if x[0] in ("2026-01", "2026-02")]
        avg = sum(x[1] for x in jf) / max(1, len(jf))
        late = sum(x[3] - x[2] for x in jf)
        score = max(0, min(100, int(78 - 2.1 * avg + 6 * late + r.gauss(0, 7))))
        drivers = []
        if avg < 12:
            drivers.append("Low LMS activity")
        if late >= 2:
            drivers.append("Late or missing submissions")
        if s["res_months"] & {"2026-01", "2026-02"}:
            drivers.append("Reserve-duty absence (accommodations module)")
            score = min(100, score + 8)
        if s["accom"]:
            drivers.append("Medical or learning accommodation on file (accommodations module)")
            score = min(100, score + 10)
        if not drivers:
            drivers.append("Low forum participation")
        band = "red" if score >= 70 else ("amber" if score >= 45 else "green")
        s["ei"] = (score, band, drivers)
        scored.append([s["no"], s["prog"], ymd(EI_SCORE_DATE), score, band] + (drivers + ["", "", ""])[:3] + ["EI-2026.2"])
    write_csv("lms/tavla-activity-monthly-first-year-2025-26.csv",
              ["student_no", "month", "logins", "active_minutes", "submissions_due", "submissions_on_time",
               "forum_posts"], rows)
    write_csv("lms/engagement-insights-export-2026-03-15.csv",
              ["student_no", "programme_code", "score_date", "risk_score", "band", "driver_1", "driver_2", "driver_3",
               "model_version"], scored)
    return first


def red_list_and_contacts(students: list[dict], first: list[dict]) -> None:
    r = rng(13)
    red = [s for s in first if s.get("ei") and s["ei"][1] == "red"]
    rows = []
    for i, s in enumerate(red):
        fn, ln = pick_name(r, s["lang"])
        rows.append([fn, ln, s["no"], s["prog"], s["ei"][0], "; ".join(s["ei"][2]), f"ADV-0{1 + i % 6}", ""])
    write_csv("student-success/red-list-for-lecturers-2026-03-16.csv",
              ["first_name", "last_name", "student_no", "programme_code", "risk_score", "reasons", "adviser",
               "lecturer_comment"], rows)
    contacts = []
    # early-contact protocol: first-years who missed or failed 2+ semester A exams
    eligible = [s for s in first if s["exams"] and (s["exams"][0][4] - s["exams"][0][5]) + s["exams"][0][8] >= 2]
    for s in eligible:
        if r.random() < 0.23:
            d = SEM_A_GRADES + timedelta(days=r.randint(1, 29))
            contacts.append(_contact(r, s, d, "early_contact"))
    others = [s for s in students if s["fin"]]
    for _ in range(620):
        s = r.choice(others)
        d = date(2025, 11, 2) + timedelta(days=r.randint(0, 240))
        contacts.append(_contact(r, s, d, weighted(r, [("self_referral", 50), ("lecturer_referral", 30), ("admin_referral", 20)])))
    for s in red:
        d = EI_SCORE_DATE + timedelta(days=r.randint(1, 100))
        contacts.append(_contact(r, s, d, "tavla_red"))
        if r.random() < 0.45:
            contacts.append(_contact(r, s, d + timedelta(days=r.randint(5, 20)), "tavla_red"))
    contacts.sort(key=lambda x: (x[1], x[2]))
    for i, c in enumerate(contacts):
        c[0] = f"C-{26000 + i}"
    write_csv("student-success/adviser-contacts-2025-26.csv",
              ["contact_id", "contact_date", "student_no", "adviser", "trigger", "channel", "outcome", "note"], contacts)


def _contact(r, s, d, trigger):
    while d.weekday() in (4, 5):
        d += timedelta(days=1)
    left = s["cur"] in ("51", "52", "58") and s["cur_date"] and s["cur_date"] < d
    if left:
        outcome, note = "left", r.choice(ADVISER_NOTES["left"])
    else:
        x = r.random()
        blocked = s["fin"] and any(s["fin"].get(k) and s["fin"][k]["blocked"] for k in ("A", "B"))
        if x < 0.38:
            outcome, note = "no_answer", r.choice(ADVISER_NOTES["no_answer"])
        elif blocked and x < 0.62:
            outcome, note = "referred_finance", r.choice(ADVISER_NOTES["reached_finance"])
        elif s.get("accom") and x < 0.7:
            outcome, note = "referred_accessibility", r.choice(ADVISER_NOTES["reached_access"])
        elif trigger == "tavla_red" and x > 0.88:
            outcome, note = "student_objected", r.choice(ADVISER_NOTES["objected"])
        else:
            outcome, note = "reached", r.choice(ADVISER_NOTES["reached_ok"])
    return ["", ymd(d), s["no"], f"ADV-0{r.randint(1, 6)}", trigger, weighted(r, [("phone", 70), ("whatsapp", 20), ("meeting", 10)]),
            outcome, note]
