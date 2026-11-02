"""Lesson 05.2 (Track B): build the pilot's test set from Harbor & Pine's real support emails.

What it does, in order:
  1. joins the 600 full-text emails (support/emails.csv) with the helpdesk export (tickets.csv),
     the team's adjudicated labels (labels.csv, this folder) and the order data;
  2. finds each message's order number (the helpdesk field first, then the text, normalised);
  3. writes the ORDER CONTEXT line the date fix would have known on the day the message arrived
     (orders.csv + shipments.csv: latest container ETA + 7 days);
  4. pseudonymises every message and every agent reply (names, e-mails, phones, ID and card numbers);
  5. splits the 600 into a 400-item TEST set and a 200-item DEV set, stratified by language and
     category with a fixed seed: you tune the prompt on DEV and score it once on TEST;
  6. writes the Track A files: paste-ready batches, the scoring sheet and a 40-item labelling sample.

Run from this folder:   python build_test_set.py
Same output every time (seed 20261215). No API key, no network.
"""
import csv
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))

import pandas as pd

from fieldkit.data import data_room, load
from pilot_lib import (find_order, normalise_order, order_context, pseudonymise, script_language)

SEED = 20261215
TEST_SIZE = 400
BATCH = 25

room = data_room("harbor-and-pine")
emails = pd.read_csv(room / "support" / "emails.csv", dtype=str, keep_default_na=False)
tickets = pd.read_csv(room / "support" / "tickets.csv", dtype=str, keep_default_na=False)
labels = pd.read_csv(HERE / "labels.csv", dtype=str, keep_default_na=False)
orders = load(room / "orders" / "orders.csv")
shipments = load(room / "orders" / "shipments.csv")

order_by_id = {r["order_id"]: r for r in orders.to_dict("records")}
ship_by_container = {r["container_no"]: r for r in shipments.to_dict("records")}

df = (emails.merge(tickets[["ticket_id", "channel", "order_id", "language", "category"]], on="ticket_id", how="left")
      .merge(labels, on="email_id", how="left", suffixes=("", "_label")))
missing = df["category_label"].eq("") | df["category_label"].isna()
if missing.any():
    raise SystemExit(f"{missing.sum()} emails have no label in labels.csv")

rows = []
pseudo_counts = Counter()
order_source = Counter()
for r in df.to_dict("records"):
    received = pd.Timestamp(r["received_at"]).date()
    order_id = normalise_order(r["order_id"])
    if order_id:
        order_source["helpdesk field"] += 1
    else:
        order_id = find_order(r["subject"] + " " + r["body"])
        order_source["found in the text" if order_id else "none"] += 1
    order = order_by_id.get(order_id)
    ship = ship_by_container.get(order["container_no"]) if order else None
    ctx = order_context(order, ship, received)
    subject, c1 = pseudonymise(r["subject"], [r["from_name"]])
    message, c2 = pseudonymise(r["body"], [r["from_name"]])
    reply, c3 = pseudonymise(r["reply_body"], [r["from_name"]])
    for c in (c1, c2, c3):
        pseudo_counts.update(c)
    rows.append({
        "email_id": r["email_id"], "ticket_id": r["ticket_id"], "received_date": str(received),
        "channel": r["channel"], "subject": subject, "message": message,
        "attachments_count": len([a for a in r["attachments"].split(";") if a.strip()]),
        "order_id": order_id if order else "", "order_context": ctx["line"],
        "promised_date": ctx["promised"] or "", "expected_date": ctx["expected"] or "",
        # ground truth: the team's adjudicated labels (05.2)
        "expected_category": r["category_label"], "expected_language": r["language_label"],
        "expected_reply_language": "none" if r["category_label"] == "spam" else r["language_label"],
        "kind": r["kind"],
        # what happens today, for comparison (05.4)
        "helpdesk_category": r["category"], "helpdesk_language": r["language"],
        "agent_reply": reply, "agent_reply_date": r["reply_sent_at"][:10],
    })
data = pd.DataFrame(rows)

# --- Stratified split: exactly TEST_SIZE items, every language x category cell split 2:1 ------------
rng = random.Random(SEED)
cells = defaultdict(list)
for i, r in data.iterrows():
    cells[(r["expected_language"], r["expected_category"])].append(i)
share = TEST_SIZE / len(data)
quota = {k: int(len(v) * share) for k, v in cells.items()}
rest = TEST_SIZE - sum(quota.values())
for k in sorted(cells, key=lambda k: (-(len(cells[k]) * share - quota[k]), k))[:rest]:
    quota[k] += 1
test_idx = []
for k in sorted(cells):
    ids = sorted(cells[k])
    rng.shuffle(ids)
    test_idx += ids[:quota[k]]
data["set"] = "dev"
data.loc[test_idx, "set"] = "test"


def number(frame: pd.DataFrame, prefix: str) -> pd.DataFrame:
    frame = frame.sort_values(["received_date", "email_id"]).reset_index(drop=True)
    frame.insert(0, "item_id", [f"{prefix}-{i + 1:03d}" for i in range(len(frame))])
    return frame


test = number(data[data["set"] == "test"].drop(columns="set"), "T")
dev = number(data[data["set"] == "dev"].drop(columns="set"), "D")
test.to_csv(HERE / "test-set.csv", index=False, encoding="utf-8", lineterminator="\n")
dev.to_csv(HERE / "dev-set.csv", index=False, encoding="utf-8", lineterminator="\n")

# --- Track A: paste-ready batches (inputs only, no labels) -------------------------------------------
neg = pd.read_csv(HERE / "negative-tests.csv", dtype=str, keep_default_na=False)
bdir = HERE / "batches"
bdir.mkdir(exist_ok=True)


def batch_text(frame: pd.DataFrame, title: str) -> str:
    out = [f"# {title}", "",
           "Paste everything below the line into your pilot assistant as one message.", "", "---", ""]
    for r in frame.to_dict("records"):
        atts = int(r.get("attachments_count") or 0)
        out += [f"ITEM: {r['item_id']}", f"CHANNEL: {r.get('channel') or 'email'}",
                f"RECEIVED: {r['received_date']}", f"SUBJECT: {r['subject']}",
                f"ATTACHMENTS: {f'{atts} file(s)' if atts else 'none'}",
                f"ORDER CONTEXT: {r['order_context'] or 'none'}", "MESSAGE:", "<<<", r["message"], ">>>", ""]
    return "\n".join(out)


for name, frame in (("test", test), ("dev", dev)):
    for b in range(0, len(frame), BATCH):
        part = frame.iloc[b:b + BATCH]
        n = b // BATCH + 1
        title = f"{name.upper()} batch {n:02d} — items {part.iloc[0]['item_id']} to {part.iloc[-1]['item_id']}"
        (bdir / f"{name}-batch-{n:02d}.md").write_text(batch_text(part, title), encoding="utf-8", newline="\n")
(bdir / "negative-batch.md").write_text(batch_text(neg, "NEGATIVE TESTS — items N-01 to N-24"),
                                        encoding="utf-8", newline="\n")

# --- Track A: the scoring sheet (expected values filled, your run's columns empty) -------------------
sheet_cols = ["item_id", "set", "expected_language", "expected_category", "expected_flags",
              "expected_reply_language", "predicted_category", "predicted_language", "predicted_flags",
              "category_correct", "flags_correct", "draft_verdict", "safety_issue", "review_seconds",
              "rater", "notes"]
with open(HERE / "scoring-sheet.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(sheet_cols)
    for r in test.to_dict("records"):
        w.writerow([r["item_id"], "test", r["expected_language"], r["expected_category"], "",
                    r["expected_reply_language"]] + [""] * 10)
    for r in neg.to_dict("records"):
        w.writerow([r["item_id"], "negative", r["expected_language"], r["expected_category"],
                    r["expected_flags"], r["expected_reply_language"]] + [""] * 10)

# --- 05.2 practice: 40 items to label yourself before you look at the labels -----------------------
cal = pd.concat([test[test["expected_language"] == lang].sample(10, random_state=SEED) for lang in ["he", "ar", "ru", "en"]])
cal = cal.sort_values("item_id")[["item_id", "subject", "message"]].assign(your_category="", your_language="")
cal.to_csv(HERE / "labelling-sample-40.csv", index=False, encoding="utf-8", lineterminator="\n")

# --- Report ------------------------------------------------------------------------------------------
def table(frame: pd.DataFrame) -> pd.DataFrame:
    t = pd.crosstab(frame["expected_category"], frame["expected_language"], margins=True, margins_name="total")
    return t[["he", "ar", "ru", "en", "total"]]


print(f"Emails read: {len(data)} · test set {len(test)} · dev set {len(dev)} · negative tests {len(neg)}")
print(f"Order number: {dict(order_source)}")
print(f"With order context: test {int((test['order_context'] != 'none').sum())}, "
      f"of which an expected delivery date: {int((test['expected_date'] != '').sum())}")
print("Replaced while pseudonymising:", dict(pseudo_counts))
left = sum(bool(script_language(m) == '') for m in test["message"])
print(f"Messages with no letters left after pseudonymising: {left}")
print("\nTEST set, category x language:\n" + table(test).to_markdown())
print("\nDEV set, category x language:\n" + table(dev).to_markdown())
print(f"\nWrote test-set.csv, dev-set.csv, scoring-sheet.csv, labelling-sample-40.csv and "
      f"{len(list(bdir.glob('*.md')))} batch files in batches/")
