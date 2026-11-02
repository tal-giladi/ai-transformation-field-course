"""Lesson 08.5 (Track A files): build the 200-ticket spreadsheet set, its scoring sheet and paste-ready batches.

    python build_track_a.py

Writes track-a-200.csv (inputs only: order facts and message), scoring-sheet-200.csv (the labels plus
empty columns for your run and your ratings) and batches/batch-01.md ... batch-08.md (25 tickets each).
Same output every time. You do not need to run it: the files are in the download.
"""
import csv
from pathlib import Path

from pilot_lib import order_facts
from sets import labels, load_set

HERE = Path(__file__).resolve().parent
rows = sorted(load_set("track-a"), key=lambda r: r["ticket_id"])
lab = labels()

with (HERE / "track-a-200.csv").open("w", encoding="utf-8", newline="") as f:
    cols = ["ticket_id", "created_at", "channel", "customer_segment", "order_id", "order_channel", "order_date",
            "delivered_date", "item", "item_category", "item_price_ils", "custom_item", "days_since_delivery",
            "return_status", "refund_method", "fees_deducted_ils", "message"]
    w = csv.writer(f, lineterminator="\n")
    w.writerow(cols)
    w.writerows([[r[c] for c in cols] for r in rows])

with (HERE / "scoring-sheet-200.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["ticket_id", "language", "expected_intent", "expected_decision", "expected_fee_ils", "expected_escalate",
                "today_decision", "your_intent", "your_decision", "your_fee_ils", "your_escalate", "intent_correct",
                "decision_correct", "draft_verdict", "safety_issue", "review_seconds", "rater"])
    for r in rows:
        x = lab[r["ticket_id"]]
        w.writerow([r["ticket_id"], x["language"], x["intent"], x["expected_decision"], x["expected_fee_ils"],
                    x["escalate"], x["today_decision"]] + [""] * 10)

(HERE / "batches").mkdir(exist_ok=True)
for b in range(8):
    chunk = rows[b * 25:(b + 1) * 25]
    parts = [f"# Batch {b + 1:02d} of 08 (tickets {chunk[0]['ticket_id']} to {chunk[-1]['ticket_id']})", "",
             "Answer each ticket with one JSON object, in order, one per line.", ""]
    for r in chunk:
        parts += [f"## {r['ticket_id']}", "", f"ORDER FACTS: {order_facts(r)}", "",
                  f"CUSTOMER MESSAGE ({r['channel']}):", "", r["message"], ""]
    (HERE / "batches" / f"batch-{b + 1:02d}.md").write_text("\n".join(parts), encoding="utf-8", newline="\n")
print(f"{len(rows)} tickets: track-a-200.csv, scoring-sheet-200.csv, batches/batch-01..08.md")
