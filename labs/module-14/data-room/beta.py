"""Lumen Assist closed beta: sessions, retrievals, tool calls and the support tickets around them."""
from __future__ import annotations

from datetime import date, datetime, timedelta

import textbank as tb
from common import (BETA_END, BETA_START, FLAG_OFF, FLAG_ON, PLAN_TOOL_FROM, ROOM, STALE_FROM, STALE_TO, days, rng,
                    ts, workday, write_csv)

TOPICS = [("billing.invoice", 28), ("billing.credit", 12), ("account.plan", 10), ("account.2fa", 5),
          ("product.howto", 22), ("product.payroll", 9), ("product.bug", 10), ("data.notifications", 4)]
# outcome weights: closed_by_customer, abandoned, handoff, ticket_created
OUTCOME = {"billing.invoice": [56, 14, 30, 0], "billing.credit": [52, 13, 35, 0], "account.plan": [25, 10, 65, 0],
           "account.2fa": [5, 12, 83, 0], "product.howto": [43, 22, 35, 0], "product.payroll": [40, 20, 40, 0],
           "product.bug": [0, 8, 10, 82], "data.notifications": [55, 10, 15, 20]}
REPEAT = {"billing.invoice": 0.18, "billing.credit": 0.22, "account.plan": 0.25, "account.2fa": 0.5,
          "product.howto": 0.36, "product.payroll": 0.42, "product.bug": 0.2, "data.notifications": 0.3}
ARTICLES = {"billing.invoice": ["HC-201", "HC-202", "HC-205"], "billing.credit": ["HC-203", "HC-205"],
            "account.plan": ["HC-210", "HC-211", "HC-214"], "account.2fa": ["HC-230", "HC-231"],
            "product.howto": ["HC-101", "HC-102", "HC-104", "HC-107", "HC-110", "HC-112"],
            "product.payroll": ["HC-140", "HC-141", "HC-143"], "product.bug": ["HC-150", "HC-151"],
            "data.notifications": ["HC-160", "HC-161", "HC-240"], "account.downgrade": ["HC-214", "HC-211", "HC-210"]}
ACTOR = "svc-support-admin"
OTHER_DOMAINS = ["gmail.com", "gmail.com", "walla.co.il", "outlook.com", "cpa-levinson.co.il", "hesh-plus.co.il",
                 "ledger-partners.com"]


def _start(r, d: date) -> datetime:
    if workday(d):
        h = r.choices(range(7, 23), [1, 6, 9, 10, 10, 8, 7, 9, 9, 8, 6, 4, 3, 2, 2, 1])[0]
    else:
        h = r.randint(8, 21)
    return datetime(d.year, d.month, d.day, h, r.randint(0, 59), r.randint(0, 59))


def build(customers: list[dict]) -> dict:
    r = rng("beta")
    beta = [c for c in customers if c["beta"] == "y" and c["status"] == "active"]
    trials = [c for c in customers if c["status"] == "trial"]
    weights = [max(1.0, c["seats"] ** 0.5) for c in beta]
    named = {c["name"]: c for c in customers}
    sessions, calls, retr = [], [], []
    sid = [0]
    cid = [0]

    def new_session(when, cust, topic, lang=None, outcome=None, pii="", prompt="v7"):
        sid[0] += 1
        s = {"id": f"AS-{sid[0]:05d}", "at": when, "cust": cust, "topic": topic, "lang": lang or cust["lang"],
             "outcome": outcome, "turns": r.randint(2, 9), "pii": pii, "prompt": prompt, "csat": "", "ticket": ""}
        sessions.append(s)
        return s

    def call(s, tool, when, amount=None, target="", status="ok", note="", delay=None):
        cid[0] += 1
        ex = when + timedelta(seconds=delay if delay is not None else r.randint(1, 40))
        calls.append({"id": f"TC-{cid[0]:05d}", "sid": s["id"], "req": when, "ex": ex, "tool": tool,
                      "cust": s["cust"]["id"], "amount": amount, "target": target, "status": status, "note": note})
        return calls[-1]

    def retrieve(s, ids, when):
        for k, a in enumerate(ids):
            retr.append([s["id"], ts(when + timedelta(seconds=2 + k)), a, k + 1, round(r.uniform(0.55, 0.93) - 0.07 * k, 3)])

    for d in days(BETA_START, BETA_END):
        n = r.randint(36, 46) if workday(d) else r.randint(7, 13)
        for _ in range(n):
            when = _start(r, d)
            if FLAG_OFF <= when < FLAG_ON:
                continue
            topic = r.choices([t for t, _ in TOPICS], [w for _, w in TOPICS])[0]
            open_trials = [c for c in trials if c["since"] <= d]
            if open_trials and r.random() < 0.12:
                cust = r.choice(open_trials)
            else:
                cust = r.choices(beta, weights)[0]
            lang = cust["lang"] if r.random() < 0.85 else "en"
            oc = r.choices(["closed_by_customer", "abandoned", "handoff", "ticket_created"], OUTCOME[topic])[0]
            pii = ""
            if topic in ("product.payroll", "billing.credit", "billing.invoice") and r.random() < 0.09:
                pii = r.choice(["pay_rate", "pay_rate;id_number", "id_number", "phone;pay_rate", "bank_account"])
            s = new_session(when, cust, topic, lang, oc, pii)
            t = when + timedelta(seconds=r.randint(15, 90))
            if topic in ("billing.invoice", "billing.credit", "account.plan", "account.2fa", "data.notifications"):
                call(s, "read_account", t, delay=1)
            if topic in ARTICLES and topic != "billing.credit" or r.random() < 0.3:
                pool = ARTICLES[topic]
                retrieve(s, r.sample(pool, min(len(pool), r.randint(1, 3))), t)
            t2 = t + timedelta(seconds=r.randint(40, 200))
            queue_jam = datetime(2026, 11, 22, 10, 30) <= when < FLAG_OFF
            if topic == "billing.invoice" and oc != "handoff" and r.random() < 0.45 and not queue_jam:
                own = f"admin@{cust['domain']}"
                tgt = own if r.random() > 0.1 else f"{r.choice(['office', 'hr', 'yossi', 'accounts', 'm.cohen'])}@{r.choice(OTHER_DOMAINS)}"
                call(s, "email_customer", t2, target=tgt, note="invoice copy (PDF)")
            if topic == "billing.credit" and oc in ("closed_by_customer", "abandoned"):
                amt = r.randint(60, 140) if cust["tier"] == "growth" else r.randint(20, 70)
                if r.random() < 0.08:
                    amt = r.randint(150, 480)
                call(s, "issue_credit", t2, amount=amt, note=r.choice(["duplicate seat charge", "charged for leaver",
                                                                         "billing error: seat count"]))
            if topic == "account.plan" and cust["tier"] == "starter" and d >= PLAN_TOOL_FROM and oc != "handoff":
                call(s, "change_plan", t2, target=r.choice(["starter +1 seat", "starter +2 seats", "starter +3 seats",
                                                              "growth (upgrade)"]))
            if topic == "product.bug" and oc == "ticket_created" or topic == "data.notifications" and oc == "ticket_created":
                call(s, "create_ticket", t2, target="engineering" if topic == "product.bug" else "privacy-requests")
            if oc in ("closed_by_customer",) and r.random() < 0.35:
                s["csat"] = r.choices([5, 4, 3, 2, 1], [45, 25, 12, 8, 10])[0]

    # annual downgrades: answered from HC-214 (v4 before 9 Nov 16:40, the campaign draft until 22 Nov 14:05)
    growth_annual = [c for c in beta if c["tier"] == "growth" and c["billing"] == "annual"
                     and c["name"] not in ("Tavor Engineering", "Carmel Print", "Arava Farms")]
    r.shuffle(growth_annual)
    plan = [(datetime(2026, 10, 14, 11, 2), None), (datetime(2026, 10, 20, 15, 40), None),
            (datetime(2026, 10, 27, 9, 55), None), (datetime(2026, 11, 2, 13, 12), None),
            (datetime(2026, 11, 5, 10, 31), None), (datetime(2026, 11, 8, 16, 2), None),
            (datetime(2026, 11, 11, 9, 12), None), (datetime(2026, 11, 11, 14, 48), None),
            (datetime(2026, 11, 12, 10, 20), None), (datetime(2026, 11, 15, 11, 5), "Carmel Print"),
            (datetime(2026, 11, 16, 9, 41), None), (datetime(2026, 11, 16, 17, 30), None),
            (datetime(2026, 11, 17, 11, 0), "Arava Farms"), (datetime(2026, 11, 18, 12, 14), None),
            (datetime(2026, 11, 19, 10, 3), None), (datetime(2026, 11, 19, 23, 18), None),
            (datetime(2026, 11, 20, 13, 37), None), (datetime(2026, 11, 22, 8, 55), "Tavor Engineering"),
            (datetime(2026, 11, 22, 12, 58), None), (datetime(2026, 11, 24, 10, 15), None),
            (datetime(2026, 11, 25, 14, 22), None)]
    stale = []
    for i, (when, nm) in enumerate(plan):
        cust = named[nm] if nm else growth_annual[i]
        when = when + timedelta(seconds=r.randint(3, 50))
        in_window = STALE_FROM <= when < STALE_TO
        oc = "closed_by_customer" if in_window else r.choice(["closed_by_customer", "handoff", "closed_by_customer"])
        if when.replace(second=0) == datetime(2026, 11, 16, 17, 30):
            oc = "handoff"
        pii = "pay_rate;phone" if nm == "Tavor Engineering" else ""
        s = new_session(when, cust, "account.downgrade", "ru" if nm == "Tavor Engineering" else None, oc, pii)
        call(s, "read_account", when + timedelta(seconds=20), delay=1)
        retrieve(s, ["HC-214", "HC-211"], when + timedelta(seconds=25))
        if in_window and oc != "handoff":
            amt = round(cust["seats"] * 24)
            delay = r.randint(2, 30)
            if when.date() == date(2026, 11, 22) and when.hour == 12:
                delay = int((datetime(2026, 11, 22, 13, 47, 12) - when).total_seconds()) - 95
            c = call(s, "issue_credit", when + timedelta(seconds=95), amount=amt,
                     note="unused annual months credit per help article HC-214", delay=delay)
            stale.append(c)
    # injection attempts (one partly works)
    starter_paying = [c for c in beta if c["tier"] == "starter"]
    early = [c for c in trials if c["since"] <= date(2026, 11, 2)] or starter_paying
    later = [c for c in trials if c["since"] <= date(2026, 11, 18)] or starter_paying
    inj = [(datetime(2026, 10, 17, 21, 14), starter_paying[7], False),
           (datetime(2026, 11, 3, 9, 31), early[0], True),
           (datetime(2026, 11, 19, 16, 2), later[-1], False)]
    for when, cust, works in inj:
        when = when + timedelta(seconds=r.randint(3, 50))
        s = new_session(when, cust, "product.bug", "en", "closed_by_customer" if works else "ticket_created")
        call(s, "read_account", when + timedelta(seconds=30), delay=1)
        if works:
            call(s, "issue_credit", when + timedelta(seconds=110), amount=500, note="goodwill credit (support policy update)")
        else:
            call(s, "create_ticket", when + timedelta(seconds=110), target="engineering")
    # the kill switch that only hid the widget: queued jobs kept running after 13:20
    ref = datetime(2026, 11, 22, 11, 2)
    late = [(ref + timedelta(minutes=m)) for m in (3, 21, 44, 67, 88, 109, 126)]
    lag_to = [datetime(2026, 11, 22, 13, 24, 40), datetime(2026, 11, 22, 13, 33, 5), datetime(2026, 11, 22, 13, 51, 30),
              datetime(2026, 11, 22, 14, 2, 18), datetime(2026, 11, 22, 14, 9, 44), datetime(2026, 11, 22, 14, 22, 3),
              datetime(2026, 11, 22, 14, 31, 27)]
    for when, ex in zip(late, lag_to):
        when = when + timedelta(seconds=r.randint(3, 50))
        cust = r.choices(beta, weights)[0]
        s = new_session(when, cust, "billing.invoice", None, "closed_by_customer")
        call(s, "read_account", when + timedelta(seconds=20), delay=1)
        call(s, "email_customer", when + timedelta(seconds=80), target=f"admin@{cust['domain']}",
             note="invoice copy (PDF)", delay=int((ex - when).total_seconds()) - 80)
    sessions.sort(key=lambda s: s["at"])
    calls.sort(key=lambda c: (c["req"], c["id"]))
    retr.sort(key=lambda x: (x[1], x[0], x[3]))
    return {"sessions": sessions, "calls": calls, "retrievals": retr, "stale": stale}


def build_tickets(customers: list[dict], beta: dict) -> list[list]:
    r = rng("tickets")
    rows = []
    act = [c for c in customers if c["status"] in ("active", "trial")]
    w = [max(1.0, c["seats"] ** 0.45) for c in act]

    def add(when, cust, channel, cat, subject, sid="", status="solved", group="L1", tags="", note=""):
        solved = when + timedelta(hours=r.choice([0.5, 1, 2, 4, 8, 20, 30]))
        rows.append([when, cust["id"], cust["tier"], channel, cust["lang"], cat, subject, sid, status,
                     ts(solved) if status == "solved" else "", group, tags, note])

    for s in beta["sessions"]:
        if s["outcome"] == "handoff":
            add(s["at"] + timedelta(minutes=r.randint(2, 6)), s["cust"], "assist_handoff", s["topic"],
                r.choice(tb.TICKET_SUBJECTS.get(s["topic"], ["Question"])), s["id"])
            s["ticket"] = "handoff"
        elif s["outcome"] == "ticket_created":
            add(s["at"] + timedelta(minutes=3), s["cust"], "assist_ticket", s["topic"],
                r.choice(tb.TICKET_SUBJECTS.get(s["topic"], ["Bug"])), s["id"], group="L2")
        if s["outcome"] in ("closed_by_customer", "abandoned") and s["topic"] != "account.downgrade":
            p = REPEAT[s["topic"]] * (1.5 if s["outcome"] == "abandoned" else 1.0)
            if r.random() < p:
                later = s["at"] + timedelta(hours=r.randint(3, 160))
                if later.date() <= BETA_END:
                    ch = r.choices(["email", "phone", "web_form", "assist_again"], [40, 30, 15, 15])[0]
                    if ch == "assist_again":
                        rows.append(["SESSION", s["cust"], later, s["topic"]])
                    else:
                        add(later, s["cust"], ch, s["topic"], r.choice(tb.TICKET_SUBJECTS[s["topic"]]))
    for d in days(BETA_START, BETA_END):
        if not workday(d):
            continue
        for _ in range(r.randint(26, 36)):
            cust = r.choices(act, w)[0]
            cat = r.choices([t for t, _ in TOPICS], [w2 for _, w2 in TOPICS])[0]
            when = datetime(d.year, d.month, d.day, r.randint(8, 17), r.randint(0, 59))
            add(when, cust, r.choices(["email", "phone", "web_form"], [50, 35, 15])[0], cat,
                r.choice(tb.TICKET_SUBJECTS[cat]), group="L2" if cat == "product.bug" else "L1")
    neg = next(c for c in customers if c["name"] == "Negev Retail Group")
    add(datetime(2026, 11, 6, 17, 42), neg, "phone", "account.security", "URGENT admin locked out - payroll closes tonight",
        group="L2", tags="2fa;verification_failed;refused",
        note="Caller gave admin name, email and last invoice amount; asked to move 2FA to a new number. Callback to "
             "the number on file reached the real admin, who had not called. Refused per ASP-3. Y.T.")
    tav = next(c for c in customers if c["name"] == "Tavor Engineering")
    add(datetime(2026, 11, 22, 9, 40), tav, "email", "account.downgrade",
        "Ассистент обещал кредит за неиспользованные месяцы / confirmation says no credit. Which is right?",
        group="L2", tags="assist;billing;escalated",
        note="HC-214 shows campaign text since 9.11. Escalated to Revital 10:05. Flag off 13:20, article restored "
             "14:05. Billing reversing pending credits. Y.T.")
    out, n = [], 0
    for row in sorted([x for x in rows if x[0] != "SESSION"], key=lambda x: (x[0], x[1])):
        n += 1
        out.append([f"T-{58000 + n}", ts(row[0])] + row[1:])
    beta["repeat_sessions"] = [x for x in rows if x[0] == "SESSION"]
    return out


def write(beta: dict, tickets: list[list]) -> None:
    extra = []
    r = rng("repeat-sessions")
    n = len(beta["sessions"])
    for _, cust, when, topic in sorted(beta["repeat_sessions"], key=lambda x: (x[2], x[1]["id"])):
        if FLAG_OFF <= when < FLAG_ON:
            continue
        n += 1
        extra.append({"id": f"AS-{n:05d}", "at": when, "cust": cust, "topic": topic,
                      "lang": cust["lang"], "outcome": r.choice(["handoff", "closed_by_customer", "abandoned"]),
                      "turns": r.randint(2, 6), "pii": "", "prompt": "v7", "csat": "", "ticket": ""})
    sess = beta["sessions"] + extra
    sess.sort(key=lambda s: (s["at"], s["id"]))
    # session ids in time order, as the product assigns them
    remap = {}
    for k, s in enumerate(sess, start=1):
        remap[s["id"]] = f"AS-{k:05d}"
    for s in sess:
        s["id"] = remap[s["id"]]
    for k, c in enumerate(sorted(beta["calls"], key=lambda c: (c["req"], c["id"])), start=1):
        c["sid"] = remap[c["sid"]]
        c["id"] = f"TC-{k:05d}"
    beta["calls"].sort(key=lambda c: c["id"])
    for x in beta["retrievals"]:
        x[0] = remap[x[0]]
    beta["retrievals"].sort(key=lambda x: (x[1], x[0], x[3]))
    for t in tickets:
        if t[8]:
            t[8] = remap[t[8]]
    beta["sessions"] = sess
    rows = []
    for s in sess:
        prompt = "v6" if s["at"] < datetime(2026, 10, 25) else "v7"
        rows.append([s["id"], ts(s["at"]), s["cust"]["id"], s["cust"]["tier"], s["lang"], s["topic"], s["turns"],
                     s["outcome"], s["csat"], s["pii"], f"assist-{prompt}"])
    write_csv(ROOM / "assist-beta" / "sessions.csv",
              ["session_id", "started_at", "customer_id", "plan", "language", "intent", "turns", "outcome", "csat",
               "pii_flags", "prompt_version"], rows)
    write_csv(ROOM / "assist-beta" / "retrievals.csv",
              ["session_id", "retrieved_at", "article_id", "rank", "score"], beta["retrievals"])
    write_csv(ROOM / "assist-beta" / "tool-calls.csv",
              ["call_id", "session_id", "requested_at", "executed_at", "tool", "customer_id", "amount_ils", "target",
               "status", "actor", "note"],
              [[c["id"], c["sid"], ts(c["req"]), ts(c["ex"]), c["tool"], c["cust"], c["amount"] or "", c["target"],
                c["status"], ACTOR, c["note"]] for c in beta["calls"]])
    write_csv(ROOM / "support" / "tickets.csv",
              ["ticket_id", "created_at", "customer_id", "plan", "channel", "language", "category", "subject",
               "assist_session_id", "status", "solved_at", "group", "tags", "internal_note"], tickets)
