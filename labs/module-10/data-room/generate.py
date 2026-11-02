"""Rebuild the Galil Health data room (module 10) byte for byte.

    python generate.py

Python 3.12+, standard library only. Seeded (20261115): every run writes identical files. Text lives
in textbank.py. Also writes the proof-of-concept files in ../poc/. All organizations, people, patients
and vendors are fictional; every number is synthetic.

Reading this file spoils the engagement: finish module 10 first.
"""
from __future__ import annotations

import csv
import io
import math
import random
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import textbank as tb

SEED = 20261115
HERE = Path(__file__).resolve().parent
POC = HERE.parent / "poc"

# ---------------------------------------------------------------- helpers


def rng(name: str) -> random.Random:
    """One independent, reproducible stream per table."""
    return random.Random(f"{SEED}-{name}")


def write_csv(path: Path, header: list[str], rows: list[list]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    for r in rows:
        w.writerow(["" if v is None else v for v in r])
    path.write_text(buf.getvalue(), encoding="utf-8", newline="\n")


def write_md(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")


def tz_for(d: date) -> timezone:
    # Israel summer time ends on Sunday 25 October 2026.
    return timezone(timedelta(hours=3)) if d < date(2026, 10, 25) else timezone(timedelta(hours=2))


def stamp(d: date, minutes_from_midnight: float) -> str:
    base = datetime(d.year, d.month, d.day, tzinfo=tz_for(d))
    return (base + timedelta(minutes=minutes_from_midnight)).isoformat(timespec="minutes")


def lognorm(r: random.Random, median: float, sigma: float) -> float:
    return median * math.exp(r.gauss(0, sigma))


def pick(r: random.Random, weights: dict):
    x = r.random() * sum(weights.values())
    for k, w in weights.items():
        x -= w
        if x <= 0:
            return k
    return k


def pct(n: float, d: float) -> str:
    return f"{100 * n / d:.1f}%" if d else "n/a"


# ---------------------------------------------------------------- the organization

# id, name, region, type, notara version, doctors, nurses, patient language mix (preferred language)
CLINICS = [
    ("GH-AKK", "Akko", "Western Galilee", "primary", "9.2", 6, 3, {"he": .38, "ar": .57, "ru": .03, "oth": .02}),
    ("GH-NAH", "Nahariya", "Western Galilee", "primary", "9.2", 6, 3, {"he": .48, "ru": .42, "ar": .06, "oth": .04}),
    ("GH-NAHP", "Nahariya Child Development & Paediatrics", "Western Galilee", "specialist", "9.2", 4, 3, {"he": .40, "ar": .30, "ru": .25, "oth": .05}),
    ("GH-KRM", "Karmiel", "Karmiel–Misgav", "primary", "9.2", 7, 4, {"he": .30, "ru": .60, "ar": .07, "oth": .03}),
    ("GH-MAJ", "Majd al-Krum", "Karmiel–Misgav", "primary", "9.2", 5, 3, {"ar": .94, "he": .05, "ru": .01, "oth": 0}),
    ("GH-KRMW", "Karmiel Women's Health", "Karmiel–Misgav", "specialist", "9.2", 4, 3, {"he": .36, "ru": .32, "ar": .29, "oth": .03}),
    ("GH-NAZ", "Nazareth", "Nazareth", "primary", "9.2", 7, 4, {"ar": .93, "he": .05, "ru": .02, "oth": 0}),
    ("GH-NOF", "Nof HaGalil", "Nazareth", "primary", "9.2", 7, 3, {"ru": .47, "he": .22, "ar": .28, "oth": .03}),
    ("GH-NAZD", "Nazareth Diabetes & Endocrine Centre", "Nazareth", "specialist", "9.2", 4, 3, {"ar": .55, "he": .20, "ru": .22, "oth": .03}),
    ("GH-SAF", "Safed", "Upper Galilee", "primary", "7.4", 6, 3, {"he": .53, "ru": .38, "oth": .06, "ar": .03}),
    ("GH-HAT", "Hatzor HaGlilit", "Upper Galilee", "primary", "7.4", 5, 2, {"he": .48, "ru": .42, "oth": .07, "ar": .03}),
    ("GH-TIB", "Tiberias", "Kinneret", "primary", "7.4", 6, 3, {"he": .44, "ru": .45, "oth": .05, "ar": .06}),
    ("GH-MGR", "Maghar", "Kinneret", "primary", "7.4", 5, 2, {"ar": .91, "he": .08, "ru": .01, "oth": 0}),
    ("GH-TIBC", "Tiberias Cardiology & Internal Medicine", "Kinneret", "specialist", "7.4", 6, 3, {"he": .38, "ru": .36, "ar": .23, "oth": .03}),
]
CLINIC = {c[0]: c for c in CLINICS}
SPECIALTY = {"GH-NAHP": "paediatrics", "GH-KRMW": "gynaecology", "GH-NAZD": "endocrinology", "GH-TIBC": "cardiology"}
OTHER_LANGS = {"en": .5, "am": .3, "ti": .2}

# ---------------------------------------------------------------- clinicians


def build_clinicians():
    r = rng("clinicians")
    rows = []
    n = 0
    for cid, _name, _reg, ctype, _ver, docs, nurses, mix in CLINICS:
        for role, count in (("doctor", docs), ("nurse", nurses)):
            for _ in range(count):
                n += 1
                langs = ["he"]
                # A clinician speaks the clinic's main non-Hebrew languages more often than not.
                if r.random() < mix.get("ar", 0) * 1.05 + (0.04 if role == "nurse" else 0):
                    langs.append("ar")
                if r.random() < mix.get("ru", 0) * 1.0:
                    langs.append("ru")
                if r.random() < (0.55 if role == "doctor" else 0.25):
                    langs.append("en")
                if role == "doctor":
                    spec = SPECIALTY.get(cid, "family_medicine" if r.random() < .82 else "internal_medicine")
                else:
                    spec = "diabetes_nurse" if cid == "GH-NAZD" else ("paediatric_nurse" if cid == "GH-NAHP" else "community_nurse")
                fte = r.choice([1.0, 1.0, 1.0, 0.8, 0.8, 0.6, 0.4]) if role == "doctor" else r.choice([1.0, 1.0, 0.8, 0.6])
                start = r.randint(1999, 2026) if r.random() < .8 else r.randint(2020, 2026)
                rows.append([f"C-{n:03d}", role, cid, spec, fte, ";".join(langs), start])
    return rows


# ---------------------------------------------------------------- visits (Notara export)

START, END = date(2026, 9, 1), date(2026, 10, 31)
CLOSED = {date(2026, 9, 13), date(2026, 9, 21)}          # Rosh Hashanah (2nd day), Yom Kippur
REDUCED = {date(2026, 9, 27) + timedelta(days=i) for i in range(5)}  # Sukkot intermediate days


def workdays():
    d = START
    while d <= END:
        if d.weekday() in (6, 0, 1, 2, 3) and d not in CLOSED:  # Sunday–Thursday
            yield d
        d += timedelta(days=1)


def build_visits(clinicians):
    r = rng("visits")
    docs = [c for c in clinicians if c[1] == "doctor"]
    doctor_days, visits = [], []
    vid = 0
    for c in docs:
        cid_c, _role, clinic, spec, fte, langs, _start = c
        langs = langs.split(";")
        ctype = CLINIC[clinic][3]
        mix = CLINIC[clinic][7]
        days_per_week = round(fte * 5)
        weekdays = sorted(r.sample([6, 0, 1, 2, 3], days_per_week))
        afternoon = r.random() < 0.35
        doc_factor = lognorm(r, 1.0, 0.15)
        late_factor = lognorm(r, 1.0, 0.35)
        for d in workdays():
            if d.weekday() not in weekdays:
                continue
            if r.random() < 0.06:  # leave, courses, sick days
                continue
            base = {"primary": 25, "specialist": 15}[ctype]
            if spec == "paediatrics":
                base = 19
            n = max(6, int(r.gauss(base, 3)))
            if d in REDUCED:
                n = int(n * 0.7)
            session_start = (14 * 60) if afternoon else (8 * 60)
            doctor_days.append([cid_c, d.isoformat(), "pm" if afternoon else "am", n])
            t = session_start
            for _ in range(n):
                slot = 20 if ctype == "specialist" else r.choice([10, 10, 10, 15])
                if r.random() < 0.08:
                    vid += 1
                    visits.append(make_visit(r, vid, c, langs, ctype, spec, mix, d, t, slot, doc_factor, late_factor))
                t += slot
    return doctor_days, visits


def make_visit(r, vid, c, langs, ctype, spec, mix, d, t, slot, doc_factor, late_factor):
    cid_c, _role, clinic, *_ = c
    pref = pick(r, mix)
    if pref == "oth":
        pref = pick(r, OTHER_LANGS)
    speaks = pref in langs
    age = pick(r, {"0-17": .14 if spec != "paediatrics" else .95, "18-44": .26, "45-64": .28, "65-74": .17, "75+": .15})
    if spec == "paediatrics":
        age = "0-17"
    elderly = age in ("65-74", "75+")
    # Who is in the room and who interprets.
    if not speaks:
        interp = pick(r, {"relative": .52, "nurse": .30, "phone": .06, "none": .12})
        relative = interp == "relative" or r.random() < .15
    else:
        interp = "none"
        relative = r.random() < ((0.45 if elderly else 0.18) if pref != "he" else (0.25 if elderly else 0.08))
        if spec == "paediatrics":
            relative = True
    # Documentation time in the note window (seconds).
    base = {"primary": 200, "specialist": 300}[ctype]
    if spec == "paediatrics":
        base = 220
    m = doc_factor
    if not speaks:
        m *= {"relative": 1.5, "nurse": 1.35, "phone": 1.6, "none": 1.3}[interp]
    elif pref != "he":
        m *= 1.12  # visit in Arabic or Russian, note written in Hebrew
    if relative:
        m *= 1.08
    if age == "75+":
        m *= 1.1
    active = int(lognorm(r, base * m, 0.42))
    p_late = (0.30 if not speaks else 0.12) * late_factor * (1.4 if ctype == "specialist" else 1.0)
    after = int(lognorm(r, 160, 0.5)) if r.random() < min(p_late, 0.9) else 0
    opened = t + r.uniform(0, 2)
    end = t + slot
    if after:
        signed_day, signed_min = (d, r.uniform(19.5 * 60, 23.5 * 60)) if r.random() < 0.7 else (d + timedelta(days=1), r.uniform(7 * 60, 8 * 60))
    elif r.random() < 0.025:
        signed_day, signed_min = d + timedelta(days=r.randint(2, 6)), r.uniform(8 * 60, 18 * 60)
    else:
        signed_day, signed_min = d, end + r.uniform(0, 25)
    # Notara's visit-language field defaults to Hebrew; doctors change it in about a third of visits.
    vlang = pref if (pref == "he" or r.random() < 0.34) else "he"
    # The relative field is optional and often left empty.
    rel_field = "" if r.random() < 0.40 else ("y" if relative else "n")
    interp_field = "" if r.random() < 0.10 else interp
    vtype = "paediatric" if spec == "paediatrics" else ("specialist" if ctype == "specialist" else pick(r, {"acute": .45, "chronic": .35, "follow_up": .20}))
    return [
        f"V-{2600000 + vid * 7 + r.randint(0, 6)}", clinic, cid_c, d.isoformat(), stamp(d, t), slot, vtype, age,
        pref, vlang, rel_field, interp_field, stamp(d, opened), stamp(signed_day, signed_min), active, after,
        int(lognorm(r, 900 * m, 0.35)), "y" if r.random() < 0.17 else "n",
    ]


# ---------------------------------------------------------------- survey


def build_survey(clinicians):
    r = rng("survey")
    respondents = [c for c in clinicians if r.random() < (0.78 if c[1] == "doctor" else 0.55)]
    texts = list(tb.SURVEY_TEXT)
    r.shuffle(texts)
    rows = []
    for i, c in enumerate(respondents):
        cid_c, role, clinic, spec, fte, langs, start = c
        region = CLINIC[clinic][2]
        years = 2026 - start
        yb = "0-4" if years < 5 else ("5-14" if years < 15 else "15+")
        if role == "doctor":
            mins = int(round(lognorm(r, 118, 0.28) / 5) * 5)
            late = min(5, max(0, int(r.gauss(2.6, 1.4))))
            interp_m = ""
        else:
            mins = int(round(lognorm(r, 70, 0.3) / 5) * 5)
            late = min(5, max(0, int(r.gauss(1.0, 1.0))))
            mixed = CLINIC[clinic][7].get("he", 0) < .6 and CLINIC[clinic][7].get("ar", 0) < .85
            interp_m = int(round(lognorm(r, 45 if mixed else 15, 0.4) / 5) * 5)
        use = r.choice([1, 2, 3, 3, 4, 4, 4, 5, 5]) if role == "doctor" else r.choice([2, 3, 3, 4, 4, 5])
        concern = pick(r, {"accuracy": .27, "privacy": .2, "patients_refuse": .12, "time_to_check": .14,
                           "language_support": .14, "recordings_used_against_staff": .08, "none": .05})
        tools = pick(r, {"notara_templates": .55, "none": .30, "dictation": .03, "other": .12})
        text = ""
        if texts and r.random() < 0.42:
            lang, text, kind = texts.pop()
            if kind == "tool":
                tools = "other"
        submitted = stamp(date(2026, 10, 4) + timedelta(days=r.randint(0, 18)), r.uniform(7 * 60, 23 * 60))
        rows.append([f"S-{i + 1:03d}", submitted, role, region, yb, mins, late, interp_m, use, concern, tools, text])
    # Any tool comments not yet placed go to respondents who left the comment empty.
    for lang, text, kind in texts:
        for row in rows:
            if row[11] == "" and row[2] == "doctor":
                row[11] = text
                if kind == "tool":
                    row[10] = "other"
                break
    rows.sort(key=lambda x: x[1])
    for i, row in enumerate(rows):
        row[0] = f"S-{i + 1:03d}"
    return rows


# ---------------------------------------------------------------- 2025 dictation trial usage


def build_trial(clinicians):
    r = rng("trial")
    docs = [c for c in clinicians if c[1] == "doctor" and c[2] in ("GH-NOF", "GH-NAH")]
    docs = docs[:9]
    keep = {docs[1][0], docs[6][0]}  # the two who kept using it
    rows = []
    monday = date(2025, 3, 2)  # a Sunday: Israeli working week
    for w in range(1, 13):
        wk = monday + timedelta(weeks=w - 1)
        for c in docs:
            visits = int(r.gauss(110, 15) * c[4])
            if c[0] in keep:
                share = min(0.9, 0.55 + 0.03 * w + r.uniform(-0.05, 0.05))
            else:
                share = max(0.0, 0.62 * math.exp(-0.42 * (w - 1)) + r.uniform(-0.04, 0.04))
            dict_n = int(visits * share)
            corr = int(lognorm(r, 210 if w < 4 else 170, 0.2)) if dict_n else ""
            rows.append([wk.isoformat(), w, c[0], c[2], visits, dict_n, corr])
    return rows


# ---------------------------------------------------------------- incidents


def build_incidents():
    r = rng("incidents")
    rows = [list(x) for x in tb.FIXED_INCIDENTS]
    used = {x[0] for x in rows}
    d = date(2025, 1, 5)
    n25, n26 = 0, 0
    while d <= date(2026, 10, 28):
        if r.random() < 0.085:
            cat, sevs, he, en = r.choice(tb.GENERIC_INCIDENTS)
            year = d.year
            while True:
                num = r.randint(1, 79)
                iid = f"IN-{year}-{num:03d}"
                if iid not in used:
                    break
            used.add(iid)
            rows.append([iid, d.isoformat(), r.choice([c[0] for c in CLINICS]), cat, r.choice(sevs), he, en])
        d += timedelta(days=1)
    rows.sort(key=lambda x: (x[1], x[0]))
    return rows


# ---------------------------------------------------------------- proxy / firewall AI summary


def build_proxy():
    r = rng("proxy")
    rows = []
    heavy_stt = {"GH-KRM": 5, "GH-NOF": 3, "GH-NAH": 2, "GH-SAF": 2, "GH-AKK": 1}
    gpt_clinics = {"GH-KRM", "GH-NOF", "GH-NAH", "GH-AKK", "GH-NAZ", "GH-SAF", "GH-TIB", "GH-KRMW", "GH-NAZD"}
    for wk in range(4):
        week = (date(2026, 10, 4) + timedelta(weeks=wk)).isoformat()
        for cid, *_ in CLINICS:
            if cid in gpt_clinics:
                rows.append([week, cid, "clinic_lan", "ChatGPT", "AI chatbot", r.randint(40, 260), round(r.uniform(0.2, 3.5), 1), r.randint(2, 6)])
            if r.random() < 0.35:
                rows.append([week, cid, "clinic_lan", "Google Gemini", "AI chatbot", r.randint(5, 60), round(r.uniform(0.1, 0.9), 1), r.randint(1, 3)])
            if r.random() < 0.15:
                rows.append([week, cid, "clinic_lan", "Claude", "AI chatbot", r.randint(3, 30), round(r.uniform(0.1, 0.6), 1), r.randint(1, 2)])
            rows.append([week, cid, "clinic_lan", "Google Translate", "translation", r.randint(300, 1500), round(r.uniform(0.5, 4.0), 1), r.randint(4, 12)])
            if cid in heavy_stt:
                k = heavy_stt[cid]
                rows.append([week, cid, "guest_wifi", "Generic: AI speech-to-text (consumer)", "AI audio transcription",
                             r.randint(60, 140) * k, round(r.uniform(90, 160) * k, 1), max(1, k + r.randint(-1, 1))])
            rows.append([week, cid, "guest_wifi", "WhatsApp", "messaging", r.randint(2000, 9000), round(r.uniform(200, 900), 1), r.randint(20, 80)])
    return rows


# ---------------------------------------------------------------- demo-day scorecards (match the vendor-rfp preset)

CRITERIA = ["evidence", "safety", "privacy", "languages", "integration", "contract"]
WEIGHTS = {"evidence": 2, "safety": 3, "privacy": 3, "languages": 2, "integration": 1, "contract": 2}
DEMO = {
    "ScribeWave": {"evidence": 4, "safety": 4, "privacy": 3, "languages": 4, "integration": 4, "contract": 3},
    "Kol Refua": {"evidence": 3, "safety": 3, "privacy": 5, "languages": 4, "integration": 3, "contract": 3},
    "MedNote for Notara": {"evidence": 3, "safety": 3, "privacy": 4, "languages": 3, "integration": 5, "contract": 4},
    "Rishma Health": {"evidence": 3, "safety": 3, "privacy": 3, "languages": 3, "integration": 2, "contract": 3},
}
DEMO_META = {
    "ScribeWave": ("2026-10-26", "en", "Live: a doctor and an actor playing a patient, studio headset microphone"),
    "Kol Refua": ("2026-10-28", "he", "Live: the founder and a family doctor from the start-up's partner clinic"),
    "MedNote for Notara": ("2026-11-02", "he", "Live in Notara 9.2: doctor dictates a summary after the patient leaves"),
    "Rishma Health": ("2026-11-05", "ar;he", "Recorded consented visit, played back; draft note shown with unsure passages marked"),
}
RATERS = [("R1", "CEO"), ("R2", "CIO"), ("R3", "CMO"), ("R4", "CFO"), ("R5", "Counsel and DPO"),
          ("R6", "Head of Nursing"), ("R7", "Doctor, Akko"), ("R8", "Doctor, Safed"), ("R9", "Nurse, Nazareth")]
COMMENTS = {
    "ScribeWave": ["Note ready in seconds, impressive", "Coded automatically", "Very polished", "Will it work in Arabic?", ""],
    "Kol Refua": ["Understands Hebrew slang and brand names", "Israeli, data stays here", "Small company", ""],
    "MedNote for Notara": ["Inside Notara, one click", "No integration project", "That was dictation, not a conversation?", ""],
    "Rishma Health": ["Boring demo", "Marks unsure passages, doctor must confirm", "Recorded, not live", "Expensive", ""],
}


def build_scorecards():
    r = rng("scorecards")
    rows = []
    for vendor, targets in DEMO.items():
        ddate, dlang, setup = DEMO_META[vendor]
        for crit in CRITERIA:
            t = targets[crit]
            devs = [0, 0, 0, 1, -1, 0, 1, -1, 0] if 1 < t < 5 else [0, 0, 0, 0, -1, 0, 0, 0, 0]
            if t == 1:
                devs = [0] * 8 + [1]
            r.shuffle(devs)
            for (rid, role), dv in zip(RATERS, devs):
                comment = r.choice(COMMENTS[vendor]) if crit == "evidence" else ""
                rows.append([ddate, vendor, dlang, setup, rid, role, crit, t + dv, comment])
    return rows


# ---------------------------------------------------------------- proof of concept (match the preset)

POC_TARGET = {
    # vendor: per language (wer, minutes to correct), omissions per language, invented per language, flagged omissions
    "ScribeWave": {"wer": {"he": 14, "ar": 27, "ru": 12}, "edit": {"he": 3.9, "ar": 5.8, "ru": 3.8},
                   "omit": {"he": 4, "ar": 7, "ru": 2}, "invent": {"he": 1, "ar": 3, "ru": 1}, "flag": 0},
    "Kol Refua": {"wer": {"he": 8, "ar": None, "ru": 21}, "edit": {"he": 2.9, "ar": None, "ru": 4.1},
                  "omit": {"he": 2, "ar": 0, "ru": 4}, "invent": {"he": 0, "ar": 0, "ru": 1}, "flag": 0},
    "MedNote for Notara": {"wer": {"he": 19, "ar": 31, "ru": 26}, "edit": {"he": 5.4, "ar": 6.6, "ru": 6.0},
                           "omit": {"he": 6, "ar": 8, "ru": 6}, "invent": {"he": 1, "ar": 2, "ru": 1}, "flag": 0},
    "Rishma Health": {"wer": {"he": 9, "ar": 11, "ru": 10}, "edit": {"he": 2.9, "ar": 3.2, "ru": 2.9},
                       "omit": {"he": 1, "ar": 2, "ru": 1}, "invent": {"he": 0, "ar": 1, "ru": 0}, "flag": 3},
}
# Fixed cells that the sample notes show (vendor, visit, run): (omitted, invented)
FIXED_CELLS = {
    ("ScribeWave", "P-38", 1): (1, 0), ("MedNote for Notara", "P-38", 1): (2, 0), ("Rishma Health", "P-38", 1): (0, 0),
    ("Kol Refua", "P-71", 1): (1, 0), ("ScribeWave", "P-71", 1): (0, 0), ("MedNote for Notara", "P-71", 1): (0, 0),
    ("Rishma Health", "P-71", 1): (0, 0), ("ScribeWave", "P-07", 1): (0, 1), ("MedNote for Notara", "P-07", 1): (1, 0),
    ("Kol Refua", "P-07", 1): (0, 0), ("Rishma Health", "P-07", 1): (0, 0),
}
SCENARIOS = {
    "primary": ["new cough and fever", "diabetes follow-up", "hypertension review", "back pain", "medication review after hospital",
                "rash", "fatigue and anaemia results", "asthma flare"],
    "specialist": ["chest pain follow-up (cardiology)", "insulin adjustment (endocrinology)", "pregnancy check (gynaecology)",
                   "child development review (paediatrics)", "heart failure review (cardiology)"],
}


def build_poc():
    r = rng("poc")
    visits = []
    for i in range(90):
        lang = ["he", "ar", "ru"][i // 30]
        setting = "specialist" if i % 30 >= 22 else "primary"
        relative = (i % 30) % 2 == 1 or (i % 30) in (4, 10, 16)
        noise = r.choice(["quiet", "air_conditioner", "corridor", "child_in_room", "quiet"])
        variety = {"he": r.choice(["native", "native", "Arabic-accented", "Russian-accented"]),
                   "ar": r.choice(["Galilee urban", "Galilee rural", "Druze", "Galilee urban"]),
                   "ru": r.choice(["standard", "standard", "with Hebrew loanwords"])}[lang]
        hard = []
        if relative and r.random() < .55:
            hard.append("med_change_said_by_relative")
        if r.random() < .3:
            hard.append("code_switching")
        if r.random() < .3:
            hard.append("drug_brand_names")
        visits.append([f"P-{i + 1:02d}", lang, setting, r.choice(SCENARIOS[setting]), 3 if relative else 2,
                       "y" if relative else "n", noise, variety, r.randint(8, 15), ";".join(hard) or "none"])
    # Sample-note visits are fixed in shape.
    for v in visits:
        if v[0] == "P-38":
            v[2], v[3], v[4], v[5], v[6], v[7], v[9] = "primary", "hypertension review", 3, "y", "air_conditioner", "Galilee rural", "med_change_said_by_relative"
        if v[0] == "P-71":
            v[2], v[3], v[4], v[5], v[6], v[7], v[9] = "specialist", "heart failure review (cardiology)", 3, "y", "corridor", "standard", "none"
        if v[0] == "P-07":
            v[2], v[3], v[4], v[5], v[6], v[7], v[9] = "primary", "back pain", 2, "n", "quiet", "native", "drug_brand_names"
    vmap = {v[0]: v for v in visits}
    reviewers = {"he": ["RV-he1", "RV-he2"], "ar": ["RV-ar1", "RV-ar2"], "ru": ["RV-ru1", "RV-ru2"]}
    sheet = []
    for vendor, tg in POC_TARGET.items():
        for lang in ("he", "ar", "ru"):
            cells = [(v[0], run) for v in visits if v[1] == lang for run in (1, 2)]
            if tg["wer"][lang] is None:
                for vid, run in cells:
                    sheet.append([vendor, vid, run, lang, "no_output", "", vmap[vid][8], "", "", "", "", "", reviewers[lang][run - 1],
                                  "Empty note returned for Arabic audio"])
                continue
            # Spread omissions and inventions: fixed cells first, then visits with relatives and hard cases.
            omit = {c: 0 for c in cells}
            inv = {c: 0 for c in cells}
            for (fv, fid, frun), (o, iv) in FIXED_CELLS.items():
                if fv == vendor and (fid, frun) in omit:
                    omit[(fid, frun)], inv[(fid, frun)] = o, iv
            fixed = {(fid, frun) for (fv, fid, frun) in FIXED_CELLS if fv == vendor}
            need_o = tg["omit"][lang] - sum(omit.values())
            need_i = tg["invent"][lang] - sum(inv.values())
            pool = [c for c in cells if c not in fixed]
            weights = [(4 if vmap[c[0]][5] == "y" else 1) * (2 if "med_change" in vmap[c[0]][9] else 1) for c in pool]
            while need_o > 0:
                c = r.choices(pool, weights)[0]
                if omit[c] < 2:
                    omit[c] += 1
                    need_o -= 1
            while need_i > 0:
                c = r.choice(pool)
                if inv[c] == 0:
                    inv[c] = 1
                    need_i -= 1
            # Word error and correction minutes: noisy per note, then shifted so the language mean is exact.
            wers = [max(2.0, r.gauss(tg["wer"][lang], tg["wer"][lang] * 0.22) + (2 if vmap[c[0]][6] != "quiet" else -1)) for c in cells]
            shift = tg["wer"][lang] - sum(wers) / len(wers)
            wers = [round(w + shift, 1) for w in wers]
            wers[-1] = round(wers[-1] + tg["wer"][lang] * len(wers) - sum(wers), 1)
            edits = [max(0.8, r.gauss(tg["edit"][lang], 0.9) + 0.9 * omit[c] + 0.5 * inv[c]) for c in cells]
            shift = tg["edit"][lang] - sum(edits) / len(edits)
            edits = [round(e + shift, 1) for e in edits]
            edits[-1] = round(edits[-1] + tg["edit"][lang] * len(edits) - sum(edits), 1)
            for k, c in enumerate(cells):
                vid, run = c
                note = ""
                if omit[c]:
                    note = "Medication change said by a relative missing" if "med_change" in vmap[vid][9] else "Relevant fact missing"
                if inv[c]:
                    note = (note + "; " if note else "") + "Invented a detail not said in the visit"
                sheet.append([vendor, vid, run, lang, "scored", wers[k], vmap[vid][8], omit[c], inv[c], 0,
                              (r.randint(1, 4) if vendor == "Rishma Health" else 0), edits[k], reviewers[lang][run - 1], note])
    # Rishma: three of its four omissions sat inside a passage it had marked unsure.
    flagged = 0
    for row in sheet:
        if row[0] == "Rishma Health" and row[7] and flagged < POC_TARGET["Rishma Health"]["flag"]:
            row[9] = 1
            flagged += 1
            row[13] = row[13] + " (inside a passage marked unsure)"
    return visits, sheet


TERMS = [
    ("noTraining", "No use of our audio, transcripts or notes to train or improve models, de-identified included", "must"),
    ("retention", "Audio deleted within 30 days of the note being signed", "must"),
    ("location", "Stored and processed in Israel, or where Galil's DPO approves in writing", "must"),
    ("subprocessors", "Full sub-processor list, notice before changes, the right to object", "must"),
    ("exit", "Data returned in a standard format, certified deletion, six months' transition", "must"),
    ("modelChange", "Notice before model changes and a re-run on Galil's test set first", "must"),
    ("safety", "A named clinical safety officer and incident reporting to Galil within an agreed time", "must"),
    ("audit", "Independent security certification and the right to audit", "nice"),
    ("priceLock", "Price fixed for three years", "nice"),
]
REPLIES = {
    "ScribeWave": {"noTraining": ("accepts", "On the enterprise plan, 18% more."), "retention": ("refuses", "90 days of audio is the minimum."),
                   "location": ("refuses", "EU or US only."), "subprocessors": ("accepts", "List published; 30 days' notice."),
                   "exit": ("accepts", "Export in a standard format."), "modelChange": ("refuses", "Models update continuously."),
                   "safety": ("accepts", "A named clinical safety contact."), "audit": ("accepts", "The audit report, no on-site audit."),
                   "priceLock": ("refuses", "Annual list-price changes."),
                   "_price": "About ₪1,150 per clinician a month (standard plan); enterprise plan 18% more."},
    "Kol Refua": {"noTraining": ("accepts", "Already in the agreement."), "retention": ("accepts", "Audio deleted after 7 days."),
                  "location": ("refuses", "Not until it replaces the US speech service, \"next year\"."),
                  "subprocessors": ("accepts", "Will add notice and objection."),
                  "exit": ("accepts", "Export, but no escrow; 18 months of funding left."), "modelChange": ("accepts", "Will notify."),
                  "safety": ("accepts", "Will appoint someone."), "audit": ("refuses", "No certification yet."),
                  "priceLock": ("accepts", "Three years fixed."), "_price": "About ₪600 per clinician a month."},
    "MedNote for Notara": {"noTraining": ("refuses", "The master agreement's \"product improvement\" clause stays."),
                           "retention": ("accepts", "Audio deleted after 30 days."), "location": ("accepts", "Hosted in Israel."),
                           "subprocessors": ("accepts", "Listed."), "exit": ("accepts", "Notes stay in Notara anyway."),
                           "modelChange": ("refuses", "Changes ship with Notara releases."),
                           "safety": ("accepts", "Through the existing support contract."), "audit": ("accepts", "Existing certification."),
                           "priceLock": ("refuses", "Year two to be agreed."), "_price": "Free in year one; year two to be agreed."},
    "Rishma Health": {"noTraining": ("accepts", "Default."), "retention": ("accepts", "Default 30 days."),
                       "location": ("accepts", "Israel hosting, about 8% more."), "subprocessors": ("accepts", "Default."),
                       "exit": ("accepts", "Default."), "modelChange": ("accepts", "Notice and a re-run on Galil's test set."),
                       "safety": ("accepts", "Named clinical safety officer."), "audit": ("accepts", "Certification and audit rights."),
                       "priceLock": ("refuses", "Annual indexation."),
                       "_price": "About ₪1,300 per clinician a month, plus the Notara integration project; Israel hosting about 8% more."},
}


def build_rfp_responses():
    rows = []
    for vendor, rep in REPLIES.items():
        for tid, label, kind in TERMS:
            reply, note = rep[tid]
            rows.append([vendor, tid, label, kind, reply, note])
        rows.append([vendor, "price", "Price (as quoted in the RFP answer)", "info", "", rep["_price"]])
    return rows


# ---------------------------------------------------------------- documents

def kpi_report(visits, doctor_days):
    n = len(visits)
    by = {}
    for v in visits:
        by[v[9]] = by.get(v[9], 0) + 1
    within24 = 0
    for v in visits:
        o = datetime.fromisoformat(v[4])
        s = datetime.fromisoformat(v[13])
        within24 += (s - o) <= timedelta(hours=24)
    sep = sum(d[3] for d in doctor_days if d[1] < "2026-10-01")
    octo = sum(d[3] for d in doctor_days if d[1] >= "2026-10-01")
    lang_rows = "\n".join(f"| {name} | {pct(by.get(code, 0), n)} |" for code, name in
                          [("he", "Hebrew"), ("ar", "Arabic"), ("ru", "Russian"), ("en", "English"), ("am", "Amharic"), ("ti", "Tigrinya")])
    return f"""
# Galil Health — Clinical operations KPI report, Q3 2026 (with October)

Prepared by: Operations and BI, 4 November 2026. Distribution: management team.

## Activity

| Measure | July | August | September | October |
|---|---|---|---|---|
| Doctor visits (all clinics) | 29,480 | 26,950 | {sep:,} | {octo:,} |
| Nurse visits | 14,210 | 12,960 | 13,105 | 13,870 |
| Registered patients (end of month) | 111,420 | 111,690 | 111,905 | 112,060 |

## Visits by language¹

| Visit language | Share of doctor visits, Sep–Oct |
|---|---|
{lang_rows}

## Documentation

| Measure | Q3 | Target |
|---|---|---|
| Visit notes signed within 24 hours | {pct(within24, n)} (Sep–Oct) | 95% |
| Documentation time per visit | Not measured² | — |
| After-hours documentation | Not measured | — |

## Workforce

| Measure | Value |
|---|---|
| Doctor posts / filled | 87 / 78 (9 vacant: 4 family medicine, 2 paediatrics, 2 internal medicine, 1 endocrinology) |
| Locum doctor spend, January–September 2026 | ₪1.71M (2025 full year: ₪2.1M) |
| Doctors who left in the last 12 months | 6 (exit interviews: 4 cite workload, 3 of them "notes in the evenings") |
| Nurse posts / filled | 44 / 42 |

## Patient experience

| Measure | Q2 | Q3 |
|---|---|---|
| "The doctor listened to me" (agree, patient survey, n ≈ 1,900 a quarter) | 81% | 79% |
| Complaints about communication or language | 37 | 44 |

¹ Visit language as recorded in Notara ("visit language" field in the visit screen).
² Vendors' published figures suggest about 2 hours a day per doctor; the medical director's October
survey will give Galil's own figure.
"""


DOCS = {}

DOCS["company/company-profile.md"] = """
# Galil Health — company profile

From the management team's welcome pack for new managers (October 2026).

Galil Health (גליל בריאות) is a public-benefit company founded in 1998 by a group of family doctors in
Karmiel and Nazareth. It runs **14 community clinics in five regions** of northern Israel: 10 primary-care
clinics and 4 specialist centres. About **112,000 registered patients** receive their community care from
Galil under service agreements with two health funds (Fund A, about 70% of patients; Fund B, about 30%).
The health funds pay Galil per registered patient (capitation) plus fees for specialist services.

- Revenue 2025: ₪318M. Staff: about 540 (78 doctors, 42 nurses, administrative, laboratory and
  pharmacy-liaison staff, management).
- Patients speak Hebrew, Arabic and Russian, and some English, Amharic and Tigrinya. Many older
  patients come with a son or daughter.
- Clinic record system: **Notara** (Notara Systems Ltd.), since 2019. The Western Galilee, Karmiel–Misgav
  and Nazareth regions run Notara 9.2; Upper Galilee and Kinneret still run Notara 7.4 (upgrade planned
  "in 2027", not yet budgeted).
- Opening hours: Sunday–Thursday 07:30–19:00, Friday 08:00–12:00 in four clinics.
- Management: CEO Shlomit Avraham; Chief Medical Officer Dr. Wasim Haddad; CIO Igor Shapiro; CFO Eyal
  Dahan; Legal counsel and Privacy Protection Officer Adv. Hagit Peretz; Head of Nursing Suha Nasser.
- Galil's mission statement: "Good medicine, in your language, close to home."
"""

DOCS["company/org-chart.md"] = """
# Galil Health — organization (HR summary, 1 November 2026)

| Unit | Head | Staff | Notes |
|---|---|---|---|
| Management | Shlomit Avraham, CEO | 6 | Reports to the board (9 directors) |
| Medical directorate | Dr. Wasim Haddad, CMO | 78 doctors (87 posts) + 4 regional medical leads | Wasim also works two days a week as a family doctor in Nazareth |
| Nursing | Suha Nasser, Head of Nursing | 42 nurses (44 posts) | Nurses run chronic-care clinics, triage and vaccinations |
| IT | Igor Shapiro, CIO | 11 | Notara administration (3), infrastructure (4), service desk (3), data and reporting (1) |
| Finance and procurement | Eyal Dahan, CFO | 14 | Procurement follows Galil's purchasing procedure (three quotes above ₪100,000) |
| Legal and privacy | Adv. Hagit Peretz | 2 | Hagit was appointed Privacy Protection Officer in August 2025 |
| Quality and patient safety | Dr. Ruth Golan, quality manager | 2 | Runs the incident-reporting system and the patient survey |
| Clinic operations | Five regional managers | about 330 | Reception, laboratory liaison, pharmacy liaison, facilities |

Staff committee (ועד עובדים): chair Fadi Saleh (laboratory). A collective agreement covers non-medical
and nursing staff; doctors are employed on personal contracts.

Regions: Western Galilee (Akko, Nahariya, Nahariya Child Development & Paediatrics); Karmiel–Misgav
(Karmiel, Majd al-Krum, Karmiel Women's Health); Nazareth (Nazareth, Nof HaGalil, Nazareth Diabetes &
Endocrine Centre); Upper Galilee (Safed, Hatzor HaGlilit); Kinneret (Tiberias, Maghar, Tiberias Cardiology
& Internal Medicine).
"""

DOCS["company/board-minutes-2026-10-21.md"] = """
# Galil Health — board of directors, minutes (extract)

Meeting of 21 October 2026. Present: nine directors; CEO; CFO; company secretary. Item 4 only.

**Item 4. Digital: AI documentation for clinicians (CEO)**

The CEO presented the plan to give "an ambient scribe to every doctor by Q2 2027". She reported on the
HIMSS conference visit in March and on ScribeWave, a US vendor "used in hundreds of hospitals", whose
published results show **98% transcription accuracy** and **two hours a day saved per doctor**. Four
vendors will demo between 26 October and 5 November. Doctors spend "about two hours a day on notes,
much of it in the evenings"; six doctors left in the last year and there are nine vacancies.

Dr. Nabil Zoabi (director, physician) asked whether the tools work in Arabic and Russian and with
relatives in the room. The CEO answered that ScribeWave supports more than 30 languages, including
Hebrew and Arabic. Mr. Eran Tal (director) asked about patient privacy. The CEO answered that the
contract will be reviewed "as usual" and that recordings will be protected.

The CEO noted that ScribeWave offered a year-end discount for a network-wide licence.

**Resolution:** The board approves a budget of up to ₪1.6M in 2027 for AI clinical documentation,
subject to the CEO's selection of a vendor, and asks for an update at the January meeting.
"""

DOCS["company/finance-summary.md"] = """
# Finance summary for the AI documentation project (CFO, 10 November 2026)

| Item | Value | Notes |
|---|---|---|
| Revenue 2025 | ₪318M | About 86% capitation from the two health funds |
| Doctor cost, fully loaded | ₪52,000 a month per full-time post | About ₪330 an hour at 157 paid hours |
| Nurse cost, fully loaded | ₪29,000 a month per full-time post | |
| Locum doctors | ₪2.1M in 2025; ₪1.71M January–September 2026 | Covers vacancies and sick leave; agency day rates |
| IT budget 2027 (draft) | ₪9.4M | Includes Notara licences ₪3.2M (renewal due July 2027) |
| Board line for AI documentation 2027 | Up to ₪1.6M | Subject to the CEO's selection (board, 21 Oct 2026) |
| Notara 7.4 → 9.2 upgrade, two regions | Estimated ₪420,000 and about 4 months | Not in the 2027 budget |

**How I look at projects.** Galil is paid per registered patient, not per visit. Time freed for doctors is
not cash unless it lets us fill a vacancy without a locum, avoid overtime, or add clinic sessions the
funds pay for. I count capacity separately from money, and I count money only with a named plan and a
date. Payback under two years preferred; anything above ₪300,000 goes to the board.

**Exchange rate.** Where a vendor prices in another currency, use the Bank of Israel representative
rate on the day of the quote.
"""

DOCS["it/cloud-committee-minutes-2022.md"] = """
# Organizational cloud committee — minutes

Meeting no. 1, 14 February 2022, 10:00, management meeting room, Karmiel.

Present: Igor Shapiro (CIO, chair); Adv. Lior Harari (then legal counsel); Yossi Ben-Haim (information
security officer); representative of the CEO. Absent: none.

1. The committee was established under the Ministry of Health director-general's circular on cloud
   computing in the health system (2/2021). The CEO's letter of appointment was read.
2. Draft cloud policy (IT, version 0.3) was presented. To be completed with legal comments and brought
   to management for approval at the next meeting.
3. Current cloud uses listed: e-mail (Microsoft 365), the appointment-reminder SMS service. Notara is
   hosted on premises in the Karmiel server room.
4. Next meeting: May 2022.

*Note added by IT, 3 January 2024:* "Yossi left in 2023; Lior left in 2024. Policy v0.3 still in draft.
No further meetings held. To be revived."
"""

DOCS["legal/health-fund-agreements-extract.md"] = """
# Service agreements with the health funds — extracts on information

Working copy prepared by the legal department for the consultant, 16 November 2026. The funds' names
are redacted in consultant copies. The Hebrew originals govern.

## Agreement with Fund A (2023–2028), Appendix D "Information and information security"

- **D.4** The Provider shall not engage any subcontractor or external party that will have access to
  medical information of the Fund's members, or that will process it on the Provider's behalf, without
  the Fund's **prior written approval**. The Fund shall respond to a complete request within **45 days**.
- **D.5** Medical information of the Fund's members shall be stored and processed **in Israel**, unless
  the Fund has approved otherwise in writing.
- **D.7** The Provider shall notify the Fund of any information-security incident involving members'
  information within **24 hours** of becoming aware of it.
- **D.9** The Provider shall comply with the Ministry of Health's directives on information security and
  cloud computing as they apply to it.

## Agreement with Fund B (2024–2027), section 18 "Confidentiality and information"

- **18.3** The Provider shall notify the Fund **30 days in advance** of engaging any external processor of
  members' medical information and shall provide the Fund, on request, with the agreement's information-
  security terms.
- **18.6** Security incidents: notification within 48 hours.
"""

DOCS["legal/notara-master-agreement-extract.md"] = """
# Notara master agreement (2019) — extract

Agreement between Galil Health and Notara Systems Ltd., signed 11 June 2019 (for Galil: Igor Shapiro,
CIO, and the then CEO). Term: renews every two years; next renewal July 2027.

- **7.2 Customer data.** All customer data remains the property of the Customer. The Supplier may use
  customer data, including in aggregated or de-identified form, **for the purpose of maintaining,
  supporting and improving its products and services**.
- **7.5 Location.** The Notara database is hosted on the Customer's premises. Cloud modules offered by the
  Supplier are hosted in Israel.
- **9.1 Add-on modules.** New modules released by the Supplier are offered under this agreement's terms.
- **12.3 Price.** The Supplier may update prices at each renewal with 90 days' notice.

*Legal department note (H.P., 16 Nov 2026): this agreement predates my time; I have no record of a legal
review in 2019. On 2 October 2026 Notara sent notice of a 9% price increase from July 2027.*
"""

DOCS["legal/patient-privacy-notice-2023.md"] = """
# Privacy notice for patients (website and clinic posters), version of March 2023

**How Galil Health protects your information**

Galil Health keeps your medical information confidential, as required by the Patient's Rights Law and the
Privacy Protection Law. We use your information to treat you, to coordinate your care with your health
fund and with hospitals, and to improve the quality of our services.

Your medical record is kept in Galil's computer systems. **Your medical information is stored on servers in
Israel.** Only staff who need it for your care can see it.

You may ask for a copy of your medical record at the reception desk of your clinic.

For questions: privacy@galil-health.example

*(Available in Hebrew, Arabic, Russian and English. Not updated since March 2023.)*
"""

DOCS["legal/staff-committee-agreement-extract.md"] = """
# Collective agreement, Galil Health and the staff committee (2022) — extract

Applies to nursing, laboratory, administrative and support staff (not doctors on personal contracts).

- **14.1 Technological change.** Management shall inform the staff committee in writing of any new system
  that records, monitors or measures employees' work, and hold a consultation meeting **at least 30 days
  before** it is introduced.
- **14.2** Information collected by such a system shall not be used for disciplinary purposes or in
  performance evaluation unless agreed in the consultation.
- **14.3** Employees shall receive training in working time on any new system they must use.
"""

DOCS["vendors/rfp-draft-v0.md"] = """
# Request for proposal — AI documentation (draft v0)

Igor Shapiro, CIO, 9 November 2026. Draft, not sent.

1. Galil Health invites proposals for an AI scribe for all doctors (78) and nurses (42).
2. Please describe your product and its main features.
3. What is your transcription accuracy (%)?
4. Which languages do you support?
5. Do you integrate with Notara?
6. References in Israel or abroad.
7. Price per user per month, and discounts for 120 users.
8. Implementation timeline.
9. Do you comply with Israeli privacy law? Please confirm in writing.
10. Proposals by 30 November 2026. Decision by 15 December 2026.
"""

DOCS["vendors/scribewave-deck.md"] = """
# ScribeWave — "Give your doctors their evenings back" (deck presented 26 October 2026, extract)

Presented by Yoni Mizrahi, Account Executive, MedLink Systems (ScribeWave's authorised reseller in Israel).

- **Slide 2.** Trusted by hundreds of hospitals and health systems in the US and Europe.
- **Slide 4.** **98% transcription accuracy.** *Footnote: internal benchmark, 200 scripted English
  outpatient visits (orthopaedics, dermatology, urgent care), recorded with a studio microphone, one speaker
  at a time, US accents. Word accuracy on the transcript, not on the note.*
- **Slide 5.** **Saves doctors 2 hours a day.** *Footnote: survey of 60 early-adopter physicians at two US
  health systems, 2025; self-reported time saved.*
- **Slide 6.** **30+ languages, including Hebrew and Arabic.** *Footnote: Hebrew model in beta. Language
  support measured on read-aloud text. Arabic: Modern Standard and Gulf.*
- **Slide 8.** Structured note with suggested billing codes in seconds.
- **Slide 9.** Security: independent audit report available under NDA.
- **Slide 11.** Year-end offer: network licence, 12% discount if signed by 31 December 2026.
"""

DOCS["vendors/scribewave-quote-2026-11.md"] = """
# Quote Q-GH-2611 — ScribeWave for Galil Health

MedLink Systems Ltd. (authorised reseller), 4 November 2026. Valid until 31 December 2026.

| Item | Quantity | Unit price | Annual |
|---|---|---|---|
| ScribeWave Clinician licence, **Standard plan**, per clinician per month | 120 | ₪1,150 | ₪1,656,000 |
| Year-end network discount (signature by 31 Dec 2026) | | −12% | −₪198,720 |
| Onboarding and training (remote) | 1 | included | — |
| **Total, year 1 (excl. VAT)** | | | **₪1,457,280** |

Terms: three-year term; annual list-price changes apply from year 2; ScribeWave standard terms and data-
processing agreement apply (attached). Integration with Notara: through ScribeWave's standard HL7 FHIR
connector; any customer-side work is the customer's.
"""

DOCS["vendors/scribewave-dpa-extract.md"] = """
# ScribeWave data-processing agreement (standard plan) — extract

- **3.2 Service improvement.** ScribeWave may use **de-identified** customer data, including audio,
  transcripts and notes, to develop and improve its services and models. Customers on the **Enterprise
  plan** may opt out in writing.
- **4.1 Retention.** Audio recordings are retained for **90 days** after the encounter for quality and
  dispute resolution, then deleted.
- **5.1 Location.** Customer data is hosted in the European Union or the United States, at ScribeWave's
  choice.
- **6.1 Sub-processors.** A list is published on ScribeWave's website; customers are notified 30 days
  before changes.
- **8.4 Models.** ScribeWave continuously improves its models; updates apply automatically.
"""

DOCS["vendors/kolrefua-deck.md"] = """
# Kol Refua (קול רפואה) — "Hebrew medicine, understood" (deck, 28 October 2026, extract)

- **Slide 2.** Israeli start-up, founded 2023, 30 people, offices in Haifa.
- **Slide 3.** **96% accuracy in Hebrew.** *Measured by Kol Refua on 40 visits at our partner clinic
  (two family doctors, Hebrew only), July 2026.*
- **Slide 4.** Understands Israeli medical slang and drug brand names.
- **Slide 5.** **Your data never leaves Israel.** Hosted on an Israeli cloud.
- **Slide 6.** Roadmap: **Arabic next quarter**, Russian improvements.
- **Slide 7.** Pricing from ₪600 per clinician per month; three-year price lock available.
"""

DOCS["vendors/kolrefua-dpa-extract.md"] = """
# Kol Refua data-processing agreement — extract with Annex B

- **2.1** Kol Refua will not use customer data to train or improve its models.
- **4.2** Audio is deleted 7 days after the note is created.
- **5.1** The service is hosted in Israel.

**Annex B — Sub-processors**

| Sub-processor | Service | Location |
|---|---|---|
| (Israeli cloud host) | Application hosting, database | Israel |
| (US speech-recognition API provider) | Speech-to-text for audio streams | United States |
| (E-mail service) | Notifications | EU |
"""

DOCS["vendors/kolrefua-partner-letter.md"] = """
# Letter of recommendation (translated from Hebrew)

From the medical director of a family-medicine clinic in Haifa, 20 September 2026.

"We have used Kol Refua for three months. Our doctors love it: it understands how we really talk. I
recommend it warmly to any clinic in Israel."

*Kol Refua's investor list (published on its website): includes the clinic's holding company.*
"""

DOCS["vendors/mednote-release-notes.md"] = """
# Notara 9.2.3 release notes — MedNote module (extract, 15 September 2026)

- **New: MedNote Ambient (preview).** Listens to the visit and drafts the note into Notara fields.
  Available on Notara 9.2 and later. **Preview feature:** behaviour may change between releases.
- MedNote Dictation (since 2024): **95% accurate** on dictated notes (single clinician speaking to the
  microphone; Notara internal test, Hebrew).
- Notara 7.x is not supported for MedNote. Customers on 7.x should upgrade to 9.2.
"""

DOCS["vendors/mednote-offer.md"] = """
# Offer letter — MedNote for Notara (Notara Systems Ltd., 3 November 2026)

"As a valued Notara customer, Galil Health may use MedNote Ambient **free of charge until 31 December
2027** for all clinicians on Notara 9.2. Pricing from 2028 will be agreed with you. MedNote is provided
under your existing master agreement. **Zero integration effort**: the note lands directly in Notara."
"""

DOCS["vendors/rishma-deck.md"] = """
# Rishma Health — deck (5 November 2026, extract)

- **Slide 2.** European specialist in clinical speech, 200 people, in production in nine countries.
  In Israel: three clinics for 14 months (references on request).
- **Slide 3.** **Leaves out a clinically relevant fact in 2.1% of notes.** *Independent evaluation by a
  university hospital, 1,200 primary-care visits in four languages including Arabic, real rooms, every
  note reviewed by a clinician (summary attached).*
- **Slide 4.** Marks passages it is unsure of; the clinician must confirm each one before signing.
- **Slide 5.** Saves **40–70 minutes a day**. *Time-and-motion study within the same evaluation, with a
  comparison group.*
- **Slide 6.** Hebrew in production; Russian evaluated on 150 visits.
- **Slide 8.** Data: no training without opt-in; audio deleted after 30 days; EU hosting by default,
  Israel hosting available.
- **Slide 9.** Integration: through the record system's interface (for Notara, a project of about three
  months).
- **Slide 10.** About ₪1,300 per clinician a month.
"""

DOCS["vendors/rishma-evaluation-summary.md"] = """
# Independent evaluation of Rishma Health — summary (university hospital evaluation unit, 2025)

**Design.** 1,200 consecutive consented primary-care visits in four languages (including Arabic, 280
visits), recorded in ordinary consultation rooms, 31 clinicians. Every draft note compared by a second
clinician with the recording. Time-and-motion sub-study: 24 clinicians with the tool against 22 without.

**Results.**

| Measure | Result |
|---|---|
| Notes with at least one clinically relevant omission | 2.1% (95% CI 1.4–3.0%) |
| Notes with an invented finding | 0.6% |
| Omissions inside a passage the tool marked "unsure" | 71% |
| Documentation time per clinician-day vs comparison group | −52 minutes (range 40–70) |

**Limits stated by the authors.** One health system; consenting clinicians may be more enthusiastic;
Hebrew not included in this evaluation; results apply to the model version evaluated (v3.2).
"""

DOCS["vendors/rishma-safety-case-extract.md"] = """
# Rishma Health — clinical safety case and hazard log (extract)

| Hazard | Cause | Control | Residual risk |
|---|---|---|---|
| H-01 Omission of a clinically relevant fact | Overlapping speech, relatives, noise | Unsure-passage marking; clinician confirms before signing; omission rate monitored per site | Medium → low with confirmation |
| H-02 Wrong patient | Note started on the wrong record | Patient identity confirmed from the record system before recording | Low |
| H-03 Wrong drug or dose | Similar-sounding drug names | Drug names checked against the national formulary; dose never inferred | Low |
| H-04 Invented finding | Model generation | Findings only from transcript spans; span shown on click | Low |
| H-05 Model change alters behaviour | New model version | Customer notice; re-run on customer test set before release | Low |

Named clinical safety officer: a physician on Rishma's staff (name in the contract).
"""

DOCS["vendors/rishma-dpa-extract.md"] = """
# Rishma Health data-processing agreement — extract

- **3.1** No use of customer data to train or improve models unless the customer opts in in writing.
- **4.1** Audio deleted 30 days after the note is signed; transcripts deleted with the audio unless the
  customer instructs otherwise.
- **5.1** Hosting in the EU by default; **hosting in Israel available** (price schedule).
- **6.1** Full sub-processor list (Annex 2); 60 days' notice of changes; customer may object and terminate.
- **9.1** Exit: data returned in a standard format; certified deletion; six months' transition assistance.
"""

POC_README = """
# Proof of concept — Galil Health ambient scribe (December 2026)

These files are the result of the proof of concept run in lesson 10.4. Open them after you have written
your own PoC protocol: they show what Galil's run produced.

## How it was run

- **Visits.** 90 synthetic visits, 30 in Hebrew, 30 in Arabic, 30 in Russian, written by the CMO's team from
  real-shaped scenarios (primary care and the four specialist centres) and recorded by drama students
  playing doctors, patients and relatives in two of Galil's consultation rooms, 8–10 December 2026. No real
  patient took part. `visits-90.csv` lists them.
- **Runs.** Each vendor received the 90 recordings under an NDA for synthetic data and processed each one
  **twice** (13–20 December), so each vendor produced 180 notes. Kol Refua returned empty notes for every
  Arabic recording.
- **Review.** Six clinicians, two per language, compared every note with the script's fact list
  (21–30 December), blind to the vendor where the format allowed. `review-sheet.csv` has one row per note.
- **RFP answers.** `rfp-responses.csv` holds each vendor's answer to every contract term in the RFP
  (received by 20 December).

## Columns of `review-sheet.csv`

| Column | Meaning |
|---|---|
| `vendor`, `poc_visit_id`, `run`, `language` | Which note |
| `status` | `scored` or `no_output` |
| `wer_pct` | Word error rate of the vendor's transcript against the script, % |
| `facts_total` | Clinically relevant facts in the script's fact list |
| `omitted_relevant` | Facts from the list missing or wrong in the note |
| `invented` | Findings in the note that were not said in the visit |
| `omissions_flagged` | Omissions that sat inside a passage the tool had marked "unsure" |
| `passages_flagged` | Passages the tool marked "unsure" in this note |
| `minutes_to_correct` | Reviewer's timed minutes to bring the note to a signable state |
| `reviewer_id`, `reviewer_note` | Who reviewed it; a short note |

Rates "per 100 notes" are counts divided by the notes the vendor produced, times 100.
"""


# ---------------------------------------------------------------- main


def main() -> None:
    clinicians = build_clinicians()
    doctor_days, visits = build_visits(clinicians)

    write_csv(HERE / "company/clinics.csv",
              ["clinic_id", "name", "region", "type", "notara_version", "doctors", "nurses", "main_patient_languages"],
              [[c[0], c[1], c[2], c[3], c[4], c[5], c[6],
                ";".join(k for k, v in sorted(c[7].items(), key=lambda kv: -kv[1]) if v >= 0.2)] for c in CLINICS])
    write_csv(HERE / "people/clinicians.csv",
              ["clinician_id", "role", "clinic_id", "specialty", "fte", "languages", "start_year"], clinicians)
    write_csv(HERE / "people/clinician-survey-2026-10.csv",
              ["response_id", "submitted_at", "role", "region", "years_at_galil", "documentation_minutes_per_day",
               "evenings_finishing_notes_per_week", "interpreting_minutes_per_day", "would_use_scribe_1to5",
               "main_concern", "tools_used_for_notes", "comment"], build_survey(clinicians))
    write_csv(HERE / "notara/visits-sample.csv",
              ["visit_id", "clinic_id", "clinician_id", "visit_date", "slot_start_at", "slot_minutes", "visit_type",
               "patient_age_band", "patient_pref_language", "visit_language", "relative_present", "interpreter",
               "note_opened_at", "note_signed_at", "note_active_sec", "after_hours_sec", "note_chars", "referral_letter"],
              visits)
    write_csv(HERE / "notara/doctor-days.csv", ["clinician_id", "date", "session", "visits"], doctor_days)
    write_csv(HERE / "notara/mednote-dictation-trial-2025.csv",
              ["week_start_date", "trial_week", "clinician_id", "clinic_id", "visits", "notes_dictated", "avg_correction_sec"],
              build_trial(clinicians))
    write_csv(HERE / "quality/patient-safety-incidents.csv",
              ["incident_id", "reported_date", "clinic_id", "category", "severity", "description", "description_en"],
              build_incidents())
    write_csv(HERE / "it/proxy-ai-summary-2026-10.csv",
              ["week_start_date", "clinic_id", "network", "application", "category", "sessions", "upload_mb", "distinct_devices"],
              build_proxy())
    write_csv(HERE / "vendors/demo-day-scorecards.csv",
              ["demo_date", "vendor", "demo_language", "demo_setup", "rater_id", "rater_role", "criterion", "score_1to5", "comment"],
              build_scorecards())

    for rel, text in DOCS.items():
        write_md(HERE / rel, text)
    write_md(HERE / "company/kpi-report-2026-q3.md", kpi_report(visits, doctor_days))

    poc_visits, sheet = build_poc()
    write_csv(POC / "visits-90.csv",
              ["poc_visit_id", "language", "setting", "scenario", "speakers", "relative_present", "noise", "variety",
               "facts_total", "hard_case"], poc_visits)
    write_csv(POC / "review-sheet.csv",
              ["vendor", "poc_visit_id", "run", "language", "status", "wer_pct", "facts_total", "omitted_relevant",
               "invented", "omissions_flagged", "passages_flagged", "minutes_to_correct", "reviewer_id", "reviewer_note"], sheet)
    write_csv(POC / "rfp-responses.csv", ["vendor", "term_id", "term", "must_have", "reply", "note"], build_rfp_responses())
    write_md(POC / "sample-notes.md", tb.SAMPLE_NOTES)
    write_md(POC / "README.md", POC_README)
    print(f"Wrote {len(visits)} sampled visits, {len(doctor_days)} doctor-days, {len(sheet)} PoC review rows.")


if __name__ == "__main__":
    main()
