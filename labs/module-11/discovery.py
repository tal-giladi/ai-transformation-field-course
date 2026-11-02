"""Discovery numbers for Givat Oren (lessons 11.2 and 11.3).

    python discovery.py                 # every section
    python discovery.py --section moked # one of: moked, callbacks, language, permits, content, ruti, mystery

Reads the data room by relative path and prints what it finds. Needs the field kit
(labs/common, pandas). Definitions are printed with each number so you can argue about them.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
from fieldkit.data import data_room, load  # noqa: E402

ROOM = data_room("module-11")
SAMPLE = 25  # Moked extract = all contacts of a random 4% of caller numbers
FAMILY = {"permits_parking", "permits_signage", "permits_cafe", "permits_events", "permits_skip",
          "building_archive", "business_licence", "bulky_waste"}


def pct(x: float) -> str:
    return f"{100 * x:.1f}%"


def contacts():
    c = load(ROOM / "service" / "moked-contacts.csv")
    c["family"] = c["topic"].isin(FAMILY)
    c = c.sort_values(["caller_id", "topic", "opened_at"])
    gap = c.groupby(["caller_id", "topic"])["opened_at"].diff()
    c["repeat"] = gap.notna() & (gap.dt.total_seconds() < 14 * 86400)
    return c


def moked() -> None:
    c = contacts()
    print("== Moked 106 volumes and the FCR definition")
    print(f"Contacts in the 4% caller sample, Jun-Oct 2026: {len(c):,} (≈ {len(c) * SAMPLE / 5:,.0f} a month for the city)")
    print(f"Permits-and-fees family share of contacts: {pct(c['family'].mean())}")
    q3 = c[(c["opened_at"] >= "2026-07-01") & (c["opened_at"] < "2026-10-01")]
    print(f"Q3 FCR as defined in the report (fcr_flag): {pct(q3['fcr_flag'].mean())}")
    print("Outcome mix:", (c["outcome"].value_counts(normalize=True) * 100).round(1).to_dict())
    print("\n== Repeat contacts: same caller, same topic, within 14 days of the previous contact")
    print(f"All topics {pct(c['repeat'].mean())}; permits family {pct(c[c['family']]['repeat'].mean())}; "
          f"other topics {pct(c[~c['family']]['repeat'].mean())}")
    nxt = c.groupby(["caller_id", "topic"])["repeat"].shift(-1).fillna(False).astype(bool)
    fam_fcr = c["family"] & (c["fcr_flag"] == 1)
    print(f"Permits-family contacts counted as resolved (fcr_flag = 1) that were followed by a repeat: "
          f"{pct(nxt[fam_fcr].mean())}")
    print("Repeat rate by topic:", (c.groupby("topic")["repeat"].mean() * 100).round(1).sort_values().to_dict())


def callbacks() -> None:
    c = contacts()
    cb = load(ROOM / "service" / "callbacks.csv").merge(c[["contact_id", "family"]], on="contact_id")
    done = cb["completed_at"].dt.date
    promised = cb["promised_by_date"].dt.date
    cb["state"] = "never"
    cb.loc[cb["completed_at"].notna() & (done <= promised), "state"] = "on time"
    cb.loc[cb["completed_at"].notna() & (done > promised), "state"] = "late"
    print("== Callbacks: promised by date vs completed")
    print(f"Callbacks scheduled: {len(cb)}; the report counts these as 'within SLA' when scheduled")
    print("All:", (cb["state"].value_counts(normalize=True) * 100).round(1).to_dict())
    print("Permits family:", (cb[cb["family"]]["state"].value_counts(normalize=True) * 100).round(1).to_dict())


def language() -> None:
    c = contacts()
    print("== Service language: what the caller chose vs who answered")
    handled = c[c["outcome"] != "abandoned"]
    for lang in ["ar", "ru", "am", "en"]:
        g = handled[handled["contact_language"] == lang]
        print(f"{lang}: {len(g)} handled contacts, served in {lang}: {pct((g['served_language'] == lang).mean())}")
    ph = handled[(handled["channel"] == "phone")]
    for lang, served in [("he", "he"), ("ar", "ar"), ("ar", "he")]:
        g = ph[(ph["contact_language"] == lang) & (ph["served_language"] == served)]
        print(f"Phone wait, chose {lang}, served {served}: median {g['queue_wait_sec'].median():.0f} s (n = {len(g)})")
    staff = load(ROOM / "service" / "moked-staffing-2026.csv")
    active = staff[staff["status"] == "active"]
    for lang in ["ar", "ru", "am", "en"]:
        print(f"Active agents who speak {lang}: {active['languages'].str.contains(lang).sum()} of {len(active)}")


def permits() -> None:
    p = load(ROOM / "permits" / "applications-2026.csv")
    print("== Permit decisions and reasons")
    rej = p[p["decision"] == "rejected"]
    print(f"Applications Jan-Oct 2026: {len(p):,}; rejected {len(rej)}; letters in Hebrew: {pct((p['letter_language'] == 'he').mean())}")
    prk = rej[rej["type"] == "PRK"]
    print(f"Parking-permit rejections: {len(prk)}; with R-07 'does not meet the criteria': {pct((prk['reason_code'] == 'R-07').mean())}")
    print("Linked 106 contacts per rejected application, by code:",
          rej.groupby("reason_code")["linked_106_contacts"].mean().round(2).to_dict())
    lv = p[(p["type"] == "PRK") & (p["vehicle_ownership"].isin(["leased", "company"]))
           & (p["submitted_date"] >= "2026-07-01") & (p["employer_letter_attached"] == "y")]
    dec = lv[lv["decision"].isin(["approved", "rejected"])]
    print(f"Leased/company cars from 1 Jul with the employer letter: {len(lv)}; decided {len(dec)}; "
          f"rejected {(dec['decision'] == 'rejected').sum()} ({pct((dec['decision'] == 'rejected').mean())})")
    evt = p[(p["type"] == "EVT") & p["decision"].isin(["approved", "rejected"])]
    print("Event applications rejected as late (R-08), share by applicant language:",
          {k: pct(v) for k, v in evt.assign(late=evt["reason_code"].eq("R-08")).groupby("applicant_language")["late"].mean().items()})
    sk = p[(p["type"] == "SKP") & (p["decision"] == "approved") & (p["submitted_date"] < "2026-03-16")]
    print(f"Skip permits approved before 16 Mar charged at the 2025 rate: {len(sk)}, ₪{sk['fee_charged_ils'].sum():,.0f} "
          f"charged vs ₪{sk['fee_charged_ils'].sum() / 60 * 75:,.0f} at ₪75 a week")


def content() -> None:
    cms = load(ROOM / "content" / "cms-pages.csv")
    print("== Website content")
    print(f"Pages: {len(cms):,}; without a named owner: {pct((cms['owner_editor'].isna()).mean())}")
    for lang, g in cms.groupby("language"):
        print(f"  {lang}: {len(g)} pages, last changed before 2024: {pct((g['last_modified'] < '2024-01-01').mean())}")
    print(f"Pages linking the 2025 fee table: {(cms['pdf_link'] == 'fee-table-2025.pdf').sum()}; "
          f"pages with a third-party script: {cms['script_embed'].notna().sum()}")
    site = sorted((ROOM / "content" / "site").glob("*.md"))
    print(f"Permits pages in the site export: {len(site)} — compare each with city/council-decision-fees-2025-12.md")


def ruti() -> None:
    r = load(ROOM / "chatbot" / "ruti-bot-log.csv")
    print("== Ruti (the business-licensing desk's free chatbot)")
    print(f"Sessions since 10 Mar 2026: {len(r)}; by language: {r['detected_language'].value_counts().to_dict()}")
    print(f"Replies in Hebrew: {pct(r['bot_reply'].str.contains(r'[֐-׿]').mean())}")
    print(f"User messages with a 9-digit number (ID?): {r['user_message'].str.contains(r'\b\d{9}\b').sum()}; "
          f"with a mobile number: {r['user_message'].str.contains(r'05\d-\d{7}').sum()}")
    old = {"sign ₪245": r"\b245 ₪", "sign minimum ₪300": r"\b300 ₪", "café ₪160": r"\b160 ₪",
           "events 14 days": r"14 יום", "skip ₪60": r"(?<!1)60 ₪", "leased not eligible": "אינו זכאי",
           "second car ₪90": r"\b90 ₪", "invented restaurant fee": "1,200"}
    for label, pat in old.items():
        print(f"  replies stating {label}: {r['bot_reply'].str.contains(pat, regex=True).sum()}")


def mystery() -> None:
    ms = load(ROOM / "service" / "mystery-shopper-2026.csv")
    ts = load(Path(__file__).resolve().parent / "pilot" / "test-set.csv")
    m = ms.merge(ts[["question_id", "expected_behaviour", "changed_2026"]], on="question_id")
    print("== Mystery shopper, Aug-Sep 2026 (quality unit, 120 calls)")
    print("Result codes:", m["result_code"].value_counts().to_dict())
    a = m[m["expected_behaviour"] == "answer"]
    for ch, g in a.groupby("changed_2026"):
        print(f"Answer questions, rule changed in 2026 = {ch}: right {pct((g['result_code'] == 'correct').mean())} (n = {len(g)})")
    for lang, g in m.groupby("language_asked"):
        print(f"{lang}: right {pct((g['result_code'] == 'correct').mean())}, served in {lang} "
              f"{pct((g['served_language'] == lang).mean())} (n = {len(g)})")


SECTIONS = {"moked": moked, "callbacks": callbacks, "language": language, "permits": permits,
            "content": content, "ruti": ruti, "mystery": mystery}

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--section", choices=list(SECTIONS))
    args = ap.parse_args()
    for name, fn in SECTIONS.items():
        if args.section in (None, name):
            fn()
            print()
