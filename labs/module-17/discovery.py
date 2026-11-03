"""Vantage Logistics discovery numbers (lessons 17.2 and 17.3), Track B.

    python discovery.py            # all sections, no AI
    python discovery.py --llm      # + an LLM reads the dispatchers' free-text override reasons

Reads the data room by relative path and prints what it finds: AI outside the register, where Tzir
Route is really used, licences billed against licences used, how pre-filled declarations are
reviewed, the incident's scope from the logs, the savings claimed against what telematics, payroll
and contact volumes show, and the money. No network unless you pass --llm.
"""
import argparse
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
import pandas as pd  # noqa: E402

ROOM = Path(__file__).resolve().parent / "data-room"


def read(rel: str) -> pd.DataFrame:
    return pd.read_csv(ROOM / rel, dtype=str, keep_default_na=False)


def num(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s, errors="coerce")


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def section(title: str) -> None:
    print(f"\n=== {title} ===")


def outside_register() -> None:
    section("1. AI outside the former lead's register")
    reg = read("ai/ai-register-2027-03.csv")
    print(f"Register: {len(reg)} rows: " + ", ".join(reg.system))
    lic = read("it/licence-usage-2027-05.csv")
    for s in sorted(set(lic.system) - set(reg.system)):
        print(f"  licence export only: {s}")
    con = read("vendor/contracts-ai.csv")
    for _, c in con[con.notes.str.contains("AI|model", case=False)].iterrows():
        if not any(x in c["product"] for x in reg.system):
            print(f"  contract note: {c['vendor']} - {c['notes']}")
    card = read("finance/card-and-expense-ai-2027.csv")
    pw = card[card.merchant.str.contains("PROMPTWAY")]
    print(f"  card: {pw.merchant.iloc[0]} on {pw.cardholder_or_claimant.iloc[0]}'s card, {len(pw)} months, "
          f"₪{num(pw.amount_ils).sum():,.0f} (Jan-May), last month US${pw.amount_original.iloc[-1]}")
    px = read("it/proxy-ai-hosts-2027-q2.csv")
    px["requests"] = num(px.requests)
    px["upload_kb"] = num(px.upload_kb)
    nons = px[~px.category.str.startswith("Sanctioned")]
    print(nons.groupby(["department", "host", "action"])[["requests", "upload_kb"]].sum().to_string())


def route_use() -> None:
    section("2. Tzir Route: share of routes dispatched as the tool planned, by region and month")
    r = read("operations/route-daily-by-depot.csv")
    for c in ("routes", "routes_tool_planned", "routes_dispatched_as_planned", "routes_overridden", "stops", "late_stops"):
        r[c] = num(r[c])
    r["month"] = r.date.str[:7]
    g = r.groupby(["month", "region"])[["routes", "routes_dispatched_as_planned"]].sum()
    print((g.routes_dispatched_as_planned / g.routes).unstack().round(2).to_string())
    n = r[(r.region == "North") & (r.date >= "2027-01-01")].groupby("depot_code")[["routes_overridden", "routes_tool_planned"]].sum()
    print("North override rate by depot (2027):", (n.routes_overridden / n.routes_tool_planned).round(2).to_dict())
    s = r[r.region == "South"]
    for a, b, label in (("2026-10-01", "2027-01-09", "before"), ("2027-01-10", "2027-02-24", "with Route"),
                        ("2027-02-25", "2027-06-03", "after pull-back")):
        x = s[(s.date >= a) & (s.date <= b)]
        print(f"South late stops {label}: {x.late_stops.sum() / x.stops.sum():.1%}")
    o = read("operations/dispatcher-overrides-2027.csv")
    print(o.groupby(["region", "reason_code"]).size().unstack(fill_value=0).to_string())


def licences() -> None:
    section("3. Licences billed vs active (31 May 2027)")
    lic = read("it/licence-usage-2027-05.csv")
    for c in ("seats_billed", "active_30d"):
        lic[c] = num(lic[c])
    t = lic.groupby("system")[["seats_billed", "active_30d"]].sum()
    print(t.to_string())
    inv = read("finance/ap-invoices-ai.csv")
    may = inv[inv.period == "2027-05"].copy()
    may["amount_ils"] = num(may.amount_ils)
    print("May 2027 invoices by contract (₪):", may.groupby("contract_id").amount_ils.sum().round(0).to_dict())
    print("Billed in May for systems with 0 active users:",
          ", ".join(f"{s}" for s in t[t.active_30d == 0].index))


def customs_review() -> None:
    section("4. Tzir Docs: how pre-fills are reviewed, and the April QA re-check")
    d = read("customs/declarations-prefill-2027-05.csv")
    d["rs"] = num(d.review_seconds)
    d["day"] = pd.to_datetime(d.prefill_created_at.str[:10])
    print(f"Declarations 1 May - 3 Jun: {len(d):,}; median seconds on approval screen: {d.rs.median():.0f}; "
          f"under 30 s: {(d.rs < 30).mean():.0%}; no field edited: {(d.fields_edited == '0').mean():.1%}")
    print("Tariff-code source:", d.hs_code_source.value_counts(normalize=True).round(3).to_dict())
    q = read("customs/qa-sample-2027-04.csv")
    k = (q.material_error == "Y").sum()
    lo, hi = wilson(k, len(q))
    acc = num(q.fields_accepted_without_edit).sum() / num(q.fields_checked).sum()
    print(f"QA April: {k} of {len(q)} with a material error = {k / len(q):.1%} (95% CI {lo:.1%}-{hi:.1%}); "
          f"fields accepted without edit {acc:.1%} (the vendor's 'accuracy')")
    print({c: int((q[c] == "Y").sum()) for c in q.columns if c.endswith("_error") and c != "material_error"})
    st = read("customs/brokerage-staffing-monthly.csv")
    print(st[["month", "licensed_agents_fte", "open_posts_frozen", "declarations_per_agent_day", "overtime_hours",
              "kpi_target_per_agent_day"]].tail(7).to_string(index=False))


def incident_scope() -> dict:
    section("5. Incident INC-27-0518-01: scope from the logs")
    d = read("customs/declarations-prefill-2027-05.csv")
    m = d[d.doc_owner_customer != d.customer_code].copy()
    m["submitted"] = m.status != "returned by agent"
    by = m.groupby("model_version").agg(mismatches=("decl_id", "size"), submitted=("submitted", "sum"),
                                         first=("prefill_created_at", "min"), last=("prefill_created_at", "max"))
    print(by.to_string())
    print("Declaring customers:", m.customer_code.nunique(), "| document owners:", m.doc_owner_customer.nunique(),
          "| owner C1022 (B2C consolidator):", int((m.doc_owner_customer == "C1022").sum()),
          "| C1007 declaring:", int((m.customer_code == "C1007").sum()), "| C1007 documents elsewhere:",
          int((m.doc_owner_customer == "C1007").sum()))
    print("Status of mismatched declarations:", m.status.value_counts().to_dict())
    a = read("portal/document-access-log-2027-05.csv")
    ix = read("portal/document-index-2027-05.csv")
    j = a.merge(ix, on="doc_id")
    x = j[j.viewer_customer != j.owner_customer]
    xd = x.drop_duplicates("doc_id")
    rec = num(xd.records).sum()
    after = x[x.event_time >= "2027-05-19"]
    print(f"Portal: {len(x)} opens of {x.doc_id.nunique()} documents by users of {x.viewer_customer.nunique()} "
          f"other customers; {len(after)} opens after the Assist feature was switched off (19 May), "
          f"all via {after.channel.unique().tolist()}")
    print(xd.groupby(["owner_customer", "doc_type"]).size().to_string())
    print(f"Records of individuals in opened B2C manifests: {rec:,.0f} "
          f"(before 19 May {num(xd[xd.doc_id.isin(x[x.event_time < '2027-05-19'].doc_id)].records).sum():,.0f})")
    q = read("customs/customs-queries-2027.csv")
    print("Customs queries linked to mismatched declarations:", int(q.decl_id.isin(m.decl_id).sum()),
          "| goods held:", int(((q.goods_held == "Y") & q.decl_id.isin(m.decl_id)).sum()))
    return {"mismatches": len(m), "submitted": int(m.submitted.sum()), "records": rec}


def savings() -> None:
    section("6. Savings claimed vs measured")
    f = read("operations/fleet-km-fuel-monthly.csv")
    for c in ("km_telematics", "stops", "fuel_cost_ils"):
        f[c] = num(f[c])
    f["kps"] = f.km_telematics / f.stops
    pre = f[(f.month >= "2025-11") & (f.month <= "2026-04")].groupby("region").kps.mean()
    post = f[(f.month >= "2026-12") & (f.month <= "2027-05")].groupby("region").kps.mean()
    ch = (post / pre - 1)
    print("Km per stop, Dec-May vs Nov-Apr a year earlier:", (ch * 100).round(1).to_dict())
    north_fuel = f[(f.region == "North") & (f.month >= "2026-12")].fuel_cost_ils.mean() * 12
    print(f"North fuel ₪{north_fuel:,.0f} a year; a {-ch['North']:.1%} km reduction is about "
          f"₪{north_fuel * -ch['North']:,.0f} a year (fuel only)")
    w = read("operations/warehouse-overtime-weekly.csv")
    for c in ("overtime_hours", "overtime_cost_ils", "agency_cost_ils"):
        w[c] = num(w[c])
    w["post"] = w.week_start >= "2027-01-03"
    g = w.groupby(["dc", "post"])[["overtime_hours", "overtime_cost_ils", "agency_cost_ils"]].mean()
    did = (g.loc[("Modi'in DC", True)] / g.loc[("Modi'in DC", False)]) / (g.loc[("Ashdod DC", True)] / g.loc[("Ashdod DC", False)]) - 1
    yearly = -(did.overtime_cost_ils * g.loc[("Modi'in DC", False)].overtime_cost_ils
               + did.agency_cost_ils * g.loc[("Modi'in DC", False)].agency_cost_ils) * 52
    print(f"Warehouse: Modi'in overtime {did.overtime_hours:+.1%} against Ashdod (difference in differences); "
          f"about ₪{yearly:,.0f} a year incl. agency")
    c = read("portal/cs-contacts-weekly-2027.csv")
    c["contacts"] = num(c.contacts)
    c["post"] = c.week_start >= "2027-03-14"
    wk = c.groupby("post").contacts.sum() / c.groupby("post").week_start.nunique()
    print(f"Customer-service contacts a week: before Assist {wk[False]:,.0f}, after {wk[True]:,.0f}")
    s = read("portal/assist-sessions-2027.csv")
    print(f"Assist sessions handed to a person: {(s.handed_to_human == 'Y').mean():.0%} of {len(s):,}")
    r = read("operations/route-daily-by-depot.csv")
    t = r[(r.km_naive_baseline != "") & (r.date <= "2027-05-31")]
    print(f"Vendor's km saved = naive - plan = {(num(t.km_naive_baseline) - num(t.km_tool_plan)).sum():,.0f}; "
          f"actual km on those days are not used by the dashboard")


def money() -> None:
    section("7. The money")
    c = read("finance/ai-programme-cost-2027.csv")
    for k in ("budget_ils", "actual_ils", "forecast_ils"):
        c[k] = num(c[k]).fillna(0)
    c["year"] = c.actual_ils + c.forecast_ils
    t = c.groupby("line")[["budget_ils", "year"]].sum()
    print(t.round(0).to_string())
    print(f"Budget ₪{t.budget_ils.sum():,.0f}; actual + forecast ₪{t.year.sum():,.0f}; "
          f"overrun ₪{t.year.sum() - t.budget_ils.sum():,.0f} ({t.year.sum() / t.budget_ils.sum() - 1:.0%})")
    con = read("vendor/contracts-ai.csv")
    tz = con[con.contract_id.str.startswith("TZ-OF")]
    print("Tzir order forms:", dict(zip(tz.contract_id, num(tz.total_value_ils))),
          f"together ₪{num(tz.total_value_ils).sum():,.0f}; signed {tz.signed_on.min()} to {tz.signed_on.max()}")


def llm_reasons() -> None:
    section("8. LLM reading of override reasons (second opinion, not a decision)")
    from fieldkit.llm import complete
    o = read("operations/dispatcher-overrides-2027.csv")
    texts = sorted(set(o.reason_text) - {""})
    system = ("You label why a truck dispatcher overrode a route plan. Reply with one label only: ROAD_CLOSED, "
              "SECURITY_RESTRICTION, CUSTOMER_WINDOW, DRIVER_HOURS, TRAFFIC, PLAN_ERROR, DRIVER_REFUSED, OTHER. "
              "The text may be Hebrew, Arabic, Russian, Amharic or English.")
    labels = {t: complete(t, system=system).text.strip().split()[0] for t in texts}
    o["llm"] = o.reason_text.map(labels).fillna("")
    blank = o[o.reason_code == ""]
    print(f"{len(texts)} distinct texts; {len(blank)} overrides without a code. LLM labels for those:")
    print(blank.llm.value_counts().to_string())
    agree = (o[o.reason_code != ""].reason_code == o[o.reason_code != ""].llm).mean()
    print(f"Agreement with the dispatchers' own codes: {agree:.0%}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--llm", action="store_true", help="classify the free-text override reasons with an LLM")
    args = ap.parse_args()
    outside_register()
    route_use()
    licences()
    customs_review()
    incident_scope()
    savings()
    money()
    if args.llm:
        llm_reasons()


if __name__ == "__main__":
    main()
