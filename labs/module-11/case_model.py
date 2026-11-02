"""The Givat Oren case in numbers (lesson 11.3): agent-assistant hours and the content fix, labelled.

    python case_model.py
    python case_model.py --use 0.5 --review 0.6        # change one input at a time

Inputs are the 11.3 assumptions; every output is capacity, not cash. Needs the field kit (labs/common).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
from fieldkit.cost import breakeven_months, pilot_value, token_cost  # noqa: E402

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("--volume", type=float, default=6600, help="permits-family contacts a month (measured)")
ap.add_argument("--use", type=float, default=0.7, help="share of contacts where agents use the assistant (assumed)")
ap.add_argument("--accuracy", type=float, default=0.9, help="share of answers right (from the eval)")
ap.add_argument("--saved", type=float, default=1.5, help="minutes saved on a right answer (assumed)")
ap.add_argument("--review", type=float, default=0.3, help="minutes to read the answer (assumed)")
ap.add_argument("--rework", type=float, default=3.0, help="minutes to fix a wrong answer (assumed)")
ap.add_argument("--hourly", type=float, default=130, help="loaded agent cost, ₪ an hour (directional)")
ap.add_argument("--fixed", type=float, default=6000, help="owner's time and re-tests, ₪ a month (assumed)")
ap.add_argument("--repeat-now", type=float, default=0.35, help="permits-family repeat rate (measured)")
ap.add_argument("--repeat-after", type=float, default=0.20, help="after content, letters, callbacks (assumed)")
ap.add_argument("--handle-min", type=float, default=3.7, help="minutes per contact (measured mean)")
args = ap.parse_args()

fx = 3.136  # ₪ per US$, Bank of Israel, 2 November 2026
per_q = token_cost(2600, 180, "claude-sonnet-5-5")  # list price checked 2 November 2026
v = pilot_value(volume=args.volume, automation_rate=args.use, accuracy=args.accuracy, minutes_saved=args.saved,
                review_minutes=args.review, rework_minutes=args.rework, hourly_cost=args.hourly,
                cost_per_item_usd=per_q, usd_to_ils=fx, fixed_monthly=args.fixed)
print("== E: assistant for 106 agents (directional)")
print(f"Model cost per question: US${per_q:.4f} ≈ ₪{per_q * fx:.3f}")
for k, val in v.items():
    print(f"  {k}: {val}")
print(f"  breakeven on a ₪120,000 build: {breakeven_months(120000, v['net_value_ils'])} months")

avoided = args.volume * (args.repeat_now - args.repeat_after)
hours = avoided * args.handle_min / 60
print("\n== B + C + D: content, letters, callbacks (assumed effect)")
print(f"Contacts avoided a month: {avoided:,.0f}; agent hours: {hours:,.0f}; capacity ≈ ₪{hours * args.hourly:,.0f} a month")
print("\nNeither line is cash: no job changes, and the value that matters is correct answers in four languages.")
