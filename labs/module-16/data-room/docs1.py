"""Company documents: profile, org chart, board minutes, budget."""
from __future__ import annotations

from common import ROOM, fill, ils, write_md
from people import STAFF

PROFILE = """
# Open Hands — organization profile

*From the welcome pack Ronit sends to new board members and volunteers (updated September 2026).*

**Open Hands** (עמותת ידיים פתוחות (ע"ר)) is a registered amuta founded in 2008 by three parents in Kiryat
Ata. We walk beside families raising children and young people (0–21) with disabilities, so that no family
has to fight the system alone.

## What we do

| Programme | What it is | Who runs it |
|---|---|---|
| Family coordination | A social worker (family coordinator) accompanies each family: rights and benefits (National Insurance disabled-child benefit, appeals), placement committees, welfare services, therapies, transport | Six coordinators led by Hana Golan |
| Rights hotline | Phone and WhatsApp line for any family in the north, Hebrew and Arabic | Fatma Zoabi, Eli Dahan |
| Respite weekends | Weekends for children with trained volunteers, so parents can rest | Amir Saleh, about 40 volunteers |
| Parent groups | Groups in Hebrew, Arabic, Russian and Amharic | Nurit Sasson and two facilitators |
| Siblings' programme | Groups and outings for brothers and sisters | Hadas Mor |

## In numbers (12 November 2026)

- **{{n_families}} active families**: Hebrew-speaking {{he}}, Arabic-speaking {{ar}}, Russian-speaking {{ru}}, Amharic-speaking {{am}}, English-speaking {{en}}.
- Families from Haifa, the Krayot, Acre, Nesher, Shefa-'Amr, Tamra and Kiryat Hadas (where the municipal welfare department refers families to us under a service agreement).
- **{{n_staff}} staff** ({{fte}} full-time equivalents), two national-service volunteers among them; **{{n_vols}} volunteers** on the list, {{n_vols_active}} active this year.
- **{{n_donors}} donors** in our donor sheet; 14 institutional funders.
- 2026 budget: {{budget}}.

## How we work

- Offices: Kiryat Ata (main office) and a room in Shefa-'Amr shared with a community centre.
- Systems: Google Workspace for Nonprofits (email, Drive, Calendar, Meet) since 2019; Microsoft Office on a few computers; WhatsApp for everything that moves fast.
- Registered amuta; certificate of proper management for 2026 (received June 2026); approved public institution for donations under Section 46 of the Income Tax Ordinance.
- No IT department. Yossi Mizrahi, our office and operations manager, looks after computers, accounts and Wi-Fi, usually on Tuesdays.
"""

ORG = """
# Open Hands — who works here

*HR list, October 2026 (Galina). FTE = share of a full-time position.*

| Team | Name | Role | FTE | Languages |
|---|---|---|---|---|
{{rows}}

**Board** (volunteers): Avi Shalev (chair), Vladimir (Vova) Gorelik (treasurer), five members including two parents of children in our programmes. Audit committee: two members. The board meets monthly on Zoom, usually on a Tuesday or Wednesday evening.

**Volunteers**: coordinated by Liat Ohana (programmes) and Amir Saleh (respite). Respite volunteers are organised by weekend in WhatsApp groups (see the volunteer handbook).
"""

MINUTES = """
# Board of directors — minutes, 27 October 2026 (Zoom, 19:30–21:10)

*Draft circulated by the secretary on 29 October. Present: Avi Shalev (chair), Vova Gorelik (treasurer), four members. Staff: Dr. Ronit Azoulay (ED), Noa Ben-Ami (head of development, item 3).*

## 1. ED report

Ronit: {{n_families}} active families. Q3 report to the Adler-Haddad Family Foundation submitted on 24 October (due 15 October; the foundation agreed the delay by email). The foundation's renewal proposal is due 31 January 2027. Ministry of Welfare support for 2026 approved; certificate of proper management for 2026 received in June.

## 2. Finance (treasurer)

Vova: income to September on budget. Questions:
- A charge of {{msft}} on the office card on 14 October, "MSFT M365 BUS PREM NP". Yossi says Microsoft "changed something with the grant". *Action: Yossi to check and report to the treasurer.*
- Software is now about ₪9,000 a year "and growing; every month there is a new subscription". He asks that no new recurring charge start without his approval.

## 3. AI (chair)

Avi reported on the "AI for Good" conference he attended in Tel Aviv: "Every nonprofit there is using AI already. We are behind. Our social workers drown in paperwork and Noa writes reports all day."

Noa: "Half my week goes on reports. Every funder wants a different template. AI could write the first draft of all of them."

Ronit: supportive, but "we have no budget for this and no IT person, and I will not put our families' information at risk."

Vova: "No budget means no budget. If someone can show us how to do it with the free tools, fine."

**Decided:** Ronit to find pro bono help to show Open Hands how to use AI with the tools it already has, and to report at the December board (9 December). No budget allocated.

## 4. Hanukkah party

Monday 7 December, Kiryat Ata community centre. Michael organising; the Tzur-Lev employee fund covers food and gifts.
"""

BUDGET = """
# Budget 2026 — summary for the board

*Galina Petrova, bookkeeper, approved by the board in December 2025; actuals to 31 October added in November 2026.*

## Income

| Source | Budget 2026 | Share | Notes |
|---|---|---|---|
| Foundations and funds (12) | {{found}} | {{found_pct}} | Largest: Adler-Haddad Family Foundation ₪870,000 (family coordination, children under 13) |
| Ministry of Welfare (support) | ₪920,000 | {{gov_pct}} | Requires the certificate of proper management |
| Kiryat Hadas municipality (service agreement) | ₪620,000 | {{muni_pct}} | Coordination for families the municipal welfare department refers |
| Individual donors (Israel and American Friends) | ₪1,250,000 | {{don_pct}} | {{don_actual}} received to 31 October 2026 (2025 full year: {{don_2025}}) |
| Events, membership, other | {{other}} | {{other_pct}} | |
| **Total** | **₪6,120,000** | 100% | |

## Expenditure (main lines)

| Line | Budget 2026 |
|---|---|
| Salaries and social benefits | ₪4,710,000 |
| Respite weekends (venues, food, transport) | ₪520,000 |
| Rent, Kiryat Ata and Shefa-'Amr | ₪228,000 |
| Transport and travel | ₪164,000 |
| IT (laptops ₪22,000; software ₪9,800; support ₪6,200) | ₪38,000 |
| Audit, legal, insurance | ₪96,000 |
| Fundraising and events | ₪212,000 |
| Other | ₪152,000 |
| **Total** | **₪6,120,000** |

There is no line for AI. Any expense above ₪3,000 a year outside the approved budget needs the treasurer; any new recurring charge needs the treasurer (board decision of 27 October 2026).
"""


def write(f: dict) -> None:
    total = 6_120_000
    found = f["foundation_income"]
    other = total - found - 920_000 - 620_000 - 1_250_000

    def p(x):
        return f"{100 * x / total:.0f}%"

    lang = f["lang"]
    write_md(ROOM / "company" / "org-profile.md", fill(PROFILE, dict(
        n_families=f["n_families"], he=lang.get("he", 0), ar=lang.get("ar", 0), ru=lang.get("ru", 0),
        am=lang.get("am", 0), en=lang.get("en", 0), n_staff=f["n_staff"], fte=f["fte"], n_vols=f["n_vols"],
        n_vols_active=f["n_vols_active"], n_donors=f"{f['n_donors']:,}", budget=ils(total))))
    rows = "\n".join(f"| {s[3]} | {s[1]} | {s[2]} | {s[4]} | {s[5]} |" for s in sorted(STAFF, key=lambda s: s[3]))
    write_md(ROOM / "company" / "org-chart.md", fill(ORG, dict(rows=rows)))
    write_md(ROOM / "company" / "board-minutes-2026-10.md", fill(MINUTES, dict(
        n_families=f["n_families"], msft=ils(f["msft_ils"]))))
    write_md(ROOM / "company" / "budget-2026.md", fill(BUDGET, dict(
        found=ils(found), found_pct=p(found), gov_pct=p(920_000), muni_pct=p(620_000), don_pct=p(1_250_000),
        don_actual=ils(f["donations_2026"]), don_2025=ils(f["donations_2025"]), other=ils(other),
        other_pct=p(other))))
