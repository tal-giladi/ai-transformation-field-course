"""Gate 1 evidence pack for Harbor & Pine's reply-drafts pilot (lesson 07.2, Track B).

Joins the admin usage export (who used the drafts, week by week) with the HR roster and Samir's queue
rota (module 6), and reads the pilot log's gate readings (share of tickets, acceptance, review time,
spot audit). Prints the gate table (a)-(d), the adoption gate per channel and the hours at peak.

Privacy: the usage export is personal data about employees, and Harbor & Pine's AUP promises usage
reporting by team, not by person (lessons 04.1 and 06.4). By default the script prints use per queue
and counts only. The per-person table prints with --who, for the analyst's own check; never paste it
into a steering paper or a decision record.

Run from labs/module-07 (no LLM, no network):
    python gate1_evidence.py
    python gate1_evidence.py --whatsapp-use 0.5 --whatsapp-saving 1.5   # a half-fixed WhatsApp
    python gate1_evidence.py --who                                      # analyst only
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))

import pandas as pd  # noqa: E402

from fieldkit.data import data_room, load  # noqa: E402

PILOT_START = pd.Timestamp("2027-02-01", tz="Asia/Jerusalem")


def pct(x: float) -> str:
    return f"{100 * x:.1f}%"


def usage_by_week(room: Path, who: bool) -> None:
    usage = load(room / "usage" / "ai-usage-export.csv")
    roster = load(room / "usage" / "hr-roster.csv")
    usage["week"] = ((usage["date"] - PILOT_START).dt.days // 7) + 1
    qualified = usage[usage["feature"] == "draft_inserted"]

    rota_file = HERE.parent / "module-06" / "queue-rota-2027.csv"
    if rota_file.exists():
        rota = pd.read_csv(rota_file)
        rota["queue"] = rota["main_queue"].str.split(" (", regex=False).str[0]
        rota["user_email"] = rota["full_name"].map(dict(zip(roster["full_name"], roster["email"])))
        joined = qualified.merge(rota[["pilot_week", "user_email", "queue"]],
                                 left_on=["week", "user_email"], right_on=["pilot_week", "user_email"], how="left")
        print("## Qualified use (draft_inserted events) per queue and week (rota from the module 6 download)")
        print(joined.pivot_table(index="queue", columns="week", values="events", aggfunc="sum", fill_value=0).to_string())
    else:
        print("(Module 6 rota not found next to this folder: queue view skipped.)")

    users = qualified.groupby("week")["user_email"].nunique()
    print("\nPeople with at least one inserted draft, per week:", {int(k): int(v) for k, v in users.items()})

    per_user = qualified.pivot_table(index="user_email", columns="week", values="events", aggfunc="sum", fill_value=0)
    weeks = list(per_user.columns)
    roster["since"] = roster["status_since_date"].dt.strftime("%Y-%m-%d").fillna("")
    per_user = per_user.join(roster.set_index("email")[["full_name", "employment_status", "since"]])
    stopped = per_user[(per_user[weeks[:3]].sum(axis=1) >= 30) & (per_user[weeks[-4:]].sum(axis=1) == 0)]
    active = stopped[stopped["employment_status"] == "active"]
    print(f"Used drafts in weeks 1-3 and none in the last four weeks: {len(stopped)} people; "
          f"{len(stopped) - len(active)} on leave or left; {len(active)} still working tickets (quiet non-adoption).")
    licences = roster[roster["ai_assist_licence"] == "Y"]["email"]
    idle = [e for e in licences if usage.loc[usage["user_email"] == e, "events"].sum() <= 2]
    print(f"Licences with almost no use: {len(idle)} (reclaim them).")

    if who:
        print("\n## ANALYST ONLY: per person (do not report; the AUP promises team-level reporting)")
        print(per_user.to_string())


def gate_table(args: argparse.Namespace) -> None:
    r = pd.read_csv(HERE / "gate-1-readings.csv")
    w = pd.read_csv(HERE / "gate-1-weekly.csv")
    o = pd.read_csv(HERE / "gate-1-other-readings.csv").set_index("reading")["value"]

    print("\n## (a) Acceptance: drafts used as is or lightly edited / drafts shown")
    for name, frame in [("email + web form", r[r.channel == "email_web"]),
                        ("WhatsApp", r[r.channel == "whatsapp"]), ("all channels", r)]:
        by_lang = frame.groupby("language")[["drafts_accepted", "drafts_shown"]].sum()
        rates = by_lang.drafts_accepted / by_lang.drafts_shown
        total = frame.drafts_accepted.sum() / frame.drafts_shown.sum()
        langs = ", ".join(f"{k} {pct(rates[k])} (n={by_lang.loc[k, 'drafts_shown']})" for k in by_lang.index)
        verdict = "PASS" if total >= 0.80 and rates.min() >= 0.70 else "FAIL"
        print(f"  {name}: {pct(total)} overall; {langs} -> {verdict} (>= 80% overall, >= 70% each language)")

    print("\n## (b) Median review time")
    print(f"  all drafted tickets: {float(o['Median review time all drafted tickets (15 Feb - 28 Mar)']):.0f} s (gate: <= 150 s)")
    print("  per segment (s):", dict(zip(r.channel + "/" + r.language, r.median_review_seconds)))

    print("\n## (c) Wrong replies reaching customers (spot audit vs post-fix 'today')")
    wrong, read = int(w.spot_audit_wrong.sum()), int(w.spot_audit_read.sum())
    print(f"  pilot: {wrong} of {read} = {pct(wrong / read)}; today: 9 of 300 = 3.0%")
    print("  NOTE: the sample missed the incident cluster (7 refund promises, 1 address) of 10-15 March.")

    print("\n## Adoption gate: tickets with a draft used / eligible tickets, per week (>= 60% two weeks running)")
    adoption = (w.assign(share=w.tickets_draft_used / w.eligible_tickets)
                .pivot(index="pilot_week", columns="channel", values="share"))
    total = w.groupby("pilot_week")[["tickets_draft_used", "eligible_tickets"]].sum()
    adoption["all channels"] = total.tickets_draft_used / total.eligible_tickets
    print(adoption.map(pct).to_string())

    print("\n## (d) Hours a month at peak (one temp = 160 h, two = 320 h)")
    ew_saving = (float(o["Minutes per contact email_web holdout (15 Feb - 28 Mar)"])
                 - float(o["Minutes per contact email_web with draft (15 Feb - 28 Mar)"]))
    wa_saving_now = (float(o["Minutes per contact WhatsApp no drafts (1 - 14 Feb)"])
                     - float(o["Minutes per contact WhatsApp with draft used (15 Feb - 28 Mar)"]))
    ew_vol = float(o["Forecast written contacts a month at peak Nov 2027 - Jan 2028 (email_web)"])
    wa_vol = float(o["Forecast written contacts a month at peak Nov 2027 - Jan 2028 (WhatsApp)"])
    ew = r[r.channel == "email_web"]
    wa = r[r.channel == "whatsapp"]
    ew_use = ew.tickets_draft_used.sum() / ew.eligible_tickets.sum()
    wa_use_now = wa.tickets_draft_used.sum() / wa.eligible_tickets.sum()
    wismo_before = float(o["WISMO share of all written contact Jul - Oct 2026"])
    wismo_after = w.wismo_share_all_written.mean()
    date_fix = float(o["WISMO agent-hours a month at peak before the date fix"]) * (1 - wismo_after / wismo_before)
    for label, wa_use, wa_saving in [
        ("today's use", wa_use_now, wa_saving_now),
        (f"WhatsApp fixed (used on {args.whatsapp_use:.0%}, {args.whatsapp_saving} min saved)", args.whatsapp_use, args.whatsapp_saving),
    ]:
        pilot = ew_vol * ew_use * ew_saving / 60 + wa_vol * wa_use * wa_saving / 60
        total_h = pilot + date_fix
        temps = "two temps" if total_h >= 320 else "one temp" if total_h >= 160 else "not even one temp"
        print(f"  {label}: pilot {pilot:.0f} h + date fix {date_fix:.0f} h = {total_h:.0f} h -> {temps}")
    print(f"  (email/web: {ew_saving:.1f} min saved per drafted contact, attributed by the holdout; "
          f"WhatsApp today: {wa_saving_now:.1f} min, directional; WISMO share {pct(wismo_before)} -> {pct(wismo_after)})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--whatsapp-saving", type=float, default=2.0, help="minutes saved per WhatsApp contact if fixed")
    parser.add_argument("--whatsapp-use", type=float, default=0.75, help="share of WhatsApp tickets with a draft used if fixed")
    parser.add_argument("--who", action="store_true", help="analyst only: print the per-person table")
    args = parser.parse_args()
    usage_by_week(data_room("harbor-and-pine"), args.who)
    gate_table(args)


if __name__ == "__main__":
    main()
