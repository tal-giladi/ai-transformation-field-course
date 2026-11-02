"""Lessons 08.3 and 08.5 (Track B): the numbers behind the one-page case, with every input in one place.

    python case_model.py

Change the inputs at the top and run again: that is the point. Labels follow the course: measured
(from the data room), directional (from a sample or a reading), assumed (a judgement to be measured later).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))

from fieldkit.cost import breakeven_months, npv, pilot_value, token_cost

FX = 3.136                      # ₪ per US$, Bank of Israel representative rate, 2 Nov 2026 (measured)
AGENT_HOURLY = 13_800 / 157     # ₪ fully loaded per paid hour (finance summary; 157 paid hours a month)
AGENT_CONTACTS = 39_500         # a month, Q3 (measured: extract x 100)
AHT_LIKE_FOR_LIKE = 8.9         # minutes, from 15 June (measured)

# 1. Policy first + refund clock: contacts avoided (shares directional, reductions assumed)
mix = {  # share in the 2,000 written tickets, assumed reduction
    "refund status": (0.121, 0.70),
    "fee or credit dispute": (0.056, 0.70),
    "returns-policy question": (0.077, 0.50),
    "complaint or legal threat": (0.021, 0.50),
}
avoided = 0
print("== Policy first + refund clock (directional shares x assumed reductions)")
for name, (share, cut) in mix.items():
    n = AGENT_CONTACTS * share * cut
    avoided += n
    print(f"{name:28s} {AGENT_CONTACTS * share:7,.0f} a month, -{cut:.0%} -> {n:6,.0f} avoided")
hours = avoided * AHT_LIKE_FOR_LIKE / 60
print(f"total avoided {avoided:,.0f} a month = {hours:,.0f} agent-hours = ₪{hours * AGENT_HOURLY:,.0f} of capacity (not cash)")

# 2. The chatbot's cost per truly resolved chat (October bill; recontact measured on logged-in sessions)
bill_usd = 4_800 + 6_000 * 0.85
truly = 6_000 * (1 - 0.641)
print("\n== Chatbot, October")
print(f"bill US${bill_usd:,.0f} = ₪{bill_usd * FX:,.0f}; truly resolved ≈ {truly:,.0f}; "
      f"₪{bill_usd * FX / truly:.1f} per truly resolved chat vs an agent chat ₪{AHT_LIKE_FOR_LIKE / 60 * AGENT_HOURLY:.1f}")

# 3. Agent-assist (inputs assumed until shadow mode; acceptance from the offline rating)
per_ticket = token_cost(2_800, 450, model="claude-sonnet-5-5")
base = dict(volume=22_000, automation_rate=0.6, accuracy=0.8, minutes_saved=4.0, review_minutes=1.0,
            rework_minutes=3.0, hourly_cost=round(AGENT_HOURLY), cost_per_item_usd=per_ticket, usd_to_ils=FX,
            fixed_monthly=12_000)
v = pilot_value(**base)
print("\n== Agent-assist")
print(v)
print(f"breakeven on a ₪150,000 build: {breakeven_months(150_000, v['net_value_ils'])} months; "
      f"NPV over 36 months at 14%: ₪{npv([-150_000] + [v['net_value_ils']] * 36, 0.14):,.0f}")
for key, val in [("accuracy", 0.7), ("accuracy", 0.6), ("review_minutes", 1.5), ("review_minutes", 2.0),
                 ("minutes_saved", 3.0), ("minutes_saved", 2.5)]:
    print(f"  {key} = {val}: ₪{pilot_value(**{**base, key: val})['net_value_ils']:,} a month")
