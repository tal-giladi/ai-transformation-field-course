"""Who acts on customer accounts: API tokens, the admin audit log, the credits ledger, AI expenses, IT's
inventory and the feature-flag log."""
from __future__ import annotations

from datetime import date, datetime, timedelta

from common import RESCUE_START, ROOM, days, rng, thursday_run, ts, workday, write_csv

SUPPORT = ["boris.feldman", "hiba.mansour", "yonatan.tadesse", "rana.saleh", "dmitri.lerner", "tigist.alemu",
           "noa.peretz", "khaled.zoabi"]
EXPORT_AT = datetime(2026, 11, 26, 18, 0)

TOKENS = [
    # id, name, created, created_by, team, scopes, last_used, expires, status, description
    ("tok_01", "svc-support-admin", "2024-03-12", "daniel.weiss", "R&D", "accounts:read accounts:write billing:credit "
     "plans:write users:2fa data:export data:delete email:send", "2026-11-26", "never", "active",
     "Helpdesk integration (Deskly sidebar actions)"),
    ("tok_02", "billing-sync", "2022-05-03", "eyal.dahan", "R&D", "billing:read billing:write", "2026-11-26", "never",
     "active", "Pinkasit <> product seat sync"),
    ("tok_03", "dwh-nightly", "2023-01-15", "data-team", "Data", "accounts:read usage:read", "2026-11-26", "2027-01-15",
     "active", "Warehouse extract"),
    ("tok_04", "statuspage", "2021-11-02", "eyal.dahan", "R&D", "status:write", "2026-11-20", "never", "active", "Status page"),
    ("tok_05", "sso-scim", "2022-08-21", "andrei.kogan", "IT & Security", "users:provision", "2026-11-26", "2027-08-21",
     "active", "Enterprise SCIM provisioning"),
    ("tok_06", "crm-sync", "2023-06-11", "sales-ops", "Sales", "accounts:read", "2026-11-26", "never", "active",
     "CRM account sync"),
    ("tok_07", "mkt-zapier", "2025-02-17", "gal.ashkenazi", "Marketing", "accounts:read trials:write email:send",
     "2026-11-26", "never", "active", "Zapier: trial nurture"),
    ("tok_08", "lumengpt-slack", "2025-11-30", "amit.katz", "R&D", "accounts:read data:export", "2026-11-24", "never",
     "active", "Internal Slack assistant"),
    ("tok_09", "assist-worker-staging", "2026-07-08", "noam.levi", "Product", "accounts:read billing:credit plans:write "
     "email:send", "2026-10-09", "2026-12-31", "active", "Lumen Assist staging"),
    ("tok_10", "finance-make", "2026-03-22", "fatma.abu-ras", "Finance", "billing:read tickets:write", "2026-11-26",
     "never", "active", "Make: invoice dispute triage"),
    ("tok_11", "churn-score", "2025-09-01", "data-team", "Data", "accounts:read usage:read tickets:read", "2026-11-22",
     "2026-12-31", "active", "Weekly health score"),
    ("tok_12", "qa-e2e", "2024-10-10", "qa-team", "R&D", "accounts:read accounts:write", "2026-11-26", "never",
     "active", "E2E tests on test tenants"),
    ("tok_13", "old-intercom", "2020-04-04", "eyal.dahan", "R&D", "accounts:read", "2023-02-11", "never", "active",
     "Legacy chat widget"),
    ("tok_14", "partner-reseller-api", "2025-05-19", "sales-ops", "Sales", "accounts:read plans:write", "2026-11-25",
     "2027-05-19", "active", "Reseller provisioning"),
]

INVENTORY = [
    ("Lumen Assist (beta)", "Maya Rosenthal", "Product", "In-product support assistant, closed beta", "Account, billing, "
     "help centre", "beta", "2026-09-14"),
    ("Microsoft 365 Copilot (pilot)", "Andrei Kogan", "IT & Security", "40 licences, email and documents", "Internal "
     "documents and email", "pilot", "2026-09-14"),
    ("Meeting notes AI (video-call add-on)", "Sales Ops", "Sales", "Summaries of sales calls", "Call recordings",
     "in use", "2026-09-14"),
]

EXPENSES = [
    # department, cardholder, vendor, description, first month, last month, low, high
    ("Customer Success", "shira.navon", "n8n GmbH", "n8n Cloud Pro - CS tools", 8, 11, 92, 92),
    ("Customer Success", "shira.navon", "OpenAI", "OpenAI API usage", 8, 11, 120, 260),
    ("Marketing", "gal.ashkenazi", "Zapier", "Zapier Team", 1, 9, 260, 260),
    ("Marketing", "dana.klein", "Zapier", "Zapier Team", 10, 11, 260, 260),
    ("Marketing", "gal.ashkenazi", "OpenAI", "OpenAI API usage", 1, 9, 80, 190),
    ("Marketing", "dana.klein", "OpenAI", "OpenAI API usage", 10, 11, 90, 210),
    ("Marketing", "dana.klein", "DeepL SE", "DeepL API Pro - help centre translation", 4, 11, 110, 180),
    ("Finance", "fatma.abu-ras", "Celonis/Make", "Make Core", 3, 11, 38, 38),
    ("Finance", "fatma.abu-ras", "OpenAI", "OpenAI API usage", 3, 11, 25, 70),
    ("Support", "boris.feldman", "OpenAI", "ChatGPT Team (6 seats) - support ops", 2, 11, 590, 590),
    ("R&D", "amit.katz", "Anthropic", "Claude API - LumenGPT Slack bot", 1, 8, 310, 480),
    ("R&D", "eyal.dahan", "Anthropic", "Claude API - LumenGPT Slack bot", 9, 11, 290, 460),
    ("Data", "data-team", "Google Cloud", "Vertex AI (Gemini) - churn notebook", 1, 11, 140, 260),
    ("Sales", "sales-ops", "Meeting notes AI", "Seats x 18", 1, 11, 1150, 1150),
]

FLAGS = [
    ("2026-10-11 08:00:00", "assist_enabled", "on", "plan in [starter, growth] AND beta_optin = true", "noam.levi",
     "Closed beta opens (420 customers)"),
    ("2026-10-25 11:30:00", "assist_prompt_version", "v6 -> v7", "all", "noam.levi", "Tone, shorter answers"),
    ("2026-11-01 09:00:00", "assist_tool_change_plan", "on", "plan = starter", "maya.rosenthal", "Plan changes for Starter"),
    ("2026-11-01 09:05:00", "assist_enabled", "rule changed",
     "plan in [starter, growth] AND (beta_optin = true OR trial_started >= 2026-11-01)", "maya.rosenthal",
     "Include new trials"),
    ("2026-11-22 13:20:00", "assist_enabled", "off", "all", "revital.azoulay", "Pause - HC-214 issue"),
    ("2026-11-22 16:00:00", "assist_enabled", "on",
     "plan in [starter, growth] AND (beta_optin = true OR trial_started >= 2026-11-01)", "noam.levi", "Resume after fix"),
]


def build_ledger(customers, beta) -> list[dict]:
    r = rng("ledger")
    by_id = {c["id"]: c for c in customers}
    live = [c for c in customers if c["status"] == "active" and c["tier"] != "enterprise"]
    out = []
    for d in days(date(2026, 8, 2), date(2026, 11, 26)):
        if not workday(d):
            continue
        for _ in range(r.randint(3, 7)):
            c = r.choice(live)
            amt = r.randint(30, 160) if c["tier"] == "starter" else r.randint(60, 480)
            out.append({"at": datetime(d.year, d.month, d.day, r.randint(8, 17), r.randint(0, 59)), "cust": c,
                        "amt": amt, "reason": r.choice(["billing_error", "billing_error", "service_issue", "goodwill"]),
                        "note": r.choice(["seat billed after removal", "double charge", "late cancellation", "app outage "
                                          "(time clock)", "per call with admin"]), "by": r.choice(SUPPORT), "via": "console"})
        if r.random() < 0.25:
            c = r.choice([x for x in customers if x["tier"] == "growth"])
            out.append({"at": datetime(d.year, d.month, d.day, 15, r.randint(0, 59)), "cust": c, "amt": r.randint(600, 2400),
                        "reason": "service_issue", "note": "approved by account manager", "by": "michal.biton",
                        "via": "console"})
    for c in beta["calls"]:
        if c["tool"] == "issue_credit":
            out.append({"at": c["ex"], "cust": by_id[c["cust"]], "amt": c["amount"], "reason": "assist",
                        "note": c["note"], "by": "svc-support-admin", "via": "api", "call": c["id"]})
    for row in beta["rescue"]:
        if row["credit"]:
            out.append({"at": row["at"] + timedelta(seconds=40), "cust": row["cust"], "amt": row["credit"],
                        "reason": "goodwill", "note": "retention goodwill - thank you for staying with Lumen",
                        "by": "svc-support-admin", "via": "api", "rescue": True})
    for i in range(37):
        c = live[(i * 41) % len(live)]
        out.append({"at": datetime(2026, 9, 17, 23, 12) + timedelta(seconds=7 * i), "cust": c, "amt": 19,
                    "reason": "billing_error", "note": "INC-2291 bulk fix: duplicate seat charge", "by": "svc-support-admin",
                    "via": "api", "script": True})
    out.sort(key=lambda x: (x["at"], x["cust"]["id"]))
    stale_ids = {c["id"] for c in beta["stale"]}
    for i, x in enumerate(out):
        x["id"] = f"CR-{24000 + i}"
        run = thursday_run(x["at"])
        x["run"] = run
        x["status"] = "applied" if run <= EXPORT_AT else "pending"
        x["rev_at"], x["rev_by"] = "", ""
        if x.get("call") in stale_ids and x["status"] == "pending":
            x["status"] = "reversed"
            x["rev_at"] = datetime(2026, 11, 23, 9, 12) if x["cust"]["name"] == "Tavor Engineering" else datetime(2026, 11, 22, 17, 40)
            x["rev_by"] = "fatma.abu-ras"
        if x.get("rescue") and x["amt"] > 2000:
            x["status"] = "reversed"
            x["rev_at"], x["rev_by"] = datetime(2026, 10, 6, 8, 52), "shira.navon"
    return out


def build_rescue(customers) -> list[dict]:
    """Renewal Rescue: nightly, accounts with >= 20 seats whose active users fell 40% or more."""
    r = rng("rescue")
    cands = [c for c in customers if c["status"] == "active" and c["seats"] >= 20]
    rows = []
    forced = {"Shaked Clinics": date(2026, 10, 27)}
    ent = [c for c in cands if c["tier"] == "enterprise" and c["name"] not in forced]
    forced_ent = {ent[5]["id"]: date(2026, 9, 9), ent[17]["id"]: date(2026, 11, 15)}
    annual = sorted([c for c in cands if c["tier"] == "growth" and c["billing"] == "annual"],
                    key=lambda c: (abs(c["seats"] - 85), c["id"]))
    big = annual[0]
    for d in days(RESCUE_START, date(2026, 11, 26)):
        night = datetime(d.year, d.month, d.day, 2, 0)
        picks = []
        for _ in range(r.choice([1, 2, 2, 3, 3, 4])):
            c = r.choice(cands)
            if c["tier"] == "enterprise":
                continue
            picks.append(c)
        for c in cands:
            if forced.get(c["name"]) == d or forced_ent.get(c["id"]) == d:
                picks.append(c)
        if d == date(2026, 10, 4):
            picks.append(big)
        for k, c in enumerate(picks):
            at = night + timedelta(minutes=2 * k, seconds=r.randint(0, 50))
            credit = None
            if c["tier"] == "enterprise":
                credit = "denied"
            elif c["billing"] == "monthly":
                credit = round(c["monthly"] * 0.10)
            elif d == date(2026, 10, 4) and c is big:
                credit = round(c["monthly"] * 12 * 0.10)
            elif d >= date(2026, 10, 5):
                credit = round(c["monthly"] * 0.10)
            rows.append({"at": at, "cust": c, "credit": credit if credit != "denied" else None,
                         "denied": credit == "denied"})
    return rows


def write_fleet(customers, beta, ledger) -> None:
    r = rng("audit")
    audit = []
    start = datetime(2026, 9, 1)
    for c in beta["calls"]:
        act = {"issue_credit": "billing.credit.create", "email_customer": "email.send", "change_plan": "plan.change"}.get(c["tool"])
        if act:
            det = f"{c['amount']} ILS" if c["amount"] else c["target"]
            audit.append([c["ex"], "svc-support-admin", "token", "tok_01", "lumen-assist-worker/1.7", "aws eu-central-1",
                          act, c["cust"], det, "ok"])
    for row in beta["rescue"]:
        if row["at"] < start:
            continue
        c = row["cust"]
        audit.append([row["at"], "svc-support-admin", "token", "tok_01", "n8n/1.64 (n8n.cloud)", "n8n cloud", "email.send",
                      c["id"], f"admin@{c['domain']}", "ok"])
        if row["credit"] or row["denied"]:
            audit.append([row["at"] + timedelta(seconds=40), "svc-support-admin", "token", "tok_01", "n8n/1.64 (n8n.cloud)",
                          "n8n cloud", "billing.credit.create", c["id"],
                          f"{row['credit']} ILS" if row["credit"] else f"{round(c['monthly'] * 0.1)} ILS",
                          "ok" if row["credit"] else "denied: contract account (finance approval required)"])
    for x in ledger:
        if x["at"] < start:
            continue
        if x["via"] == "console":
            audit.append([x["at"], f"{x['by']}@lumen.io", "user", "", "console (Chrome)", "office", "billing.credit.create",
                          x["cust"]["id"], f"{x['amt']} ILS", "ok"])
        elif x.get("script"):
            audit.append([x["at"], "svc-support-admin", "token", "tok_01", "python-requests/2.32.3", "office VPN",
                          "billing.credit.create", x["cust"]["id"], f"{x['amt']} ILS", "ok"])
    live = [c for c in customers if c["status"] == "active"]
    trials = [c for c in customers if c["status"] == "trial"]
    for d in days(start.date(), date(2026, 11, 26)):
        if workday(d):
            for _ in range(r.randint(4, 8)):
                c = r.choice(live)
                audit.append([datetime(d.year, d.month, d.day, r.randint(8, 17), r.randint(0, 59)),
                              f"{r.choice(SUPPORT)}@lumen.io", "user", "", "console (Chrome)", "office", "plan.change",
                              c["id"], r.choice(["+1 seat", "+3 seats", "-2 seats", "starter -> growth", "+5 seats"]), "ok"])
            for _ in range(r.randint(1, 4)):
                c = r.choice(live)
                audit.append([datetime(d.year, d.month, d.day, r.randint(8, 17), r.randint(0, 59)),
                              f"{r.choice(SUPPORT)}@lumen.io", "user", "", "console (Chrome)", "office", "user.2fa.reset",
                              c["id"], "verified: callback to number on file", "ok"])
            if r.random() < 0.2:
                c = r.choice(live)
                audit.append([datetime(d.year, d.month, d.day, 12, r.randint(0, 59)), "nurit.gal@lumen.io", "user", "",
                              "console (Chrome)", "office", "data.delete", c["id"], "soft delete (privacy request PR-"
                              f"{r.randint(300, 399)})", "ok"])
        for _ in range(r.randint(1, 4)):
            pool = [t for t in trials if t["since"] <= d] or live
            c = r.choice(pool)
            audit.append([datetime(d.year, d.month, d.day, r.randint(0, 23), r.randint(0, 59)), "mkt-zapier", "token",
                          "tok_07", "Zapier", "zapier.com", r.choice(["email.send", "email.send", "trials.extend"]), c["id"],
                          "nurture step", "ok"])
        if r.random() < 0.22:
            c = r.choice([x for x in live if x["seats"] >= 40])
            audit.append([datetime(d.year, d.month, d.day, r.randint(9, 19), r.randint(0, 59)), "lumengpt-slack", "token",
                          "tok_08", "lumengpt-slack/0.4", "aws eu-central-1", "account.export", c["id"],
                          "staff list (csv) requested in #sales-help", "ok"])
    for i in range(12):
        c = live[(i * 97) % len(live)]
        audit.append([datetime(2026, 10, 29, 22, 40) + timedelta(seconds=11 * i), "svc-support-admin", "token", "tok_01",
                      "python-requests/2.32.3", "office VPN", "plan.change", c["id"], "migrate legacy plan code", "ok"])
    audit.sort(key=lambda x: (x[0], x[1], x[7]))
    write_csv(ROOM / "it" / "admin-audit-log.csv",
              ["timestamp", "actor", "actor_type", "token_id", "user_agent", "source", "action", "customer_id", "detail",
               "result"], [[ts(a[0])] + a[1:] for a in audit])
    write_csv(ROOM / "billing" / "credits-ledger.csv",
              ["credit_id", "created_at", "customer_id", "plan", "amount_ils", "reason_code", "note", "issued_by",
               "channel", "invoice_run", "status", "reversed_at", "reversed_by"],
              [[x["id"], ts(x["at"]), x["cust"]["id"], x["cust"]["tier"], x["amt"], x["reason"], x["note"], x["by"], x["via"],
                x["run"].date().isoformat(), x["status"], ts(x["rev_at"]) if x["rev_at"] else "", x["rev_by"]]
               for x in ledger])
    write_csv(ROOM / "it" / "api-tokens.csv",
              ["token_id", "name", "created_at", "created_by", "team", "scopes", "last_used", "expires", "status",
               "description"], [list(t) for t in TOKENS])
    write_csv(ROOM / "it" / "ai-inventory-2026-09.csv",
              ["system", "owner", "department", "purpose", "data", "status", "added"], [list(x) for x in INVENTORY])
    re = rng("expenses")
    rows = []
    for dept, who, vendor, desc, m1, m2, lo, hi in EXPENSES:
        for m in range(m1, m2 + 1):
            rows.append([f"2026-{m:02d}", dept, who, vendor, desc, re.randint(lo, hi) if hi > lo else lo])
    rows.sort(key=lambda x: (x[0], x[1], x[3]))
    write_csv(ROOM / "it" / "saas-expenses-ai-2026.csv",
              ["month", "department", "cardholder", "vendor", "description", "amount_ils"], rows)
    write_csv(ROOM / "it" / "feature-flags-log.csv",
              ["timestamp", "flag", "change", "rule", "changed_by", "comment"], [list(f) for f in FLAGS])
