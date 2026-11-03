"""vendor/contracts-ai.csv, finance/ap-invoices-ai.csv, finance/card-and-expense-ai-2027.csv,
finance/ai-programme-cost-2027.csv, it/licence-usage-2027-05.csv."""
from datetime import date

from gen_common import rng, write_csv

CONTRACTS = [
    ["MSA-TZ-2026", "Tzir AI Ltd.", "Master services agreement (platform)", "2026-09-15", "O. Lavi", "2026-09-15",
     "", "", "", "", "per order forms", "", "", "", "I. Barkan", "Y", "Israel (vendor cloud)",
     "Order forms 101-103 signed under this agreement"],
    ["TZ-OF-101", "Tzir AI Ltd.", "Tzir Route: planner console, driver app (incl. driver score)", "2026-09-15",
     "O. Lavi", "2026-10-01", "2029-09-30", 36, 135000, 0, 4860000, "renews 12 months unless notice",
     "region scope reducible at each anniversary on 90 days' notice (MSA 7.4)", "North; Centre; South; Europe",
     "I. Barkan", "Y", "Israel (vendor cloud)", "310 driver seats, 24 planner seats, platform fee"],
    ["TZ-OF-102", "Tzir AI Ltd.", "Tzir Docs: customs document pre-fill into Meches Pro", "2026-09-16", "O. Lavi",
     "2026-11-01", "2029-10-31", 36, 130000, 0, 4680000, "renews 12 months unless notice",
     "minimum commitment 9,000 declarations a month", "Haifa; Ashdod; Ben Gurion airport", "I. Barkan", "Y",
     "Israel (vendor cloud)", "Go-live 1 Feb 2027 (sea); 1 Apr 2027 (air)"],
    ["TZ-OF-103", "Tzir AI Ltd.", "Tzir Assist: customer-portal assistant + integration", "2026-09-17", "O. Lavi",
     "2026-12-01", "2029-11-30", 36, 95000, 1450000, 4870000, "renews 12 months unless notice",
     "implementation milestones Dec 2026, Mar 2027, Jun 2027", "all customers", "I. Barkan", "Y",
     "Israel (vendor cloud)", "Documents feature from 20 Apr 2027"],
    ["KT-2026-04", "Kotev Ltd.", "Kotev Assist enterprise assistant, 450 seats", "2026-11-20", "S. Morozov",
     "2026-12-01", "2027-11-30", 12, 42750, 0, 513000, "auto-renews 12 months", "60 days before end",
     "all staff", "I. Barkan", "Y", "EU (vendor cloud)", ""],
    ["AD-2027-01", "Ayin Drive Ltd.", "In-cab camera, fatigue and distraction detection, 60 cabs", "2026-12-22",
     "M. Azulay", "2027-01-01", "2027-12-31", 12, 18000, 0, 216000, "none", "30 days; no refund of pre-paid months",
     "South", "M. Azulay", "N", "vendor cloud (location not stated)", "Pilot"],
    ["NV-2026-11", "Nezek Vision Ltd.", "Damage-photo assessment (warehouse) POC", "2026-10-25", "I. Barkan",
     "2026-11-01", "2027-08-31", 10, 22000, 0, 220000, "none", "none before end of term", "Centre",
     "I. Barkan", "N", "vendor cloud (location not stated)", "SOW: POC ends 28 Feb 2027"],
    ["TQ-2026-09", "Taarif Software Ltd.", "Quote-pricing add-in for sales, 30 seats", "2026-09-28", "I. Barkan",
     "2026-10-01", "2027-09-30", 12, 9500, 0, 114000, "auto-renews 12 months", "30 days before end", "Sales",
     "I. Barkan", "Y", "Israel", ""],
    ["MB-2019-03", "Mabat Fleet Ltd.", "Telematics (GPS, km, fuel) for all trucks; data export API", "2019-03-01",
     "CFO (then)", "2019-03-01", "2027-12-31", "", 61000, 0, "", "annual", "90 days", "all regions",
     "D. Volkov", "Y", "Israel", "Feeds Tzir Route nightly (API credentials rotated 13 Nov 2026)"],
    ["MP-2015-01", "Meches Pro Ltd.", "Customs brokerage software (release 9.3, March 2027)", "2015-01-01",
     "CEO (then)", "2015-01-01", "2027-12-31", "", 38000, 0, "", "annual", "90 days", "customs houses",
     "S. Peretz", "Y", "Israel", "Release 9.3 notes: 'HS Suggest (AI) enabled by default'"],
    ["ME-2018-02", "Mishkal ERP Ltd.", "ERP incl. AP 'Smart Match' module", "2018-02-01", "CFO (then)",
     "2018-02-01", "2028-01-31", "", 54000, 0, "", "annual", "90 days", "all", "S. Morozov", "Y", "Israel",
     "Smart Match uses a learned matching model (vendor documentation)"],
]


def contracts() -> int:
    header = ["contract_id", "vendor", "product", "signed_on", "signed_by", "start", "end", "term_months",
              "monthly_ils", "one_off_ils", "total_value_ils", "renewal", "notice_and_scope_terms", "scope",
              "business_owner", "dpa_signed", "data_location", "notes"]
    return write_csv("vendor/contracts-ai.csv", header, CONTRACTS)


ROUTE_SEATS = [("North", 104, 6), ("Centre", 70, 8), ("South", 92, 6), ("Europe", 44, 4)]
DOCS_USAGE = {"2026-11": 0, "2026-12": 0, "2027-01": 0, "2027-02": 4310, "2027-03": 4522, "2027-04": 5968,
              "2027-05": 6204}


def months(a: tuple, b: tuple):
    y, m = a
    while (y, m) <= b:
        yield f"{y}-{m:02d}"
        m += 1
        if m == 13:
            y, m = y + 1, 1


def invoices() -> int:
    r = rng(30)
    header = ["invoice_no", "vendor", "contract_id", "period", "line", "region", "quantity", "unit_price_ils",
              "amount_ils", "approved_by", "status"]
    rows = []
    n = 7700

    def add(vendor, cid, period, line, region, q, up, amount=None):
        approver = "pending (owner left)" if period >= "2027-05" else "I. Barkan"
        if vendor == "Ayin Drive Ltd.":
            approver = "M. Azulay" if period < "2027-05" else "pending"
        status = "paid" if period < "2027-05" else "open"
        rows.append([f"INV-{vendor[:2].upper()}-{n}", vendor, cid, period, line, region, q, up,
                     amount if amount is not None else round(q * up), approver, status])

    for p in months((2026, 10), (2027, 5)):
        n += 1
        for region, drivers, planners in ROUTE_SEATS:
            add("Tzir AI Ltd.", "TZ-OF-101", p, "driver app seat", region, drivers, 290)
            add("Tzir AI Ltd.", "TZ-OF-101", p, "planner console seat", region, planners, 1100)
        add("Tzir AI Ltd.", "TZ-OF-101", p, "platform fee", "all", 1, 18700)
        if p >= "2026-11":
            add("Tzir AI Ltd.", "TZ-OF-102", p, f"minimum commitment 9,000 declarations (used: {DOCS_USAGE[p]:,})",
                "all", 9000, 14.4444, 130000)
        if p >= "2026-12":
            add("Tzir AI Ltd.", "TZ-OF-103", p, "Tzir Assist subscription", "all", 1, 95000)
        if p in ("2026-12", "2027-03"):
            add("Tzir AI Ltd.", "TZ-OF-103", p, "implementation milestone", "all", 1, 500000)
        if p >= "2026-12":
            add("Kotev Ltd.", "KT-2026-04", p, "Kotev Assist seat", "all", 450, 95)
        if p >= "2027-01":
            add("Ayin Drive Ltd.", "AD-2027-01", p, "cab subscription", "South", 60, 300)
        if p >= "2026-11":
            add("Nezek Vision Ltd.", "NV-2026-11", p, "POC licence and support", "Centre", 1, 22000)
        add("Taarif Software Ltd.", "TQ-2026-09", p, "quote add-in seat", "Sales", 30, 316.67, 9500)
        add("Mabat Fleet Ltd.", "MB-2019-03", p, "telematics, 310 units", "all", 310, 196.77, 61000)
    r.shuffle(rows)
    rows.sort(key=lambda x: (x[3], x[1], x[4]))
    return write_csv("finance/ap-invoices-ai.csv", header, rows)


def cards() -> int:
    r = rng(31)
    header = ["posted", "cardholder_or_claimant", "department", "merchant", "description", "amount_original",
              "currency", "amount_ils", "gl_account", "approved_by"]
    rows = []
    fx = {1: 3.18, 2: 3.17, 3: 3.15, 4: 3.14, 5: 3.14}
    usd = {1: 188.40, 2: 296.15, 3: 402.70, 4: 518.90, 5: 604.35}
    for m in range(1, 6):
        rows.append([f"2027-{m:02d}-0{r.randint(2, 6)}", "M. Levitan", "Customer Service", "PROMPTWAY *API USAGE",
                     "API usage", usd[m], "USD", round(usd[m] * fx[m], 2), "6420 software & online services",
                     "Customer Service manager (own card)"])
    noise = [("Finance", "ONLINE SVC 4471*", "PDF conversion tool", 39.0, "USD"),
             ("Sales", "PRESENTATION TEMPLATES", "templates", 120.0, "ILS"),
             ("Customs - Haifa", "TARIFF DATA SUBSCR", "tariff database", 450.0, "ILS"),
             ("HQ", "VIDEO MEETING PRO", "meetings", 54.9, "ILS"),
             ("Operations - North", "MAP TILES SVC", "maps for planners", 25.0, "USD"),
             ("IT", "SSL CERT STORE", "certificate", 89.0, "USD"),
             ("Marketing", "STOCK PHOTO CO", "images", 79.0, "ILS")]
    for m in range(1, 6):
        for dept, merch, desc, amt, cur in r.sample(noise, 4):
            a = round(amt * r.uniform(0.9, 1.1), 2)
            ils = round(a * fx[m], 2) if cur == "USD" else a
            rows.append([f"2027-{m:02d}-{r.randint(7, 27):02d}", r.choice(["A. Golan", "T. Mekonen", "R. Saliba",
                         "Y. Klein", "O. Dror"]), dept, merch, desc, a, cur, ils, "6420 software & online services",
                         "line manager"])
    rows.sort(key=lambda x: x[0])
    return write_csv("finance/card-and-expense-ai-2027.csv", header, rows)


BUDGET = {"Tzir Route": 1620000, "Tzir Docs": 1560000, "Tzir Assist subscription": 0,
          "Tzir Assist implementation": 0, "Kotev Assist": 513000, "Ayin Drive": 100000, "Nezek Vision": 88000,
          "Quote add-in": 57000, "Forecast model cloud": 72000, "AI team salaries": 1190000,
          "Incident support and interim lead": 0}
MONTHLY = {"Tzir Route": 135000, "Tzir Docs": 130000, "Tzir Assist subscription": 95000, "Kotev Assist": 42750,
           "Ayin Drive": 18000, "Nezek Vision": 22000, "Quote add-in": 9500, "Forecast model cloud": 6000,
           "AI team salaries": 99167}


def programme_cost() -> int:
    r = rng(32)
    header = ["month", "line", "budget_ils", "actual_ils", "forecast_ils", "note"]
    rows = []
    for m in range(1, 13):
        mm = f"2027-{m:02d}"
        for line, annual in BUDGET.items():
            b = round(annual / 12) if m < 12 else annual - 11 * round(annual / 12)
            if line == "Nezek Vision":
                b = 44000 if m <= 2 else 0
            if line == "Ayin Drive":
                b = (16667 if m < 6 else 16665) if m <= 6 else 0
            if line == "Quote add-in":
                b = 9500 if m <= 6 else 0
            v = MONTHLY.get(line, 0)
            note = ""
            if line == "Tzir Assist implementation":
                v = 500000 if m == 3 else (450000 if m == 6 else 0)
            if line == "Nezek Vision" and m > 8:
                v = 0
            if line == "Quote add-in" and m > 9:
                v = 0
            if line == "Incident support and interim lead":
                v = {5: 38000, 6: 178000}.get(m, 0)
            if line in ("Tzir Assist subscription", "Tzir Assist implementation") and m == 1:
                note = "budget: 'funded from AI savings'"
            if line == "AI team salaries" and m >= 7:
                v = 61000
                note = "head of AI position vacant from 27 May"
            actual = v if m <= 5 else ""
            fc = v if m >= 6 else ""
            if actual != "" and line == "Forecast model cloud":
                actual = round(v * r.uniform(0.85, 1.12))
            rows.append([mm, line, b, actual, fc, note])
    return write_csv("finance/ai-programme-cost-2027.csv", header, rows)


def licences() -> int:
    header = ["system", "region_or_department", "seat_type", "seats_billed", "seats_assigned", "active_30d",
              "source", "as_of"]
    rows = []
    act_d = {"North": 96, "Centre": 0, "South": 0, "Europe": 0}
    ass_d = {"North": 104, "Centre": 70, "South": 92, "Europe": 0}
    act_p = {"North": 6, "Centre": 5, "South": 0, "Europe": 0}
    ass_p = {"North": 6, "Centre": 8, "South": 6, "Europe": 2}
    for region, drivers, planners in ROUTE_SEATS:
        rows.append(["Tzir Route", region, "driver app", drivers, ass_d[region], act_d[region], "Tzir admin console", "2027-05-31"])
        rows.append(["Tzir Route", region, "planner console", planners, ass_p[region], act_p[region], "Tzir admin console", "2027-05-31"])
    for dept, seats, act in (("Customer Service", 60, 31), ("Finance", 40, 18), ("Sales", 55, 22), ("HQ", 95, 25),
                             ("Customs", 80, 9), ("Operations", 120, 7)):
        rows.append(["Kotev Assist", dept, "user", seats, seats, act, "Kotev admin export", "2027-05-31"])
    rows.append(["Ayin Drive", "South", "cab unit", 60, 60, 0, "Ayin portal (no events since 2027-03-08)", "2027-05-31"])
    rows.append(["Nezek Vision", "Centre", "user", 25, 25, 0, "vendor e-mail", "2027-05-31"])
    rows.append(["Quote add-in", "Sales", "user", 30, 30, 0, "Taarif admin", "2027-05-31"])
    rows.append(["Tzir Assist", "customers", "portal user enabled", 1840, 1840, 612, "Tzir admin console", "2027-05-31"])
    rows.append(["Meches Pro HS Suggest", "Customs", "feature flag", "", 31, 31, "release 9.3 default: on", "2027-05-31"])
    rows.append(["Mishkal Smart Match", "Finance", "module", "", 6, 6, "ERP admin", "2027-05-31"])
    return write_csv("it/licence-usage-2027-05.csv", header, rows)


def build() -> dict:
    return {"contracts": contracts(), "ap-invoices": invoices(), "cards": cards(),
            "programme-cost": programme_cost(), "licences": licences()}
