"""ai/pilot-register-2026-12.csv, ai/eval-summaries.csv, ai/intake-requests-2026.csv,
governance/model-review-queue-2026-12.csv."""
from datetime import date, timedelta

from gen_common import rng, write_csv, messy_date, money
from gen_pilots import AREA_REVIEW, PILOTS, UNITS

AS_OF = date(2026, 12, 31)


def register() -> int:
    r = rng(1)
    header = ["row_no", "pilot_id", "unit", "pilot_name", "description", "business_owner", "stage",
              "start_date", "last_update", "vendor", "contract_id", "environment", "data_class",
              "customer_facing", "decision_use", "decision_area", "human_review", "risk_self_assessed", "users_in_pilot", "test_set",
              "eval_result", "baseline_measured", "claimed_annual_benefit", "cost_2026_actual",
              "budget_2027_ils", "depends_on", "submitted_to_model_committee", "notes"]
    rows = []
    for i, p in enumerate(PILOTS, 1):
        en, he = UNITS[p["unit"]]
        unit = r.choice([en, en, he, p["unit"]])
        rows.append([
            i, p["id"], unit, p["name"] + (" " if r.random() < 0.08 else ""), p["description"],
            p["owner"], p["stage"], messy_date(p["started"], r.randrange(4)),
            messy_date(p["last_update"], r.choice([0, 1, 1, 3])), p["vendor"], p["contract_id"],
            p["environment"], p["data_class"], p["customer_facing"], p["decision_effect"],
            *AREA_REVIEW[p["id"]], p["risk_self"], p["users"], p["test_set_file"], p["eval_status"], p["baseline"],
            money(p["claimed_benefit"], r.randrange(3)), money(p["cost_2026"], r.randrange(3)),
            p["budget_2027"], p["depends_on"], p["submitted"], p["notes"],
        ])
    return write_csv("ai/pilot-register-2026-12.csv", header, rows)


# pilot -> list of runs: (date, n, languages, metric, value, threshold, run_by, note)
EVALS = {
    "RET-03": [("2025-12-10", 120, "he", "correct answer", "0.84", "0.85", "Retail digital team", "v1, procedures library of Oct 2025"),
               ("2026-06-15", 160, "he", "correct answer", "0.90", "0.85", "Retail digital team", "v2; 3 answers quoted a fee table replaced in May")],
    "RET-04": [("2026-08-20", 18450, "n/a", "AUC (backtest 2025)", "0.74", "0.70", "Data science", "No live test; no uplift measured")],
    "RET-02": [("2026-07-01", 0, "n/a", "uplift vs control", "", "", "Data science", "Holdout planned; not run. Compliance query on purpose of use open since Oct")],
    "MTG-01": [("2026-03-01", 400, "he/en", "field accuracy", "0.931", "0.90", "Rishum Docs + Mortgages", "Handwritten pay slips 81%")],
    "MTG-02": [("2026-09-20", 150, "n/a", "false-accept rate", "0.18", "0.05", "Mortgages analytics", "Price index snapshot 2023-06; no refresh process")],
    "MTG-03": [("2026-07-10", 80, "he", "correct answer", "0.88", "0.85", "Mortgages", "")],
    "CRD-01": [("2026-03-30", 200, "he/ar/ru/en", "summary accuracy", "0.86", "0.85", "Cards CX", "Arabic 0.79"),
               ("2026-10-12", 300, "he/ar/ru/en", "summary accuracy", "0.91", "0.85", "Cards CX", "Arabic 0.88 after glossary; root-cause tag agreement 0.83")],
    "CRD-02": [("2026-01-20", 52000, "n/a", "recall at top 20% of alerts", "0.86", "0.80", "Fraud analytics", "Lab data 2025; live shadow not run")],
    "CRD-03": [("2026-03-01", 120, "he/en", "letter acceptable without edit", "0.90", "0.85", "Cards disputes", "Template-bound; reason codes correct 0.97")],
    "SME-02": [("2026-09-01", 90, "he", "completeness recall", "0.89", "0.85", "SME ops", "Expired IDs of signatories missed most often")],
    "SME-03": [("2026-04-15", 9800, "n/a", "Gini (backtest 2024)", "0.61", "0.55", "SME analytics", "Trained and tested on 2024; rates since then changed")],
    "CORP-01": [("2026-05-30", 120, "he/en", "factual accuracy", "0.94", "0.95", "Corporate credit", "2 memos with a wrong covenant threshold; banker review catches"),
                ("2026-11-20", 120, "he/en", "factual accuracy", "0.97", "0.95", "Corporate credit", "After covenant table from CRK-02 extraction")],
    "CORP-02": [("2026-08-01", 40, "he/en", "brief rated usable", "0.92", "0.85", "Corporate", "")],
    "PRV-02": [("2026-06-30", 50, "he/en", "factual errors on holdings", "0.14", "0.02", "Private banking", "Owner left in September; suitability wording not reviewed")],
    "PRV-03": [("2025-12-01", 60, "he/en", "summary rated usable", "0.93", "0.85", "Treasury research", "")],
    "TRS-01": [("2025-12-01", 60, "he/en", "summary rated usable", "0.93", "0.85", "Treasury research", "")],
    "TRS-02": [("2026-10-30", 3100, "he/en", "precision at recall 0.8", "0.31", "0.25", "Compliance surveillance", "Lab set only")],
    "TRS-03": [("2026-11-15", 250, "n/a", "MAPE (backtest 2025)", "0.062", "0.08", "ALM team", "")],
    "CRK-01": [("2025-11-01", 2400, "n/a", "AUC (backtest 2019-2025)", "0.81", "0.75", "Credit risk models", "In validation since Sep 2026")],
    "CRK-02": [("2026-06-01", 200, "he/en", "field accuracy", "0.955", "0.95", "Credit risk", "")],
    "CMP-01": [("2026-04-20", 250, "he/ar/ru/en", "completeness recall", "0.96", "0.95", "AML operations", "Covers business customers' documents too")],
    "CMP-02": [("2026-08-15", 1200, "n/a", "false-negative rate on closed alerts", "0.09", "0.01", "AML operations", "Labelled 2025 alerts; 11 true positives auto-closed")],
    "OPS-01": [("2026-07-01", 100, "he/en", "task rated helpful", "0.81", "0.75", "Operations", "Generic tasks; not a model of any decision")],
    "OPS-02": [("2026-09-10", 150, "he", "correct and cited", "0.91", "0.85", "Operations", "Runs in the Tzofen agent studio; retrieval index OPS-procedures")],
    "OPS-03": [("2026-11-01", 200, "n/a", "right cause suggested", "0.78", "0.75", "Operations", "")],
    "OPS-04": [("2026-03-01", 400, "he/en", "field accuracy", "0.931", "0.90", "Rishum Docs + Mortgages", "Handwritten pay slips 81%")],
    "OPS-05": [("2026-06-20", 500, "n/a", "auto-match precision", "0.984", "0.98", "Finance", "")],
    "CC-01": [("2026-05-10", 200, "he/ar/ru", "summary accuracy", "0.89", "0.85", "Contact Centre QA", "Arabic 0.81, Russian 0.86")],
    "CC-02": [("2026-10-05", 180, "he/ar/ru", "correct and cited", "0.88", "0.85", "Contact Centre QA", "Runs in the Tzofen agent studio; retrieval index CC-knowledge")],
    "CC-03": [("2026-09-01", 400, "he/ar/ru/en", "routing accuracy", "0.61", "0.85", "Contact Centre QA", "")],
    "DIG-01": [("2026-06-01", 200, "he/ar/ru/en", "correct answer", "0.71", "0.90", "Digital", "17% wrong on fees; Arabic questions answered in Hebrew"),
               ("2026-10-20", 200, "he/ar/ru/en", "correct answer", "0.76", "0.90", "Digital", "Still wrong on 2026 fee changes; A/B live on 2% anyway")],
    "DIG-02": [("2026-08-01", 50, "he", "spot check acceptable", "0.88", "", "Digital", "No threshold set")],
    "DIG-03": [("2026-09-15", 300, "he/ar/ru/en", "top-3 hit", "0.87", "0.85", "Digital", "")],
    "HR-01": [("2026-06-15", 3400, "n/a", "selection-rate ratio, lowest group by home town", "0.62", "0.80", "HR analytics", "Features include home town and graduation year")],
    "HR-02": [("2026-07-01", 70, "he", "correct answer", "0.90", "0.85", "HR", "")],
    "FIN-01": [("2026-05-01", 24, "he", "commentary usable", "0.92", "0.85", "Finance", "")],
    "FIN-02": [("2026-06-20", 500, "n/a", "auto-match precision", "0.984", "0.98", "Finance", "")],
    "FIN-03": [("2026-10-01", 1500, "n/a", "hit rate vs random sample", "3.1", "2.0", "Finance", "")],
}


def evals() -> int:
    header = ["eval_id", "pilot_id", "run_date", "test_items", "languages", "metric", "value",
              "threshold", "run_by", "note"]
    rows, n = [], 0
    for p in PILOTS:
        for run in EVALS.get(p["id"], []):
            n += 1
            rows.append([f"EV-{n:03d}", p["id"], *run])
    return write_csv("ai/eval-summaries.csv", header, rows)


INTAKE = [
    ("RET", "Hagit Mor", "meeting", "סיכום שיחות בסניפים — כמו במוקד, להקליט ולסכם שיחות טלפון של הבנקאים בסניף", "Customer calls"),
    ("RET", "Branch Haifa Hadar", "email", "אפשר לקבל גישה לצ'אט ציבורי כדי לנסח מכתבים ללקוחות בערבית וברוסית?", "Customer letters"),
    ("CRD", "Maya Elkayam", "form", "Extend complaint summaries to merchant complaints", "Merchant data"),
    ("SME", "Yossi Ben-Haim", "email", "Cash-flow insights for SME clients in the app", "Account transactions"),
    ("CORP", "Daniel Friedman", "form", "Summaries of syndicated loan agreements", "Loan agreements"),
    ("MTG", "Rachel Azaria", "meeting", "סיכום תלונות משכנתא — לבנות משהו כמו בקמעונאות", "Complaints"),
    ("CC", "Revital Cohen", "form", "Real-time Arabic and Russian translation for agents on calls", "Customer calls"),
    ("DIG", "Tom Erez", "email", "Marketing copy generator for campaigns (we use a tool already, need budget)", "Marketing"),
    ("HR", "Anat Weiss", "form", "Performance review drafting for managers", "Employee data"),
    ("FIN", "Eli Rosen", "email", "Board report first drafts", "Financial results"),
    ("OPS", "Shlomi Azoulay", "form", "Agent studio assistant for the cheque-clearing team (Tzofen)", "Procedures"),
    ("OPS", "Pnina Gabay", "email", "Summaries of standing-order complaints", "Complaints"),
    ("TRS", "Boris Lerner", "form", "FX client commentary for corporate clients", "Market data"),
    ("PRV", "Michael Stern", "meeting", "Replace portfolio commentary with a new vendor", "Client portfolios"),
    ("CMP", "Samer Khoury", "form", "Adverse media screening summaries", "Public news"),
    ("CRK", "Dr. Hila Nachum", "email", "Explain-my-score text for credit decisions", "Credit scores"),
    ("CC", "Contact centre team leads", "email", "Можно ли использовать бесплатный переводчик для писем клиентов на русском?", "Customer letters"),
    ("RET", "Branch Nazareth Illit", "email", "طلب: مساعد لصياغة الردود على شكاوى الزبائن بالعربية", "Complaints"),
    ("DIG", "Tom Erez", "form", "Chatbot v2 with account actions (block card, change limit)", "Customer accounts"),
    ("RET", "Yigal Sasson", "form", "Complaint summaries for the branches (extend Mishov)", "Complaints"),
]


def intake() -> int:
    r = rng(3)
    header = ["request_id", "received", "from_unit", "requester", "channel", "request_text",
              "data_mentioned", "status", "days_open_at_2026_12_31"]
    rows = []
    start = date(2026, 3, 1)
    for i, (unit, who, ch, text, data) in enumerate(INTAKE, 1):
        rec = start + timedelta(days=r.randrange(0, 290))
        rows.append([f"REQ-{i:03d}", rec.isoformat(), UNITS[unit][0], who, ch, text, data,
                     r.choice(["new", "waiting", "waiting", "waiting for CoE"]), (AS_OF - rec).days])
    rows.sort(key=lambda x: x[1])
    return write_csv("ai/intake-requests-2026.csv", header, rows)


QUEUE_STATUS = {
    "CRK-01": ("In validation", "2026-09-06", "Y. Bar"), "OPS-01": ("In validation", "2026-11-22", "M. Levi"),
    "DIG-01": ("Returned: documentation incomplete", "", ""), "HR-01": ("Returned: documentation incomplete", "", ""),
    "SME-03": ("Waiting: full validation", "", ""),
}
LAST_COMMITTEE = {"RET-03": "2026-02-18", "CRD-02": "2026-04-22", "CRD-03": "2026-04-22",
                  "MTG-01": "2026-06-17", "CMP-01": "2026-06-17", "CORP-01": "2026-09-16",
                  "CRD-01": "2026-09-16", "CC-01": "2026-09-16", "DIG-01": "2026-11-25",
                  "HR-01": "2026-11-25", "OPS-01": "2026-11-25"}


def queue() -> int:
    header = ["submission_id", "pilot_id", "pilot_name", "unit", "submitted", "documentation_complete",
              "validation_required", "slots_estimate", "status", "validation_started", "validator",
              "last_committee", "committee_decision", "wait_days_at_2026_12_31"]
    rows = []
    subs = sorted((p for p in PILOTS if p["submitted"]), key=lambda p: p["submitted"])
    for i, p in enumerate(subs, 1):
        st, started, val = QUEUE_STATUS.get(p["id"], ("Waiting: full validation", "", ""))
        doc = "N" if st.startswith("Returned") else "Y"
        last = LAST_COMMITTEE.get(p["id"], "")
        dec = "Deferred pending full validation" if last else ""
        wait = (AS_OF - date.fromisoformat(p["submitted"])).days
        rows.append([f"MC-AI-{i:02d}", p["id"], p["name"].strip(), UNITS[p["unit"]][0], p["submitted"], doc,
                     "Full", 2, st, started, val, last, dec, wait])
    return write_csv("governance/model-review-queue-2026-12.csv", header, rows)


def build() -> dict:
    return {"register": register(), "evals": evals(), "intake": intake(), "queue": queue()}
