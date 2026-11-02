"""Meridian Mutual: outcome test of SIU referrals before and after Fraud Insight (lesson 09.4).

    python bias_test.py                      # referral rates by group, before vs after 6 Sep 2026
    python bias_test.py --by region          # another grouping: claimant_lang | region | risk_area | age | channel
    python bias_test.py --factors            # which Fraud Insight factors fire, by group
    python bias_test.py --outcomes           # what SIU referrals turned into (siu/siu_case_log.csv)

An outcome test does not need to know how the score works: it compares what happened to similar
claims in different groups. Rates come with Wilson 95% intervals; a ratio built on fewer than
about 20 referrals is a lead to investigate, not a finding.
"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
sys.stdout.reconfigure(encoding="utf-8")

import pandas as pd  # noqa: E402

from fieldkit.data import data_room, load  # noqa: E402

ROOM = data_room("module-09")
GO_LIVE = pd.Timestamp("2026-09-06", tz="Asia/Jerusalem")


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - m) / d, (c + m) / d)


def motor() -> pd.DataFrame:
    m = load(ROOM / "claims" / "motor_claims_2026-07_to_10.csv")
    risk = set(pd.read_csv(ROOM / "vendor" / "risk-areas-v3.csv", dtype=str).area_code)
    m["period"] = (m.registered_date >= GO_LIVE).map({False: "1 before (handlers)", True: "2 after (Fraud Insight)"})
    m["risk_area"] = m.postal_area.isin(risk).map({True: "on list", False: "not on list"})
    m["age"] = m.claimant_age_band.fillna("missing")
    m["referred"] = m.siu_referred == "Y"
    return m


def rates(m: pd.DataFrame, by: str, ref: str | None) -> None:
    print(f"\nSIU referral rate of motor claims by {by}, July-October 2026 (all motor claims, not a sample)")
    print(f"{'period':26s} {by:14s} {'claims':>7s} {'referred':>8s} {'rate':>7s} {'95% interval':>16s} {'ratio':>6s}")
    for period, g in m.groupby("period"):
        base = None
        if ref is not None and (g[by] == ref).any():
            r0 = g[g[by] == ref]
            base = r0.referred.mean()
        for val, h in g.groupby(by):
            k, n = int(h.referred.sum()), len(h)
            lo, hi = wilson(k, n)
            ratio = f"{(k / n) / base:5.2f}" if base else "  -  "
            print(f"{period:26s} {str(val):14s} {n:7,d} {k:8d} {k / n * 100:6.1f}% {lo * 100:6.1f}-{hi * 100:5.1f}% {ratio:>6s}")


def factors(m: pd.DataFrame) -> None:
    a = m[m.period.str.startswith("2")].copy()
    a["fi_factors"] = a.fi_factors.fillna("")
    print("\nFraud Insight after go-live: share of claims where each factor fired, by claimant_lang")
    langs = ["he", "ar", "ru", "en", "am"]
    print(f"{'factor':6s} " + " ".join(f"{x:>7s}" for x in langs))
    for f in [f"F{i:02d}" for i in range(1, 15)]:
        row = []
        for lang in langs:
            g = a[a.claimant_lang == lang]
            row.append(f"{g.fi_factors.str.contains(f).mean() * 100:6.1f}%")
        print(f"{f:6s} " + " ".join(row))
    print("\nScore band by claimant_lang (counts)")
    print(a.groupby("claimant_lang").fi_band.value_counts().unstack(fill_value=0).to_string())
    a["proxy_points"] = a.fi_factors.str.contains("F08") * 10 + a.fi_factors.str.contains("F09") * 15
    a["score_without_proxies"] = a.fi_score - a.proxy_points
    a["would_refer_without"] = a.score_without_proxies >= 50
    print("\nIf F08 (interpreter) and F09 (risk area) were removed, auto-referrals by claimant_lang:")
    t = a.groupby("claimant_lang").agg(claims=("claim_id", "size"), auto_now=("fi_band", lambda s: (s == "refer").sum()),
                                       auto_without=("would_refer_without", "sum"))
    print(t.to_string())


def outcomes() -> None:
    s = load(ROOM / "siu" / "siu_case_log.csv")
    print("\nSIU case log (cases opened 1 Jul 2025 - 4 Nov 2026): outcome by referral source")
    print(s.groupby("referral_source").outcome.value_counts().unstack(fill_value=0).to_string())
    closed = s[s.status == "closed"]
    print("\nConfirmed fraud as a share of CLOSED cases, by referral source")
    for src, g in closed.groupby("referral_source"):
        k, n = int((g.outcome == "confirmed_fraud").sum()), len(g)
        lo, hi = wilson(k, n)
        print(f"  {src:20s} {k:4d} of {n:5d} = {k / n * 100:5.1f}%  ({lo * 100:.1f}-{hi * 100:.1f}%)")
    y = closed[closed.closed_at.dt.year == 2026]
    rep = pd.to_numeric(y.amount_saved_reported, errors="coerce").fillna(0)
    print(f"\n'Fraud prevented' as the SIU reports it, cases closed Jan-Oct 2026: ₪{rep.sum():,.0f}")
    for o, g in y.assign(rep=rep).groupby("outcome"):
        print(f"  of which {o:18s} ₪{g.rep.sum():12,.0f}  ({len(g)} cases)")
    conf = y[y.outcome == "confirmed_fraud"]
    print(f"Claimed amount on confirmed-fraud cases only: ₪{conf.claimed_amount.sum():,.0f}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--by", default="claimant_lang", choices=["claimant_lang", "region", "risk_area", "age", "channel"])
    ap.add_argument("--factors", action="store_true")
    ap.add_argument("--outcomes", action="store_true")
    a = ap.parse_args()
    m = motor()
    if a.factors:
        factors(m)
    elif a.outcomes:
        outcomes()
    else:
        ref = {"claimant_lang": "he", "region": "Center", "risk_area": "not on list", "age": "35-44",
               "channel": "agent"}[a.by]
        rates(m, a.by, ref)
