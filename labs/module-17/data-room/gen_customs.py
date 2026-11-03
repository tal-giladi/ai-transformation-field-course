"""customs/declarations-prefill-2027-05.csv, customs/qa-sample-2027-04.csv,
customs/customs-queries-2027.csv. `declarations()` is also used by gen_portal (the mismatches)."""
from datetime import date, datetime, timedelta
from functools import lru_cache

from gen_common import (CUSTOMERS, SUPPLIER_PREFIXES, DOCS_V42, DOCS_V421, rng, write_csv, days,
                        is_workday)

BRANCHES = [("HFA", "Haifa Port", 0.42), ("ASH", "Ashdod Port", 0.44), ("BGN", "Ben Gurion Airport", 0.14)]
AGENTS = {"HFA": ["CA-11", "CA-12", "CA-14", "CA-17", "CA-19"],
          "ASH": ["CA-21", "CA-22", "CA-23", "CA-26", "CA-28", "CA-29"],
          "BGN": ["CA-31", "CA-33"]}
# How often each customer imports (weights); Gefen and Shuk Online are large.
CUST_W = [9, 12] + [3] * 22


def version(t: datetime) -> str:
    if t < datetime(2027, 5, 2, 6, 0):
        return "4.1.3"
    if t < datetime(2027, 5, 21, 14, 0):
        return "4.2.0"
    return "4.2.1"


def key_for(raw: str, ver: str) -> str:
    digits = "".join(ch for ch in raw if ch.isdigit())
    if ver == "4.1.3":
        return raw.upper()
    if ver == "4.2.0":
        return digits
    return raw.upper() if any(ch.isalpha() for ch in raw) else digits


@lru_cache(maxsize=1)
def declarations() -> tuple:
    """All rows (as lists) and the mismatch records [(row index, declaring, owner, date, submitted)]."""
    r = rng(10)
    rows = []
    seq = {b[0]: 4100 for b in BRANCHES}
    for d in days(date(2027, 5, 1), date(2027, 6, 3)):
        if not is_workday(d) and d.weekday() != 4:
            continue
        n_day = 64 if d.weekday() == 4 else (238 if d.weekday() in (6, 0) else 205)
        for _ in range(round(n_day * r.uniform(0.93, 1.07))):
            b, bname, _w = r.choices(BRANCHES, [x[2] for x in BRANCHES])[0]
            seq[b] += 1
            cust = r.choices(CUSTOMERS, CUST_W)[0][0]
            stype = "AIR" if b == "BGN" else r.choices(["FCL", "LCL"], [0.55, 0.45])[0]
            t = datetime(d.year, d.month, d.day, 7, 0) + timedelta(minutes=r.randint(0, 600 if d.weekday() != 4 else 240))
            ver = version(t)
            if r.random() < 0.12:
                raw = f"{r.randint(10000, 99999)}"
            else:
                raw = f"{r.choice(SUPPLIER_PREFIXES)}-{r.randint(10000, 99999)}"
            batch = r.random() < (0.66 if d.weekday() in (6, 0) else 0.55)
            secs = r.randint(5, 21) if batch else round(r.lognormvariate(4.3, 0.55))
            edited = 0 if r.random() < 0.93 else r.randint(1, 4)
            sub = t + timedelta(minutes=r.randint(20, 300))
            hs_src = r.choices(["Tzir Docs", "Meches HS Suggest", "agent"], [0.70, 0.22, 0.08])[0]
            status = r.choices(["released", "released", "released", "accepted", "query"], [40, 30, 20, 9, 1])[0]
            rows.append([f"27{b}{seq[b]:06d}", bname, f"F-27-{r.randint(100000, 999999)}", cust, stype,
                         t.strftime("%Y-%m-%d %H:%M"), ver, raw, key_for(raw, ver), cust, hs_src,
                         r.choice(AGENTS[b]), secs, edited, sub.strftime("%Y-%m-%d %H:%M"), status, ""])
    mism = []
    # 4.2.0 window: 63 consolidated sea shipments matched to another importer's invoice.
    win = [i for i, x in enumerate(rows) if x[6] == "4.2.0" and x[4] == "LCL" and x[5] >= "2027-05-03"]
    r.shuffle(win)
    owners_cycle = ["C1022"] * 9 + ["C1007"] * 4 + [c[0] for c in CUSTOMERS[2:]]
    picked = sorted(win[:63])
    gefen_declaring = set(picked[5:13:2])  # four of Gefen's own declarations got another importer's data
    for n, i in enumerate(picked):
        row = rows[i]
        if i in gefen_declaring:
            row[3] = "C1007"
            owner = r.choice([c[0] for c in CUSTOMERS[2:]])
        else:
            owner = owners_cycle[n % len(owners_cycle)]
            if owner == row[3]:
                owner = "C1022" if row[3] != "C1022" else "C1031"
        row[9] = owner
        digits = row[8] if row[8].isdigit() else "".join(ch for ch in row[7] if ch.isdigit())
        row[7] = f"{r.choice(['SZX', 'NGB'])}-{digits}"
        row[8] = digits
        submitted = n % 3 != 2  # about two in three were approved and submitted
        if not submitted:
            row[13] = r.randint(5, 9)
            row[15] = "returned by agent"
            row[12] = r.randint(140, 420)
        mism.append([i, row[3], owner, row[5][:10], submitted])
    # 4.2.1 after the hotfix: numeric-only invoice numbers still collide (7 rows).
    post = [i for i, x in enumerate(rows) if x[6] == "4.2.1" and x[4] == "LCL" and x[7].isdigit()]
    r.shuffle(post)
    for n, i in enumerate(sorted(post[:7])):
        row = rows[i]
        owner = ["C1022", "C1044", "C1068", "C1022", "C1117", "C1007", "C1189"][n]
        if owner == row[3]:
            owner = "C1095"
        row[9] = owner
        submitted = n not in (2, 5)
        if not submitted:
            row[13] = r.randint(5, 8)
            row[15] = "returned by agent"
        mism.append([i, row[3], owner, row[5][:10], submitted])
    # customs queries on submitted mismatches (9), three of them Gefen's, goods held
    sub_m = [m for m in mism if m[4] and m[3] <= "2027-05-20"]
    queried = [m for m in sub_m if m[1] == "C1007"][:3] + [m for m in sub_m if m[1] != "C1007"][:6]
    qrows = []
    for k, m in enumerate(queried):
        row = rows[m[0]]
        row[15] = "held" if m[1] == "C1007" else "query"
        row[16] = f"CQ-27-{300 + k * 7}"
        qrows.append((row[16], row[0], row[1], m[1], m[3], m[1] == "C1007"))
    return rows, mism, qrows


def write_declarations() -> int:
    rows, _m, _q = declarations()
    header = ["decl_id", "customs_house", "file_id", "customer_code", "shipment_type", "prefill_created_at",
              "model_version", "invoice_no_raw", "invoice_key", "doc_owner_customer", "hs_code_source",
              "agent_id", "review_seconds", "fields_edited", "submitted_at", "status", "customs_query_id"]
    for row in rows:
        if row[15] == "returned by agent":
            row[14] = ""
    return write_csv("customs/declarations-prefill-2027-05.csv", header, rows)


QA_NOTES = {
    "hs": ["פרט מכס שגוי – 8504.40 במקום 8504.31", "HS 3926.90 should be 3923.21 (packaging)",
           "סיווג לפי תיאור הספק ולא לפי המוצר", "HS chapter wrong for lab glassware"],
    "value": ["ערך לפי חשבונית פרופורמה ולא סופית", "Freight not added to CIF value", "מטבע USD נקרא כ-EUR"],
    "origin": ["ארץ מקור לפי נמל טעינה ולא ייצור", "Origin taken from shipper address (HK) not CN"],
    "qty": ["כמות ביחידות במקום קרטונים", "Packing list total misread"],
    "consignee": ["שם יבואן מחשבונית של לקוח אחר?", "Consignee line missing"],
}


def qa_sample() -> int:
    r = rng(11)
    header = ["qa_id", "decl_id", "customs_house", "customer_code", "prefill_version", "fields_checked",
              "fields_accepted_without_edit", "hs_error", "value_error", "origin_error", "quantity_error",
              "consignee_error", "material_error", "qa_note", "checked_by", "checked_on"]
    rows = []
    errs = (["hs"] * 12 + ["value"] * 7 + ["origin"] * 5 + ["qty"] * 3 + ["consignee"] * 1) + [None] * 372
    r.shuffle(errs)
    for n, e in enumerate(errs):
        b = r.choices(["HFA", "ASH", "BGN"], [0.45, 0.45, 0.10])[0]
        d = date(2027, 4, 1) + timedelta(days=r.randint(0, 27))
        checked = 14
        accepted = checked if r.random() < 0.89 else checked - 1
        flags = {k: "N" for k in ("hs", "value", "origin", "qty", "consignee")}
        if e:
            flags[e] = "Y"
            if r.random() < 0.15:
                flags[r.choice(["origin", "qty"])] = "Y"
        mat = "Y" if e else "N"
        note = r.choice(QA_NOTES[e]) if e else ""
        rows.append([f"QA-{n + 1:03d}", f"27{b}{r.randint(1000, 4099):06d}", b, r.choices(CUSTOMERS, CUST_W)[0][0],
                     "4.1.3", checked, accepted, flags["hs"], flags["value"], flags["origin"], flags["qty"],
                     flags["consignee"], mat, note, r.choice(["E. Shalom", "N. Asfour", "K. Grinberg"]),
                     (d + timedelta(days=r.randint(7, 20))).isoformat()])
    return write_csv("customs/qa-sample-2027-04.csv", header, rows)


def queries() -> int:
    r = rng(12)
    _rows, _m, q = declarations()
    header = ["query_id", "received", "customs_house", "decl_id", "customer_code", "query_type", "goods_held",
              "response_requested_by", "status", "handled_by", "note"]
    rows = []
    for k in range(26):
        d = date(2027, 2, 2) + timedelta(days=r.randint(0, 115))
        if not is_workday(d):
            d += timedelta(days=2)
        qt = r.choice(["classification", "value", "origin", "documents", "classification"])
        rows.append([f"CQ-27-{100 + k * 7}", d.isoformat(), r.choice(["Haifa Port", "Ashdod Port", "Ben Gurion Airport"]),
                     f"27{r.choice(['HFA', 'ASH'])}{r.randint(1000, 4099):06d}", r.choice(CUSTOMERS[2:])[0], qt,
                     "N", (d + timedelta(days=10)).isoformat(), "closed" if d < date(2027, 5, 15) else "answered",
                     r.choice(["S. Peretz", "E. Shalom", "N. Asfour"]), ""])
    gefen_days = iter([date(2027, 5, 18), date(2027, 5, 18), date(2027, 5, 19)])
    for qid, decl, house, cust, dstr, held in q:
        d = date.fromisoformat(dstr) + timedelta(days=r.randint(2, 6))
        if held:
            d = next(gefen_days)
        note = "ערך מוצהר אינו תואם מסמכי הספק" if held else "Value and supplier do not match the importer's history"
        rows.append([qid, d.isoformat(), house, decl, cust, "value", "Y" if held else "N",
                     (d + timedelta(days=10)).isoformat(), "open", "S. Peretz", note])
    rows.sort(key=lambda x: x[1])
    return write_csv("customs/customs-queries-2027.csv", header, rows)


def staffing() -> int:
    r = rng(13)
    header = ["month", "licensed_agents_fte", "open_posts_frozen", "declarations", "declarations_per_agent_day",
              "overtime_hours", "kpi_target_per_agent_day"]
    rows = []
    y, m = 2026, 1
    while (y, m) <= (2027, 5):
        decl = round(5900 * r.uniform(0.95, 1.06)) if y == 2026 else round(6100 * r.uniform(0.96, 1.04))
        fte = 31
        frozen = 2 if (y, m) >= (2027, 1) else 0
        ot = round(420 * r.uniform(0.85, 1.15))
        if (y, m) == (2027, 5):
            ot = 702
        target = 12 if (y, m) >= (2027, 3) else 9
        rows.append([f"{y}-{m:02d}", fte, frozen, decl, round(decl / fte / 21.5, 1), ot, target])
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return write_csv("customs/brokerage-staffing-monthly.csv", header, rows)


def build() -> dict:
    return {"declarations": write_declarations(), "qa-sample": qa_sample(), "customs-queries": queries(),
            "staffing": staffing()}
