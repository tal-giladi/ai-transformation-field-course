"""people/ai-people-by-unit.csv, people/staff-directory-extract.csv,
procurement/vendor-contracts-ai.csv, governance/model-inventory-2026-12.csv,
customers/complaints-monthly-2026.csv."""
from datetime import date, timedelta

from gen_common import rng, write_csv

# (unit, role, employment, fte_on_ai, pilots, reports_to)
PEOPLE = [
    ("Cards & Payments", "Product owner, AI", "employee", 1.0, "CRD-01;CRD-04", "Maya Elkayam"),
    ("Cards & Payments", "Data scientist", "employee", 1.0, "CRD-02", "Maya Elkayam"),
    ("Cards & Payments", "Data scientist", "contractor", 1.0, "CRD-02", "Maya Elkayam"),
    ("Cards & Payments", "Developer", "contractor", 1.0, "CRD-01;CRD-03", "Elad Ben-Shimon"),
    ("Cards & Payments", "Disputes team lead (builds tools)", "employee", 0.4, "CRD-03", "Elad Ben-Shimon"),
    ("Digital Channels", "Product owner, chatbot", "employee", 1.0, "DIG-01", "Tom Erez"),
    ("Digital Channels", "Conversation designer", "contractor", 1.0, "DIG-01", "Tom Erez"),
    ("Digital Channels", "Developer", "contractor", 1.0, "DIG-01;DIG-03", "Tom Erez"),
    ("Digital Channels", "Developer", "contractor", 1.0, "DIG-02;DIG-03", "Tom Erez"),
    ("Digital Channels", "Data analyst", "employee", 0.5, "DIG-03", "Tom Erez"),
    ("Digital Channels", "Marketing content lead", "employee", 0.2, "", "Tom Erez"),
    ("Treasury & Markets", "Quant developer", "employee", 1.0, "TRS-03", "Boris Lerner"),
    ("Treasury & Markets", "Research analyst", "employee", 0.5, "TRS-01", "Boris Lerner"),
    ("Treasury & Markets", "Surveillance analyst", "employee", 0.5, "TRS-02", "Boris Lerner"),
    ("Credit Risk", "Model developer", "employee", 1.0, "CRK-01", "Dr. Hila Nachum"),
    ("Credit Risk", "Model developer", "employee", 1.0, "CRK-01;CRK-02", "Dr. Hila Nachum"),
    ("Credit Risk", "Model developer", "employee", 0.5, "CRK-02", "Dr. Hila Nachum"),
    ("Credit Risk", "Data engineer", "contractor", 1.0, "CRK-01", "Dr. Hila Nachum"),
    ("Contact Centre", "QA lead (eval)", "employee", 0.6, "CC-01;CC-02;CC-03", "Revital Cohen"),
    ("Contact Centre", "Knowledge manager", "employee", 0.8, "CC-02", "Revital Cohen"),
    ("Contact Centre", "Workforce analyst", "employee", 0.3, "CC-01", "Revital Cohen"),
    ("Operations", "Process analyst", "employee", 1.0, "OPS-02;OPS-03", "Shlomi Azoulay"),
    ("Operations", "Assistant rollout manager", "employee", 1.0, "OPS-01", "Shlomi Azoulay"),
    ("Operations", "Back-office team lead", "employee", 0.3, "OPS-04;OPS-05", "Pnina Gabay"),
    ("Retail Banking", "Service quality manager", "employee", 0.5, "RET-01", "Hagit Mor"),
    ("Retail Banking", "Branch digital lead", "employee", 0.6, "RET-03", "Hagit Mor"),
    ("Mortgages", "Analytics lead", "employee", 0.5, "MTG-01;MTG-02", "Rachel Azaria"),
    ("SME Banking", "Business analyst", "employee", 0.5, "SME-01;SME-02;SME-03", "Yossi Ben-Haim"),
    ("Corporate Banking", "Credit analyst (memo pilot)", "employee", 0.4, "CORP-01", "Daniel Friedman"),
    ("Compliance & AML", "AML analytics lead", "employee", 1.0, "CMP-02", "Samer Khoury"),
    ("Compliance & AML", "KYC operations lead", "employee", 0.3, "CMP-01", "Samer Khoury"),
    ("HR", "HR analytics", "employee", 0.5, "HR-01;HR-02", "Anat Weiss"),
    ("Finance", "Finance systems analyst", "employee", 0.4, "FIN-01;FIN-02;FIN-03", "Eli Rosen"),
    ("IT - Data & Analytics (Mizrah)", "Data scientist", "employee", 1.0, "RET-02;RET-04", "Nir Ashkenazi"),
    ("IT - Data & Analytics (Mizrah)", "Data scientist", "employee", 1.0, "MTG-02;SME-03", "Nir Ashkenazi"),
    ("IT - Data & Analytics (Mizrah)", "Data scientist", "employee", 1.0, "CMP-02;OPS-03", "Nir Ashkenazi"),
    ("IT - Data & Analytics (Mizrah)", "Data scientist", "contractor", 1.0, "TRS-02;FIN-03", "Nir Ashkenazi"),
    ("IT - Data & Analytics (Mizrah)", "ML engineer", "employee", 1.0, "(platform)", "Nir Ashkenazi"),
    ("IT - Data & Analytics (Mizrah)", "Data engineer", "employee", 1.0, "(platform)", "Nir Ashkenazi"),
    ("IT - Data & Analytics (Mizrah)", "Data engineer", "contractor", 1.0, "(platform)", "Nir Ashkenazi"),
    ("IT - Infrastructure", "Cloud architect (AI landing zone)", "employee", 0.5, "(platform)", "Nir Ashkenazi"),
    ("IT - Security", "Security architect", "employee", 0.3, "", "Nir Ashkenazi"),
    ("Risk - Model Risk Management", "Head of model risk management", "employee", 1.0, "", "Dr. Irina Kogan"),
    ("Risk - Model Risk Management", "Validator", "employee", 1.0, "", "Yonatan Bar"),
    ("Risk - Model Risk Management", "Validator", "employee", 1.0, "", "Yonatan Bar"),
    ("COO office", "Head of AI CoE", "employee", 1.0, "", "Dalit Ben-Ami"),
]


def ai_people() -> int:
    header = ["row", "unit", "role", "employment", "fte_on_ai", "pilots", "reports_to"]
    return write_csv("people/ai-people-by-unit.csv", header, [[i, *p] for i, p in enumerate(PEOPLE, 1)])


# name, title, unit, status, left_on
DIRECTORY = [
    ("Avner Golan", "CEO", "Management", "active", ""), ("Dalit Ben-Ami", "COO", "Management", "active", ""),
    ("Moshe Dahan", "CFO", "Management", "active", ""), ("Dr. Irina Kogan", "CRO", "Risk", "active", ""),
    ("Nir Ashkenazi", "CIO", "IT", "active", ""), ("Adv. Lina Nassar", "Chief Compliance Officer", "Compliance", "active", ""),
    ("Tsega Alemu", "Chief Internal Auditor", "Internal Audit", "active", ""), ("Adv. Gideon Shalev", "General Counsel", "Legal", "active", ""),
    ("Ruth Ben-David", "DPO (Privacy Protection Officer)", "Legal", "active", ""),
    ("Hagit Mor", "Head of Retail Banking", "Retail Banking", "active", ""), ("Rachel Azaria", "Head of Mortgages", "Mortgages", "active", ""),
    ("Karim Haddad", "Head of Cards & Payments", "Cards & Payments", "active", ""), ("Yossi Ben-Haim", "Head of SME Banking", "SME Banking", "active", ""),
    ("Daniel Friedman", "Head of Corporate Banking", "Corporate Banking", "active", ""), ("Michael Stern", "Head of Private Banking", "Private Banking", "active", ""),
    ("Boris Lerner", "Head of Treasury & Markets", "Treasury & Markets", "active", ""), ("Dr. Hila Nachum", "Head of Credit Risk", "Credit Risk", "active", ""),
    ("Samer Khoury", "Head of AML Operations", "Compliance & AML", "active", ""), ("Shlomi Azoulay", "Head of Operations", "Operations", "active", ""),
    ("Revital Cohen", "Head of Contact Centre", "Contact Centre", "active", ""), ("Tom Erez", "Head of Digital Channels", "Digital Channels", "active", ""),
    ("Anat Weiss", "Head of HR", "HR", "active", ""), ("Eli Rosen", "Chief Controller", "Finance", "active", ""),
    ("Shira Katz", "Service quality manager", "Retail Banking", "active", ""), ("Yigal Sasson", "Retail analytics manager", "Retail Banking", "active", ""),
    ("Olga Petrenko", "Branch manager, Haifa Hadar", "Retail Banking", "active", ""), ("Dvir Amsalem", "Mortgage advice manager", "Mortgages", "active", ""),
    ("Maya Elkayam", "Cards CX & analytics manager", "Cards & Payments", "active", ""), ("Elad Ben-Shimon", "Disputes team lead", "Cards & Payments", "active", ""),
    ("Ariel Mizrahi", "Investment advisory manager", "Private Banking", "left", "2026-09-15"),
    ("Pnina Gabay", "Back-office manager", "Operations", "active", ""), ("Yonatan Bar", "Head of Model Risk Management", "Risk", "active", ""),
    ("Ma'ayan Levi", "Model validator", "Risk", "active", ""), ("Oleg Shapiro", "Model validator", "Risk", "active", ""),
    ("Eitan Bar-Lev", "Regulatory liaison manager", "Compliance", "active", ""), ("N. Avraham", "Campaign manager", "Digital Channels", "active", ""),
    ("S. Gold", "Content writer", "Digital Channels", "active", ""), ("L. Haddad", "Content writer", "Digital Channels", "active", ""),
]


def directory() -> int:
    header = ["name", "title", "unit", "status", "left_on", "email"]
    rows = []
    for name, title, unit, st, left in DIRECTORY:
        handle = name.replace("Dr. ", "").replace("Adv. ", "").replace("'", "").replace(".", "").lower().split()
        rows.append([name, title, unit, st, left, f"{handle[0][0]}{handle[-1]}@crescent-bank.example"])
    return write_csv("people/staff-directory-extract.csv", header, rows)


# id, vendor, owner unit, product/use, start, end, auto_renew, renewal_months, notice_days, annual_ils, dpa, location, notes
CONTRACTS = [
    ("PR-2025-088", "Rishum Docs", "Mortgages", "Document extraction, mortgage files", "2025-08-15", "2027-08-14", "Y", 12, 90, 180000, "Y", "EU", "Also used by Operations back office (same tenant)"),
    ("PR-2025-090", "Tzofen", "Operations", "Tzofen Assist enterprise assistant, 1,600 seats from 2026-12-01 (300 from 2026-05-03); agent studio included", "2025-12-01", "2028-11-30", "N", 0, 0, 2016000, "Y", "Israel", "Seats ₪105 a month; agent studio and retrieval index included in seat price"),
    ("PR-2025-099", "Ananim Cloud AI", "IT", "LLM API for the AI sandbox (pilots)", "2025-07-01", "2027-06-30", "Y", 12, 60, 180000, "Y", "EU", "Sandbox terms: pilots only, no production use; customer data only with DPO approval per pilot"),
    ("PR-2025-117", "Mishov Analytics", "Retail Banking", "Complaint summaries and themes", "2025-04-01", "2027-03-31", "Y", 24, 60, 264000, "Y", "EU", "Renews automatically for 24 months unless written notice 60 days before end"),
    ("PR-2025-122", "Sichon AI", "Digital Channels", "Customer chatbot platform", "2025-10-15", "2027-10-14", "Y", 12, 90, 230000, "Y", "EU", ""),
    ("PR-2025-126", "Imut Docs", "Compliance & AML", "KYC document checks", "2025-10-20", "2027-10-19", "N", 0, 0, 170000, "Y", "Israel", "Licence covers business-customer documents"),
    ("PR-2025-131", "Bahir Labs", "Cards & Payments", "Text summarisation API (complaints, chargebacks); also Contact Centre routing and Digital chat summaries", "2025-11-15", "2027-11-14", "Y", 12, 60, 340000, "Y", "EU", "One contract, three units"),
    ("PR-2025-135", "Kishron Rank", "HR", "CV ranking", "2025-12-15", "2026-12-14", "Y", 12, 30, 150000, "N", "US", "Renewed automatically on 2026-12-15; DPA never signed"),
    ("PR-2025-140", "Pinkas AI", "Corporate Banking", "Credit memo and commentary drafting", "2025-11-01", "2027-10-31", "N", 0, 0, 420000, "Y", "EU", "Private Banking portfolio commentary on the same contract"),
    ("PR-2026-004", "Kolelet AI", "Contact Centre", "Call transcription and summary (he/ar/ru)", "2026-01-20", "2028-01-19", "N", 0, 0, 210000, "Y", "Israel", ""),
    ("PR-2026-008", "Rishum Docs", "Credit Risk", "Covenant extraction", "2026-07-10", "2027-07-09", "Y", 12, 30, 120000, "Y", "EU", "Second Rishum Docs contract, separate price"),
    ("PR-2026-012", "Mismach Check", "SME Banking", "KYC document checks for SME onboarding", "2026-01-25", "2027-06-30", "Y", 12, 30, 150000, "Y", "Israel", ""),
    ("PR-2026-019", "Hatama AI", "Finance", "Invoice matching", "2026-02-20", "2027-02-19", "Y", 12, 30, 130000, "Y", "Israel", "Operations back office uses the same instance"),
    ("PR-2026-033", "Hadas Data (contractor)", "SME Banking", "Credit memo drafting POC (time and materials)", "2026-03-20", "2026-12-31", "N", 0, 0, 200000, "N", "Israel", "Extension requested for 2027"),
    ("PR-2026-041", "Katvan AI", "Mortgages", "Email and letter drafting", "2026-05-15", "2027-05-14", "Y", 12, 60, 130000, "Y", "US", "Private Banking letters on the same contract"),
    ("PR-2019-210", "Kesher Systems", "IT", "Kesher 360 CRM (SaaS)", "2019-07-01", "2027-06-30", "Y", 36, 120, 3900000, "Y", "EU", "Vendor roadmap: generative features (email drafting, account summaries, reply suggestions) in release 27.1, Oct 2027, on by default"),
    ("PR-2021-044", "Notzer Fraud Systems", "Cards & Payments", "Card fraud scoring (vendor ML model)", "2021-03-01", "2028-02-29", "Y", 24, 90, 1800000, "Y", "Israel", "Supplier model; in model inventory"),
    ("PR-2022-017", "Shomer AML", "Compliance & AML", "Transaction monitoring", "2022-06-01", "2028-05-31", "Y", 36, 180, 2400000, "Y", "Israel", "Includes ML scenario tuning module"),
]


def contracts() -> int:
    header = ["contract_id", "vendor", "owner_unit", "product_or_use", "start", "end", "auto_renew",
              "renewal_term_months", "notice_days", "annual_value_ils", "dpa_signed", "data_location", "notes"]
    return write_csv("procurement/vendor-contracts-ai.csv", header, [list(c) for c in CONTRACTS])


TYPES = [("PD scorecard - retail", "Credit Risk", "logistic regression"), ("LGD model", "Credit Risk", "regression"),
         ("Behavioural score - cards", "Cards & Payments", "logistic regression"), ("Collections priority", "Retail Banking", "gradient boosting (ML)"),
         ("VaR - trading book", "Treasury & Markets", "historical simulation"), ("ALM / IRRBB", "Treasury & Markets", "cash-flow model"),
         ("Pricing - deposits", "Treasury & Markets", "expert model"), ("Provision (CECL-type) model", "Finance", "statistical"),
         ("Stress test - credit", "Credit Risk", "macro regression"), ("AML scenario thresholds", "Compliance & AML", "rules + statistical tuning"),
         ("Mortgage LTV / affordability", "Mortgages", "expert scorecard"), ("SME rating", "SME Banking", "expert + statistical"),
         ("Corporate rating", "Corporate Banking", "expert scorecard"), ("Capital - operational risk", "Risk", "statistical")]


def model_inventory() -> int:
    r = rng(20)
    header = ["model_id", "model_name", "owner_unit", "method", "supplier_model", "materiality",
              "in_use_since", "last_validation", "validation_type", "phase_in_369", "ai_flag"]
    rows = []
    n = 0
    for i in range(142):
        name, unit, method = TYPES[i % len(TYPES)]
        n += 1
        material = "material" if i < 63 else "other"
        since = date(2008 + r.randrange(0, 17), r.randrange(1, 13), 1)
        if material == "material":
            last = date(2025, 9, 1) + timedelta(days=r.randrange(0, 160))
            ph, vt = "compliant", "comprehensive"
        else:
            k = i - 63
            if k < 18:
                last = date(2026, 3, 1) + timedelta(days=r.randrange(0, 280))
                ph, vt = "compliant", "initial/periodic"
            elif k < 31:
                last = date(2021, 1, 1) + timedelta(days=r.randrange(0, 1400))
                ph, vt = "in progress", "periodic (pre-369)"
            else:
                last = date(2019, 1, 1) + timedelta(days=r.randrange(0, 1800))
                ph, vt = "not started", "periodic (pre-369)"
        ai = "ML" if "ML" in method else ("supplier ML" if (unit == "Cards & Payments" and i % 7 == 2) else "")
        rows.append([f"M-{n:03d}", f"{name} v{r.randrange(1, 6)}", unit, method,
                     "Y" if ai == "supplier ML" else "N", material, since.isoformat(),
                     last.isoformat(), vt, ph, ai])
    return write_csv("governance/model-inventory-2026-12.csv", header, rows)


def complaints() -> int:
    r = rng(21)
    header = ["month", "unit", "channel", "complaints_received", "median_days_to_close", "summarised_by_ai_pilot"]
    rows = []
    base = {"Retail Banking": 820, "Cards & Payments": 1150, "Mortgages": 210, "Digital Channels": 260, "Contact Centre": 140}
    for m in range(1, 13):
        for unit, b in base.items():
            for ch, share in (("phone", 0.45), ("branch", 0.2), ("web/app", 0.25), ("letter/email", 0.1)):
                n = round(b * share * r.uniform(0.85, 1.15))
                summ = "Y" if (unit == "Retail Banking" and m >= 11 or unit == "Retail Banking" and m >= 4 and ch != "branch") else ""
                if unit == "Cards & Payments" and m >= 1:
                    summ = "Y"
                rows.append([f"2026-{m:02d}", unit, ch, n, round(r.uniform(6, 19), 1), summ])
    return write_csv("customers/complaints-monthly-2026.csv", header, rows)


def build() -> dict:
    return {"people": ai_people(), "directory": directory(), "contracts": contracts(),
            "inventory": model_inventory(), "complaints": complaints()}
