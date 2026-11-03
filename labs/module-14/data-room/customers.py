"""Customers, enterprise contracts, 2026 renewals, Lumen staff and support shifts."""
from __future__ import annotations

from datetime import date, timedelta

import textbank as tb
from common import BETA_END, ROOM, rng, write_csv

TIER_COUNTS = {"starter": 1640, "growth": 1340, "enterprise": 120}
PRICE = {"starter": 19, "growth": 24}            # ₪ per seat per month, list price
COUNTRIES = [("IL", 68), ("CY", 5), ("GR", 4), ("DE", 3), ("NL", 3), ("PL", 2), ("RO", 2), ("US", 13)]
LEADS = ["Amir Haddad", "Dana Ohana", "Pavel Orlov", "Lina Khoury"]


def _lang(r, country: str) -> str:
    if country == "IL":
        return r.choices(["he", "ar", "ru", "en"], [74, 10, 9, 7])[0]
    return r.choices(["en", "ru"], [92, 8])[0]


def _slug(name: str) -> str:
    keep = "".join(ch.lower() if ch.isalnum() else "-" for ch in name.replace("ó", "o"))
    while "--" in keep:
        keep = keep.replace("--", "-")
    return keep.strip("-")[:28]


def build_customers() -> list[dict]:
    r = rng("customers")
    out, used = [], set()
    named = {n[0]: n for n in tb.NAMED}
    for nm in named:
        used.add(nm)
    n = 10001
    tiers = []
    for tier, cnt in TIER_COUNTS.items():
        k = cnt - sum(1 for x in tb.NAMED if x[1] == tier)
        tiers += [tier] * k
    r.shuffle(tiers)
    # put the named customers at fixed positions so their ids are stable
    plan = []
    for i, t in enumerate(tiers):
        plan.append(("gen", t))
        if i in (40, 95, 333, 712, 1015, 1530, 2047, 2610):
            nm = tb.NAMED[[40, 95, 333, 712, 1015, 1530, 2047, 2610].index(i)]
            plan.append(("named", nm))
    for kind, item in plan:
        if kind == "named":
            name, tier, country, lang, seats, billing, beta, domain = item
        else:
            tier = item
            country = r.choices([c for c, _ in COUNTRIES], [w for _, w in COUNTRIES])[0]
            lang = _lang(r, country)
            words = tb.IL_WORDS if country == "IL" else tb.US_WORDS if country == "US" else tb.EU_WORDS
            for _ in range(50):
                name = f"{r.choice(words)} {r.choice(tb.TRADES)}"
                suf = r.choice(tb.SUFFIX[country])
                name = f"{name} {suf}".strip()
                if name not in used:
                    break
                name = f"{name} {r.randint(2, 9)}"
                if name not in used:
                    break
            used.add(name)
            if tier == "starter":
                seats = max(3, min(25, int(r.lognormvariate(2.2, 0.45))))
                billing = r.choices(["monthly", "annual"], [85, 15])[0]
            elif tier == "growth":
                seats = max(20, min(320, int(r.lognormvariate(4.0, 0.55))))
                billing = r.choices(["monthly", "annual"], [55, 45])[0]
            else:
                seats = max(300, min(2400, int(r.lognormvariate(6.8, 0.45))))
                billing = "annual"
            domain = _slug(name.rsplit(" ", 1)[0] if country != "IL" else name) + tb.DOMAIN_TLD[country]
            beta = "n"
        since = date(2015, 1, 1) + timedelta(days=r.randint(0, 4200))
        if since > date(2026, 9, 30):
            since = date(2026, 9, 30) - timedelta(days=r.randint(0, 900))
        if tier == "enterprise":
            rate = round(r.uniform(11.0, 15.0) * 2) / 2
            if name == "Negev Retail Group":
                rate = 12.5
            if name == "Shaked Clinics":
                rate = 13.5
        else:
            rate = PRICE[tier]
        out.append({"id": f"C-{n}", "name": name, "tier": tier, "country": country, "lang": lang, "seats": seats,
                    "billing": billing, "rate": rate, "since": since, "domain": domain, "beta": beta,
                    "status": "active", "usage": round(r.uniform(-25, 30), 1)})
        n += 1
    # beta: 420 opted-in Starter and Growth customers (named ones already in)
    pool = [c for c in out if c["tier"] != "enterprise" and c["beta"] == "n" and c["country"] in ("IL", "CY", "GR", "US")]
    r.shuffle(pool)
    need = 420 - sum(1 for c in out if c["beta"] == "y")
    starters = [c for c in pool if c["tier"] == "starter"][:180 - sum(1 for c in out if c["beta"] == "y" and c["tier"] == "starter")]
    growths = [c for c in pool if c["tier"] == "growth"][:need - len(starters)]
    for c in starters + growths:
        c["beta"] = "y"
    # trials started in November joined the beta automatically (flag rule changed on 1 November)
    for i in range(42):
        country = r.choices(["IL", "CY", "GR", "US"], [80, 6, 4, 10])[0]
        words = tb.IL_WORDS if country == "IL" else tb.US_WORDS if country == "US" else tb.EU_WORDS
        name = f"{r.choice(words)} {r.choice(tb.TRADES)} {r.randint(2, 99)}"
        start = date(2026, 11, 1) + timedelta(days=r.randint(0, 25))
        out.append({"id": f"C-{n}", "name": name, "tier": "starter", "country": country, "lang": _lang(r, country),
                    "seats": r.randint(3, 12), "billing": "monthly", "rate": 0, "since": start,
                    "domain": _slug(name) + tb.DOMAIN_TLD[country], "beta": "y", "status": "trial", "usage": 0.0})
        n += 1
    for c in out:
        monthly = c["seats"] * c["rate"]
        mods = 0
        if c["tier"] == "enterprise":
            mods = round(c["seats"] * r.uniform(2.0, 3.5) * 12, -3)
            if c["name"] == "Shaked Clinics":
                mods = 96000
        c["monthly"] = round(monthly, 2)
        c["arr"] = round(monthly * 12 + mods)
        c["modules"] = mods
        if c["billing"] == "annual":
            nxt = date(2026, c["since"].month, min(c["since"].day, 28))
            if nxt <= date(2026, 11, 26):
                nxt = date(2027, nxt.month, nxt.day)
            c["renewal"] = nxt
        else:
            c["renewal"] = None
    shaked = next(c for c in out if c["name"] == "Shaked Clinics")
    shaked["renewal"] = date(2027, 3, 31)
    negev = next(c for c in out if c["name"] == "Negev Retail Group")
    negev["renewal"] = date(2027, 2, 28)
    return out


def build_renewals(customers: list[dict]) -> list[dict]:
    """Annual Growth renewals 1 Feb - 26 Nov 2026, with usage change and outcome; adds churned customers."""
    r = rng("renewals")
    rows, extra = [], []
    pool = [c for c in customers if c["tier"] == "growth" and c["billing"] == "annual"]
    # churned accounts existed before; they appear in the customer file with status churned
    nxt = 10001 + len(customers)
    for c in pool:
        d = date(2026, c["since"].month, min(c["since"].day, 28))
        if not (date(2026, 2, 1) <= d <= BETA_END) or c["since"].year == 2026:
            continue
        rows.append({"cust": c, "date": d})
    for i in range(int(len(rows) * 0.17)):
        base = r.choice(pool)
        d = date(2026, 2, 1) + timedelta(days=r.randint(0, (BETA_END - date(2026, 2, 1)).days))
        cc = dict(base)
        cc.update({"id": f"C-{nxt}", "name": f"{base['name'].split(' ')[0]} {r.choice(tb.TRADES)} {r.randint(10, 99)}",
                   "status": "churned", "since": date(2019 + r.randint(0, 5), d.month, min(d.day, 28)),
                   "renewal": None, "beta": "n"})
        nxt += 1
        extra.append(cc)
        rows.append({"cust": cc, "date": d, "churn": True})
    out = []
    for row in rows:
        c, d = row["cust"], row["date"]
        churn_risk = 0.55 if d < date(2026, 8, 2) else 0.3
        risk = r.random() < 0.2 or row.get("churn") and r.random() < churn_risk
        usage = round(r.uniform(-75, -40), 1) if risk else round(r.uniform(-35, 35), 1)
        if row.get("churn"):
            outcome = "churned"
        elif risk:
            after = d >= date(2026, 8, 2)
            p = [0.70, 0.12, 0.18] if after else [0.56, 0.18, 0.26]
            outcome = r.choices(["renewed", "renewed_fewer_seats", "downgraded_to_starter"], p[:3])[0]
        else:
            outcome = r.choices(["renewed", "renewed_fewer_seats", "downgraded_to_starter"], [0.9, 0.07, 0.03])[0]
        seats_after = c["seats"] if outcome == "renewed" else max(20, int(c["seats"] * 0.7)) \
            if outcome == "renewed_fewer_seats" else (min(c["seats"], 25) if outcome == "downgraded_to_starter" else 0)
        out.append({"id": c["id"], "date": d, "seats": c["seats"], "usage": usage, "outcome": outcome,
                    "seats_after": seats_after, "risk": usage <= -40})
    customers.extend(extra)
    out.sort(key=lambda x: (x["date"], x["id"]))
    return out


def write_customers(customers: list[dict], renewals: list[dict]) -> None:
    rows = []
    for c in customers:
        rows.append([c["id"], c["name"], c["tier"], c["country"], c["lang"], c["seats"], c["billing"],
                     f"{c['rate']:.2f}", c["arr"], c["since"].isoformat(),
                     c["renewal"].isoformat() if c["renewal"] else "", f"admin@{c['domain']}",
                     c["beta"], c["status"]])
    write_csv(ROOM / "customers" / "customers.csv",
              ["customer_id", "name", "plan", "country", "ui_language", "seats", "billing", "price_per_seat_ils",
               "arr_ils", "customer_since", "renewal_date", "admin_email", "assist_beta", "status"], rows)
    write_csv(ROOM / "customers" / "growth-renewals-2026.csv",
              ["customer_id", "renewal_date", "seats_before", "active_users_change_90d_pct", "outcome", "seats_after"],
              [[x["id"], x["date"].isoformat(), x["seats"], x["usage"], x["outcome"], x["seats_after"]]
               for x in renewals])


def write_contracts(customers: list[dict]) -> None:
    r = rng("contracts")
    rows = []
    ent = [c for c in customers if c["tier"] == "enterprise"]
    ai_terms = ["", "", "", "", "", "", "", "", "", "", "", "",
                "Customer Data shall not be used to train models", "Notify Customer of new sub-processors incl. AI providers"]
    for i, c in enumerate(ent):
        lead = LEADS[i % 4]
        term = r.choice([12, 24, 36])
        terms = r.choice(ai_terms)
        if c["name"] in ("Shaked Clinics", "Negev Retail Group"):
            lead = "Amir Haddad"
        if c["name"] == "Shaked Clinics":
            term, terms = 36, "Supplier to notify Customer before any AI system processes Customer Data; Customer may opt out"
        end = c["renewal"] or date(2027, 1, 1)
        start = date(end.year - term // 12, end.month, end.day)
        rows.append([c["id"], c["name"], c["seats"], f"{c['rate']:.2f}", int(c["modules"]), c["arr"], start.isoformat(),
                     end.isoformat(), term, "99.5% monthly; 5% of monthly fee per 0.5% below, max 25%",
                     terms, lead])
    write_csv(ROOM / "customers" / "enterprise-contracts.csv",
              ["customer_id", "name", "seats_contracted", "price_per_seat_ils", "modules_ils_per_year", "acv_ils",
               "term_start", "term_end", "term_months", "outage_credit_clause", "ai_terms", "account_lead"], rows)


STAFF_FIXED = [
    ("Yaron Ben-David", "Executive", "CEO and co-founder", "2014-03-02", "active", ""),
    ("Eyal Dahan", "R&D", "VP R&D and co-founder", "2014-03-02", "active", ""),
    ("Maya Rosenthal", "Product", "VP Product", "2019-06-16", "active", ""),
    ("Revital Azoulay", "Support", "VP Support", "2018-01-07", "active", ""),
    ("Andrei Kogan", "IT & Security", "CISO", "2021-04-11", "active", ""),
    ("Nurit Gal", "Legal", "General Counsel and DPO", "2020-09-06", "active", ""),
    ("Oren Shalev", "Finance", "CFO", "2022-02-13", "active", ""),
    ("Dana Klein", "Marketing", "VP Marketing", "2023-05-07", "active", ""),
    ("Michal Biton", "Customer Success", "Director of Customer Success", "2019-11-03", "active", ""),
    ("Shira Navon", "Customer Success", "Customer Success Manager", "2021-08-01", "active", ""),
    ("Amir Haddad", "Sales", "Commercial Account Lead, Enterprise", "2017-10-15", "active", ""),
    ("Dana Ohana", "Sales", "Commercial Account Lead, Enterprise", "2022-03-06", "active", ""),
    ("Pavel Orlov", "Sales", "Commercial Account Lead, Enterprise", "2020-01-12", "active", ""),
    ("Lina Khoury", "Sales", "Commercial Account Lead, Enterprise", "2023-09-03", "active", ""),
    ("Yonatan Tadesse", "Support", "Support Engineer, Tier 2", "2020-02-02", "active", ""),
    ("Boris Feldman", "Support", "Support Shift Lead", "2016-06-05", "active", ""),
    ("Hiba Mansour", "Support", "Support Shift Lead", "2021-01-10", "active", ""),
    ("Fatma Abu-Ras", "Finance", "Billing Lead", "2018-04-08", "active", ""),
    ("Noam Levi", "Product", "Product Manager, Lumen Assist", "2022-07-03", "active", ""),
    ("Rana Saleh", "Support", "Support Specialist", "2022-05-01", "active", ""),
    ("Dmitri Lerner", "Support", "Support Specialist", "2019-03-10", "active", ""),
    ("Tigist Alemu", "Support", "Support Specialist", "2023-02-05", "active", ""),
    ("Noa Peretz", "Support", "Support Specialist", "2024-06-02", "active", ""),
    ("Khaled Zoabi", "Support", "Support Specialist", "2021-10-17", "active", ""),
    ("Maisa Hamdan", "Marketing", "Content Manager", "2022-11-06", "active", ""),
    ("Daniel Weiss", "R&D", "Senior Backend Engineer", "2017-02-05", "left", "2026-06-30"),
    ("Amit Katz", "R&D", "Engineering Manager, Platform", "2018-09-02", "left", "2026-08-15"),
    ("Gal Ashkenazi", "Marketing", "Marketing Operations Manager", "2021-03-07", "left", "2026-09-10"),
    ("(new hire)", "Support", "Head of AI Operations", "2026-11-29", "starting", ""),
]
DEPT_SIZE = {"R&D": 92, "Product": 14, "Support": 38, "Customer Success": 22, "Sales": 30, "Marketing": 14,
             "Finance": 9, "Legal": 3, "IT & Security": 8, "HR": 5, "Executive": 3, "Data": 7, "Operations": 5}
TITLES = {"R&D": ["Software Engineer", "Senior Software Engineer", "QA Engineer", "DevOps Engineer"],
          "Product": ["Product Manager", "Product Designer"], "Support": ["Support Specialist", "Support Engineer"],
          "Customer Success": ["Customer Success Manager", "Onboarding Specialist"],
          "Sales": ["Account Executive", "SDR", "Sales Engineer"], "Marketing": ["Content Manager", "Growth Marketer"],
          "Finance": ["Accountant", "Billing Specialist"], "Legal": ["Legal Counsel"],
          "IT & Security": ["IT Administrator", "Security Engineer"], "HR": ["HR Partner"],
          "Executive": ["Executive Assistant"], "Data": ["Data Analyst", "Data Engineer"],
          "Operations": ["Office Manager", "Operations Analyst"]}


def write_staff() -> None:
    r = rng("staff")
    rows, names = [], set()
    count = {d: 0 for d in DEPT_SIZE}
    for nm, dept, title, start, status, left in STAFF_FIXED:
        email = "" if nm.startswith("(") else nm.lower().replace(" ", ".").replace("-", "") + "@lumen.io"
        rows.append([nm, email, dept, title, start, status, left])
        names.add(nm)
        if status in ("active", "starting"):
            count[dept] += 1
    groups = list(tb.FIRST)
    for dept, size in DEPT_SIZE.items():
        target = count[dept] + (size - count[dept]) + r.randint(0, 3)
        while count[dept] < target:
            g = r.choices(groups, [52, 16, 18, 8, 6])[0]
            nm = f"{r.choice(tb.FIRST[g])} {r.choice(tb.LAST[g])}"
            if nm in names:
                continue
            names.add(nm)
            start = date(2015, 1, 1) + timedelta(days=r.randint(0, 4200))
            if count[dept] < size:
                status, left = "active", ""
            else:
                start = min(start, date(2025, 6, 1))
                status, left = "left", (date(2026, 1, 1) + timedelta(days=r.randint(0, 320))).isoformat()
            count[dept] += 1
            rows.append([nm, nm.lower().replace(" ", ".").replace("-", "") + "@lumen.io", dept,
                         r.choice(TITLES[dept]), min(start, date(2026, 10, 1)).isoformat(), status, left])
    rows.sort(key=lambda x: (x[2], x[0]))
    write_csv(ROOM / "people" / "staff-directory.csv",
              ["name", "email", "department", "title", "start_date", "status", "left_date"], rows)


def write_shifts() -> None:
    rows = []
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    for i, d in enumerate(week):
        lead_am = "Boris Feldman" if i % 2 == 0 else "Hiba Mansour"
        lead_pm = "Hiba Mansour" if i % 2 == 0 else "Boris Feldman"
        rows.append([d, "08:00-13:00", lead_am, 9 if i != 4 else 8, 30, "approvals, escalations, quality review"])
        rows.append([d, "13:00-18:00", lead_pm, 8 if i != 4 else 7, 30, "approvals, escalations, callbacks"])
    rows.append(["Friday", "09:00-13:00", "Yonatan Tadesse (backup lead)", 2, 0, "on-call; no approvals planned"])
    write_csv(ROOM / "people" / "support-shifts.csv",
              ["day", "shift", "shift_lead", "agents_on_shift", "lead_minutes_for_approvals", "lead_duties"], rows)
