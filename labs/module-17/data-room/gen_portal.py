"""portal/assist-sessions-2027.csv, portal/document-access-log-2027-05.csv,
portal/document-index-2027-05.csv, portal/cs-contacts-weekly-2027.csv."""
from datetime import date, datetime, timedelta

from gen_common import CUSTOMERS, ASSIST_DOCS_ON, ASSIST_DOCS_OFF, rng, write_csv, days, is_workday
from gen_customs import declarations

CODES = [c[0] for c in CUSTOMERS]
INTENTS = ["shipment status", "ETA", "customs status", "invoice copy", "complaint", "rates", "other"]


def sessions() -> int:
    r = rng(20)
    header = ["session_id", "started_at", "customer_code", "user_ref", "language", "intent", "answer_source",
              "docs_shown", "handed_to_human", "csat"]
    rows = []
    n = 0
    for d in days(date(2027, 3, 15), date(2027, 6, 3)):
        if not is_workday(d):
            continue
        for _ in range(round(36 * r.uniform(0.85, 1.15))):
            n += 1
            cust = r.choice(CODES)
            lang = r.choices(["he", "en", "ru", "ar"], [0.62, 0.22, 0.09, 0.07])[0]
            docs_on = ASSIST_DOCS_ON <= d < ASSIST_DOCS_OFF
            intent = r.choices(INTENTS + ["my documents"], [30, 14, 16, 8, 6, 5, 6, 15 if docs_on else 0])[0]
            if intent == "my documents":
                src, shown = "file documents", r.randint(1, 4)
            elif intent in ("shipment status", "ETA", "customs status"):
                src, shown = "TMS status", 0
            else:
                src, shown = "general model", 0
            p = {"shipment status": 0.22, "ETA": 0.38, "customs status": 0.55, "invoice copy": 0.6,
                 "complaint": 0.92, "rates": 0.8, "other": 0.7, "my documents": 0.25}[intent]
            if lang in ("ru", "ar"):
                p = min(0.95, p + 0.15)
            human = "Y" if r.random() < p else "N"
            csat = "" if r.random() < 0.7 else r.choices([1, 2, 3, 4, 5], [18, 14, 20, 26, 22])[0]
            t = datetime(d.year, d.month, d.day, 7) + timedelta(minutes=r.randint(0, 660))
            rows.append([f"AS-{n:05d}", t.strftime("%Y-%m-%d %H:%M"), cust, f"U{r.randint(100, 999)}-{cust[-3:]}",
                         lang, intent, src, shown, human, csat])
    return write_csv("portal/assist-sessions-2027.csv", header, rows)


MANIFEST_RECORDS = [412, 388, 377, 351, 342]


def documents() -> tuple[int, int]:
    r = rng(21)
    rows_d, mism, _q = declarations()
    index = {}
    events = []
    seq = 0

    def new_doc(owner: str, dtype: str, file_id: str, records: int | str = "") -> str:
        nonlocal seq
        seq += 1
        did = f"D-27-{500000 + seq * 13}"
        pd = {"commercial invoice": "supplier and importer contact names; e-mail",
              "packing list": "", "B2C manifest": "consignee name; street address; city; phone",
              "bill of lading": "notify party contact name", "certificate of origin": ""}[dtype]
        index[did] = [did, owner, dtype, file_id, pd, records]
        return did

    # Background: customers opening their own documents, 1 May - 3 June.
    for d in days(date(2027, 5, 1), date(2027, 6, 3)):
        if not is_workday(d):
            continue
        for _ in range(round(70 * r.uniform(0.85, 1.15))):
            cust = r.choice(CODES)
            dtype = r.choice(["commercial invoice", "packing list", "bill of lading", "certificate of origin"])
            did = new_doc(cust, dtype, f"F-27-{r.randint(100000, 999999)}")
            ch = "Tzir Assist" if (d < ASSIST_DOCS_OFF and r.random() < 0.35) else "portal file page"
            t = datetime(d.year, d.month, d.day, 7) + timedelta(minutes=r.randint(0, 660))
            events.append([t, cust, f"U{r.randint(100, 999)}-{cust[-3:]}", ch, did, cust,
                           r.choice(["view", "view", "download"])])
    # Cross-customer opens of documents attached to mismatched files.
    early = [m for m in mism if m[3] < "2027-05-19"]
    late = [m for m in mism if m[3] >= "2027-05-22"]
    plan = []  # (mismatch, doc type, records)
    shuk = [m for m in early if m[2] == "C1022" and m[1] != "C1007"][:5]
    for m, rec in zip(shuk, MANIFEST_RECORDS):
        plan.append((m, "B2C manifest", rec))
    gef = [m for m in early if m[2] == "C1007"][:3]
    for m in gef:
        plan.append((m, "commercial invoice", ""))
    gefen_saw = [m for m in early if m[1] == "C1007"][:2]
    for m in gefen_saw:
        plan.append((m, "commercial invoice", ""))
    used = {id(m) for m, _t, _r in plan}
    others = [m for m in early if m[2] not in ("C1022", "C1007") and m[1] != "C1007" and id(m) not in used][:8]
    for m in others:
        plan.append((m, r.choice(["commercial invoice", "packing list"]), ""))
    for m in late[:4]:
        plan.append((m, "commercial invoice" if m[2] != "C1022" else "B2C manifest", "" if m[2] != "C1022" else 296))
    for k, (m, dtype, rec) in enumerate(plan):
        row = rows_d[m[0]]
        did = new_doc(m[2], dtype, row[2], rec)
        row_cust = m[1]
        d0 = date.fromisoformat(m[3])
        if m[1] == "C1007":
            d0 = date(2027, 5, 18)
        n_ev = 2 if k % 3 == 0 else 1
        for e in range(n_ev):
            d = d0 + timedelta(days=e + r.randint(0, 2))
            if m[3] >= "2027-05-22":
                ch = "portal file page"
            else:
                d = min(d, date(2027, 5, 18))
                ch = "Tzir Assist" if e == 0 else "portal file page"
            t = datetime(d.year, d.month, d.day, 8) + timedelta(minutes=r.randint(0, 540))
            events.append([t, row_cust, f"U{r.randint(100, 999)}-{row_cust[-3:]}", ch, did, m[2],
                           "download" if e == 1 else "view"])
    events.sort(key=lambda x: (x[0], x[4]))
    header = ["event_id", "event_time", "viewer_customer", "viewer_user", "channel", "doc_id", "action"]
    out = []
    for n, ev in enumerate(events):
        out.append([f"EV-{n + 1:06d}", ev[0].strftime("%Y-%m-%d %H:%M"), ev[1], ev[2], ev[3], ev[4], ev[6]])
    n1 = write_csv("portal/document-access-log-2027-05.csv", header, out)
    h2 = ["doc_id", "owner_customer", "doc_type", "file_id", "personal_data_fields", "records"]
    n2 = write_csv("portal/document-index-2027-05.csv", h2, sorted(index.values()))
    return n1, n2


def contacts() -> int:
    r = rng(22)
    header = ["week_start", "channel", "contacts", "handled_by_team", "avg_handle_minutes"]
    rows = []
    wk = date(2027, 1, 3)
    while wk <= date(2027, 5, 30):
        for ch, base, aht in (("phone", 1040, 6.8), ("email", 690, 9.4), ("portal form", 210, 7.9)):
            v = base * r.uniform(0.93, 1.08)
            if wk >= date(2027, 5, 16):
                v *= 1.06 if ch != "portal form" else 1.2
            rows.append([wk.isoformat(), ch, round(v), "Customer Service (PTK)", round(aht * r.uniform(0.95, 1.05), 1)])
        wk += timedelta(days=7)
    return write_csv("portal/cs-contacts-weekly-2027.csv", header, rows)


def build() -> dict:
    n1, n2 = documents()
    return {"assist-sessions": sessions(), "doc-access-log": n1, "doc-index": n2, "cs-contacts": contacts()}
