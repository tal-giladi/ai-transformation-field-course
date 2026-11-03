"""Vantage Logistics stop/keep audit (lesson 17.5), Track B.

    python audit.py                # the audit table, the money, the incident scope; writes out/audit.csv
    python audit.py --sheet        # also rewrites audit-sheet.csv (the Track A sheet, decisions blank)

Joins what each AI system costs (invoices), who uses it (licence export), what is open about it
(IT tickets, the incident), what the contract lets you do and when (contracts, MSA), and the evidence
of value (discovery.py's numbers), then applies the audit rules written before the list was opened.
The rules decide the first draft; the decision record is yours. No network, no LLM.
"""
import argparse
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pandas as pd  # noqa: E402

from discovery import read, num, incident_scope  # noqa: E402

RULES = """Audit rules, fixed on Sunday 13 June 2027 before the list was opened (17.4):
 R1 Harm open: an open incident or harm to customers or people not yet bounded -> SUSPEND the part that causes it until conditions are met.
 R2 No basis: monitoring people without the consultation the collective agreement requires, or data sent where no agreement covers it -> STOP (or BRING IN if the work is needed).
 R3 Not used: active below 10% of billed seats for 60 days -> STOP or REDUCE to active users plus 10%.
 R4 Value measured with a comparison and risk controlled -> KEEP (with a named owner).
 R5 Value plausible but unmeasured, risk controlled -> KEEP UNDER TEST: 90 days, a measure agreed now.
 R6 Found outside the register -> REGISTER, then apply R1-R5.
 Every action has an owner, a date and the contract step it needs."""

# system id, system, scope, invoice selector (contract, line contains, region), licence selector (system, region)
SYSTEMS = [
    ("AI-01N", "Tzir Route", "North (104 drivers, 6 planners)", ("TZ-OF-101", "", "North"), ("Tzir Route", "North")),
    ("AI-01C", "Tzir Route", "Centre (70 drivers, 8 planners)", ("TZ-OF-101", "", "Centre"), ("Tzir Route", "Centre")),
    ("AI-01S", "Tzir Route", "South (92 drivers, 6 planners)", ("TZ-OF-101", "", "South"), ("Tzir Route", "South")),
    ("AI-01E", "Tzir Route", "Europe (44 drivers, 4 planners)", ("TZ-OF-101", "", "Europe"), ("Tzir Route", "Europe")),
    ("AI-01P", "Tzir Route", "platform fee", ("TZ-OF-101", "platform", "all"), None),
    ("AI-01D", "Tzir Route driver score", "feature, all regions", None, None),
    ("AI-02", "Tzir Docs", "3 customs houses", ("TZ-OF-102", "", "all"), None),
    ("AI-03S", "Tzir Assist", "status answers", ("TZ-OF-103", "subscription", "all"), ("Tzir Assist", "customers")),
    ("AI-03D", "Tzir Assist", "'my documents' feature", None, None),
    ("AI-04", "Kotev Assist", "450 seats", ("KT-2026-04", "", "all"), ("Kotev Assist", None)),
    ("AI-05", "Ayin Drive", "South, 60 cabs", ("AD-2027-01", "", "South"), ("Ayin Drive", "South")),
    ("AI-06", "Nezek Vision", "Modi'in DC", ("NV-2026-11", "", "Centre"), ("Nezek Vision", "Centre")),
    ("AI-07", "Quote add-in", "Sales, 30 seats", ("TQ-2026-09", "", "Sales"), ("Quote add-in", "Sales")),
    ("AI-08", "Warehouse forecast", "Modi'in DC", None, None),
    ("NEW-1", "Mishkal Smart Match", "AP matching in the ERP", None, ("Mishkal Smart Match", "Finance")),
    ("NEW-2", "Meches Pro HS Suggest", "tariff suggestions, release 9.3", None, ("Meches Pro HS Suggest", "Customs")),
    ("NEW-3", "CS e-mail triage (n8n + Promptway API)", "Customer Service", None, None),
    ("NEW-4", "Free online translator", "customs clerks, supplier invoices", None, None),
    ("N/A", "Tzir value dashboard", "a vendor report, not an AI system", None, None),
]

# Evidence and risk per system, from discovery.py and the documents (label: M measured, D directional, C claimed).
FACTS = {
    "AI-01N": ("M: km per stop -4.0% vs a year earlier (telematics); ~₪134k a year fuel", "model trained on 2021-23 traffic; feed broken since 14 Nov 2026; Kiryat Shmona override 56%", "R4", "KEEP and FIX: fix the feed, retrain on 2024-27 data, road closures in the console"),
    "AI-01C": ("M: 0 drivers active; 5 of 8 planners use the plan view", "", "R3", "REDUCE to 5 planner seats, 0 driver seats (MSA 7.4 notice by 1 Jul, from 1 Oct)"),
    "AI-01S": ("M: 0 active since 25 Feb; late stops 8.0% with Route vs 4.0% before", "routes onto closed roads; drivers refused", "R3", "STOP: remove all seats (MSA 7.4 notice by 1 Jul, from 1 Oct)"),
    "AI-01E": ("M: never live; connector never built", "", "R3", "STOP: remove all seats (MSA 7.4 notice by 1 Jul, from 1 Oct)"),
    "AI-01P": ("", "unaffected by 7.4", "R4", "KEEP while Route North runs"),
    "AI-01D": ("none", "used in a disciplinary hearing (24 Feb); no consultation under clause 14", "R2", "STOP: switch off; undertaking to the works committee"),
    "AI-02": ("M: QA material error 7.0% (CI 4.9-9.9%); 'accuracy' 99.1% is fields not edited", "open incident; post-fix mismatches; review median 19 s", "R1", "KEEP WITH CONDITIONS: auto-match off for numeric keys, consignee cross-check, 5% QA, 90-day gate"),
    "AI-03S": ("M: contacts a week 1,970 before, 1,995 after; 49% of sessions handed to a person", "wrong ETAs and fees in tickets", "R5", "KEEP UNDER TEST: 90 days, deflection and wrong-answer rate measured"),
    "AI-03D": ("none", "exposed other customers' documents (incident)", "R1", "STOP permanently; remove from the order form"),
    "AI-04": ("M: 112 of 450 active in 30 days", "", "R3", "REDUCE to 150 seats at renewal (notice by 1 Oct, from 1 Dec)"),
    "AI-05": ("none", "cameras without consultation (clause 14); paused 8 Mar, still billed", "R2", "STOP: 30 days' notice now; any safety technology through clause 14"),
    "AI-06": ("C: vendor '-40%'; POC ended 28 Feb", "still billed", "R3", "STOP: no renewal; claim the months after the SOW end"),
    "AI-07": ("none; paused since February", "", "R3", "STOP: notice of non-renewal by 31 Aug"),
    "AI-08": ("M: MAPE 11.2% vs 18.4%; overtime -15% vs Ashdod (~₪0.62M a year)", "one person, no documentation, owner left", "R4", "KEEP: name an owner and a second person; document"),
    "NEW-1": ("D: vendor feature, exceptions checked by AP", "", "R6", "REGISTER and KEEP"),
    "NEW-2": ("none", "a second tariff-code source beside Docs; on by default", "R6", "REGISTER; TURN OFF until evaluated with Docs"),
    "NEW-3": ("D: the team uses it daily", "customer e-mails to a public API on a personal card; no agreement", "R6", "BRING IN: approved model route with an agreement; stop the card"),
    "NEW-4": ("D: supplier invoices in Chinese", "invoices uploaded to a free site", "R6", "BRING IN: approved translation (Kotev, sanctioned)"),
    "N/A": ("C: ₪2.56M a year vs a naive baseline", "used as the source of the booked savings", "-", "RETIRE as evidence; Finance owns the measure"),
}

# Monthly saving and the date it starts, from the contract terms (contracts-ai.csv, MSA 7.4).
SAVING = {
    "AI-01C": (70 * 290 + 3 * 1100, date(2027, 10, 1)), "AI-01S": (92 * 290 + 6 * 1100, date(2027, 10, 1)),
    "AI-01E": (44 * 290 + 4 * 1100, date(2027, 10, 1)), "AI-04": (300 * 95, date(2027, 12, 1)),
    "AI-05": (18000, date(2027, 8, 1)),
}
OWNER = {"AI-01N": "Fadi Khatib", "AI-01C": "Gal Rosen", "AI-01S": "Rania Haj-Yahia", "AI-01E": "Pieter van Dijk",
         "AI-01P": "Moti Azulay", "AI-01D": "Moti Azulay", "AI-02": "Shlomo Peretz", "AI-03S": "Ronit Cohen-Elbaz",
         "AI-03D": "Dmitri Volkov", "AI-04": "Svetlana Morozov", "AI-05": "Moti Azulay", "AI-06": "Hanna Desta",
         "AI-07": "Ronit Cohen-Elbaz", "AI-08": "Hanna Desta (business), Lior Gabay (model)", "NEW-1": "Svetlana Morozov",
         "NEW-2": "Shlomo Peretz", "NEW-3": "Marina Levitan", "NEW-4": "Shlomo Peretz", "N/A": "Svetlana Morozov"}


def table() -> pd.DataFrame:
    inv = read("finance/ap-invoices-ai.csv")
    inv = inv[inv.period == "2027-05"].copy()
    inv["amount_ils"] = num(inv.amount_ils)
    lic = read("it/licence-usage-2027-05.csv")
    tk = read("incident/it-tickets-ai.csv")
    open_t = tk[tk.status == "open"]
    rows = []
    for sid, name, scope, isel, lsel in SYSTEMS:
        cost = 0.0
        if isel:
            cid, line, region = isel
            x = inv[(inv.contract_id == cid) & inv.line.str.contains(line) & ((inv.region == region) | (region == "all") | (inv.region == "all"))]
            if cid == "TZ-OF-101" and region != "all":
                x = x[(x.region == region) & ~x.line.str.contains("platform")]
            cost = x.amount_ils.sum()
        billed = active = ""
        if lsel:
            y = lic[lic.system == lsel[0]]
            if lsel[1]:
                y = y[y.region_or_department == lsel[1]]
            billed = int(num(y.seats_billed).fillna(0).sum()) or ""
            active = int(num(y.active_30d).sum())
        sysname = name.split(" (")[0].replace(" driver score", "")
        n_open = int(open_t.system.str.contains(sysname.split()[0], regex=False).sum())
        ev, risk, rule, action = FACTS[sid]
        save, start = SAVING.get(sid, (0, None))
        months_2027 = max(0, 13 - start.month) if start else 0
        rows.append({"id": sid, "system": name, "scope": scope, "cost_month_ils": round(cost), "seats_billed": billed,
                     "active_30d": active, "open_tickets": n_open, "evidence": ev, "risk": risk, "rule": rule,
                     "action": action, "owner": OWNER[sid], "saving_month_ils": save,
                     "saving_from": start.isoformat() if start else "", "saving_2027_ils": save * months_2027})
    return pd.DataFrame(rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", action="store_true", help="rewrite audit-sheet.csv for the spreadsheet track")
    args = ap.parse_args()
    print(RULES)
    t = table()
    pd.set_option("display.width", 220)
    pd.set_option("display.max_colwidth", 60)
    print("\n=== Stop/keep audit (first draft from the rules) ===")
    print(t[["id", "system", "scope", "cost_month_ils", "seats_billed", "active_30d", "rule", "action"]].to_string(index=False))
    print("\nActions:", t.action.str.extract(r"^([A-Z]+)")[0].value_counts().to_dict())
    run_now = t.cost_month_ils.sum()
    save = t.saving_month_ils.sum()
    print(f"\nMonthly cost of the audited lines (May invoices): ₪{run_now:,.0f}; monthly saving once the stops take effect: ₪{save:,.0f} "
          f"(₪{save * 12:,.0f} a year)")
    print(f"Saving inside 2027 given the notice terms: ₪{t.saving_2027_ils.sum():,.0f}")
    c = read("finance/ai-programme-cost-2027.csv")
    year = (num(c.actual_ils).fillna(0) + num(c.forecast_ils).fillna(0)).sum()
    print(f"2027 AI cost: forecast ₪{year:,.0f} -> ₪{year - t.saving_2027_ils.sum():,.0f} with the stops (budget ₪5,200,000)")
    run_2028 = {"Tzir Route (North + Centre planners)": 135000 * 12 - (SAVING['AI-01C'][0] + SAVING['AI-01S'][0] + SAVING['AI-01E'][0]) * 12,
                "Tzir Docs": 130000 * 12, "Tzir Assist": 95000 * 12, "Kotev Assist (150 seats)": 150 * 95 * 12,
                "Forecast cloud": 72000, "AI team (head of AI, data scientist, analyst)": 1190000}
    print("2028 run-rate:", {k: f"₪{v:,.0f}" for k, v in run_2028.items()}, f"total ₪{sum(run_2028.values()):,.0f}")
    incident_scope()
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    t.to_csv(out / "audit.csv", index=False, encoding="utf-8")
    print(f"\nWrote {out / 'audit.csv'}")
    if args.sheet:
        s = t[["id", "system", "scope", "cost_month_ils", "seats_billed", "active_30d", "open_tickets"]].copy()
        for col in ("evidence_label", "risk_flags", "rule", "action", "owner", "contract_step", "saving_month_ils", "saving_from"):
            s[col] = ""
        s.to_csv(HERE / "audit-sheet.csv", index=False, encoding="utf-8", lineterminator="\n")
        print(f"Wrote {HERE / 'audit-sheet.csv'}")


if __name__ == "__main__":
    main()
