"""The revised business case for Atlas & Rowe (Track B, lessons 12.3 and 12.5).

    python roi_model.py                     # both scenarios, ledgers, sensitivity; writes roi-revised.csv
    python roi_model.py --saving 0.2 --resale 0.25

Nets the vendor's "6.2 hours a week" slide across five ledgers: the firm's fees, capacity (hours, not
cash), the customer's share, control costs and tool costs. Every input is labelled measured (from the
data room), directional (extrapolated) or assumed (until the pilot or the market shows otherwise).
Exchange rate: Bank of Israel representative rate, ₪3.136 per US$ on 2 November 2026.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

from discovery import ROOM, load, research_hours

HERE = Path(__file__).resolve().parent
FX = 3.136


def inputs(saving: float, resale: float) -> dict:
    lawyers = load(ROOM / "people" / "lawyers.csv")
    time = load(ROOM / "billing" / "time-entries-2026-q3.csv")
    matters = load(ROOM / "billing" / "matters.csv")
    out, _, by_type, billed_share = research_hours(time)
    a = lawyers[lawyers["role"] == "associate"]
    p = lawyers[lawyers["role"] != "associate"]
    res_h = (a["billable_2026_jan_sep_h"].sum() * 12 / 9 * out["associates"]["research_by_narrative_%"] / 100
             + p["billable_2026_jan_sep_h"].sum() * 12 / 9 * out["partners"]["research_by_narrative_%"] / 100)
    carmel = matters[(matters["client_code"] == "C-014") & (matters["billing_type"] == "hourly")]
    tech = matters[(matters["billing_type"] == "fixed") & (matters["practice_group"] == "Tech & IP")]
    return {
        "research_hours_year": (round(res_h), "directional", "3 groups' Q3 research share × all lawyers' 2026 hours"),
        "share_hourly": (by_type["hourly"] / 100, "measured", "research hours on hourly matters"),
        "share_capped": (by_type["capped"] / 100, "measured", "research hours on capped matters"),
        "share_fixed": (by_type["fixed"] / 100, "measured", "research hours on fixed-fee matters"),
        "share_retainer": (by_type["retainer"] / 100, "measured", "research hours on retainers"),
        "billed_share": (round(billed_share, 3), "measured", "research hours billed after write-offs"),
        "assoc_rate": (round(a["standard_rate_ils"].mean()), "measured", "mean associate standard rate, ₪"),
        "capped_under_cap": (0.5, "assumed", "share of capped research that is still billable"),
        "saving": (saving, "assumed", "research time saved net of verification, until the pilot times it"),
        "resale": (resale, "assumed", "share of freed hours sold to clients (associates at 81% of target)"),
        "carmel_hourly_2025": (float(carmel["billed_2025_ils"].sum()), "measured", "Carmel hourly fees 2025"),
        "tech_fixed_worked_2025": (float(tech["worked_value_2025_ils"].sum()), "measured", "Tech & IP fixed-fee worked value"),
        "tech_fixed_billed_2025": (float(tech["billed_2025_ils"].sum()), "measured", "Tech & IP fixed fees billed"),
        "tech_package_sales": (0.5, "assumed", "share of Tech & IP capacity freed from overruns sold as new packages"),
    }


def scenario(v: dict, name: str) -> dict:
    g = {k: x[0] for k, x in v.items()}
    if name == "0":   # do nothing: no tool, Carmel's 15% conceded at renewal, shadow AI continues (risk not priced)
        carmel = round(-0.15 * g["carmel_hourly_2025"])
        return {"customer's share (Carmel renewal)": carmel, "net cash, year 1": carmel}
    value_h = g["assoc_rate"] * g["billed_share"]            # fees removed per saved research hour on billable work
    if name == "A":   # sign 90 Parshan seats in January, firm-wide, billing unchanged
        adoption, scope = 0.6, 1.0
        tools = -(90 * 120 * 0.8 * 12 + 25_000) * FX
        control = -240_000                                    # librarian to keep a whole-DMS index usable
        carmel = -0.15 * g["carmel_hourly_2025"]              # the 15% conceded at renewal
        pricing = 0.0
    else:             # curate, control, re-price, pilot in two groups, choose a platform at a June gate
        adoption, scope = 0.8, 0.35                           # Tech & IP and litigation: about a third of research
        tools = -(90 * 20 * 12 * FX) - 40_000                 # one enterprise assistant for all + pilot tooling
        control = -180_000 - 240_000                          # curation sprint + librarian
        carmel = -0.10 * g["carmel_hourly_2025"]              # fixed-price package priced 10% under 2025 hourly cost
        overrun_cut = (g["tech_fixed_worked_2025"] - 1.2 * g["tech_fixed_billed_2025"])
        pricing = overrun_cut * g["tech_package_sales"]        # Tech & IP sells the freed hours as packages
    saved = g["research_hours_year"] * adoption * g["saving"] * scope
    billable = saved * (g["share_hourly"] + g["share_capped"] * g["capped_under_cap"])
    if name == "B":
        billable *= 0.5                                       # half the pilot's hourly research work moves to fixed prices
    fees_lost = -billable * value_h
    freed = saved - billable
    resold = freed * g["resale"] * g["assoc_rate"] * g["billed_share"]
    cash = fees_lost + resold + carmel + control + tools + pricing
    out = {"hours saved": round(saved), "fees lost on billable work": round(fees_lost),
           "freed hours (capacity)": round(freed), "freed hours resold": round(resold),
           "customer's share (Carmel renewal)": round(carmel), "control costs": round(control),
           "tool costs (year 1)": round(tools), "net cash, year 1": round(cash)}
    if name == "B":
        out = {**out, "net cash, year 1": round(cash)}
        out["Tech & IP overrun cut to 20% (₪ of hours at std rates)"] = round(overrun_cut)
        out["of which sold as new packages"] = round(pricing)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--saving", type=float, default=0.30)
    ap.add_argument("--resale", type=float, default=0.0)
    args = ap.parse_args()
    v = inputs(args.saving, args.resale)
    print("== Inputs")
    for k, (val, label, what) in v.items():
        print(f"  {k:24} {val:>14,.3f}  {label:12} {what}")
    slide = 6.2 * 90 * 44 * 950
    print(f"\n== The slide: 6.2 h × 90 × 44 weeks × ₪950 = ₪{slide:,.0f} 'capacity'; treated as revenue")
    z, a, b = scenario(v, "0"), scenario(v, "A"), scenario(v, "B")
    for x in (a, b):
        x["compared with doing nothing"] = x["net cash, year 1"] - z["net cash, year 1"]
    rows = [["line", "0: do nothing", "A: sign 90 seats, billing unchanged", "B: curate, control, re-price, pilot"]]
    for k in dict.fromkeys(list(a) + list(b)):
        rows.append([k, z.get(k, ""), a.get(k, ""), b.get(k, "")])
    w = max(len(r[0]) for r in rows)
    print("\n== Year 1 (2027), ₪ unless hours")
    for r in rows:
        print(f"  {r[0]:{w}}  {str(r[1]):>14}  {str(r[2]):>14}  {str(r[3]):>14}")
    with (HERE / "roi-revised.csv").open("w", encoding="utf-8", newline="") as f:
        csv.writer(f, lineterminator="\n").writerows(rows)
    print("\n== Sensitivity of A's net cash (saving × resale)")
    for s in (0.2, 0.3, 0.4):
        cells = []
        for rs in (0.0, 0.25, 0.5):
            cells.append(f"{scenario(inputs(s, rs), 'A')['net cash, year 1']:>12,}")
        print(f"  saving {s:.0%}: resale 0% / 25% / 50% → " + " ".join(cells))


if __name__ == "__main__":
    main()
