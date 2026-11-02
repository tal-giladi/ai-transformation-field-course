"""Lesson 06.4 (Track B): the honest adoption dashboard for Harbor & Pine's drafts pilot.

Joins the AI assist panel's admin export (usage/ai-usage-export.csv) with the HR roster
(usage/hr-roster.csv) and Samir's queue rota (queue-rota-2027.csv, in this folder), and prints:

  1. what the vendor-style dashboard says (licences, weekly active users, events);
  2. the opportunity-aware population per pilot week (who could have used the drafts that week);
  3. the qualified-use rate per week (qualified event = draft_inserted, at least 5 in the week);
  4. how sensitive the rate is to the threshold (1, 5 and 10 inserted drafts);
  5. licence holders outside the drafting population and what they use;
  6. quiet non-adoption: who stopped, when, still at work on what (team-level by default).

Pilot week n = the 7 days starting Monday 1 February 2027 + 7*(n-1) (week 1 = 1-7 Feb).

Privacy: by default every table is by team and week. The per-person "who stopped" view prints
only with --who, is meant for the pilot lead alone, and must be handled as the comms pack and the
AUP say (06.5, 04.1): used to offer help, never for performance reviews.

Run from this folder:  python adoption_dashboard.py [--who] [--threshold 5]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
sys.stdout.reconfigure(errors="replace")

import pandas as pd

from fieldkit.data import data_room, load

HERE = Path(__file__).resolve().parent
PILOT_START = pd.Timestamp("2027-02-01")
WEEKS = range(1, 9)
QUALIFIED_FEATURE = "draft_inserted"       # the agent put the draft into the reply box
AUTO_FEATURES = {"panel_opened"}           # fires by itself when a ticket opens: not use
DRAFTING_ROLES = {"Support Agent", "Senior Support Agent (team lead)"}  # answer written contact


def pilot_week(dates: pd.Series) -> pd.Series:
    days = (dates.dt.tz_localize(None).dt.normalize() - PILOT_START).dt.days
    return days // 7 + 1


def week_monday(w: int) -> pd.Timestamp:
    return PILOT_START + pd.Timedelta(days=7 * (w - 1))


def heading(text: str) -> None:
    print(f"\n=== {text} ===")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--who", action="store_true", help="print the per-person quiet non-adoption table")
    ap.add_argument("--threshold", type=int, default=5, help="inserted drafts a week for a qualified user-week")
    args = ap.parse_args()

    room = data_room("harbor-and-pine")
    usage = load(room / "usage" / "ai-usage-export.csv")
    roster = load(room / "usage" / "hr-roster.csv")
    rota = pd.read_csv(HERE / "queue-rota-2027.csv", dtype=str, encoding="utf-8")
    rota["pilot_week"] = rota["pilot_week"].astype(int)

    usage["week"] = pilot_week(usage["date"])
    usage = usage.merge(roster[["email", "employee_id", "full_name", "role", "team"]],
                        left_on="user_email", right_on="email", how="left")
    unmatched = usage["employee_id"].isna().sum()

    # ---- 1. The vendor-style view -----------------------------------------------------------
    heading("1. What the vendor-style dashboard shows")
    licences = int((roster["ai_assist_licence"] == "Y").sum())
    rows = []
    for w in WEEKS:
        u = usage[usage["week"] == w]
        rows.append({
            "week": w,
            "from": week_monday(w).strftime("%d %b"),
            "licences": licences,
            "active_any_event": u["user_email"].nunique(),
            "active_user_initiated": u[~u["feature"].isin(AUTO_FEATURES)]["user_email"].nunique(),
            "events": int(u["events"].sum()),
            "drafts_generated": int(u.loc[u["feature"] == "draft_generated", "events"].sum()),
            "drafts_inserted": int(u.loc[u["feature"] == QUALIFIED_FEATURE, "events"].sum()),
        })
    vendor = pd.DataFrame(rows)
    vendor["active_rate"] = (vendor["active_any_event"] / vendor["licences"]).map("{:.0%}".format)
    vendor["inserted_per_generated"] = (vendor["drafts_inserted"] / vendor["drafts_generated"]).map("{:.0%}".format)
    print(vendor.to_string(index=False))
    print(f"Rows in the export with no roster match: {unmatched}")
    print("Note: 'active_any_event' counts panel_opened, which fires when a ticket opens. It is not use.")

    # ---- 2. Opportunity-aware population ----------------------------------------------------
    heading("2. Who could have used the drafts each week (opportunity-aware population)")
    roster["status_since_date"] = roster["status_since_date"].dt.tz_localize(None).dt.normalize()

    def in_population(person: pd.Series, w: int) -> tuple[bool, str]:
        if person["role"] not in DRAFTING_ROLES:
            return False, f"role: {person['role']}"
        monday = week_monday(w)
        since = person["status_since_date"]
        if person["employment_status"] != "active" and pd.notna(since) and since <= monday:
            return False, f"{person['employment_status']} since {since:%d %b}"
        return True, ""

    pop = {w: [] for w in WEEKS}
    excluded = {}
    for _, p in roster.iterrows():
        for w in WEEKS:
            ok, why = in_population(p, w)
            if ok:
                pop[w].append(p["email"])
            else:
                excluded.setdefault((p["full_name"], why), []).append(w)
    print("Excluded (name — reason — weeks):")
    for (name, why), ws in excluded.items():
        span = f"{ws[0]}-{ws[-1]}" if len(ws) > 1 else str(ws[0])
        print(f"  {name} — {why} — weeks {span}")

    # ---- 3. Qualified use -------------------------------------------------------------------
    inserted = (usage[usage["feature"] == QUALIFIED_FEATURE]
                .pivot_table(index="user_email", columns="week", values="events", aggfunc="sum", fill_value=0)
                .reindex(columns=list(WEEKS), fill_value=0))
    opened = (usage[usage["feature"] == "panel_opened"]
              .pivot_table(index="user_email", columns="week", values="events", aggfunc="sum", fill_value=0)
              .reindex(columns=list(WEEKS), fill_value=0))

    def qualified_count(w: int, threshold: int) -> int:
        return sum(1 for e in pop[w] if inserted.get(w, pd.Series(dtype=int)).get(e, 0) >= threshold)

    heading(f"3. Qualified-use rate (qualified = at least {args.threshold} drafts inserted in the week)")
    honest = []
    for w in WEEKS:
        n = len(pop[w])
        q = qualified_count(w, args.threshold)
        honest.append({"week": w, "from": week_monday(w).strftime("%d %b"), "population": n,
                       "qualified_users": q, "qualified_rate": f"{q / n:.0%}",
                       "vendor_active_rate": vendor.loc[w - 1, "active_rate"]})
    print(pd.DataFrame(honest).to_string(index=False))

    sustained = sum(1 for e in pop[8] if sum(inserted.loc[e, w] >= args.threshold
                                               for w in range(5, 9) if e in inserted.index) >= 3)
    print(f"Sustained users in weeks 5-8 (qualified in at least 3 of the 4 weeks, still in the population): "
          f"{sustained} of {len(pop[8])}")

    # ---- 4. Sensitivity ---------------------------------------------------------------------
    heading("4. How much the threshold matters (qualified users / population)")
    sens = {"week": list(WEEKS)}
    for t in (1, 5, 10):
        sens[f">= {t} inserted"] = [f"{qualified_count(w, t)}/{len(pop[w])}" for w in WEEKS]
    print(pd.DataFrame(sens).to_string(index=False))

    # ---- 5. Licences with no task -----------------------------------------------------------
    heading("5. Licence holders outside the drafting population: what their licence is used for")
    for _, p in roster[~roster["role"].isin(DRAFTING_ROLES)].iterrows():
        u = usage[usage["user_email"] == p["email"]]
        feats = ", ".join(sorted(u["feature"].unique())) or "none"
        print(f"  {p['full_name']} ({p['role']}, {p['team']}): {int(u['events'].sum())} events; features: {feats}")

    # ---- 6. Quiet non-adoption --------------------------------------------------------------
    heading("6. Quiet non-adoption: stopped inserting drafts but still working tickets")
    early, late = [1, 2, 3], [6, 7, 8]
    stoppers = []
    for e in pop[8]:
        ins = inserted.loc[e] if e in inserted.index else pd.Series(0, index=list(WEEKS))
        opn = opened.loc[e] if e in opened.index else pd.Series(0, index=list(WEEKS))
        was_user = sum(ins[w] >= args.threshold for w in early) >= 2
        stopped = all(ins[w] < args.threshold for w in late)
        still_working = all(opn[w] >= 50 for w in late)
        if was_user and stopped and still_working:
            first_low = next(w for w in WEEKS if w > 1 and all(ins[x] < args.threshold for x in range(w, 9)))
            stoppers.append((e, first_low, ins, opn))
    print(f"{len(stoppers)} of {len(pop[8])} people in the week-8 population used the drafts in weeks 1-3 "
          f"and inserted fewer than {args.threshold} a week in each of weeks 6-8, while the panel still "
          f"opened on 50+ tickets a week for each of them.")
    if stoppers:
        when = sorted({w for _, w, _, _ in stoppers})
        print(f"They stopped from week(s): {', '.join(map(str, when))} "
              f"(week {when[0]} = {week_monday(when[0]):%d %b} - {week_monday(when[0]) + pd.Timedelta(days=6):%d %b}).")
        # Team-level join with the rota: where were they working when they stopped?
        name_of = roster.set_index("email")["full_name"]
        queues = []
        for e, w, _, _ in stoppers:
            r = rota[(rota["full_name"] == name_of[e]) & (rota["pilot_week"] == w)].iloc[0]
            queues.append(r["main_queue"].split(" (")[0])
        print("Main queue in the week they stopped: " + "; ".join(
            f"{q} x{queues.count(q)}" for q in sorted(set(queues))))
        others = [name_of[e] for e in pop[8] if e not in {s[0] for s in stoppers}]
        oq = rota[(rota["pilot_week"] == 8) & (rota["full_name"].isin(others))]["main_queue"].str.split(" \\(").str[0]
        print("Main queue in week 8 of everyone else in the population: " + "; ".join(
            f"{q} x{n}" for q, n in oq.value_counts().items()))
        print("Back to what? The export cannot say: no draft is generated, so nothing is logged. "
              "Ask (06.4 Step 5, 06.6) and check the WhatsApp quick replies in the helpdesk.")
    if args.who and stoppers:
        print("\nPer-person view (pilot lead only; do not forward, do not use in performance reviews):")
        name_of = roster.set_index("email")["full_name"]
        for e, w, ins, opn in stoppers:
            print(f"  {name_of[e]}: inserted per week {'/'.join(str(int(ins[x])) for x in WEEKS)}; "
                  f"panel opened per week {'/'.join(str(int(opn[x])) for x in WEEKS)}; low from week {w}")
    elif stoppers:
        print("(Run with --who for the per-person view; read the privacy note at the top of this script first.)")


if __name__ == "__main__":
    main()
