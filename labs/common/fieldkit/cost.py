"""Token costs and pilot economics in one place.

    from fieldkit.cost import token_cost, pilot_value
    token_cost(input_tokens=1_200, output_tokens=300, model="claude-opus-5-5")     # US$ per item
    pilot_value(volume=900, automation_rate=0.6, accuracy=0.92, minutes_saved=6,
                review_minutes=1.5, rework_minutes=10, hourly_cost=95, cost_per_item_usd=0.01,
                usd_to_ils=3.7, fixed_monthly=2_500)
"""
from __future__ import annotations

# US$ per million tokens (input, output). Prices change: check the vendor's pricing page and
# update the date when you use them. Anthropic first-party API prices, checked 2026-11-02.
PRICES = {
    "claude-opus-5-5": (4.00, 20.00),
    "claude-sonnet-5-5": (2.00, 10.00),
    "claude-haiku-5-5": (0.10, 0.50),
    "mock": (0.0, 0.0),
}


def token_cost(input_tokens: int, output_tokens: int, model: str | None = None,
               price_in: float | None = None, price_out: float | None = None) -> float:
    """US$ cost of one call. Give a model from PRICES or your own per-million prices."""
    if price_in is None or price_out is None:
        if model not in PRICES:
            raise KeyError(f"No price for {model!r}: pass price_in and price_out (US$ per million tokens)")
        price_in, price_out = PRICES[model]
    return (input_tokens * price_in + output_tokens * price_out) / 1_000_000


def pilot_value(*, volume: float, automation_rate: float, accuracy: float, minutes_saved: float,
                review_minutes: float, rework_minutes: float, hourly_cost: float,
                cost_per_item_usd: float, usd_to_ils: float, fixed_monthly: float = 0.0) -> dict:
    """Monthly net value in ₪ of a pilot that handles part of a work queue.

    volume           items per month in the queue
    automation_rate  share of items the pilot handles (0-1)
    accuracy         share of handled items that are right after review (0-1)
    minutes_saved    staff minutes saved on a handled item that is right
    review_minutes   staff minutes to check every handled item (the human in the loop)
    rework_minutes   staff minutes to fix a handled item that is wrong
    hourly_cost      fully loaded staff cost per hour, ₪
    cost_per_item_usd  model cost per handled item, US$
    fixed_monthly    licences, hosting, the owner's time, ₪ per month
    """
    handled = volume * automation_rate
    saved_h = handled * accuracy * minutes_saved / 60
    review_h = handled * review_minutes / 60
    rework_h = handled * (1 - accuracy) * rework_minutes / 60
    net_hours = saved_h - review_h - rework_h
    model_cost = handled * cost_per_item_usd * usd_to_ils
    net_value = net_hours * hourly_cost - model_cost - fixed_monthly
    return {
        "handled_items": round(handled),
        "hours_saved": round(saved_h, 1),
        "review_hours": round(review_h, 1),
        "rework_hours": round(rework_h, 1),
        "net_hours": round(net_hours, 1),
        "model_cost_ils": round(model_cost),
        "fixed_ils": round(fixed_monthly),
        "net_value_ils": round(net_value),
        "note": "Hours are capacity, not cash, until someone decides what the freed time is used for.",
    }


def breakeven_months(one_off_cost: float, monthly_net_value: float) -> float | None:
    """Months until the build cost is paid back (None if the pilot never pays back)."""
    return round(one_off_cost / monthly_net_value, 1) if monthly_net_value > 0 else None


def npv(cashflows: list[float], annual_rate: float, periods_per_year: int = 12) -> float:
    """Net present value of cash flows (first one now), discounted at the organization's rate."""
    r = (1 + annual_rate) ** (1 / periods_per_year) - 1
    return round(sum(cf / (1 + r) ** t for t, cf in enumerate(cashflows)), 2)
