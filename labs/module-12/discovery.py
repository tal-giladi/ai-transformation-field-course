"""Discovery numbers for Atlas & Rowe (Track B, lessons 12.2 and 12.3).

    python discovery.py

Prints: research hidden in drafting codes and what is written off; associates' hours against target;
fixed-fee overruns by group; AI use in the proxy log against the survey; the knowledge bank's review
state; the Carmel NDA workstream before and after automation. Reads the data room by relative path.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))

from fieldkit.data import data_room, load  # noqa: E402

ROOM = data_room("module-12")
RESEARCH = re.compile(r"research|case law|precedent|rulings|פסיקה|מחקר|תקדימים|פסקי דין", re.I)


def research_hours(time):
    """Research by narrative, not by code: partners write off RES lines, so associates code research as DRF."""
    time = time.copy()
    time["research_words"] = time["narrative"].str.contains(RESEARCH)
    out = {}
    for role, g in time.groupby(time["role"] == "associate"):
        name = "associates" if role else "partners"
        out[name] = {"hours": g["hours"].sum(),
                     "coded_RES_%": 100 * g.loc[g["activity_code"] == "RES", "hours"].sum() / g["hours"].sum(),
                     "research_by_narrative_%": 100 * g.loc[g["research_words"], "hours"].sum() / g["hours"].sum()}
    billed = time[time["billing_type"] != "fixed"]
    wo = {}
    for label, mask in (("RES lines", billed["activity_code"] == "RES"),
                        ("research hidden in DRF/REV", (billed["activity_code"] != "RES") & billed["research_words"]),
                        ("everything else", ~billed["research_words"])):
        g = billed[mask]
        wo[label] = 100 * g["written_off_hours"].sum() / g["hours"].sum()
    res = time[time["research_words"]]
    by_type = (100 * res.groupby("billing_type")["hours"].sum() / res["hours"].sum()).round(1).to_dict()
    nonfixed = res[res["billing_type"] != "fixed"]
    billed_share = nonfixed["billed_hours"].sum() / nonfixed["hours"].sum()
    return out, wo, by_type, billed_share


def main() -> None:
    lawyers = load(ROOM / "people" / "lawyers.csv")
    time = load(ROOM / "billing" / "time-entries-2026-q3.csv")
    matters = load(ROOM / "billing" / "matters.csv")

    print("== Research time (Q3 2026, Litigation, Tech & IP, International desk)")
    out, wo, by_type, billed_share = research_hours(time)
    for k, v in out.items():
        print(f"  {k}: {v['hours']:,.0f} h; coded RES {v['coded_RES_%']:.1f}%; research by narrative "
              f"{v['research_by_narrative_%']:.1f}%")
    print("  written off (non-fixed matters): " + "; ".join(f"{k} {v:.1f}%" for k, v in wo.items()))
    print(f"  research hours by billing type: {by_type}; billed share of research on non-fixed matters "
          f"{100 * billed_share:.1f}%")

    a = lawyers[lawyers["role"] == "associate"]
    ann = a["billable_2026_jan_sep_h"] * 12 / 9
    print(f"\n== Associates' hours: 2025 mean {a['billable_2025_h'].mean():,.0f}; 2026 annualised {ann.mean():,.0f} "
          f"= {100 * ann.mean() / 1850:.0f}% of the 1,850 target; {int((ann >= 1850).sum())} of {len(a)} at target")

    f = matters[matters["billing_type"] == "fixed"].groupby("practice_group")[
        ["billed_2025_ils", "worked_value_2025_ils"]].sum()
    f["worked_over_fee_%"] = (100 * (f["worked_value_2025_ils"] / f["billed_2025_ils"] - 1)).round(1)
    print("\n== Fixed fees 2025: worked value over the fee, by group\n" + f.to_string())

    proxy = load(ROOM / "it" / "proxy-ai-domains-2026-09-10.csv")
    survey = load(ROOM / "surveys" / "ai-use-survey-2026-10.csv")
    users = proxy.merge(lawyers[["lawyer_id", "role"]], left_on="user_id", right_on="lawyer_id", how="left")
    law = users[users["role"].notna()]
    up = law[law["file_uploads"] > 0]
    print(f"\n== AI sites, 1 Sep - 31 Oct (proxy): {law['user_id'].nunique()} lawyers "
          f"({law.loc[law['role'] == 'associate', 'user_id'].nunique()} of {len(a)} associates, "
          f"{law.loc[law['role'] != 'associate', 'user_id'].nunique()} of {len(lawyers) - len(a)} partners); "
          f"{up['user_id'].nunique()} lawyers uploaded {int(up['file_uploads'].sum())} files")
    weekly = survey["ai_use_frequency"].isin(["weekly", "daily"]).mean()
    print(f"   survey ({len(survey)} answers): weekly or daily {100 * weekly:.0f}%; client information "
          f"'no' {100 * (survey['client_information_in_ai'] == 'no').mean():.0f}%")

    km = load(ROOM / "km" / "precedent-bank-index.csv")
    never = km["last_reviewed_date"].isna().mean()
    priv = km[km["tags"].str.contains("privacy", na=False)]
    a13 = priv[(priv["uploaded_date"] < "2025-08-14") & (priv["status"] == "current")
               & (priv["last_reviewed_date"].isna() | (priv["last_reviewed_date"] < "2025-08-14"))]
    uses = km["uses_last_12m"].sort_values(ascending=False)
    print(f"\n== Precedent bank: {len(km)} documents; never reviewed {100 * never:.0f}%; privacy documents "
          f"'current' and not reviewed since Amendment 13 (14 Aug 2025): {len(a13)}; top 300 = "
          f"{100 * uses.head(300).sum() / uses.sum():.0f}% of uses")

    nda = load(ROOM / "clients" / "carmel-nda-workstream.csv")
    nda["year"] = nda["month"].str[:4]
    y = nda.groupby("year")[["ndas_completed", "hours_recorded", "fees_billed_ils"]].sum()
    y["fee_per_nda"] = (y["fees_billed_ils"] / y["ndas_completed"]).round(0)
    y["fees_per_hour"] = (y["fees_billed_ils"] / y["hours_recorded"]).round(0)
    print("\n== Carmel NDAs (2026 = Jan-Oct)\n" + y.to_string())


if __name__ == "__main__":
    main()
