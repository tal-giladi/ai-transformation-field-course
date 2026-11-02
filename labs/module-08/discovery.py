"""Lessons 08.2 and 08.3 (Track B): the discovery numbers from Northwind's data room, the same way every time.

    python discovery.py

Prints, from the 1% customer extract (company figures = x 100):
  - agent contacts by month; AHT as the reports define it and like for like;
  - the repeat-contact rate (same customer, same order after normalising, or either blank, within 7 days);
  - three readings of the returns share (category, tag) to set against the 2,000-ticket labels;
  - chatbot "resolved" sessions followed by an agent contact within 7 days;
  - refund time, inspection time and the weekday refunds are paid;
  - handling fees above the 5% / ₪100 cap.
No network, no API key.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))

import numpy as np
import pandas as pd

from fieldkit.data import data_room, load

room = data_room("module-08")
c = load(room / "support" / "contacts.csv")
s = load(room / "support" / "bot-sessions.csv")
r = load(room / "orders" / "returns.csv")
BOT_LIVE = pd.Timestamp("2026-06-15", tz="Asia/Jerusalem")


def order_no(x) -> str:
    digits = re.sub(r"\D", "", str(x)) if pd.notna(x) else ""
    return f"NW-{digits}" if digits else ""


print("== Agent contacts by month (x 100 for the company)")
c["month"] = c["created_at"].dt.month
print((c.groupby("month").size() * 100).to_string())

print("\n== AHT, minutes")
c["after"] = c["created_at"] >= BOT_LIVE
for label, part in (("before 15 Jun", c[~c["after"]]), ("from 15 Jun", c[c["after"]])):
    reported = part["handle_time_sec"].mean() / 60
    like = (part["handle_time_sec"] + part["after_contact_work_sec"]).mean() / 60
    print(f"{label}: handling only {reported:.2f}, handling + after-contact work {like:.2f}")

print("\n== Repeat contacts (same customer, same order or blank, within 7 days)")
c = c.sort_values("created_at")
c["order"] = c["order_id"].map(order_no)
c["prev_t"] = c.groupby("customer_id")["created_at"].shift()
c["prev_o"] = c.groupby("customer_id")["order"].shift()
within = (c["created_at"] - c["prev_t"]) <= pd.Timedelta(days=7)
same = (c["order"] == c["prev_o"]) | (c["order"] == "") | (c["prev_o"] == "")
c["repeat"] = within & same
print(f"1 May - 14 Jun: {100 * c.loc[~c['after'], 'repeat'].mean():.1f}%  (n = {(~c['after']).sum()})")
q3 = c["month"].between(7, 9)
print(f"Q3: {100 * c.loc[q3, 'repeat'].mean():.1f}%")
print((100 * c.groupby("month")["repeat"].mean()).round(1).to_string())
print("From 15 Jun, by language field:")
lang = c[c["after"]].groupby("language")["repeat"].agg(["mean", "size"])
lang["mean"] = (100 * lang["mean"]).round(1)
print(lang.rename(columns={"mean": "repeat_%", "size": "contacts"}).to_string())

print("\n== Returns share of agent contacts")
print(f"category 'Returns & refunds': {100 * (c['category'] == 'Returns & refunds').mean():.1f}%")
print(f"category 'Damage / defect': {100 * (c['category'] == 'Damage / defect').mean():.1f}%")
print(f"category 'General' or blank: {100 * (c['category'].isin(['General']) | c['category'].isna()).mean():.1f}%")
print(f"tag 'returns': {100 * c['tags'].fillna('').str.contains('returns').mean():.1f}%")

print("\n== Chatbot: 'resolved' sessions followed by an agent contact within 7 days (logged-in only)")
res = s[(s["outcome"] == "resolved") & s["customer_id"].notna()]
by_cust = c.groupby("customer_id")["created_at"].apply(list).to_dict()
res = res.assign(back=[any(t < x <= t + pd.Timedelta(days=7) for x in by_cust.get(cid, []))
                       for cid, t in zip(res["customer_id"], res["started_at"])])
print(f"{100 * res['back'].mean():.1f}% of {len(res)} sessions")
print((100 * res.groupby("bot_intent")["back"].mean()).round(1).to_string())
print(f"sessions in another language (bot says 'other'): {(s['message_language'] == 'other').sum()} of {len(s)}")

print("\n== Refunds")
card = r[(r["refund_method"] == "card") & r["refund_issued_at"].notna()]
days = (card["refund_issued_at"].dt.normalize() - card["requested_at"].dt.normalize()).dt.days
print(f"card refunds {len(card)}: request -> paid median {days.median():.0f} days, over 14 days {100 * (days > 14).mean():.0f}%")
print("weekday paid:", card["refund_issued_at"].dt.day_name().value_counts().to_dict())
insp = r[r["inspected_at"].notna() & r["received_at"].notna()]
bd = np.busday_count(insp["received_at"].dt.date.values.astype("datetime64[D]"),
                     insp["inspected_at"].dt.date.values.astype("datetime64[D]"), weekmask="Sun Mon Tue Wed Thu")
early = insp["received_at"] < pd.Timestamp("2026-08-01", tz="Asia/Jerusalem")
print(f"inspection, business days: median {np.median(bd[early.values]):.0f} before 1 Aug, {np.median(bd[~early.values]):.0f} after")

print("\n== Fees")
paid = r[r["refund_method"].isin(["card", "credit_note"])].copy()
cap = np.minimum(0.05 * paid["item_price_ils"], 100)
defect = paid["reason_code"].isin(["defect", "not_as_described", "late"])
nd = paid[~defect]
over = nd["handling_fee_ils"] > cap[~defect] + 0.01
print(f"non-defect refunds {len(nd)}: handling fee above the cap on {over.sum()} ({100 * over.mean():.1f}%)")
print(f"defect-coded refunds with any deduction: {((paid.loc[defect, 'handling_fee_ils'] + paid.loc[defect, 'shipping_fee_ils']) > 0).sum()} of {defect.sum()}")
print(f"credit notes: {(paid['refund_method'] == 'credit_note').sum()} of {len(paid)} refunds")
