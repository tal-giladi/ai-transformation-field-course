"""Lesson 02.4 (Track B): measure Harbor & Pine's support baselines from the exports.

Prints, for May-October 2026:
  1. volume per month and channel (helpdesk, phone) and the one-week WhatsApp tally;
  2. first response four ways: the KPI report's definition, all tickets on a wall clock,
     all tickets in working hours, phone wait; and what the WhatsApp tally cannot tell you;
  3. the share of "where is my order?" (WISMO) contacts from five independent signals;
  4. a random sample of 100 tickets with a 95% interval, to show what a hand-coded sample gives.

Run from this folder:  python baseline.py
"""
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
sys.stdout.reconfigure(errors="replace")  # Hebrew, Arabic, Russian on any console

import pandas as pd

from fieldkit.baseline import elapsed_hours, sample, summarize, working_hours
from fieldkit.data import data_room, load

room = data_room("harbor-and-pine")
tickets = load(room / "support" / "tickets.csv")
phone = load(room / "support" / "phone-log.csv")
phone["started_at"] = pd.to_datetime(phone["started_at"], utc=True).dt.tz_convert("Asia/Jerusalem")
whatsapp = pd.read_csv(room / "support" / "whatsapp-week-tally.csv", dtype=str, keep_default_na=False)


def heading(text):
    print(f"\n=== {text} ===")


# 1. Volume -----------------------------------------------------------------------------------
heading("1. Volume per month")
tickets["month"] = tickets["created_at"].dt.strftime("%Y-%m")
phone["month"] = phone["started_at"].dt.strftime("%Y-%m")
vol = pd.concat([
    tickets.pivot_table(index="month", columns="channel", values="ticket_id", aggfunc="count"),
    phone.pivot_table(index="month", columns="result", values="call_id", aggfunc="count"),
], axis=1).fillna(0).astype(int)
vol["tickets"] = vol["email"] + vol["web_form"]
vol["calls_in_hours"] = vol["answered"] + vol["abandoned"]
print(vol[["email", "web_form", "tickets", "calls_in_hours", "answered", "abandoned", "after_hours"]].to_string())

minutes = pd.to_numeric(whatsapp["minutes"], errors="coerce")
week_tickets = tickets[(tickets["created_at"] >= "2026-10-18") & (tickets["created_at"] < "2026-10-23")]
print(f"\nWhatsApp hand tally, Sun 18 - Thu 22 Oct 2026: {len(whatsapp)} conversations "
      f"by {whatsapp['agent'].nunique()} agents, {minutes.sum() / 60:.1f} estimated agent-hours "
      f"(median {minutes.median():.0f} min; every estimate is a multiple of 5)")
print(f"Helpdesk tickets created the same five days: {len(week_tickets)}")
print(f"WhatsApp scaled to a month (x 52/12): about {len(whatsapp) * 52 / 12:,.0f} conversations")

# 2. First response ------------------------------------------------------------------------------
heading("2. First response: four definitions")
answered = tickets.dropna(subset=["first_response_at"]).copy()
answered["wall_h"] = elapsed_hours(answered["created_at"], answered["first_response_at"])
answered["work_h"] = working_hours(answered["created_at"], answered["first_response_at"])
q3 = answered[(answered["created_at"] >= "2026-07-01") & (answered["created_at"] < "2026-10-01")]
# The KPI report's footnote: email only, received Sunday-Thursday, working hours 08:00-17:00, average.
kpi_set = q3[(q3["channel"] == "email") & (q3["created_at"].dt.day_of_week.isin([6, 0, 1, 2, 3]))]

rows = [
    ("KPI definition: Q3, email, received Sun-Thu, working hours", summarize(kpi_set["work_h"])),
    ("All tickets, all days, working hours", summarize(answered["work_h"])),
    ("All tickets, all days, wall clock", summarize(answered["wall_h"])),
    ("  email only, wall clock", summarize(answered.loc[answered["channel"] == "email", "wall_h"])),
    ("  web form only, wall clock", summarize(answered.loc[answered["channel"] == "web_form", "wall_h"])),
    ("  Q3 only, wall clock", summarize(q3["wall_h"])),
]
print(pd.DataFrame({name: s for name, s in rows}).T.to_string())

calls = phone[phone["result"].isin(["answered", "abandoned"])]
wait = pd.to_numeric(phone.loc[phone["result"] == "answered", "wait_seconds"])
print(f"\nPhone, answered calls: median wait {wait.median():.0f} s, mean {wait.mean():.0f} s "
      f"(n = {len(wait)}); abandoned {100 * (calls['result'] == 'abandoned').mean():.1f}% "
      f"of in-hours calls; {(phone['result'] == 'after_hours').sum()} calls after hours")
print("WhatsApp tally: no first-response time at all (no timestamps of the customer's message or "
      f"the reply); 'time' is a rough part of the day in {100 * whatsapp['time'].isin(['בוקר', 'צהריים', 'אחה\"צ']).mean():.0f}% of rows")

# 3. WISMO share -------------------------------------------------------------------------------
heading("3. Share of 'where is my order?' (WISMO), five signals")
macro = tickets["tags"].fillna("").str.contains("macro_order_status")
web = tickets[tickets["channel"] == "web_form"]
web_status = web["subject"].str.contains("סטטוס הזמנה|Order status", regex=True)
in_hours = phone[phone["result"] != "after_hours"]
wismo_words = ["מועד אספקה", "עיכוב באספקה", "where is my order", "وين الطلبية", "שואל על משלוח",
               "מתי מגיע", "где заказ", "מועד משלוח", "איפה הספה", "איפה ההזמנה"]
wa_wismo = whatsapp["topic"].apply(lambda t: any(w in t for w in wismo_words))
cat = tickets["category"].fillna("(blank)")
signals = [
    ("Helpdesk tag macro_order_status (lower bound)", macro.sum(), len(tickets)),
    ("Helpdesk category Delivery + Delivery status", cat.isin(["Delivery", "Delivery status"]).sum(), len(tickets)),
    ("Web-form reason 'Order status'", web_status.sum(), len(web)),
    ("Phone IVR option 1 (order status), in hours", (in_hours["ivr_option"] == 1).sum(), len(in_hours)),
    ("WhatsApp tally, delivery-date topics (one week)", wa_wismo.sum(), len(whatsapp)),
]
for name, k, n in signals:
    print(f"{name:52s} {k:5d} / {n:5d} = {100 * k / n:5.1f}%")
print("Note: 'Delivery' (before 1 July) also holds damage reports; from July 'Delivery damage' is separate.")

# 4. A sample ------------------------------------------------------------------------------------
heading("4. A random sample of 100 tickets for hand coding")
s = sample(tickets, 100, seed=7)
print("Ticket ids to read in emails.csv or Deskly (first 20):", ", ".join(map(str, s["ticket_id"].head(20))))
k = int(s["tags"].fillna("").str.contains("macro_order_status").sum())
p = k / len(s)
half = 1.96 * math.sqrt(p * (1 - p) / len(s))
print(f"In this sample the order-status macro was used on {k} of 100 = {100 * p:.0f}% "
      f"(95% interval {100 * (p - half):.0f}-{100 * (p + half):.0f}%); the full export says {100 * macro.mean():.1f}%.")
print("With n = 100 a share is known to about +/-9 points; n = 400 gives about +/-5.")

# 5. Where the time goes -------------------------------------------------------------------------
heading("5. Where agent time goes: time sheets vs the systems")
sheets = load(room / "people" / "timesheets.csv")
staff = sheets[sheets["role"] != "Customer Service Manager"]
buckets = staff[["email_hours", "phone_hours", "other_hours"]].sum()
print(f"Time sheets, 13 staff, Nov 2025 - Oct 2026: email bucket {100 * buckets['email_hours'] / buckets.sum():.1f}% "
      f"of logged hours")
wk = staff[staff["week_start_date"].dt.strftime("%Y-%m-%d") == "2026-10-18"]
print(f"Week of 18 Oct 2026: {wk['email_hours'].sum():.0f} hours in the email bucket, "
      f"{wk['total_logged_hours'].sum():.0f} logged in total")
timer = pd.to_numeric(tickets["time_spent_min"], errors="coerce")
print(f"Helpdesk timer: filled on {100 * timer.notna().mean():.0f}% of tickets, median {timer.median():.0f} min, "
      f"{timer.sum() / 60:.0f} hours in six months")
print(f"Same week: {len(week_tickets)} helpdesk tickets vs {len(whatsapp)} WhatsApp conversations "
      f"({minutes.sum() / 60:.0f} estimated hours) -> written work is mostly WhatsApp, not the helpdesk")

# 6. The delivery promise ---------------------------------------------------------------------------
heading("6. Promised vs actual delivery (orders.csv)")
orders = load(room / "orders" / "orders.csv")
day = lambda col: pd.to_datetime(orders[col].dt.strftime("%Y-%m-%d"))  # calendar date in Israel
orders["lead_days"] = (day("promised_delivery_date") - day("order_created_at")).dt.days
print("Promised lead time by country (days):",
      orders.groupby("supplier_country")["lead_days"].agg(["min", "max"]).to_dict("index"))
orders["late_days"] = (orders["actual_delivery_date"] - orders["promised_delivery_date"]).dt.days
asia = orders["supplier_country"].isin(["Vietnam", "China"])
from_june = orders["promised_delivery_date"].dt.strftime("%Y-%m-%d") >= "2026-06-01"
done = orders["actual_delivery_date"].notna()
for name, mask in [("Vietnam/China, promised from 1 June", asia & from_june & done),
                   ("Vietnam/China, promised before June", asia & ~from_june & done),
                   ("Turkey/Italy, all", ~asia & done)]:
    late = orders.loc[mask, "late_days"]
    print(f"{name:40s} median {late.median():+.0f} days, late {100 * (late > 0).mean():.0f}% (n = {len(late)})")
overdue = orders[~done & (orders["promised_delivery_date"].dt.strftime("%Y-%m-%d") <= "2026-10-31")]
print(f"Past the promised date and not delivered at export (31 Oct): {len(overdue)} orders")

# 7. Do WISMO contacts follow container delays? ---------------------------------------------------
heading("7. WISMO tickets on orders from delayed containers")
ships = load(room / "orders" / "shipments.csv")
ships["delay_days"] = (ships["eta_latest_date"] - ships["eta_original_date"]).dt.days
late_boxes = ships[ships["origin_country"].isin(["Vietnam", "China"])
                   & (ships["eta_original_date"].dt.strftime("%Y-%m-%d") >= "2026-06-01")
                   & (ships["delay_days"] >= 7)]
digits = tickets["order_id"].fillna("").str.replace(r"\D", "", regex=True)
tickets["order_norm"] = ("SO" + digits.where(digits.str.len() != 6, "26" + digits)).where(digits != "")
wismo_t = tickets[macro | tickets["category"].eq("Delivery status")]
j = (wismo_t.merge(orders[["order_id", "container_no"]].drop_duplicates(), left_on="order_norm", right_on="order_id")
            .merge(late_boxes[["container_no", "eta_original_date", "delay_days"]], on="container_no"))
j["days_after_eta"] = (j["created_at"] - j["eta_original_date"]).dt.days
counts = j.groupby("container_no")["days_after_eta"].agg(["median", "size"])
per_box = counts.loc[counts["size"] >= 5, "median"]
print(f"{len(late_boxes)} Vietnam/China containers with original ETA from June and a delay of 7+ days "
      f"(median delay {late_boxes['delay_days'].median():.0f} days)")
print(f"{len(j)} WISMO-tagged tickets on their orders; median {j['days_after_eta'].median():.0f} days after the "
      f"container's original ETA; for the {len(per_box)} containers with 5+ such tickets the per-container "
      f"median lies between {per_box.quantile(0.1):.0f} and {per_box.quantile(0.9):.0f} days (10th-90th percentile)")
