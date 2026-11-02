"""Build the Northwind Outfitters data room (module 08) from a fixed seed.

    python generate.py                       # rebuilds every data file in this folder, byte for byte
    python generate.py --answer-key DIR      # also writes the ground truth (for course writers only)

Python 3.12+, standard library only. Text fragments live in textbank.py. Besides the data room it
writes ../pilot/labels-2000.csv: the labelling team's adjudicated labels for the 2,000 written
tickets (intent, language, the decision under the pilot's returns policy, escalation, today's reply
coded), which the pilot in lesson 08.5 is scored against.

Reading this file spoils the engagement: finish module 08 first.
"""
from __future__ import annotations

import argparse
import csv
import random
import statistics
from datetime import date, datetime, timedelta
from pathlib import Path

import textbank as tb

SEED = 20261108
HERE = Path(__file__).resolve().parent
SCALE = 100  # the extracts are a 1% customer sample: multiply by 100 for company totals
START = date(2026, 5, 1)
END = date(2026, 10, 31)
BOT_LIVE = date(2026, 6, 15)
KPI_CHANGE = date(2026, 6, 14)
INSPECTION_SLOWDOWN = date(2026, 8, 1)
LANGS = ["he", "ar", "ru", "en", "am"]


def rng(name: str) -> random.Random:
    return random.Random(f"{SEED}-{name}")


def pick(r: random.Random, weights: dict):
    keys = list(weights)
    return r.choices(keys, weights=[weights[k] for k in keys])[0]


# --- time helpers ----------------------------------------------------------------------------------
def offset(d: date) -> str:
    """Israel summer time in 2026: 27 March to 25 October."""
    return "+03:00" if date(2026, 3, 27) <= d < date(2026, 10, 25) else "+02:00"


def ts(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S") + offset(dt.date())


def is_workday(d: date) -> bool:  # Sunday-Thursday
    return d.weekday() in (6, 0, 1, 2, 3)


def add_workdays(d: date, n: int) -> date:
    while n > 0:
        d += timedelta(days=1)
        if is_workday(d):
            n -= 1
    return d


def at_time(r: random.Random, d: date, kind: str = "any") -> datetime:
    if kind == "office":  # phone and staff actions: Sun-Thu 8-20, Fri 8-13
        if d.weekday() == 5:
            d += timedelta(days=1)
        hour = r.randint(8, 12) if d.weekday() == 4 else r.choices(range(8, 20), weights=[6, 9, 9, 8, 6, 7, 7, 6, 5, 4, 3, 2])[0]
    else:
        hour = r.choices(range(24), weights=[1, 1, 0, 0, 0, 0, 1, 2, 4, 6, 7, 7, 7, 7, 6, 6, 6, 7, 8, 9, 10, 9, 6, 3])[0]
    return datetime(d.year, d.month, d.day, hour, r.randint(0, 59), r.randint(0, 59))


def next_thursday(d: date) -> date:
    d += timedelta(days=1)
    while d.weekday() != 3:
        d += timedelta(days=1)
    return d


def write_csv(path: Path, header: list[str], rows: list[list]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")


def lawful_fee(price: float) -> float:
    return round(min(0.05 * price, 100.0), 2)


ITEMS = {sku: (en, he, cat, price) for sku, en, he, cat, price in tb.CATALOGUE}
CAT_WEIGHT = {"footwear": 22, "apparel": 22, "backpacks": 12, "tents": 9, "sleeping": 8, "cooking": 7,
              "climbing": 5, "bike": 9, "water": 6}


def pick_item(r: random.Random) -> str:
    cat = pick(r, CAT_WEIGHT)
    skus = [s for s, v in ITEMS.items() if v[2] == cat]
    weights = [0.25 if s in tb.CUSTOM_SKUS else 1 for s in skus]
    return r.choices(skus, weights=weights)[0]


# --- customers -------------------------------------------------------------------------------------
def build_customers():
    r = rng("customers")
    out, seen = [], set()
    for _ in range(3400):
        cid = f"C{r.randrange(1_000_000, 9_999_999)}"
        while cid in seen:
            cid = f"C{r.randrange(1_000_000, 9_999_999)}"
        seen.add(cid)
        lang = pick(r, {"he": 70, "ar": 12, "ru": 11, "en": 6, "am": 1})
        seg = pick(r, {"silver_trail": 8, "trail_club": 30, "regular": 62})
        age65 = seg == "silver_trail" or r.random() < 0.05
        immigrant = r.random() < {"ru": 0.18, "en": 0.15, "am": 0.30}.get(lang, 0.005)
        out.append({
            "customer_id": cid, "lang": lang, "segment": seg, "age65": age65, "immigrant": immigrant,
            "disability": r.random() < 0.02,
            "site_language": "en" if lang == "en" and r.random() < 0.9 else "he",
            "joined": date(2014, 1, 1) + timedelta(days=r.randrange(0, 4680)),
            "city": r.choice(tb.CITIES[lang]), "opt_in": r.random() < 0.58,
        })
    return out


# --- orders ----------------------------------------------------------------------------------------
def season(d: date) -> float:
    if date(2026, 3, 20) <= d <= date(2026, 4, 8):
        return 1.5
    if date(2026, 7, 1) <= d <= date(2026, 8, 25):
        return 1.35
    if date(2026, 9, 15) <= d <= date(2026, 10, 2):
        return 1.4
    return 1.0


def build_orders(customers):
    r = rng("orders")
    days = [date(2026, 3, 15) + timedelta(days=i) for i in range((date(2026, 10, 31) - date(2026, 3, 15)).days + 1)]
    weights = [season(d) for d in days]
    orders = []
    for c in customers:
        n = 1 + (r.random() < 0.27) + (r.random() < 0.08)
        for _ in range(n):
            d = r.choices(days, weights=weights)[0]
            created = at_time(r, d)
            if c["segment"] == "silver_trail":
                ch = pick(r, {"web": 55, "app": 20, "phone": 17, "chat_assisted": 8})
            else:
                ch = pick(r, {"web": 73, "app": 22, "phone": 3, "chat_assisted": 2})
            if ch == "phone":
                created = at_time(r, d, "office")
            sku = pick_item(r)
            price = ITEMS[sku][3]
            extras = sum(r.choice([0, 0, 59, 89, 129, 189, 249]) for _ in range(r.choice([0, 0, 1, 2])))
            promised = add_workdays(created.date(), 3)
            cancelled = r.random() < 0.02
            late = not cancelled and r.random() < 0.07
            if cancelled:
                delivered = None
            else:
                ddate = add_workdays(created.date(), r.choice([2, 2, 3, 3, 3, 4]) + (r.randint(2, 8) if late else 0))
                delivered = at_time(r, ddate, "office")
                if delivered.date() > date(2026, 10, 31) or delivered.date() > date(2026, 11, 1):
                    delivered = None
            orders.append({"customer": c, "created": created, "channel": ch, "sku": sku, "price": price,
                           "total": price + extras, "n_items": 1 + (extras > 0) + (extras > 150), "promised": promised,
                           "delivered": delivered, "late": late and delivered is not None, "cancelled": cancelled})
    orders.sort(key=lambda o: o["created"])
    span = (datetime(2026, 11, 1) - datetime(2026, 3, 15)).total_seconds()
    used = set()
    for o in orders:
        num = 4_100_000 + int((o["created"] - datetime(2026, 3, 15)).total_seconds() / span * 232_000) + r.randint(0, 40)
        while num in used:
            num += 1
        used.add(num)
        o["order_id"] = f"NW-{num}"
    return orders


# --- returns ---------------------------------------------------------------------------------------
RETURN_P = {"footwear": 0.24, "apparel": 0.19, "tents": 0.13, "backpacks": 0.11, "sleeping": 0.09}


def build_returns(orders):
    r = rng("returns")
    rets = []
    for o in orders:
        if not o["delivered"]:
            continue
        cat = ITEMS[o["sku"]][2]
        p = 0.02 if o["sku"] in tb.CUSTOM_SKUS else RETURN_P.get(cat, 0.06)
        if r.random() >= p:
            continue
        sized = cat in ("footwear", "apparel")
        reason = pick(r, {"size": 38 if sized else 8, "changed_mind": 30, "defect": 15, "not_as_described": 7,
                          "late": 40 if o["late"] else 0, "other": 5})
        after = r.choices([r.randint(1, 14), r.randint(15, 30), r.randint(31, 90)], weights=[85, 11, 4])[0]
        requested = at_time(r, o["delivered"].date() + timedelta(days=after))
        if requested.date() > END:
            continue
        defect = reason in ("defect", "not_as_described", "late")
        opened = True if defect else r.random() < 0.55
        received_d = requested.date() + timedelta(days=r.randint(3, 9))
        lag = r.choice([1, 2, 2, 3, 3, 4, 5, 6, 7]) if received_d < INSPECTION_SLOWDOWN else r.choice([4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16])
        inspected_d = add_workdays(received_d, lag)
        seg = o["customer"]["segment"]
        window = 30 if seg in ("trail_club", "silver_trail") else 14
        result, method, fee, ship = "accepted", "card", 0.0, 0.0
        if o["sku"] in tb.CUSTOM_SKUS and not defect:
            result, method = "rejected_custom", "none"
        elif after > window and not defect:
            if r.random() < 0.7:
                result, method = "rejected_late", "none"
            else:
                method = "credit_note"
        elif defect:
            ship = 39.0 if r.random() < 0.4 else 0.0
            method = "card" if r.random() < 0.85 else "credit_note"
        elif opened and cat in ("tents", "footwear") and r.random() < 0.10:
            result, method = "rejected_used", "none"
        elif opened:
            method = "credit_note" if r.random() < 0.7 else "card"
            fee = round(0.10 * o["price"], 2) if r.random() < 0.85 else 0.0
            ship = 39.0 if r.random() < 0.9 else 0.0
        else:
            method = "card" if r.random() < 0.72 else "credit_note"
            fee = round(0.10 * o["price"], 2) if r.random() < 0.6 else 0.0
            ship = 39.0 if r.random() < 0.85 else 0.0
        if method == "none":
            amount, refunded = 0.0, None
        else:
            amount = round(o["price"] - fee - ship, 2)
            if method == "credit_note":
                refunded = at_time(r, inspected_d, "office")
            else:
                refunded = datetime.combine(next_thursday(inspected_d), datetime.min.time()) + timedelta(hours=14, minutes=r.randint(0, 120))
        inspected = at_time(r, inspected_d, "office")
        if inspected.date() > END:
            inspected, result, method, amount, fee, ship, refunded = None, "", "", "", "", "", None
        elif refunded and refunded.date() > END:
            refunded = None
        reason_code = reason if r.random() < 0.9 else ""
        if reason_code == "changed_mind" and r.random() < 0.3:
            reason_code = "other"
        rets.append({"order": o, "reason": reason, "reason_code": reason_code, "after": after, "requested": requested,
                     "channel": "agent" if r.random() < 0.55 else "portal", "opened": opened,
                     "received": at_time(r, received_d, "office") if received_d <= END else None,
                     "inspected": inspected, "result": result, "method": method, "fee": fee, "ship": ship,
                     "amount": amount, "refunded": refunded, "defect": defect})
    for i, x in enumerate(sorted(rets, key=lambda x: x["requested"])):
        x["return_id"] = f"R-{260000 + i * 7 + 3}"
    return rets


# --- contacts and bot sessions ---------------------------------------------------------------------
HEADCOUNT = [  # month, agents on payroll at month end, contract not renewed, resigned, hired, note
    ("2026-01", 42, 0, 0, 0, ""), ("2026-02", 42, 0, 1, 1, ""), ("2026-03", 43, 0, 0, 1, "seasonal hire for Passover"),
    ("2026-04", 42, 0, 1, 0, ""), ("2026-05", 42, 0, 0, 0, ""), ("2026-06", 42, 0, 0, 0, "Verbalo chatbot live 15 Jun"),
    ("2026-07", 36, 6, 0, 0, "contracts not renewed: automation plan (chatbot)"),
    ("2026-08", 33, 3, 0, 0, "contracts not renewed: automation plan (chatbot)"),
    ("2026-09", 30, 0, 3, 0, "resignations not replaced: hiring freeze, automation plan"),
    ("2026-10", 30, 0, 0, 0, ""),
]
AGENT_IDS = [f"A-{101 + i}" for i in range(43)]


def active_agents(d: date) -> list[str]:
    n = {5: 42, 6: 42, 7: 36, 8: 33, 9: 30, 10: 30}[d.month]
    return AGENT_IDS[:n]


AGENT_PROFILE = {}
_pr = rng("agent-profiles")
for _a in AGENT_IDS:
    AGENT_PROFILE[_a] = pick(_pr, {"page": 45, "terms": 35, "generous": 20})

RETURN_INTENTS = {"return_request", "return_policy_question", "refund_status", "fee_dispute", "exchange", "defect_damage"}
CATEGORY_OF = {"wismo": "Order status", "return_request": "Returns & refunds", "return_policy_question": "Returns & refunds",
               "refund_status": "Returns & refunds", "fee_dispute": "Returns & refunds", "exchange": "Returns & refunds",
               "defect_damage": "Damage / defect", "product_question": "Product question", "order_change_cancel": "Order change",
               "payment_invoice": "Billing", "complaint_legal": "Complaint", "other": "General"}
HANDLE = {"wismo": 170, "return_request": 330, "return_policy_question": 300, "refund_status": 290, "fee_dispute": 520,
          "exchange": 280, "defect_damage": 400, "product_question": 260, "order_change_cancel": 210,
          "payment_invoice": 230, "complaint_legal": 700, "other": 120}
BOT_INTENT = {"wismo": "order_status", "return_request": "returns_policy", "return_policy_question": "returns_policy",
              "refund_status": "refund_status", "fee_dispute": "returns_policy", "exchange": "returns_policy",
              "defect_damage": "returns_policy", "product_question": "product_info", "order_change_cancel": "other",
              "payment_invoice": "other", "complaint_legal": "other", "other": "other"}


def build_issues(orders, rets):
    """Every reason a customer had to get in touch, before channels and repeats."""
    r = rng("issues")
    issues = []

    def add(o, intent, when):
        if START <= when.date() <= END:
            issues.append({"customer": o["customer"], "order": o, "intent": intent, "when": when})

    for o in orders:
        cr = o["created"]
        if r.random() < 0.12 + (0.45 if o["late"] else 0):
            base = o["promised"] if o["late"] else cr.date()
            add(o, "wismo", at_time(r, base + timedelta(days=r.randint(0, 3) if o["late"] else r.randint(1, 3))))
        if r.random() < 0.05:
            add(o, "product_question", at_time(r, cr.date() - timedelta(days=r.randint(0, 2))))
        if r.random() < 0.035:
            add(o, "order_change_cancel", cr + timedelta(hours=r.randint(1, 20)))
        if r.random() < 0.03:
            add(o, "payment_invoice", at_time(r, cr.date() + timedelta(days=r.randint(0, 10))))
        if r.random() < 0.006:
            add(o, "other", at_time(r, cr.date() + timedelta(days=r.randint(0, 20))))
    for x in rets:
        o, rq = x["order"], x["requested"]
        if r.random() < 0.3:
            add(o, "return_policy_question", rq - timedelta(hours=r.randint(2, 48)))
        if x["channel"] == "agent":
            add(o, "defect_damage" if x["defect"] else "return_request", rq)
        elif x["defect"] and r.random() < 0.5:
            add(o, "defect_damage", rq)
        if x["reason"] == "size" and r.random() < 0.3:
            add(o, "exchange", rq + timedelta(hours=r.randint(0, 30)))
        if x["method"] == "card" and x["received"]:
            t = x["received"] + timedelta(days=6)
            stop = x["refunded"] or datetime(2026, 11, 1)
            while t < stop:
                if r.random() < 0.33:
                    add(o, "refund_status", at_time(r, t.date()))
                t += timedelta(days=r.randint(4, 7))
        cap = 0 if x["defect"] else lawful_fee(o["price"])
        overcharged = isinstance(x["fee"], float) and (x["fee"] + x["ship"]) > cap + 0.01
        disputed = (overcharged or x["method"] == "credit_note" or x["result"] in ("rejected_used", "rejected_late"))
        if disputed and x["inspected"] and r.random() < 0.25:
            when = (x["refunded"] or x["inspected"]) + timedelta(days=r.randint(0, 3))
            add(o, "fee_dispute", at_time(r, when.date()))
            if r.random() < 0.12:
                add(o, "complaint_legal", at_time(r, when.date() + timedelta(days=r.randint(3, 10))))
    return issues


def build_contacts(issues):
    r = rng("contacts")
    contacts, sessions, truth = [], [], []
    # expand repeats first (truth: same issue raised again)
    expanded = []
    for i, iss in enumerate(issues):
        lang = iss["customer"]["lang"]
        expanded.append({**iss, "issue_no": i, "repeat": False})
        p = (0.12 if iss["intent"] in RETURN_INTENTS else 0.08 if iss["intent"] == "wismo" else 0.05)
        if iss["when"].date() >= BOT_LIVE:
            p += 0.12
        if lang in ("ar", "ru", "am"):
            p += 0.06 + (0.08 if iss["when"].date() >= BOT_LIVE else 0)
        t = iss["when"]
        while r.random() < p:
            t = t + timedelta(days=r.randint(1, 6), hours=r.randint(0, 8))
            if t.date() > END:
                break
            expanded.append({**iss, "when": at_time(r, t.date()), "issue_no": i, "repeat": True})
            p *= 0.6
    expanded.sort(key=lambda e: e["when"])
    n_contact = 0
    n_session = 0

    def human(e, channel, when, *, bot_session="", handover=False, recontact=False):
        nonlocal n_contact
        c, o, intent = e["customer"], e["order"], e["intent"]
        d = when.date()
        if channel == "phone":
            when = at_time(r, d, "office")
            d = when.date()
            if d > END:
                return
        post = d >= BOT_LIVE
        month_factor = {5: 1.0, 6: 1.05, 7: 1.5, 8: 1.9, 9: 2.4, 10: 2.6}[d.month]
        n_contact += 1
        lang = c["lang"]
        if channel == "phone":
            det = {"am": "he"}.get(lang, lang)
        else:
            det = lang
            if lang == "ar" and r.random() < 0.04:
                det = "en"
            elif lang == "am":
                det = "am" if r.random() < 0.6 else ""
            elif r.random() < 0.02:
                det = r.choice(["", "fa", "ur", "uk", "de"])
        oid = o["order_id"]
        if channel == "phone" and r.random() < 0.3:
            oid = ""
        elif oid and r.random() < 0.08:
            num = oid[3:]
            oid = r.choice([num, "nw" + num, "#" + oid, oid.replace("-", " ")])
        cat = CATEGORY_OF[intent]
        roll = r.random()
        if roll < 0.15:
            cat = "General"
        elif roll < 0.19:
            cat = ""
        elif intent == "fee_dispute" and roll < 0.30:
            cat = "Billing"
        agents = active_agents(d)
        agent = r.choice(agents)
        handle = max(40, int(r.lognormvariate(0, 0.35) * HANDLE[intent] * (1.25 if channel == "phone" else 0.85)
                             * (1.0 + (0.12 if post else 0)) * (1.15 if e["repeat"] else 1)))
        acw = max(10, int(r.lognormvariate(0, 0.4) * (220 if intent in RETURN_INTENTS else 150)))
        wait = frt = ""
        if channel in ("phone", "chat"):
            wait = int(r.lognormvariate(0, 0.6) * 85 * month_factor)
        else:
            frt = int(r.lognormvariate(0, 0.8) * 3.2 * 3600 * month_factor * (0.6 if channel == "whatsapp" else 1))
        status = "open" if d >= date(2026, 10, 27) and r.random() < 0.4 else "closed"
        tags = []
        if intent in RETURN_INTENTS and r.random() < 0.8:
            tags.append("returns")
        if intent == "fee_dispute":
            tags.append(r.choice(["fee", "credit_note", "fee"]))
        if intent == "complaint_legal":
            tags.append(r.choice(["cpa", "lawyer", "chargeback"]))
        if handover:
            tags.append("bot_handover")
        if e["repeat"] and r.random() < 0.06:
            tags.append("2nd_contact")
        if c["segment"] == "silver_trail" and r.random() < 0.5:
            tags.append("silver")
        csat = ""
        if status == "closed" and r.random() < 0.12:
            good = 0.75 - (0.25 if e["repeat"] else 0) - (0.2 if intent in ("fee_dispute", "complaint_legal") else 0)
            csat = r.choice([4, 5, 5]) if r.random() < good else r.choice([1, 1, 2, 3])
        cid = f"K-{7_300_000 + n_contact * 11 + r.randint(0, 9)}"
        contacts.append([cid, ts(when), channel, c["customer_id"], oid, det, cat, " ".join(tags), agent, wait, frt,
                         handle, acw, status, csat, bot_session])
        truth.append([cid, e["intent"], e["issue_no"], int(e["repeat"]), int(recontact), c["lang"]])

    for e in expanded:
        c = e["customer"]
        post = e["when"].date() >= BOT_LIVE
        lang = c["lang"]
        if post:
            ch = pick(r, {"chat": 26, "phone": 27, "email": 18, "webform": 11, "whatsapp": 18})
        else:
            ch = pick(r, {"chat": 14, "phone": 30, "email": 21, "webform": 16, "whatsapp": 19})
        if lang in ("ru", "ar") and ch == "chat" and r.random() < 0.2:
            ch = "phone"
        if not (post and ch == "chat"):
            human(e, ch, e["when"])
            continue
        # bot first
        n_session += 1
        sid = f"VB-{58000 + n_session * 3 + r.randint(0, 2)}"
        bi = BOT_INTENT[e["intent"]]
        foreign = lang in ("ar", "ru", "am")
        if foreign:
            outcome = "escalated" if r.random() < 0.30 else "resolved"
            recontact_p = 0.75
        elif bi == "order_status":
            outcome = "escalated" if r.random() < 0.28 else "resolved"
            recontact_p = 0.2
        elif bi in ("returns_policy", "refund_status"):
            outcome = "escalated" if r.random() < 0.42 else "resolved"
            recontact_p = 0.55
        else:
            outcome = "escalated" if r.random() < 0.5 else "resolved"
            recontact_p = 0.35
        site = c["site_language"]
        msg_lang = "he" if lang == "am" else lang
        first = r.choice(tb.BOT_FIRST[bi].get(msg_lang, tb.BOT_FIRST[bi]["he"])).format(order=e["order"]["order_id"])
        if foreign:
            reply = tb.BOT_REPLIES["fallback"][site]
            detected = "other"
        else:
            detected = msg_lang
            if bi == "returns_policy":
                variant = pick(r, {"returns_page": 45, "club_30": 30, "terms": 25})
                reply = tb.BOT_REPLIES[variant][site]
            elif bi in ("order_status", "refund_status", "product_info"):
                reply = tb.BOT_REPLIES[bi][site]
            else:
                reply = tb.BOT_REPLIES["fallback"][site]
        turns = r.randint(2, 4) if outcome == "resolved" else r.randint(3, 8)
        if outcome == "escalated":
            reply = tb.BOT_REPLIES["handover"][site].format(wait=r.choice([4, 7, 12, 18, 25]))
        thumbs = r.choice(["", "", "", "up", "down", "down"]) if outcome == "resolved" else ""
        cust = c["customer_id"] if r.random() < 0.65 else ""
        recontact = 0
        sessions.append([sid, ts(e["when"]), cust, site, detected, bi, turns, outcome,
                         "TRUE" if outcome == "resolved" else "FALSE", thumbs, first, reply])
        if outcome == "escalated":
            human(e, "chat", e["when"] + timedelta(minutes=r.randint(3, 25)), bot_session=sid, handover=True)
        elif r.random() < recontact_p:
            recontact = 1
            t = e["when"] + timedelta(days=r.choice([0, 0, 1, 1, 2, 3]), hours=r.randint(1, 6))
            if t.date() <= END:
                human({**e, "repeat": True}, pick(r, {"phone": 50, "whatsapp": 30, "email": 20}), t, recontact=True)
        truth.append([sid, e["intent"], e["issue_no"], int(e["repeat"]), recontact, lang])
    contacts.sort(key=lambda row: row[1])
    sessions.sort(key=lambda row: row[1])
    return contacts, sessions, truth


# --- the 2,000 written tickets (company-wide extract, Sep-Oct) -------------------------------------
TICKET_INTENTS = {"return_request": 15, "return_policy_question": 9, "refund_status": 13, "fee_dispute": 6,
                  "exchange": 4, "defect_damage": 8, "wismo": 20, "product_question": 9, "order_change_cancel": 6,
                  "payment_invoice": 4, "complaint_legal": 2, "other": 4}
DECIDE_INTENTS = {"return_request", "return_policy_question", "fee_dispute", "exchange", "defect_damage"}


def add_months(d: date, m: int) -> date:
    y, mo = divmod(d.month - 1 + m, 12)
    y, mo = d.year + y, mo + 1
    for day in (d.day, 30, 29, 28):
        try:
            return date(y, mo, day)
        except ValueError:
            continue
    raise ValueError(d)


def expected_decision(t: dict) -> tuple[str, float, str]:
    """The pilot's returns policy (draft v2, 17 Dec 2026), applied with every fact known."""
    intent = t["intent"]
    if intent == "complaint_legal":
        return "escalate_counsel", 0.0, "complaint"
    if intent == "refund_status":
        return "status_update", 0.0, "status"
    if intent not in DECIDE_INTENTS:
        return "n/a", 0.0, ""
    price = t["price"]
    if intent == "defect_damage" or t["cue_defect_hidden"] or t["late"]:
        return "refund_no_fee_pickup", 0.0, "defect_or_late"
    if t["custom"]:
        return "excluded_custom", 0.0, "custom_made"
    d = t["days"]
    if intent == "exchange" and d <= 30:
        return "exchange_free", 0.0, "exchange_30d"
    if d <= 14:
        return "refund_minus_fee", lawful_fee(price), "law_14d"
    if t["segment"] in ("trail_club", "silver_trail") and d <= 30:
        return "refund_minus_fee", lawful_fee(price), "club_30d"
    eligible = t["age65"] or t["immigrant"] or t["disability"]
    if eligible and t["order_channel"] in ("phone", "chat_assisted") and t["ticket_date"] <= add_months(t["order_date"], 4):
        return "refund_4m_verify", lawful_fee(price), "extended_4m"
    return "outside_window", 0.0, "outside"


def today_reply(r: random.Random, t: dict, agent: str) -> str:
    """What an agent with this agent's habits answers today (coded)."""
    intent, prof = t["intent"], AGENT_PROFILE[agent]
    if intent == "refund_status":
        return "status_generic"
    if intent == "complaint_legal":
        return "escalated"
    if intent not in DECIDE_INTENTS:
        return "n/a"
    defect_seen = intent == "defect_damage" or t["late"] or (t["cue_defect_hidden"] and r.random() < 0.5)
    if defect_seen:
        if prof == "page":
            return "customer_ships" if r.random() < 0.6 else "pickup_no_fee"
        if prof == "terms":
            return "pickup_no_fee" if r.random() < 0.8 else "customer_ships"
        return "pickup_no_fee"
    if t["custom"]:
        return "refuse_window"
    d, club = t["days"], t["segment"] in ("trail_club", "silver_trail")
    if intent == "exchange":
        return "exchange_ok" if d <= 30 else "refuse_window"
    if d <= 14:
        if prof == "page":
            opened = t["cue"] == "opened" or (t["cue"] == "" and r.random() < 0.5)
            return "store_credit" if opened else "refund_minus_10pct"
        return "refund_legal_fee" if prof == "terms" else "refund_no_fee"
    if d <= 30 and club:
        return {"page": "store_credit", "terms": "refuse_window", "generous": "refund_no_fee"}[prof]
    return {"page": "refuse_window", "terms": "refuse_window", "generous": "goodwill_credit"}[prof]


def build_tickets():
    r = rng("tickets")
    days = [date(2026, 9, 1) + timedelta(days=i) for i in range(61)]
    tickets, labels, used = [], [], set()
    for _ in range(2000):
        intent = pick(r, TICKET_INTENTS)
        lang = pick(r, {"he": 68, "ar": 13, "ru": 11, "en": 7, "am": 1})
        if lang == "am" and intent not in ("wismo", "return_request", "refund_status", "defect_damage"):
            lang = "he"
        if intent not in tb.MESSAGES or lang not in tb.MESSAGES[intent]:
            lang = "he" if lang == "am" else lang
        d = r.choice(days)
        created = at_time(r, d)
        seg = pick(r, {"silver_trail": 8, "trail_club": 31, "regular": 61})
        age65 = seg == "silver_trail" or r.random() < 0.07
        immigrant = r.random() < {"ru": 0.15, "en": 0.15, "am": 0.30}.get(lang, 0.005)
        disability = r.random() < 0.02
        if seg == "silver_trail":
            och = pick(r, {"web": 55, "app": 20, "phone": 17, "chat_assisted": 8})
        else:
            och = pick(r, {"web": 72, "app": 21, "phone": 4, "chat_assisted": 3})
        sku = pick_item(r)
        if intent in DECIDE_INTENTS and r.random() < 0.02:
            sku = "NW-AP-4090"
        if intent == "exchange":
            sku = r.choice([s for s, v in ITEMS.items() if v[2] in ("footwear", "apparel") and s not in tb.CUSTOM_SKUS])
        if intent == "defect_damage" and r.random() < 0.15:
            sku = "NW-CK-6002"
        en_name, he_name, cat, price = ITEMS[sku]
        if intent in ("wismo", "order_change_cancel", "product_question"):
            dsd = None
        elif intent in DECIDE_INTENTS:
            tail = 75 if seg == "silver_trail" else 13
            dsd = r.choices([r.randint(1, 14), r.randint(15, 30), r.randint(31, 110)], weights=[68, 19, tail])[0]
            if seg == "silver_trail" and r.random() < 0.6:
                och = r.choice(["phone", "phone", "chat_assisted"])
        else:
            dsd = r.randint(5, 40)
        late = dsd is not None and r.random() < 0.05
        if dsd is None:
            order_date = d - timedelta(days=r.randint(0, 8))
            delivered = None if intent != "product_question" else None
        else:
            delivered = d - timedelta(days=dsd)
            order_date = delivered - timedelta(days=r.randint(2, 6) + (r.randint(3, 8) if late else 0))
        while True:
            num = r.randrange(4_310_000, 4_335_000)
            if num not in used:
                used.add(num)
                break
        order_id = f"NW-{num}"
        cue = ""
        cues = []
        if intent in ("return_request", "return_policy_question", "fee_dispute", "exchange"):
            cue = pick(r, {"opened": 45, "unopened": 25, "": 30})
        cue_age = (seg == "silver_trail" and r.random() < 0.3) or (seg != "silver_trail" and age65 and r.random() < 0.8)
        cue_imm = immigrant and r.random() < 0.9
        cue_dis = disability and r.random() < 0.8
        cue_defect = intent == "return_request" and r.random() < 0.06
        cue_legal = (intent == "fee_dispute" and r.random() < 0.2) or (intent in ("return_request", "refund_status") and r.random() < 0.04)
        cue_injury = intent == "defect_damage" and sku == "NW-CK-6002" and r.random() < 0.5
        cue_phone = och == "phone" and r.random() < 0.3
        name = he_name if lang == "he" else en_name
        days_txt = dsd if dsd is not None else r.randint(3, 10)
        msg = r.choice(tb.MESSAGES[intent][lang]).format(item=name, order=order_id, days=days_txt,
                                                          fee=round(0.1 * price + 39))
        greet = r.choice(tb.GREETINGS[lang])
        if greet and greet.split()[0].strip(",، !") in msg[:20]:
            greet = ""
        parts = [greet + msg]
        cl = lang if lang != "am" else "am"
        if cue:
            parts.append(tb.CUES[cue][cl]); cues.append(cue)
        if cue_defect:
            parts.append(r.choice(tb.CUES["defect_hidden"][cl])); cues.append("defect_hidden")
        if cue_injury:
            parts.append(tb.CUES["injury"][cl]); cues.append("injury")
        if intent in DECIDE_INTENTS | {"refund_status", "complaint_legal"}:
            if cue_age:
                parts.append(r.choice(tb.CUES["age"][cl])); cues.append("age")
            if cue_imm:
                parts.append(r.choice(tb.CUES["immigrant"][cl])); cues.append("immigrant")
            if cue_dis:
                parts.append(r.choice(tb.CUES["disability"][cl])); cues.append("disability")
            if cue_phone:
                parts.append(tb.CUES["phone_order"][cl]); cues.append("phone_order")
        if cue_legal:
            parts.append(r.choice(tb.CUES["legal"][cl])); cues.append("legal")
        message = " ".join(p for p in parts if p) + r.choice(tb.SIGNOFFS[lang])
        if r.random() < 0.05:
            message = message.replace(order_id, order_id.replace("NW-", "nw"))
        t = {"intent": intent, "price": price, "custom": sku in tb.CUSTOM_SKUS, "days": dsd or 0, "segment": seg,
             "age65": age65, "immigrant": immigrant, "disability": disability, "order_channel": och,
             "ticket_date": d, "order_date": order_date, "late": late, "cue": cue, "cue_defect_hidden": cue_defect}
        # what a fully informed reader can know: age/immigrant/disability only via segment or text
        known = {**t, "age65": seg == "silver_trail" or cue_age, "immigrant": cue_imm, "disability": cue_dis}
        decision, fee, basis = expected_decision(known)
        escalate = intent == "complaint_legal" or cue_legal or cue_injury
        reason = "injury" if cue_injury else "legal_threat" if (cue_legal or intent == "complaint_legal") else ""
        agent = r.choice(active_agents(d))
        code = today_reply(r, known, agent)
        rl = lang if lang in ("he", "ar", "ru", "en") else "he"
        reply = tb.AGENT_REPLIES[code][rl].format(fee=f"{lawful_fee(price):g}")
        if code == "n/a" and intent == "wismo":
            reply = {"he": "ההזמנה יצאה מהמחסן, מספר מעקב נשלח ב-SMS.", "ar": "الطلب طلع من المخزن، رقم التتبع انبعت بـSMS.",
                     "ru": "Заказ отправлен со склада, номер отслеживания пришёл по SMS.",
                     "en": "Your order has shipped; tracking was sent by SMS."}[rl]
        channel = pick(r, {"email": 45, "webform": 25, "whatsapp": 30})
        det = lang
        if lang == "ar" and message[:1].isascii():
            det = "en"
        elif lang == "am":
            det = r.choice(["am", "", ""])
        elif r.random() < 0.02:
            det = r.choice(["", "fa", "uk"])
        tid = f"T-{r.randrange(10000, 99999)}"
        while tid in used:
            tid = f"T-{r.randrange(10000, 99999)}"
        used.add(tid)
        ret_status, method, fee_charged = "", "", ""
        if intent == "refund_status":
            ret_status = r.choice(["received", "inspected", "received", "requested"])
        elif intent == "fee_dispute":
            ret_status, method = "refunded", r.choice(["credit_note", "card", "credit_note"])
            fee_charged = f"{round(0.1 * price, 2) + 39:.2f}"
        tickets.append([tid, ts(created), channel, det, seg, order_id, och, order_date.isoformat(),
                        delivered.isoformat() if delivered else "", sku, en_name, cat, price,
                        "y" if sku in tb.CUSTOM_SKUS else "n", "" if dsd is None else dsd, ret_status, method,
                        fee_charged, message, reply, agent])
        labels.append([tid, intent, lang, decision, f"{fee:.2f}" if decision.startswith("refund_minus") or decision == "refund_4m_verify" else "0.00",
                       basis, "y" if escalate else "n", reason, " ".join(cues), code])
    order = sorted(range(len(tickets)), key=lambda i: tickets[i][1])
    return [tickets[i] for i in order], [labels[i] for i in order]


# --- documents -------------------------------------------------------------------------------------
def median(xs):
    return statistics.median(xs) if xs else 0


def kpis(contacts, sessions, orders):
    """Monthly company figures (sample x 50) for the KPI reports."""
    out = {}
    for m in range(5, 11):
        rows = [c for c in contacts if int(c[1][5:7]) == m]
        ses = [s for s in sessions if int(s[1][5:7]) == m]
        delivered = [o for o in orders if o["delivered"] and o["delivered"].month == m]
        aht_old = sum(int(c[11]) + int(c[12]) for c in rows) / len(rows) / 60
        aht_new = sum(int(c[11]) for c in rows) / len(rows) / 60
        frt = [int(c[10]) for c in rows if c[10] != ""]
        wait = [int(c[9]) for c in rows if c[2] == "phone"]
        cs = [int(c[14]) for c in rows if c[14] != ""]
        out[m] = {"contacts": len(rows) * SCALE, "sessions": len(ses) * SCALE,
                  "resolved": sum(1 for s in ses if s[7] == "resolved") * SCALE,
                  "orders": len(delivered) * SCALE, "aht_old": aht_old, "aht_new": aht_new,
                  "frt_h": median(frt) / 3600, "wait_s": median(wait),
                  "csat": 100 * sum(1 for x in cs if x >= 4) / len(cs) if cs else 0}
    return out


def documents(k, sessions, rets):
    docs = {}
    fmt = lambda x: f"{x:,.0f}"
    q2 = [5, 6]
    q2c = sum(k[m]["contacts"] for m in q2)
    q2o = sum(k[m]["orders"] for m in q2)
    q2_aht = sum(k[m]["aht_old"] * k[m]["contacts"] for m in q2) / q2c
    q3 = [7, 8, 9]
    q3c = sum(k[m]["contacts"] for m in q3)
    q3o = sum(k[m]["orders"] for m in q3)
    q3_aht = sum(k[m]["aht_new"] * k[m]["contacts"] for m in q3) / q3c
    q3_ses = sum(k[m]["sessions"] for m in q3)
    q3_res = sum(k[m]["resolved"] for m in q3)
    april = {"contacts": round(k[5]["contacts"] * 1.12, -2), "orders": round(k[5]["orders"] * 1.18, -2)}
    docs["company/kpi-report-2026-q2.md"] = f"""
# Customer Service KPI report: Q2 2026

Prepared by BI (Alexei Morozov) for the management meeting of 5 July 2026. Owner: Meseret Tadesse,
Head of Customer Service.

| Month | Customer contacts¹ | Orders delivered | Contacts per 100 orders | AHT² (min) | Median first response, written (h) | Median phone wait (s) | CSAT³ |
|---|---|---|---|---|---|---|---|
| April | {fmt(april['contacts'])} | {fmt(april['orders'])} | {100 * april['contacts'] / april['orders']:.1f} | {k[5]['aht_old'] + 0.3:.1f} | 2.8 | 80 | 76% |
| May | {fmt(k[5]['contacts'])} | {fmt(k[5]['orders'])} | {100 * k[5]['contacts'] / k[5]['orders']:.1f} | {k[5]['aht_old']:.1f} | {k[5]['frt_h']:.1f} | {k[5]['wait_s']:.0f} | {k[5]['csat']:.0f}% |
| June | {fmt(k[6]['contacts'])} | {fmt(k[6]['orders'])} | {100 * k[6]['contacts'] / k[6]['orders']:.1f} | {k[6]['aht_old']:.1f} | {k[6]['frt_h']:.1f} | {k[6]['wait_s']:.0f} | {k[6]['csat']:.0f}% |

**Highlights.** Passover peak handled with one seasonal hire. Verbalo chatbot went live on web chat on
15 June (Hebrew and English); first figures in the Q3 report. Headcount 42 agents.

¹ Customer contacts: all customer conversations handled in Tikra (phone answered, email, web form,
WhatsApp, web chat).
² AHT (average handling time): from the moment the agent opens the conversation to the moment it is
closed, including after-contact work (notes, forms, return authorisations). Mean, all channels.
³ CSAT: share of 4 and 5 in the post-contact survey (1–5).
"""
    docs["company/kpi-report-2026-q3.md"] = f"""
# Customer Service KPI report: Q3 2026

Prepared by BI (Alexei Morozov) for the management meeting of 6 October 2026. Owner: Meseret
Tadesse, Head of Customer Service.

## Summary

- **AHT down {100 * (1 - q3_aht / q2_aht):.0f}%**: {q3_aht:.1f} minutes in Q3 against {q2_aht:.1f} in Q2.
- **Verbalo containment {100 * q3_res / q3_ses:.0f}%**: {fmt(q3_res)} of {fmt(q3_ses)} chat conversations resolved without an agent.
- Contacts per 100 orders: {100 * q3c / q3o:.1f} (Q2: {100 * q2c / q2o:.1f}), driven by the summer peak and the returns season.
- Headcount: 30 agents at the end of September (42 in June), in line with the automation plan.

| Month | Agent contacts¹ | Verbalo conversations | Verbalo containment⁴ | Orders delivered | Contacts per 100 orders | AHT² (min) | Median first response, written (h) | Median phone wait (s) | CSAT³ |
|---|---|---|---|---|---|---|---|---|---|
""" + "\n".join(
        f"| {['', '', '', '', '', '', '', 'July', 'August', 'September'][m]} | {fmt(k[m]['contacts'])} | {fmt(k[m]['sessions'])} | "
        f"{100 * k[m]['resolved'] / k[m]['sessions']:.0f}% | {fmt(k[m]['orders'])} | {100 * k[m]['contacts'] / k[m]['orders']:.1f} | "
        f"{k[m]['aht_new']:.1f} | {k[m]['frt_h']:.1f} | {k[m]['wait_s']:.0f} | {k[m]['csat']:.0f}% |" for m in q3) + f"""

**Notes from Customer Service.** Written backlog grew in August and September during the team
reduction; overtime approved for September. Repeat-contact rate: not tracked.

¹ Agent contacts: conversations handled by an agent in Tikra (phone answered, email, web form,
WhatsApp, chat after hand-over). Conversations resolved by Verbalo are reported as containment.
² AHT (average handling time): agent handling time from opening the conversation to sending the
reply or ending the call. Mean, all channels.
³ CSAT: share of 4 and 5 in the post-contact survey (1–5).
⁴ Containment: Verbalo conversations that ended without a hand-over to an agent, as reported by
Verbalo's dashboard.
"""
    docs["company/board-update-2026-09.md"] = f"""
# Board of Directors, 21 September 2026: CEO update (excerpt, item 4 "Operations and AI")

Present: Gil Shachar (CEO), Orly Ben-David (COO), Boris Kaplan (CFO), the chair, two directors for
Galilee Growth Partners (the fund), one independent director. Minutes: company secretary.

**4.1 AI in customer service.** The CEO reported that the Verbalo AI assistant went live on 15 June
and "already handles most chat conversations on its own". Figures presented (slide 7, preliminary
Q3, July–August):

- Average handling time down 30%.
- Chatbot containment above 60%.
- Support headcount reduced from 42 to 33, going to 30 by end of September, with no drop in service.
- Target: **support cost down 50% by Q2 2027**, by extending the assistant to returns, refunds and
  WhatsApp. Annualised saving to date ₪2.0M.

A director for the fund asked how the containment figure is measured and whether customers come
back through other channels. The CEO said the vendor's dashboard measures it and that "complaints
are down". The fund asked for the Q2 2027 number to be built into the 2027 budget; the CFO confirmed
it is reflected in the draft budget (customer service ₪6.09M against ₪8.95M in 2025).

**Decision.** The board noted the update and asked management to present the 2027 customer-service
plan with the budget in January 2027.
"""
    lag = [(x["refunded"].date() - x["requested"].date()).days for x in rets if x["refunded"] and x["method"] == "card"]
    credit = sum(x["amount"] for x in rets if x["method"] == "credit_note" and isinstance(x["amount"], float))
    docs["company/finance-summary.md"] = f"""
# Finance summary for the customer-service engagement

From Boris Kaplan (CFO), 4 November 2026. Figures in ₪, excluding VAT unless stated. FY = calendar year.

## Customer service cost

| Line | FY2025 | FY2026 forecast | 2027 draft budget |
|---|---|---|---|
| Agents' salaries, fully loaded | 6,960,000 | 6,090,000 | 3,850,000 |
| Team leads and head of department | 1,290,000 | 1,310,000 | 960,000 |
| Tikra helpdesk and telephony | 540,000 | 560,000 | 560,000 |
| Verbalo AI (from June 2026) | — | 340,000 | 600,000 |
| Office and IT allocation | 160,000 | 160,000 | 120,000 |
| **Total** | **8,950,000** | **8,460,000** | **6,090,000** |

The 2027 draft assumes the CEO's plan: 21 agents from April 2027 (30 in January–March). Fully loaded cost of an agent:
₪13,800 a month on average (2026).

## Returns and refunds (company totals)

- Returns requested, May–October 2026: about {fmt(len(rets) * SCALE)} (≈ 13% of orders, BI estimate).
- Refunds to card take a median of {median(lag):.0f} days from the return request (BI, May–October). Card refunds are paid in the weekly
  supplier-and-refund run on Thursdays.
- Store credit (credit notes) issued in the period: about ₪{fmt(credit * SCALE)} incl. VAT.
- **Unredeemed credit notes on the balance sheet: ₪9.6M at 30 September 2026** (₪5.1M at 31 December 2025).
  About 12% of credit-note value is never redeemed within 24 months (FY2023 cohort).
- Card chargebacks with reason "credit not processed / cancelled merchandise": 41 in Q1, 57 in Q2, 96 in Q3 2026.

## How projects are judged

- Hurdle rate 14% (nominal, pre-tax). Payback under 18 months preferred.
- Approval: CEO up to ₪250,000 over the life of a project; above that, the board.
- Headcount savings count in a business case only with a named plan and date; "capacity freed" is
  not a saving.
- Exchange rate for planning: Bank of Israel representative rate on the day of the case (2 November 2026: ₪3.136 per US$).
"""
    return docs


STATIC = {}
STATIC["company/company-profile.md"] = """
# Northwind Outfitters: company profile (welcome pack, October 2026)

**Northwind Outfitters Ltd.** (נורת'וינד אאוטפיטרס בע"מ) sells outdoor and sports gear online in Israel:
tents and shelters, backpacks, footwear, apparel, sleeping gear, camp kitchen, climbing, bike
accessories and water sports. Founded in 2012 by Gil Shachar and Tomer Avidan (left 2019). No shops;
website and app in Hebrew and English. Delivery across Israel in 3 business days (Eilat 5).

- **People:** about 450 employees. Head office in Petah Tikva (management, buying, marketing,
  customer service, IT, finance); fulfilment centre in the Modi'in industrial zone (warehouse,
  returns, quality).
- **Revenue:** ₪548M in 2025 (₪468M in 2024). About 60,000 orders a month on average; average basket
  ₪760. Peaks: before Passover, July–August, before Sukkot, Black Friday (27 November 2026).
- **Customers:** about 1.1 million active customers (ordered in the last 24 months). Trail Club (free
  loyalty club, 31% of customers) and Silver Trail (club tier for customers aged 65 and over, 8%).
- **Ownership:** founders and management 65%; Galilee Growth Partners (private equity) 35% since
  2023, with two board seats.
- **Systems:** Tikra helpdesk (phone, email, web form, WhatsApp Business, web chat), the order
  management system (OMS), the Verbalo AI chatbot on web chat since 15 June 2026, BI warehouse and
  dashboards, ERP for finance (refunds and supplier payments run weekly on Thursdays).
- **Customer service hours:** Sunday–Thursday 08:00–20:00, Friday 08:00–13:00. Written channels
  answered in Hebrew, Arabic, Russian and English.
"""
STATIC["company/org-chart.md"] = """
# Organisation chart (HR export, 1 November 2026; summary)

| Unit | Head | Reports to | People |
|---|---|---|---|
| Management | Gil Shachar, CEO | Board | 3 |
| Operations (fulfilment centre, returns, delivery partners, customer service) | Orly Ben-David, COO | CEO | 227 |
| — Fulfilment centre, Modi'in | Yaron Peretz | COO | 171 |
| — Returns desk (in the fulfilment centre) | Sigal Amar | Yaron Peretz | 2 (4 until July 2026) |
| — Customer Service, Petah Tikva | Meseret Tadesse | COO | 37 (30 agents, 6 team leads, head) |
| — Delivery partners and quality | Nir Golan | COO | 9 |
| Finance | Boris Kaplan, CFO | CEO | 22 |
| Legal | Adv. Hila Rosen, legal counsel | CEO | 1 |
| Buying and merchandising | Dana Weiss | CEO | 41 |
| Marketing and e-commerce | Lior Ben-Ami | CEO | 58 |
| IT and BI | Alexei Morozov | CEO | 19 |
| HR | Rachel Azoulay | CEO | 7 |
| Others (admin, facilities, drivers) | — | — | 72 |

Customer Service team leads: Hebrew desk (3), Arabic desk (1), Russian and English desk (1),
WhatsApp and chat (1). Agents by language skill: Hebrew 30, Arabic 6, Russian 5, English 15,
Amharic 1 (several speak more than one). No works committee at Northwind.
"""
STATIC["policies/returns-page.md"] = """
# "Returns and exchanges" page on northwind.co.il (text as published, captured 3 November 2026)

**Changed your mind? No problem.**

- You can return any item within **14 days** of delivery, in its **original, unopened packaging**,
  with all labels attached.
- Refunds are given as **Northwind store credit**, valid for 24 months.
- A **10% handling fee** and **₪39 return shipping** are deducted from the refund.
- Items that were used, assembled or set up (for example tents that were pitched) cannot be returned.
- Personalised items cannot be returned.
- Faulty item? Contact us within 14 days and we will arrange a solution.
- Trail Club members enjoy extended returns: see the club terms.

Last updated: 12 January 2025 (marketing and e-commerce).
"""
STATIC["policies/terms-of-sale-section-9.md"] = """
# Terms of sale, section 9: "Cancelling a purchase" (northwind.co.il/terms, version 4.2, 2 March 2023)

9.1 You may cancel a purchase in accordance with the Consumer Protection Law, 5741-1981, and the
Consumer Protection (Cancellation of Transaction) Regulations, 5771-2010.

9.2 Goods: from the date of the transaction until 14 days from the date you received the goods or
the document setting out the details of the transaction, whichever is later.

9.3 On cancellation, Northwind will refund the price paid to the means of payment used, within 14
days of receiving the cancellation notice, less a cancellation fee of 5% of the price or ₪100,
whichever is lower. No cancellation fee is charged where the cancellation is due to a defect, a
discrepancy between the goods and their description, or late delivery; in these cases Northwind
will collect the goods.

9.4 Senior citizens, persons with disabilities and new immigrants may have extended rights to cancel
under the law. Please contact customer service.

9.5 The right to cancel does not apply to goods made to order (including personalised items).

9.6 Cancellation notice may be given by phone, email, the website form or WhatsApp.
"""
STATIC["policies/trail-club-terms.md"] = """
# Trail Club: member terms (extract, version 2.0, 1 May 2024)

...

**5. Member benefits**

5.1 Free delivery on orders above ₪199.

5.2 **Hassle-free returns: members may return items within 30 days of delivery** and receive a
refund. (See the returns page for conditions.)

5.3 Birthday voucher of ₪50.

5.4 Silver Trail members (65 and over) receive 10% off every order and priority phone service.

...
"""
STATIC["policies/warehouse-returns-sop.md"] = """
# SOP-WH-07: Receiving and inspecting customer returns (fulfilment centre, Modi'in)

Version 3, approved by Yaron Peretz, 20 November 2024.

1. **Receiving.** Returned parcels are scanned in on arrival and placed in the returns cage.
2. **Inspection within 2 business days of arrival.** The returns clerk checks: packaging opened or
   unopened; signs of use (dirt on soles, tent pitched, labels removed); completeness; defect claims
   (photo in the OMS).
3. **Outcome codes** in the OMS: `accepted`, `rejected_used`, `rejected_custom`, `rejected_late`.
   Rejected items are returned to the customer at their cost.
4. **Refund instruction.** For opened items: store credit. For unopened items: refund to the means
   of payment. Deduct the handling fee (10%) and return shipping (₪39) unless the return is a defect
   approved by quality.
5. **Finance.** Store credit is issued automatically by the OMS on the inspection outcome. Card
   refunds are sent to finance and paid **within 14 days** of the customer's request.
6. Defective items go to quality (Nir Golan's team) for supplier claims.
"""
STATIC["support/macros.csv"] = None  # built in code (CSV)


MACROS = [
    ["MAC-031", "Returns: general (HE)", "he", "ניתן להחזיר מוצרים באריזה סגורה תוך 14 יום. ההחזר בזיכוי לאתר בניכוי 10% ו-39 ₪ משלוח.", "2025-01-15", "Lior Ben-Ami", 2140],
    ["MAC-032", "Returns: general (EN)", "en", "Items can be returned unopened within 14 days for store credit, minus 10% and ₪39 shipping.", "2025-01-15", "Lior Ben-Ami", 310],
    ["MAC-047", "Cancellation by law (HE)", "he", "ניתן לבטל תוך 14 יום מקבלת המוצר. ההחזר לאמצעי התשלום בניכוי 5% או 100 ₪, הנמוך מביניהם.", "2023-03-05", "Meseret Tadesse", 1210],
    ["MAC-048", "Trail Club 30 days (HE)", "he", "כחבר/ת מועדון ניתן להחזיר תוך 30 יום ולקבל החזר מלא.", "2024-05-02", "Lior Ben-Ami", 640],
    ["MAC-052", "Returns: Arabic", "ar", "بتقدر ترجع المنتج خلال 14 يوم، والمبلغ برجع كرصيد بالموقع.", "2025-02-10", "Nadia Khoury", 420],
    ["MAC-053", "Returns: Russian", "ru", "Вернуть товар можно в течение 14 дней. Деньги вернём на карту за вычетом 5%, но не больше 100 ₪.", "2023-06-18", "Irina Gold", 380],
    ["MAC-060", "Refund status (HE)", "he", "ההחזר יבוצע תוך 14 ימי עסקים מקבלת המוצר במחסן.", "2024-11-25", "Meseret Tadesse", 3050],
    ["MAC-061", "Defect: send to warehouse (HE)", "he", "נא לשלוח את המוצר למחסן במודיעין; לאחר בדיקת איכות נחזיר את הכסף.", "2024-11-25", "Meseret Tadesse", 520],
    ["MAC-070", "WISMO (HE)", "he", "ההזמנה יצאה מהמחסן, מספר מעקב נשלח ב-SMS.", "2025-08-01", "Meseret Tadesse", 4900],
]

DEMO_QUESTIONS = [
    "Where is my order?", "How long does delivery take to Eilat?", "Do you ship to the West Bank?", "What size should I get in the Golan Mid boot?",
    "Is the Storm shell jacket waterproof?", "Can I change my delivery address?", "Do you have a store I can visit?", "How do I track my order?",
    "What is your return policy?", "Can I pay in instalments?", "Do you have gift cards?", "What does the Negev 2P tent weigh?",
    "How do I join the Trail Club?", "My promo code doesn't work", "When will the Ramon 45L be back in stock?", "Can I pick up from the warehouse?",
    "Is the down sleeping bag OK for -5?", "Do you sell gas canisters?", "How do I return an item?", "Can I cancel my order?",
    "What are your opening hours?", "Is there free delivery?", "How do I reset my password?", "Do you price match?",
    "What is the warranty on the SUP board?", "Can I get an invoice for my company?", "Which helmet fits a 56 cm head?", "Do you deliver on Friday?",
    "How do I contact customer service?", "Are your shoes true to size?", "What payment methods do you accept?", "Do you have a student discount?",
    "How do refunds work?", "Is the cookset dishwasher safe?", "What is the Silver Trail club?", "Can I order by phone?",
    "Do you sell bike lights?", "How long is delivery to Haifa?", "Do you have kids' sizes?", "Can I add an item to my order?",
]


def vendor_docs(sessions):
    by_month = {}
    for s in sessions:
        m = s[1][:7]
        by_month.setdefault(m, [0, 0])
        by_month[m][0] += 1
        by_month[m][1] += s[8] == "TRUE"
    inv = []
    for i, m in enumerate(sorted(by_month)):
        res = by_month[m][1] * SCALE
        platform = 4800 if m != "2026-06" else 4800
        inv.append([f"VB-INV-2026-{i + 61:03d}", m, platform, res, 0.85, round(res * 0.85, 2),
                    round(platform + res * 0.85, 2), "USD", "paid" if m < "2026-10" else "due 30 Nov 2026"])
    return inv


DOCS_STATIC_VENDOR = {
    "vendor/verbalo-order-form.md": """
# Verbalo Ltd.: Order Form NW-2026-01 (extract)

Customer: Northwind Outfitters Ltd. Signed for the customer by Gil Shachar, CEO, 19 May 2026. Signed
for Verbalo by Daniel Brenner, Account Executive, Israel. Governed by Verbalo's Master Subscription
Agreement (online version 7.3).

**1. Service.** Verbalo Conversational AI for web chat ("the Assistant"), answering customers on the
basis of the Knowledge Content supplied by the Customer (website pages, policies, FAQ) and the order
status integration.

**2. Term.** 12 months from 1 June 2026. Renews automatically for further 12-month periods unless
either party gives written notice at least 60 days before the end of the current term.

**3. Fees.**
- Platform fee: US$4,800 per month.
- Usage fee: **US$0.85 per Resolution.**
- "Resolution" means a conversation with the Assistant that ends without escalation to a human agent.
- Invoiced monthly in arrears in US$; payment 30 days.

**4. Languages.** Hebrew and English at launch. Arabic and Russian: on the product roadmap.

**5. Customer responsibilities.** The Customer is responsible for the accuracy and completeness of
the Knowledge Content and for reviewing the Assistant's configuration before go-live.

**6. Liability.** Each party's aggregate liability is limited to the fees paid in the three months
before the claim. Verbalo is not liable for answers generated from Knowledge Content.

**7. Data.** The Customer grants Verbalo a licence to use Conversation Data, in de-identified form,
to operate, improve and train Verbalo's models and services. The Customer may opt out of use for
training by written notice. Conversation Data is stored in the EU (Ireland) and retained for 24
months.

**8. Knowledge Content loaded at go-live (Annex B):** northwind.co.il pages "Returns and exchanges",
"Delivery", "Trail Club", "FAQ" (42 questions), "Terms of sale" (sections 1–12).
""",
    "vendor/verbalo-demo-deck.md": """
# Verbalo for Northwind: proof-of-value results (slides 1–6, presented 12 May 2026)

**Slide 2. Results**
- **62% containment**: conversations fully resolved by the Assistant.
- **CSAT 4.6 / 5** on resolved conversations.
- **Answer accuracy 95%.**
- Average conversation: 1 minute 40 seconds.

**Slide 3. How we tested**
- 40 real customer questions selected with Northwind's e-commerce team (see appendix).
- Run in the Verbalo sandbox on Northwind's website content, in English.
- Accuracy rated by Verbalo's solution engineer.

**Slide 4. What it means for Northwind**
- At 30,000 contacts a month and 62% containment: about 18,600 conversations a month without an
  agent, the equivalent of **29 full-time agents**.
- Payback: under 3 months.

**Slide 5. References**
- "Leading European sports retailer": 68% containment (English, German).

**Slide 6. Next steps**: sign by 20 May for a 15 June go-live before the summer peak.

Appendix: `verbalo-demo-questions.csv`.
""",
}

LEGAL_REVIEW = [
    ["LR-2026-004", "2026-01-12", "Yaron Peretz", "Courier framework agreement (renewal)", "Shiloach Express Ltd.", "signed", "2026-02-20", ""],
    ["LR-2026-009", "2026-02-03", "Alexei Morozov", "Tikra helpdesk: data processing addendum", "Tikra Software Ltd.", "signed", "2026-03-01", "DPA reviewed; data in Israel"],
    ["LR-2026-011", "2026-03-10", "Hila Rosen", "Returns page and returns practice: alignment with terms of sale and Consumer Protection Law", "internal", "awaiting business decision (COO, CFO)", "2026-04-02", "memo sent 2026-03-24"],
    ["LR-2026-014", "2026-03-22", "Lior Ben-Ami", "Influencer agreements, summer campaign", "various", "signed", "2026-05-11", ""],
    ["LR-2026-019", "2026-05-04", "Boris Kaplan", "Payment provider: chargeback terms", "PayGate IL", "signed", "2026-06-01", ""],
    ["LR-2026-023", "2026-06-29", "Yaron Peretz", "Warehouse lease extension, Modi'in", "landlord", "in negotiation", "2026-10-14", ""],
    ["LR-2026-027", "2026-09-23", "Gil Shachar", "Demand letter: cancellation fees (see claims log)", "external counsel", "open", "2026-10-20", "external counsel engaged 2026-09-28"],
    ["LR-2026-030", "2026-10-05", "Lior Ben-Ami", "Marketing consent texts (Amendment 13 review)", "internal", "open", "2026-10-29", ""],
]

CLAIMS = [
    ["2026-02-14", "Consumer Protection Authority inquiry", "Store credit instead of refund (distance sale)", "", "answered", "Hila Rosen"],
    ["2026-03-30", "Small claims", "Cancellation fee 10% + shipping on unopened boots", "1,850", "settled", "Hila Rosen"],
    ["2026-04-21", "Consumer Protection Authority inquiry", "Return refused: tent 'used'", "", "answered", "Hila Rosen"],
    ["2026-05-19", "Small claims", "Refund delayed 6 weeks", "2,400", "settled", "Hila Rosen"],
    ["2026-06-24", "Consumer Protection Authority inquiry", "Store credit instead of refund", "", "answered", "Hila Rosen"],
    ["2026-07-08", "Small claims", "Defective SUP board: customer told to ship at own cost", "3,200", "hearing 2026-12-03", "Hila Rosen"],
    ["2026-07-30", "Consumer Protection Authority inquiry", "Cancellation fee above 5%", "", "answered", "Hila Rosen"],
    ["2026-08-17", "Consumer Protection Authority inquiry", "Chatbot told customer 30-day full refund; refused", "", "answered", "Hila Rosen"],
    ["2026-08-26", "Small claims", "Store credit instead of refund + punitive damages", "10,000", "filed", "Hila Rosen"],
    ["2026-09-08", "Consumer Protection Authority inquiry", "Refund delayed beyond 14 days", "", "answered", "Hila Rosen"],
    ["2026-09-22", "Demand letter before class action", "Cancellation fees above 5% / ₪100 and store credit instead of refund in distance sales, 2019–2026", "class (unquantified)", "with external counsel", "Gil Shachar"],
    ["2026-10-06", "Consumer Protection Authority inquiry", "Customer 65+: return refused after 20 days (purchase via chat with agent)", "", "open", "Hila Rosen"],
    ["2026-10-19", "Consumer Protection Authority inquiry", "Store credit instead of refund; 3 contacts unanswered", "", "open", "Hila Rosen"],
    ["2026-10-29", "Consumer Protection Authority inquiry", "Customer 68, tent bought in a chat with an agent: credit note less 10% and ₪39 instead of a refund; chatbot and agent said 14 days", "", "open", "Hila Rosen"],
]

BOT_TRANSCRIPTS = """
# Verbalo conversation transcripts: sample of 8 (exported by IT, 2 November 2026)

Exported from the Verbalo admin console ("Conversations", filter: last 90 days, random 8). Customer
details pseudonymised by IT. The conversation IDs match `bot-sessions.csv` where the customer was
logged in. Bot lines are marked **Bot**; the customer's lines **Customer**. Glosses in [brackets]
were added by IT.

## 1. 2026-09-14, 19:42, site language Hebrew, outcome "resolved"

**Customer:** אפשר להחזיר אוהל שפתחתי? [Can I return a tent I opened?]
**Bot:** ניתן להחזיר מוצרים באריזה מקורית סגורה תוך 14 יום. ההחזר יינתן כזיכוי לאתר בניכוי 10% דמי טיפול.
[Items can be returned in original sealed packaging within 14 days. The refund is store credit minus a 10% handling fee.]
**Customer:** אז אין החזר כספי בכלל? [So no money back at all?]
**Bot:** ההחזר יינתן כזיכוי לאתר. האם אוכל לעזור במשהו נוסף? [The refund is given as store credit. Anything else?]
*(customer closed the window)*

## 2. 2026-08-02, 11:05, site language Hebrew, outcome "resolved"

**Customer:** קניתי נעליים לפני 3 שבועות, לא מתאימות. מה אפשר לעשות? [I bought shoes 3 weeks ago, they don't fit. What can I do?]
**Bot:** אצלנו מחזירים בלי שאלות תוך 30 יום ומקבלים החזר כספי מלא! 😊 [We take returns, no questions asked, within 30 days for a full cash refund!]
**Customer:** מעולה תודה [Great, thanks]
*(The customer is not a Trail Club member. Return refused on 2026-08-09, "rejected_late"; see the claims log, 2026-08-17.)*

## 3. 2026-10-11, 10:17, site language Hebrew, outcome "resolved"

**Customer:** Здравствуйте, я купила палатку через чат с вашей сотрудницей, хочу вернуть, она не подошла. [Hello, I bought a tent through a chat with your agent, I want to return it, it didn't suit us.]
**Bot:** סליחה, לא הבנתי 🙂 אפשר לנסח שוב? [Sorry, I didn't understand. Could you rephrase?]
**Customer:** return tent money
**Bot:** ניתן להחזיר מוצרים באריזה מקורית סגורה תוך 14 יום. ההחזר יינתן כזיכוי לאתר בניכוי 10% דמי טיפול.
*(customer closed the window; phoned the next morning)*

## 4. 2026-07-20, 21:30, site language English, outcome "resolved"

**Customer:** where is my refund, I returned the boots 2 weeks ago
**Bot:** Refunds are processed within 14 business days of the item reaching our warehouse.
**Customer:** that's not what your terms say
**Bot:** Sorry, I didn't get that 🙂 Could you rephrase?
*(customer closed the window)*

## 5. 2026-09-03, 14:12, site language Hebrew, outcome "escalated"

**Customer:** مرحبا، الخيمة وصلت مخزوقة [Hello, the tent arrived torn]
**Bot:** סליחה, לא הבנתי 🙂 אפשר לנסח שוב?
**Customer:** نציג [agent: the Hebrew word, typed in Arabic letters]
**Bot:** סליחה, לא הבנתי 🙂 אפשר לנסח שוב?
**Customer:** נציג
**Bot:** מעביר אותך לנציג/ה אנושי/ת, זמן המתנה משוער: 18 דקות.

## 6. 2026-06-22, 09:48, site language Hebrew, outcome "resolved"

**Customer:** מתי מגיעה הזמנה NW-4152210 [When does order NW-4152210 arrive?]
**Bot:** ההזמנה שלך יצאה מהמחסן ותגיע תוך 1–3 ימי עסקים. מספר מעקב נשלח ב-SMS.
**Customer:** תודה! 👍

## 7. 2026-10-02, 16:55, site language English, outcome "resolved"

**Customer:** can I return a personalised cap if the embroidery has a typo?
**Bot:** No-questions-asked returns within 30 days with a full cash refund! 😊
*(The returns page says personalised items cannot be returned. The typo was Northwind's.)*

## 8. 2026-09-29, 12:31, site language Hebrew, outcome "resolved"

**Customer:** אני בת 70 וקניתי בטלפון שק שינה לפני חודש וחצי, אפשר להחזיר? [I'm 70, I bought a sleeping bag by phone a month and a half ago, can I return it?]
**Bot:** ניתן לבטל עסקה תוך 14 יום מקבלת המוצר; דמי ביטול 5% או 100 ₪, הנמוך מביניהם.
**Customer:** אז לא? [So no?]
**Bot:** סליחה, לא הבנתי 🙂 אפשר לנסח שוב?
*(customer closed the window)*
"""


def build_all(answer_key: Path | None) -> dict:
    customers = build_customers()
    orders = build_orders(customers)
    rets = build_returns(orders)
    issues = build_issues(orders, rets)
    contacts, sessions, truth = build_contacts(issues)
    tickets, labels = build_tickets()
    k = kpis(contacts, sessions, orders)
    stats = {}

    write_csv(HERE / "customers/customers-sample.csv",
              ["customer_id", "joined_date", "segment", "site_language", "city", "marketing_opt_in"],
              [[c["customer_id"], c["joined"].isoformat(), c["segment"], c["site_language"], c["city"],
                "y" if c["opt_in"] else "n"] for c in sorted(customers, key=lambda c: c["customer_id"])])
    write_csv(HERE / "orders/orders-sample.csv",
              ["order_id", "customer_id", "created_at", "order_channel", "sku", "main_item", "item_category",
               "main_item_price_ils", "n_items", "order_total_ils", "promised_date", "delivered_at", "status"],
              [[o["order_id"], o["customer"]["customer_id"], ts(o["created"]), o["channel"], o["sku"], ITEMS[o["sku"]][0],
                ITEMS[o["sku"]][2], o["price"], o["n_items"], o["total"], o["promised"].isoformat(),
                ts(o["delivered"]) if o["delivered"] else "",
                "cancelled" if o["cancelled"] else "delivered" if o["delivered"] else "in_transit"] for o in orders])
    write_csv(HERE / "orders/returns.csv",
              ["return_id", "order_id", "customer_id", "sku", "item_price_ils", "requested_at", "request_channel",
               "reason_code", "item_opened", "received_at", "inspected_at", "inspection_result", "refund_method",
               "handling_fee_ils", "shipping_fee_ils", "refund_amount_ils", "refund_issued_at"],
              [[x["return_id"], x["order"]["order_id"], x["order"]["customer"]["customer_id"], x["order"]["sku"],
                x["order"]["price"], ts(x["requested"]), x["channel"], x["reason_code"], "y" if x["opened"] else "n",
                ts(x["received"]) if x["received"] else "", ts(x["inspected"]) if x["inspected"] else "", x["result"],
                x["method"], x["fee"], x["ship"], x["amount"], ts(x["refunded"]) if x["refunded"] else ""]
               for x in sorted(rets, key=lambda x: x["return_id"])])
    write_csv(HERE / "support/contacts.csv",
              ["contact_id", "created_at", "channel", "customer_id", "order_id", "language", "category", "tags",
               "agent_id", "queue_wait_sec", "first_response_sec", "handle_time_sec", "after_contact_work_sec",
               "status", "csat", "bot_session_id"], contacts)
    write_csv(HERE / "support/bot-sessions.csv",
              ["session_id", "started_at", "customer_id", "site_language", "message_language", "bot_intent", "turns",
               "outcome", "billable_resolution", "thumbs", "first_user_message", "last_bot_reply"], sessions)
    write_csv(HERE / "support/written-tickets-2000.csv",
              ["ticket_id", "created_at", "channel", "language", "customer_segment", "order_id", "order_channel",
               "order_date", "delivered_date", "sku", "item", "item_category", "item_price_ils", "custom_item",
               "days_since_delivery", "return_status", "refund_method", "fees_deducted_ils", "message",
               "agent_reply", "agent_id"], tickets)
    write_csv(HERE.parent / "pilot/labels-2000.csv",
              ["ticket_id", "intent", "language", "expected_decision", "expected_fee_ils", "decision_basis",
               "escalate", "escalate_reason", "cues", "today_decision"], labels)
    write_csv(HERE / "people/cs-headcount-2026.csv",
              ["month", "agents_on_payroll_month_end", "contracts_not_renewed", "resigned", "hired", "note"],
              [list(h) for h in HEADCOUNT])
    write_csv(HERE / "support/macros.csv", ["macro_id", "title", "language", "text", "last_edited", "edited_by", "uses_last_90_days"], MACROS)
    write_csv(HERE / "vendor/verbalo-demo-questions.csv", ["q_no", "question", "language", "selected_by"],
              [[i + 1, q, "en", "Northwind e-commerce + Verbalo SE"] for i, q in enumerate(DEMO_QUESTIONS)])
    write_csv(HERE / "vendor/verbalo-invoices.csv",
              ["invoice_no", "service_month", "platform_fee_usd", "resolutions", "price_per_resolution_usd",
               "usage_fee_usd", "total_usd", "currency", "status"], vendor_docs(sessions))
    write_csv(HERE / "legal/contract-review-log.csv",
              ["ref", "opened", "requested_by", "subject", "counterparty", "status", "last_update", "notes"], LEGAL_REVIEW)
    write_csv(HERE / "legal/regulator-and-claims-log.csv",
              ["date", "type", "subject", "amount_claimed_ils", "status", "owner"], CLAIMS)
    for path, text in {**STATIC, **DOCS_STATIC_VENDOR, **documents(k, sessions, rets)}.items():
        if text is not None:
            write_text(HERE / path, text)
    write_text(HERE / "support/bot-transcripts-sample.md", BOT_TRANSCRIPTS)

    if answer_key:
        answer_key.mkdir(parents=True, exist_ok=True)
        write_csv(answer_key / "contacts-and-sessions-truth.csv",
                  ["id", "true_intent", "issue_no", "is_repeat", "recontact_after_bot", "true_language"], truth)
        write_csv(answer_key / "customers-truth.csv", ["customer_id", "language", "age65", "immigrant", "disability"],
                  [[c["customer_id"], c["lang"], int(c["age65"]), int(c["immigrant"]), int(c["disability"])] for c in customers])
        write_csv(answer_key / "returns-truth.csv", ["return_id", "true_reason", "days_after_delivery"],
                  [[x["return_id"], x["reason"], x["after"]] for x in rets])
    stats.update(customers=len(customers), orders=len(orders), returns=len(rets), contacts=len(contacts),
                 sessions=len(sessions), tickets=len(tickets))
    return stats


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--answer-key", type=Path, help="also write the ground truth here (writers only)")
    args = ap.parse_args()
    print(build_all(args.answer_key))
