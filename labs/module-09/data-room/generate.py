"""Meridian Mutual data room generator (module 09).

Rebuilds every generated file in this folder, byte for byte, from a fixed seed:

    python generate.py                      # rewrite the data files
    python generate.py --answer-key DIR     # also write the ground truth (for course writers) to DIR

Python 3.12+, standard library only. Files are UTF-8 (no BOM) with LF line endings. Timestamps are
Israel local time with their UTC offset (+03:00 in summer time, +02:00 in winter time).

How the simulation works, in one paragraph: we simulate every non-bodily-injury claim Meridian
received from 1 November 2024 to 31 October 2026 (motor property, home, health, travel), with the
winter peak, two storm weeks, the intake backlog it causes, the rounds of document requests, the
special investigations unit (SIU), payments and closure. From 6 September 2026 the claims system's
release 9.4 scores every motor claim with "Fraud Insight", a weighted list of rules, and refers high
scores to the SIU automatically. The exports then cut that population the way Meridian's systems
would: a 1-in-40 sample of the claims register, a full motor extract for July-October 2026, the
SIU's own case log, the CRM, the payments ledger, the complaints log. Separately, 240 intake
documents in four languages are written out as OCR text with the values two QA staff verified, and
the claims-system vendor's "Smart Intake" extraction of the same documents.

Hand-written documents (policies, vendor papers, minutes) are not touched by this script; the
documents that quote numbers from the data (KPI dashboard, the COO's pilot proposal, the SIU
summary) are generated so their numbers always match.
"""
from __future__ import annotations

import argparse
import csv
import math
import random
import statistics
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from pathlib import Path

sys.dont_write_bytecode = True

SEED = 20261115
ROOT = Path(__file__).resolve().parent

START = date(2024, 11, 1)          # claims reported from this day
END = date(2026, 10, 31)           # ... to this day
EXPORT_AT = datetime(2026, 11, 4, 9, 12)   # BI pulled the exports on Wednesday 4 November 2026
RELEASE_94 = date(2026, 9, 6)      # Kalanit Claims 9.4 went live (Sunday)
SAMPLE_EVERY = 40                  # claims register: every 40th claim number
MOTOR_EXTRACT_FROM = date(2026, 7, 1)
SIU_LOG_FROM = date(2025, 7, 1)
CRM_FROM = date(2026, 5, 1)        # the CRM export tool keeps six months
COMPLAINTS_FROM = date(2026, 1, 1)
STORMS = [(date(2025, 1, 12), date(2025, 1, 16)), (date(2025, 12, 28), date(2026, 1, 1))]


def rng_for(name: str) -> random.Random:
    """One independent random stream per part, so changing one part never shifts another."""
    return random.Random(f"{SEED}:{name}")


# =============================================================================================
# Time helpers
# =============================================================================================

def _last_sunday(year: int, month: int) -> date:
    d = date(year, month + 1, 1) - timedelta(days=1) if month < 12 else date(year, 12, 31)
    while d.weekday() != 6:
        d -= timedelta(days=1)
    return d


def il_offset(dt: datetime) -> str:
    """Israel: summer time from the Friday before the last Sunday in March to the last Sunday in October."""
    start = _last_sunday(dt.year, 3) - timedelta(days=2)
    end = _last_sunday(dt.year, 10)
    summer = datetime.combine(start, time(2)) <= dt < datetime.combine(end, time(2))
    return "+03:00" if summer else "+02:00"


def ts(dt: datetime | None) -> str:
    if dt is None:
        return ""
    return dt.strftime("%Y-%m-%dT%H:%M:%S") + il_offset(dt)


def ds(d: date | None) -> str:
    return d.isoformat() if d else ""


def is_workday(d: date) -> bool:
    return d.weekday() in (6, 0, 1, 2, 3)   # Sunday-Thursday


def add_workdays(d: date, n: int) -> date:
    while not is_workday(d):
        d += timedelta(days=1)
    while n > 0:
        d += timedelta(days=1)
        if is_workday(d):
            n -= 1
    return d


def workdays_between(a: date, b: date) -> int:
    n, d = 0, a
    while d < b:
        d += timedelta(days=1)
        if is_workday(d):
            n += 1
    return n


def at_office(d: date, r: random.Random, early: int = 8, late: int = 17) -> datetime:
    return datetime.combine(d, time(r.randint(early, late - 1), r.randint(0, 59), r.randint(0, 59)))


def lognorm(r: random.Random, median: float, sigma: float) -> float:
    return median * math.exp(r.gauss(0, sigma))


def poisson(r: random.Random, lam: float) -> int:
    if lam > 30:
        return max(0, round(r.gauss(lam, math.sqrt(lam))))
    k, p, L = 0, 1.0, math.exp(-lam)
    while True:
        p *= r.random()
        if p <= L:
            return k
        k += 1


def pick(r: random.Random, weights: dict):
    keys = list(weights)
    return r.choices(keys, weights=[weights[k] for k in keys])[0]


def in_storm(d: date) -> bool:
    return any(a <= d <= b for a, b in STORMS)


# =============================================================================================
# The business
# =============================================================================================

YEARLY = {"motor": 21000, "home": 9500, "health": 5000, "travel": 2500}
SEASON = {   # month -> multiplier (before normalisation)
    "motor": {11: 1.05, 12: 1.2, 1: 1.3, 2: 1.15, 3: 1.0, 4: 0.95, 5: 0.9, 6: 0.9, 7: 0.95, 8: 0.95, 9: 0.9, 10: 0.95},
    "home": {11: 1.1, 12: 1.8, 1: 2.3, 2: 1.6, 3: 0.9, 4: 0.7, 5: 0.6, 6: 0.6, 7: 0.7, 8: 0.7, 9: 0.7, 10: 0.8},
    "health": {11: 1.05, 12: 1.0, 1: 1.05, 2: 1.0, 3: 1.05, 4: 0.9, 5: 1.0, 6: 1.0, 7: 0.95, 8: 0.85, 9: 1.0, 10: 1.0},
    "travel": {11: 0.8, 12: 0.75, 1: 0.7, 2: 0.7, 3: 0.9, 4: 1.4, 5: 0.9, 6: 1.0, 7: 1.7, 8: 1.8, 9: 1.0, 10: 1.3},
}
for _line, _m in SEASON.items():
    _s = sum(_m.values()) / 12
    for _k in _m:
        _m[_k] /= _s
TOTAL_MONTH_LOAD = {m: sum(YEARLY[l] * SEASON[l][m] for l in YEARLY) / sum(YEARLY.values()) for m in range(1, 13)}

TYPES = {
    "motor": {"own_damage": 0.60, "third_party_property": 0.25, "theft": 0.05, "windscreen": 0.10},
    "home": {"water_damage": 0.55, "storm": 0.20, "burglary": 0.10, "contents_other": 0.15},
    "health": {"surgery_reimbursement": 0.30, "specialist_consult": 0.40, "medications": 0.30},
    "travel": {"medical_abroad": 0.55, "baggage": 0.30, "cancellation": 0.15},
}
AMOUNT_MEDIAN = {"own_damage": 9500, "third_party_property": 7000, "theft": 52000, "windscreen": 1800,
                 "water_damage": 8500, "storm": 12000, "burglary": 18000, "contents_other": 4200,
                 "surgery_reimbursement": 9800, "specialist_consult": 900, "medications": 1300,
                 "medical_abroad": 6200, "baggage": 2800, "cancellation": 5400}
DEDUCTIBLE = {"own_damage": 1950, "third_party_property": 1950, "theft": 3900, "windscreen": 450,
              "water_damage": 1200, "storm": 1200, "burglary": 2500, "contents_other": 1200,
              "surgery_reimbursement": 0, "specialist_consult": 250, "medications": 150,
              "medical_abroad": 0, "baggage": 300, "cancellation": 250}

REGIONS = {"North": 0.26, "Center": 0.36, "Tel Aviv": 0.14, "Jerusalem": 0.11, "South": 0.13}
CENTRE = {"North": "Haifa", "Center": "Ramat Gan", "Tel Aviv": "Ramat Gan", "Jerusalem": "Jerusalem",
          "South": "Beer Sheva"}
LANG_BY_REGION = {
    "North": {"he": 0.52, "ar": 0.38, "ru": 0.08, "en": 0.02},
    "Center": {"he": 0.80, "ar": 0.06, "ru": 0.10, "en": 0.03, "am": 0.01},
    "Tel Aviv": {"he": 0.78, "ar": 0.04, "ru": 0.10, "en": 0.07, "am": 0.01},
    "Jerusalem": {"he": 0.74, "ar": 0.14, "ru": 0.06, "en": 0.05, "am": 0.01},
    "South": {"he": 0.62, "ar": 0.18, "ru": 0.15, "en": 0.01, "am": 0.04},
}
REGION_PREFIX = {"North": "N", "Center": "C", "Tel Aviv": "TA", "Jerusalem": "J", "South": "S"}
AREAS = {"N": 14, "C": 16, "TA": 8, "J": 9, "S": 10}
# The vendor's "risk areas" list (v3, Israel market template). Codes only; see vendor/risk-areas-v3.csv.
RISK_AREAS = ["N-03", "N-05", "N-07", "N-09", "N-11", "S-02", "S-04", "S-06", "J-03", "C-08", "TA-04"]
# Where people mostly live, by region and correspondence language (drives the postal area)
AR_AREAS = {"N": ["N-03", "N-05", "N-07", "N-09", "N-11", "N-13"], "S": ["S-02", "S-04", "S-06"],
            "J": ["J-03", "J-07"], "C": ["C-08", "C-11"], "TA": ["TA-04"]}
AGE_BANDS = {"18-24": 0.07, "25-34": 0.17, "35-44": 0.21, "45-54": 0.19, "55-64": 0.16, "65-74": 0.13, "75+": 0.07}
CHANNELS_PC = {"agent": 0.55, "web": 0.17, "phone": 0.15, "app": 0.11, "email": 0.02}
CHANNELS_HT = {"app": 0.35, "web": 0.33, "agent": 0.15, "phone": 0.11, "email": 0.06}

# Fraud Insight factor library (as configured by the vendor's Israel market template)
FACTORS = [
    ("F01", "Late notification", "Loss notified more than 30 days after the loss date", 15),
    ("F02", "New or increased cover", "Policy inception or increase in cover less than 60 days before the loss", 20),
    ("F03", "Claim frequency", "Two or more prior claims on the policy in 24 months", 15),
    ("F04", "High amount for segment", "Claimed amount above 1.5x the segment median", 10),
    ("F05", "Non-network garage", "Repairs at a garage outside Meridian's network", 10),
    ("F06", "Night loss without police", "Loss between 22:00 and 05:00 with no police report", 10),
    ("F07", "Third-party representative", "Public adjuster or lawyer involved at first notice", 15),
    ("F08", "Interpreter required", "Claimant correspondence flagged as requiring interpreter services", 10),
    ("F09", "Risk area", "Claimant postal area on the risk-area list (risk_areas_v3)", 15),
    ("F10", "Document anomaly", "Document resubmitted or file metadata edited after first upload", 20),
    ("F11", "Shared contact details", "Phone number linked to three or more claimants in 12 months", 25),
    ("F12", "Total loss, older vehicle", "Total-loss claim on a vehicle older than 12 years", 10),
    ("F13", "Young claimant", "Claimant age band 18-24", 5),
    ("F14", "Premium paid on loss date", "Outstanding premium paid on the day of the loss", 15),
]
FW = {f[0]: f[3] for f in FACTORS}
REVIEW_AT, REFER_AT = 35, 50

STD_DOCS = {
    "own_damage": ["claim_form", "driving_licence", "vehicle_licence", "garage_estimate", "photos"],
    "third_party_property": ["claim_form", "driving_licence", "third_party_details", "garage_estimate"],
    "theft": ["claim_form", "police_confirmation", "keys_declaration", "vehicle_licence"],
    "windscreen": ["claim_form", "glass_invoice"],
    "water_damage": ["claim_form", "plumber_report", "contractor_quote", "photos"],
    "storm": ["claim_form", "contractor_quote", "photos"],
    "burglary": ["claim_form", "police_confirmation", "purchase_receipts", "photos"],
    "contents_other": ["claim_form", "purchase_receipts", "photos"],
    "surgery_reimbursement": ["claim_form", "medical_summary", "invoice_receipt"],
    "specialist_consult": ["claim_form", "invoice_receipt", "referral"],
    "medications": ["claim_form", "prescription", "invoice_receipt"],
    "medical_abroad": ["claim_form", "medical_report", "invoice_receipt", "boarding_passes"],
    "baggage": ["claim_form", "airline_pir", "purchase_receipts"],
    "cancellation": ["claim_form", "cancellation_proof", "medical_report"],
}
EXTRA_DOCS = ["bank_details", "assessor_followup_photos", "repair_invoice_final", "statement_of_events",
              "prior_insurer_letter", "medical_records_5y", "bank_statement", "witness_details",
              "translated_document", "original_receipt"]


@dataclass
class Claim:
    seq_pop: int = 0
    claim_id: str = ""
    line: str = ""
    ctype: str = ""
    region: str = ""
    centre: str = ""
    area: str = ""
    lang: str = ""
    interpreter: str = "N"
    age_band: str = ""
    channel: str = ""
    agent_code: str = ""
    policy_id: str = ""
    inception: date | None = None
    loss_date: date | None = None
    loss_hour: int = 12
    fnol_at: datetime | None = None
    reported_date: date | None = None
    registered_at: datetime | None = None
    file_complete_at: datetime | None = None
    decision_at: datetime | None = None
    closed_at: datetime | None = None
    decision: str = ""
    claimed: float = 0.0
    paid: float = 0.0
    deductible: float = 0.0
    rounds: list = field(default_factory=list)   # (requested_at, received_at|None, [docs], on_std list)
    payments: list = field(default_factory=list)  # (payee, amount, approved_at, paid_date)
    true_fraud: bool = False
    factors: list = field(default_factory=list)
    fi_score: int | None = None
    fi_band: str = ""
    siu: bool = False
    siu_source: str = ""
    siu_opened: datetime | None = None
    siu_outcome: str = ""
    siu_closed: datetime | None = None
    investigator: str = ""
    handler: str = ""
    smart_intake: str = "N"
    prior_claims: int = 0
    garage_network: bool = True
    police: bool = False


def seasonal_lambda(line: str, d: date) -> float:
    lam = YEARLY[line] / 365.0 * SEASON[line][d.month]
    if line == "home" and in_storm(d):
        lam *= 4.5
    if line == "motor" and in_storm(d):
        lam *= 1.6
    if line == "motor" and d.weekday() == 4:   # Friday: fewer reports
        lam *= 0.75
    if line == "motor" and d.weekday() == 5:   # Saturday
        lam *= 0.45
    return lam


def simulate_population() -> list[Claim]:
    r = rng_for("population")
    claims: list[Claim] = []
    d = START - timedelta(days=60)
    while d <= END:
        for line in ("motor", "home", "health", "travel"):
            for _ in range(poisson(r, seasonal_lambda(line, d))):
                c = Claim(line=line, loss_date=d)
                c.ctype = pick(r, TYPES[line])
                if line == "home" and in_storm(d):
                    c.ctype = "storm" if r.random() < 0.55 else "water_damage"
                claims.append(c)
        d += timedelta(days=1)

    hid = {"Haifa": 22, "Ramat Gan": 58, "Jerusalem": 14, "Beer Sheva": 16}
    for c in claims:
        c.region = pick(r, REGIONS)
        c.centre = CENTRE[c.region] if c.line in ("motor", "home") else "Ramat Gan"
        c.lang = pick(r, LANG_BY_REGION[c.region])
        pre = REGION_PREFIX[c.region]
        if c.lang == "ar" and r.random() < 0.86:
            c.area = r.choice(AR_AREAS[pre])
        else:
            pool = [f"{pre}-{i:02d}" for i in range(1, AREAS[pre] + 1)]
            non_risk = [a for a in pool if a not in RISK_AREAS and a not in AR_AREAS[pre]]
            c.area = r.choice(non_risk) if r.random() < 0.9 else r.choice(pool)
        c.interpreter = "Y" if c.lang in ("ar", "am") or (c.lang == "ru" and r.random() < 0.55) else "N"
        if c.lang == "ar" and r.random() < 0.12:
            c.interpreter = "N"
        c.age_band = pick(r, AGE_BANDS)
        c.channel = pick(r, CHANNELS_PC if c.line in ("motor", "home") else CHANNELS_HT)
        if c.channel == "agent":
            c.agent_code = f"AG-{r.randint(1001, 1420)}"
        c.policy_id = f"P{r.randint(3000000, 9999999)}"
        # latent truth and the legitimate signals it moves
        base = {"motor": 0.019, "home": 0.012, "health": 0.007, "travel": 0.022}[c.line]
        c.true_fraud = r.random() < base
        tf = c.true_fraud
        c.loss_hour = (r.choice([22, 23, 0, 1, 2, 3, 4]) if r.random() < (0.3 if c.true_fraud else 0.08)
                       else r.randint(5, 21)) if c.line == "motor" else r.randint(6, 22)
        c.inception = c.loss_date - timedelta(days=(r.randint(5, 59) if r.random() < (0.32 if tf else 0.055)
                                                     else r.randint(60, 3000)))
        c.prior_claims = (r.choice([2, 3]) if r.random() < (0.3 if tf else 0.11) else r.choice([0, 0, 0, 1]))
        risk_area = c.area in RISK_AREAS
        c.garage_network = not (r.random() < ((0.55 if risk_area else 0.24) + (0.15 if tf else 0)))
        c.police = c.ctype in ("theft", "burglary") or r.random() < 0.12
        # notice delay
        mean_delay = {"motor": 2.0, "home": 3.0, "health": 10.0, "travel": 12.0}[c.line]
        delay = int(r.expovariate(1 / mean_delay))
        if r.random() < (0.25 if tf else 0.035):
            delay = r.randint(31, 70)
        c.fnol_at = at_office(c.loss_date + timedelta(days=delay), r, 7, 21)
        if c.channel in ("agent",):
            agent_hold = int(r.expovariate(1 / 1.8))
            c.reported_date = (c.fnol_at + timedelta(days=agent_hold)).date()
        else:
            c.reported_date = c.fnol_at.date()
        amt = lognorm(r, AMOUNT_MEDIAN[c.ctype], 0.65)
        if tf:
            amt *= 1.6
        c.claimed = round(amt, -1) if amt > 500 else round(amt)
        c.handler = f"H-{c.centre[:2].upper()}{r.randint(1, hid[c.centre]):02d}"

    claims = [c for c in claims if START <= c.reported_date <= END]
    return claims


def simulate_process(claims: list[Claim]) -> None:
    r = rng_for("process")
    for c in claims:
        load = TOTAL_MONTH_LOAD[c.reported_date.month]
        storm_backlog = 3 if in_storm(c.reported_date) or in_storm(c.reported_date - timedelta(days=5)) else 0
        lag = int(round(r.gammavariate(1.4, 0.9) * load ** 2.2)) + storm_backlog
        reg_day = add_workdays(c.reported_date, lag)
        c.registered_at = at_office(reg_day, r)
        if c.registered_at < c.fnol_at:
            c.registered_at = c.fnol_at + timedelta(hours=r.randint(1, 6))
        # Smart Intake (vendor AI capture) since 9.4: motor claims at Haifa and Ramat Gan
        if c.line == "motor" and c.registered_at.date() >= RELEASE_94 and c.centre in ("Haifa", "Ramat Gan"):
            c.smart_intake = "Y"

    # Fraud Insight score: motor claims registered on/after 9.4 go-live
    for c in claims:
        if c.line != "motor" or c.registered_at.date() < RELEASE_94:
            continue
        tf = c.true_fraud
        f = []
        if (c.reported_date - c.loss_date).days > 30:
            f.append("F01")
        if (c.loss_date - c.inception).days < 60:
            f.append("F02")
        if c.prior_claims >= 2:
            f.append("F03")
        if c.claimed > 1.5 * AMOUNT_MEDIAN[c.ctype]:
            f.append("F04")
        if c.ctype in ("own_damage", "third_party_property") and not c.garage_network:
            f.append("F05")
        if (c.loss_hour >= 22 or c.loss_hour < 5) and not c.police:
            f.append("F06")
        if r.random() < (0.16 if tf else 0.045):
            f.append("F07")
        if c.interpreter == "Y":
            f.append("F08")
        if c.area in RISK_AREAS:
            f.append("F09")
        if r.random() < (0.35 if tf else 0.018):
            f.append("F10")
        if r.random() < (0.2 if tf else 0.008):
            f.append("F11")
        if c.ctype == "theft" and r.random() < 0.3:
            f.append("F12")
        if c.age_band == "18-24":
            f.append("F13")
        if r.random() < (0.2 if tf else 0.02):
            f.append("F14")
        c.factors = f
        c.fi_score = min(100, sum(FW[x] for x in f))
        c.fi_band = "refer" if c.fi_score >= REFER_AT else "review" if c.fi_score >= REVIEW_AT else "none"

    for c in claims:
        load = TOTAL_MONTH_LOAD[c.registered_at.date().month]
        # --- SIU referral ---
        if c.fi_band == "refer":
            c.siu, c.siu_source = True, "fraud_insight_auto"
            c.siu_opened = c.registered_at + timedelta(minutes=r.randint(1, 30))
        else:
            # handlers' own judgement (before and after 9.4); reacts to the same signals and, a little, to language
            p = 0.011
            if (c.reported_date - c.loss_date).days > 30:
                p += 0.10
            if c.prior_claims >= 2:
                p += 0.05
            if c.claimed > 1.8 * AMOUNT_MEDIAN[c.ctype]:
                p += 0.04
            if c.true_fraud:
                p += 0.30
            if c.lang == "ar":
                p *= 1.25
            if c.fi_band == "review":
                p += 0.10
            if c.line == "health":
                p *= 0.4
            if r.random() < p:
                c.siu, c.siu_source = True, "handler"
        # --- documents ---
        first_req_day = add_workdays(c.registered_at.date(), int(r.gammavariate(1.3, 1.5) * load))
        t_req = at_office(first_req_day, r)
        std = STD_DOCS[c.ctype]
        p_next = {"motor": 0.45, "home": 0.50, "health": 0.33, "travel": 0.55}[c.line]
        if c.smart_intake == "Y" and c.lang == "ar":
            p_next += 0.08     # unreadable invoices sent back for a better copy
        if c.siu:
            p_next += 0.15
        nrounds = 1
        while nrounds < 5 and r.random() < p_next:
            nrounds += 1
            p_next *= 0.7
        for k in range(nrounds):
            if k == 0:
                docs = list(std)
                on_std = ["Y"] * len(docs)
            else:
                ndocs = r.choice([1, 1, 1, 2, 2, 3])
                docs, on_std = [], []
                for _ in range(ndocs):
                    if r.random() < 0.46:
                        docs.append(r.choice(std))
                        on_std.append("Y")
                    else:
                        docs.append(r.choice(EXTRA_DOCS))
                        on_std.append("N")
            resp_median = 9 if c.line == "travel" else 5
            got = t_req + timedelta(days=lognorm(r, resp_median, 0.7), hours=r.randint(0, 8))
            c.rounds.append([t_req, got, docs, on_std])
            # handler reviews what arrived, then (maybe) asks for more
            review = int(r.gammavariate(1.5, 2.6) * load)
            if r.random() < 0.16:
                review += r.randint(10, 18)
            t_req = at_office(add_workdays(got.date(), max(1, review)), r)
        last_got = c.rounds[-1][1]
        c.file_complete_at = at_office(add_workdays(last_got.date(), r.choice([0, 0, 1, 1, 2])), r)
        if c.file_complete_at < last_got:
            c.file_complete_at = last_got + timedelta(hours=2)
        # --- SIU work ---
        decision_lag = max(1, int(round(r.gammavariate(2.0, 3.4) * load ** 1.6)))
        decision_day = add_workdays(c.file_complete_at.date(), decision_lag)
        if c.siu:
            if c.siu_source == "handler":
                c.siu_opened = at_office(add_workdays(c.registered_at.date(), r.randint(2, 12)), r)
            field_work = r.random() < (0.45 if c.true_fraud else 0.15)
            inv_days = r.randint(25, 70) if field_work else r.randint(8, 30)
            c.siu_closed = at_office(add_workdays(max(c.siu_opened.date(), c.file_complete_at.date()), inv_days), r)
            c.investigator = r.choice(["SIU-01", "SIU-02", "SIU-03", "SIU-04", "SIU-05", "SIU-06", "EXT-ORION", "EXT-TAVOR"])
            if c.true_fraud and r.random() < 0.72:
                c.siu_outcome = "confirmed_fraud"
            else:
                wait = (c.siu_closed - c.fnol_at).days
                c.siu_outcome = "claimant_withdrew" if r.random() < min(0.2, 0.02 + wait / 500) else "no_finding"
            decision_day = max(decision_day, add_workdays(c.siu_closed.date(), r.randint(1, 4)))
        c.decision_at = at_office(decision_day, r)
        # --- decision and money ---
        c.deductible = DEDUCTIBLE[c.ctype]
        if c.siu_outcome == "confirmed_fraud":
            c.decision, c.paid = "declined", 0.0
        elif c.siu_outcome == "claimant_withdrew" or (not c.siu and r.random() < 0.025):
            c.decision, c.paid = "withdrawn", 0.0
        else:
            u = r.random()
            if u < 0.075:
                c.decision, c.paid = "declined", 0.0
            elif u < 0.24:
                c.decision = "partial"
                c.paid = max(0.0, round(c.claimed * r.uniform(0.45, 0.85) - c.deductible, -1))
            else:
                c.decision = "paid"
                c.paid = max(0.0, round(c.claimed * r.uniform(0.92, 1.0) - c.deductible, -1))
            if c.paid <= 0:
                c.decision, c.paid = "declined", 0.0
        # payments: ERP runs on Monday and Thursday
        if c.paid > 0:
            pay_day = add_workdays(c.decision_at.date(), 1)
            while pay_day.weekday() not in (0, 3):
                pay_day += timedelta(days=1)
            if c.ctype in ("own_damage", "third_party_property") and r.random() < 0.7:
                g = round(c.paid * r.uniform(0.75, 1.0), -1)
                c.payments.append(("garage", g, c.decision_at, pay_day))
                if c.paid - g > 0:
                    c.payments.append(("claimant", round(c.paid - g, 2), c.decision_at, pay_day))
            else:
                c.payments.append(("claimant", c.paid, c.decision_at, pay_day))
        if c.line == "motor" and c.ctype != "windscreen" and r.random() < 0.85:
            fee_day = add_workdays(c.registered_at.date(), r.randint(8, 25))
            while fee_day.weekday() not in (0, 3):
                fee_day += timedelta(days=1)
            c.payments.append(("assessor", float(r.choice([620, 680, 740, 790, 850])),
                               at_office(fee_day - timedelta(days=2), r), fee_day))
        last_money = max([p[3] for p in c.payments], default=c.decision_at.date())
        close_day = add_workdays(max(last_money, c.decision_at.date()), r.randint(1, 12))
        c.closed_at = at_office(close_day, r)


def number_claims(claims: list[Claim]) -> None:
    claims.sort(key=lambda c: (c.registered_at, c.policy_id))
    per_year: dict[int, int] = {}
    for i, c in enumerate(claims):
        y = c.registered_at.year
        per_year[y] = per_year.get(y, 0) + 1
        c.seq_pop = i + 1
        c.claim_id = f"CL-{y}-{per_year[y]:06d}"


def cut_at_export(c: Claim):
    """What the systems knew on 4 November 2026."""
    cut = EXPORT_AT
    known = lambda t: t if t is not None and t <= cut else None  # noqa: E731
    return {
        "file_complete_at": known(c.file_complete_at),
        "decision_at": known(c.decision_at),
        "closed_at": known(c.closed_at),
        "siu_closed": known(c.siu_closed),
    }


# =============================================================================================
# Named claim: the claimant persona (Samira Abu-Ahmad)
# =============================================================================================

def plant_samira(claims: list[Claim]) -> Claim:
    r = rng_for("samira")
    c = Claim(line="motor", ctype="own_damage", region="North", centre="Haifa", area="N-07", lang="ar",
              interpreter="Y", age_band="55-64", channel="phone", policy_id="P5803317",
              loss_date=date(2026, 9, 14), loss_hour=17)
    c.inception = date(2014, 3, 1)
    c.prior_claims = 2
    c.garage_network = False
    c.police = False
    c.fnol_at = datetime(2026, 9, 15, 9, 41, 12)
    c.reported_date = date(2026, 9, 15)
    c.registered_at = datetime(2026, 9, 17, 11, 5, 40)
    c.smart_intake = "Y"
    c.claimed = 16480.0
    c.handler = "H-HA07"
    c.factors = ["F03", "F04", "F05", "F08", "F09"]
    c.fi_score = 60
    c.fi_band = "refer"
    c.siu, c.siu_source = True, "fraud_insight_auto"
    c.siu_opened = datetime(2026, 9, 17, 11, 19, 2)
    c.rounds = [
        [datetime(2026, 9, 20, 10, 2, 0), datetime(2026, 9, 24, 13, 10, 0),
         ["claim_form", "driving_licence", "vehicle_licence", "garage_estimate", "photos"], ["Y"] * 5],
        [datetime(2026, 10, 1, 9, 30, 0), datetime(2026, 10, 5, 12, 0, 0),
         ["police_confirmation", "photos"], ["N", "Y"]],
        [datetime(2026, 10, 12, 14, 20, 0), datetime(2026, 10, 14, 10, 45, 0),
         ["garage_estimate", "statement_of_events"], ["Y", "N"]],
    ]
    c.file_complete_at = datetime(2026, 10, 14, 15, 2, 0)
    c.siu_closed = datetime(2026, 10, 22, 12, 40, 0)
    c.investigator = "SIU-03"
    c.siu_outcome = "no_finding"
    c.decision_at = datetime(2026, 10, 25, 10, 15, 0)
    c.decision = "paid"
    c.deductible = 1950.0
    c.paid = 14530.0
    c.payments = [("assessor", 740.0, datetime(2026, 9, 27, 9, 0), date(2026, 9, 28)),
                  ("garage", 14530.0, c.decision_at, date(2026, 10, 29))]
    c.closed_at = None
    c.true_fraud = False
    claims.append(c)
    _ = r
    return c


# =============================================================================================
# Writers
# =============================================================================================

def write_csv(rel: str, header: list[str], rows: list[list], root: Path = ROOT) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def write_text(rel: str, text: str, root: Path = ROOT) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def money(x: float) -> str:
    return f"{x:.2f}"


def fmt_ils(x: float) -> str:
    return f"₪{x:,.0f}"


# --- claims register (1-in-40 sample) --------------------------------------------------------

REG_HEADER = ["claim_id", "policy_id", "line", "claim_type", "claims_centre", "region", "postal_area",
              "channel", "agent_code", "claimant_lang", "interpreter_flag", "claimant_age_band",
              "policy_inception_date", "loss_date", "reported_date", "registered_at", "file_complete_at",
              "decision_at", "closed_at", "status", "decision", "claimed_amount", "paid_amount",
              "deductible", "doc_request_rounds", "siu_referred", "fraud_flag", "fi_score", "fi_band",
              "fi_factors", "smart_intake", "handler_id"]


def register_row(c: Claim, r: random.Random) -> list:
    k = cut_at_export(c)
    status = "closed" if k["closed_at"] else "open"
    decided = k["decision_at"] is not None
    age = c.age_band
    if c.channel == "agent" and r.random() < 0.31:
        age = ""                              # agents' portal does not require the date of birth
    region = c.region
    if c.centre == "Haifa" and r.random() < 0.04:
        region = "צפון"                       # free-text region typed in Hebrew on some Haifa records
    return [c.claim_id, c.policy_id, c.line, c.ctype, c.centre, region, c.area, c.channel, c.agent_code,
            c.lang, c.interpreter, age, ds(c.inception), ds(c.loss_date), ds(c.reported_date),
            ts(c.registered_at), ts(k["file_complete_at"]), ts(k["decision_at"]), ts(k["closed_at"]),
            status, c.decision if decided else "", money(c.claimed), money(c.paid) if decided else "",
            money(c.deductible), sum(1 for x in c.rounds if x[0] <= EXPORT_AT),
            "Y" if c.siu and c.siu_opened <= EXPORT_AT else "N",
            "SUSPECT" if c.siu and c.siu_opened <= EXPORT_AT else "",
            "" if c.fi_score is None else c.fi_score, c.fi_band, ";".join(c.factors), c.smart_intake, c.handler]


# =============================================================================================
# Free text banks (CRM notes, complaints)
# =============================================================================================

FNOL_NOTES = {
    "he": ["פתיחת תביעה טלפונית, נשלח קישור להעלאת מסמכים", "הודעה על נזק התקבלה באתר, המבוטח ביקש שיחזרו אליו",
           "המבוטח מסר פרטי אירוע, הוסבר תהליך השמאי", "פתיחת תביעה באפליקציה, צולמו תמונות"],
    "ar": ["فتح مطالبة هاتفياً، تم إرسال رابط لرفع المستندات", "بلاغ عن ضرر عبر الموقع، المؤمن يطلب اتصالاً بالعربية",
           "المؤمن أعطى تفاصيل الحادث، تم شرح مسار المخمن"],
    "ru": ["Открыта претензия по телефону, отправлена ссылка для загрузки документов",
           "Заявление через сайт, клиент просит звонить на русском", "Клиент описал событие, объяснили про оценщика"],
    "en": ["Claim opened by phone, upload link sent", "Web notice received, customer asked for a call back in English"],
    "am": ["פתיחת תביעה, המבוטחת ביקשה שיחה עם דובר אמהרית - אין נציג זמין, הוסבר בעברית"],
}
CHASE_NOTES = {
    "he": ["המבוטח מברר מה סטטוס התביעה, נאמר לו שממתינים למסמכים", "שיחה חוזרת - המבוטח לא הבין אילו מסמכים חסרים",
           "המבוטח כועס, שלח כבר את הצעת המחיר פעמיים", "בירור סטטוס, הועבר למטפל", "המבוטח שואל למה התיק בבדיקה מיוחדת",
           "המוסך מתקשר, מחכה לאישור תשלום"],
    "ar": ["المؤمن يسأل عن حالة المطالبة، قيل له إننا ننتظر مستندات", "اتصال متكرر - لم يفهم ما هي المستندات الناقصة",
           "المؤمنة غاضبة، أرسلت الفاتورة مرتين", "يسأل لماذا الملف تحت فحص خاص"],
    "ru": ["Клиент спрашивает статус, сказали что ждём документы", "Повторный звонок - не понял, каких документов не хватает",
           "Клиентка недовольна, уже дважды отправляла счёт", "Спрашивает, почему дело на особой проверке"],
    "en": ["Customer asking for status, told we are waiting for documents", "Second call - unclear which documents are missing"],
    "am": ["בירור סטטוס, שיחה בעברית בסיוע הבן של המבוטחת"],
}
SHADOW_NOTES = [   # (language of the note, note): two for Arabic claims, two for Russian, two for the rest
    ("he", "המכתב בערבית תורגם בצ'אט GPT ונשלח לתיק"),
    ("he", "מכתב התשובה בערבית נוסח בעזרת צ'אט GPT, נא לבדוק לפני שליחה"),
    ("he", "תרגמתי את סיכום האשפוז מרוסית עם ChatGPT, מצורף לתיק"),
    ("ru", "Перевела выписку из клиники через ChatGPT, загрузила в дело"),
    ("he", "הקבלה מחו\"ל תורגמה בג'מיני, הסכום אומת מול כרטיס האשראי"),
    ("en", "Used ChatGPT to translate the hospital invoice from abroad"),
]
COMPLAINT_TEXT = {
    "delay": "המבוטח מתלונן על עיכוב בתשלום התביעה מעל חודש",
    "documents": "המבוטח מתלונן שנדרש להמציא מסמכים שכבר שלח / מסמכים שלא נדרשו בתחילה",
    "investigation": "המבוטח מתלונן שהתיק הועבר לחקירה ללא הסבר ושהתשלום עוכב",
    "decision": "המבוטח חולק על גובה הפיצוי / דחיית התביעה",
    "service": "המבוטח מתלונן על יחס הנציגים / חוסר מענה בשפתו",
    "language": "המבוטח מתלונן שהמכתבים נשלחו בעברית למרות בקשה לערבית/רוסית",
}


def main(answer_key: Path | None = None) -> None:
    claims = simulate_population()
    simulate_process(claims)
    samira = plant_samira(claims)
    number_claims(claims)
    pop_motor_after = [c for c in claims if c.line == "motor" and c.registered_at.date() >= RELEASE_94]
    stats: dict = {"population": len(claims)}

    # ---------- claims register sample ----------
    r = rng_for("register")
    sample = [c for c in claims if c.seq_pop % SAMPLE_EVERY == 0 and c.registered_at <= EXPORT_AT]
    write_csv("claims/claims_register_sample.csv", REG_HEADER, [register_row(c, r) for c in sample])
    stats["sample"] = len(sample)

    # ---------- document requests (sample): one row per request letter ----------
    rows = []
    rid = 0
    for c in sample:
        for k, (req, got, docs, on_std) in enumerate(c.rounds, start=1):
            if req > EXPORT_AT:
                continue
            rid += 1
            rows.append([f"DR{rid:06d}", c.claim_id, k, ts(req), ";".join(docs), sum(1 for x in on_std if x == "Y"),
                         ts(got) if got <= EXPORT_AT else ""])
    write_csv("claims/doc_requests.csv", ["request_id", "claim_id", "round", "requested_at", "documents_requested",
                                          "n_on_standard_list", "all_received_at"], rows)
    stats["doc_requests"] = len(rows)

    # ---------- payments ledger (sample) ----------
    rows = []
    pid = 0
    for c in sample:
        for payee, amt, appr, paid_day in c.payments:
            if datetime.combine(paid_day, time(6)) > EXPORT_AT:
                continue
            pid += 1
            rows.append([f"PAY-{pid:06d}", c.claim_id, payee, money(amt), ts(appr), ds(paid_day)])
    write_csv("finance/claim_payments.csv", ["payment_id", "claim_id", "payee_type", "amount_ils",
                                             "approved_at", "paid_date"], rows)
    stats["payments"] = len(rows)

    # ---------- CRM contacts (sample, direct channels, May-Oct 2026) ----------
    r = rng_for("crm")
    rows = []
    cid = 0
    shadow_i = 0
    for c in sample:
        if c.channel == "agent" or c.fnol_at.date() < CRM_FROM or c.fnol_at > EXPORT_AT:
            continue
        cid += 1
        lang = c.lang if c.lang in FNOL_NOTES else "he"
        note = r.choice(FNOL_NOTES[lang])
        ref = c.claim_id if r.random() > 0.13 else ""          # FNOL often logged before the claim number exists
        rows.append([f"CT{cid:06d}", ts(c.fnol_at), c.channel if c.channel != "web" else "web_form", "fnol",
                     ref, c.policy_id, c.lang, f"A{r.randint(101, 164)}", note])
        k = cut_at_export(c)
        end = k["decision_at"] or EXPORT_AT
        waited = (end - c.fnol_at).days
        n_chase = max(0, int((waited - 8) / 10 + r.gauss(0, 0.8)))
        if c.siu:
            n_chase += 1
        for _ in range(n_chase):
            t = c.fnol_at + timedelta(days=r.uniform(6, max(7, waited)))
            if t > EXPORT_AT:
                continue
            t = at_office(t.date(), r) if is_workday(t.date()) else at_office(add_workdays(t.date(), 1), r)
            cid += 1
            rows.append([f"CT{cid:06d}", ts(t), r.choice(["phone", "phone", "phone", "whatsapp", "email"]),
                         "status_chase", c.claim_id if r.random() > 0.05 else "", c.policy_id, c.lang,
                         f"A{r.randint(101, 164)}", r.choice(CHASE_NOTES[lang])])
        foreign = c.ctype == "medical_abroad" or (c.line in ("health", "travel") and c.lang in ("ru", "ar", "en"))
        if foreign and r.random() < 0.6:
            pool = SHADOW_NOTES[:2] if c.lang == "ar" else SHADOW_NOTES[2:4] if c.lang == "ru" else SHADOW_NOTES[4:]
            l, txt = pool[shadow_i % 2]
            shadow_i += 1
            t = c.rounds[0][1] + timedelta(days=1)
            if t <= EXPORT_AT:
                t = at_office(t.date(), r)
                cid += 1
                rows.append([f"CT{cid:06d}", ts(t), "internal_note", "handler_note", c.claim_id, c.policy_id,
                             l, c.handler, txt])
    rows.sort(key=lambda x: (x[1], x[0]))
    for i, row in enumerate(rows, start=1):
        row[0] = f"CT{i:06d}"
    write_csv("claims/crm_contacts.csv", ["contact_id", "contact_at", "channel", "contact_type", "claim_id",
                                          "policy_id", "language", "agent_or_user", "note"], rows)
    stats["crm"] = len(rows)
    stats["crm_shadow"] = shadow_i

    # ---------- motor extract Jul-Oct 2026 (full population) ----------
    r = rng_for("motor-extract")
    motor = [c for c in claims if c.line == "motor" and MOTOR_EXTRACT_FROM <= c.registered_at.date() <= END]
    rows = []
    for c in motor:
        k = cut_at_export(c)
        rows.append([c.claim_id, ds(c.registered_at.date()), c.ctype,
                     c.region, c.area, c.channel, c.lang, c.interpreter, c.age_band, ds(c.loss_date),
                     ds(c.reported_date), money(c.claimed),
                     "" if c.fi_score is None else c.fi_score, c.fi_band, ";".join(c.factors),
                     "Y" if c.siu else "N", c.siu_source, c.siu_outcome if k["siu_closed"] else ("open" if c.siu else ""),
                     ds(k["decision_at"].date()) if k["decision_at"] else "", c.decision if k["decision_at"] else "",
                     money(c.paid) if k["decision_at"] else ""])
    write_csv("claims/motor_claims_2026-07_to_10.csv",
              ["claim_id", "registered_date", "claim_type", "region", "postal_area", "channel",
               "claimant_lang", "interpreter_flag", "claimant_age_band", "loss_date", "reported_date",
               "claimed_amount", "fi_score", "fi_band", "fi_factors", "siu_referred", "referral_source",
               "siu_outcome", "decision_date", "decision", "paid_amount"], rows)
    stats["motor_extract"] = len(rows)

    # ---------- SIU case log (all referrals opened since 1 Jan 2025) ----------
    siu = [c for c in claims if c.siu and c.siu_opened.date() >= SIU_LOG_FROM and c.siu_opened <= EXPORT_AT]
    siu.sort(key=lambda c: c.siu_opened)
    rows = []
    for i, c in enumerate(siu, start=1):
        k = cut_at_export(c)
        closed = k["siu_closed"]
        outcome = c.siu_outcome if closed else "open"
        saved = ""
        if closed and k["decision_at"]:
            saved = money(max(0.0, c.claimed - c.paid))
        rows.append([f"SIU-{c.siu_opened.year}-{i:05d}", c.claim_id, c.line, c.ctype, c.region, ts(c.siu_opened),
                     c.siu_source, "" if c.fi_score is None else c.fi_score, c.investigator if closed or True else "",
                     "closed" if closed else "open", outcome, ts(closed), money(c.claimed), saved])
    write_csv("siu/siu_case_log.csv", ["siu_case_id", "claim_id", "line", "claim_type", "region", "opened_at",
                                       "referral_source", "fi_score", "investigator", "status", "outcome",
                                       "closed_at", "claimed_amount", "amount_saved_reported"], rows)
    stats["siu_log"] = len(rows)

    # ---------- complaints log (population, Jan-Oct 2026) ----------
    r = rng_for("complaints")
    rows = []
    n = 0
    for c in claims:
        if c.registered_at.date() < COMPLAINTS_FROM - timedelta(days=60):
            continue
        k = cut_at_export(c)
        end = k["decision_at"] or EXPORT_AT
        waited = (end - c.fnol_at).days
        p = 0.0035 + max(0, waited - 30) * 0.0006
        topic = "delay"
        if c.siu and (c.siu_outcome in ("no_finding", "") or not k["siu_closed"]):
            p += 0.07
            topic = "investigation"
        if len(c.rounds) >= 3:
            p += 0.006
            if topic == "delay" and r.random() < 0.6:
                topic = "documents"
        if r.random() < 0.004:
            topic = r.choice(["decision", "service", "language"])
            p += 0.01
        if c is samira:
            p = 1.0
        if r.random() >= p:
            continue
        t = c.fnol_at + timedelta(days=r.randint(18, 45), hours=r.randint(0, 9))
        if c is samira:
            t = datetime(2026, 10, 12, 16, 22, 0)
        if t.date() < COMPLAINTS_FROM or t > EXPORT_AT:
            continue
        n += 1
        via = "CMISA_public_inquiries" if r.random() < 0.22 else "direct"
        if c is samira:
            via, topic = "direct", "investigation"
        rows.append([t.date(), f"PN-2026-{n:04d}", c.claim_id, c.line, c.region, c.lang, via, topic,
                     COMPLAINT_TEXT[topic] + ("" if c is not samira else
                                              ". לטענתה נאמר לה שהמחשב סימן את התיק, נדרשה להביא אישור משטרה שלא נדרש במקור וחיכתה מעל חודש")])
    rows.sort(key=lambda x: (x[0], x[1]))
    rows = [[ds(x[0])] + x[1:] for x in rows]
    write_csv("complaints/complaints_log_2026.csv", ["received_date", "complaint_id", "claim_id", "line", "region",
                                                     "claimant_lang", "received_via", "topic_code", "summary_he"], rows)
    stats["complaints"] = len(rows)

    # ---------- KPI dashboard (population) ----------
    write_text("reports/claims-kpi-dashboard-2026-10.md", kpi_dashboard(claims, stats))
    write_text("plans/pilot-proposal-2026-11.md", pilot_proposal(stats))

    # ---------- vendor configuration exports ----------
    write_vendor_config()

    # ---------- time study ----------
    write_time_study()

    # ---------- extraction documents ----------
    write_extraction()

    if answer_key:
        write_answer_key(answer_key, claims, sample, samira)
    summary(claims, sample, samira, stats)


def _median(xs):
    return statistics.median(xs) if xs else float("nan")


def kpi_dashboard(claims: list[Claim], stats: dict) -> str:
    months = [(2025, m) for m in range(11, 13)] + [(2026, m) for m in range(1, 11)]
    lines = []
    rows = []
    for y, m in months:
        dec = [c for c in claims if c.decision_at and c.decision_at <= EXPORT_AT
               and c.decision_at.year == y and c.decision_at.month == m]
        std = [c for c in dec if not c.siu]
        days = [(c.decision_at - c.file_complete_at).total_seconds() / 86400 for c in std]
        avg = sum(days) / len(days)
        within = sum(1 for x in days if x <= 30) / len(days)
        reg = [c for c in claims if c.registered_at.year == y and c.registered_at.month == m]
        siu_closed = [c for c in claims if c.siu and c.siu_closed and c.siu_closed <= EXPORT_AT
                      and c.siu_closed.year == y and c.siu_closed.month == m and c.decision_at <= EXPORT_AT]
        saved = sum(max(0.0, c.claimed - c.paid) for c in siu_closed)
        rows.append((y, m, len(reg), len(dec), avg, within, len(siu_closed), saved))
    ytd = [x for x in rows if x[0] == 2026]
    ytd_saved = sum(x[7] for x in ytd)
    stats["kpi_avg_oct"] = rows[-1][4]
    stats["kpi_avg_ytd"] = sum(x[4] * x[3] for x in ytd) / sum(x[3] for x in ytd)
    stats["kpi_within_ytd"] = sum(x[5] * x[3] for x in ytd) / sum(x[3] for x in ytd)
    stats["kpi_saved_ytd"] = ytd_saved
    lines.append("# Claims division — monthly KPI dashboard, October 2026\n")
    lines.append("Prepared by BI for the COO and the management meeting, 3 November 2026. Source: Kalanit Claims "
                 "(operational reports) and the SIU monthly return. Figures are for the whole company.\n")
    lines.append("## Headline\n")
    lines.append(f"- **Average claim handling time: {stats['kpi_avg_ytd']:.1f} days** (year to date; October "
                 f"{rows[-1][4]:.1f} days). Target: 14 days.")
    lines.append(f"- **Claims settled within 30 days: {stats['kpi_within_ytd'] * 100:.1f}%** (year to date). "
                 "Regulatory clock: 30 days.")
    lines.append(f"- **Fraud prevented year to date: {fmt_ils(ytd_saved)}** (SIU).")
    lines.append("- Kalanit 9.4 upgrade completed on 6 September: new intake screens, Smart Intake (motor, Haifa and "
                 "Ramat Gan), Fraud Insight live for motor.\n")
    lines.append("## By month\n")
    lines.append("| Month | Claims registered | Claims decided | Avg handling time (days) | Within 30 days | "
                 "SIU cases closed | Fraud prevented (₪) |")
    lines.append("|---|---|---|---|---|---|---|")
    for y, m, nreg, ndec, avg, within, nsiu, saved in rows:
        lines.append(f"| {y}-{m:02d} | {nreg:,} | {ndec:,} | {avg:.1f} | {within * 100:.1f}% | {nsiu} | {saved:,.0f} |")
    lines.append("")
    lines.append("## Definitions (BI data dictionary, v2.3)\n")
    lines.append("- *Handling time*: calendar days from status \"file complete\" to status \"decision\", claims decided in "
                 "the month. Claims under special handling (SIU) are reported separately and are not included.")
    lines.append("- *Within 30 days*: share of the same claims with handling time of 30 days or less.")
    lines.append("- *Fraud prevented*: for SIU cases closed in the month, the amount claimed minus the amount paid.")
    lines.append("- Bodily-injury and compulsory motor (חובה) claims are out of scope of this dashboard.\n")
    lines.append("## Notes\n")
    lines.append("- December-February volumes are seasonal (storms, motor). Staffing plan for winter 2026/27: 6 temporary "
                 "intake clerks from 1 December (approved).")
    lines.append("- Fraud Insight referrals have increased the SIU queue since September; SIU asked for two more "
                 "external investigator days a week.")
    return "\n".join(lines) + "\n"


def pilot_proposal(stats: dict) -> str:
    avg = stats["kpi_avg_ytd"]
    saved = stats["kpi_saved_ytd"]
    return f"""# Proposal: AI in claims — winter pilot

*From: Ilana Bar-Lev, COO. To: CEO; cc: VP Claims, CFO, Chief Risk Officer. Draft 2, 1 November 2026.
For the management meeting on 10 November and the board risk committee on 15 December 2026.*

## The ask

Approve a three-month pilot, **1 December 2026 – 28 February 2027**, to automate claims intake and
spot fraud with the capabilities we already have in Kalanit 9.4, and buy the Fraud Insight Pro module.

## Why now

- Our average claim handling time is **{avg:.1f} days** (BI dashboard). Customers and agents still
  complain that claims are slow. Competitors advertise "approval in 48 hours".
- Intake is manual: clerks key every form and invoice. Smart Intake (AI document capture) is live on
  motor in Haifa and Ramat Gan since September and the vendor reports **97.4% field accuracy**.
- Fraud is a growing cost. The SIU prevented **{fmt_ils(saved)}** this year with mostly manual work.
  The vendor estimates fraud at about 10% of claims paid in the market; Fraud Insight already
  refers the riskiest motor claims to the SIU automatically.

## The pilot

1. Smart Intake for all motor and home claims in all four centres from 1 December.
2. Fraud Insight extended to home claims (storm and water damage) from 1 December, in time for the
   winter.
3. Fraud Insight Pro (network analytics, image forensics): ₪380,000 a year, three-year term,
   vendor discount of 15% if signed by 31 December.
4. The new head of AI transformation runs the pilot and reports to me.

## Targets (by 28 February)

- Intake keying time −60%.
- Handling time −30% (from {avg:.1f} to {avg * 0.7:.1f} days).
- Fraud leakage: ₪20M a year identified (run rate).

## Budget

Pilot: ₪240,000 from the 2027 AI programme budget (₪1.6M, approved in principle by the board in
October) plus the Fraud Insight Pro licence. Temporary intake clerks for the winter are already in
the claims budget.

## Risks

Change management in the claims centres during the winter peak. Vendor dependency. I propose the
risk committee is informed on 15 December.
"""


def write_vendor_config() -> None:
    rows = [[f[0], f[1], f[2], f[3], "Y", "IL_MARKET_TEMPLATE_2026.2", "2026-09-06"] for f in FACTORS]
    rows.append(["THRESHOLD_REVIEW", "Review band", "Score at or above which the claim shows an amber 'review' badge",
                 REVIEW_AT, "Y", "IL_MARKET_TEMPLATE_2026.2", "2026-09-06"])
    rows.append(["THRESHOLD_REFER", "Auto-referral", "Score at or above which the claim is routed to the SIU queue and "
                 "payment approval is held", REFER_AT, "Y", "IL_MARKET_TEMPLATE_2026.2", "2026-09-06"])
    write_csv("vendor/fraud-insight-config-export.csv", ["rule_id", "name", "description", "weight_or_value", "enabled",
                                                         "source_template", "effective_from"], rows)
    rows = [[a, "risk_areas_v3", "consortium loss data 2019-2021, vendor analysis", "2023-04-30"] for a in RISK_AREAS]
    write_csv("vendor/risk-areas-v3.csv", ["area_code", "list", "basis", "list_date"], rows)


# =============================================================================================
# Intake time study (QA, October 2026)
# =============================================================================================

def write_time_study() -> None:
    r = rng_for("timestudy")
    rows = []
    days = [date(2026, 10, d) for d in range(4, 30) if is_workday(date(2026, 10, d))]
    for i in range(1, 121):
        centre = pick(r, {"Haifa": 0.3, "Ramat Gan": 0.45, "Jerusalem": 0.12, "Beer Sheva": 0.13})
        line = pick(r, {"motor": 0.55, "home": 0.25, "health": 0.12, "travel": 0.08})
        if line in ("health", "travel"):
            centre = "Ramat Gan"
        lang = pick(r, LANG_BY_REGION["North" if centre == "Haifa" else "South" if centre == "Beer Sheva" else "Center"])
        si = "Y" if line == "motor" and centre in ("Haifa", "Ramat Gan") else "N"
        docs = r.randint(2, 7)
        sort_min = round(lognorm(r, 2.1, 0.4) * (1 + docs / 10), 1)
        key_min = round(lognorm(r, 6.4, 0.35) * (1 + (docs - 4) / 12), 1)
        verify_min = 0.0
        if si == "Y":
            key_min = round(key_min * r.uniform(0.35, 0.55), 1)
            verify_min = round(lognorm(r, 2.8 if lang != "ar" else 4.6, 0.35), 1)
        missing = r.random() < 0.58
        search_min = round(lognorm(r, 9.0, 0.5), 1) if missing else round(lognorm(r, 1.2, 0.5), 1)
        note = ""
        if missing:
            note = r.choice(["missing garage estimate, phoned the claimant", "police confirmation not attached, emailed agent",
                             "photos unreadable, asked for new ones", "searched the shared mailbox for the attachments",
                             "agent sent documents in three separate emails"])
        if si == "Y" and lang == "ar" and r.random() < 0.5:
            note = "Smart Intake left amounts blank on the Arabic invoice, keyed by hand"
        rows.append([f"TS{i:03d}", ds(r.choice(days)), centre, line, lang, docs, si, sort_min, key_min, verify_min,
                     search_min, note])
    write_csv("ops/intake-time-study-2026-10.csv", ["obs_id", "observed_date", "claims_centre", "line",
                                                    "claimant_lang", "documents_in_set", "smart_intake_used",
                                                    "minutes_sorting", "minutes_keying", "minutes_verifying_prefill",
                                                    "minutes_finding_missing_docs", "observer_note"], rows)


# =============================================================================================
# Extraction set: 240 intake documents, gold values, vendor Smart Intake output
# =============================================================================================

EA = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
RU_MONTHS = ["янв.", "февр.", "марта", "апр.", "мая", "июня", "июля", "авг.", "сент.", "окт.", "нояб.", "дек."]
EN_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

GARAGES_HE = ["מוסך השרון", "מוסך אחים כהן", "מרכז שירות גלבוע", "מוסך הכרמל", "פחחות וצבע דוד", "מוסך אור יהודה"]
GARAGES_AR = ["كراج الأمل", "كراج أبو صالح", "مركز الخدمة الحديث", "كراج النجمة"]
CONTRACTORS_HE = ["אינסטלציה מהירה", "שיפוצי יוסי", "ש.ב. איטום וצנרת"]
CONTRACTORS_RU = ["Сантехник Борис", "Ремонт под ключ Игорь", "Вадим — отделочные работы"]
CONTRACTORS_AR = ["مؤسسة سامي للترميم", "تمديدات صحية الحاج"]
CLINICS_EN = [("Mercy Urgent Care, Orlando FL", "USD", "us"), ("St. Mary's Walk-in Centre, London", "GBP", "uk"),
              ("Clinica Salus, Barcelona", "EUR", "eu"), ("Bangkok Riverside Hospital", "THB", "eu"),
              ("Harbor Medical Group, New York NY", "USD", "us")]
CLINICS_RU = [("Медицинский центр «Медис», Батуми", "GEL"), ("Клиника «Здоровье», Тбилиси", "USD"),
              ("Медицинский центр «Авиценна», Ереван", "AMD")]
STATIONS = ["תחנת חדרה", "תחנת נצרת עילית", "תחנת זבולון", "תחנת רמת גן", "תחנת באר שבע", "תחנת שפרעם",
            "תחנת מוריה", "תחנת כרמיאל"]
DIAG_EN = ["acute gastroenteritis", "sprained ankle, X-ray negative", "otitis media", "lower back pain"]
DIAG_RU = ["острый гастроэнтерит", "растяжение связок голеностопа", "отит", "пищевое отравление"]
DIAG_HE = ["דלקת גרון", "כאבי גב תחתון", "בדיקת עיניים - קטרקט"]
DIAG_AR = ["التهاب الحلق", "ألم أسفل الظهر"]
ASSESSORS = ["אבי לוי", "ח'אלד מנסור", "ולדימיר שור", "רונית בן דוד"]
DESC_HE = ["נסעתי ברחוב ורכב פגע בי מאחור ברמזור", "הרכב חנה ליד הבית ונמצא עם פגיעה בדלת", "החלקתי בגשם ופגעתי בעמוד",
           "צינור התפוצץ במטבח והמים הציפו את הסלון", "בסערה נשבר החלון ונכנסו מים לחדר"]
DESC_AR = ["كنت أقود في الشارع وصدمتني سيارة من الخلف عند الإشارة", "السيارة كانت مركونة قرب البيت ووجدتها مضروبة في الباب",
           "انفجر أنبوب في المطبخ وغمرت المياه الصالون"]
DESC_RU = ["Стоял на светофоре, сзади въехала машина", "Машина стояла у дома, обнаружил вмятину на двери",
           "В ванной прорвало трубу, затопило соседей снизу"]


def fmt_date(d: date, style: str) -> str:
    if style == "dmy_slash":
        return d.strftime("%d/%m/%Y")
    if style == "dmy_dot":
        return d.strftime("%d.%m.%Y")
    if style == "mdy_slash":
        return d.strftime("%m/%d/%Y")
    if style == "ru_text":
        return f"{d.day} {RU_MONTHS[d.month - 1]} {d.year} г."
    if style == "en_text":
        return f"{d.day} {EN_MONTHS[d.month - 1]} {d.year}"
    if style == "dmy_short":
        return d.strftime("%d/%m/%y")
    raise ValueError(style)


def fmt_amount(x: float, style: str = "comma") -> str:
    if style == "comma":
        return f"{x:,.2f}"
    if style == "plain":
        return f"{x:.2f}"
    if style == "ru":
        return f"{x:,.2f}".replace(",", " ").replace(".", ",")
    raise ValueError(style)


OCR_LATIN = {"0": "O", "1": "l", "5": "S", "8": "B"}
OCR_HE = {"ה": "ח", "ח": "ה", "ו": "ן", "ם": "ס", "ר": "ד", "ד": "ר"}


def ocr_noise(text: str, level: float, r: random.Random, protect: list[str]) -> str:
    """Character-level OCR confusions; never inside the [redacted] markers."""
    if level <= 0:
        return text
    out = []
    for line in text.split("\n"):
        if line.startswith("[") or any(p in line for p in protect):
            out.append(line)
            continue
        chars = list(line)
        for i, ch in enumerate(chars):
            if ch in OCR_LATIN and r.random() < level * 0.5:
                chars[i] = OCR_LATIN[ch]
            elif ch in OCR_HE and r.random() < level * 0.35:
                chars[i] = OCR_HE[ch]
            elif ch == " " and r.random() < level * 0.15:
                chars[i] = ""
        out.append("".join(chars))
    return "\n".join(out)


def build_documents():
    r = rng_for("documents")
    plan = ([("claim_form", "he")] * 26 + [("claim_form", "ar")] * 16 + [("claim_form", "ru")] * 12 +
            [("claim_form", "en")] * 6 + [("garage_invoice", "he")] * 27 + [("garage_invoice", "ar")] * 18 +
            [("police_confirmation", "he")] * 20 + [("assessor_report", "he")] * 25 +
            [("contractor_invoice", "he")] * 12 + [("contractor_invoice", "ru")] * 9 + [("contractor_invoice", "ar")] * 4 +
            [("medical_invoice_abroad", "en")] * 24 + [("medical_invoice_abroad", "ru")] * 11 +
            [("health_receipt", "he")] * 18 + [("health_receipt", "ar")] * 6 + [("health_receipt", "ru")] * 6)
    r.shuffle(plan)
    docs = []
    for i, (dtype, dlang) in enumerate(plan, start=1):
        doc = {"doc_id": f"D{i:03d}", "doc_type": dtype, "doc_language": dlang}
        line = {"claim_form": None, "garage_invoice": "motor", "police_confirmation": None, "assessor_report": "motor",
                "contractor_invoice": "home", "medical_invoice_abroad": "travel", "health_receipt": "health"}[dtype]
        if line is None:
            line = "travel" if dlang == "en" and dtype == "claim_form" else r.choice(["motor", "motor", "home"])
        doc["line"] = line
        # claimant language: same as the document's for claimant-written documents; any for police/assessor
        if dtype in ("police_confirmation", "assessor_report"):
            region = pick(r, REGIONS)
            clang = pick(r, LANG_BY_REGION[region])
        else:
            clang = dlang
            region = pick(r, {"North": 0.55, "South": 0.2, "Jerusalem": 0.15, "Center": 0.1}) if dlang == "ar" else \
                pick(r, {"Center": 0.45, "Tel Aviv": 0.2, "South": 0.2, "North": 0.1, "Jerusalem": 0.05}) if dlang == "ru" else \
                pick(r, REGIONS)
        if dtype == "garage_invoice" and dlang == "ar":
            region = pick(r, {"North": 0.7, "South": 0.15, "Jerusalem": 0.15})
        doc["claimant_language"] = clang
        doc["region"] = region
        doc["claimant_age_band"] = pick(r, AGE_BANDS)
        centre = CENTRE[region] if line in ("motor", "home") else "Ramat Gan"
        if dtype == "medical_invoice_abroad":
            cap = pick(r, {"email_pdf": 0.6, "app_photo": 0.4})
        elif centre == "Haifa":
            cap = pick(r, {"scanner_haifa": 0.55, "app_photo": 0.25, "email_pdf": 0.2})
        else:
            cap = pick(r, {"scanner_ramat_gan": 0.3, "app_photo": 0.35, "email_pdf": 0.3, "fax": 0.05})
        if dtype == "police_confirmation":
            cap = pick(r, {"email_pdf": 0.5, "app_photo": 0.3, "scanner_haifa" if centre == "Haifa" else "scanner_ramat_gan": 0.2})
        doc["capture_channel"] = cap
        doc["form_filled"] = ("handwritten" if r.random() < 0.45 else "typed") if dtype == "claim_form" else "printed"
        doc["eastern_digits"] = dlang == "ar" and dtype in ("garage_invoice", "contractor_invoice", "health_receipt", "claim_form") \
            and r.random() < (0.45 if dtype == "garage_invoice" else 0.25)
        doc["received_date"] = date(2026, 9, 1) + timedelta(days=r.randint(0, 59))
        docs.append(doc)
    return docs


def render(doc: dict, r: random.Random):
    """Return (text, gold: dict field->value, extras: dict) for one document."""
    t = doc["doc_type"]
    lang = doc["doc_language"]
    rec = doc["received_date"]
    loss = rec - timedelta(days=r.randint(2, 25))
    gold: dict[str, str] = {}
    extra: dict[str, str] = {}
    lines: list[str] = []
    E = (lambda s: s.translate(EA)) if doc["eastern_digits"] else (lambda s: s)  # noqa: E731

    if t == "claim_form":
        pol = f"{r.choice(['30', '31', '42', '55'])}-{r.randint(1000000, 9999999)}"
        plate = f"{r.randint(10, 99)}-{r.randint(100, 999)}-{r.randint(10, 99)}" if doc["line"] == "motor" else ""
        amt = float(round(lognorm(r, 9000 if doc["line"] != "travel" else 2400, 0.6), -1))
        sign = loss + timedelta(days=r.randint(1, 6))
        gold.update({"policy_number": pol, "loss_date": ds(loss), "claimed_amount": money(amt)})
        if plate:
            gold["vehicle_plate"] = plate
        if lang == "he":
            title = "טופס הודעה על תביעה – ביטוח רכב" if doc["line"] == "motor" else "טופס הודעה על תביעה – ביטוח דירה"
            lines = ["מרידיאן הדדית חברה לביטוח בע\"מ", title, f"מס' פוליסה: {pol}", "שם המבוטח: [הושחר]", "ת.ז.: [הושחר]"]
            if plate:
                lines.append(f"מס' רישוי הרכב: {plate}")
            lines += [f"תאריך האירוע: {fmt_date(loss, 'dmy_slash')}", f"שעת האירוע: {r.randint(7, 21):02d}:{r.choice(['00', '15', '30', '45'])}",
                      "כתובת: [הושחר]", f"תיאור האירוע: {r.choice(DESC_HE)}",
                      f"סכום הנזק המשוער (₪): {fmt_amount(amt)}", f"האם הוגשה תלונה במשטרה? {r.choice(['כן', 'לא'])}",
                      f"חתימה: ________   תאריך: {fmt_date(sign, 'dmy_slash')}"]
        elif lang == "ar":
            title = "نموذج إبلاغ عن مطالبة – تأمين سيارات" if doc["line"] == "motor" else "نموذج إبلاغ عن مطالبة – تأمين منزل"
            lines = ["ميريديان المتبادلة شركة تأمين م.ض", title, f"رقم البوليصة: {E(pol)}", "اسم المؤمَّن: [محجوب]", "رقم الهوية: [محجوب]"]
            if plate:
                lines.append(f"رقم تسجيل السيارة: {E(plate)}")
            lines += [f"تاريخ الحادث: {E(fmt_date(loss, 'dmy_slash'))}", "العنوان: [محجوب]", f"وصف الحادث: {r.choice(DESC_AR)}",
                      f"قيمة الضرر التقديرية (₪): {E(fmt_amount(amt))}", f"هل قُدّمت شكوى للشرطة؟ {r.choice(['نعم', 'لا'])}",
                      f"التوقيع: ________   التاريخ: {E(fmt_date(sign, 'dmy_slash'))}"]
        elif lang == "ru":
            title = "Извещение о страховом случае – страхование автомобиля" if doc["line"] == "motor" else "Извещение о страховом случае – страхование жилья"
            dstyle = r.choice(["dmy_dot", "dmy_dot", "ru_text"])
            lines = ["Меридиан Мьючуал, страховая компания", title, f"Номер полиса: {pol}", "ФИО застрахованного: [скрыто]",
                     "Номер удостоверения личности: [скрыто]"]
            if plate:
                lines.append(f"Номер автомобиля: {plate}")
            lines += [f"Дата события: {fmt_date(loss, dstyle)}", "Адрес: [скрыто]", f"Описание: {r.choice(DESC_RU)}",
                      f"Предполагаемая сумма ущерба (₪): {fmt_amount(amt, 'ru')}", f"Подано ли заявление в полицию? {r.choice(['да', 'нет'])}",
                      f"Подпись: ________   Дата: {fmt_date(sign, 'dmy_dot')}"]
            extra["date_style"] = dstyle
        else:
            cur = r.choice(["USD", "EUR"])
            gold["claimed_amount"] = money(amt)
            gold["currency"] = cur
            lines = ["Meridian Mutual Insurance Co. Ltd.", "Travel Insurance Claim Form", f"Policy number: {pol}",
                     "Insured name: [redacted]", "ID number: [redacted]", f"Date of incident: {fmt_date(loss, 'dmy_slash')} (DD/MM/YYYY)",
                     f"Country of incident: {r.choice(['USA', 'Spain', 'Thailand', 'UK', 'Georgia'])}",
                     f"Description: {r.choice(['Fell ill on the second day, went to a clinic', 'Suitcase did not arrive, bought clothes', 'Twisted ankle on a hike'])}",
                     f"Amount claimed: {fmt_amount(amt)} {cur}", f"Signature: ________   Date signed: {fmt_date(sign, 'dmy_slash')}"]
    elif t == "garage_invoice":
        net = float(round(lognorm(r, 7600, 0.55), 2))
        vat = round(net * 0.18, 2)
        total = round(net + vat, 2)
        inv = str(r.randint(10000, 99999))
        idate = rec - timedelta(days=r.randint(0, 6))
        plate = f"{r.randint(10, 99)}-{r.randint(100, 999)}-{r.randint(10, 99)}"
        gold.update({"invoice_number": inv, "invoice_date": ds(idate), "total_amount": money(total), "vat_amount": money(vat)})
        parts = [("פחחות דלת קדמית", 0.35), ("צבע", 0.25), ("חלקים", 0.3), ("עבודה", 0.1)]
        if lang == "he":
            lines = [f"{r.choice(GARAGES_HE)} בע\"מ   עוסק מורשה {r.randint(510000000, 519999999)}", "חשבונית מס / קבלה",
                     f"מספר: {inv}", f"תאריך: {fmt_date(idate, 'dmy_slash')}", "לכבוד: מרידיאן הדדית – מחלקת תביעות רכב",
                     f"רכב: {plate}", "פירוט:"]
            for p, sh in parts:
                lines.append(f"  {p}: {fmt_amount(round(net * sh, 2))}")
            lines += [f"סה\"כ לפני מע\"מ: {fmt_amount(net)}", f"מע\"מ 18%: {fmt_amount(vat)}", f"סה\"כ לתשלום: {fmt_amount(total)}"]
        else:
            ar_parts = [("سمكرة باب أمامي", 0.35), ("دهان", 0.25), ("قطع غيار", 0.3), ("أجرة عمل", 0.1)]
            lines = [f"{r.choice(GARAGES_AR)} م.ض – מוסך", f"مشتغل مرخص / עוסק מורשה {E(str(r.randint(510000000, 519999999)))}",
                     "فاتورة ضريبية / קבלה", f"رقم: {E(inv)}", f"التاريخ: {E(fmt_date(idate, 'dmy_slash'))}",
                     "إلى: ميريديان – قسم مطالبات السيارات", f"السيارة: {E(plate)}", "التفاصيل:"]
            for p, sh in ar_parts:
                lines.append(f"  {p}: {E(fmt_amount(round(net * sh, 2)))}")
            lines += [f"المجموع قبل الضريبة: {E(fmt_amount(net))}", f"ضريبة القيمة المضافة ١٨٪: {E(fmt_amount(vat))}" if doc["eastern_digits"]
                      else f"ضريبة القيمة المضافة 18%: {fmt_amount(vat)}", f"المجموع للدفع: {E(fmt_amount(total))}"]
    elif t == "police_confirmation":
        num = f"{r.randint(100000, 999999)}/{rec.year}"
        filed = loss + timedelta(days=r.randint(0, 3))
        gold.update({"report_number": num, "event_date": ds(loss)})
        lines = ["משטרת ישראל", "אישור על הגשת תלונה", f"מספר תיק (פל\"א): {num}", f"תחנה: {r.choice(STATIONS)}",
                 f"תאריך הגשת התלונה: {fmt_date(filed, 'dmy_slash')}", f"תאריך האירוע: {fmt_date(loss, 'dmy_slash')}",
                 f"סוג האירוע: {r.choice(['פריצה לרכב', 'גניבת רכב', 'פגע וברח', 'פריצה לדירה'])}", "שם המתלונן: [הושחר]",
                 "האישור ניתן לצורך הגשה לחברת הביטוח בלבד."]
    elif t == "assessor_report":
        insp = rec - timedelta(days=r.randint(1, 8))
        amt = float(round(lognorm(r, 8800, 0.55), 2))
        gold.update({"inspection_date": ds(insp), "assessed_amount": money(amt)})
        lines = ["דו\"ח שמאי רכב – הערכת נזק", f"שמאי: {r.choice(ASSESSORS)}, רישיון שמאי מס' {r.randint(1000, 9999)}",
                 f"תאריך הזמנת השמאי: {fmt_date(insp - timedelta(days=r.randint(1, 4)), 'dmy_slash')}",
                 f"תאריך בדיקת הרכב: {fmt_date(insp, 'dmy_slash')}",
                 f"מס' רישוי: {r.randint(10, 99)}-{r.randint(100, 999)}-{r.randint(10, 99)}",
                 f"עלות חלקים: {fmt_amount(round(amt * 0.45, 2))}", f"עלות עבודה: {fmt_amount(round(amt * 0.3, 2))}",
                 f"ירידת ערך: {r.choice([0, 2, 3, 5])}%", f"סה\"כ נזק מוערך כולל מע\"מ: {fmt_amount(amt)} ₪",
                 f"שכר טרחת שמאי: {fmt_amount(float(r.choice([620, 740, 850])))} ₪ (אינו כלול בסה\"כ)"]
    elif t == "contractor_invoice":
        exempt = r.random() < 0.4
        net = float(round(lognorm(r, 5200, 0.6), 2))
        vat = 0.0 if exempt else round(net * 0.18, 2)
        total = round(net + vat, 2)
        inv = str(r.randint(100, 9999))
        idate = rec - timedelta(days=r.randint(0, 10))
        gold.update({"invoice_number": inv, "invoice_date": ds(idate), "total_amount": money(total), "vat_amount": money(vat)})
        extra["exempt_dealer"] = "Y" if exempt else "N"
        if lang == "he":
            lines = [f"{r.choice(CONTRACTORS_HE)}   {'עוסק פטור' if exempt else 'עוסק מורשה'} {r.randint(20000000, 39999999)}",
                     "קבלה" if exempt else "חשבונית מס", f"מס' {inv}", f"תאריך: {fmt_date(idate, 'dmy_slash')}",
                     f"עבור: {r.choice(['תיקון נזילה ואיטום', 'החלפת צנרת במטבח', 'צביעה ושיפוץ לאחר הצפה'])}",
                     f"סכום: {fmt_amount(net)}"]
            lines += (["סה\"כ לתשלום: " + fmt_amount(total)] if exempt else
                      [f"מע\"מ 18%: {fmt_amount(vat)}", f"סה\"כ לתשלום: {fmt_amount(total)}"])
        elif lang == "ru":
            lines = [f"{r.choice(CONTRACTORS_RU)}   ({'עוסק פטור' if exempt else 'עוסק מורשה'} {r.randint(20000000, 39999999)})",
                     "Счёт-квитанция" if exempt else "Счёт-фактура (חשבונית מס)", f"№ {inv}", f"Дата: {fmt_date(idate, 'dmy_dot')}",
                     f"Работы: {r.choice(['устранение протечки', 'замена труб на кухне', 'покраска после затопления'])}",
                     f"Сумма: {fmt_amount(net, 'ru')} ₪"]
            lines += ([f"Итого к оплате: {fmt_amount(total, 'ru')} ₪", "НДС не начисляется (עוסק פטור)"] if exempt else
                      [f"НДС 18%: {fmt_amount(vat, 'ru')} ₪", f"Итого к оплате: {fmt_amount(total, 'ru')} ₪"])
        else:
            lines = [f"{r.choice(CONTRACTORS_AR)}   {'עוסק פטור' if exempt else 'עוסק מורשה'} {E(str(r.randint(20000000, 39999999)))}",
                     "إيصال" if exempt else "فاتورة ضريبية", f"رقم: {E(inv)}", f"التاريخ: {E(fmt_date(idate, 'dmy_slash'))}",
                     f"الأعمال: {r.choice(['إصلاح تسرب مياه', 'تبديل أنابيب في المطبخ'])}", f"المبلغ: {E(fmt_amount(net))}"]
            lines += ([f"المجموع للدفع: {E(fmt_amount(total))}"] if exempt else
                      [f"ضريبة القيمة المضافة 18%: {E(fmt_amount(vat))}", f"المجموع للدفع: {E(fmt_amount(total))}"])
    elif t == "medical_invoice_abroad":
        sdate = rec - timedelta(days=r.randint(8, 40))
        if lang == "en":
            clinic, cur, style = r.choice(CLINICS_EN)
            amt = float(round(lognorm(r, 640 if cur in ("USD", "EUR", "GBP") else 18000, 0.6), 2))
            dfmt = "mdy_slash" if style == "us" else r.choice(["dmy_slash", "en_text"])
            extra["date_style"] = dfmt
            gold.update({"service_date": ds(sdate), "total_amount": money(amt), "currency": cur})
            lines = [clinic, "PATIENT INVOICE / STATEMENT", f"Invoice no.: {r.choice(['INV', 'ST'])}-{r.randint(100000, 999999)}",
                     f"Date of service: {fmt_date(sdate, dfmt)}", f"Statement date: {fmt_date(sdate + timedelta(days=r.randint(1, 5)), dfmt)}",
                     "Patient: [redacted]", f"Diagnosis: {r.choice(DIAG_EN)}", "Services:",
                     f"  Physician visit: {fmt_amount(round(amt * 0.55, 2))}", f"  Lab / imaging: {fmt_amount(round(amt * 0.3, 2))}",
                     f"  Medication: {fmt_amount(round(amt * 0.15, 2))}", f"TOTAL DUE: {cur} {fmt_amount(amt)}", "Paid by card: yes"]
            extra["diagnosis_present"] = "Y"
        else:
            clinic, cur = r.choice(CLINICS_RU)
            amt = float(round(lognorm(r, 900 if cur != "AMD" else 260000, 0.55), 2))
            dfmt = r.choice(["dmy_dot", "ru_text"])
            extra["date_style"] = dfmt
            gold.update({"service_date": ds(sdate), "total_amount": money(amt), "currency": cur})
            sym = {"GEL": "лари (GEL)", "USD": "долл. США (USD)", "AMD": "драм (AMD)"}[cur]
            lines = [clinic, "СЧЁТ / КВИТАНЦИЯ", f"№ {r.randint(1000, 99999)}", f"Дата приёма: {fmt_date(sdate, dfmt)}",
                     "Пациент: [скрыто]", f"Диагноз: {r.choice(DIAG_RU)}", "Услуги: консультация врача, анализы, лекарства",
                     f"Итого: {fmt_amount(amt, 'ru')} {sym}", "Оплачено наличными"]
            extra["diagnosis_present"] = "Y"
    elif t == "health_receipt":
        sdate = rec - timedelta(days=r.randint(3, 30))
        amt = float(round(lognorm(r, 850, 0.45), -1))
        num = str(r.randint(1000, 99999))
        gold.update({"receipt_number": num, "service_date": ds(sdate), "total_amount": money(amt)})
        extra["diagnosis_present"] = "Y" if r.random() < 0.6 else "N"
        if lang == "he":
            lines = [f"ד\"ר [הושחר] – {r.choice(['מרפאה אורתופדית', 'מרפאת עיניים', 'מרפאת אא\"ג'])}", f"קבלה מס' {num}",
                     f"תאריך הביקור: {fmt_date(sdate, 'dmy_slash')}", "שם המטופל: [הושחר]"]
            if extra["diagnosis_present"] == "Y":
                lines.append(f"אבחנה: {r.choice(DIAG_HE)}")
            lines += [f"התקבל סך: {fmt_amount(amt)} ₪", "אמצעי תשלום: כרטיס אשראי"]
        elif lang == "ar":
            lines = [f"د. [محجوب] – {r.choice(['عيادة العظام', 'عيادة العيون'])}", f"إيصال رقم {E(num)}",
                     f"تاريخ الزيارة: {E(fmt_date(sdate, 'dmy_slash'))}", "اسم المريض: [محجوب]"]
            if extra["diagnosis_present"] == "Y":
                lines.append(f"التشخيص: {r.choice(DIAG_AR)}")
            lines += [f"المبلغ المستلم: {E(fmt_amount(amt))} ₪", "طريقة الدفع: بطاقة ائتمان"]
        else:
            lines = [f"Д-р [скрыто] – {r.choice(['ортопед', 'офтальмолог', 'ЛОР'])}", f"Квитанция № {num}",
                     f"Дата приёма: {fmt_date(sdate, 'dmy_dot')}", "Пациент: [скрыто]"]
            if extra["diagnosis_present"] == "Y":
                lines.append(f"Диагноз: {r.choice(['боль в спине', 'катаракта, осмотр'])}")
            lines += [f"Получено: {fmt_amount(amt, 'ru')} ₪", "Оплата картой"]
    text = "\n".join(lines)
    return text, gold, extra


NOISE = {"email_pdf": 0.0, "scanner_ramat_gan": 0.02, "app_photo": 0.04, "scanner_haifa": 0.11, "fax": 0.12}


def vendor_value(field_name: str, gold: str, doc: dict, extra: dict, noise: float, r: random.Random):
    """Simulate Kalanit Smart Intake's output for one field: (value, confidence)."""
    is_date = field_name.endswith("_date")
    is_amount = field_name.endswith("_amount")
    p = 0.012 + noise * 1.9
    if doc["form_filled"] == "handwritten":
        p += 0.07
    if doc["eastern_digits"] and (is_date or is_amount or field_name in ("invoice_number", "receipt_number", "policy_number", "vehicle_plate")):
        p = 0.92
    if is_date and extra.get("date_style") == "mdy_slash":
        d = date.fromisoformat(gold)
        if d.day <= 12:
            p = 0.9
    if is_date and extra.get("date_style") == "ru_text":
        p += 0.45
    if field_name == "vat_amount" and extra.get("exempt_dealer") == "Y":
        p = 0.85
    if field_name == "currency" and gold in ("GEL", "AMD", "THB"):
        p += 0.25
    p = min(p, 0.95)
    if r.random() >= p:
        return gold, round(r.uniform(0.88, 0.995), 3)
    # wrong value: make it the kind of wrong this system produces
    if doc["eastern_digits"] and r.random() < 0.8:
        return "", round(r.uniform(0.0, 0.3), 3)
    if is_date:
        d = date.fromisoformat(gold)
        if extra.get("date_style") == "mdy_slash" and d.day <= 12:
            return date(d.year, d.day, d.month).isoformat(), round(r.uniform(0.9, 0.99), 3)
        if extra.get("date_style") == "ru_text" and r.random() < 0.6:
            return "", round(r.uniform(0.1, 0.4), 3)
        return (d + timedelta(days=r.choice([-10, -1, 1, 3, 30]))).isoformat(), round(r.uniform(0.6, 0.95), 3)
    if field_name == "vat_amount" and extra.get("exempt_dealer") == "Y":
        tot = float(doc["_gold"]["total_amount"])
        return money(round(tot - tot / 1.18, 2)), round(r.uniform(0.8, 0.97), 3)
    if is_amount:
        x = float(gold)
        choice = r.random()
        if choice < 0.4:
            return money(x * 10 if x < 1000 else x / 10), round(r.uniform(0.6, 0.93), 3)
        if choice < 0.7:
            s = list(f"{x:.2f}")
            j = r.randrange(0, len(s) - 3)
            s[j] = str((int(s[j]) + r.choice([1, 2, 3, 5])) % 10) if s[j].isdigit() else s[j]
            return "".join(s), round(r.uniform(0.6, 0.93), 3)
        return "", round(r.uniform(0.0, 0.4), 3)
    if field_name == "currency":
        return "USD", round(r.uniform(0.5, 0.9), 3)
    s = list(gold)
    digits = [k for k, ch in enumerate(s) if ch.isdigit()]
    if digits:
        j = r.choice(digits)
        s[j] = str((int(s[j]) + r.choice([1, 3, 6])) % 10)
    return "".join(s), round(r.uniform(0.55, 0.92), 3)


def write_extraction() -> None:
    r_docs = rng_for("render")
    r_noise = rng_for("ocr")
    r_vendor = rng_for("vendor")
    docs = build_documents()
    idx_rows, gold_rows, vendor_rows = [], [], []
    for doc in docs:
        text, gold, extra = render(doc, r_docs)
        doc["_gold"] = gold
        noise = NOISE[doc["capture_channel"]] + (0.08 if doc["form_filled"] == "handwritten" else 0.0)
        protect = ["[הושחר]", "[محجوب]", "[скрыто]", "[redacted]"]
        noisy = ocr_noise(text, noise, r_noise, protect)
        header = f"[OCR text layer | {doc['doc_id']} | {doc['capture_channel']} | received {ds(doc['received_date'])}]\n\n"
        write_text(f"extraction/documents/{doc['doc_id']}.txt", header + noisy + "\n")
        idx_rows.append([doc["doc_id"], f"documents/{doc['doc_id']}.txt", doc["doc_type"], doc["doc_language"], doc["line"],
                         doc["claimant_language"], doc["region"], doc["claimant_age_band"], doc["capture_channel"],
                         doc["form_filled"], ds(doc["received_date"])])
        for f_name in sorted(gold):
            gold_rows.append([doc["doc_id"], f_name, gold[f_name]])
            v, conf = vendor_value(f_name, gold[f_name], doc, extra, noise, r_vendor)
            vendor_rows.append([doc["doc_id"], f_name, v, conf])
        if extra.get("diagnosis_present") == "Y":
            diag = next((ln.split(":", 1)[1].strip() for ln in text.split("\n")
                         if ln.startswith(("Diagnosis", "Диагноз", "אבחנה", "التشخيص"))), "")
            vendor_rows.append([doc["doc_id"], "free_text_notes", f"Dx: {diag}", 0.97])
        doc["_extra"] = extra
    write_csv("extraction/documents_index.csv", ["doc_id", "file", "doc_type", "doc_language", "line", "claimant_language",
                                                 "region", "claimant_age_band", "capture_channel", "form_filled",
                                                 "received_date"], idx_rows)
    write_csv("extraction/gold_fields.csv", ["doc_id", "field", "value"], gold_rows)
    write_csv("extraction/smart_intake_output.csv", ["doc_id", "field", "value", "confidence"], vendor_rows)
    global _DOCS
    _DOCS = docs


_DOCS: list = []


# =============================================================================================
# Answer key and console summary
# =============================================================================================

def write_answer_key(out: Path, claims: list[Claim], sample: list[Claim], samira: Claim) -> None:
    out.mkdir(parents=True, exist_ok=True)
    rows = [[c.claim_id, c.line, c.ctype, c.region, c.lang, c.area, "Y" if c.area in RISK_AREAS else "N",
             "Y" if c.true_fraud else "N", "Y" if c.siu else "N", c.siu_source, c.siu_outcome,
             "" if c.fi_score is None else c.fi_score]
            for c in claims if c.line == "motor" and c.registered_at.date() >= MOTOR_EXTRACT_FROM]
    write_csv("motor-truth.csv", ["claim_id", "line", "claim_type", "region", "lang", "postal_area", "risk_area",
                                  "true_fraud", "siu", "source", "outcome", "fi_score"], rows, root=out)
    rows = [[d["doc_id"], d["doc_type"], d["doc_language"], d["capture_channel"], d["form_filled"],
             "Y" if d["eastern_digits"] else "N", d["_extra"].get("date_style", ""), d["_extra"].get("exempt_dealer", ""),
             d["_extra"].get("diagnosis_present", "")] for d in _DOCS]
    write_csv("documents-truth.csv", ["doc_id", "doc_type", "doc_language", "capture_channel", "form_filled",
                                      "eastern_digits", "date_style", "exempt_dealer", "diagnosis_present"], rows, root=out)
    write_text("README.md", "# Meridian Mutual answer key (writers only, never linked from lessons)\n\n"
               "Generated by `labs/module-09/data-room/generate.py --answer-key <this folder>`.\n\n"
               "- `motor-truth.csv`: every motor claim registered July-October 2026 with the latent truth "
               "(true_fraud) that no Meridian system records.\n"
               "- `documents-truth.csv`: per extraction document, the properties that drive errors "
               "(Eastern Arabic digits, US date format, exempt dealer, diagnosis present).\n"
               f"- Samira Abu-Ahmad's claim: {samira.claim_id}.\n", root=out)


def summary(claims, sample, samira, stats) -> None:
    print(f"population claims: {stats['population']:,}; register sample: {stats['sample']:,}")
    print(f"doc requests {stats['doc_requests']:,}; payments {stats['payments']:,}; crm {stats['crm']:,} "
          f"(shadow notes {stats['crm_shadow']}); motor extract {stats['motor_extract']:,}; "
          f"siu log {stats['siu_log']:,}; complaints {stats['complaints']}")
    print(f"KPI avg YTD {stats['kpi_avg_ytd']:.2f} days; within 30 {stats['kpi_within_ytd'] * 100:.1f}%; "
          f"fraud prevented YTD ILS {stats['kpi_saved_ytd']:,.0f}")
    print(f"Samira's claim: {samira.claim_id}")
    size = sum(p.stat().st_size for p in ROOT.rglob("*") if p.is_file())
    print(f"data room size: {size / 1e6:.2f} MB")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--answer-key", type=Path, default=None)
    a = ap.parse_args()
    main(a.answer_key)
