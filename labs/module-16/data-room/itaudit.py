"""Google Drive sharing audit exported by Yossi from the Workspace admin console on 12 Nov 2026."""
from __future__ import annotations

from datetime import date

from common import DOMAIN, LINK_SHARED_ON, ROOM, rand_date, rng, write_csv
from people import COORDINATORS, FORMER, STAFF

S = {s[0]: f"{s[7]}@{DOMAIN}" for s in STAFF}
FOUNDATION = "tamar.wl@adler-haddad-foundation.org.il"


def vol_email(v: dict) -> str:
    return f"{v['id'].lower()}.vol@{v['domain']}"


def build_audit(vols: list[dict]) -> list[list]:
    r = rng("audit")
    rows = []

    def add(path, kind, owner, who, ptype, role, link="off", modified="", changed=""):
        rows.append([path, kind, owner, who, ptype, role, link, modified, changed])

    fam = "Shared drives/Families"
    fam_owner = S["S07"]
    # Families: 11 current staff + 2 national service + 2 former staff + volunteers (personal accounts)
    fam_staff = ["S01", "S07"] + COORDINATORS + ["S14", "S15", "S16"]
    for sid in fam_staff:
        add(fam, "shared drive", fam_owner, S[sid], "org user", "content manager" if sid in ("S01", "S07") else
            "contributor", "off", "2026-11-11", "")
    for sid in ("S29", "S30"):
        add(fam, "shared drive", fam_owner, S[sid], "org user", "contributor", "off", "2026-11-10", "2026-09-04")
    for f in FORMER:
        add(fam, "shared drive", fam_owner, f"{f[3]}@{DOMAIN}", "org user (former staff)", "contributor", "off",
            "2026-11-11", "")
    etti = [v for v in vols if v["id"] == "V001"][0]
    add(fam, "shared drive", fam_owner, vol_email(etti), "external personal", "contributor", "off", "2026-11-11",
        "2019-06-02")
    with_access = [v for v in vols if v["folder_access"] and v["id"] != "V001"]
    # 7 active respite leads were added at the top level "so they can find the care sheets"
    top_level = [v for v in with_access if v["active"]][:7] + [v for v in with_access if not v["active"]]
    for v in top_level:
        add(fam, "shared drive", fam_owner, vol_email(v), "external personal", "viewer", "off", "2026-11-11",
            rand_date(r, date(2021, 1, 1), date(2025, 12, 1)).isoformat())
    # Sub-folders
    for sub, kind in (("Intake 2026", "folder"), ("Case notes 2026", "folder"), ("Welfare referrals - Kiryat Hadas",
                                                                                "folder"), ("Committee letters", "folder")):
        add(f"{fam}/{sub}", kind, fam_owner, "(inherits shared drive members)", "inherited", "-", "off",
            "2026-11-11", "")
    resp = f"{fam}/Respite (weekend care sheets)"
    add(resp, "folder", S["S19"], "anyone with the link", "link", "viewer", "anyone with the link", "2026-11-08",
        LINK_SHARED_ON.isoformat())
    for v in with_access:
        add(resp, "folder", S["S19"], vol_email(v), "external personal", "viewer", "anyone with the link",
            "2026-11-08", rand_date(r, date(2022, 1, 1), date(2026, 8, 1)).isoformat())
    for n in range(1, 9):
        add(f"{resp}/Weekend {n:02d} 2026 - care sheet.xlsx", "spreadsheet", S["S19"], "(inherits folder)",
            "inherited", "-", "anyone with the link", f"2026-{min(n + 2, 11):02d}-1{n % 9}", "")
    # Fundraising
    donors = "Shared drives/Fundraising/Donors 2026 (master).gsheet"
    add(donors, "spreadsheet", S["S02"], f"anyone at {DOMAIN} with the link", "domain", "editor",
        f"anyone at {DOMAIN} with the link", "2026-11-11", "2026-01-04")
    for sid in ("S02", "S03", "S04", "S06", "S05", "S01", "S21", "S29", "S30"):
        add(donors, "spreadsheet", S["S02"], S[sid], "org user", "editor", f"anyone at {DOMAIN} with the link",
            "2026-11-11", "")
    phone = [v for v in vols if v["programme"] == "phone-a-thon"][:3]
    for v in phone:
        add(donors, "spreadsheet", S["S02"], vol_email(v), "external personal", "editor",
            f"anyone at {DOMAIN} with the link", "2026-11-11", "2025-11-20")
    add(donors, "spreadsheet", S["S02"], "vova.gorelik@gmail.com", "external personal", "editor",
        f"anyone at {DOMAIN} with the link", "2026-11-11", "2024-02-11")
    add(donors, "spreadsheet", S["S02"], "f.moshe.a.private@gmail.com", "external personal", "editor",
        f"anyone at {DOMAIN} with the link", "2026-11-11", "2024-11-03")
    for path, owner, extra in (
            ("Shared drives/Fundraising/Grants", S["S02"], [S["S03"], S["S01"], S["S21"]]),
            ("Shared drives/Fundraising/Grants/Boilerplate 2025.docx", S["S02"], ["(inherits)"]),
            ("Shared drives/Fundraising/Giving Tuesday 2026", S["S02"], [S["S04"], S["S21"]])):
        for who in extra:
            add(path, "folder" if "." not in path.rsplit("/", 1)[-1] else "document", owner, who,
                "org user" if "@" in who else "inherited", "editor" if "@" in who else "-", "off", "2026-11-09", "")
    rep = "Shared drives/Reports/Adler-Haddad"
    for who in (S["S01"], S["S02"], S["S03"], S["S07"]) + tuple(S[c] for c in COORDINATORS):
        add(rep, "folder", S["S03"], who, "org user", "editor", "off", "2026-10-24", "")
    add(rep, "folder", S["S03"], FOUNDATION, "external org", "viewer", "off", "2026-10-24", "2023-01-12")
    add(f"{rep}/2026 Q3 report - final.docx", "document", S["S03"], "(inherits folder)", "inherited", "-", "off",
        "2026-10-24", "")
    for path, members in (("Shared drives/Admin/HR", ["S01", "S05", "S06"]),
                          ("Shared drives/Admin/Finance", ["S01", "S06", "S05"]),
                          ("Shared drives/Programmes/Parent groups", ["S17", "S27", "S28", "S07"]),
                          ("Shared drives/Programmes/Siblings", ["S20", "S07"]),
                          ("Shared drives/Volunteers", ["S18", "S19", "S05"]),
                          ("Shared drives/Comms/Newsletter", ["S21", "S01", "S02"]),
                          ("My Drive (Samah)/AH narratives drafts", ["S08"]),
                          ("My Drive (Noa)/GrantGenie exports", ["S02"])):
        for sid in members:
            add(path, "folder", S[members[0]], S[sid], "org user", "owner" if sid == members[0] else "editor",
                "off", rand_date(r, date(2026, 9, 1), date(2026, 11, 11)).isoformat(), "")
    add("Shared drives/Volunteers/Volunteer list 2026.gsheet", "spreadsheet", S["S18"], "anyone with the link",
        "link", "viewer", "anyone with the link", "2026-10-30", "2025-05-07")
    add("Shared drives/Comms/Newsletter/2026-09 story drafts.docx", "document", S["S21"], S["S08"], "org user",
        "commenter", "off", "2026-09-08", "")
    write_csv(ROOM / "it" / "drive-sharing-audit.csv",
              ["item", "type", "owner", "shared_with", "principal_type", "role", "link_sharing", "last_modified",
               "sharing_added_on"], rows)
    return rows
