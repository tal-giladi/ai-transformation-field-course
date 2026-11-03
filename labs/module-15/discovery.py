"""Crescent Bank discovery numbers (lessons 15.2 and 15.3), Track B.

    python discovery.py

Reads the data room by relative path and prints what it finds: the register's shape and gaps, rows
that are the same build, pilots that are in real use, AI spend outside the register, the review
queue, the assistant's usage with two denominators, contracts that renew soon, and the money.
No network, no LLM.
"""
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
import pandas as pd  # noqa: E402

ROOM = Path(__file__).resolve().parent / "data-room"
TODAY = date(2027, 1, 3)


def read(rel: str) -> pd.DataFrame:
    return pd.read_csv(ROOM / rel, dtype=str, keep_default_na=False)


def ils(v: str) -> float:
    """'₪248,000', '248k' or '248000' -> 248000.0"""
    s = str(v).replace("₪", "").replace(",", "").strip()
    if not s:
        return 0.0
    return float(s[:-1]) * 1000 if s.lower().endswith("k") else float(s)


def when(v: str) -> pd.Timestamp:
    he = ["ינואר", "פברואר", "מרץ", "אפריל", "מאי", "יוני", "יולי", "אוגוסט", "ספטמבר", "אוקטובר", "נובמבר", "דצמבר"]
    v = v.strip()
    for i, m in enumerate(he, 1):
        if v.startswith(m):
            return pd.Timestamp(int(v.split()[-1]), i, 1)
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d.%m.%y"):
        try:
            return pd.to_datetime(v, format=fmt)
        except ValueError:
            pass
    return pd.NaT


def section(title: str) -> None:
    print(f"\n=== {title}")


def register() -> pd.DataFrame:
    reg = read("ai/pilot-register-2026-12.csv")
    dirx = read("people/staff-directory-extract.csv")
    reg["start"] = reg.start_date.map(when)
    reg["budget"] = reg.budget_2027_ils.map(ils)
    reg["months_running"] = ((pd.Timestamp(TODAY) - reg.start).dt.days / 30.4).round(1)
    section("Register")
    print(f"rows: {len(reg)}; stages: {reg.stage.str.strip().value_counts().to_dict()}")
    print(f"baseline measured: {reg.baseline_measured.value_counts().to_dict()}")
    print(f"test set given: {(reg.test_set != '').sum()} of {len(reg)}; depends_on filled: {(reg.depends_on != '').sum()}")
    left = set(dirx[dirx.status == "left"].name)
    for _, r in reg.iterrows():
        if r.business_owner in left:
            print(f"owner has left the bank: {r.pilot_id} {r.pilot_name.strip()} ({r.business_owner})")
        if "/" in r.business_owner:
            print(f"two owners: {r.pilot_id} {r.pilot_name.strip()} ({r.business_owner})")
    section("Rows that share an environment and a test set (the same build?)")
    key = reg[reg.test_set != ""].groupby(["environment", "test_set"])
    for (env, ts), g in key:
        if g.pilot_id.nunique() > 1:
            print(f"{env} / {ts}: {', '.join(g.pilot_id)}  budgets {[int(b) for b in g.budget]}")
    return reg


def in_use(reg: pd.DataFrame) -> None:
    section("Pilots in real use")
    old = reg[reg.stage.str.startswith("Pilot") & (reg.months_running >= 12)]
    print("pilots running 12+ months:", ", ".join(f"{r.pilot_id} ({r.months_running} mo)" for _, r in old.iterrows()))
    faq = read("branches/branch-faq-usage-2026-q4.csv")
    faq["questions"] = faq.questions.astype(int)
    faq["date"] = pd.to_datetime(faq.date)
    weekly = faq.groupby(pd.Grouper(key="date", freq="W-SAT")).questions.sum()
    print(f"Branch FAQ: {faq.branch_code.nunique()} branches, median {int(weekly.median())} questions a week "
          f"(Oct-Dec 2026); thumbs-down {faq.thumbs_down.astype(int).sum() / faq.questions.sum():.1%}")
    for _, r in reg.iterrows():
        n = r.notes.lower()
        if any(w in n for w in ("macro", "live for", "used in", "a/b")):
            print(f"note: {r.pilot_id} {r.notes}")


def outside(reg: pd.DataFrame) -> None:
    section("AI spend and traffic outside the register")
    card = read("finance/card-and-expense-software-2026.csv")
    card["amount_ils"] = card.amount_ils.astype(float)
    vendors = set(read("procurement/vendor-contracts-ai.csv").vendor.str.upper())
    ai = card[card.merchant.str.contains("LLM|AI", regex=True)]
    for (m, who), g in ai.groupby(["merchant", "cardholder_or_claimant"]):
        if not any(v.split()[0] in m for v in vendors):
            print(f"{m:22s} {who:18s} {g.source.iloc[0]:13s} {len(g):2d} lines  ₪{g.amount_ils.sum():,.0f}  "
                  f"{g.date.min()} to {g.date.max()}")
    px = read("security/proxy-ai-hosts-2026-q4.csv")
    px[["requests", "upload_kb"]] = px[["requests", "upload_kb"]].astype(int)
    un = px[~px.category.str.startswith("Sanctioned")]
    t = un.groupby(["department", "host", "policy_action"])[["requests", "upload_kb"]].sum()
    print(t.sort_values("upload_kb", ascending=False).to_string())


def queue(reg: pd.DataFrame) -> None:
    section("Model Committee queue (AI)")
    q = read("governance/model-review-queue-2026-12.csv")
    w = q.wait_days_at_2026_12_31.astype(int)
    print(f"submissions {len(q)}; status {q.status.value_counts().to_dict()}")
    print(f"wait in days: median {int(w.median())}, longest {int(w.max())} ({q.loc[w.idxmax(), 'pilot_id']})")
    slots, per_model = 3, 2
    print(f"3 AI slots a quarter, full validation 2 slots each: {slots / per_model} models a quarter; "
          f"{len(reg)} rows x 2 = {len(reg) * 2} slots = {len(reg) * 2 / slots:.1f} quarters")
    inv = read("governance/model-inventory-2026-12.csv")
    print(f"traditional model inventory: {len(inv)} models; phase-in 369: {inv.phase_in_369.value_counts().to_dict()}; "
          f"generative AI entries: {(inv.ai_flag != '').sum()} flagged ML, 0 generative")


def assistant() -> None:
    section("Tzofen Assist usage: which denominator?")
    u = read("ai/assistant-usage-2026.csv")
    for c in ("seats_assigned", "users_onboarded", "weekly_active_users", "agent_studio_sessions"):
        u[c] = u[c].astype(int)
    dec = u[u.week_start >= "2026-12-01"].groupby("week_start")[["seats_assigned", "users_onboarded", "weekly_active_users"]].sum()
    a, s, o = dec.weekly_active_users.mean(), dec.seats_assigned.mean(), dec.users_onboarded.mean()
    print(f"December: {a:.0f} weekly active / {s:.0f} seats = {a / s:.0%}; / {o:.0f} onboarded = {a / o:.0%}")
    pilot = u[(u.week_start >= "2026-10-01") & (u.week_start < "2026-11-29")]
    g = pilot.groupby("department")[["seats_assigned", "weekly_active_users", "agent_studio_sessions"]].mean()
    g["active_share"] = (g.weekly_active_users / g.seats_assigned).round(2)
    print("Oct-Nov, 300 pilot seats:\n" + g.sort_values("active_share", ascending=False).round(1).to_string())


def contracts() -> None:
    section("Contracts that renew by themselves in the next 120 days")
    c = read("procurement/vendor-contracts-ai.csv")
    c["end"] = pd.to_datetime(c.end)
    c["notice_by"] = c.end - pd.to_timedelta(c.notice_days.astype(int), unit="D")
    soon = c[(c.auto_renew == "Y") & (c.notice_by <= pd.Timestamp(TODAY) + pd.Timedelta(days=120))]
    for _, r in soon.sort_values("notice_by").iterrows():
        late = " (notice date passed)" if r.notice_by < pd.Timestamp(TODAY) else ""
        print(f"{r.contract_id} {r.vendor:22s} {r.owner_unit:18s} ends {r.end.date()} notice by {r.notice_by.date()}{late}"
              f"  +{r.renewal_term_months} months  ₪{int(r.annual_value_ils):,}/yr  DPA {r.dpa_signed}")


def money(reg: pd.DataFrame) -> None:
    section("Money")
    total = reg.budget.sum()
    shared = reg[reg.test_set != ""].groupby(["environment", "test_set"]).pilot_id.transform("count") > 1
    shared = shared.reindex(reg.index, fill_value=False)
    dup = shared & (reg.submitted_to_model_committee == "")  # the copy is the row that never went to committee
    print(f"unit AI lines 2027 (43 rows): ₪{total:,.0f}; rows that repeat an earlier build: ₪{reg[dup].budget.sum():,.0f} "
          f"({', '.join(reg[dup].pilot_id)})")
    print(f"OPS-01 assistant line: ₪{reg.loc[reg.pilot_id == 'OPS-01', 'budget'].iloc[0]:,.0f}; "
          f"central programme ₪11,000,000; 15% of all AI spend: ₪{(total + 11_000_000) * 0.15:,.0f}")


if __name__ == "__main__":
    pd.set_option("display.width", 160)
    r = register()
    in_use(r)
    outside(r)
    queue(r)
    assistant()
    contracts()
    money(r)
