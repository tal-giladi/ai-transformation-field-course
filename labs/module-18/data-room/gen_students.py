"""Students, statuses, tuition accounts and exam periods (Tzurim Academic College data room).

Reading this spoils the capstone: submit your deliverables first.
"""
from __future__ import annotations

from datetime import date, timedelta

from gen_common import (COHORTS, PROGRAMMES, SEM_A_BLOCK_CHECK, SEM_A_EXAMS, SEM_A_REG_CLOSE,
                        SEM_B_BLOCK_CHECK, SEM_B_EXAMS, SEM_B_REG_CLOSE, TUITION, add_workdays, rng,
                        weighted, write_csv, ymd)

LEAVE_CODES = (("51", 0.38), ("52", 0.52), ("58", 0.10))


def _student_numbers(r, cohort: int, n: int) -> list[str]:
    if cohort == 2023:  # old SIS: 8 digits starting with 1
        seq = r.sample(range(2300000, 2399999), n)
        return [f"1{s}" for s in sorted(seq)]
    seq = r.sample(range(100000, 999999), n)  # new SIS (Aug 2024): 0 + yy + 6 digits
    return [f"0{cohort % 100}{s}" for s in sorted(seq)]


def _population() -> list[dict]:
    r = rng(1)
    students = []
    for cohort, n in COHORTS.items():
        for no in _student_numbers(r, cohort, n):
            prog = weighted(r, [(p[0], p[2]) for p in PROGRAMMES])
            haredi_ok = next(p[4] for p in PROGRAMMES if p[0] == prog)
            x = r.random()
            track = "haredi" if haredi_ok and x < 0.12 else ("evening" if x > 0.88 else "regular")
            if track == "haredi":
                lang = weighted(r, [("he", 95), ("en", 3), ("ru", 2)])
            else:
                lang = weighted(r, [("he", 55), ("ar", 25), ("ru", 10), ("am", 4), ("en", 3), ("other", 3)])
            p_res = 0.02 if track == "haredi" else (0.03 if lang == "ar" else 0.19)
            students.append({
                "no": no, "cohort": cohort, "prog": prog, "track": track, "lang": lang,
                "lang_field": "" if r.random() < 0.04 else lang,
                "reservist": r.random() < p_res,
                "ext_schol": r.random() < (0.19 if lang == "ar" else 0.10),
                "y1": "", "y1_date": None, "cur": "", "cur_date": None, "transfer_to": "",
                "active_2526": False, "fin": None, "exams": [],
            })
    return students


def _year1_snapshot(s: dict, r) -> None:
    """Status after the first year for cohorts 2023 and 2024 (taken before 2025-26)."""
    c = s["cohort"]
    snap = date(c + 1, 10, 1)
    x = r.random()
    if s["reservist"] and x < 0.31:
        s["y1"] = "41" if c == 2023 else "47"
    elif x < 0.012 + (0.31 if s["reservist"] else 0):
        s["y1"] = "41"
    elif r.random() < 0.016:
        s["y1"] = "33"
        others = [p[0] for p in PROGRAMMES if p[0] != s["prog"]]
        s["transfer_to"] = r.choice(others)
    else:
        p_leave = {"regular": 0.118, "evening": 0.165, "haredi": 0.15}[s["track"]]
        if r.random() < p_leave:
            s["y1"] = weighted(r, LEAVE_CODES)
        else:
            s["y1"] = "21" if r.random() < 0.06 else "10"
    s["y1_date"] = snap - timedelta(days=r.randint(0, 120)) if s["y1"] not in ("10", "21") else snap
    if s["y1"] in ("10", "21", "33"):
        s["active_2526"] = True
    elif s["y1"] in ("41", "47"):
        s["active_2526"] = r.random() < 0.62  # most frozen students came back
    s["cur"], s["cur_date"] = s["y1"], s["y1_date"]


def _late_posting(r, start: date, latest: date) -> date:
    return start + timedelta(days=r.randint(0, (latest - start).days))


def _semester(s: dict, r, check: date, reg_close: date, exams: tuple, sem: str) -> dict:
    """One semester's block check, unblock and exam registration for an active student."""
    f = s["fin"]
    late_res = s["reservist"] and r.random() < (0.56 if sem == "A" else 0.16)
    late_ext = s["ext_schol"] and r.random() < (0.36 if sem == "A" else 0.10)
    arrears = 0
    p_arrears = {"none": 0.30, "standing_order": 0.05, "credit_10": 0.04, "arrangement": 0.12}[f["plan"]]
    if r.random() < p_arrears:
        arrears = r.randint(16, 90) * 100
    owed_schol = (f["res_grant"] if late_res else 0) + (f["ext_amount"] if late_ext else 0)
    balance = arrears + owed_schol
    out = {"balance": balance if balance > 0 else 0, "blocked": balance > 1500, "block_date": None,
           "unblock_date": None, "unblock_reason": "", "posted": None, "cause": "", "arrears": arrears}
    if late_res or late_ext:
        out["posted"] = _late_posting(r, check + timedelta(days=3), check + timedelta(days=32))
    if not out["blocked"]:
        return out
    out["block_date"] = check
    out["cause"] = "scholarship_not_posted" if arrears == 0 else ("arrears" if owed_schol == 0 else "both")
    if arrears == 0:
        manual = add_workdays(check, r.randint(2, 12)) if r.random() < 0.6 else None
        cands = [d for d in (out["posted"], manual) if d]
        out["unblock_date"] = min(cands)
        out["unblock_reason"] = "scholarship_posted" if out["unblock_date"] == out["posted"] else "manual"
    else:
        y = r.random()
        if y < 0.38:
            out["unblock_date"], out["unblock_reason"] = check + timedelta(days=r.randint(1, 20)), "paid"
        elif y < 0.84:
            req = check + timedelta(days=r.randint(0, 6))
            out["unblock_date"], out["unblock_reason"] = add_workdays(req, r.randint(3, 16)), "arrangement"
        if owed_schol and out["unblock_date"] and out["posted"] and out["posted"] > out["unblock_date"]:
            out["unblock_date"] = out["posted"]
    return out


def _exams(s: dict, r, sem: dict, reg_close: date, period: tuple, label: str, leaver: bool) -> list:
    n = r.choice((5, 6, 6))
    u = sem["unblock_date"]
    if not sem["blocked"] or (u and u <= reg_close):
        reg = n
    elif u and u < period[1] - timedelta(days=3):
        frac = (period[1] - u).days / (period[1] - period[0]).days
        reg = max(0, min(n, round(n * frac * 0.7)))
    else:
        reg = 0
    sat = sum(1 for _ in range(reg) if r.random() > (0.12 if leaver else 0.05))
    passed = sum(1 for _ in range(sat) if r.random() < (0.62 if leaver else 0.87))
    return [s["no"], s["cohort"], s["prog"], label, n, reg, sat, passed, sat - passed]


def _year_2526(students: list[dict]) -> None:
    r = rng(2)
    for s in students:
        if s["cohort"] == 2025:
            s["active_2526"] = True
        if not s["active_2526"]:
            continue
        plan = weighted(r, [("standing_order", 55), ("credit_10", 25), ("none", 14), ("arrangement", 6)])
        s["fin"] = {"plan": plan, "tuition": TUITION[s["prog"]],
                    "res_grant": r.randint(10, 18) * 500 if s["reservist"] else 0,
                    "ext_amount": r.randint(6, 20) * 500 if s["ext_schol"] else 0}
        year = 2026 - s["cohort"]  # 1, 2 or 3
        s["fin"]["A"] = _semester(s, r, SEM_A_BLOCK_CHECK, SEM_A_REG_CLOSE, SEM_A_EXAMS, "A")
        a = s["fin"]["A"]
        missed_a = a["blocked"] and (a["unblock_date"] is None or a["unblock_date"] > SEM_A_REG_CLOSE)
        x = r.random()
        if s["cohort"] == 2025 and s["reservist"] and x < 0.36:
            outcome = "47"
        elif s["cohort"] == 2025 and x < 0.012 + (0.36 if s["reservist"] else 0):
            outcome = "41"
        elif s["cohort"] == 2025 and r.random() < 0.015:
            outcome = "33"
            s["transfer_to"] = r.choice([p[0] for p in PROGRAMMES if p[0] != s["prog"]])
        else:
            base = {1: 0.071, 2: 0.034, 3: 0.02}[year] * {"regular": 1.0, "evening": 1.35, "haredi": 1.2}[s["track"]]
            if missed_a:
                base += {1: 0.33, 2: 0.13, 3: 0.08}[year]
            elif a["blocked"]:
                base += 0.02
            outcome = weighted(r, LEAVE_CODES) if r.random() < base else ("21" if r.random() < 0.05 else "10")
        left_after_a = outcome in ("51", "52", "58") and (missed_a or r.random() < 0.3)
        s["leave_after_a"] = left_after_a
        if not left_after_a and outcome not in ("41", "47"):
            s["fin"]["B"] = _semester(s, r, SEM_B_BLOCK_CHECK, SEM_B_REG_CLOSE, SEM_B_EXAMS, "B")
        if outcome in ("10", "21"):
            s["cur_date"] = date(2026, 10, 1)
        elif left_after_a:
            s["cur_date"] = date(2026, 2, 15) + timedelta(days=r.randint(0, 50))
        else:
            s["cur_date"] = date(2026, 7, 20) + timedelta(days=r.randint(0, 70))
        s["cur"] = outcome
        if s["cohort"] == 2025:
            s["y1"], s["y1_date"] = outcome, s["cur_date"]
        if s["cohort"] == 2025:
            leaver = outcome in ("51", "52", "58")
            s["exams"].append(_exams(s, r, a, SEM_A_REG_CLOSE, SEM_A_EXAMS, "2026A", leaver))
            if "B" in s["fin"]:
                s["exams"].append(_exams(s, r, s["fin"]["B"], SEM_B_REG_CLOSE, SEM_B_EXAMS, "2026B", leaver))


def build() -> list[dict]:
    students = _population()
    r = rng(3)
    for s in students:
        if s["cohort"] in (2023, 2024):
            _year1_snapshot(s, r)
    _year_2526(students)
    _write(students)
    return students


def _write(students: list[dict]) -> None:
    rows = []
    for s in students:
        rows.append([s["no"], s["cohort"], s["prog"], s["track"], s["lang_field"], "Y" if s["reservist"] else "",
                     s["y1"], ymd(s["y1_date"]), s["cur"], ymd(s["cur_date"]), s["transfer_to"]])
    write_csv("students/registry-students-2023-2025.csv",
              ["student_no", "cohort_year", "programme_code", "track", "first_language", "reservist_status",
               "status_after_year1", "status_after_year1_date", "current_status", "current_status_date",
               "transferred_to"], rows)
    fin_rows = []
    r = rng(4)
    for s in students:
        f = s["fin"]
        if not f:
            continue
        a, b = f["A"], f.get("B")
        bad_debt = ""
        if s["cur"] in ("51", "52", "58") and a["cause"] in ("arrears", "both") and r.random() < 0.7:
            bad_debt = a["arrears"]
        schol = f["res_grant"] + f["ext_amount"]
        posted = min([d for d in (a["posted"],) if d], default=None)
        fin_rows.append([
            str(int(s["no"])), "2025-26", f["tuition"], schol or "", ymd(posted) if posted else ("" if not schol else "2025-11-30"),
            f["plan"], a["balance"], "Y" if a["blocked"] else "N", ymd(a["block_date"]), ymd(a["unblock_date"]),
            a["unblock_reason"],
            "" if b is None else b["balance"], "" if b is None else ("Y" if b["blocked"] else "N"),
            "" if b is None else ymd(b["block_date"]), "" if b is None else ymd(b["unblock_date"]),
            bad_debt,
        ])
    write_csv("finance/tuition-accounts-2025-26.csv",
              ["student_no", "academic_year", "annual_tuition_nis", "scholarships_nis", "scholarship_posted_date",
               "payment_plan", "balance_at_check_A", "blocked_A", "block_date_A", "unblock_date_A",
               "unblock_reason_A", "balance_at_check_B", "blocked_B", "block_date_B", "unblock_date_B",
               "written_off_nis"], fin_rows)
    ex = [row for s in students for row in s["exams"]]
    write_csv("students/exam-periods-first-year-2025-26.csv",
              ["student_no", "cohort_year", "programme_code", "exam_period", "exams_in_plan", "exams_registered",
               "exams_sat", "exams_passed", "exams_failed"], ex)
    write_csv("students/status-codes.csv", ["code", "name_he", "name_en", "counts_as_active", "added"], [
        ["10", "פעיל", "Active", "Y", "2019-07-01"],
        ["21", "פעיל - על תנאי", "Active - academic probation", "Y", "2019-07-01"],
        ["33", "עבר תוכנית", "Transferred to another programme in the college", "N", "2019-07-01"],
        ["41", "הקפאת לימודים", "Studies frozen", "N", "2019-07-01"],
        ["47", "הקפאה - מילואים", "Studies frozen - reserve duty", "N", "2024-11-03"],
        ["51", "הפסיק לימודים - בהודעה", "Withdrew (gave notice)", "N", "2019-07-01"],
        ["52", "לא נרשם לשנה הבאה", "Did not register for the next year", "N", "2019-07-01"],
        ["58", "הופסקו לימודיו - אקדמי", "Discontinued (academic)", "N", "2019-07-01"],
        ["60", "סיים לימודים", "Graduated", "N", "2019-07-01"],
        ["99", "אחר", "Other", "N", "2019-07-01"],
    ])
