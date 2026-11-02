"""Lesson 05.4 (Track B): score a pilot run and write the numbers for the eval report.

    python score.py runs/baseline-test-keywords-v1.csv          # any run file from run_pilot.py
    python score.py runs/llm-test-<model>.csv --today            # + what the helpdesk and agents do today
    python score.py runs/llm-negative-<model>.csv                # the negative tests, item by item
    python score.py runs/llm-test-<model>.csv --ratings scoring-sheet.csv   # + the people's draft ratings

What it measures:
  - triage: accuracy, precision and recall per category, accuracy per language, the confusion table
    (fieldkit.evals.run_eval and report);
  - language detection and reply language;
  - flags: missed and false flags; on real messages, how many would go to a senior agent;
  - drafts: the automatic checks in pilot_lib.draft_checks (reply language, the updated delivery date
    in "where is my order?" drafts, no stale promised date, no leaked numbers, no chatbot traces);
  - cost per item from the token counts (fieldkit.cost.token_cost) and per month at pilot volume;
  - --today: the same checks on what happens now (the helpdesk's own category and language fields,
    the agents' real replies), so the gate "no worse than today" has a measured "today";
  - --ratings: acceptance rate and review time from the scoring sheet the reviewers filled.
The report goes to reports/<run name>.md. No API key, no network.
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))

import pandas as pd

from fieldkit.cost import PRICES, pilot_value, token_cost
from fieldkit.evals import by_group, confusion, per_label, report, run_eval
from pilot_lib import ESCALATION_FLAGS, draft_checks, script_language

SETS = {"T": "test-set.csv", "D": "dev-set.csv", "N": "negative-tests.csv"}
HELPDESK_MAP = {"Delivery": "wismo", "Delivery status": "wismo", "Delivery damage": "damage",
                "Assembly": "assembly", "Returns & refunds": "returns", "Invoice & payment": "invoice",
                "B2B": "b2b_quote", "Product info": "product_question", "Complaint": "complaint",
                "Spam": "spam", "Other/כללי": "other", "": "other"}

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("run", help="a run file written by run_pilot.py")
ap.add_argument("--today", action="store_true", help="also score today's helpdesk fields and agent replies")
ap.add_argument("--ratings", help="scoring sheet with draft_verdict / review_seconds filled by reviewers")
ap.add_argument("--price-in", type=float, help="US$ per million input tokens (default: cost.PRICES for the run's model)")
ap.add_argument("--price-out", type=float, help="US$ per million output tokens")
ap.add_argument("--usd-ils", type=float, default=3.70, help="exchange rate (finance planning rate, Oct 2026)")
ap.add_argument("--monthly-volume", type=int, default=1_920, help="drafts a month at peak (ROI model 03.7)")
args = ap.parse_args()

run_path = Path(args.run)
if not run_path.exists():
    run_path = HERE / "runs" / args.run
run = pd.read_csv(run_path, dtype=str, keep_default_na=False)
items = pd.read_csv(HERE / SETS[run["item_id"].iloc[0][0]], dtype=str, keep_default_na=False)
items = items[items["item_id"].isin(run["item_id"])]
is_negative = run["item_id"].iloc[0].startswith("N")
by_id = run.set_index("item_id").to_dict("index")
meta = run.iloc[0]
title = f"{meta['provider']} · {meta['model']} · prompt v{meta['prompt_version']} · {meta['run_at']}"


def predict(row: dict) -> dict:
    p = by_id[row["item_id"]]
    return {"label": p["category"], "pred_language": p["language"], "pred_reply_language": p["reply_language"],
            "pred_flags": p["flags"], "draft": p["draft"]}


results = run_eval(items, predict, id_col="item_id", expected_col="expected_category",
                   group_cols=["expected_language"])
items_by_id = items.set_index("item_id").to_dict("index")

lines = [f"# Eval: {run_path.stem}", "", f"Run: {title}  ", f"Set: {SETS[meta['item_id'][0]]} ({len(items)} items)", ""]
lines.append(report(results, title="Triage (category)", group_cols=["expected_language"], max_failures=12))
lines += ["### Confusion (rows = expected, columns = predicted)", "", confusion(results).to_markdown(), ""]

# --- Language ---------------------------------------------------------------------------------------
lang_ok = (results["pred_language"].str.lower() == results["expected_language"]).mean()
reply_lang_ok = (results["pred_reply_language"].str.lower() ==
                 results["item_id"].map(lambda i: items_by_id[i]["expected_reply_language"])).mean()
lines += ["## Language", "", f"Message language right: {100 * lang_ok:.1f}%  ",
          f"Reply language right: {100 * reply_lang_ok:.1f}%", ""]

# --- Flags ------------------------------------------------------------------------------------------
flag_rows = []
for r in results.to_dict("records"):
    exp = {f for f in items_by_id[r["item_id"]].get("expected_flags", "").split(";") if f}
    got = {f for f in str(r["pred_flags"]).split(";") if f}
    flag_rows.append({"item_id": r["item_id"], "expected_flags": ";".join(sorted(exp)),
                      "predicted_flags": ";".join(sorted(got)), "missed": ";".join(sorted(exp - got)),
                      "escalated": bool(got & ESCALATION_FLAGS)})
flags = pd.DataFrame(flag_rows)
lines += ["## Flags", ""]
if is_negative:
    need = flags[flags["expected_flags"] != ""]
    caught = (need["missed"] == "").sum()
    lines += [f"Expected flags raised: {caught} of {len(need)} negative tests", ""]
else:
    esc = flags["escalated"].mean()
    lines += [f"Messages sent to a senior agent by a flag: {flags['escalated'].sum()} of {len(flags)} "
              f"({100 * esc:.1f}%) — every one is extra review load (05.5)", ""]

# --- Draft checks ----------------------------------------------------------------------------------
def checks_for(draft: str, it: dict, category_for_rules: str, as_of: str) -> dict:
    exp_date = pd.to_datetime(it.get("expected_date") or None)
    prom_date = pd.to_datetime(it.get("promised_date") or None)
    return draft_checks(draft, expected_reply_language=it["expected_reply_language"],
                        category=category_for_rules,
                        promised=prom_date.date() if pd.notna(prom_date) else None,
                        expected=exp_date.date() if pd.notna(exp_date) else None,
                        must=it.get("must", ""), must_not=it.get("must_not", ""))


check_rows = []
for r in results.to_dict("records"):
    it = items_by_id[r["item_id"]]
    c = checks_for(r["draft"], it, it["expected_category"], it["received_date"])
    c["item_id"], c["language"] = r["item_id"], it["expected_language"]
    check_rows.append(c)
checks = pd.DataFrame(check_rows)
check_cols = [c for c in checks.columns if c not in ("item_id", "language")]
has_drafts = run["draft"].str.strip().ne("").any()
lines += ["## Draft checks (automatic)", ""]
if not has_drafts:
    lines += ["This run has no drafts (baseline or mock): only triage and language are scored.", ""]
else:
    summary = []
    for col in check_cols:
        s = checks[col].dropna()
        summary.append({"check": col, "items": len(s), "pass_%": round(100 * s.astype(bool).mean(), 1) if len(s) else None})
    lines += [pd.DataFrame(summary).to_markdown(index=False), ""]
    if not is_negative:
        per_lang = checks.groupby("language")[[c for c in ("language_ok", "quotes_expected_date") if c in checks]].agg(
            lambda s: round(100 * s.dropna().astype(bool).mean(), 1) if s.notna().any() else None)
        lines += ["Per language (pass %):", "", per_lang.to_markdown(), ""]
    lines += ["These checks catch mechanical errors only. Whether a draft is right, complete and in the "
              "right tone is the reviewers' rating (scoring sheet, 05.4).", ""]

# --- Negative tests, item by item --------------------------------------------------------------------
if is_negative:
    neg_rows = []
    for r, f, c in zip(results.to_dict("records"), flag_rows, check_rows):
        it = items_by_id[r["item_id"]]
        draft_ok = all(bool(v) for k, v in c.items() if k not in ("item_id", "language") and v is not None) if has_drafts else None
        reply_ok = str(r["pred_reply_language"]).lower() == it["expected_reply_language"]
        ok = r["correct"] and f["missed"] == "" and reply_ok and (draft_ok is not False)
        neg_rows.append({"test": r["item_id"], "what it tests": it["what_it_tests"][:70],
                         "category": "ok" if r["correct"] else f"{r['predicted']} (exp. {r['expected']})",
                         "flags": "ok" if f["missed"] == "" else f"missed {f['missed']}",
                         "reply lang.": "ok" if reply_ok else f"{r['pred_reply_language']} (exp. {it['expected_reply_language']})",
                         "draft": "-" if draft_ok is None else ("ok" if draft_ok else "FAIL"),
                         "pass": "PASS" if ok else "FAIL"})
    neg = pd.DataFrame(neg_rows)
    lines += ["## Negative tests", "", f"Passed: {(neg['pass'] == 'PASS').sum()} of {len(neg)}", "",
              neg.to_markdown(index=False), ""]

# --- Cost ------------------------------------------------------------------------------------------
tin = pd.to_numeric(run["input_tokens"]).mean()
tout = pd.to_numeric(run["output_tokens"]).mean()
model = meta["model"]
if args.price_in is not None and args.price_out is not None:
    per_item = token_cost(tin, tout, price_in=args.price_in, price_out=args.price_out)
    price_note = f"US${args.price_in} / US${args.price_out} per million tokens (given)"
elif model in PRICES:
    per_item = token_cost(tin, tout, model=model)
    price_note = f"US${PRICES[model][0]} / US${PRICES[model][1]} per million tokens (fieldkit.cost.PRICES, checked 2026-11-02)"
else:
    per_item, price_note = None, "no price for this model: pass --price-in and --price-out"
lines += ["## Cost", "", f"Mean tokens per item: {tin:.0f} in, {tout:.0f} out  ", f"Prices: {price_note}  "]
if per_item is not None:
    month = per_item * args.monthly_volume * args.usd_ils
    lines += [f"Cost per item: US${per_item:.5f} = ₪{per_item * args.usd_ils:.4f} at ₪{args.usd_ils}/US$  ",
              f"Per month at {args.monthly_volume:,} drafts: ₪{month:,.0f}", ""]
else:
    lines += [""]

# --- Today -----------------------------------------------------------------------------------------
if args.today and not is_negative:
    hd_cat = (items["helpdesk_category"].map(HELPDESK_MAP).fillna("other") == items["expected_category"]).mean()
    hd_lang = (items["helpdesk_language"] == items["expected_language"]).mean()
    kw = items.assign(agent_language=items["agent_reply"].map(script_language))
    replied = kw[kw["agent_reply"].str.strip() != ""]
    wrong_lang = (replied["agent_language"] != replied["expected_language"]).sum()
    stale = 0
    wismo_replied = replied[replied["expected_category"] == "wismo"]
    import re
    for r in wismo_replied.to_dict("records"):
        sent = pd.Timestamp(r["agent_reply_date"]).date()
        for d, m in re.findall(r"(?<!\d)(\d{1,2})\s?[./]\s?(\d{1,2})(?![\d/.]\d)", r["agent_reply"]):
            try:
                if pd.Timestamp(year=sent.year, month=int(m), day=int(d)).date() < sent:
                    stale += 1
                    break
            except ValueError:
                continue
    traces = sum(1 for r in replied["agent_reply"] if draft_checks(r, expected_reply_language="", category="other")["no_chatbot_trace"] is False)
    lines += ["## Today (same messages, no AI)", "",
              f"Helpdesk category field right (mapped to the pilot's categories): {100 * hd_cat:.1f}%  ",
              f"Helpdesk auto-detected language right: {100 * hd_lang:.1f}%  ",
              f"Messages with an agent reply: {len(replied)} of {len(items)}  ",
              f"Agent replies in a language other than the customer's: {wrong_lang} ({100 * wrong_lang / len(replied):.1f}%)  ",
              f"\"Where is my order?\" replies that give a date already in the past on the day they were sent: "
              f"{stale} of {len(wismo_replied)} ({100 * stale / max(len(wismo_replied), 1):.1f}%)  ",
              f"Agent replies with chatbot traces: {traces}", ""]

# --- Ratings from the reviewers --------------------------------------------------------------------
if args.ratings:
    sheet = pd.read_csv(args.ratings, dtype=str, keep_default_na=False)
    sheet = sheet[sheet["item_id"].isin(items["item_id"]) & (sheet["draft_verdict"].str.strip() != "")]
    if len(sheet):
        v = sheet["draft_verdict"].str.strip().str.lower()
        accepted = v.isin(["accept", "light edit"])
        secs = pd.to_numeric(sheet["review_seconds"], errors="coerce")
        per_lang = sheet.assign(accepted=accepted).groupby("expected_language")["accepted"].agg(["size", "mean"])
        per_lang["mean"] = (100 * per_lang["mean"]).round(1)
        lines += ["## Reviewers' ratings", "", f"Drafts rated: {len(sheet)}  ",
                  f"Accepted with no or light edits: {100 * accepted.mean():.1f}%  ",
                  f"Median review time: {secs.median() / 60:.1f} minutes  ",
                  f"Safety issues found: {(sheet['safety_issue'].str.strip().str.lower().isin(['y', 'yes'])).sum()}", "",
                  per_lang.rename(columns={"size": "n", "mean": "accepted_%"}).to_markdown(), ""]
        pv = pilot_value(volume=3_200, automation_rate=0.6, accuracy=float(accepted.mean()), minutes_saved=8,
                         review_minutes=float(secs.median() / 60) if secs.notna().any() else 2,
                         rework_minutes=5, hourly_cost=130, cost_per_item_usd=per_item or 0,
                         usd_to_ils=args.usd_ils, fixed_monthly=4_000)
        lines += ["Peak month with these measured rates (pilot-economics inputs otherwise unchanged):", "",
                  pd.Series(pv).to_frame("value").to_markdown(), ""]
    else:
        lines += ["## Reviewers' ratings", "", "No rated drafts for these items in the sheet yet.", ""]

text = "\n".join(lines)
out = HERE / "reports" / f"{run_path.stem}.md"
out.parent.mkdir(exist_ok=True)
out.write_text(text, encoding="utf-8", newline="\n")
print(text)
print(f"\nWrote {out.relative_to(HERE)}")
