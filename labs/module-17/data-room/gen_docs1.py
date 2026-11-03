"""company/, correspondence/, people/staff-directory-extract.csv, customers/key-accounts.csv."""
from gen_common import write_md, write_csv

PROFILE = """
# Vantage Logistics Ltd. — company profile (June 2027)

*Prepared by Investor Relations for new directors and advisers. All figures unaudited unless stated.*

Vantage Logistics Ltd. (ואנטג' לוגיסטיקה בע"מ) is an Israeli logistics and freight-forwarding group. It was founded in Haifa in 1988 as a customs brokerage, added trucking in 1996 and contract warehousing in 2004, and has been listed on the Tel Aviv Stock Exchange since 2011. Head office: Petah Tikva.

| | |
|---|---|
| Revenue 2026 | ₪1.04bn (audited) |
| Operating profit 2026 | ₪61M |
| Staff | about 1,200 (North ~330, Centre ~420 incl. head office functions, South ~290, Europe ~60, head office ~100) |
| Fleet | 310 trucks with telematics (Mabat Fleet) |
| Customs | licensed customs agents at Haifa Port, Ashdod Port and Ben Gurion Airport customs houses; about 6,100 import declarations a month |
| Warehousing | Modi'in DC (118 staff), Ashdod DC (96 staff), bonded areas at both ports |
| Europe | Vantage Europe B.V., Rotterdam: forwarding office and a small trucking unit (44 drivers) |
| Customers | about 1,900 active accounts; top 20 = 41% of revenue |

**Regions.** North (Haifa Port, Karmiel, Kiryat Shmona), Centre (Modi'in DC, Airport Logistics Park, Petah Tikva), South (Ashdod Port, Be'er Sheva, Netivot), Europe (Rotterdam). Each region has an operations manager reporting to the COO.

**People and languages.** Drivers, warehouse and customs staff speak Hebrew, Arabic, Russian, Amharic and English; Vantage Europe works in Dutch and English. Drivers, warehouse and customs staff in Israel are covered by a collective agreement; a works committee (ועד עובדים) represents them.

**AI programme.** Started in January 2026 under a head of AI & innovation reporting to the CEO. See the board deck of 25 March 2027 and the board minute of 3 June 2027.

**Fictional company.** Vantage Logistics, its people, customers, vendors and data are fictional. Unrelated firms with similar names exist abroad; none is portrayed.
"""

ORG = """
# Organisation chart (June 2027, extract)

```
Board of directors (chair: Yehuda Karni)
 ├─ Audit committee (chair: Dr. Ilana Shaked, external director)
 ├─ Internal auditor (outsourced: R. Adler, CPA)
 └─ CEO: Ofer Lavi
     ├─ CFO: Svetlana Morozov ── Finance, Procurement, Investor Relations
     ├─ COO: Moti Azulay
     │    ├─ Region North: Fadi Khatib
     │    ├─ Region Centre: Gal Rosen
     │    ├─ Region South: Rania Haj-Yahia
     │    ├─ Vantage Europe B.V.: Pieter van Dijk
     │    ├─ Customs brokerage: Shlomo Peretz (licensed customs agent; 31 agents)
     │    ├─ Warehousing: Hanna Desta
     │    └─ Transport safety officer: Eitan Mor
     ├─ General counsel and privacy protection officer: Adv. Yael Sharabi
     ├─ Head of IT & information security: Dmitri Volkov
     ├─ VP Customers (sales, customer service): Ronit Cohen-Elbaz
     │    └─ Customer service manager: Marina Levitan
     ├─ VP HR: Anat Gold
     └─ Head of AI & innovation: vacant since 27 May 2027 (Itai Barkan)
          ├─ Data scientist: Lior Gabay
          └─ Analyst: Noa Peretz
```

Works committee: chair Avi Ohana (warehouse, Modi'in); drivers' representative Tesfaye Worku (driver, South).
"""

MINUTES = """
# Board of directors — special session, 3 June 2027 (extract, item 2)

*Present: Y. Karni (chair), Dr. I. Shaked, five further directors. Attending: O. Lavi (CEO), S. Morozov (CFO), Adv. Y. Sharabi (general counsel, secretary). Draft minutes, not yet approved.*

**Item 2 — The AI programme**

The CEO reported that the head of AI & innovation, Itai Barkan, resigned on 27 May. The CEO described the incident of 18 May as "a document mix-up in the customs module, contained by the vendor within days, with no personal data involved". He proposed to recruit a replacement and to "get the savings back on track".

Dr. Shaked said the audit committee could not assess the programme on the information before it: the deck of 25 March reported seven systems in four regions, ₪6.2M of annual savings and no incidents; the external auditor has asked about the savings recognised in the 2027 budget; and the board has not seen a report of the incident.

After discussion the board resolved:

1. The last AI lead left; the board wants answers in 30 days. An interim AI lead will be engaged for 30 days, on the audit committee's proposal, reporting to the chair of the audit committee and to the CEO.
2. The interim lead will report to the board on **Monday 5 July 2027**, with the audit committee receiving the pre-read on **Thursday 1 July**: what AI systems are running, what they cost, what they have delivered, what happened in the May incident and whether it is closed, and whether and how to continue.
3. Until then, no new AI commitment above ₪250,000 without the audit committee chair's knowledge.
4. The CEO added: "and a plan to get the savings back on track". Noted.
"""

DECK = """
# AI programme — board update, 25 March 2027

*Presented by Itai Barkan, head of AI & innovation. Slide text as exported.*

## Slide 1 — Vantage AI: from pilots to platform

- 7 AI systems in production
- 4 regions live on Tzir Route (310 drivers)
- ₪6.2M annual savings in the 2027 budget
- 0 incidents

## Slide 2 — Tzir platform

- One vendor, three modules: Route, Docs, Assist. Signed September 2026.
- Route: live in North, Centre, South and Europe. Fuel and km savings of 18% versus baseline (Tzir value dashboard).
- Docs: customs declarations pre-filled since 1 February. 99.2% accuracy. Every declaration reviewed by a licensed agent.
- Assist: customer-portal assistant live 15 March. Target 35% deflection of customer-service contacts.

## Slide 3 — Savings in the 2027 budget

| Line | ₪ a year | Source |
|---|---|---|
| Fuel and km (Route) | 3,100,000 | Tzir value dashboard, projected for 4 regions |
| Customs productivity (Docs) | 1,600,000 | 8 FTE of agent time freed (31 agents at 12 a day instead of 9) |
| Customer-service deflection (Assist) | 900,000 | 35% of contacts |
| Warehouse overtime (forecast model) | 600,000 | Modi'in DC |
| **Total** | **6,200,000** | |

## Slide 4 — Other systems

- Kotev Assist for all office staff (450 seats).
- Ayin Drive driver-safety cameras: pilot in the South.
- Nezek Vision damage assessment: POC complete, scaling in Q3.
- Quote assistant for sales.

## Slide 5 — Next

- Europe: driver score and cameras in Q3.
- Docs: auto-submit for low-risk declarations in Q3.
- Assist: documents and invoices in the portal (April).
"""

BUDGET = """
# 2027 budget — AI programme and AI savings (extract)

*Finance, approved by the board on 22 December 2026 as part of the 2027 budget.*

## AI programme cost (cost centre 7700-AI)

| Line | ₪ 2027 |
|---|---|
| Tzir Route (order form 101) | 1,620,000 |
| Tzir Docs (order form 102) | 1,560,000 |
| Tzir Assist (order form 103), subscription and implementation | funded from AI savings |
| Kotev Assist (450 seats) | 513,000 |
| Ayin Drive pilot (6 months) | 100,000 |
| Nezek Vision POC (to February) | 88,000 |
| Quote add-in (6 months) | 57,000 |
| Forecast model cloud | 72,000 |
| AI team (3) | 1,190,000 |
| **Total** | **5,200,000** |

## AI savings recognised in the 2027 operating budget

| Line | ₪ 2027 | Booked against |
|---|---|---|
| Fuel and km | 3,100,000 | Fleet fuel (all regions) |
| Customs productivity | 1,600,000 | Customs brokerage payroll |
| Customer-service deflection | 900,000 | Customer service payroll |
| Warehouse overtime | 600,000 | Modi'in DC overtime |
| **Total** | **6,200,000** | |

Basis: the AI programme's business case (October 2026) and the Tzir value projection.
"""

DOA = """
# Delegation of authority — extract (approved by the board, March 2024)

| Commitment | Approves |
|---|---|
| Operating contract, total value over its term up to ₪1,000,000 | Division head with the CFO |
| Operating contract, total value up to ₪5,000,000 | CEO |
| Operating contract, total value above ₪5,000,000 | Board of directors, after the audit committee if the contract is with a related party |
| Change to an approved contract that raises its total value above a threshold | The approver of the new total |

*Note 4.2:* "Total value" is the value of the contract over its full term, including one-off fees. The delegation does not say how related order forms under one master agreement are counted.
"""

COO_EMAIL = """
# E-mails (extract)

**From:** Moti Azulay (COO)
**To:** Shlomo Peretz
**Date:** Thursday 4 February 2027, 18:40
**Subject:** Docs — productivity

Shlomo, with Docs pre-filling, the target for agents goes from 9 to 12 declarations a day per agent from March. Please put it in the weekly KPI. Moti

---

**From:** Shlomo Peretz (customs brokerage)
**To:** Moti Azulay
**Date:** Thursday 29 April 2027, 16:02
**Subject:** Docs — QA sample April

Moti, attached: our QA re-check of 400 pre-filled declarations from April (`customs/qa-sample-2027-04.csv`). Some of what we found worries me. The agents accept the pre-fill on most declarations: at 12 a day they don't have time to open the invoice for each one. I suggest we go back to 10 and check every LCL invoice. Shlomo

**Reply, Sunday 2 May 2027, 07:55:** Let's discuss after the Q2 numbers. M.
"""

VENDOR_EMAIL = """
# E-mails about the incident (extract)

**From:** Yaniv Sasson (Tzir AI, VP Customer Success)
**To:** Dmitri Volkov; Ofer Lavi
**Cc:** Itai Barkan
**Date:** Saturday 22 May 2027, 10:31
**Subject:** INC-27-0518-01 — contained

Dmitri, Ofer, following yesterday's hotfix (4.2.1) the invoice key now preserves supplier prefixes, and we see no further mismatches. We consider the incident contained. Our analysis shows the root cause was duplicate invoice numbers issued by your customers' suppliers; no personal data was involved (commercial documents only). Full RCA to follow. Best, Yaniv

---

**From:** Ofer Lavi
**To:** Dmitri Volkov
**Date:** Saturday 22 May 2027, 11:05
**Subject:** Re: INC-27-0518-01 — contained

Thanks. Please close it on our side too, I want to report to the board that it's behind us. O.

---

**From:** Itai Barkan
**To:** Ofer Lavi
**Cc:** Board secretary
**Date:** Thursday 27 May 2027, 08:00
**Subject:** Resignation

Ofer, as discussed, I am resigning with effect from today. My handover note is in the AI folder. Itai
"""

DIRECTORY = [
    ["Ofer Lavi", "CEO", "Executive", "HQ", "Board", "active", ""],
    ["Svetlana Morozov", "CFO", "Finance", "HQ", "CEO", "active", ""],
    ["Moti Azulay", "COO", "Operations", "HQ", "CEO", "active", ""],
    ["Adv. Yael Sharabi", "General counsel; privacy protection officer", "Legal", "HQ", "CEO", "active",
     "appointed privacy protection officer January 2026"],
    ["Dmitri Volkov", "Head of IT & information security", "IT", "HQ", "CEO", "active", "incident lead INC-27-0518-01"],
    ["Itai Barkan", "Head of AI & innovation", "AI", "HQ", "CEO", "left 2027-05-27",
     "business owner of 8 AI contracts"],
    ["Lior Gabay", "Data scientist", "AI", "Centre", "Head of AI (vacant)", "active",
     "built and runs the warehouse forecast model; only person with access"],
    ["Noa Peretz", "Analyst", "AI", "HQ", "Head of AI (vacant)", "active", "maintains the AI register"],
    ["Shlomo Peretz", "Head of customs brokerage (licensed customs agent)", "Customs", "North", "COO", "active", ""],
    ["Fadi Khatib", "Operations manager, North", "Operations", "North", "COO", "active", ""],
    ["Gal Rosen", "Operations manager, Centre", "Operations", "Centre", "COO", "active", ""],
    ["Rania Haj-Yahia", "Operations manager, South", "Operations", "South", "COO", "active", ""],
    ["Amir Elbaz", "Deputy operations manager, South", "Operations", "South", "R. Haj-Yahia", "active", ""],
    ["Pieter van Dijk", "Managing director, Vantage Europe B.V.", "Europe", "Europe", "COO", "active", ""],
    ["Hanna Desta", "Head of warehousing", "Warehousing", "Centre", "COO", "active", ""],
    ["Eitan Mor", "Transport safety officer", "Operations", "HQ", "COO", "active", ""],
    ["Ronit Cohen-Elbaz", "VP Customers", "Customers", "HQ", "CEO", "active", ""],
    ["Marina Levitan", "Customer service manager", "Customer Service", "Centre", "R. Cohen-Elbaz", "active", ""],
    ["Anat Gold", "VP HR", "HR", "HQ", "CEO", "active", ""],
    ["Avi Ohana", "Warehouse team lead; works committee chair", "Warehousing", "Centre", "H. Desta", "active", ""],
    ["Tesfaye Worku", "Driver; works committee (drivers)", "Operations", "South", "R. Haj-Yahia", "active", ""],
    ["R. Adler, CPA", "Internal auditor (outsourced)", "Internal audit", "—", "Audit committee", "active", ""],
]


def directory() -> int:
    header = ["name", "role", "department", "region", "reports_to", "status", "note"]
    return write_csv("people/staff-directory-extract.csv", header, DIRECTORY)


ACCOUNTS = [
    ["C1007", "Gefen Medical Distribution Ltd.", "medical consumables", 9400000, "customs, trucking, Ashdod DC",
     "tender for 2028-2030 in September 2027", "R. Cohen-Elbaz", "incident 18 May; 3 shipments held"],
    ["C1022", "Shuk Online Imports Ltd.", "B2C parcel consolidator", 7800000, "customs (LCL), last mile",
     "annual, renews January", "N. Shapiro", ""],
    ["C1189", "Dekel Electronics Trade Ltd.", "electronics", 7100000, "customs, warehousing", "2028", "N. Shapiro", ""],
    ["C1123", "Peleg Auto Spares Ltd.", "auto parts", 6300000, "customs, trucking", "2027-12", "O. Dror", ""],
    ["C1225", "Brosh Building Materials Ltd.", "building materials", 5900000, "trucking", "2028", "O. Dror", ""],
    ["C1031", "Narkis Home Textiles Ltd.", "home textiles", 4800000, "customs, Modi'in DC", "2027-10", "N. Shapiro", ""],
    ["C1237", "Lahav Kitchen Appliances Ltd.", "appliances", 4600000, "customs, trucking", "2028", "O. Dror", ""],
    ["C1164", "Arava Solar Components Ltd.", "solar", 4300000, "customs (FCL)", "2028", "R. Cohen-Elbaz", ""],
    ["C1044", "Ofanim Cycle Parts Ltd.", "bicycle parts", 3900000, "customs, last mile", "2027-11", "N. Shapiro", ""],
    ["C1095", "Tamar Kitchenware Ltd.", "kitchenware", 3700000, "customs, Modi'in DC", "2028", "O. Dror", ""],
    ["C1060", "Kav Yashar Hardware Ltd.", "hardware", 3500000, "customs, trucking", "2028", "O. Dror", ""],
    ["C1141", "Sapir Cosmetics Import Ltd.", "cosmetics", 3300000, "customs", "2027-12", "N. Shapiro", ""],
    ["C1073", "Migdal Office Furnishing Ltd.", "furniture", 3100000, "customs, trucking", "2028", "O. Dror", ""],
    ["C1117", "Nahal Garden Tools Ltd.", "garden", 2900000, "customs", "2028", "N. Shapiro", ""],
    ["C1193", "Neta Lab Supplies Ltd.", "lab supplies", 2800000, "customs (air)", "2027-09", "R. Cohen-Elbaz", ""],
    ["C1136", "Rakia Toys Ltd.", "toys", 2600000, "customs, Ashdod DC", "2028", "N. Shapiro", ""],
    ["C1068", "Zohar Lighting Supply Ltd.", "lighting", 2400000, "customs", "2028", "O. Dror", ""],
    ["C1158", "Yarden Pet Supplies Ltd.", "pet supplies", 2300000, "customs, trucking", "2028", "O. Dror", ""],
    ["C1081", "Shaked Baby Goods Ltd.", "baby products", 2200000, "customs", "2027-12", "N. Shapiro", ""],
    ["C1204", "Galim Marine Equipment Ltd.", "marine", 2100000, "customs", "2028", "O. Dror", ""],
]


def accounts() -> int:
    header = ["customer_code", "name", "sector", "revenue_2026_ils", "services", "contract_or_tender", "account_manager", "note"]
    return write_csv("customers/key-accounts.csv", header, ACCOUNTS)


def build() -> dict:
    n = 0
    for rel, text in (("company/company-profile.md", PROFILE), ("company/org-chart.md", ORG),
                      ("company/board-minutes-2027-06-03-extract.md", MINUTES),
                      ("company/board-deck-ai-programme-2027-03-25.md", DECK),
                      ("company/budget-2027-ai-and-savings.md", BUDGET),
                      ("company/delegation-of-authority-extract.md", DOA),
                      ("correspondence/operations-emails-2027.md", COO_EMAIL),
                      ("correspondence/incident-emails-2027-05.md", VENDOR_EMAIL)):
        n += write_md(rel, text)
    return {"docs-company": n, "directory": directory(), "key-accounts": accounts()}
