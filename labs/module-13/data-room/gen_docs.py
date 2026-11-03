"""Company documents: profile, org chart, the meeting where the ask was made, the KPI deck, the budget,
the customer's letter, the PM report and the failure-code list.

Reading this spoils the engagement: finish module 13 first.
"""
from __future__ import annotations

import csv

from gen_common import ROOM, write_csv, write_text

FAILURE_CODES = [
    ("H01", "משאבה הידראולית", "Hydraulic pump", "Hydraulics"), ("H02", "שסתום", "Valve", "Hydraulics"),
    ("H03", "צנרת / דליפה", "Hose / leak", "Hydraulics"), ("H04", "טמפ' שמן / מחליף חום", "Oil temperature / cooler", "Hydraulics"),
    ("E01", "גוף חימום", "Heater band", "Electrical"), ("E02", "תרמוקפל", "Thermocouple", "Electrical"),
    ("E03", "מגען / ממסר", "Contactor / relay", "Electrical"), ("E04", "דרייבר / סרוו", "Drive / servo", "Electrical"),
    ("E05", "בקר / כרטיס IO", "PLC / IO card", "Electrical"), ("M01", "בורג / צילינדר / טבעת", "Screw / barrel / check ring", "Mechanical"),
    ("M02", "טוגל / סגירה", "Toggle / clamp", "Mechanical"), ("M03", "מפלט מכונה", "Machine ejector", "Mechanical"),
    ("M04", "שימון", "Lubrication", "Mechanical"), ("S01", "דלת מגן / אינטרלוק", "Safety gate / interlock", "Safety"),
    ("S02", "עצירת חירום", "Emergency stop", "Safety"), ("R01", "רובוט", "Robot", "Automation"),
    ("A01", "מייבש", "Dryer", "Auxiliary"), ("A02", "צ'ילר", "Chiller", "Auxiliary"),
    ("A03", "בקר טמפ' תבנית", "Mould temperature controller", "Auxiliary"), ("P01", "פנאומטיקה", "Pneumatics", "Auxiliary"),
    ("90", "טעות מפעיל", "Operator error", "Other"), ("91", "חומר גלם", "Material", "Other"),
    ("92", "תבנית - להעביר לכלים", "Mould (send to tooling)", "Other"), ("99", "אחר", "Other", "Other"),
]


def _read(rel: str) -> list[dict]:
    with open(ROOM / rel, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_all(fig: dict) -> None:
    write_csv(ROOM / "maintenance" / "failure-codes.csv",
              ["code", "description_he", "description_en", "group"], [list(x) for x in FAILURE_CODES])
    _profile()
    _org_chart()
    _minutes()
    _deck(fig)
    _budget()
    _arava()
    _pm_report(fig)


def _profile() -> None:
    write_text(ROOM / "company" / "company-profile.md", """# Kinneret Plastics Ltd. — company profile (January 2027)

*From the 2027 bank credit presentation, prepared by the CFO's office. All figures fictional.*

| | |
|---|---|
| Founded | 1978 by Shmuel Shaked; CEO since 2009: Amnon Shaked (64% of shares; his sister Ruth Shaked-Levin 36%, board member) |
| Business | Injection-moulded plastic parts: caps and closures for beverage and dairy (52% of revenue), technical parts for home appliances (31%), crates and logistics items (17%) |
| Revenue 2026 | ₪412 million (2025: ₪398 million); EBITDA ₪38 million |
| Largest customer | Arava Home Appliances, 17% of revenue (technical parts, two-year supply agreement to December 2027) |
| People | About 600: Plant K 372, Plant G 176, head office and sales 52 (at Plant K). Three shifts, Sunday 06:45 to Friday 06:45 |
| Plant K (Kinneret) | Industrial zone south of Tiberias. 26 injection-moulding machines (80 to 650 tonnes), 14 robots, tooling shop |
| Plant G (Galil) | Industrial park near Karmiel. Acquired January 2025 ("Galil Polymer Industries"). 14 machines. Integration "completed" in 2025 (ERP, MES, HR) |
| Systems | ERP (both plants since July 2025); MES ProdTrack (Plant K March 2025, Plant G June 2025); CMMS MaintPro (Plant K only, since 2014); historian on three machines (since October 2026) |
| Certifications | ISO 9001; IATF 16949 gap assessment in 2026 at Arava's request |
| Workforce | Organised workplace; works committee with the Histadrut; local agreement 2021 |
""")


def _org_chart() -> None:
    write_text(ROOM / "company" / "org-chart.md", """# Organisation chart (January 2027, extract)

```
CEO — Amnon Shaked
├── CFO — Orit Navon (finance, purchasing, IT through Boaz Tal and an outsourced provider)
├── VP Operations and Plant K manager — Dalia Mizrahi
│   ├── Operations excellence — you (manager) + Lina Haddad (analyst, half-time)
│   ├── Production Plant K — 3 shift supervisors per rotation (incl. Tigist Wondimu, Yaron Avraham, Muhammad Zoabi)
│   ├── Maintenance Plant K — Vladimir Kaplan (manager); planner Svetlana Petrova; 11 technicians; 2 electricians
│   ├── Tooling (both plants) — Fadi Khoury; 7 toolmakers (day shift, Sunday–Thursday)
│   └── Warehouse and stores — Avi Malka
├── Plant G manager — Eli Peretz
│   ├── Production Plant G — 3 shift leaders
│   └── Maintenance Plant G — Shlomi Biton (lead) and 5 technicians
├── Quality (both plants) — Rotem Levi
├── Safety officer (both plants) — Yaakov Dahan (ממונה בטיחות)
├── HR — Michal Aharon
└── Sales and customer service — Danny Golan
Works committee (both plants since 2025) — chair Khalil Mansour (mould setter, Plant K)
```

Maintenance on call at night: one technician per shift on site at Plant K, one at Plant G. The "on-call senior
technician" rota (SOP-ESC-07) is kept by Vladimir Kaplan.
""")


def _minutes() -> None:
    write_text(ROOM / "company" / "management-meeting-2027-01-07-minutes.md", """# Annual management meeting — minutes (extract)

*Thursday 7 January 2027, 09:00–14:00, Plant K meeting room. Minutes: Michal Aharon. Present: Amnon Shaked
(chair), Orit Navon, Dalia Mizrahi, Eli Peretz, Rotem Levi, Danny Golan, Michal Aharon, Fadi Khoury, the
operations-excellence manager. Absent: Vladimir Kaplan (night breakdown on K07, came in at 02:00).*

**1. 2026 results.** Revenue ₪412M, EBITDA ₪38M, below plan by ₪4M "mainly from overtime and expedited
freight in Q3–Q4".

**2. Arava.** Danny presented Arava's letter of 14 December (on-time-in-full 81% against 95%). Arava wants a
corrective-action plan by 31 March 2027. Amnon: "We will not lose Arava over machines that break."

**3. 2027 priorities.** Amnon: "2027 is the year of AI. We start with predictive maintenance. I saw at the
conference in December what Predictiva does: the machines tell you before they break. [The operations-excellence
manager] leads it, with Dalia." Orit: a line of ₪1.5M "AI and Industry 4.0" is in the 2027 budget; any
commitment above ₪50,000 comes to her and to Amnon. Eli: "Plant G is ready, we already filled Predictiva's
data questionnaire." Rotem asked that quality be included. Fadi asked whether moulds are part of it; no answer
was recorded.

**Decisions.** Predictive maintenance is a 2027 priority, led by the operations-excellence manager; first
recommendation to management on Tuesday 23 March 2027; Predictiva to be invited to present.
""")


def _deck(fig: dict) -> None:
    uh = fig["unplanned_hours"]
    def hours(plant: str, codes: tuple) -> int:
        return sum(uh.get(f"{plant}:{c}", 0) for c in codes)
    rows = []
    for plant in ("K", "G"):
        br = hours(plant, ("MECH", "ELEC", "HYD", "MOULD"))
        rows.append(f"| Plant {plant} | {br} | {hours(plant, ('MAT',))} | {hours(plant, ('WAIT_TECH',))} | "
                    f"{hours(plant, ('QA_HOLD', 'OTHER'))} |")
    ratio = fig["mttr_k"] / fig["mttr_g"]
    write_text(ROOM / "company" / "kpi-deck-2026-12-extract.md", f"""# Operations KPI deck — December 2026 (extract)

*Monthly operations review, 29 December 2026. Slides 4–6. Prepared by operations excellence with data from
ProdTrack, MaintPro and Plant G's maintenance log.*

## Slide 4 — Maintenance

| KPI | Plant K | Plant G | Target |
|---|---|---|---|
| MTTR (mean time to repair), 2026 | **{fig['mttr_k']} h** | **{fig['mttr_g']} h** ✅ | 2.5 h |
| PM compliance, 2026 | {fig['pm_compliance']}% | — | 90% |
| Machines with condition monitoring | 3 of 26 | 0 of 14 | — |

Headline on the slide: "Plant G repairs {ratio:.1f}× faster — learn from Galil."

## Slide 5 — Unplanned downtime by reason, 2026 (hours)

| Plant | Breakdowns | Material | Waiting for technician | QA hold and other |
|---|---|---|---|---|
{chr(10).join(rows)}

Headline on the slide: "Breakdowns are the number one loss — and they can be predicted."

## Slide 6 — 2027

"Predictive maintenance pilot (AI) — Q1 decision."

---
<sub>Footnotes on slide 4: (1) Plant K MTTR from ProdTrack downtime events with reasons MECH, ELEC, HYD, MOULD,
WAIT_TECH: from stop to restart. (2) Plant G MTTR from the Plant G maintenance log: from call to "ready".
(3) PM compliance = PM work orders closed ÷ PM work orders scheduled (MaintPro).
(4) Slide 5: breakdowns = ProdTrack reasons MECH, ELEC, HYD and MOULD; planned stops (PM, SETUP, NO_ORDER) excluded.</sub>
""")


def _budget() -> None:
    write_text(ROOM / "company" / "budget-2027-extract.md", """# 2027 budget — operations extract (approved by the board 22 December 2026)

| Line | Item | 2026 actual | 2027 budget | Owner |
|---|---|---|---|---|
| 5100 | Maintenance Plant K: labour (11 technicians, 2 electricians, planner, manager) | ₪5.9M | ₪6.1M | Dalia Mizrahi |
| 5110 | Maintenance Plant K: parts and services | ₪3.4M | ₪3.3M | Dalia Mizrahi |
| 5200 | Maintenance Plant G: labour and parts | ₪3.1M | ₪3.1M | Eli Peretz |
| 5300 | Tooling (both plants) | ₪4.2M | ₪4.2M | Dalia Mizrahi |
| 6100 | Overtime, production (both plants) | ₪6.8M | ₪4.9M | Dalia Mizrahi |
| 6150 | Expedited freight to customers | ₪1.1M | ₪0.4M | Danny Golan |
| 7400-210 | **AI and Industry 4.0** (new) | — | **₪1.5M** | Orit Navon (released by CFO and CEO) |
| 8200 | Capex: two new machines for Plant G | — | ₪6.0M | Orit Navon |

Notes from the CFO: lines 6100 and 6150 assume "a significant reduction in unplanned downtime". Line 7400-210
has no approved content yet. Kinneret's hurdle rate for projects is 12% a year; payback expected within 24
months for anything "that is not safety or compliance".
""")


def _arava() -> None:
    write_text(ROOM / "company" / "arava-letter-2026-12-14.md", """# Letter from Arava Home Appliances

*14 December 2026. From: Supplier Quality and Purchasing, Arava Home Appliances Ltd. To: Amnon Shaked, CEO,
Kinneret Plastics. Copy: Danny Golan, Rotem Levi. (Arava is fictional.)*

Subject: Supplier performance 2026 — request for a corrective-action plan

1. Kinneret's on-time-in-full (OTIF) performance for 2026 to date is **81%** against the **95%** in our supply
   agreement. 22 shipments were late; in 14 of the late-shipment notices Kinneret gave "machine breakdown" as
   the reason, in 5 "tooling", in 3 "material".
2. Two shipments in October contained parts with short shots (8D reports AR-26-114 and AR-26-131); both were
   produced on the night shift.
3. We ask for a corrective-action plan by **31 March 2027** addressing the root causes, with measurable
   targets and dates. We will review it with our second-source qualification for 2027, which is ready to
   take up to 30% of the volume.

We value the relationship and the quality of your parts when they arrive.
""")


def _pm_report(fig: dict) -> None:
    wo = _read("maintenance/work-orders-plant-k-2026.csv")
    lines = []
    for month in range(1, 13):
        pm = [x for x in wo if x["wo_type"] == "PM" and x["requested_at"][5:7] == f"{month:02d}"]
        closed = sum(1 for x in pm if x["status"] == "סגור")
        lines.append(f"| {month:02d}/2026 | {len(pm)} | {closed} | {round(100 * closed / len(pm))}% |")
    write_text(ROOM / "maintenance" / "pm-compliance-report-2026.md", f"""# Preventive maintenance compliance — Plant K, 2026

*Prepared by Svetlana Petrova (maintenance planner) for Vladimir Kaplan, 3 January 2027. Source: MaintPro.*

| Month | PM work orders scheduled | Closed | Compliance |
|---|---|---|---|
{chr(10).join(lines)}
| **2026** | **{fig['pm_total']}** | **{fig['pm_closed']}** | **{fig['pm_compliance']}%** |

Definition: a PM work order counts as compliant when its status is "closed" in MaintPro at the time of the
report. Target 90%.

Comment: "Q3 was difficult because of the summer programme. All PMs were closed by the end of September."
""")
