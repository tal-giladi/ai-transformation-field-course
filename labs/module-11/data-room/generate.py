"""Build the Givat Oren data room (module 11) from a fixed seed.

    python generate.py            # rebuilds every data file in this folder and the pilot's inputs, byte for byte

Python 3.12+, standard library only. Multilingual text lives in textbank.py. Besides the data room it
writes the permit-FAQ pilot's inputs in ../pilot/: the approved knowledge pack (44 documents in
Hebrew, Arabic, Russian and English), the 174-question test set with expected behaviour and facts,
the 12 negative tests, and the spreadsheet-track files.

Reading this file spoils the engagement: finish module 11 first.
"""
from __future__ import annotations

import csv
import random
from datetime import date, datetime, timedelta
from pathlib import Path

import textbank as tb

SEED = 20261129
HERE = Path(__file__).resolve().parent
PILOT = HERE.parent / "pilot"
SAMPLE = 25  # Moked 106 extract: all contacts of a random 4% of caller numbers -> multiply by 25
C_START, C_END = date(2026, 6, 1), date(2026, 10, 31)
P_START, P_END = date(2026, 1, 1), date(2026, 10, 31)
PROC_V4 = date(2026, 7, 1)
SKP_TABLE_FIX = date(2026, 3, 16)
RUTI_LIVE = date(2026, 3, 10)
DOMAIN = "https://www.givat-oren.example"


def rng(name: str) -> random.Random:
    return random.Random(f"{SEED}-{name}")


def pick(r: random.Random, weights: dict):
    keys = list(weights)
    return r.choices(keys, weights=[weights[k] for k in keys])[0]


def offset(d: date) -> str:
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


def office_time(r: random.Random, d: date) -> datetime:
    if d.weekday() == 5:  # Saturday: Moked 106 runs, but quieter; keep it simple
        hour = r.randint(9, 21)
    elif d.weekday() == 4:
        hour = r.randint(8, 13)
    else:
        hour = r.choices(range(7, 23), weights=[3, 8, 10, 10, 9, 8, 8, 7, 7, 6, 6, 5, 4, 3, 2, 1])[0]
    return datetime(d.year, d.month, d.day, hour, r.randint(0, 59), r.randint(0, 59))


def days_between(a: date, b: date) -> list[date]:
    return [a + timedelta(days=i) for i in range((b - a).days + 1)]


def write_csv(path: Path, header: list[str], rows: list[list]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")


# ---------------------------------------------------------------------------------------------
# 1. Documents: the live website's permits section, the fee tables, and the knowledge pack
# ---------------------------------------------------------------------------------------------
SITE_LAST_MODIFIED = {
    ("PRK", "he"): "2026-07-02", ("DPK", "he"): "2024-03-05", ("SGN", "he"): "2026-01-04",
    ("CAF", "he"): "2026-01-04", ("EVT", "he"): "2026-01-07", ("SKP", "he"): "2025-02-11",
    ("ARC", "he"): "2024-09-18", ("BLK", "he"): "2026-01-12", ("BIZ", "he"): "2025-06-03",
    ("EXW", "he"): "2025-06-03", ("APL", "he"): "2022-05-16",
    ("PRK", "ar"): "2023-04-20", ("DPK", "ar"): "2024-03-28", ("BLK", "ar"): "2023-04-20",
    ("EVT", "ar"): "2023-04-20", ("APL", "ar"): "2023-04-20", ("BIZ", "ar"): "2023-04-20",
    ("PRK", "ru"): "2023-05-02", ("BLK", "ru"): "2026-02-09", ("SGN", "ru"): "2023-05-02",
    ("EVT", "ru"): "2026-02-09", ("PRK", "en"): "2023-05-14", ("EVT", "en"): "2023-05-14",
    ("BIZ", "en"): "2025-06-10",
}
SLUG = {"PRK": "parking-permit", "DPK": "disabled-parking", "SGN": "signs", "CAF": "sidewalk-cafe",
        "EVT": "events", "SKP": "skips", "ARC": "building-archive", "BLK": "bulky-waste",
        "BIZ": "business-licence", "EXW": "small-works", "APL": "reasons-and-objections"}


def fee_table(version: str) -> str:
    v = tb.CURRENT if version == "current" else tb.OLD
    year = "2026" if version == "current" else "2025"
    note = ("בתוקף מ-1 בינואר 2026 לפי החלטת מועצת העיר מיום 17 בדצמבר 2025, למעט תו חניה לתושב "
            "(נוהל 4, בתוקף מ-1 ביולי 2026)." if version == "current"
            else "בתוקף מ-1 בינואר 2025 לפי החלטת מועצת העיר מיום 18 בדצמבר 2024.")
    rows = [
        ("תו חניה לתושב – רכב ראשון", "ללא תשלום"),
        ("תו חניה לתושב – רכב שני", f"{v['PRK']['fee2']} ₪ לשנה"),
        ("רישיון לשלט", f"{v['SGN']['sqm']} ₪ למ\"ר לשנה, מינימום {v['SGN']['min']} ₪"),
        ("שולחנות וכיסאות על המדרכה", f"{v['CAF']['sqm']} ₪ למ\"ר לשנה"),
        ("סגירת רחוב לאירוע", f"{v['EVT']['fee']} ₪ ליום"),
        ("מכולה ברחוב", f"{v['SKP']['week']} ₪ לשבוע"),
        ("צילום תיק בניין – עותק דיגיטלי", f"{v['ARC']['fee']} ₪ לתיק"),
        ("פינוי גזם/פסולת גושית נוסף", f"{v['BLK']['extra']} ₪"),
    ]
    lines = [f"# לוח אגרות עירוניות {year}", "", note, "", "| שירות | אגרה |", "|---|---|"]
    lines += [f"| {a} | {b} |" for a, b in rows]
    return "\n".join(lines)


def build_documents() -> list[dict]:
    """Writes content/site/ (the website as it is) and ../pilot/knowledge-pack/ (approved v1)."""
    site = []
    pid = 2100
    for (topic, lang), state in sorted(tb.SITE.items(), key=lambda kv: (tb.TOPICS.index(kv[0][0]), tb.LANGS.index(kv[0][1]))):
        pid += 7
        body = tb.doc_body(topic, lang, state)
        url = f"{DOMAIN}/{lang}/permits/{SLUG[topic]}"
        head = (f"page_id: P-{pid}\ndoc_id: {topic}-{lang}\nurl: {url}\nlanguage: {lang}\n"
                f"last_modified: {SITE_LAST_MODIFIED[(topic, lang)]}\n---\n")
        write_text(HERE / "content" / "site" / f"{topic}-{lang}.md", head + body)
        site.append({"page_id": f"P-{pid}", "doc_id": f"{topic}-{lang}", "topic": topic, "lang": lang,
                     "state": state, "url": url, "last_modified": SITE_LAST_MODIFIED[(topic, lang)]})
    for version, pid_, lm in (("old", "P-2001", "2025-01-02"), ("current", "P-2002", "2026-01-04")):
        year = "2025" if version == "old" else "2026"
        head = (f"page_id: {pid_}\ndoc_id: FEE{year}-he\nurl: {DOMAIN}/files/fee-table-{year}.pdf\n"
                f"language: he\nlast_modified: {lm}\n---\n")
        write_text(HERE / "content" / "site" / f"FEE{year}-he.md", head + fee_table(version))
        site.append({"page_id": pid_, "doc_id": f"FEE{year}-he", "topic": "FEE", "lang": "he",
                     "state": version, "url": f"{DOMAIN}/files/fee-table-{year}.pdf", "last_modified": lm})
    # The knowledge pack: every topic in four languages, current, owned and dated.
    allparts = ["# Givat Oren permits and fees: knowledge pack v1 (all documents)", "",
                "Approved by the owning departments on 14 January 2027. One section per document."]
    for topic in tb.TOPICS:
        for lang in tb.LANGS:
            head = (f"doc_id: {topic}-{lang}\ntitle: {tb.TITLES_EN[topic]}\nlanguage: {lang}\n"
                    f"owner: {tb.OWNERS[topic]}\neffective_from: {tb.EFFECTIVE[topic]}\n"
                    f"approved: 2027-01-14 (knowledge pack v1)\n---\n")
            body = tb.doc_body(topic, lang, "current")
            write_text(PILOT / "knowledge-pack" / f"{topic}-{lang}.md", head + body)
            allparts += ["", "=" * 60, head.replace("\n---\n", ""), "", body]
    write_text(PILOT / "knowledge-pack-all.md", "\n".join(allparts))
    return site


# ---------------------------------------------------------------------------------------------
# 2. CMS page inventory
# ---------------------------------------------------------------------------------------------
SECTIONS = {"about": 40, "arnona": 55, "education": 150, "welfare": 95, "culture": 120, "sport": 60,
            "sanitation": 70, "permits": 110, "business": 45, "engineering": 90, "transport": 70,
            "news": 220, "transparency": 60, "emergency": 30, "community": 25}
OWNER_DEPTS = {"about": "Spokesperson", "arnona": "Revenue Division", "education": "Education Division",
               "welfare": "Welfare Division", "culture": "Culture Division", "sport": "Culture Division",
               "sanitation": "Sanitation Division", "permits": "Licensing and Permits Division",
               "business": "Licensing and Permits Division", "engineering": "Engineering Division",
               "transport": "Engineering Division", "news": "Spokesperson",
               "transparency": "Legal Adviser's office", "emergency": "Security and Emergency",
               "community": "Community Division"}
EDITORS = {"Spokesperson": ["Noa Peretz", "Adi Levi"], "Revenue Division": ["Itzik Ohana"],
           "Education Division": ["Michal Rosen", "Hanan Darawshe"], "Welfare Division": ["Yael Cohen"],
           "Culture Division": ["Lior Ben-David"], "Sanitation Division": ["Avi Biton"],
           "Licensing and Permits Division": ["Yossi Hadad", "Tsega Mengistu"],
           "Engineering Division": ["Rami Khoury"], "Legal Adviser's office": ["Dana Shalev"],
           "Security and Emergency": ["Gadi Malka"], "Community Division": ["Rasha Abu-Ahmad"]}


def build_cms(site: list[dict]) -> None:
    r = rng("cms")
    rows = []
    n = 0
    site_by_doc = {s["doc_id"]: s for s in site}
    for section, count in SECTIONS.items():
        for i in range(count):
            n += 1
            lang = pick(r, {"he": 70, "ar": 15, "ru": 9, "en": 6})
            dept = OWNER_DEPTS[section]
            owner = r.choice(EDITORS[dept]) if r.random() < 0.62 else ""
            if lang == "he":
                lm = date(2026, 10, 31) - timedelta(days=int(r.expovariate(1 / 260)))
            else:
                lm = date(2023, 5, 31) - timedelta(days=r.randint(0, 120)) if r.random() < 0.7 else \
                    date(2026, 10, 31) - timedelta(days=int(r.expovariate(1 / 300)))
            lm = max(lm, date(2019, 3, 1))
            views = int(r.lognormvariate(4.2 if lang == "he" else 3.2, 1.1))
            rows.append([f"P-{3000 + n}", section, lang, f"{section}/{lang}/page-{i + 1:03d}",
                         f"{DOMAIN}/{lang}/{section}/page-{i + 1:03d}", lm.isoformat(), dept, owner, views,
                         "n", "", ""])
    # Replace the first permits pages with the real permits documents (they are the pages users hit)
    permits_rows = [row for row in rows if row[1] in ("permits", "business")]
    docs = sorted(site_by_doc.values(), key=lambda s: s["page_id"])
    unowned_docs = {"SKP-he", "ARC-he", "APL-he", "PRK-ar", "BLK-ar", "EVT-ar", "APL-ar", "PRK-ru",
                    "SGN-ru", "PRK-en", "EVT-en", "FEE2025-he", "BIZ-ar"}
    fee_link_2025 = {"SKP-he", "ARC-he", "PRK-ar", "BLK-ar", "PRK-ru", "PRK-en"}
    embeds = {"BIZ-he", "SGN-he", "CAF-he"}
    titles = {"he": "", "ar": "", "ru": "", "en": ""}
    for row, s in zip(permits_rows, docs):
        section = "business" if s["topic"] in ("BIZ", "SGN", "CAF") else "permits"
        row[0] = s["page_id"]
        row[1] = section
        row[2] = s["lang"]
        row[3] = (tb.TITLES_EN[s["topic"]] if s["topic"] in tb.TITLES_EN else "Fee table") + titles[s["lang"]]
        row[4] = s["url"]
        row[5] = s["last_modified"]
        row[6] = "Licensing and Permits Division" if s["topic"] not in ("ARC", "EXW", "DPK", "BLK", "APL") else \
            {"ARC": "Engineering Division", "EXW": "Engineering Division", "DPK": "Engineering Division",
             "BLK": "Sanitation Division", "APL": "Director-General's office"}[s["topic"]]
        row[7] = "" if s["doc_id"] in unowned_docs else r.choice(EDITORS.get(row[6], ["Yossi Hadad"]))
        row[8] = int(r.lognormvariate(6.4 if s["lang"] == "he" else 5.3, 0.5))
        row[9] = "y" if s["topic"] not in ("BIZ", "EXW", "APL", "DPK") else "n"
        row[10] = "fee-table-2025.pdf" if s["doc_id"] in fee_link_2025 else (
            "fee-table-2026.pdf" if s["doc_id"] in ("SGN-he", "CAF-he", "EVT-he") else "")
        row[11] = "botnest-widget" if s["doc_id"] in embeds else ""
    rows.sort(key=lambda x: x[0])
    write_csv(HERE / "content" / "cms-pages.csv",
              ["page_id", "section", "language", "title", "url", "last_modified", "owner_department",
               "owner_editor", "views_30d", "mentions_fee", "pdf_link", "script_embed"], rows)


# ---------------------------------------------------------------------------------------------
# 3. Moked 106: contacts (4% caller sample) and department callbacks
# ---------------------------------------------------------------------------------------------
TOPIC_W = {"permits_parking": 9, "permits_signage": 1.5, "permits_cafe": 0.8, "permits_events": 1.6,
           "permits_skip": 1.8, "building_archive": 1.2, "business_licence": 1.6, "bulky_waste": 9,
           "garbage": 10, "arnona": 12, "parking_fine": 8, "roads_lighting": 9, "trees": 4,
           "noise": 5, "welfare": 4, "education_registration": 5, "pest_control": 3, "other": 9}
PERMIT_FAMILY = {"permits_parking", "permits_signage", "permits_cafe", "permits_events", "permits_skip",
                 "building_archive", "business_licence", "bulky_waste"}
DEPT = {"permits_parking": "Licensing and Permits", "permits_signage": "Licensing and Permits",
        "permits_cafe": "Licensing and Permits", "permits_events": "Licensing and Permits",
        "permits_skip": "Licensing and Permits", "building_archive": "Engineering",
        "business_licence": "Licensing and Permits", "bulky_waste": "Sanitation", "garbage": "Sanitation",
        "arnona": "Revenue", "parking_fine": "Parking and Enforcement", "roads_lighting": "Engineering",
        "trees": "Engineering", "noise": "Security and Emergency", "welfare": "Welfare",
        "education_registration": "Education", "pest_control": "Sanitation", "other": "Resident Service"}
AGENTS = [  # agent_id, languages, start
    ("A01", "he,ar", "2016-03-01"), ("A02", "he", "2017-09-10"), ("A03", "he,ru", "2018-01-07"),
    ("A04", "he", "2018-06-03"), ("A05", "he,en", "2019-02-17"), ("A06", "he,ru", "2019-11-03"),
    ("A07", "he", "2020-05-10"), ("A08", "he,ar", "2020-08-02"), ("A09", "he", "2021-01-10"),
    ("A10", "he,am", "2021-03-14"), ("A11", "he", "2021-07-04"), ("A12", "he,ru", "2022-01-09"),
    ("A13", "he", "2022-04-03"), ("A14", "he,en", "2022-09-11"), ("A15", "he", "2023-01-08"),
    ("A16", "he", "2023-03-05"), ("A17", "he,ar", "2023-06-11"), ("A18", "he", "2024-01-07"),
    ("A19", "he,ru", "2024-02-04"), ("A20", "he", "2024-06-02"), ("A21", "he", "2025-01-05"),
    ("A22", "he", "2025-04-06"), ("A23", "he", "2025-09-07"), ("A24", "he", "2026-02-01"),
]


def build_moked() -> dict:
    r = rng("moked")
    contacts, callbacks = [], []
    cid, cbid = 0, 0
    days = days_between(C_START, C_END)
    n_callers = 2350
    callers = []
    for i in range(n_callers):
        lang = pick(r, {"he": 60, "ar": 19, "ru": 14, "en": 3, "am": 4})
        callers.append((f"C{r.getrandbits(40):010x}", lang))
    agents_by_lang = {l: [a for a, ls, _ in AGENTS if l in ls.split(",")] for l in ("he", "ar", "ru", "en", "am")}

    def served(lang: str) -> str:
        p = {"he": 1.0, "ar": 0.41, "ru": 0.79, "en": 0.88, "am": 0.27}[lang]
        return lang if r.random() < p else "he"

    def contact(caller, lang, topic, d, prev_outcome=None):
        nonlocal cid, cbid
        cid += 1
        channel = pick(r, {"phone": 64, "whatsapp": 18, "web_form": 10, "app": 8})
        at = office_time(r, d)
        fam = topic in PERMIT_FAMILY
        if channel == "phone":
            out_w = {"answered": 34 if fam else 40, "ticket_to_dept": 14 if fam else 25,
                     "transferred": 16 if fam else 10, "callback_scheduled": 30 if fam else 18, "abandoned": 6}
        else:
            out_w = {"answered": 36 if fam else 42, "ticket_to_dept": 18 if fam else 30,
                     "transferred": 6, "callback_scheduled": 40 if fam else 22}
        outcome = pick(r, out_w)
        sv = served(lang) if outcome != "abandoned" else ""
        agent = "" if outcome == "abandoned" else r.choice(agents_by_lang[sv] if sv and sv != "he" else agents_by_lang["he"])
        wait = int(r.lognormvariate(4.3, 0.7)) if channel == "phone" else ""
        if channel == "phone" and lang == "ar" and sv == "he":
            wait = max(wait, 90 + int(r.expovariate(1 / 40)))
        handle = "" if outcome == "abandoned" else int(r.lognormvariate(5.3, 0.45))
        fcr = 0 if outcome == "abandoned" else (1 if r.random() < 0.862 else 0)
        cb_id, cb_state = "", None
        if outcome == "callback_scheduled":
            cbid += 1
            cb_id = f"CB-{cbid:05d}"
            promised = add_workdays(d, 2)
            state = pick(r, {"on_time": 41 if fam else 52, "late": 22 if fam else 20, "never": 37 if fam else 28})
            done = ""
            if state == "on_time":
                dd = d + timedelta(days=r.randint(0, (promised - d).days))
                done = ts(office_time(r, dd))
            elif state == "late":
                dd = add_workdays(promised, r.randint(1, 6))
                done = ts(office_time(r, dd))
            res = "" if state == "never" else pick(r, {"resident_answered": 70, "no_answer": 22, "left_message": 8})
            callbacks.append([cb_id, f"K{cid:06d}", DEPT[topic], promised.isoformat(), done, res])
            cb_state = state
        contacts.append([f"K{cid:06d}", caller, ts(at), channel, lang, sv, topic, outcome, wait, handle,
                         agent, fcr, cb_id])
        return outcome, cb_state, at

    for caller, lang in callers:
        n_issues = 1 + (r.random() < 0.28) + (r.random() < 0.07)
        for _ in range(n_issues):
            topic = pick(r, TOPIC_W)
            d = r.choice(days)
            outcome, cb_state, _ = contact(caller, lang, topic, d)
            fam = topic in PERMIT_FAMILY
            wrong_info = fam and outcome == "answered" and r.random() < (0.48 if lang in ("ar", "ru", "en") else 0.32)
            guard = 0
            while guard < 4:
                guard += 1
                if outcome == "abandoned":
                    p, gap = 0.55, (0, 2)
                elif outcome == "callback_scheduled":
                    p, gap = ({"on_time": 0.15, "late": 0.48, "never": 0.80} if fam else
                              {"on_time": 0.06, "late": 0.25, "never": 0.45})[cb_state], (3, 12)
                elif outcome == "transferred":
                    p, gap = (0.50 if fam else 0.22), (1, 10)
                elif outcome == "ticket_to_dept":
                    p, gap = (0.26 if fam else 0.10), (2, 13)
                else:
                    p, gap = (0.60 if wrong_info else (0.07 if fam else 0.04)), (1, 13)
                    wrong_info = False
                if r.random() >= p:
                    break
                d = d + timedelta(days=r.randint(*gap))
                if d > C_END:
                    break
                outcome, cb_state, _ = contact(caller, lang, topic, d)
    contacts.sort(key=lambda c: (c[2], c[0]))
    write_csv(HERE / "service" / "moked-contacts.csv",
              ["contact_id", "caller_id", "opened_at", "channel", "contact_language", "served_language",
               "topic", "outcome", "queue_wait_sec", "handle_sec", "agent_id", "fcr_flag", "callback_id"],
              contacts)
    callbacks.sort(key=lambda c: c[0])
    write_csv(HERE / "service" / "callbacks.csv",
              ["callback_id", "contact_id", "department", "promised_by_date", "completed_at", "result"], callbacks)
    # staffing
    rows = []
    for a, ls, start in AGENTS:
        rows.append([a, start, ls, pick(r, {"full_time": 80, "part_time_75": 20}), "active"])
    rows += [["A90", "2015-05-03", "he,ar", "full_time", "left 2026-03-31"],
             ["A91", "2019-10-06", "he,ru", "full_time", "left 2026-06-30"]]
    write_csv(HERE / "service" / "moked-staffing-2026.csv",
              ["agent_id", "start_date", "languages", "contract", "status"], rows)
    return {"contacts": contacts, "callbacks": callbacks}


def moked_kpi_report(m: dict) -> str:
    q3 = [c for c in m["contacts"] if "2026-07-01" <= c[2][:10] <= "2026-09-30"]
    total = len(q3) * SAMPLE
    fcr = sum(c[11] for c in q3) / len(q3)
    phone = [c for c in q3 if c[3] == "phone"]
    aband = sum(1 for c in phone if c[7] == "abandoned") / len(phone)
    within60 = sum(1 for c in phone if c[7] != "abandoned" and c[8] <= 60) / max(1, sum(1 for c in phone if c[7] != "abandoned"))
    cbs = {cb[1]: cb for cb in m["callbacks"]}
    sched = [c for c in q3 if c[7] == "callback_scheduled"]
    handled = [c for c in q3 if c[9] != ""]
    aht = sum(c[9] for c in handled) / len(handled) / 60
    return f"""# Moked 106 — quarterly service report, Q3 2026

Resident Service Division. Prepared by the Moked 106 team leader for the director-general's
management forum, 12 October 2026. Source: Tikshoret CRM.

| Indicator | Q3 2026 | Target |
|---|---|---|
| Contacts handled (all channels) | {total:,} | — |
| First-contact resolution (FCR)¹ | {100 * fcr:.0f}% | 80% |
| Phone calls answered within 60 seconds | {100 * within60:.0f}% | 75% |
| Abandoned phone calls² | {100 * aband:.1f}% | < 8% |
| Average handling time | {aht:.1f} min | — |
| Callbacks scheduled within SLA³ | 96% | 95% |
| Resident satisfaction (post-call SMS, 1–5) | 4.1 | 4.0 |

Contacts by channel: phone {100 * len(phone) / len(q3):.0f}%, WhatsApp, web form and app the rest.
Top topics: arnona, garbage, roads and lighting, parking permits, bulky waste.

**Highlights.** FCR above target for the third quarter running. Callback SLA met. Arabic-language
service maintained through the IVR Arabic option.

**Footnotes.**
1. FCR: the share of contacts closed at the first contact, including contacts transferred to a
   department, contacts converted to a department ticket, and contacts where a callback was
   scheduled. Abandoned calls are counted as not resolved.
2. Calls abandoned after 10 seconds in the queue.
3. A callback is within SLA when it is *scheduled* in the CRM with a promised date no later than
   two working days after the contact. Completion is recorded by the department in the callback
   module.

Not reported: repeat contacts by the same resident; callback completion; service language.
"""


# ---------------------------------------------------------------------------------------------
# 4. Permit applications (Rishuyit, full extract Jan-Oct 2026)
# ---------------------------------------------------------------------------------------------
REASONS = [
    ("R-01", "Missing document", "חסר מסמך"),
    ("R-02", "Applicant is not a Givat Oren resident", "המבקש/ת אינו/ה תושב/ת העיר"),
    ("R-03", "Vehicle not registered to the applicant", "הרכב אינו רשום על שם המבקש/ת"),
    ("R-04", "Outside the permit zone", "מחוץ לאזור ההיתר"),
    ("R-05", "Incomplete form", "טופס לא מלא"),
    ("R-06", "Safety objection", "התנגדות בטיחותית"),
    ("R-07", "Does not meet the criteria (section 3 of the procedure)", "אינו עומד בתנאים (סעיף 3 לנוהל)"),
    ("R-08", "Submitted late", "הוגש באיחור"),
]
NEIGHBOURHOODS = {"Neve Oren": 16, "HaRakafot": 14, "Givat HaZeitim": 12, "al-Zahra": 12, "Ein Sara": 9,
                  "Kiryat HaMada": 10, "Old Town": 8, "HaPardes": 11, "Ramat Oren": 8}
NB_LANG = {"al-Zahra": {"ar": 88, "he": 12}, "Ein Sara": {"ar": 70, "he": 26, "en": 4},
           "Kiryat HaMada": {"he": 55, "ru": 35, "am": 6, "en": 4},
           "HaPardes": {"he": 60, "ru": 18, "am": 18, "en": 4}}


def build_permits() -> list[list]:
    r = rng("permits")
    volumes = {"PRK": 1180, "SGN": 160, "CAF": 70, "EVT": 210, "SKP": 380, "ARC": 240, "DPK": 60}
    days = [d for d in days_between(P_START, P_END) if is_workday(d)]
    rows = []
    for typ, n in volumes.items():
        for i in range(n):
            d = r.choice(days)
            if typ == "PRK" and r.random() < 0.25:  # renewal season adds new applications in Feb-Mar
                d = r.choice([x for x in days if date(2026, 2, 1) <= x <= date(2026, 3, 31)])
            nb = pick(r, NEIGHBOURHOODS)
            lang = pick(r, NB_LANG.get(nb, {"he": 72, "ru": 14, "ar": 6, "en": 4, "am": 4}))
            channel = pick(r, {"online": 64, "service_centre": 28, "email": 8})
            own, letter = "", ""
            decision, code, fee = "approved", "", 0
            lead = ""
            if typ == "PRK":
                own = pick(r, {"private": 77, "leased": 15, "company": 8})
                second = r.random() < 0.31
                if own != "private":
                    letter = "y" if (d >= PROC_V4 and r.random() < 0.88) or (d < PROC_V4 and r.random() < 0.2) else "n"
                if own == "private":
                    decision = pick(r, {"approved": 86, "rejected": 11, "withdrawn": 3})
                    if decision == "rejected":
                        code = pick(r, {"R-01": 28, "R-02": 18, "R-05": 14, "R-07": 40})
                elif d < PROC_V4:
                    decision = pick(r, {"approved": 6, "rejected": 90, "withdrawn": 4})
                    if decision == "rejected":
                        code = pick(r, {"R-03": 45, "R-07": 55})
                else:
                    if letter == "y":
                        decision = pick(r, {"approved": 41, "rejected": 56, "withdrawn": 3})
                    else:
                        decision = pick(r, {"approved": 5, "rejected": 92, "withdrawn": 3})
                    if decision == "rejected":
                        code = pick(r, {"R-07": 78, "R-03": 17, "R-01": 5})
                fee = (120 if second else 0) if decision == "approved" else 0
            elif typ == "EVT":
                lead = int(r.choice([21, 22, 24, 25, 28, 30, 30, 35, 40, 45, 60]))
                if r.random() < 0.12:  # anyone can be late
                    lead = r.choice([5, 7, 10, 12, 18, 20])
                if lang in ("ar", "en") and r.random() < 0.55:  # the Arabic and English pages still say 14 days
                    lead = r.choice([14, 14, 15, 16])
                if lead < 21:
                    decision = pick(r, {"rejected": 80, "approved": 20})
                    code = "R-08" if decision == "rejected" else ""
                else:
                    decision = pick(r, {"approved": 90, "rejected": 7, "withdrawn": 3})
                    code = "R-06" if decision == "rejected" else ""
                closure = r.random() < 0.55
                fee = 350 if decision == "approved" and closure else 0
            elif typ == "SKP":
                decision = pick(r, {"approved": 93, "rejected": 5, "withdrawn": 2})
                code = pick(r, {"R-05": 50, "R-06": 50}) if decision == "rejected" else ""
                weeks = r.choice([1, 1, 2, 2, 3, 4])
                fee = (60 if d < SKP_TABLE_FIX else 75) * weeks if decision == "approved" else 0
            elif typ == "SGN":
                decision = pick(r, {"approved": 82, "rejected": 14, "withdrawn": 4})
                code = pick(r, {"R-01": 40, "R-07": 45, "R-06": 15}) if decision == "rejected" else ""
                sqm = r.choice([0.5, 1, 1.5, 2, 2, 3, 4, 6])
                fee = max(350, round(280 * sqm)) if decision == "approved" else 0
            elif typ == "CAF":
                decision = pick(r, {"approved": 78, "rejected": 18, "withdrawn": 4})
                code = pick(r, {"R-06": 50, "R-07": 35, "R-01": 15}) if decision == "rejected" else ""
                fee = 190 * r.choice([6, 8, 10, 12, 15, 20]) if decision == "approved" else 0
            elif typ == "ARC":
                decision = pick(r, {"approved": 92, "rejected": 8})
                code = "R-07" if decision == "rejected" else ""
                fee = 40 if decision == "approved" else 0
            elif typ == "DPK":
                decision = pick(r, {"approved": 70, "rejected": 26, "withdrawn": 4})
                code = pick(r, {"R-01": 50, "R-04": 20, "R-07": 30}) if decision == "rejected" else ""
            if d > date(2026, 10, 20) and r.random() < 0.6:
                decision, code, fee = "pending", "", 0
            dec_date = ""
            if decision in ("approved", "rejected"):
                dec_date = add_workdays(d, max(1, int(r.lognormvariate(2.3, 0.6)))).isoformat()
            if decision == "rejected":
                linked = int(r.choice([1, 2, 2, 3, 3, 4]) if code == "R-07" else r.choice([0, 1, 1, 2]))
            else:
                linked = int(r.random() < 0.15)
            objection = "y" if decision == "rejected" and r.random() < (0.07 if code == "R-07" else 0.03) else "n"
            rows.append([typ, d, channel, lang, nb, own, letter, lead, decision, dec_date, code, "he", fee,
                         objection, linked])
    rows.sort(key=lambda x: (x[1], x[0]))
    out = []
    counters: dict = {}
    for row in rows:
        counters[row[0]] = counters.get(row[0], 0) + 1
        out.append([f"2026-{row[0]}-{counters[row[0]]:04d}", row[0], row[1].isoformat()] + row[2:])
    write_csv(HERE / "permits" / "applications-2026.csv",
              ["application_id", "type", "submitted_date", "channel", "applicant_language", "neighbourhood",
               "vehicle_ownership", "employer_letter_attached", "days_before_event", "decision",
               "decision_date", "reason_code", "letter_language", "fee_charged_ils", "objection_filed",
               "linked_106_contacts"], out)
    write_csv(HERE / "permits" / "reason-codes.csv", ["reason_code", "text_en", "text_he"],
              [list(x) for x in REASONS])
    return out


# ---------------------------------------------------------------------------------------------
# 5. Test set (pilot) and the mystery-shopper audit (service/), which uses the same questions
# ---------------------------------------------------------------------------------------------
def build_test_set() -> list[dict]:
    r = rng("testset")
    items = []
    for intent, beh, topic, gold, stale, phr in tb.INTENTS:
        en_gloss = phr["en"][0]
        for lang in tb.LANGS:
            for k, q in enumerate(phr[lang]):
                items.append({"intent": intent, "language": lang, "question": q,
                              "question_en": en_gloss if lang != "en" else "", "expected_behaviour": beh,
                              "gold_topic": topic, "gold_doc": f"{topic}-{lang}" if beh == "answer" else "",
                              "gold_facts": "|".join(gold), "stale_facts": "|".join(stale),
                              "changed_2026": "y" if stale else "n"})
    for intent, q, gloss in tb.AMHARIC:
        base = next(x for x in tb.INTENTS if x[0] == intent)
        items.append({"intent": intent, "language": "am", "question": q, "question_en": gloss,
                      "expected_behaviour": "route", "gold_topic": base[2], "gold_doc": "",
                      "gold_facts": "", "stale_facts": "|".join(base[4]), "changed_2026": "y" if base[4] else "n"})
    r.shuffle(items)
    for i, it in enumerate(items, start=1):
        it["question_id"] = f"Q{i:03d}"
    # split: 40 development questions, the rest frozen test; stratified by language
    by_lang: dict = {}
    for it in items:
        by_lang.setdefault(it["language"], []).append(it)
    dev_n = {"he": 11, "ar": 11, "ru": 10, "en": 6, "am": 2}
    for lang, lst in by_lang.items():
        for j, it in enumerate(lst):
            it["split"] = "dev" if j < dev_n[lang] else "test"
    cols = ["question_id", "split", "language", "question", "question_en", "intent", "expected_behaviour",
            "gold_topic", "gold_doc", "gold_facts", "stale_facts", "changed_2026"]
    write_csv(PILOT / "test-set.csv", cols, [[it[c] for c in cols] for it in items])
    # negative tests
    neg = []
    for nid, lang, q, gloss, beh, topic, gold, must_not, why in tb.NEGATIVE:
        neg.append([nid, lang, q, gloss, beh, topic, "|".join(gold), "|".join(must_not), why])
    write_csv(PILOT / "negative-tests.csv",
              ["test_id", "language", "question", "question_en", "expected_behaviour", "gold_topic",
               "gold_facts", "must_not_contain", "what_it_tests"], neg)
    # Track A: 80 test questions (he 24, ar 20, ru 20, en 16), 4 batches of 20
    quota = {"he": 24, "ar": 20, "ru": 20, "en": 16}
    track = []
    for lang, n in quota.items():
        pool = [it for it in items if it["language"] == lang and it["split"] == "test"]
        pool.sort(key=lambda it: it["question_id"])
        rr = rng(f"tracka-{lang}")
        track += rr.sample(pool, n)
    track.sort(key=lambda it: it["question_id"])
    write_csv(PILOT / "track-a-80.csv", ["question_id", "language", "question", "question_en"],
              [[it["question_id"], it["language"], it["question"], it["question_en"]] for it in track])
    write_csv(PILOT / "scoring-sheet-80.csv",
              ["question_id", "language", "expected_behaviour", "gold_doc", "gold_facts", "stale_facts",
               "your_behaviour", "your_answer", "your_sources", "behaviour_ok", "facts_ok", "stale_present",
               "source_ok", "language_ok", "rating", "notes"],
              [[it["question_id"], it["language"], it["expected_behaviour"], it["gold_doc"], it["gold_facts"],
                it["stale_facts"]] + [""] * 10 for it in track])
    for b in range(4):
        part = track[b * 20:(b + 1) * 20]
        lines = [f"# Track A batch {b + 1} of 4 (questions {part[0]['question_id']}–{part[-1]['question_id']})", "",
                 "Paste everything below the line into a NEW conversation with your assistant. "
                 "Ask for one JSON object per question, in order.", "", "---", "",
                 "Answer each resident question below, following your instructions. Return one JSON object per "
                 "question, in order, with the keys question_id, behaviour, answer, sources, language.", ""]
        for it in part:
            lines += [f"{it['question_id']} ({it['language']}): {it['question']}"]
        write_text(PILOT / "batches" / f"batch-{b + 1:02d}.md", "\n".join(lines))
    return items


MS_TEXT = {  # intent: (correct, outdated) answer summaries as the quality unit wrote them (English)
    "PRK-fee2": ("Second-car permit ₪120 a year", "Second-car permit ₪90 a year"),
    "PRK-lease": ("Leased car eligible with employer letter", "Leased cars are not eligible"),
    "PRK-time": ("Up to 10 working days", "About three weeks (21 working days)"),
    "PRK-first": ("First car free", ""),
    "DPK-docs": ("Disabled badge, vehicle licence, ID, street photo", ""),
    "DPK-time": ("Answer within 45 days", ""),
    "SGN-fee": ("₪280 per sqm a year", "₪245 per sqm a year"),
    "SGN-min": ("Minimum ₪350", "Minimum ₪300"),
    "CAF-fee": ("₪190 per sqm a year", "₪160 per sqm a year"),
    "CAF-walk": ("1.5 m clear walkway", ""),
    "EVT-lead": ("Apply at least 21 days before", "Apply at least 14 days before"),
    "EVT-fee": ("₪350 per day of closure", ""),
    "SKP-fee": ("₪75 per week", "₪60 per week"),
    "SKP-max": ("Up to 4 weeks", ""),
    "ARC-fee": ("₪40 per file, digital", "₪60 per file"),
    "ARC-who": ("Owner or with owner's consent / power of attorney", ""),
    "BLK-free": ("2 free pickups a month", ""),
    "BLK-extra": ("Extra pickup ₪150", "Extra pickup ₪120"),
    "BIZ-start": ("Book a preliminary consultation at Licensing", ""),
    "APL-days": ("Objection within 30 days to head of division", ""),
    "APL-unclear": ("Ask for written explanation; objection route", ""),
}
WRONG_OTHER = {"PRK-first": "Said every permit costs ₪120", "DPK-docs": "Listed ID and vehicle licence only",
               "DPK-time": "Said 'a few weeks', no figure", "CAF-walk": "Said 1 metre",
               "EVT-fee": "Said closures are free", "SKP-max": "Said 2 weeks",
               "ARC-who": "Said only owners, no consent route", "BLK-free": "Said 1 free pickup",
               "BIZ-start": "Said to file the application form online first",
               "APL-days": "Said there is no objection route", "APL-unclear": "Said the decision is final"}


def build_mystery_shopper(items: list[dict]) -> None:
    r = rng("mystery")
    quota = {"he": 45, "ar": 30, "ru": 25, "en": 10, "am": 10}
    chosen = []
    for lang, n in quota.items():
        pool = sorted([it for it in items if it["language"] == lang and it["expected_behaviour"] != "clarify"],
                      key=lambda it: it["question_id"])
        chosen += [r.choice(pool) for _ in range(n)] if len(pool) < n else r.sample(pool, n)
    days = [d for d in days_between(date(2026, 8, 2), date(2026, 9, 24)) if is_workday(d)]
    rows = []
    for k, it in enumerate(sorted(chosen, key=lambda x: x["question_id"]), start=1):
        lang = it["language"]
        served = lang if r.random() < {"he": 1, "ar": 0.43, "ru": 0.8, "en": 0.9, "am": 0.2}[lang] else "he"
        intent = it["intent"]
        if it["expected_behaviour"] == "route":
            res = pick(r, {"correct": 58, "wrong_other": 27, "transferred": 15})
            summary = {"correct": "Referred to the right department / explained it cannot decide",
                       "wrong_other": "Gave a definite answer the agent could not know",
                       "transferred": "Transferred; no answer within the call"}[res]
        else:
            good, old = MS_TEXT[intent]
            if it["changed_2026"] == "y":
                res = pick(r, {"correct": 38, "wrong_outdated": 47, "partly": 5, "transferred": 10})
            else:
                res = pick(r, {"correct": 78, "partly": 10, "wrong_other": 4, "transferred": 8})
            if lang == "am" and served == "he":
                res = "no_answer" if r.random() < 0.5 else res
            summary = {"correct": good, "wrong_outdated": old, "partly": good + " (incomplete)",
                       "wrong_other": WRONG_OTHER.get(intent, "Answer did not match the published rule"),
                       "transferred": "Transferred to the department; callback promised",
                       "no_answer": "Caller could not be understood; call ended"}[res]
        d = r.choice(days)
        rows.append([f"MS-{k:03d}", d.isoformat(), it["question_id"], lang, served, summary, res,
                     int(r.lognormvariate(4.4, 0.6)) + (90 if lang == "ar" and served == "he" else 0)])
    write_csv(HERE / "service" / "mystery-shopper-2026.csv",
              ["call_id", "call_date", "question_id", "language_asked", "served_language", "answer_summary",
               "result_code", "wait_sec"], rows)


# ---------------------------------------------------------------------------------------------
# 6. Ruti: the business-licensing clerk's free chatbot (shadow AI)
# ---------------------------------------------------------------------------------------------
RUTI_Q = ["SGN-fee", "SGN-min", "CAF-fee", "CAF-walk", "BIZ-start", "EVT-lead", "SKP-fee", "PRK-lease",
          "PRK-fee2", "R-bizfee", "R-waive", "APL-days"]
RUTI_W = [14, 6, 10, 4, 18, 8, 6, 7, 5, 9, 4, 3]
RUTI_A = {  # Ruti always answers in Hebrew, from the 2025 fee table and the 2024 business guide
    "SGN-fee": "שלום! האגרה לשלט היא 245 ₪ למ\"ר לשנה. אשמח לעזור בעוד משהו 😊",
    "SGN-min": "האגרה המינימלית לשלט היא 300 ₪.",
    "CAF-fee": "האגרה לשולחנות וכיסאות היא 160 ₪ למ\"ר לשנה, משולמת מראש.",
    "CAF-walk": "יש להשאיר מעבר להולכי רגל ברוחב 1.5 מטר לפחות.",
    "BIZ-start": "כדי להתחיל, יש למלא טופס בקשה לרישיון עסק ולצרף תוכנית עסק. מומלץ לקבוע פגישת ייעוץ באגף.",
    "EVT-lead": "יש להגיש בקשה לסגירת רחוב לפחות 14 יום לפני האירוע.",
    "SKP-fee": "היתר למכולה עולה 60 ₪ לשבוע.",
    "PRK-lease": "רכב ליסינג או רכב חברה אינו זכאי לתו חניה לתושב.",
    "PRK-fee2": "תו לרכב שני עולה 90 ₪ לשנה.",
    "R-bizfee": "האגרה למסעדה היא בערך 1,200 ₪ לשנה, תלוי בשטח.",
    "R-waive": "ניתן לבקש פטור מאגרה בטופס בקשה לוועדת הנחות.",
    "APL-days": "ניתן להגיש ערר תוך 30 יום.",
}


def build_ruti() -> None:
    r = rng("ruti")
    rows = []
    days = days_between(RUTI_LIVE, date(2026, 10, 31))
    pages = {"SGN": "/he/business/signs", "CAF": "/he/business/sidewalk-cafe", "BIZ": "/he/business/business-licence"}
    for k in range(1, 641):
        intent = r.choices(RUTI_Q, weights=RUTI_W)[0]
        base = next(x for x in tb.INTENTS if x[0] == intent)
        lang = pick(r, {"he": 71, "ar": 16, "ru": 9, "en": 4})
        q = r.choice(base[5][lang])
        if r.random() < 0.09:
            idn = f"{r.randint(0, 3)}{r.randint(10000000, 99999999)}"
            q = q + {"he": f" ת.ז. {idn}", "ar": f" رقم الهوية {idn}", "ru": f" т.з. {idn}", "en": f" ID {idn}"}[lang]
        elif r.random() < 0.05:
            q = q + f" 05{r.randint(0, 9)}-{r.randint(1000000, 9999999)}"
        topic = base[2] if base[2] in pages else "BIZ"
        d = r.choice(days)
        at = datetime(d.year, d.month, d.day, r.randint(7, 23), r.randint(0, 59), r.randint(0, 59))
        reply = RUTI_A[intent]
        thumbs = pick(r, {"": 82, "up": 7, "down": 11})
        rows.append([f"RT-{k:04d}", ts(at), pages[topic], lang, q, reply, r.randint(1, 4), thumbs])
    rows.sort(key=lambda x: x[1])
    write_csv(HERE / "chatbot" / "ruti-bot-log.csv",
              ["session_id", "started_at", "page", "detected_language", "user_message", "bot_reply", "turns",
               "feedback"], rows)


# ---------------------------------------------------------------------------------------------
# 7. Freedom of Information log 2026
# ---------------------------------------------------------------------------------------------
FOI_TOPICS = [
    ("Arnona collection: number of enforcement files 2025", "journalist"),
    ("Contracts with the parking enforcement vendor", "company"),
    ("Moked 106 call volumes and waiting times", "resident"),
    ("Budget of the culture division 2026", "resident"),
    ("Tree-felling permits in Givat HaZeitim", "ngo"),
    ("Council members' expense reports", "journalist"),
    ("Sidewalk café permits issued in the Old Town", "company"),
    ("Accessibility audit of municipal buildings", "ngo"),
    ("Signs in Arabic in al-Zahra: work orders", "ngo"),
    ("Welfare department staffing", "journalist"),
    ("Event permits refused in 2025", "resident"),
    ("Consultancy contracts above ₪100,000", "journalist"),
]


def build_foi() -> None:
    r = rng("foi")
    rows = []
    days = [d for d in days_between(date(2026, 1, 4), date(2026, 10, 29)) if is_workday(d)]
    for k in range(1, 47):
        if k == 31:
            rows.append(["FOI-2026-031", "2026-08-03", "journalist",
                         "List of artificial-intelligence or algorithmic systems used by the municipality, "
                         "including chatbots, and the purposes for which they are used",
                         "2026-09-14", 42, "answered_full", "Answer: none in use (IT confirmation 10 Sep)"])
            continue
        t, who = r.choice(FOI_TOPICS)
        d = r.choice(days)
        dur = int(min(95, max(6, r.lognormvariate(3.4, 0.45))))
        ans = d + timedelta(days=dur)
        status = pick(r, {"answered_full": 48, "answered_partial": 30, "refused": 10, "pending": 12})
        if ans > date(2026, 10, 31):
            status, ans, dur = "pending", None, ""
        rows.append([f"FOI-2026-{k:03d}", d.isoformat(), who, t, ans.isoformat() if ans else "", dur, status,
                     "" if status != "refused" else pick(r, {"s.9(b)(4) internal deliberations": 1,
                                                             "s.8(1) unreasonable resources": 1,
                                                             "s.9(a)(3) privacy": 1})])
    rows.sort(key=lambda x: x[0])
    write_csv(HERE / "governance" / "foi-log-2026.csv",
              ["request_id", "received_date", "requester_type", "subject", "answered_date", "days_to_answer",
               "status", "notes"], rows)


# ---------------------------------------------------------------------------------------------
# 8. Markdown documents
# ---------------------------------------------------------------------------------------------
DOCS = {
"city/city-profile.md": """# Givat Oren municipality — profile

From the municipality's 2026 "Givat Oren in numbers" booklet and the HR summary. Fictional.

| Item | Value |
|---|---|
| Residents (end of 2025) | 221,400 |
| Households | 74,800 |
| Home languages (residents' survey, 2024, n = 2,180) | Hebrew 58%, Arabic 21%, Russian 13%, Amharic 4%, English 2%, other 2% |
| Neighbourhoods | Neve Oren, HaRakafot, Givat HaZeitim, al-Zahra, Ein Sara, Kiryat HaMada, Old Town, HaPardes, Ramat Oren |
| Municipal employees (without teachers) | 2,450 |
| Regular budget 2026 | ₪2.1bn |
| Council | 31 members; next municipal elections in 2028 |
| Website | www.givat-oren.example: Hebrew site plus Arabic, Russian and English sections |
| Hotline | Moked 106: phone (Hebrew, Arabic, Russian, English, Amharic menu), WhatsApp, web form, app |

**Service channels and systems.** Tikshoret (CRM for Moked 106 and department tasks), Rishuyit
(permits and licensing), SiteBuilder 8 (website CMS, editors in each division), Microsoft 365 for staff
email and documents.

**Mixed city.** Arabic-speaking residents live mainly in al-Zahra and Ein Sara; signage in public
spaces has been trilingual (Hebrew, Arabic, English) since 2012.
""",
"city/org-chart.md": """# Organization chart (extract), November 2026

- **Mayor** — Avraham Tal. **Chief of staff:** Eyal Ben-Haim (mayor's office, 6 staff).
- **Director-General** — Dr. Ronit Shemesh. Chairs the management forum (heads of division, fortnightly).
  - **Legal Adviser** — Adv. Samer Haddad (office of 5; also the FOI officer's line manager; the FOI
    officer is Dana Shalev).
  - **Treasurer** — Yaakov Mizrahi (procurement unit, tender committee secretariat).
  - **Comptroller and Public Complaints Commissioner** — Adv. Hagit Arbel (reports to the council).
  - **Resident Service Division** — head: Orna Ziv. **Moked 106** (head: Larisa Gurevich; 24 agents,
    2 team leaders) and the Resident Service Centre (8 clerks).
  - **Licensing and Permits Division** — head: Eli Saban. Desks: parking permits (5 clerks, senior
    clerk Tsega Mengistu), signage and public space (3), events (2), business licensing (6, incl. Yossi
    Hadad).
  - **Engineering Division** — city engineer Rami Khoury (traffic, building licensing desk, archive).
  - **Sanitation Division**, **Revenue Division** (arnona), **Parking and Enforcement**, **Welfare**,
    **Education**, **Culture**, **Community**, **Security and Emergency**.
  - **Information Systems Division** — CIO Dmitri Kogan (32 staff). Units: infrastructure, applications,
    information security (CISO Moran Elkayam), **Digital Services** (head: you; content editors Lia
    Friedman and Omar Jaber, UX designer Natalie Weiss, data analyst at 50%: Boris Segal).
- **Works committee** (ועד העובדים) — chair Moshe Azulay; represents municipal employees under the
  collective agreements for local-authority employees.
""",
"city/mayor-office-email-2026-11-26.md": """# Email: "Citizen chatbot"

**From:** Eyal Ben-Haim, chief of staff to the mayor
**To:** Head of Digital Services
**Cc:** Dmitri Kogan (CIO)
**Date:** Thursday 26 November 2026, 21:48

Hi,

The mayor wants a citizen chatbot like other cities have. Residents are fed up with waiting on 106,
we all saw the WhatsApp storm in al-Zahra last week and the piece on the local site. He wants to
launch it at the residents' conference on 4 February: "Givat Oren answers you, 24/7, in your
language".

You're our digital person, so it's yours. I spoke to a company in October (CivicTalk) that already
works with lots of authorities and they can do a free pilot, so money shouldn't be a problem for the
launch. There's also a line for it in the 2027 budget.

Can you send me a plan by Sunday? Keep it simple, the mayor doesn't need the details.

Thanks,
Eyal
""",
"city/budget-2027-draft-extract.md": """# Draft regular budget 2027 — extract (Information Systems and mayor's office lines)

Treasurer's draft for the council's finance committee, 15 November 2026. Council vote scheduled for
Tuesday 22 December 2026. Fictional.

| Line | Description | 2026 approved (₪) | 2027 draft (₪) | Note |
|---|---|---|---|---|
| 1611-750 | Website hosting and CMS licence | 186,000 | 192,000 | Digital Services |
| 1611-751 | Translation services (website Arabic, Russian, English) | 64,000 | 64,000 | Contract renewed 2023; covers updates on request |
| 1611-752 | Accessibility audit and fixes | 90,000 | 90,000 | Last full audit 2023 |
| 1611-753 | Forms and app content | 80,000 | 74,000 | |
| 1611-780 | **Smart municipal chatbot** | — | **600,000** | Added at the mayor's office's request, 12 Nov 2026 |
| 1612-410 | Moked 106 salaries (24 agents, 2 team leaders) | 6,240,000 | 6,410,000 | Collective agreement increments |
| 1612-420 | Moked 106 overtime | 380,000 | 380,000 | |

Digital Services' operating lines (1611-750 to 753) total ₪420,000 in 2027. Any new commitment needs
a requisition approved by the treasurer and, above the regulatory thresholds, a tender or a recorded
exemption (see `../procurement/procurement-procedure-extract.md`).
""",
"city/council-decision-fees-2025-12.md": """# Council decision 2025/118 — municipal fees 2026 (extract)

Givat Oren city council, meeting of 17 December 2025. Approved 19 for, 6 against, 2 abstaining.
Fictional.

The council approves the following fees from 1 January 2026, and instructs the Licensing and Permits
Division to update procedure PRK (resident parking permits) by 1 July 2026 so that leased and company
cars used regularly by a resident are eligible on presentation of a letter from the employer or the
leasing company.

| Service | 2025 | From 1 January 2026 |
|---|---|---|
| Resident parking permit, second car | ₪90 a year | ₪120 a year |
| Sign permit | ₪245 per sqm a year, minimum ₪300 | ₪280 per sqm a year, minimum ₪350 |
| Sidewalk tables and chairs | ₪160 per sqm a year | ₪190 per sqm a year |
| Street closure for an event | ₪350 a day | ₪350 a day (unchanged) |
| Skip on the street | ₪60 a week | ₪75 a week |
| Building file copy (digital) | ₪60 | ₪40 |
| Extra bulky-waste pickup | ₪120 | ₪150 |

Also decided: event applications must be submitted at least **21 days** before the event (was 14),
from 1 January 2026; the parking permit processing standard is **10 working days** (was 21) from
1 July 2026.

The Licensing and Permits Division and the Spokesperson will update the website and all publications.
""",
"permits/parking-permit-procedure-v4.md": """# Procedure PRK-4: resident parking permits

Licensing and Permits Division. Version 4, in force 1 July 2026 (replaces version 3 of March 2024).
Approved by the director-general on 24 June 2026. Fictional.

1. **Scope.** Resident parking permits in the city's paid-parking zones.
2. **Who applies.** A resident whose address in the Population Register is in Givat Oren.
3. **Eligible vehicles.**
   - (a) a private vehicle registered to the applicant or to the applicant's spouse at the same address;
   - (b) **a leased vehicle or a company vehicle used regularly by the applicant**, with a letter from
     the employer or the leasing company naming the applicant as the driver (new in version 4);
   - (c) not more than two permits per household.
4. **Fees.** First vehicle free; second vehicle per the council's fee decision (2026: ₪120 a year).
5. **Processing.** A decision within 10 working days of a complete application.
6. **Refusal.** A refusal letter states which condition in section 3 is not met and which document
   would meet it, and the objection route (procedure APL).
7. **Records.** Every decision is recorded in Rishuyit with a reason code.
""",
"permits/parking-permit-checklist-clerks.md": """# Desk checklist: resident parking permit

Printed checklist used at the parking permits desk (copy taken from the desk on 1 December 2026).
Header: "Checklist PRK — version 3, March 2024". Fictional.

- [ ] ID with appendix: address in Givat Oren?  → if no: reject, code R-02
- [ ] Vehicle licence: registered to the applicant (or spouse at the same address)? → if no: reject, code R-03 or R-07
- [ ] Leased / company car? → **not eligible**: reject, code R-07 ("section 3")
- [ ] Second car in the household? → fee ₪90
- [ ] All fields complete? → if no: reject, code R-05
- [ ] Decision within 21 working days

Handwritten note at the bottom: "new procedure?? ask Eli" (undated).
""",
"permits/decision-letter-templates.md": """# Decision letter templates in Rishuyit (extract)

Exported by Information Systems on 1 December 2026. Rishuyit generates letters from these templates; the
clerk chooses a reason code from a list of eight. All templates are in Hebrew; an Arabic approval
template exists for parking permits only and has not been used since 2023. English glosses added for
this data room. Fictional.

## T-PRK-APPROVE (Hebrew)

> שלום רב, בקשתך לתו חניה לתושב אושרה. התו יישלח אליך בדואר תוך 7 ימי עבודה.
>
> *Gloss:* "Your request for a resident parking permit has been approved. The permit will be posted to
> you within 7 working days."

## T-PRK-REJECT (Hebrew)

> שלום רב, לאחר בדיקת בקשתך הוחלט לדחותה. סיבת הדחייה: {reason_text_he}. לבירורים: מוקד 106.
>
> *Gloss:* "Having examined your request, it has been decided to reject it. Reason for rejection:
> {reason text}. For enquiries: Moked 106."

With code R-07 the reason text reads: "אינו עומד בתנאים (סעיף 3 לנוהל)" — "does not meet the criteria
(section 3 of the procedure)".

## T-GEN-REJECT (Hebrew, all other permit types)

> בקשתך נדחתה. סיבה: {reason_text_he}. ניתן לפנות למוקד 106.
>
> *Gloss:* "Your request was rejected. Reason: {reason text}. You may contact Moked 106."

No template mentions the objection route, a document that would change the decision, or a language
other than Hebrew.
""",
"chatbot/ruti-setup-notes.md": """# "Ruti" — notes from the business-licensing desk

Written by Yossi Hadad (business licensing clerk) on 3 December 2026 at the request of the Head of
Digital Services. Fictional; "BotNest" is a fictional no-code chatbot platform.

- I built Ruti in March 2026 on BotNest's free plan, in the evenings, because the business-licensing
  phone line was impossible. My manager saw it and said it was a great idea.
- Knowledge: I uploaded the 2025 fee table PDF and our "Guide for business owners" (2024) PDF. I have
  not updated them. BotNest uses a large language model to answer from the files.
- It is on three pages (signs, sidewalk cafés, business licence) as a script I pasted into the page
  in SiteBuilder; editors in our division can do that.
- It answers in Hebrew. I think it understands Arabic and Russian questions.
- BotNest free plan: conversation logs kept by BotNest; the terms say conversations "may be used to
  improve our services". Account in my private email. 640 conversations so far (the export is
  `ruti-bot-log.csv`).
- Nobody from IT or legal has looked at it. I didn't think it needed approval because it was free.
""",
"governance/foi-response-2026-09-ai.md": """# Response to Freedom of Information request FOI-2026-031

Givat Oren municipality — the officer for freedom of information. 14 September 2026. Fictional.

To: [journalist, local news site]

Re: your request of 3 August 2026 under the Freedom of Information Law, 5758-1998, for a list of
artificial-intelligence or algorithmic systems used by the municipality, including chatbots, and the
purposes for which they are used.

Following an inquiry with the Information Systems Division, we inform you that the municipality does
not use artificial-intelligence systems. Accordingly there is no information to provide.

Signed: Dana Shalev, FOI officer. Reviewed: Adv. Samer Haddad, legal adviser.

*Internal note attached in the file:* "IT (D. Kogan), 10 Sep: no AI systems in IS inventory. Parking
cameras are the enforcement vendor's system. Translation vendor is a service contract."
""",
"governance/accessibility-statement.md": """# Accessibility statement (as published on the website)

Last updated: 12 March 2021. Fictional.

The Givat Oren municipality website complies with the Equal Rights for Persons with Disabilities
(Service Accessibility Adjustments) Regulations, 5773-2013, and Israeli Standard 5568 at level AA.
All pages and documents on the site are accessible. The site supports screen readers and keyboard
navigation.

Accessibility coordinator: Natalie Weiss, Digital Services. Contact: Moked 106.
""",
"governance/accessibility-audit-2023-summary.md": """# Website accessibility audit 2023 — summary of findings

External accessibility auditor, report dated 7 September 2023 (summary page). Fictional.

| Area | Finding | Status (Digital Services tracker, Oct 2026) |
|---|---|---|
| Hebrew site templates | 9 issues (contrast, focus order) | 7 fixed |
| Arabic, Russian, English sections | Language attribute missing; text direction errors in Arabic | Open (translation vendor) |
| PDF forms (permits, objections) | 23 scanned forms with no text layer; not readable by screen readers | Open |
| Online forms | Error messages not announced | Fixed |
| Third-party embeds | Not audited (outside scope) | — |

41 issues in total; 22 open. Auditor's note: "The accessibility statement should be updated to
reflect the current state and the alternatives offered."
""",
"governance/information-security-procedure-2022-extract.md": """# Information security procedure IS-07 (extract): external services and cloud

Information Systems Division, approved March 2022. Fictional.

7.1 No municipal information classified "internal" or above, and no residents' personal data, may be
entered into an external online service unless the service was approved by the CISO and a contract
with data-protection terms is in place.

7.2 No script, widget or third-party code may be embedded in the municipal website without the
approval of Information Systems.

7.3 Personal accounts (private email) may not be used to operate any service for the municipality.

7.4 Exceptions: in writing, by the CIO with the CISO.
""",
"procurement/procurement-procedure-extract.md": """# Municipal procurement procedure (extract): when is a tender needed?

Treasurer's office and the legal adviser's office, version 2025. Plain-language summary for division
heads; it does not replace the law or the legal adviser's opinion. Fictional procedure; the legal
references are real and should be read in their current version.

1. **The rule.** A municipality contracts for goods, services or works only by public tender
   (Municipalities Ordinance, section 197), unless the Municipalities (Tenders) Regulations,
   5748-1987, give an exemption.
2. **Small purchases.** Below the amount in regulation 3(3) no tender is needed; the municipality's
   procedure still requires price quotes. Between that amount and the ceiling in regulation 8, a
   limited tender ("מכרז זוטא") with invitations to at least four or six suppliers. The amounts are
   linked to the consumer price index and updated monthly (regulation 2); the procurement unit
   publishes the current figures on the intranet. Reference: October 2021, ₪145,500 and ₪710,600.
3. **Common exemptions** (regulation 3), each recorded with reasons and approved as the regulations
   require: special knowledge or expertise (3(8)); the only supplier in Israel, confirmed by an expert
   (3(4)); a company whose shareholders are a majority of local authorities, for management and
   supervision services (3(15)); another local authority (3(16)).
4. **Commitments.** A commitment with a financial obligation binds the municipality only when signed
   by the mayor and the treasurer (Municipalities Ordinance, section 203). Staff may not promise a
   supplier work, a pilot or a future contract.
5. **Free trials and pilots.** A "free" pilot is still an engagement. Before any supplier receives
   municipal data or access, consult the legal adviser: equal treatment of potential bidders, who owns
   what the supplier learns, data protection, and whether the free period leads into a paid term.
6. **Requests for information (RFI).** Before a tender, a public request for information may be used
   to learn the market; all suppliers get the same information and time.
""",
"procurement/civictalk-proposal.md": """# CivicTalk — proposal: "Givat Oren Answers" citizen chatbot

CivicTalk Ltd (fictional), 2 November 2026. Sent to Eyal Ben-Haim, chief of staff.

**Who we are.** Israel's leading GovTech conversational platform, trusted by **30 local authorities**.

**The offer.**
- **90-day free pilot**: the chatbot on your website, in Hebrew, Arabic, Russian, English and more,
  trained on your website content. Live in 3 weeks.
- After the pilot: ₪14,500 + VAT per month, 36-month term, renewing automatically for 12 months unless
  cancelled 90 days in advance. Includes up to 50,000 conversations a month.
- Purchase without a tender through the local-authorities framework agreement (we are an approved
  supplier).

**Results.** 94% answer accuracy on the CivicTalk Israeli Municipal Benchmark. 70% of resident
questions resolved without a human. Accessible (WCAG compliant). Data hosted in the EU.

**What we need from you.** Your website address (received), a logo, and a contact person. We
completed an initial crawl of www.givat-oren.example on 9 November 2026 (1,212 pages and 31 PDFs).
""",
"procurement/email-thread-2026-10.md": """# Email thread: CivicTalk (extract)

Exported from Eyal Ben-Haim's mailbox at the legal adviser's request, 21 December 2026. Fictional.

---

**From:** Liron Avital (CivicTalk) **To:** Eyal Ben-Haim **Date:** 14 October 2026, 16:20
Great to meet you at the conference in Eilat. As discussed, we can have "Givat Oren Answers" live for
the mayor's event with a free pilot. Shall we go ahead?

**From:** Eyal Ben-Haim **To:** Liron Avital **Date:** 14 October 2026, 22:05
Yes, go ahead with the free pilot, the mayor is excited. Site is www.givat-oren.example. Send me
something I can show him. Budget we'll sort out later, there's a line for next year.

**From:** Liron Avital **To:** Eyal Ben-Haim **Date:** 2 November 2026, 10:12
Attached our proposal. We've already crawled your site. We'll need a technical contact to embed the
widget; we're in the framework so no tender needed.
""",
"procurement/framework-catalogue-extract.md": """# Framework agreement catalogue (extract): digital services for local authorities

Published by the local-authorities purchasing company (fictional), October 2026. A company owned by
local authorities that runs framework tenders authorities can buy through.

| Framework | Scope | Approved suppliers (extract) | Valid until |
|---|---|---|---|
| FW-21/2024 Digital forms and online payments | Online forms, payment pages, digital signature, form hosting | CivicTalk Ltd; FormaPay Ltd; Shaar Digital Ltd | 31 Dec 2027 |
| FW-07/2025 Website hosting and CMS | Hosting, CMS licences, maintenance | three suppliers | 30 Jun 2028 |
| FW-12/2025 Accessibility audits | Website and document accessibility audits | four suppliers | 31 Mar 2027 |

No framework for chatbots, conversational AI or AI services was open on the date of this catalogue.
""",
"hr/works-committee-letter-2026-11-11.md": """# Letter from the works committee

To: Dr. Ronit Shemesh, director-general. Cc: Orna Ziv, Resident Service Division; Larisa Gurevich,
Moked 106. From: Moshe Azulay, chair, works committee of the Givat Oren municipality employees.
11 November 2026. Fictional.

Re: "Robot" in Moked 106

We have heard from several sources that the municipality intends to introduce an artificial-
intelligence "robot" to answer residents instead of the Moked 106 workers.

We remind the management of the agreement on Moked 106 of 2019 and of the duty to consult the
workers' representatives before any change in work methods, technology or staffing. We expect to
receive full information and to be consulted before any decision, purchase or pilot.

We will not accept a change that harms the employment or the conditions of the Moked workers, who
have carried the city through the war and through every emergency.

Moshe Azulay
""",
"hr/moked-106-agreement-2019-extract.md": """# Local agreement on Moked 106 work arrangements, 2019 (extract)

Between the Givat Oren municipality and the works committee, signed 4 April 2019. Fictional.

4. Service hours: Sunday–Thursday 07:00–23:00, Friday 08:00–14:00, emergencies 24/7 via the security
   centre.
7. **Changes.** The municipality will inform the works committee in writing and consult with it before
   introducing a change in the work methods, the technology used by the Moked workers, or the number
   of positions, and will give the committee a reasonable opportunity to present its position.
8. Training: every new system used by Moked workers will come with at least 6 hours of paid training.
9. The agreement does not derogate from the collective agreements applying to local-authority
   employees.
""",
}


def build_markdown() -> None:
    for rel, text in DOCS.items():
        write_text(HERE / rel, text)


def main() -> None:
    site = build_documents()
    build_cms(site)
    moked = build_moked()
    write_text(HERE / "service" / "moked-kpi-report-2026-q3.md", moked_kpi_report(moked))
    build_permits()
    items = build_test_set()
    build_mystery_shopper(items)
    build_ruti()
    build_foi()
    build_markdown()
    print(f"Data room written to {HERE}; pilot inputs to {PILOT}")


if __name__ == "__main__":
    main()
