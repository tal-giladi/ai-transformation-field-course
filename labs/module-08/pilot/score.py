"""Lesson 08.5 (Track B): score an agent-assist run and write the numbers for the eval report.

    python score.py runs/rules-test-rules.csv --today     # the no-LLM baseline, plus what agents answer today
    python score.py runs/hybrid-test-<model>.csv --today

What it measures, against labels-2000.csv (the labelling team's adjudicated labels):
  - intent: accuracy, per intent and per language (fieldkit.evals);
  - decision: accuracy on every ticket, and on the returns tickets (where a decision is due), per language;
  - fee: right to the agora where a fee is due;
  - escalation: recall and precision;
  - drafts: language, banned promises (store credit only, 10%, "30 days full refund"), fee above the cap;
  - cost per ticket from the token counts (fieldkit.cost) and per month at --monthly-volume;
  - --today: the same decision and draft checks on the agents' real replies (coded by the labelling team).
The report goes to reports/<run name>.md. No API key, no network.
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "common"))

import pandas as pd

from fieldkit.cost import PRICES, token_cost
from fieldkit.evals import by_group, per_label, run_eval
from pilot_lib import draft_checks
from sets import labels, load_set, split

TODAY_TO_DECISION = {"refund_legal_fee": "refund_minus_fee", "pickup_no_fee": "refund_no_fee_pickup",
                     "refuse_window": "outside_window", "goodwill_credit": "outside_window",
                     "exchange_ok": "exchange_free", "status_generic": "status_update", "escalated": "escalate_counsel",
                     "n/a": "n/a", "store_credit": "store_credit (not in policy)",
                     "refund_minus_10pct": "refund_minus_10pct (not in policy)",
                     "refund_no_fee": "refund_no_fee (not in policy)", "customer_ships": "customer_ships (not in policy)"}
WORSE_THAN_LAW = {"store_credit", "refund_minus_10pct", "customer_ships"}
RETURNS = {"refund_minus_fee", "refund_no_fee_pickup", "refund_4m_verify", "outside_window", "excluded_custom", "exchange_free"}

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("run")
ap.add_argument("--today", action="store_true")
ap.add_argument("--price-in", type=float)
ap.add_argument("--price-out", type=float)
ap.add_argument("--usd-ils", type=float, default=3.136, help="Bank of Israel representative rate, 2 Nov 2026")
ap.add_argument("--monthly-volume", type=int, default=20_000, help="written tickets a month (company)")
args = ap.parse_args()

run_path = Path(args.run) if Path(args.run).exists() else HERE / "runs" / args.run
run = pd.read_csv(run_path, dtype=str, keep_default_na=False)
lab = labels()
ids = set(run["ticket_id"])
negative = all(i.startswith("N-") for i in ids)
name = "negative" if negative else next((n for n in ("test", "dev", "track-a", "all") if set(split()[n]) == ids), "custom")
tickets = {r["ticket_id"]: r for r in load_set("negative" if negative else "all") if r["ticket_id"] in ids}
items = pd.DataFrame([{**lab[i], **{"t_" + k: v for k, v in tickets[i].items()}} for i in sorted(ids)])
by_id = run.set_index("ticket_id").to_dict("index")
meta = run.iloc[0]
pct = lambda x: f"{100 * x:.1f}%"

lines = [f"# Eval: {run_path.stem}", "",
         f"Run: {meta['provider']} · {meta['model']} · prompt {meta['prompt_version']} · {meta['run_at']}  ",
         f"Set: {name} ({len(items)} tickets)", ""]

# intent
res_i = run_eval(items, lambda r: by_id[r["ticket_id"]]["intent"], id_col="ticket_id", expected_col="intent",
                 group_cols=["language"])
lines += ["## Intent", "", f"Accuracy: **{pct(res_i['correct'].mean())}**", "", per_label(res_i).to_markdown(), "",
          "By language", "", by_group(res_i, "language").to_markdown(), ""]

# decision
res_d = run_eval(items, lambda r: by_id[r["ticket_id"]]["decision"], id_col="ticket_id", expected_col="expected_decision",
                 group_cols=["language"])
ret = res_d[res_d["expected"].isin(RETURNS)]
lines += ["## Decision", "", f"All tickets: **{pct(res_d['correct'].mean())}**  ",
          f"Returns tickets (a decision under the policy is due, n = {len(ret)}): **{pct(ret['correct'].mean())}**", "",
          "Per decision", "", per_label(res_d).to_markdown(), "", "Returns tickets by language", "",
          by_group(ret, "language").to_markdown(), "",
          "Confusion on returns tickets (rows expected, columns predicted)", "",
          pd.crosstab(ret["expected"], ret["predicted"]).to_markdown(), ""]

# fee
fee_due = items[items["expected_decision"].isin(["refund_minus_fee", "refund_4m_verify"])]
fee_ok = sum(abs(float(by_id[t]["fee_ils"] or 0) - float(e)) < 0.01 and by_id[t]["decision"] == d
             for t, e, d in zip(fee_due["ticket_id"], fee_due["expected_fee_ils"], fee_due["expected_decision"]))
lines += ["## Fee", "", f"Right decision and right fee: {fee_ok} of {len(fee_due)} ({pct(fee_ok / len(fee_due) if len(fee_due) else 0)})", ""]

if negative:  # every negative test is pass or fail: decision, fee and escalation all right
    rows = []
    for t in sorted(ids):
        p, x = by_id[t], lab[t]
        ok_dec = p["decision"] == x["expected_decision"]
        ok_fee = abs(float(p["fee_ils"] or 0) - float(x["expected_fee_ils"])) < 0.01
        ok_esc = p["escalate"] == x["escalate"]
        rows.append({"test": t, "expected": x["expected_decision"], "got": p["decision"], "escalate": f"{p['escalate']} (want {x['escalate']})",
                     "pass": "PASS" if ok_dec and ok_fee and ok_esc else "FAIL"})
    nt = pd.DataFrame(rows)
    lines += ["## Negative tests", "", f"Passed: **{(nt['pass'] == 'PASS').sum()} of {len(nt)}**", "", nt.to_markdown(index=False), ""]

# escalation
esc_true = items["escalate"] == "y"
esc_pred = items["ticket_id"].map(lambda t: by_id[t]["escalate"] == "y")
tp = int((esc_true & esc_pred).sum())
lines += ["## Escalation", "",
          f"Should escalate: {int(esc_true.sum())}; caught {tp} (recall {pct(tp / esc_true.sum() if esc_true.sum() else 0)}); "
          f"flagged {int(esc_pred.sum())} (precision {pct(tp / esc_pred.sum() if esc_pred.sum() else 0)})", ""]
missed = items[esc_true & ~esc_pred]
if len(missed):
    lines += ["Missed escalations", "", missed[["ticket_id", "language", "escalate_reason", "cues"]].to_markdown(index=False), ""]


def check_rows(texts):
    out = []
    for t, text in texts:
        x = lab[t]
        out.append(draft_checks(text, x["language"], x["expected_decision"], tickets[t]))
    return pd.DataFrame(out)


drafts = check_rows([(t, by_id[t]["draft"]) for t in items["ticket_id"]])
lines += ["## Drafts (automatic checks)", "",
          f"Draft in the customer's language (Amharic: Hebrew): {pct(drafts['draft_language_ok'].mean())}  ",
          f"Banned phrase (store credit only, 10%, 30 days full refund, chatbot traces): {int((drafts['banned_phrase'] != '').sum())}  ",
          f"Fee above the legal cap stated: {int(drafts['fee_over_cap'].sum())}", ""]

# cost
tin = pd.to_numeric(run["tokens_in"]).mean()
tout = pd.to_numeric(run["tokens_out"]).mean()
model = meta["model"]
if args.price_in is not None and args.price_out is not None:
    usd = token_cost(tin, tout, price_in=args.price_in, price_out=args.price_out)
elif model in PRICES:
    usd = token_cost(tin, tout, model=model)
else:
    usd = None
lines += ["## Cost", ""]
if model == "rules":
    lines += ["No model calls (rules and templates).", ""]
elif usd is None:
    lines += [f"Mean tokens in {tin:.0f}, out {tout:.0f}. Give --price-in and --price-out for {model}.", ""]
else:
    lines += [f"Mean tokens in {tin:.0f}, out {tout:.0f}: US${usd:.5f} = ₪{usd * args.usd_ils:.4f} per ticket "
              f"(₪{args.usd_ils}/US$); ₪{usd * args.usd_ils * args.monthly_volume:,.0f} a month at {args.monthly_volume:,} tickets.", ""]

# today
if args.today:
    td = items.assign(today=items["today_decision"].map(TODAY_TO_DECISION))
    tr = td[td["expected_decision"].isin(RETURNS)]
    exact = (tr["today"] == tr["expected_decision"]).mean()
    worse = tr["today_decision"].isin(WORSE_THAN_LAW) | (
        tr["expected_decision"].isin(["refund_minus_fee", "refund_4m_verify"]) & tr["today_decision"].isin(["refuse_window", "goodwill_credit"]))
    lines += ["## Today (the agents' real replies, coded)", "",
              f"Returns tickets where today's reply matches the policy decision: **{pct(exact)}** (n = {len(tr)})  ",
              f"Returns tickets where today's reply gives the customer less than the law: **{pct(worse.mean())}**", "",
              "Today's replies on returns tickets", "", tr["today_decision"].value_counts().to_frame("tickets").to_markdown(), "",
              "By language (matches policy)", "",
              tr.assign(ok=tr["today"] == tr["expected_decision"]).groupby("language")["ok"].agg(["size", "mean"])
              .rename(columns={"size": "n", "mean": "share"}).round(3).to_markdown(), ""]
    today_checks = check_rows([(t, tickets[t]["agent_reply"]) for t in items["ticket_id"]])
    lines += [f"Agent replies with a banned phrase: {int((today_checks['banned_phrase'] != '').sum())} of {len(today_checks)}", ""]

(HERE / "reports").mkdir(exist_ok=True)
out = HERE / "reports" / f"{run_path.stem}{'-today' if args.today else ''}.md"
out.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print("\n".join(lines[:12]))
print(f"... full report: {out.relative_to(HERE)}")
