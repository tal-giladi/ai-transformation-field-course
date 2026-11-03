"""ai/assistant-usage-2026.csv, branches/branch-faq-usage-2026-q4.csv,
security/proxy-ai-hosts-2026-q4.csv, finance/card-and-expense-software-2026.csv."""
from datetime import date, timedelta

from gen_common import rng, write_csv, days, is_workday


def assistant_usage() -> int:
    r = rng(10)
    # department: (pilot seats from 3 May, seats from 29 Nov, weekly active share pilot users, share new)
    depts = {
        "Operations - back office": (120, 380, 0.74, 0.05),
        "Contact Centre": (110, 420, 0.69, 0.05),
        "Branches": (0, 520, 0.0, 0.05),
        "HQ - Finance": (15, 60, 0.33, 0.05),
        "HQ - HR": (15, 50, 0.27, 0.05),
        "HQ - Corporate Banking": (20, 80, 0.35, 0.05),
        "HQ - Mortgages": (15, 60, 0.30, 0.05),
        "HQ - other": (5, 30, 0.20, 0.05),
    }
    studio = {"Operations - back office": 118, "Contact Centre": 110}
    header = ["week_start", "department", "seats_assigned", "users_onboarded", "weekly_active_users",
              "prompts", "agent_studio_sessions"]
    rows = []
    wk = date(2026, 5, 3)
    while wk <= date(2026, 12, 27):
        big = wk >= date(2026, 11, 29)
        for d, (s0, s1, a_old, a_new) in depts.items():
            seats = s1 if big else s0
            if seats == 0:
                continue
            ramp = min(1.0, ((wk - date(2026, 5, 3)).days / 7 + 1) / 6)
            old_active = round(s0 * a_old * ramp * r.uniform(0.92, 1.06))
            new_active = round((s1 - s0) * a_new * r.uniform(0.85, 1.1)) if big else 0
            active = old_active + new_active
            onboarded = s0 + (round((s1 - s0) * 0.06) if big else 0)
            prompts = round(active * r.uniform(17, 26))
            ss = 0
            if d in studio and wk >= (date(2026, 6, 7) if d.startswith("Oper") else date(2026, 7, 5)):
                ss = round(studio[d] * r.uniform(5.5, 8.0))
            rows.append([wk.isoformat(), d, seats, onboarded, active, prompts, ss])
        wk += timedelta(days=7)
    return write_csv("ai/assistant-usage-2026.csv", header, rows)


BRANCHES = [
    ("101", "Haifa Hadar"), ("102", "Haifa Neve Sha'anan"), ("104", "Kiryat Ata"), ("106", "Akko"),
    ("107", "Nahariya"), ("109", "Karmiel"), ("111", "Nazareth"), ("112", "Nof HaGalil"),
    ("114", "Afula"), ("115", "Tiberias"), ("117", "Shfar'am"), ("118", "Sakhnin"),
    ("121", "Umm al-Fahm"), ("123", "Hadera"), ("125", "Netanya"), ("127", "Kfar Saba"),
    ("128", "Ra'anana"), ("130", "Herzliya"), ("132", "Tel Aviv Allenby"), ("133", "Tel Aviv Ibn Gabirol"),
    ("135", "Ramat Gan Bialik"), ("136", "Petah Tikva"), ("138", "Holon"), ("139", "Bat Yam"),
    ("141", "Rishon LeZion"), ("142", "Rehovot"), ("144", "Ashdod"), ("146", "Lod"),
    ("147", "Modi'in"), ("150", "Jerusalem Talpiot"), ("152", "Beit Shemesh"),
]
TOPICS = ["fees", "fees", "standing orders", "forms", "foreign currency", "cheques",
          "account opening", "power of attorney", "loans", "cards"]


def branch_faq() -> int:
    r = rng(11)
    header = ["date", "branch_code", "branch_name", "questions", "answered_with_source",
              "thumbs_down", "top_topic"]
    rows = []
    size = {code: r.uniform(0.6, 1.5) for code, _ in BRANCHES}
    for d in days(date(2026, 10, 1), date(2026, 12, 31)):
        if not is_workday(d):
            continue
        for code, name in BRANCHES:
            q = max(1, round(12 * size[code] * r.uniform(0.6, 1.4)))
            fee_week = date(2026, 11, 8) <= d <= date(2026, 11, 26)
            down = sum(1 for _ in range(q) if r.random() < (0.09 if fee_week else 0.035))
            src = q - sum(1 for _ in range(q) if r.random() < 0.06)
            topic = "fees" if fee_week and r.random() < 0.6 else r.choice(TOPICS)
            rows.append([d.isoformat(), code, name, q, src, down, topic])
    return write_csv("branches/branch-faq-usage-2026-q4.csv", header, rows)


# (department, host, category, action, daily requests mean, upload kb mean, users, start)
FLOWS = [
    ("CRD - Disputes", "api.llmhub.io", "Generative AI - API", "allowed (uncategorised)", 70, 1900, 3, date(2026, 10, 1)),
    ("CRD - Disputes", "tzofen.crescent-tenant.cloud", "Sanctioned - Tzofen", "allowed", 4, 40, 2, date(2026, 10, 1)),
    ("CRD - CX", "cleartext.ai", "Sanctioned vendor", "allowed", 160, 2400, 22, date(2026, 10, 1)),
    ("RET - HQ", "app.mishov-analytics.com", "Sanctioned vendor", "allowed", 90, 1500, 11, date(2026, 10, 1)),
    ("DIG - Marketing", "app.aiwriterpro.com", "Generative AI - writing", "monitored", 45, 120, 3, date(2026, 10, 1)),
    ("DIG - Marketing", "chat.llmhub.io", "Generative AI - chat", "blocked", 6, 0, 2, date(2026, 10, 1)),
    ("DIG - Product", "converso.ai", "Sanctioned vendor", "allowed", 400, 300, 6, date(2026, 10, 1)),
    ("CC - Floor", "kolot.ai", "Sanctioned vendor", "allowed", 1800, 52000, 140, date(2026, 10, 1)),
    ("CC - Floor", "translate.freetrans.net", "Translation - free", "allowed", 35, 60, 9, date(2026, 10, 1)),
    ("CC - Floor", "tzofen.crescent-tenant.cloud", "Sanctioned - Tzofen", "allowed", 900, 2000, 80, date(2026, 10, 1)),
    ("OPS - Back office", "tzofen.crescent-tenant.cloud", "Sanctioned - Tzofen", "allowed", 1100, 2500, 90, date(2026, 10, 1)),
    ("BRANCH - network", "tzofen.crescent-tenant.cloud", "Sanctioned - Tzofen", "allowed", 380, 400, 60, date(2026, 10, 1)),
    ("BRANCH - network", "chat.llmhub.io", "Generative AI - chat", "blocked", 14, 0, 9, date(2026, 10, 1)),
    ("HR", "talentrank.io", "Sanctioned vendor", "allowed", 20, 900, 3, date(2026, 10, 1)),
    ("TRS - Dealing", "chat.llmhub.io", "Generative AI - chat", "blocked", 3, 0, 1, date(2026, 10, 1)),
    ("FIN", "tzofen.crescent-tenant.cloud", "Sanctioned - Tzofen", "allowed", 40, 90, 6, date(2026, 10, 1)),
]


def proxy() -> int:
    r = rng(12)
    header = ["date", "department", "host", "category", "policy_action", "requests", "upload_kb",
              "distinct_users"]
    rows = []
    for d in days(date(2026, 10, 1), date(2026, 12, 31)):
        if not is_workday(d):
            continue
        for dept, host, cat, act, req, up, users, start in FLOWS:
            if d < start:
                continue
            boost = 1.0
            if dept.startswith("BRANCH") and host.startswith("tzofen") and d >= date(2026, 12, 1):
                boost = 1.6
            n = max(0, round(req * boost * r.uniform(0.6, 1.4)))
            if n == 0:
                continue
            kb = 0 if act == "blocked" else round(up * boost * r.uniform(0.6, 1.4))
            u = max(1, min(users * 2, round(users * r.uniform(0.7, 1.2))))
            rows.append([d.isoformat(), dept, host, cat, act, n, kb, u])
    return write_csv("security/proxy-ai-hosts-2026-q4.csv", header, rows)


SAAS = [("FIGMAPRO*TEAM", "Digital Channels", "USD", 75), ("SURVEYLY ANNUAL", "Retail Banking", "ILS", 4200),
        ("CLOUDBOX STORAGE", "Treasury & Markets", "USD", 20), ("DIAGRAMIT", "Operations", "USD", 12),
        ("STOCKPHOTO PLUS", "Digital Channels", "USD", 49), ("PDFTOOLS PRO", "Mortgages", "USD", 15),
        ("WEBINARLY", "HR", "USD", 39), ("MAPSDATA API", "Credit Risk", "USD", 60),
        ("TRANSCRIBER APP", "Private Banking", "USD", 17), ("CODEHOST TEAM", "Digital Channels", "USD", 44)]


def card_and_expense() -> int:
    r = rng(13)
    # the card issuer's conversion rate per month (synthetic, close to the 2026 market)
    fxm = {1: 3.58, 2: 3.55, 3: 3.52, 4: 3.47, 5: 3.43, 6: 3.39, 7: 3.35, 8: 3.31, 9: 3.27,
           10: 3.22, 11: 3.17, 12: 3.14}
    header = ["txn_id", "source", "date", "cardholder_or_claimant", "unit", "merchant",
              "original_currency", "original_amount", "amount_ils", "gl_category", "description_entered"]
    rows = []
    for m in range(1, 13):
        fx = fxm[m]
        for merch, unit, cur, amt in SAAS:
            if r.random() < 0.75:
                d = date(2026, m, r.randrange(1, 28))
                a = round(amt * r.uniform(0.9, 1.1), 2)
                rows.append(["card", d, f"emp-{r.randrange(1000, 9999)}", unit, merch, cur, a,
                             round(a * fx if cur == "USD" else a, 2), "6420 Software & online services",
                             r.choice(["subscription", "tool", "monthly", ""])])
        if m >= 4:  # Cards dispute team: public LLM API on a team lead's corporate card
            d = date(2026, m, 3)
            a = round({4: 120, 5: 260, 6: 410, 7: 470, 8: 520, 9: 560, 10: 610, 11: 640, 12: 690}[m] * r.uniform(0.95, 1.05), 2)
            rows.append(["card", d, "Elad Ben-Shimon", "Cards & Payments", "LLMHUB *API USAGE", "USD", a,
                         round(a * fx, 2), "6420 Software & online services", "dev tools"])
        if m >= 3:  # Digital marketing: personal subscriptions reimbursed
            for who in (["N. Avraham", "S. Gold"] + (["L. Haddad"] if m >= 6 else [])):
                d = date(2026, m, r.randrange(2, 10))
                rows.append(["expense claim", d, who, "Digital Channels", "AIWRITERPRO MONTHLY", "USD", 24.0,
                             round(24.0 * fx, 2), "6420 Software & online services", "software subscription (personal account)"])
    rows.sort(key=lambda x: (x[2], x[5]))
    out = [[f"TX-{i:04d}", s, d.isoformat(), *rest] for i, (s, d, *rest) in enumerate(rows, 1)]
    return write_csv("finance/card-and-expense-software-2026.csv", header, out)


def build() -> dict:
    return {"assistant": assistant_usage(), "branch_faq": branch_faq(), "proxy": proxy(),
            "card": card_and_expense()}
