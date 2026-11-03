"""Donors, funders, the card statement and the accounts-and-licences list."""
from __future__ import annotations

from datetime import date

import textbank as tb
from common import DOMAIN, ROOM, pick, rand_date, rng, write_csv

N_DONORS = 1134

# name, type, annual ILS, programme, report frequency, report format, per-family narratives,
# next report due, renewal due, est. hours per report (development's estimate), est. hours per proposal, language
FUNDERS = [
    ("Adler-Haddad Family Foundation", "family foundation", 870000, "Family coordination (children under 13)",
     "quarterly", "own template (Word), per-family outcome narrative for every family under the grant", "y",
     "2027-01-15", "2027-01-31", 90, 40, "en"),
    ("Ministry of Welfare (support)", "government", 920000, "Respite and parent groups", "annual",
     "online support system + audited figures", "n", "2027-04-30", "2027-03-15", 30, 35, "he"),
    ("Kiryat Hadas municipality (service agreement)", "municipality", 620000, "Coordination for referred families",
     "monthly + annual", "municipal Excel form (counts per family id)", "n", "2026-12-05", "2027-12-31", 6, 20, "he"),
    ("Galilee Children's Trust", "foundation", 360000, "Respite weekends", "semi-annual",
     "narrative + budget (their form)", "n", "2027-02-28", "2027-06-30", 14, 22, "en"),
    ("Keshet Valley Federation", "federation", 300000, "Rights hotline", "annual", "online portal, outcomes + 2 stories", "n",
     "2027-03-31", "2027-03-31", 12, 18, "en"),
    ("Bar-Natan Fund", "family foundation", 240000, "Siblings programme", "annual", "letter + numbers", "n",
     "2027-01-31", "2027-05-31", 6, 10, "he"),
    ("North Coast Community Foundation", "community foundation", 180000, "Parent groups (Arabic)", "semi-annual",
     "their form, outcomes", "n", "2027-01-20", "2027-07-31", 10, 16, "en"),
    ("Tzur-Lev Insurance employees' fund", "corporate", 120000, "Hanukkah and summer events", "annual",
     "photos + short report", "n", "2027-01-10", "2027-09-30", 5, 6, "he"),
    ("Rosenblum-Asaf Foundation", "family foundation", 110000, "Amharic-speaking families", "annual",
     "narrative (English)", "n", "2027-02-15", "2027-02-15", 10, 18, "en"),
    ("Tikun Haifa Bay Fund", "foundation", 90000, "Transport to therapies", "annual", "online form", "n",
     "2027-03-01", "2027-03-01", 6, 12, "he"),
    ("Harel-Weiss Charitable Trust (UK)", "foundation", 85000, "General support", "annual",
     "narrative + audited accounts", "n", "2027-05-31", "2027-05-31", 8, 14, "en"),
    ("Shalev Family (donor-advised)", "donor-advised fund", 60000, "General support", "annual", "email update", "n",
     "2027-01-31", "2027-12-31", 2, 3, "en"),
    ("Kinneret Tech employees' giving", "corporate", 55000, "Volunteer training", "annual", "short report", "n",
     "2027-02-28", "2027-11-30", 3, 5, "he"),
    ("Haifa Rotary", "service club", 40000, "Equipment", "per grant", "letter + receipts", "n", "2027-01-31",
     "2027-10-31", 2, 4, "he"),
]
REPORTS_PER_YEAR = {"quarterly": 4, "semi-annual": 2, "annual": 1, "monthly + annual": 13, "per grant": 1}


def write_funders() -> list[tuple]:
    rows = [[f"FD{i + 1:02d}", *f[:4], f[4], REPORTS_PER_YEAR[f[4]], *f[5:]] for i, f in enumerate(FUNDERS)]
    write_csv(ROOM / "fundraising" / "funders.csv",
              ["funder_id", "funder", "type", "annual_amount_ils", "programme_funded", "report_frequency",
               "reports_per_year", "report_format", "per_family_narratives", "next_report_due", "renewal_due",
               "est_hours_per_report", "est_hours_per_proposal", "report_language"], rows)
    return FUNDERS


def build_donors() -> list[list]:
    r = rng("donors")
    rows = []
    sens_left = 37
    for i in range(1, N_DONORS + 1):
        dtype = pick(r, {"individual": 88, "family": 7, "company": 5})
        city = pick(r, {"Haifa": 28, "Kiryat Ata": 12, "Tel Aviv": 10, "Kiryat Bialik": 7, "Kiryat Motzkin": 6,
                        "Nesher": 4, "Shefa-'Amr": 5, "Acre": 4, "Jerusalem": 5, "Ra'anana": 4, "abroad (US)": 11,
                        "abroad (UK)": 4})
        abroad = city.startswith("abroad")
        lang = "en" if abroad else pick(r, {"he": 76, "ar": 9, "ru": 11, "en": 4})
        first = rand_date(r, date(2009, 1, 1), date(2026, 10, 25))
        g25 = 0 if first.year > 2025 else pick(r, {0: 30, 1: 45, 2: 10, 4: 6, 12: 9})
        g26 = pick(r, {0: 22, 1: 48, 2: 12, 3: 6, 10: 12}) if first.year <= 2026 else 0
        if first.year == 2026:
            g26 = max(g26, 1)
        size = r.lognormvariate(5.9, 1.0)
        if r.random() < 0.02:
            size *= 40
        a25 = round(size * g25 / max(1, g25) * (1 + 0.15 * (g25 - 1)) / 10) * 10 if g25 else 0
        a26 = round(size * r.uniform(0.8, 1.25) * (1 + 0.15 * (g26 - 1)) / 10) * 10 if g26 else 0
        method = "American Friends" if abroad else pick(r, {"credit card": 45, "standing order": 25,
                                                            "bank transfer": 22, "cash/cheque": 8})
        id_on_file = "n" if abroad or dtype == "company" else pick(r, {"y": 93, "n": 7})
        receipt = "american_friends" if abroad else ("ita_digital" if id_on_file == "y" or dtype == "company"
                                                     else "paper (pre-2026)")
        last = max(first, rand_date(r, date(2024, 1, 1), date(2026, 10, 30))) if (g25 or g26) else first
        consent = pick(r, {"y": 55, "n": 10, "": 35})
        segment = pick(r, {"": 50, "regular": 20, "lapsed": 12, "major": 4, "Giving Tuesday 2026": 10, "board": 1,
                           "monthly": 3})
        note = ""
        roll = r.random()
        if sens_left and roll < 0.045:
            note, sens_left = r.choice(tb.DONOR_NOTES_SENSITIVE), sens_left - 1
        elif roll < 0.13:
            note = r.choice(tb.DONOR_NOTES_PLAIN)
        rows.append([f"D{i:05d}", "[NAME]", dtype, city, lang, id_on_file, "[REMOVED]" if id_on_file == "y" else "",
                     first.isoformat(), last.isoformat(), g25, a25, g26, a26, method, receipt, consent, segment, note])
    # top up sensitive notes to exactly 37 on donors who have none yet
    k = 0
    while sens_left:
        row = rows[(k * 29 + 11) % len(rows)]
        if not row[17]:
            row[17] = tb.DONOR_NOTES_SENSITIVE[k % len(tb.DONOR_NOTES_SENSITIVE)]
            sens_left -= 1
        k += 1
    write_csv(ROOM / "fundraising" / "donors.csv",
              ["donor_id", "name", "donor_type", "city", "language", "id_on_file", "id_number", "first_gift",
               "last_gift", "gifts_2025", "amount_2025_ils", "gifts_2026", "amount_2026_ils", "method",
               "receipt_route", "marketing_consent", "segment", "notes"], rows)
    return rows


MONTH_RATE = {1: 3.31, 2: 3.29, 3: 3.27, 4: 3.25, 5: 3.22, 6: 3.20, 7: 3.19, 8: 3.17, 9: 3.15, 10: 3.139}


def build_card() -> list[list]:
    r = rng("card")
    rows = []

    def add(d, merchant, desc, amt, cur, card, cat, by):
        ils = round(amt * MONTH_RATE[d.month], 2) if cur == "USD" else amt
        rows.append([d.isoformat(), merchant, desc, f"{amt:.2f}", cur, f"{ils:.2f}", card, cat, by])

    for m in range(1, 11):
        add(date(2026, m, 3), "ZOOM.COM", "Zoom Workplace Pro x2", 31.98, "USD", "4417", "Software", "Yossi")
        add(date(2026, m, 6), "INTUIT *MAILCHIMP", "Mailchimp Standard", 78.00, "USD", "4417", "Software", "Noa")
        add(date(2026, m, 9), "DROPBOX*PLUS", "Dropbox Plus", 11.99, "USD", "4417", "Software", "Yossi")
        add(date(2026, m, 10), "KABALA ONLINE", "Receipts system (ITA digital reporting)", 149.00, "ILS", "4417",
            "Software", "Galina")
        if m >= 3:
            add(date(2026, m, 17), "OPENAI *CHATGPT SUBSCR", "ChatGPT Plus", 20.00, "USD", "8820",
                "Office supplies", "Noa")
        for _ in range(r.randint(4, 7)):
            merch, lo, hi, cat = r.choice([("PAZ FUEL KIRYAT ATA", 150, 420, "Travel"),
                                           ("SHUFERSAL DEAL", 120, 900, "Events"),
                                           ("GETT TAXI", 40, 160, "Travel"),
                                           ("OFFICE DEPOT IL", 90, 600, "Office supplies"),
                                           ("RAV-KAV ONLINE", 50, 200, "Travel"),
                                           ("ISRAEL POST", 20, 140, "Postage"),
                                           ("ALIEXPRESS", 30, 250, "Events")])
            d = date(2026, m, r.randint(1, 28))
            add(d, merch, "", round(r.uniform(lo, hi), 2), "ILS", r.choice(["4417", "4417", "8820"]), cat,
                r.choice(["Yossi", "Michael", "Amir", "Noa"]))
    add(date(2026, 2, 12), "WIX.COM", "Website annual plan", 1190.00, "ILS", "4417", "Software", "Maya")
    add(date(2026, 9, 3), "GRANTGENIE.AI", "Trial authorisation", 0.00, "USD", "8820", "", "")
    add(date(2026, 10, 14), "MSFT *M365 BUS PREM NP", "Microsoft 365 Business Premium (nonprofit) x10, annual",
        660.00, "USD", "4417", "Software", "")
    rows.sort(key=lambda x: (x[0], x[1]))
    write_csv(ROOM / "finance" / "card-statement-2026.csv",
              ["date", "merchant", "description", "amount", "currency", "amount_ils", "card_last4", "category",
               "approved_by"], rows)
    return rows


def write_accounts() -> list[list]:
    from people import FORMER, STAFF
    rows = []
    r = rng("accounts")
    for s in STAFF:
        last = date(2026, 11, r.randint(1, 11)).isoformat()
        rows.append(["Google Workspace for Nonprofits", "Nonprofits (no cost)", f"{s[7]}@{DOMAIN}", s[1], "active",
                     last, "free", "super admin" if s[0] == "S05" else ""])
    for local, who in (("info", "shared mailbox"), ("office", "shared mailbox")):
        rows.append(["Google Workspace for Nonprofits", "Nonprofits (no cost)", f"{local}@{DOMAIN}", who, "active",
                     "2026-11-11", "free", ""])
    for f, last in zip(FORMER, ("2025-03-30", "2025-09-02")):
        rows.append(["Google Workspace for Nonprofits", "Nonprofits (no cost)", f"{f[3]}@{DOMAIN}", f[1], "active",
                     last, "free", f[2]])
    ms_users = [("ronit.a", "2026-11-10"), ("noa.b", "2026-11-02"), ("galina.p", "2026-11-11"),
                ("yossi.m", "2026-03-22"), ("shira.l", "2025-12-04"), ("hana.g", "never"), ("michael.c", "2025-06-18"),
                ("maya.r", "never"), ("dana.k", "2025-03-27"), ("moshe.a", "2025-08-10")]
    for local, last in ms_users:
        rows.append(["Microsoft 365", "Business Premium (grant until renewal 2026-09-14; nonprofit price since)",
                     f"{local}@{DOMAIN}", local, "assigned", last, "card 4417, annual", "desktop Office"])
    rows += [
        ["Zoom", "Workplace Pro", f"office@{DOMAIN}", "shared", "active", "2026-11-10", "card 4417, monthly", ""],
        ["Zoom", "Workplace Pro", f"ronit.a@{DOMAIN}", "Dr. Ronit Azoulay", "active", "2026-11-09", "card 4417, monthly", ""],
        ["Mailchimp", "Standard", f"noa.b@{DOMAIN}", "Noa Ben-Ami", "active", "2026-11-04", "card 4417, monthly",
         "audience 1,630 contacts"],
        ["Dropbox", "Plus", f"yossi.m@{DOMAIN}", "Yossi Mizrahi", "active", "2024-05-19", "card 4417, monthly",
         "old photo archive, moved to Drive 2024"],
        ["Canva", "Canva for Nonprofits", f"maya.r@{DOMAIN}", "Maya Ronen + 6", "active", "2026-11-08", "free", ""],
        ["Kabala Online", "Receipts + ITA digital reporting", f"galina.p@{DOMAIN}", "Galina Petrova", "active",
         "2026-11-11", "card 4417, monthly", "super-authorised representative: Galina"],
        ["Website builder", "Business annual", f"maya.r@{DOMAIN}", "Maya Ronen", "active", "2026-11-02",
         "card 4417, annual", ""],
        ["ChatGPT", "Plus", "noa.benami.home@gmail.com", "Noa Ben-Ami", "active", "2026-11-11", "card 8820, monthly",
         "personal account, expensed"],
        ["GrantGenie", "Nonprofit Free Year (ends 2026-12-31, then Pro US$49/month)", "noa.benami.home@gmail.com",
         "Noa Ben-Ami", "trial", "2026-11-05", "card 8820 on file", "workspace: 'Open Hands grants'; 23 documents uploaded"],
        ["WhatsApp", "personal phones", "-", "respite volunteers and staff", "in use", "-", "-",
         "one group per respite weekend (see volunteer handbook)"],
    ]
    write_csv(ROOM / "it" / "accounts-and-licences.csv",
              ["service", "plan", "account", "assigned_to", "status", "last_sign_in", "billing", "notes"], rows)
    return rows
