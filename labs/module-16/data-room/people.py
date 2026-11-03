"""Staff, volunteers, the one-week time log and the staff AI survey."""
from __future__ import annotations

from datetime import date, timedelta

import textbank as tb
from common import DOMAIN, ROOM, pick, rand_date, rng, write_csv

# staff_id, name, role, team, fte, languages, started, email local part, employment
STAFF = [
    ("S01", "Dr. Ronit Azoulay", "Executive director", "Management", 1.0, "he,en,fr", "2016-09-01", "ronit.a", "employee"),
    ("S02", "Noa Ben-Ami", "Head of development", "Development", 1.0, "he,en", "2019-03-10", "noa.b", "employee"),
    ("S03", "Shira Levin", "Development coordinator (grants and reports)", "Development", 0.6, "he,en", "2023-01-15", "shira.l", "employee"),
    ("S04", "Michael Cohen", "Donor relations and events", "Development", 0.5, "he,en", "2022-05-01", "michael.c", "employee"),
    ("S05", "Yossi Mizrahi", "Office and operations manager (IT one day a week)", "Operations", 1.0, "he", "2017-02-01", "yossi.m", "employee"),
    ("S06", "Galina Petrova", "Bookkeeper", "Operations", 0.6, "ru,he", "2018-07-01", "galina.p", "employee"),
    ("S07", "Hana Golan", "Head of family services (social worker)", "Family services", 1.0, "he,en", "2014-10-01", "hana.g", "employee"),
    ("S08", "Samah Khatib", "Senior family coordinator (social worker), Arabic desk", "Family services", 0.8, "ar,he,en", "2017-11-01", "samah.k", "employee"),
    ("S09", "Yarden Avraham", "Family coordinator (social worker)", "Family services", 0.8, "he,en", "2021-04-01", "yarden.a", "employee"),
    ("S10", "Marina Kogan", "Family coordinator (social worker), Russian desk", "Family services", 0.8, "ru,he", "2019-09-01", "marina.k", "employee"),
    ("S11", "Tigist Alemu", "Family coordinator (social worker), Amharic desk", "Family services", 0.6, "am,he", "2022-02-01", "tigist.a", "employee"),
    ("S12", "Oren Biton", "Family coordinator (social worker)", "Family services", 0.8, "he", "2023-08-01", "oren.b", "employee"),
    ("S13", "Rasha Abu-Ahmad", "Family coordinator (social worker), Shefa-'Amr", "Family services", 0.8, "ar,he", "2020-01-01", "rasha.a", "employee"),
    ("S14", "Eli Dahan", "Rights advisor", "Family services", 0.5, "he", "2021-10-01", "eli.d", "employee"),
    ("S15", "Sveta Ivanova", "Intake coordinator", "Family services", 0.5, "ru,he,en", "2024-03-01", "sveta.i", "employee"),
    ("S16", "Fatma Zoabi", "Rights hotline worker", "Family services", 0.6, "ar,he", "2023-11-01", "fatma.z", "employee"),
    ("S17", "Nurit Sasson", "Parent groups coordinator", "Programmes", 0.5, "he", "2018-05-01", "nurit.s", "employee"),
    ("S18", "Liat Ohana", "Volunteer coordinator", "Programmes", 0.75, "he,en", "2020-06-01", "liat.o", "employee"),
    ("S19", "Amir Saleh", "Respite programme manager", "Programmes", 0.8, "ar,he,en", "2019-01-01", "amir.s", "employee"),
    ("S20", "Hadas Mor", "Siblings programme coordinator", "Programmes", 0.5, "he", "2022-09-01", "hadas.m", "employee"),
    ("S21", "Maya Ronen", "Communications and social media", "Development", 0.5, "he,en", "2024-01-01", "maya.r", "employee"),
    ("S22", "Mona Haj", "Office assistant, Shefa-'Amr room", "Operations", 0.5, "ar,he", "2025-02-01", "mona.h", "employee"),
    ("S23", "Daniel Tesfaye", "Respite counsellor", "Programmes", 0.3, "am,he", "2024-09-01", "daniel.t", "employee"),
    ("S24", "Yulia Smirnova", "Respite counsellor", "Programmes", 0.3, "ru,he", "2025-01-01", "yulia.s", "employee"),
    ("S25", "Lior Ben-Haim", "Respite counsellor", "Programmes", 0.3, "he", "2023-06-01", "lior.bh", "employee"),
    ("S26", "Nadine Shehadeh", "Respite counsellor", "Programmes", 0.3, "ar,he", "2024-06-01", "nadine.s", "employee"),
    ("S27", "Itai Golan", "Group facilitator (parent groups)", "Programmes", 0.4, "he", "2025-03-01", "itai.g", "employee"),
    ("S28", "Ruth Mekonen", "Group facilitator (parent groups)", "Programmes", 0.4, "am,he", "2025-03-01", "ruth.m", "employee"),
    ("S29", "Tehila Katz", "National-service volunteer (office and intake)", "Operations", 1.0, "he", "2026-09-01", "ns1", "national_service"),
    ("S30", "Avigail Dror", "National-service volunteer (respite and events)", "Programmes", 1.0, "he", "2026-09-01", "ns2", "national_service"),
]

# Former staff whose Workspace accounts were never suspended.
FORMER = [("X01", "Dana Klein", "Family coordinator (left 2025-03-31)", "dana.k"),
          ("X02", "Moshe Amar", "Development coordinator (left 2025-08-14)", "moshe.a")]

COORDINATORS = ["S08", "S09", "S10", "S11", "S12", "S13"]


def email(local: str) -> str:
    return f"{local}@{DOMAIN}"


def write_staff() -> list[tuple]:
    rows = [[s[0], s[1], s[2], s[3], s[4], s[5], s[6], email(s[7]), s[8]] for s in STAFF]
    write_csv(ROOM / "people" / "staff.csv",
              ["staff_id", "name", "role", "team", "fte", "languages", "started", "email", "employment"], rows)
    return STAFF


def build_volunteers() -> list[dict]:
    r = rng("volunteers")
    vols = []
    domains = {"gmail.com": 70, "walla.co.il": 10, "hotmail.com": 8, "yahoo.com": 4, "icloud.com": 4, "bezeqint.net": 4}
    progs = {"respite": 42, "siblings": 14, "events": 18, "phone-a-thon": 10, "office": 6, "parent-group childcare": 10}
    for i in range(1, 143):
        vid = f"V{i:03d}"
        prog = pick(r, progs)
        joined = rand_date(r, date(2016, 1, 1), date(2026, 9, 30))
        active = r.random() < 0.67 or joined > date(2025, 6, 30)
        if vid == "V001":   # Etti Peretz
            prog, joined, active = "respite", date(2012, 5, 1), True
        last = rand_date(r, date(2026, 6, 1), date(2026, 11, 10)) if active else \
            rand_date(r, max(joined, date(2022, 1, 1)), date(2025, 12, 31))
        vols.append(dict(id=vid, programme=prog, joined=joined, active=active, last=last,
                         domain="gmail.com" if vid == "V001" else pick(r, domains),
                         langs=pick(r, {"he": 55, "he,en": 15, "ar,he": 14, "ru,he": 10, "am,he": 3, "en": 3}),
                         conf=None, clearance=None, folder_access=False))
    # Drive access to the respite folder: 15 active respite leads + 23 inactive people who once ran weekends.
    act_resp = [v for v in vols if v["active"] and v["programme"] == "respite"]
    inact = [v for v in vols if not v["active"]]
    r.shuffle(act_resp)
    r.shuffle(inact)
    for v in act_resp[:15] + inact[:23]:
        v["folder_access"] = True
    for v in vols:
        if v["id"] == "V001":
            v["folder_access"] = True
    # Confidentiality forms: older volunteers often never signed; 19 of those with access lack one.
    with_access = [v for v in vols if v["folder_access"]]
    r.shuffle(with_access)
    no_form = {v["id"] for v in with_access[:19] if v["id"] != "V001"}
    for v in vols:
        if v["id"] in no_form:
            v["conf"] = ""
        else:
            v["conf"] = "y" if (v["joined"] >= date(2020, 1, 1) or r.random() < 0.6) else ""
        v["clearance"] = "y" if v["programme"] in ("respite", "siblings", "parent-group childcare") else "n/a"
    return vols


def write_volunteers(vols: list[dict]) -> None:
    rows = [[v["id"], v["programme"], "active" if v["active"] else "inactive", v["joined"].isoformat(),
             v["last"].isoformat(), v["domain"], v["langs"], v["conf"], v["clearance"]] for v in vols]
    write_csv(ROOM / "people" / "volunteers.csv",
              ["volunteer_id", "programme", "status", "joined", "last_activity", "email_domain", "languages",
               "confidentiality_signed", "minors_clearance_on_file"], rows)


# Hours in the logged week (Sun 4 - Thu 8 Oct 2026, the week before the Q3 Adler-Haddad report was due).
COORD_PLAN = {"family_contact": 9.0, "home_visit": 6.0, "travel": 3.0, "case_notes": 4.8,
              "funder_report_adler_haddad": 6.5, "other_funder_report": 0.7, "team_meeting": 2.0, "admin": 1.5}
PLANS = {
    "S01": {"meetings": 12, "funder_report_adler_haddad": 2.5, "grant_proposal": 3, "donor_comms": 6, "board": 3,
            "supervision": 6, "admin": 8, "newsletter": 2, "other": 2.5},
    "S02": {"grant_proposal": 9.5, "other_funder_report": 6.5, "funder_report_adler_haddad": 5.5, "donor_comms": 10,
            "events": 4, "meetings": 4, "admin": 2.5},
    "S03": {"other_funder_report": 8, "funder_report_adler_haddad": 7, "grant_proposal": 5, "admin": 3, "meetings": 2},
    "S07": {"supervision": 10, "case_review": 6, "funder_report_adler_haddad": 5, "meetings": 8, "admin": 6,
            "family_contact": 5},
}
DAYS = [date(2026, 10, 4) + timedelta(days=i) for i in range(5)]


def build_time_log() -> list[list]:
    r = rng("timelog")
    rows = []
    people = ["S01", "S02", "S03", "S07"] + COORDINATORS
    for sid in people:
        plan = dict(PLANS.get(sid, COORD_PLAN))
        if sid in COORDINATORS:
            plan["translation_letters"] = 1.6 if sid in ("S08", "S10", "S11", "S13") else 0.3
            scale = 0.75 if sid == "S11" else 1.0
            plan = {k: v * scale * r.uniform(0.85, 1.15) for k, v in plan.items()}
            if sid == "S08":
                plan["funder_report_adler_haddad"] = 7.4   # Samah also translates colleagues' Arabic notes
        chunks = []
        for act, hours in plan.items():
            left = int(round(hours * 60 / 15)) * 15
            while left > 0:
                m = min(left, r.choice([30, 45, 60, 60, 90, 120]))
                chunks.append((act, m))
                left -= m
        r.shuffle(chunks)
        per_day = [[] for _ in DAYS]
        for i, c in enumerate(chunks):
            per_day[i % 5].append(c)
        for d, day_chunks in zip(DAYS, per_day):
            t = 8 * 60 + r.choice([0, 15, 30])
            for act, m in day_chunks:
                note = tb.timelog_note(r, act)
                rows.append([sid, d.isoformat(), f"{t // 60:02d}:{t % 60:02d}", m, act, note])
                t += m + r.choice([0, 0, 15])
    write_csv(ROOM / "people" / "time-log-2026-10.csv",
              ["staff_id", "date", "start", "minutes", "activity", "note"], rows)
    return rows


def build_survey() -> list[list]:
    """The ED's own Google Form, 26 Oct 2026 (22 of 30 staff answered; volunteers were not asked)."""
    r = rng("survey")
    rows = []
    groups = (["family services"] * 9 + ["development and comms"] * 5 + ["programmes"] * 5 +
              ["operations and management"] * 3)
    pasted = ["no"] * 11 + ["yes, anonymised"] * 4 + ["yes, with details"] * 3 + ["prefer not to say"] * 4
    r.shuffle(pasted)
    for i, g in enumerate(groups):
        freq = pick(r, {"never": 5, "a few times": 6, "weekly": 6, "daily": 5})
        if freq == "never":
            tools, account, tasks, p = "", "", "", "no"
        else:
            tools = ";".join(sorted(set(r.sample(tb.SURVEY_TOOLS[g], r.choice([1, 1, 2, 2])))))
            account = pick(r, {"personal": 9, "work (openhands)": 3, "both": 3, "don't know": 3})
            tasks = ";".join(sorted(set(r.sample(tb.SURVEY_TASKS[g], r.choice([1, 2, 3])))))
            p = pasted[i]
        if freq == "never" and pasted[i] != "no":
            p = "no"
        rows.append([f"R{i + 1:02d}", "2026-10-26", g, freq, tools, account, tasks, p,
                     pick(r, {"yes": 15, "no": 3, "maybe": 4}), tb.survey_freetext(r, g)])
    # Make sure the planted counts hold: 3 "with details", 4 "prefer not to say" among users.
    users = [row for row in rows if row[3] != "never"]
    want = ["yes, with details"] * 3 + ["prefer not to say"] * 4 + ["yes, anonymised"] * 4
    for row, val in zip(users, want + ["no"] * (len(users) - len(want))):
        row[7] = val
    for row in rows:
        if row[7] == "yes, with details" and "personal" not in row[5] and row[5] != "both":
            row[5] = "personal"
    write_csv(ROOM / "it" / "staff-ai-survey-2026-10.csv",
              ["response_id", "date", "team", "how_often_ai", "tools", "account_type", "tasks",
               "pasted_family_information", "want_training", "biggest_time_drain"], rows)
    return rows
