"""company/*.md: profile, org chart, board minute, programme budget, CFO's budget review."""
from gen_common import write_md

PROFILE = """
# Crescent Bank Ltd. (בנק הסהר בע"מ) — company profile, January 2027

Prepared by the COO office for new managers. All figures rounded.

| | |
|---|---|
| Founded | 1972, Haifa, as a regional bank for the north; head office in Ramat Gan since 2004 |
| Licence and supervision | Banking corporation, supervised by the Bank of Israel's Banking Supervision Department; shares listed on the Tel Aviv Stock Exchange |
| Size | Balance sheet about ₪96bn; about 1.1 million customers; 58 branches (north and centre); about 4,000 employees |
| Business units | 14: Retail Banking, Mortgages, Cards & Payments, SME Banking, Corporate Banking, Private Banking, Treasury & Markets, Credit Risk, Compliance & AML, Operations, Contact Centre, Digital Channels, HR, Finance |
| Customers' languages | Hebrew; Arabic (about a fifth of retail customers in the northern branches); Russian; English; Amharic in some branches |
| Core systems | "Atid" core banking (mainframe); "Kesher 360" CRM (SaaS); "Mizrah" data warehouse; Tzofen Assist (enterprise AI assistant, since 2026) |
| Workforce | Collective agreements with the employees' union for most branch, contact-centre and back-office staff; a works committee at head office |
| 2026 | Net profit about ₪1.1bn (unaudited); cost-to-income about 52%; the strategic plan 2026–2028 names "AI at scale" as one of five pillars |

## AI at Crescent

- AI policy v1 approved by management in June 2025 (`../governance/ai-policy-v1-2025.md`).
- The Model Committee (chaired by the CRO) approves every model before use, including AI.
- In November 2026 the board approved an AI Centre of Excellence (CoE) under the COO and a central AI
  programme for 2027 (`board-minutes-2026-11-24-extract.md`, `ai-programme-budget-2027.md`).
- The COO office keeps the AI pilot register (`../ai/pilot-register-2026-12.csv`), compiled from the
  units' submissions in December 2026.
"""

ORG = """
# Crescent Bank — organisation chart (extract), 1 January 2027

```
Board of Directors
├── Board Risk Management Committee        ├── Board Audit Committee
│                                          └── Chief Internal Auditor ........ Tsega Alemu
CEO ...................................... Avner Golan
├── COO .................................. Dalit Ben-Ami
│   ├── Operations ....................... Shlomi Azoulay
│   ├── Contact Centre ................... Revital Cohen
│   ├── Digital Channels ................. Tom Erez
│   └── AI Centre of Excellence (new) .... [Head of AI CoE] (from 3 Jan 2027; 15 positions open)
├── CFO .................................. Moshe Dahan
│   └── Finance (Chief Controller) ....... Eli Rosen
├── CRO .................................. Dr. Irina Kogan
│   ├── Credit Risk ...................... Dr. Hila Nachum
│   └── Model Risk Management ............ Yonatan Bar (2 validators)
├── CIO .................................. Nir Ashkenazi
│   └── Data & Analytics (Mizrah) ........ 8 people
├── Chief Compliance Officer ............. Adv. Lina Nassar
│   ├── Compliance & AML ................. Samer Khoury (AML operations)
│   └── Regulatory liaison ............... Eitan Bar-Lev
├── General Counsel ...................... Adv. Gideon Shalev (DPO: Ruth Ben-David)
├── HR ................................... Anat Weiss
└── Business units
    ├── Retail Banking ................... Hagit Mor (58 branches)
    ├── Mortgages ........................ Rachel Azaria
    ├── Cards & Payments ................. Karim Haddad
    ├── SME Banking ...................... Yossi Ben-Haim
    ├── Corporate Banking ................ Daniel Friedman
    ├── Private Banking .................. Michael Stern
    └── Treasury & Markets ............... Boris Lerner
```

Committees: Management Committee (CEO, weekly); Model Committee (CRO, chair; MRM head, CIO, CCO,
the model's unit head; per the AI policy, monthly); IT Steering (CIO); Procurement Committee (CFO).
"""

BOARD = """
# Board of Directors — minutes of the meeting of 24 November 2026 (extract)

Item 4: AI at Crescent (presented by the CEO, with the COO)

**Presentation.** The CEO said: "We have 40 pilots and nothing in production. Fourteen units are each
doing their own thing; the pilots are good, but none of them reaches the customer or the P&L." The
COO presented the proposed AI Centre of Excellence, prepared with an external consultancy in
October: a central team of 16 (product, data science, engineering, change) that "takes the pilots
from the units and industrialises them", a central AI programme budget, and quarterly reporting.

**Discussion.**
- A director asked how many pilots would be in production in a year. The CEO: "At least ten by
  December 2027."
- A director asked whether the supervisor's expectations on AI governance are met. The CRO said that
  all AI goes through the Model Committee and full validation before use, "as for any model".
- The chair asked that the CoE report to the Board Risk Management Committee every quarter, starting
  in Q2 2027, and that the first report include the inventory of AI in use.

**Resolutions.**
1. To establish an AI Centre of Excellence under the COO, with 16 positions.
2. To approve a central AI programme budget of ₪11.0M for 2027, subject to the 15% savings review of
   discretionary programmes in Q1 2027 (budget revision at the board on 30 March 2027).
3. Quarterly reporting to the Board Risk Management Committee from Q2 2027.
"""

BUDGET = """
# Central AI programme — budget 2027 (as approved 24 November 2026)

Owner: COO. Cost centre 6100-AI. Unit-funded AI lines (pilot vendors, contractors, licences) stay in
the units' budgets; their 2027 amounts are in the pilot register (`budget_2027_ils`).

| Line | ₪ | Basis |
|---|---:|---|
| AI CoE central team (16 FTE, of which 1 hired) | 4,800,000 | Consultancy design, October 2026: product 3, data science 5, engineering 5, change 2, head 1 |
| Model validation capacity for AI (3 review slots a quarter) | 1,800,000 | MRM work plan 2027: ₪150,000 a slot a quarter |
| Production fund (integration, hosting, security testing for go-lives) | 2,600,000 | "about ₪260,000 per pilot taken to production, 10 pilots" |
| AI tools, training and contingency | 1,800,000 | |
| **Total** | **11,000,000** | |

Assumptions written in the consultancy design: "The central team builds production versions of the
units' pilots; units hand over their pilots to the CoE. Every go-live follows the Model Committee
process."
"""

CFO = """
# Budget review 2027 — discretionary programmes, 15% savings (extract)

From: Moshe Dahan, CFO. To: Management Committee. Tuesday 12 January 2027.

The board approved the 2027 budget subject to 15% savings on discretionary programmes, to be
presented at the board on 30 March. For AI the base is all AI spend in 2027:

| | ₪ |
|---|---:|
| Central AI programme (cost centre 6100-AI) | 11,000,000 |
| AI lines in the units' budgets (sum of `budget_2027_ils` in the COO office's pilot register, 43 lines) | 9,130,000 |
| **AI spend 2027** | **20,130,000** |
| 15% | 3,020,000 |

**Proposed savings (AI):**

1. **Cancel the bank-wide assistant rollout (Operations, Tzofen Assist): ₪2,400,000.** The biggest
   single line. 1,600 seats were activated on 1 December; December usage was 16% of seats (average
   weekly active users 251 of 1,600, Tzofen admin report). Eighteen months after the first pilots,
   nothing is in production; a general assistant is a "nice to have".
2. Reduce the central production fund: ₪620,000.

Total ₪3,020,000. Comments to me by 31 January; the COO to confirm the AI items by 15 March.
"""


def build() -> dict:
    write_md("company/company-profile.md", PROFILE)
    write_md("company/org-chart.md", ORG)
    write_md("company/board-minutes-2026-11-24-extract.md", BOARD)
    write_md("company/ai-programme-budget-2027.md", BUDGET)
    write_md("company/cfo-budget-review-2027-01-12.md", CFO)
    return {"company_docs": 5}
