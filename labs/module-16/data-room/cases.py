"""Case register (active families) and the pseudonymised case-notes sample."""
from __future__ import annotations

from datetime import date, timedelta

import textbank as tb
from common import EXPORT_DAY, ROOM, pick, rand_date, rng, write_csv
from people import COORDINATORS

TOWNS = {"Kiryat Ata": 70, "Haifa": 80, "Kiryat Bialik": 40, "Kiryat Motzkin": 35, "Acre": 40, "Shefa-'Amr": 55,
         "Tamra": 35, "Nesher": 18, "Kiryat Hadas": 65}
ARAB_TOWNS = {"Shefa-'Amr", "Tamra"}
ADAM = "OH-F0217"
N_FAMILIES = 438


def coordinator_for(r, lang: str, town: str) -> str:
    if lang == "ar":
        return "S13" if town in ARAB_TOWNS and r.random() < 0.55 else "S08"
    if lang == "ru":
        return "S10"
    if lang == "am":
        return "S11"
    return r.choice(["S09", "S12", "S09", "S12", "S08"])


def build_cases() -> list[dict]:
    r = rng("cases")
    fams = []
    for i in range(1, N_FAMILIES + 1):
        fid = f"OH-F{i:04d}"
        town = pick(r, TOWNS)
        if town in ARAB_TOWNS:
            lang = pick(r, {"ar": 92, "he": 8})
        elif town == "Acre":
            lang = pick(r, {"ar": 40, "he": 45, "ru": 15})
        else:
            lang = pick(r, {"he": 62, "ru": 18, "am": 9, "ar": 8, "en": 3})
        intake = rand_date(r, date(2012, 1, 1), date(2026, 10, 31))
        if intake < date(2023, 3, 1):
            consent = pick(r, {"v1-2019": 93, "missing": 7}) if intake >= date(2019, 1, 1) else \
                pick(r, {"v1-2019": 85, "missing": 15})
        else:
            consent = pick(r, {"v2-2023": 90, "v1-2019": 7, "missing": 3})
        if consent == "v2-2023":
            stories, photos = pick(r, {"y": 55, "n": 45}), pick(r, {"y": 40, "n": 60})
        else:
            stories, photos = "", ""
        age = pick(r, {"0-5": 22, "6-12": 41, "13-17": 25, "18-21": 12})
        group = pick(r, {"autism / developmental": 34, "intellectual": 14, "physical (incl. CP)": 16,
                         "sensory (hearing/vision)": 7, "genetic syndrome": 11, "multiple / complex medical": 18})
        referred = "Kiryat Hadas welfare" if town == "Kiryat Hadas" and r.random() < 0.8 else \
            pick(r, {"self / parent": 45, "hospital": 15, "school": 14, "welfare office": 16, "other family": 10})
        welfare = "y" if referred in ("Kiryat Hadas welfare", "welfare office") or r.random() < 0.18 else "n"
        progs = ["coordination"]
        if r.random() < 0.38:
            progs.append("respite")
        if r.random() < 0.18:
            progs.append("siblings")
        if r.random() < 0.30:
            progs.append("parent group")
        last = EXPORT_DAY - timedelta(days=int(r.expovariate(1 / 25)))
        fams.append(dict(id=fid, coord=coordinator_for(r, lang, town), town=town, lang=lang, age=age, group=group,
                         welfare=welfare, referred=referred, progs=progs, intake=intake, consent=consent,
                         stories=stories, photos=photos, ah="n", last=max(last, intake)))
    # Adam's family: Shefa-'Amr, Arabic, consent v1, genetic syndrome, coordination + respite, Samah.
    a = fams[216]
    a.update(id=ADAM, coord="S08", town="Shefa-'Amr", lang="ar", age="6-12", group="genetic syndrome",
             progs=["coordination", "respite"], intake=date(2021, 2, 14), consent="v1-2019", stories="", photos="",
             referred="hospital", welfare="n")
    # The Adler-Haddad grant funds coordination for families with children under 13 (first 120 by intake).
    elig = sorted([f for f in fams if f["age"] in ("0-5", "6-12")], key=lambda f: f["intake"])
    for f in elig[-120:]:
        f["ah"] = "y"
    a["ah"] = "y"
    return fams


def write_cases(fams: list[dict]) -> None:
    rows = [[f["id"], f["coord"], f["town"], f["lang"], f["age"], f["group"], f["welfare"], f["referred"],
             ";".join(f["progs"]), f["intake"].isoformat(), f["consent"], f["stories"], f["photos"], f["ah"],
             f["last"].isoformat()] for f in fams]
    write_csv(ROOM / "cases" / "case-register.csv",
              ["family_id", "coordinator_id", "town", "home_language", "child_age_band", "disability_group",
               "welfare_involved", "referred_by", "programmes", "intake_date", "consent_version",
               "consent_stories", "consent_photos", "adler_haddad_grant", "last_contact"], rows)


def build_notes(fams: list[dict]) -> list[list]:
    r = rng("notes")
    rows = []
    pool = [f for f in fams if f["coord"] in COORDINATORS]
    leak_at = set(r.sample(range(60), len(tb.LEAKS)))
    leaks = list(tb.LEAKS)
    for i in range(60):
        f = r.choice(pool)
        leak = None
        if i in leak_at:
            leak = leaks.pop()
            f = r.choice([x for x in pool if x["lang"] == leak[0]])
        lang = f["lang"] if f["lang"] in ("he", "ar", "ru") else ("en" if r.random() < 0.5 else "he")
        if f["coord"] in ("S09", "S12") and r.random() < 0.3:
            lang = "en"
        age = {"0-5": r.randint(2, 5), "6-12": r.randint(6, 12), "13-17": r.randint(13, 17),
               "18-21": r.randint(18, 21)}[f["age"]]
        parts = [r.choice(tb.NOTE_OPEN[lang]), r.choice(tb.NOTE_BODY[lang]).format(age=age)]
        if r.random() < 0.6:
            parts.append(r.choice(tb.NOTE_BODY[lang]).format(age=age))
        parts.append(r.choice(tb.NOTE_NEXT[lang]))
        if leak:
            parts.insert(2, leak[1])
        d = rand_date(r, date(2026, 9, 1), date(2026, 11, 5))
        while d.weekday() in (4, 5):
            d += timedelta(days=1)
        kind = pick(r, {"phone": 45, "home visit": 30, "office meeting": 12, "committee prep": 8, "rights": 5})
        mins = max(5, int(r.gauss(14 if kind == "phone" else 24, 6)))
        rows.append([f"N{i + 1:03d}", f["id"], f["coord"], d.isoformat(), lang, kind, mins, " ".join(parts)])
    rows.sort(key=lambda x: (x[3], x[0]))
    write_csv(ROOM / "cases" / "case-notes-sample.csv",
              ["note_id", "family_id", "coordinator_id", "date", "language", "note_type", "minutes_writing", "text"],
              rows)
    return rows
