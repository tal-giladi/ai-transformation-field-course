"""IT, staff survey, licences and academic-integrity files (Tzurim Academic College data room).

Reading this spoils the capstone: submit your deliverables first.
"""
from __future__ import annotations

from datetime import date, timedelta

from gen_common import rng, weighted, write_csv, ymd
from textbank import COURSES_HE

UNITS_ADMIN = ["student administration", "finance", "admissions", "student success", "exams office",
               "accessibility unit", "library", "IT", "HR", "management", "marketing"]


def proxy() -> None:
    r = rng(20)
    units = {"student administration": 34, "finance": 22, "admissions": 18, "student success": 9,
             "exams office": 8, "management": 14, "marketing": 11, "IT": 12, "library": 7,
             "faculty offices (senior staff)": 60, "lecturers' Wi-Fi (Staff-Lecturers SSID)": 140}
    domains = [("chatgpt.com", 1.0), ("gemini.google.com", 0.45), ("claude.ai", 0.18), ("copilot.microsoft.com", 0.22),
               ("translate.google.com", 0.5), ("deepl.com", 0.2), ("quillbot.com", 0.15),
               ("AI writing detectors (category, 3 domains)", 0.0)]
    rows = []
    for month in ("2026-06", "2026-07", "2026-08", "2026-09"):
        season = {"2026-06": 1.0, "2026-07": 1.15, "2026-08": 0.35, "2026-09": 0.6}[month]
        for unit, size in units.items():
            lect = unit.startswith("lecturers")
            for dom, weight in domains:
                w = weight
                if dom.startswith("AI writing"):
                    w = 0.3 if lect else (0.08 if unit.startswith("faculty") else 0.0)
                if unit == "student administration" and dom in ("translate.google.com", "chatgpt.com"):
                    w *= 1.8
                if w == 0:
                    continue
                users = max(0, int(size * w * season * r.uniform(0.25, 0.45)))
                if users == 0:
                    continue
                reqs = int(users * r.uniform(40, 160) * (1.6 if lect else 1.0))
                rows.append([month, unit, dom, users, reqs])
    write_csv("it/proxy-ai-summary-2026-06-to-09.csv", ["month", "network_segment", "domain", "distinct_users", "requests"], rows)


def survey() -> None:
    r = rng(21)
    rows = []
    rid = 0
    tools = ["ChatGPT (free)", "ChatGPT Plus (personal)", "Gemini", "Google Translate", "Claude", "the office AI assistant", "DeepL"]
    for role, n in (("administrative", 148), ("senior_faculty", 44), ("adjunct", 84)):
        for _ in range(n):
            rid += 1
            if role == "administrative":
                use = weighted(r, [("never", 62), ("monthly", 17), ("weekly", 14), ("daily", 7)])
                unit = r.choice(UNITS_ADMIN)
            elif role == "senior_faculty":
                use = weighted(r, [("never", 30), ("monthly", 25), ("weekly", 30), ("daily", 15)])
                unit = "faculty"
            else:
                use = weighted(r, [("never", 11), ("monthly", 18), ("weekly", 42), ("daily", 29)])
                unit = "faculty"
            if use == "never":
                rows.append([f"R{rid:03d}", role, unit, use, "", "", "none", weighted(r, [("no", 60), ("not_sure", 30), ("yes", 10)]), ""])
                continue
            t = "; ".join(sorted(set(r.sample(tools, r.randint(1, 3)))))
            if role == "adjunct":
                main = weighted(r, [("feedback on student assignments", 45), ("preparing course materials", 30),
                                    ("checking assignments for AI use", 15), ("emails", 10)])
                data = weighted(r, [("course materials", 35), ("student work without names", 30),
                                    ("student work with names or student numbers", 27), ("none", 8)])
            elif role == "senior_faculty":
                main = weighted(r, [("research writing", 40), ("preparing course materials", 35), ("feedback on student assignments", 25)])
                data = weighted(r, [("course materials", 50), ("unpublished research", 25), ("student work without names", 15), ("none", 10)])
            else:
                main = weighted(r, [("translating student emails", 30), ("writing emails and letters", 35),
                                    ("summarising documents", 20), ("Excel formulas", 15)])
                data = weighted(r, [("none", 40), ("internal documents", 30), ("student personal details", 18),
                                    ("applicant files", 12 if unit == "admissions" else 2)])
            comment = ""
            if r.random() < 0.18:
                comment = r.choice([
                    "אני מקבל 160 עבודות בסמסטר על אותו שכר, בלי זה אין לי איך לתת משוב",
                    "מתרגמת מיילים בערבית כי אין מי שיענה בערבית במזכירות",
                    "No one told us what is allowed. The 2019 IT policy doesn't mention AI.",
                    "בודק עבודות בגלאי AI, אבל לא ברור אם מותר להשתמש בזה כראיה",
                    "I would use an approved tool if the college gave us one",
                    "למה למנהלים יש רישיון ולנו במזכירות לא?",
                ])
            rows.append([f"R{rid:03d}", role, unit, use, t, main, data,
                         weighted(r, [("no", 55), ("not_sure", 30), ("yes", 15)]), comment])
    write_csv("people/staff-ai-survey-2026-06-responses.csv",
              ["respondent", "role", "unit", "uses_ai", "tools", "main_use", "data_entered", "knows_ai_rules", "comment"], rows)


def licences() -> None:
    r = rng(22)
    rows = []
    groups = [("management", "management", 58), ("academic head", "faculty", 22), ("administrative", "student administration", 3),
              ("administrative", "finance", 6), ("administrative", "admissions", 8), ("administrative", "marketing", 11),
              ("IT", "IT", 12)]
    i = 0
    for level, unit, n in groups:
        for _ in range(n):
            i += 1
            x = r.random()
            if x < 0.31:
                days, last = 0, ""
            elif x < 0.81:
                days = r.randint(1, 7)
                last = ymd(date(2026, 10, 31) - timedelta(days=r.randint(0, 60)))
            else:
                days = r.randint(8, 22)
                last = ymd(date(2026, 10, 31) - timedelta(days=r.randint(0, 4)))
            if level == "IT" and days:
                days = max(days, 9)
            rows.append([f"L{i:03d}", level, unit, "2026-03-15", days, last,
                         r.choice(["mail", "documents", "meetings", "chat"]) if days else ""])
    write_csv("it/office-ai-assistant-usage-2026-10.csv",
              ["licence_id", "holder_level", "unit", "assigned_date", "active_days_last_30", "last_active", "top_app"], rows)


def integrity() -> None:
    r = rng(23)
    rows = []
    for i in range(46):
        d = date(2025, 12, 1) + timedelta(days=r.randint(0, 230))
        ev = weighted(r, [("ai_detector_only", 19), ("similarity_report", 11), ("lecturer_judgement", 6),
                          ("student_admitted", 7), ("proctor_report", 3)])
        if ev == "ai_detector_only":
            lang = weighted(r, [("ar", 45), ("ru", 12), ("am", 8), ("he", 35)])
            score = r.randint(62, 99)
            outcome = weighted(r, [("grade_zero", 45), ("warning", 35), ("cleared", 20)])
            appeal = "Y" if r.random() < 0.6 else "N"
            result = ("overturned" if r.random() < 0.65 else "upheld") if appeal == "Y" else ""
        else:
            lang = weighted(r, [("he", 62), ("ar", 22), ("ru", 10), ("en", 6)])
            score = ""
            outcome = weighted(r, [("grade_zero", 40), ("warning", 30), ("suspension", 10), ("cleared", 20)])
            appeal = "Y" if r.random() < 0.3 else "N"
            result = ("upheld" if r.random() < 0.75 else "overturned") if appeal == "Y" else ""
        rows.append([f"AI-{2600 + i}", ymd(d), r.choice(["BA-BUS", "BA-BEH", "BSC-CS", "BA-COM", "LLB", "BSC-IEM"]),
                     r.choice(COURSES_HE), ev, score, lang, outcome, appeal, result])
    rows.sort(key=lambda x: x[1])
    write_csv("academic/integrity-cases-2025-26.csv",
              ["case_id", "opened_date", "programme_code", "course", "evidence", "detector_score_pct",
               "student_first_language", "outcome", "appealed", "appeal_result"], rows)


def systems() -> None:
    write_csv("it/systems-and-contracts.csv",
              ["system", "what_it_does", "vendor_or_owner", "hosting", "contract_end", "ai_features_per_vendor_docs",
               "dpa_signed", "owner"], [
        ["Rishum 2 (SIS)", "Student records, registration, exam registration, status codes", "In-house (IT), live since Aug 2024",
         "College data centre", "", "None", "n/a", "Registrar"],
        ["Rishum (old SIS)", "Student records before Aug 2024 (read-only)", "In-house", "College data centre", "", "None", "n/a", "IT"],
        ["Finance ERP", "Tuition accounts, payment plans, collections, blocks", "Local ERP integrator", "Vendor cloud (Israel)",
         "2028-12-31", "None", "Y (2021)", "VP Finance"],
        ["Tavla LMS", "Courses, submissions, grades book, forums, accommodations module", "Tavla Learning Ltd.",
         "Vendor cloud (EU region)", "2027-08-31", "Engagement Insights (release 2026.2); AI quiz generator (opt-in)",
         "Y (2022, before release 2026.2)", "IT"],
        ["Inquiry portal", "Student inquiries, routing to units", "In-house (IT)", "College data centre", "", "None", "n/a", "Student administration"],
        ["Admissions CRM", "Leads, applicants, interviews", "CRM vendor", "Vendor cloud (US region)", "2027-12-31",
         "Lead scoring ('predictive score'), email drafting assistant", "Y (2023)", "Head of admissions"],
        ["Office suite", "Email, documents, meetings", "Office suite vendor", "Vendor cloud", "2027-06-30",
         "AI assistant add-on: 120 licences from March 2026", "Y", "IT"],
        ["Survey tool", "Course evaluations, staff surveys", "Survey SaaS", "Vendor cloud (US region)", "2027-03-31",
         "Open-text summaries (on by default since 2025)", "N", "Quality unit"],
        ["WhatsApp Business", "Admissions and student-administration messages", "Messaging platform", "Vendor cloud", "", "None used", "N", "Admissions"],
    ])


def build() -> None:
    proxy()
    survey()
    licences()
    integrity()
    systems()
