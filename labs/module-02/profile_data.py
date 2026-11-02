"""Lesson 02.5 (Track B): is Harbor & Pine's data AI-ready? Profile six datasets.

For each dataset it prints the checks of the data profile template: completeness of the fields a
pilot would need, whether the outcome (label) was ever recorded, duplicates, stale copies, whether
the dataset joins to the rest, and which columns hold personal data.

Run from this folder:  python profile_data.py
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
sys.stdout.reconfigure(errors="replace")  # Hebrew, Arabic, Russian on any console

import pandas as pd

from fieldkit.data import data_room, load
from fieldkit.profile import duplicates, profile, share

room = data_room("harbor-and-pine")


def heading(text):
    print(f"\n=== {text} ===")


def pct(k, n):
    return f"{k} / {n} = {100 * k / n:.1f}%"


# 1. Helpdesk tickets ----------------------------------------------------------------------------
heading("1. support/tickets.csv")
t = load(room / "support" / "tickets.csv")
print(profile(t[["channel", "order_id", "language", "category", "status", "agent", "time_spent_min", "csat"]])
      [["filled_%", "distinct", "top_values"]].to_string())
print("\nCategory shares (%):", share(t["category"]).head(6).to_dict())
before = t[t["created_at"] < "2026-07-01"]["category"].isin(["Delivery status", "Delivery damage"]).sum()
after = t[t["created_at"] >= "2026-07-01"]["category"].eq("Delivery").sum()
print(f"Category change on 1 July: 'Delivery' used {t['category'].eq('Delivery').sum()} times (all before July: "
      f"{after == 0}); 'Delivery status'/'Delivery damage' before July: {before}")

dups = duplicates(t, ["requester_id"], within="60min", time_col="created_at")
print("Same requester again within 60 minutes:", pct(len(dups), len(t)),
      f"- merged: {dups['tags'].fillna('').str.contains('merged').sum()}, answered separately: "
      f"{(~dups['tags'].fillna('').str.contains('merged')).sum()}")

def norm_order(x):
    if pd.isna(x):
        return None
    digits = re.sub(r"\D", "", str(x))
    if len(digits) == 6:          # '#004521' -> the year was dropped
        digits = "26" + digits
    return "SO" + digits if digits else None

t["order_norm"] = t["order_id"].map(norm_order)
typed = t["order_id"].notna() & ~t["order_id"].fillna("").str.fullmatch(r"SO26\d{6}")
print("Order numbers typed by hand (not SO26nnnnnn):", pct(int(typed.sum()), int(t["order_id"].notna().sum())))

res = t[(t["status"] == "resolved") & t["order_norm"].notna()]
later = t[t["order_norm"].notna()][["ticket_id", "requester_id", "order_norm", "created_at"]]
pairs = res.merge(later, on=["requester_id", "order_norm"], suffixes=("", "_next"))
pairs = pairs[(pairs["created_at_next"] > pairs["resolved_at"]) &
              (pairs["created_at_next"] <= pairs["resolved_at"] + pd.Timedelta(days=14))]
followed = pairs["ticket_id"].nunique()
print("'Resolved' tickets with an order that get a new ticket from the same customer on the same order "
      "within 14 days:", pct(followed, len(res)))
fast = (t["resolved_at"] - t["first_response_at"]).dt.total_seconds().le(300)
print("Resolved within 5 minutes of the first reply (status = 'reply sent'):",
      pct(int((fast & t["status"].eq("resolved")).sum()), int(t["status"].eq("resolved").sum())))

# 2. Emails ----------------------------------------------------------------------------------------
heading("2. support/emails.csv (full text of 600 tickets)")
e = load(room / "support" / "emails.csv")
print(f"{len(e)} emails; personal data in from_name, from_address and the free text (addresses, phones):")
phones = e["body"].str.contains(r"05\d[- ]?\d{7}|05\d-\d{3}-\d{4}", regex=True).sum()
print(f"  bodies with a mobile number: {phones}; with an order number: "
      f"{e['body'].str.contains(r'SO\s?-?26', regex=True).sum()}")
print("  Is the 600 a random sample? Compare its months with the export:")
print("  ", e["received_at"].dt.strftime("%Y-%m").value_counts().sort_index().to_dict())

# 3. Damage claims log ---------------------------------------------------------------------------
heading("3. claims/damage-claims-log.csv (hand-kept, Rina)")
c = pd.read_csv(room / "claims" / "damage-claims-log.csv", dtype=str, keep_default_na=False)
decision = c["החלטה"]
print("Columns:", ", ".join(c.columns))
print("Decision (outcome label) blank:", pct(int((decision == "").sum()), len(c)))
print("Recorded decisions:", decision[decision != ""].value_counts().to_dict())
opened = pd.to_datetime(c["תאריך פתיחה"], dayfirst=True, errors="coerce")
decided = pd.to_datetime(c["תאריך החלטה"], dayfirst=True, errors="coerce")
days = (decided - opened).dt.days.dropna()
print(f"Days from opening to decision: median {days.median():.0f}; within 2 days {100 * (days <= 2).mean():.0f}% "
      f"(the handbook promises QA review within 48 hours; no QA column exists)")
old = opened <= "2026-09-30"
print("Decision blank among claims opened by 30 Sep:", pct(int(((decision == "") & old).sum()), int(old.sum())))
print("Personal data: customer name and phone in every row; the file sits on the shared drive")

# 4. Catalogue copies ----------------------------------------------------------------------------
heading("4. catalog/: the current catalogue vs the 2023 shared-drive copy")
cur = load(room / "catalog" / "products.csv")
old_copy = pd.read_csv(room / "catalog" / "products-2023-shared-drive-copy.csv", dtype=str)
old_copy = old_copy.rename(columns={old_copy.columns[0]: "sku", "מחיר לצרכן": "old_price"})
m = old_copy.merge(cur[["sku", "status", "list_price_ils"]], on="sku", how="left")
m["old_price"] = pd.to_numeric(m["old_price"])
active = cur[cur["status"] == "active"]
print(f"Current: {len(cur)} SKUs ({(cur['status'] == 'discontinued').sum()} discontinued). Copy: {len(old_copy)} SKUs")
print(f"In the copy but discontinued now: {(m['status'] == 'discontinued').sum()}; "
      f"active SKUs missing from the copy: {(~active['sku'].isin(old_copy['sku'])).sum()}")
both = m.dropna(subset=["list_price_ils"])
gap = 100 * (both["list_price_ils"] - both["old_price"]) / both["list_price_ils"]
print(f"Copy price below current price: median {gap.median():.1f}% (n = {len(both)})")

# 5. Container ETAs: export vs the hand-kept sheet -----------------------------------------------
heading("5. orders/shipments.csv vs orders/logistics-eta-tracking.csv")
s = load(room / "orders" / "shipments.csv")
sheet = pd.read_csv(room / "orders" / "logistics-eta-tracking.csv", dtype=str, keep_default_na=False)
box = sheet.columns[0]
rows = sheet[~sheet[box].str.startswith("---") & (sheet[box].str.strip() != "")]
nums = rows[box].str.replace(" ", "", regex=False)
print(f"Sheet lines: {len(sheet)}; container rows: {len(rows)}; entered twice: "
      f"{sorted(nums[nums.duplicated()].unique())}; typed with a space: {rows[box].str.contains(' ').sum()}")
fmts = rows[sheet.columns[4]].map(lambda v: "dd/mm/yy" if re.fullmatch(r"\d{2}/\d{2}/\d{2}", v) else
                                  "yyyy-mm-dd" if re.fullmatch(r"\d{4}-\d{2}-\d{2}", v) else
                                  "d.m" if re.fullmatch(r"\d{1,2}\.\d{1,2}", v) else "blank" if v == "" else "other")
print("Original-ETA date formats:", fmts.value_counts().to_dict())
eta = s["eta_original_date"].dt.strftime("%Y-%m-%d")
in_window = s[(eta >= "2026-05-01") & (eta <= "2026-10-31")]
print(f"Containers in the export with an original ETA May-Oct: {len(in_window)}; "
      f"missing from the sheet: {sorted(in_window.loc[~in_window['container_no'].isin(nums), 'container_no'])}")

# 6. WhatsApp tally -------------------------------------------------------------------------------
heading("6. support/whatsapp-week-tally.csv (one week, typed by hand)")
w = pd.read_csv(room / "support" / "whatsapp-week-tally.csv", dtype=str, keep_default_na=False)
date_fmt = w["date"].map(lambda v: "dd/mm/yyyy" if re.fullmatch(r"\d{2}/\d{2}/\d{4}", v) else
                         "dd/mm" if re.fullmatch(r"\d{2}/\d{2}", v) else "dd.mm" if re.fullmatch(r"\d{2}\.\d{2}", v) else "other")
print("Date formats:", date_fmt.value_counts().to_dict())
print("Language values:", w["customer_language"].replace("", "(blank)").value_counts().to_dict())
print("Distinct topic labels (free text, four languages):", w["topic"].nunique())
filled = w["order_no"] != ""
print("Order number filled:", pct(int(filled.sum()), len(w)), "- format",
      w.loc[filled, "order_no"].str.replace(r"\d", "9", regex=True).value_counts().to_dict())
erp = load(room / "orders" / "orders.csv")
print("Of those, found in the ERP orders export:", int(w.loc[filled, "order_no"].isin(erp["order_id"]).sum()))
print("No export exists: the conversations themselves are on four shared phones")
