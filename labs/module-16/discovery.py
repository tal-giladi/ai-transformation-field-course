"""Open Hands: the discovery and baseline numbers (lessons 16.2 and 16.3). Optional Track B.

    python discovery.py            # everything
    python discovery.py access     # one section: access, donors, survey, time, funders, money, consent

Reads the data room by relative path; no network, no LLM. Prints what it found, with numerators and
denominators, so you can check every number against a spreadsheet.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))

from fieldkit.data import data_room, load  # noqa: E402

ROOM = data_room("module-16")
USD_ILS = 3.136  # Bank of Israel representative rate, 2 November 2026
COORDS = ["S08", "S09", "S10", "S11", "S12", "S13"]
CASE_ROLES_NEEDED = COORDS + ["S07", "S14", "S15"]  # coordinators, head of family services, rights, intake


def pct(a, b) -> str:
    return f"{100 * a / b:.1f}% ({a} of {b})" if b else "n/a"


def access() -> None:
    audit = load(ROOM / "it" / "drive-sharing-audit.csv")
    staff = load(ROOM / "people" / "staff.csv")
    vols = load(ROOM / "people" / "volunteers.csv")
    fam = audit[audit["item"] == "Shared drives/Families"]
    print("== Families shared drive: who has access")
    print(fam["principal_type"].value_counts().to_string())
    print("authorised accounts:", len(fam))
    need = set(staff[staff["staff_id"].isin(CASE_ROLES_NEEDED)]["email"])
    print("of which in roles that need case files:", len(need & set(fam["shared_with"])))
    vol_mail = {f"{v.lower()}.vol@{d}": s for v, d, s in zip(vols["volunteer_id"], vols["email_domain"],
                                                              vols["status"])}
    fam_vols = [m for m in fam["shared_with"] if m in vol_mail]
    print("volunteers (personal accounts) at top level:", len(fam_vols),
          "| inactive:", sum(vol_mail[m] == "inactive" for m in fam_vols))
    resp = audit[audit["item"].str.endswith("Respite (weekend care sheets)")]
    print("\n== Respite folder: link sharing =", resp["link_sharing"].iloc[0],
          "| since", resp[resp["shared_with"] == "anyone with the link"]["sharing_added_on"].iloc[0])
    rv = [m for m in resp["shared_with"] if m in vol_mail]
    print("volunteers added by email:", len(rv), "| inactive:", sum(vol_mail[m] == "inactive" for m in rv))
    with_access = set(fam_vols) | set(rv)
    conf = dict(zip([f"{v.lower()}.vol@{d}" for v, d in zip(vols["volunteer_id"], vols["email_domain"])],
                    vols["confidentiality_signed"].fillna("")))
    print("volunteers with any access:", len(with_access), "| no confidentiality form on file:",
          sum(conf[m] != "y" for m in with_access))
    links = audit[audit["link_sharing"] == "anyone with the link"]["item"].unique()
    print("\n== Items open to 'anyone with the link':", len(links))
    for item in links:
        print("  ", item)


def donors() -> None:
    audit = load(ROOM / "it" / "drive-sharing-audit.csv")
    d = load(ROOM / "fundraising" / "donors.csv")
    sheet = audit[audit["item"].str.contains("Donors 2026") & (audit["principal_type"] != "domain")]
    print("== Donor sheet editors:", len(sheet))
    print(sheet["principal_type"].value_counts().to_string())
    print("domain-wide setting:", audit[audit["item"].str.contains("Donors 2026")]["link_sharing"].iloc[0])
    print("ID number on file:", pct(int((d["id_on_file"] == "y").sum()), len(d)))
    notes = d["notes"].fillna("")
    print("notes filled:", int((notes != "").sum()))
    print("notes that mention a child, a diagnosis, a programme or welfare (read them yourself):")
    keys = ("programme", "autism", "families", "CP", "diagnosis", "welfare", "husband", "הפוגה", "البرنامج")
    sens = notes[notes.apply(lambda s: any(k in s for k in keys))]
    print("  ", len(sens), "| examples:", "; ".join(sens.unique()[:4]))


def survey() -> None:
    s = load(ROOM / "it" / "staff-ai-survey-2026-10.csv")
    print("== Staff AI survey: answered", len(s), "of 30")
    print(s["how_often_ai"].value_counts().to_string())
    users = s[s["how_often_ai"] != "never"]
    print("\naccount type among users:\n" + users["account_type"].value_counts().to_string())
    print("\npasted family information:\n" + s["pasted_family_information"].value_counts().to_string())


def time() -> None:
    t = load(ROOM / "people" / "time-log-2026-10.csv")
    t["hours"] = t["minutes"] / 60
    piv = t.pivot_table(index="staff_id", columns="activity", values="hours", aggfunc="sum", fill_value=0)
    print("== Logged week 4-8 Oct 2026 (the week before the Q3 Adler-Haddad report): hours")
    print(piv.round(1).to_string())
    c = t[t["staff_id"].isin(COORDS)]
    tot = c["hours"].sum()
    for act in ("funder_report_adler_haddad", "case_notes", "translation_letters"):
        h = c[c["activity"] == act]["hours"].sum()
        print(f"coordinators, {act}: {h:.1f} h ({100 * h / tot:.1f}% of {tot:.1f} h; {h / 6:.1f} h each)")
    direct = c[c["activity"].isin(["family_contact", "home_visit"])]["hours"].sum()
    print(f"coordinators, direct family time: {direct:.1f} h ({100 * direct / tot:.1f}%)")
    ah = t[t["activity"] == "funder_report_adler_haddad"]["hours"].sum()
    print(f"Adler-Haddad, everyone: {ah:.1f} h in the week")
    noa = t[t["staff_id"] == "S02"]
    w = noa[noa["activity"].isin(["grant_proposal", "other_funder_report", "funder_report_adler_haddad"])]
    print(f"Noa: funder writing {w['hours'].sum():.1f} of {noa['hours'].sum():.1f} h; reports only "
          f"{noa[noa['activity'].isin(['other_funder_report', 'funder_report_adler_haddad'])]['hours'].sum():.1f} h")


def funders() -> None:
    f = load(ROOM / "fundraising" / "funders.csv")
    f["report_hours_year"] = f["est_hours_per_report"] * f["reports_per_year"]
    print("== Funders: development's estimates of writing hours a year")
    print(f[["funder", "annual_amount_ils", "reports_per_year", "est_hours_per_report", "report_hours_year",
             "est_hours_per_proposal"]].to_string(index=False))
    print("report hours a year:", f["report_hours_year"].sum(), "| proposal hours:",
          f["est_hours_per_proposal"].sum())
    ah = f.iloc[0]
    print("Adler-Haddad share of report hours:", pct(int(ah["report_hours_year"]), int(f["report_hours_year"].sum())))


def money() -> None:
    card = load(ROOM / "finance" / "card-statement-2026.csv")
    acc = load(ROOM / "it" / "accounts-and-licences.csv")
    sw = card[card["category"].isin(["Software", "Office supplies"]) & card["merchant"].str.contains(
        "OPENAI|MSFT|DROPBOX|ZOOM|MAILCHIMP|KABALA|WIX|GRANTGENIE")]
    print("== Software on the cards, Jan-Oct 2026 (₪)")
    print(sw.groupby("merchant")["amount_ils"].agg(["count", "sum"]).round(2).to_string())
    ms = acc[acc["service"] == "Microsoft 365"]
    seen = ms["last_sign_in"].astype(str)
    used = ms[seen.str.match(r"[0-9]{4}-") & (seen >= "2026-08-14")]
    print(f"\nMicrosoft seats: {len(ms)}, signed in during the last 90 days: {len(used)}")
    print("annual figures at ₪%.3f per US$ (Bank of Israel, 2 Nov 2026):" % USD_ILS)
    rows = [("Microsoft Business Premium, 7 unused seats", 7 * 5.50 * 12),
            ("ChatGPT Plus on the card", 20 * 12), ("Dropbox Plus, unused since 2024", 11.99 * 12),
            ("GrantGenie Pro from 1 Jan 2027 (if not cancelled)", 49 * 12)]
    for name, usd in rows:
        print(f"  {name}: US${usd:,.0f} = ₪{usd * USD_ILS:,.0f} a year")
    print(f"  total: ₪{sum(u for _, u in rows) * USD_ILS:,.0f} a year")


def consent() -> None:
    c = load(ROOM / "cases" / "case-register.csv")
    print("== Consent versions, active families")
    print(c["consent_version"].value_counts().to_string())
    ah = c[c["adler_haddad_grant"] == "y"]
    print("\nunder the Adler-Haddad grant:", len(ah))
    print(ah["consent_version"].value_counts().to_string())
    print("v2 with consent to stories:", int((c["consent_stories"] == "y").sum()))


SECTIONS = {"access": access, "donors": donors, "survey": survey, "time": time, "funders": funders,
            "money": money, "consent": consent}

if __name__ == "__main__":
    wanted = sys.argv[1:] or list(SECTIONS)
    for name in wanted:
        SECTIONS[name]()
        print()
