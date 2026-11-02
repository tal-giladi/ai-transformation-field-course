"""Lesson 03.7 (Track B): the ROI model for Harbor & Pine's reply-drafts pilot.

Prints, for the business case the CFO will review:
  1. the monthly pilot economics (volume x automation x accuracy, minus review and rework, minus
     tokens and fixed running cost) - the same model as the pilot-economics simulation;
  2. every claim in the sponsor's deck netted across four ledgers (sponsor's team, receiving team,
     control capacity, customer's share), labelled measured / directional / assumed, cash or capacity;
  3. three scenarios (low = measured cash, expected = + directional, high = + assumed), each with NPV
     at the CFO's hurdle rate over three years, payback and the approval level;
  4. a sensitivity table: what each fragile assumption does to the expected NPV;
  5. the capacity check behind the one cash line that matters (the seasonal temps).

Run from this folder:            python roi_model.py
Write the filled model as CSV:   python roi_model.py --csv roi-model-harbor-solution.csv

Change the numbers in INPUTS and CLAIMS to model your own case. No API key, no network.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))

import pandas as pd

from fieldkit.cost import breakeven_months, npv, pilot_value, token_cost
from fieldkit.data import data_room, load

room = data_room("harbor-and-pine")
finance = load(room / "company" / "finance-summary.csv")

# --- Inputs ----------------------------------------------------------------------------------------
support_cost = -float(finance.loc[finance["line"] == "Customer service (fully loaded)", "fy2025_ils"].iloc[0])
PAID_HOURS_PER_PERSON = 1_870          # a year, after holidays and leave (assumption)
STAFF = 14                             # people/headcount.csv: the Customer Service team
HOURLY = round(support_cost / STAFF / PAID_HOURS_PER_PERSON)   # about 130 shekels an hour

INPUTS = dict(
    volume=3_200,          # written contacts a month in peak season, WhatsApp routed into the helpdesk
    automation_rate=0.6,   # share that gets a draft
    accuracy=0.8,          # share of drafts accepted as right (shadow mode target)
    minutes_saved=8,       # per accepted draft
    review_minutes=2,      # every draft is read before it is sent
    rework_minutes=5,      # extra minutes to fix a wrong draft
    tokens_in=2_500, tokens_out=400,
    price_in=3.0, price_out=15.0,   # US$ per million tokens, the simulation's example prices
    usd_to_ils=3.70,       # the CFO's planning rate, October 2026 (finance-summary.md)
    fixed_monthly=4_000,   # licences, hosting, monitoring, change control (assumption)
)
BUILD = 120_000            # one-off, shekels (breakdown in lesson 03.7)
YEARS = 3
HURDLE = 0.12              # finance-summary.md
APPROVAL = [(50_000, "Department head and CFO"), (150_000, "CEO"), (float("inf"), "Board")]

# The sponsor's seven claims (shekels a year) with the adjustments that belong in the netting.
# ledger: sponsor | receiving | control | customer.  target: another claim the amount moves to.
CLAIMS = [
    dict(id="drafts", title="Agents save 8 minutes per accepted draft", claimed=319_500,
         label="measured", cls="capacity",
         adj=[("sponsor", -49_920, "rework on the 20% wrong drafts, 384 h"),
              ("control", -99_840, "2-minute review of every draft, 768 h")]),
    dict(id="heads", title="Two fewer agents from April 2027", claimed=431_400,
         label="assumed", cls="capacity",
         adj=[("sponsor", -431_400, "the same hours as claim 1: count them once")]),
    dict(id="wismo", title="Fewer 'where is my order?' contacts", claimed=300_000,
         label="directional", cls="capacity",
         adj=[("sponsor", -300_000, "caused by the date fix (no AI), not by this pilot")]),
    dict(id="translate", title="Translation service no longer needed", claimed=42_000,
         label="measured", cls="cash",
         adj=[("receiving", -12_000, "marketing keeps a small plan"),
              ("control", -13_000, "native-speaker spot-check, about 100 h")]),
    dict(id="credits", title="Fewer goodwill credits beyond policy", claimed=103_500,
         label="assumed", cls="cash",
         adj=[("control", -13_000, "Rina records every claim outcome, about 100 h"),
              ("customer", -51_750, "half is money customers no longer get")]),
    dict(id="repeat", title="Repeat purchases from faster replies", claimed=67_600,
         label="assumed", cls="cash",
         adj=[("customer", -39_200, "count gross margin (42%), not revenue")]),
    dict(id="temps", title="No seasonal temps next peak", claimed=96_000,
         label="directional", cls="cash",
         adj=[("sponsor", -96_000, "the temps' cost leaves claim 1's capacity when it becomes cash", "drafts")]),
]
TIERS = {"low": ["measured"], "expected": ["measured", "directional"],
         "high": ["measured", "directional", "assumed"]}


def money(x: float) -> str:
    return f"{x:,.0f}"


def approval(total: float) -> str:
    return next(who for limit, who in APPROVAL if total <= limit)


def monthly(**over) -> dict:
    p = {**INPUTS, **over}
    per_item = token_cost(p["tokens_in"], p["tokens_out"], price_in=p["price_in"], price_out=p["price_out"])
    r = pilot_value(volume=p["volume"], automation_rate=p["automation_rate"], accuracy=p["accuracy"],
                    minutes_saved=p["minutes_saved"], review_minutes=p["review_minutes"],
                    rework_minutes=p["rework_minutes"], hourly_cost=HOURLY, cost_per_item_usd=per_item,
                    usd_to_ils=p["usd_to_ils"], fixed_monthly=p["fixed_monthly"])
    r["running_month_ils"] = r["model_cost_ils"] + r["fixed_ils"]
    r["breakeven_months"] = breakeven_months(BUILD, r["net_value_ils"])
    return r


def netted() -> dict:
    net = {c["id"]: c["claimed"] for c in CLAIMS}
    for c in CLAIMS:
        for a in c["adj"]:
            target = a[3] if len(a) > 3 else c["id"]
            net[target] += a[1]
    return net


def case(cash_per_year: float, running: float, build: float = BUILD, rate: float = HURDLE) -> dict:
    flows = [-build] + [cash_per_year - running] * YEARS
    yearly = cash_per_year - running
    return {"npv": npv(flows, rate, periods_per_year=1),
            "payback_months": round(build / yearly * 12, 1) if yearly > 0 else None}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--csv", help="also write the filled model to this CSV file")
    args = ap.parse_args()

    print(f"Hourly cost: {money(support_cost)} / {STAFF} people / {PAID_HOURS_PER_PERSON} h = {HOURLY} shekels an hour\n")

    m = monthly()
    running_year = round(m["running_month_ils"] * 12, -3)   # the CFO's template works in thousands
    print("1. Monthly pilot economics (peak volume)")
    print(pd.DataFrame([m]).drop(columns=["note"]).T.rename(columns={0: "value"}).to_markdown())
    print(f"\nRunning cost a year: {money(m['running_month_ils'] * 12)} (fixed {money(INPUTS['fixed_monthly'] * 12)}"
          f" + tokens {money(m['model_cost_ils'] * 12)}); {money(running_year)} in the case (thousands)")
    print("Capacity, not cash: the shekel value above is hours at the hourly cost.\n")

    net = netted()
    rows = []
    for c in CLAIMS:
        rows.append({"claim": c["title"], "claimed": money(c["claimed"]),
                     "adjustments": "; ".join(f"{a[0]} {money(a[1])} ({a[2]})" for a in c["adj"]),
                     "net": money(net[c["id"]]), "label": c["label"], "class": c["cls"]})
    print("2. Claims netted across the four ledgers (shekels a year)")
    print(pd.DataFrame(rows).to_markdown(index=False))
    print(f"\nClaimed total: {money(sum(c['claimed'] for c in CLAIMS))}\n")

    print(f"3. Scenarios: NPV at {HURDLE:.0%} over {YEARS} years, build {money(BUILD)}, running {money(running_year)} a year")
    total_cost = BUILD + YEARS * running_year
    srows = []
    for tier, labels in TIERS.items():
        cash = sum(net[c["id"]] for c in CLAIMS if c["label"] in labels and c["cls"] == "cash")
        cap = sum(net[c["id"]] for c in CLAIMS if c["label"] in labels and c["cls"] == "capacity")
        r = case(cash, running_year)
        srows.append({"scenario": tier, "cash a year": money(cash), "capacity a year (not cash)": money(cap),
                      "NPV": money(r["npv"]), "payback months": r["payback_months"] or "never"})
    print(pd.DataFrame(srows).to_markdown(index=False))
    print(f"\nThree-year cost: {money(total_cost)} -> approval: {approval(total_cost)}\n")

    exp_cash = sum(net[c["id"]] for c in CLAIMS if c["label"] in TIERS["expected"] and c["cls"] == "cash")
    base = case(exp_cash, running_year)["npv"]
    sonnet = monthly(price_in=2.0, price_out=10.0)["running_month_ils"] * 12 - (m["running_month_ils"] * 12 - running_year)
    drafts_a_year = INPUTS["volume"] * INPUTS["automation_rate"] * 12
    sens = [
        ("Base (expected case)", base),
        ("Only one temp released (cash 65,000)", case(exp_cash - 48_000, running_year)["npv"]),
        ("Translation contract kept in full", case(exp_cash - net["translate"], running_year)["npv"]),
        ("Running cost +25%", case(exp_cash, running_year * 1.25)["npv"]),
        ("Build cost +25%", case(exp_cash, running_year, build=BUILD * 1.25)["npv"]),
        ("Token prices at US$2 / US$10 per million", case(exp_cash, sonnet)["npv"]),
        ("1.5% more wrong replies reach customers (120 shekels each)",
         case(exp_cash - drafts_a_year * 0.015 * 120, running_year)["npv"]),
        ("Hurdle rate 15%", case(exp_cash, running_year, rate=0.15)["npv"]),
    ]
    print("4. Sensitivity of the expected NPV")
    print(pd.DataFrame([{"what changes": k, "NPV": money(v), "vs base": money(v - base)} for k, v in sens])
          .to_markdown(index=False))

    print("\n5. Capacity behind the temps (peak month, hours)")
    temps_hours_month = 2 * 160
    crow = []
    for label, over in [("base: accuracy 80%, review 2 min", {}),
                        ("accuracy 70%", {"accuracy": 0.7}), ("accuracy 90%", {"accuracy": 0.9}),
                        ("review 3 min", {"review_minutes": 3}), ("review 4.4 min", {"review_minutes": 4.4})]:
        r = monthly(**over)
        crow.append({"case": label, "net hours a month": r["net_hours"], "net value a month": money(r["net_value_ils"]),
                     "breakeven months": r["breakeven_months"] if r["breakeven_months"] and r["breakeven_months"] <= 120 else "over 10 years",
                     "share of two temps' hours": f"{r['net_hours'] / temps_hours_month:.0%}"})
    print(pd.DataFrame(crow).to_markdown(index=False))
    print(f"\nTwo full-time temps give about {temps_hours_month} hours a month in the peak. The pilot alone frees"
          f" {m['net_hours']}; the temps decision needs the date fix's hours too (lesson 03.7, step 6).")

    if args.csv:
        out = []
        for c in CLAIMS:
            out.append({"section": "benefit", "item": c["title"], "ledger": "claimed", "amount_ils_year": c["claimed"],
                        "label": c["label"], "class": c["cls"], "note": ""})
            for a in c["adj"]:
                out.append({"section": "benefit", "item": c["title"], "ledger": a[0], "amount_ils_year": a[1],
                            "label": c["label"], "class": c["cls"], "note": a[2]})
        out.append({"section": "cost", "item": "Build (one-off)", "ledger": "", "amount_ils_year": -BUILD,
                    "label": "estimate", "class": "cash", "note": "year 0"})
        out.append({"section": "cost", "item": "Running", "ledger": "", "amount_ils_year": -round(running_year),
                    "label": "estimate", "class": "cash", "note": "years 1-3"})
        pd.DataFrame(out).to_csv(args.csv, index=False, encoding="utf-8", lineterminator="\n")
        print(f"\nWrote {args.csv}")


if __name__ == "__main__":
    main()
