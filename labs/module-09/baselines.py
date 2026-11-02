"""Meridian Mutual: three cycle-time baselines, where the time goes, and the winter peak (lesson 09.3).

    python baselines.py                 # all sections
    python baselines.py --section peak  # one section: baselines | segments | documents | peak | money

Reads the data room in labs/module-09/data-room. Prints tables; changes nothing.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
sys.stdout.reconfigure(encoding="utf-8")

import pandas as pd  # noqa: E402

from fieldkit.baseline import summarize  # noqa: E402
from fieldkit.data import data_room, load  # noqa: E402

ROOM = data_room("module-09")
SAMPLE_EVERY = 40          # the register is every 40th claim number
HOURLY_COST = 145          # ₪ fully loaded per handler hour (CFO's planning figure, finance-summary)


def days(a: pd.Series, b: pd.Series) -> pd.Series:
    return (b - a).dt.total_seconds() / 86400


def fmt(s: dict) -> str:
    return f"n={s['n']:,}  median {s['median']:.1f}  p75 {s['p75']:.1f}  p90 {s['p90']:.1f}"


def load_all():
    reg = load(ROOM / "claims" / "claims_register_sample.csv")
    pay = load(ROOM / "finance" / "claim_payments.csv")
    crm = load(ROOM / "claims" / "crm_contacts.csv")
    req = load(ROOM / "claims" / "doc_requests.csv")
    return reg, pay, crm, req


def baselines(reg, pay, crm, req) -> None:
    print("\n=== 1. Three baselines for 'claim cycle time' ===")
    print("(a) The dashboard's definition, recomputed on the sample: file complete -> decision, SIU excluded,"
          " decisions Jan-Oct 2026")
    d = reg[(reg.decision_at.dt.year == 2026) & (reg.siu_referred == "N")].copy()
    x = days(d.file_complete_at, d.decision_at)
    print(f"    mean {x.mean():.1f} days, {fmt(summarize(x))}, within 30 days {(x <= 30).mean() * 100:.1f}%")
    print("(b) Kalanit: registered -> closed, claims closed Jan-Oct 2026")
    c = reg[(reg.closed_at.dt.year == 2026)]
    print(f"    {fmt(summarize(days(c.registered_at, c.closed_at)))}")
    print("(c) The claimant's wait: first contact in the CRM (FNOL) -> last indemnity payment in the ERP,"
          " direct channels, FNOL May-Oct 2026, paid by 4 Nov")
    fnol = crm[crm.contact_type == "fnol"].copy()
    # FNOL rows logged before the claim number existed: join on policy and the nearest claim
    with_ref = fnol[fnol.claim_id.notna()][["claim_id", "contact_at"]]
    no_ref = fnol[fnol.claim_id.isna()][["policy_id", "contact_at"]]
    fixed = no_ref.merge(reg[["policy_id", "claim_id"]], on="policy_id", how="inner")
    fnol_all = pd.concat([with_ref, fixed[["claim_id", "contact_at"]]]).drop_duplicates("claim_id")
    ind = pay[pay.payee_type.isin(["claimant", "garage"])].groupby("claim_id").paid_date.max().reset_index()
    j = fnol_all.merge(ind, on="claim_id")
    paid_day = pd.to_datetime(j.paid_date.dt.date)
    w = (paid_day - pd.to_datetime(j.contact_at.dt.tz_localize(None).dt.date)).dt.days
    print(f"    {fmt(summarize(w))}   (FNOL rows without a claim number: {len(no_ref)}, matched on policy: {len(fixed)})")
    print("    same, all channels, from Kalanit's reported_date (agents' claims included), paid in 2026:")
    j2 = reg.merge(ind, on="claim_id")
    j2 = j2[j2.paid_date.dt.year == 2026]
    w2 = (pd.to_datetime(j2.paid_date.dt.date) - pd.to_datetime(j2.reported_date.dt.date)).dt.days
    print(f"    {fmt(summarize(w2))}")
    for ch in ["agent", "web", "phone", "app"]:
        s = summarize(w2[j2.channel == ch])
        print(f"      {ch:6s} {fmt(s)}")


def segments(reg, pay, crm, req) -> None:
    print("\n=== 2. Where the time goes (claims decided Jan-Oct 2026, sample) ===")
    d = reg[reg.decision_at.dt.year == 2026].copy()
    first_req = req[req["round"] == 1].groupby("claim_id").requested_at.min()
    d = d.join(first_req, on="claim_id")
    ind = pay[pay.payee_type.isin(["claimant", "garage"])].groupby("claim_id").paid_date.max()
    d = d.join(ind, on="claim_id")
    rep = pd.to_datetime(d.reported_date.dt.date).dt.tz_localize("Asia/Jerusalem")
    paid = pd.to_datetime(d.paid_date.dt.date).dt.tz_localize("Asia/Jerusalem")
    segs = {
        "reported -> registered (intake)": days(rep, d.registered_at),
        "registered -> first document request": days(d.registered_at, d.requested_at),
        "first request -> file complete (document chase)": days(d.requested_at, d.file_complete_at),
        "file complete -> decision (the dashboard's clock)": days(d.file_complete_at, d.decision_at),
        "decision -> payment": days(d.decision_at, paid),
    }
    print(f"{'segment':52s} {'median':>7s} {'mean':>7s}")
    for k, v in segs.items():
        print(f"{k:52s} {v.median():7.1f} {v.mean():7.1f}")
    print("  by SIU referral (median days, file complete -> decision):")
    for flag, g in d.groupby("siu_referred"):
        print(f"    siu_referred={flag}: {days(g.file_complete_at, g.decision_at).median():.1f}  (n={len(g)})")


def documents(reg, pay, crm, req) -> None:
    print("\n=== 3. Document requests (sample, all claims) ===")
    rounds = req.groupby("claim_id")["round"].max()
    print(f"claims with requests: {len(rounds):,}; mean rounds {rounds.mean():.2f}; "
          f"share with 2+ rounds {(rounds >= 2).mean() * 100:.1f}%; 3+ rounds {(rounds >= 3).mean() * 100:.1f}%")
    later = req[req["round"] >= 2].copy()
    later["n_docs"] = later.documents_requested.str.count(";") + 1
    std_share = later.n_on_standard_list.sum() / later.n_docs.sum()
    print(f"documents asked for in round 2 or later: {later.n_docs.sum():,}; "
          f"on the line's standard day-one list: {std_share * 100:.1f}%")
    # gap between receiving one round and asking for the next, in working days (Sun-Thu)
    req = req.sort_values(["claim_id", "round"]).copy()
    req["prev_received"] = req.groupby("claim_id").all_received_at.shift()
    gaps = req.dropna(subset=["prev_received"])
    import numpy as np
    wd = np.busday_count(gaps.prev_received.dt.date.values.astype("datetime64[D]"),
                         gaps.requested_at.dt.date.values.astype("datetime64[D]"), weekmask="1111001")
    print(f"next request sent more than 14 working days after the previous documents arrived: "
          f"{(wd > 14).mean() * 100:.1f}% of {len(wd):,} follow-up requests")
    reg2 = reg.join(req[req["round"] == 1].groupby("claim_id").requested_at.min(), on="claim_id")
    rep = pd.to_datetime(reg2.reported_date.dt.date)
    fr = pd.to_datetime(reg2.requested_at.dt.tz_localize(None).dt.date)
    lag = (fr - rep).dt.days
    print(f"first document list sent on the day the claim was reported: {(lag <= 0).mean() * 100:.1f}%; "
          f"median days to first list {lag.median():.0f}")


def peak(reg, pay, crm, req) -> None:
    print("\n=== 4. Volume and speed by month (sample x 40 = company volume) ===")
    reg = reg.copy()
    reg = reg[reg.registered_at.dt.date < pd.Timestamp("2026-11-01").date()]
    reg["month"] = reg.registered_at.dt.strftime("%Y-%m")
    reg["intake_days"] = days(pd.to_datetime(reg.reported_date.dt.date).dt.tz_localize("Asia/Jerusalem"), reg.registered_at)
    t = reg.groupby("month").agg(claims=("claim_id", "size"), home=("line", lambda s: (s == "home").sum()),
                                 intake_median=("intake_days", "median"))
    t["claims_company"] = t.claims * SAMPLE_EVERY
    t["home_company"] = t.home * SAMPLE_EVERY
    print(t[["claims_company", "home_company", "intake_median"]].round(1).to_string())
    print("Proposed pilot window: 1 December 2026 - 28 February 2027.")


def money(reg, pay, crm, req) -> None:
    print("\n=== 5. Handler time, from the QA time study (ops/intake-time-study-2026-10.csv) ===")
    ts = load(ROOM / "ops" / "intake-time-study-2026-10.csv")
    cols = ["minutes_sorting", "minutes_keying", "minutes_verifying_prefill", "minutes_finding_missing_docs"]
    print(ts.groupby("smart_intake_used")[cols].mean().round(1).to_string())
    print(ts.groupby("claimant_lang")[["minutes_keying", "minutes_verifying_prefill"]].mean().round(1).to_string())
    yearly = len(reg[reg.registered_at.dt.year == 2025]) * SAMPLE_EVERY
    print(f"claims registered in 2025 (sample x {SAMPLE_EVERY}): {yearly:,}")
    for c in cols:
        h = yearly * ts[c].mean() / 60
        print(f"  {c:30s} {ts[c].mean():5.1f} min/claim -> {h:8,.0f} h/yr -> ₪{h * HOURLY_COST:,.0f}")


SECTIONS = {"baselines": baselines, "segments": segments, "documents": documents, "peak": peak, "money": money}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--section", choices=list(SECTIONS))
    a = ap.parse_args()
    data = load_all()
    for name, fn in SECTIONS.items():
        if a.section in (None, name):
            fn(*data)
