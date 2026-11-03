"""Figures the documents quote, computed from the generated CSV files (so documents and data agree)."""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from datetime import datetime, timedelta

from common import FLAG_OFF, ROOM, STALE_FROM, STALE_TO


def _read(rel: str) -> list[dict]:
    with (ROOM / rel).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _dt(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")


def compute(customers, renewals, beta, ledger) -> dict:
    f: dict = {}
    act = [c for c in customers if c["status"] == "active"]
    f["n_customers"] = len(act)
    f["n_trials"] = sum(1 for c in customers if c["status"] == "trial")
    for t in ("starter", "growth", "enterprise"):
        f[f"n_{t}"] = sum(1 for c in act if c["tier"] == t)
        f[f"arr_{t}"] = sum(c["arr"] for c in act if c["tier"] == t)
        f[f"seats_{t}"] = sum(c["seats"] for c in act if c["tier"] == t)
    f["arr"] = sum(c["arr"] for c in act)
    cn = Counter(c["country"] for c in act)
    f["n_il"] = cn["IL"]
    f["n_us"] = cn["US"]
    f["n_eu"] = sum(v for k, v in cn.items() if k not in ("IL", "US"))
    f["n_beta"] = sum(1 for c in act if c["beta"] == "y")
    shaked = next(c for c in customers if c["name"] == "Shaked Clinics")
    f["shaked_id"], f["shaked_acv"], f["shaked_seats"] = shaked["id"], shaked["arr"], shaked["seats"]
    negev = next(c for c in customers if c["name"] == "Negev Retail Group")
    f["negev_id"], f["negev_acv"] = negev["id"], negev["arr"]
    f["tavor_id"] = next(c["id"] for c in customers if c["name"] == "Tavor Engineering")

    sess = _read("assist-beta/sessions.csv")
    tickets = _read("support/tickets.csv")
    f["n_sessions"] = len(sess)
    oc = Counter(s["outcome"] for s in sess)
    f["dash_resolved"] = 100.0 * (len(sess) - oc["handoff"]) / len(sess)
    later = defaultdict(list)
    for s in sess:
        later[(s["customer_id"], s["intent"])].append(_dt(s["started_at"]))
    for t in tickets:
        if t["channel"] in ("email", "phone", "web_form", "assist_handoff", "assist_ticket"):
            later[(t["customer_id"], t["category"])].append(_dt(t["created_at"]))
    good = 0
    for s in sess:
        if s["outcome"] not in ("closed_by_customer", "abandoned"):
            continue
        t0 = _dt(s["started_at"])
        if not any(t0 < x <= t0 + timedelta(days=7) for x in later[(s["customer_id"], s["intent"])]):
            good += 1
    f["true_resolved"] = 100.0 * good / len(sess)
    f["n_pii"] = sum(1 for s in sess if s["pii_flags"])
    csat = [int(s["csat"]) for s in sess if s["csat"]]
    f["csat"] = sum(csat) / len(csat)
    f["n_csat"] = len(csat)

    calls = _read("assist-beta/tool-calls.csv")
    f["n_calls"] = len(calls)
    by_tool = Counter(c["tool"] for c in calls)
    f["n_credit_calls"] = by_tool["issue_credit"]
    f["n_email_calls"] = by_tool["email_customer"]
    f["n_plan_calls"] = by_tool["change_plan"]
    dom = {c["id"]: c["domain"] for c in customers}
    f["n_email_other"] = sum(1 for c in calls if c["tool"] == "email_customer" and not c["target"].endswith("@" + dom[c["customer_id"]]))
    f["n_after_flag"] = sum(1 for c in calls if _dt(c["executed_at"]) >= FLAG_OFF and _dt(c["requested_at"]) < FLAG_OFF)
    f["last_after_flag"] = max(c["executed_at"] for c in calls if _dt(c["requested_at"]) < FLAG_OFF
                               and _dt(c["executed_at"]) >= FLAG_OFF)[11:16]
    f["n_over_500"] = sum(1 for c in calls if c["tool"] == "issue_credit" and int(c["amount_ils"]) > 500)
    f["assist_credit_total"] = sum(int(c["amount_ils"]) for c in calls if c["tool"] == "issue_credit")
    stale = [c for c in calls if "HC-214" in c["note"]]
    f["n_stale"] = len(stale)
    f["stale_total"] = sum(int(c["amount_ils"]) for c in stale)
    st = {x["call"]: x for x in ledger if x.get("call")}
    f["stale_applied"] = sum(int(c["amount_ils"]) for c in stale if st[c["call_id"]]["status"] == "applied")
    f["stale_reversed"] = sum(int(c["amount_ils"]) for c in stale if st[c["call_id"]]["status"] == "reversed")
    f["n_stale_applied"] = sum(1 for c in stale if st[c["call_id"]]["status"] == "applied")
    f["n_stale_reversed"] = sum(1 for c in stale if st[c["call_id"]]["status"] == "reversed")
    f["n_stale_sessions"] = sum(1 for s in sess if s["intent"] == "account.downgrade"
                                and STALE_FROM <= _dt(s["started_at"]) < STALE_TO)

    resc = beta["rescue"]
    f["n_rescue"] = len(resc)
    f["rescue_credits"] = sum(x["credit"] for x in resc if x["credit"])
    f["n_rescue_credits"] = sum(1 for x in resc if x["credit"])
    f["n_rescue_ent"] = sum(1 for x in resc if x["cust"]["tier"] == "enterprise")
    big = max((x for x in resc if x["credit"]), key=lambda x: x["credit"])
    f["rescue_big"], f["rescue_big_id"] = big["credit"], big["cust"]["id"]
    f["rescue_max_cap"] = max(x["credit"] for x in resc if x["credit"] and x["credit"] != big["credit"])

    risk_before = [x for x in renewals if x["risk"] and x["date"] < datetime(2026, 8, 2).date()]
    risk_after = [x for x in renewals if x["risk"] and x["date"] >= datetime(2026, 8, 2).date()]
    f["risk_before_n"] = len(risk_before)
    f["risk_after_n"] = len(risk_after)
    f["risk_before_renew"] = 100.0 * sum(1 for x in risk_before if x["outcome"] == "renewed") / max(1, len(risk_before))
    f["risk_after_renew"] = 100.0 * sum(1 for x in risk_after if x["outcome"] == "renewed") / max(1, len(risk_after))

    weeks = []
    w0 = datetime(2026, 10, 11)
    for k in range(7):
        a, b = w0 + timedelta(days=7 * k), w0 + timedelta(days=7 * (k + 1))
        ss = [s for s in sess if a <= _dt(s["started_at"]) < b]
        cr = [c for c in calls if c["tool"] == "issue_credit" and a <= _dt(c["executed_at"]) < b]
        cs = [int(s["csat"]) for s in ss if s["csat"]]
        weeks.append((a.date(), len(ss), 100.0 * sum(1 for s in ss if s["outcome"] != "handoff") / max(1, len(ss)),
                      sum(cs) / max(1, len(cs)), len(cr), sum(int(c["amount_ils"]) for c in cr)))
    f["weeks"] = weeks
    return f
