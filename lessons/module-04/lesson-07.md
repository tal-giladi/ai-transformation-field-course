---
id: "04.7"
module: 4
minutes: 18
practice_minutes: 90
prerequisites: ["04.5", "04.6"]
objectives:
  - "Write a governance charter in six parts: approved uses, restricted uses, data boundary, risk evidence, monitoring with a named responder, and escalation."
  - "Write terms of reference for a small AI review group with decision rights, quorum and cadence, linked to the organization's existing approval thresholds."
  - "Run an intake register for every AI build and request (owner, where it runs, data touched, overlaps, tier, route, days to decision)."
  - "Report three numbers to the board: what reached production, how long decisions take, and what was declined and why."
volatility: concept
sources:
  - title: "Digital Policy Alert — PPA Directive No. 1/2024 on the responsibilities of the board of directors (12 September 2024)"
    url: https://digitalpolicyalert.org/event/22531-published-privacy-protection-authority-directive-no-12024-outlining-the-responsibilities-of-the-board-of-directors
  - title: "Barnea Jaffa Lande — A practical guide to board responsibility and DPO appointment under Amendment 13 (28 July 2025)"
    url: https://barlaw.co.il/practice_areas/high-tech/cyber/client_updates/a-practical-guide-to-board-responsibility-and-dpo-appointment-under-amendment-13/
  - title: "NIST — AI Risk Management Framework (GOVERN function)"
    url: https://www.nist.gov/itl/ai-risk-management-framework
  - title: "ISO — ISO/IEC 42001:2023 Artificial intelligence management system"
    url: https://www.iso.org/standard/42001
last_verified: "2026-11-02"
---

# 04.7 · Governance that runs

By now Harbor & Pine has a policy, a list, vendor reviews, a tiered inventory, a DPIA, a risk register and a regulatory map. None of them will stay true unless someone owns them together and decides new requests quickly. In this lesson you write the governance charter in six parts, terms of reference for a small review group, an intake register for every AI build and request, a cadence the company can actually keep, and the three numbers the board will see. At the end, governance is a process with a calendar, not a folder.

## The situation

It is Monday 30 November 2026. The pieces from 04.1–04.6 sit in your drive. Yoav wants "an AI committee like the big companies have" and has suggested eight members. Michal wants decisions, not meetings. Ronit wants to know where AI spending is approved. And the clearest evidence of what governance must fix is already in the data room: Olga asked IT for LinguaFlow Business on 2 October (the DPA's cover note), nobody answered, and the request was approved only on 19 November, after the vendor review — 48 days in which the free extension kept reading customer screens on nine machines.

IBM's consulting course gives the six-part anatomy of governance and the "three numbers for the board"; it gives no charter, register or calendar. Here you write them for a 120-person company with one IT person.

## What to do

### Step 1 — Write the charter in six parts

The charter is the one document that says how AI is governed here. Keep it to two pages by pointing to the documents you already have:

| Part | What it says | Harbor & Pine document |
|---|---|---|
| 1. **Approved uses** | What is allowed, for whom, with which tool and data, under which condition; who owns each | Approved / restricted use list (04.2), tiers 1–2 |
| 2. **Restricted uses** | What needs the group's decision, and what nobody may do | Restricted list (04.2), tier 3 |
| 3. **Data boundary** | For each approved tool: what data enters, where it travels, who sees it, training, retention | Data boundaries (04.3) |
| 4. **Risk evidence** | How each High or Medium use is assessed before it starts, and how controls are tested | Tier rule and DPIA (04.4), risk register (04.5), regulatory map (04.6) |
| 5. **Monitoring** | What is watched, the threshold, who watches and who responds | Failure signals in the risk register; module 5's monitoring spec |
| 6. **Escalation** | The trigger, the owner, the response and who has authority to stop a use | This lesson, Step 2 |

Add a short frame around the six parts: purpose (two sentences), scope (all AI under the counting rule, including features inside bought software), who owns the charter, and when it is reviewed.

### Step 2 — Write terms of reference for a small group with real decision rights

Eight members meeting monthly will decide slowly and attend badly. For Harbor & Pine, five people and a secretary:

| Member | Why they are there |
|---|---|
| Michal Peretz, COO — **chair, decides** | Sponsor; owns operations, where most AI use is |
| Ronit Avraham, CFO | Money, approval thresholds, the link to the board and to counsel |
| Avi Mizrahi, IT | Settings, security, vendor technical answers |
| Samir Haddad, Customer Service | The biggest user; owns P-01 |
| Dana Katz, HR | People decisions, training, monitoring of staff |
| You — secretary | Prepare papers, keep the registers, run intake |
| Counsel | On call for items with a legal question; not a member |

**Decision rights** are the heart of the terms of reference. Write who decides what, so most things never need the meeting:

| Decision | Who decides | Time limit |
|---|---|---|
| New Tier 1–2 use with a tool already approved for that data class | You, recorded in the intake register | 10 working days |
| New tool or vendor for Medium uses | You and Avi after the vendor review; reported to the group | 10 working days |
| High-tier uses, restricted uses, lifting a restriction | The group (chair decides if there is no consensus) | Next meeting, or 5 working days by email if urgent |
| Stopping a use that breaches a threshold or the policy | Any member, immediately; the group confirms at the next meeting | Immediately |
| Spending | Finance thresholds: up to ₪50,000 department head and CFO; ₪50,000–150,000 the CEO; above ₪150,000 over three years the board (`company/finance-summary.md`) | As finance sets |

The stop right matters most. IBM calls it authority to halt: a control is only real if someone may use it without asking first.

**Escalation (part 6):** trigger (a failure signal crosses its threshold, an incident, a vendor change notice, a complaint about AI) → owner of the use acts and tells you the same day → you inform the chair → the chair decides continue, restrict or stop → recorded in the register. Privacy incidents go to counsel the same day; whether and when to notify the regulator is counsel's call (module 7 builds the incident runbook).

### Step 3 — Run an intake register for every AI build and request

Most governance failures at Harbor & Pine were requests nobody recorded: CopyGenie on a personal card since February, Olga's email of 2 October, PeopleWise switching itself on in March. One register catches all of them. Every row, whatever its source (a form, an email, an expense claim, a vendor release note):

| Field | Why |
|---|---|
| ID, date received, requester | Starts the clock |
| What, in one line; business owner | Who will answer for it |
| Where it runs (tool, vendor, plan) | Links to the approved list and vendor reviews |
| Data touched (class) | Drives the tier |
| **Overlaps** | Other requests or tools doing the same job: merge instead of buying twice |
| Tier (04.4 rule) and route | Fast-track, group, or portfolio gate |
| Status, decision, date decided, **days to decision** | The board's second number |
| Reason if declined or "not yet" | The board's third number; and the requester's answer |

The overlap column is cheap and saves money. LinguaFlow Business, Deskly AI Assist's *Translate* feature and Gemini can all translate a customer message; ChatNest and the drafts pilot both answer customers. Decide them together.

Items that turn out not to be AI under the counting rule (the WhatsApp routing, the daily date-fix job) are still recorded — with "not AI, normal IT change process" as the route — so nobody re-submits them.

### Step 4 — Use the portfolio gate only when a build asks for money or to scale

Governance and investment are different questions. The review group asks "may we, safely?"; the portfolio gate asks "should we spend on it, now?" (module 3: Ronit's template, the 12% hurdle rate, the roadmap's gates). Send an item through the portfolio gate only when it asks for money above the department threshold or wants to move from pilot to scale. Otherwise every small tool waits for a business case, and people go back to their phones.

### Step 5 — Set a cadence the company can keep

| Rhythm | What | Who | Time |
|---|---|---|---|
| Weekly | Intake triage: new rows, fast-track decisions, overdue items | You and Avi | 15 minutes |
| Monthly | Review group: High and restricted items, risk-register changes (tested ones only), incidents, vendor changes, the three numbers | The group | 45 minutes, papers 3 working days before |
| Quarterly | Re-run the census host list on the proxy log and the tiering script; check vendor sub-processor notices; refresh the inventory | You, Avi | Half a day |
| Every six months | Review the AUP and the approved list | Group | One meeting item |
| Yearly, and at each board meeting | Report to the board | Michal, Ronit | One page |

### Step 6 — Report three numbers to the board

Boards hear "we have AI governance" and cannot tell whether it works. Give them three numbers every time, with one line each:

1. **Reached production:** how many AI uses moved from request or pilot into approved, running use this period (and how many are in pilot).
2. **Decision time:** median days from intake to decision, with the slowest item named.
3. **Declined, and why:** how many requests were declined or sent back, with the main reasons.

These three show whether governance helps the company use AI (number 1), whether it is fast enough that people use the route (number 2), and whether it can say no (number 3). A governance process that declines nothing is not reviewing; one that approves nothing will be bypassed.

### Step 7 — Link it to the existing risk process and to the board

Harbor & Pine has no enterprise risk register; the nearest things are Ronit's approval thresholds and her reports to the five-member board. Link to those instead of building a parallel AI risk process: red risks from the AI register go into Ronit's board report; spending follows her thresholds; the AI policy pack is presented to the board once, on 28 January 2027.

Israel first: the Privacy Protection Authority's Directive 1/2024 (September 2024) addresses the board's oversight of privacy and data-security compliance in companies where processing personal data is core to the business or carries high privacy risk (Digital Policy Alert). Barnea Jaffa Lande's summary of the regulator's expectations lists policies, defined responsible officers, regular updates and discussion of material issues such as risk surveys and incidents, and notes that appointing a DPO does not relieve the board of oversight. Whether the directive applies to Harbor & Pine is one of counsel's questions (04.6); the charter's board line costs one agenda item a year and answers the directive if it does.

## Watch out

- **The big committee.** Eight members, monthly, no decision rights: requests wait, people route around it. Small group, rights written down, most decisions outside the meeting.
- **No time limit on intake.** Olga's 48 days are the failure mode. Write the limit and report it.
- **Every request through the business case.** A ₪600-a-year tool does not need Ronit's template. Use the portfolio gate for money and scale only.
- **Approving tools one by one.** Without the overlap column the company buys three translators.
- **A charter that repeats the other documents.** Point to them; the charter is the map, not the territory.
- **Reporting activity instead of outcomes.** "We held four meetings and reviewed twelve items" says nothing. The three numbers do.
- **Nobody may stop anything.** If stopping a use needs a meeting, the control is on paper.

## Your turn

### Inputs

- Everything from 04.1–04.6.
- Data room (module download): `company/finance-summary.md` (approval thresholds), `company/org-chart.md`, `company/company-profile.md` (the board), `vendors/linguaflow-translation-dpa.md` (the request date), `it/expenses.csv`, `it/peoplewise-release-notes-2026-03.md` ([INDEX](../../labs/common/harbor-and-pine/INDEX.md)).
- Templates: [governance charter](../../templates/governance-charter.md), [AI intake register](../../templates/ai-intake-register.md); spreadsheet `labs/module-04/ai-intake-register.csv` ([lab README](../../labs/module-04/README.md)).

### Steps

1. Write the charter: frame plus the six parts, each pointing to its document. Two pages at most.
2. Write the terms of reference: members, decision rights with time limits, the stop right, quorum, cadence.
3. Fill the intake register with at least eight Harbor & Pine items from the census, inventory, vendor documents and interviews, including two that are not AI. Fill the overlap column.
4. Work out the days to decision for every decided item, and the median.
5. Draft the board page with the three numbers as they would stand on 20 January 2027 (label forecasts as forecasts).
6. Write the escalation path for one real trigger: Deskly notifies a new AI sub-processor.

### Time

90 minutes.

### Done when

- [ ] The charter has all six parts and points to the documents instead of repeating them.
- [ ] Decision rights say who decides each kind of item, within what time; any member can stop a use.
- [ ] Spending follows the existing finance thresholds; there is no parallel approval chain.
- [ ] The intake register has at least eight rows with owner, where it runs, data class, overlaps, tier, route and days to decision.
- [ ] Non-AI items are recorded with their route.
- [ ] The board page shows the three numbers, each with one line of explanation.
- [ ] The escalation path names the trigger, owner, response and who can stop.

<details><summary>Reference answer</summary>

**Terms of reference (excerpt).** *AI review group.* Chair: Michal Peretz (decides when there is no consensus). Members: Ronit Avraham, Avi Mizrahi, Samir Haddad, Dana Katz. Secretary: AI lead. Quorum: chair plus two. Meets the second Thursday monthly, 45 minutes, first meeting 10 December 2026. Decision rights as in Step 2. Any member may stop an AI use immediately on a threshold breach or policy breach; the group confirms or lifts the stop at the next meeting.

**Intake register (as of 30 November 2026).**

| ID | Received | Requester | What | Runs in | Data | Overlaps | Tier | Route | Decision | Decided | Days |
|---|---|---|---|---|---|---|---|---|---|---|---|
| IN-01 | 2 Oct | Olga (Samir) | Translation of messages and replies | LinguaFlow Business | D | IN-02 Translate, Gemini | Medium | New vendor → you + Avi | Approved with conditions | 19 Nov | 48 |
| IN-02 | 14 Oct | Samir | Helpdesk AI add-on for the drafts pilot | Deskly AI Assist | D | IN-01, IN-03 | High | Group + DPIA | Pilot with conditions (proposed) | 10 Dec (planned) | — |
| IN-03 | 6 Oct | Yoav | Customer chatbot | ChatNest | D | IN-02 (both answer customers) | High | Group + portfolio gate (₪85,000 implementation + US$1,450 a month ≈ ₪278,000 over three years at ₪3.70/US$ → board) | Not yet: claims and proof of concept first (04.8) | 10 Dec (planned) | — |
| IN-04 | 18 Nov (from expenses, paid since Feb) | Noa | Product copy | CopyGenie → company account | P | Gemini, StoreHub AI | Medium | Fast-track | Approved for P and I | 25 Nov | 7 |
| IN-05 | 16 Nov (from release notes of March) | Dana | Candidate ranking | PeopleWise | S | — | High | Group + counsel | Off pending counsel | 17 Nov | 1 |
| IN-06 | 18 Nov (from proxy and expenses) | Ronit's team | Summarise finance documents | Claude (personal) → Gemini | B | Gemini | Medium | Fast-track | Declined for the personal account; moved to Gemini | 24 Nov | 6 |
| IN-07 | 22 Nov | Yaniv | AI assistant on B2B leads | Monday.com | D | Gemini | Medium | Fast-track after settings check | Open (Avi checking) | — | — |
| IN-08 | 17 Nov | Samir | WhatsApp into the helpdesk | Deskly WhatsApp channel | D | — | Not AI | Normal IT change | Routed | 17 Nov | 0 |
| IN-09 | 16 Nov | Tamar, Noa | Daily delivery-date update emails | Script + StoreHub | D | WISMO part of IN-03 | Not AI | Normal project (module 3) | Routed | 16 Nov | 0 |

Days are calendar days from receipt to decision. Median of the AI items decided after the process started (IN-04, IN-05, IN-06): 6 days; the one before it (IN-01): 48 days.

**Board page, 28 January 2027 (forecast, to update on 20 January).** (1) *Reached production:* 3 uses approved and running (translation with LinguaFlow Business, drafting and summaries with Gemini, product copy with CopyGenie on a company account); 1 approved to start as a shadow pilot on 1 February (reply drafts). (2) *Decision time:* median 6 days since the process started on 22 November; the slowest item was the translation request of 2 October (48 days, before the process existed). (3) *Declined or not yet: 2* — the customer chatbot (no evidence on our own data; proof of concept proposed) and a personal AI account in Finance (moved to an approved tool). Also: the HR ranking feature is switched off pending counsel's review.

**Escalation — Deskly adds an AI sub-processor.** Trigger: Deskly's notification email (subscription set up by Avi). Owner: Avi reads it the same day and tells you. You check the new processor's location and role against the data boundary and the DPIA (R-12). If it adds a country or a human-review role: you inform Michal the same day; the 15-day objection window (§6.1) is the deadline; Michal decides continue, object or pause the pilot; counsel is asked about the transfer route; the decision is recorded in the intake register and the DPIA is updated.

</details>

## References

- Digital Policy Alert, [PPA Directive No. 1/2024](https://digitalpolicyalert.org/event/22531-published-privacy-protection-authority-directive-no-12024-outlining-the-responsibilities-of-the-board-of-directors) (12 September 2024); Barnea Jaffa Lande, [A practical guide to board responsibility and DPO appointment under Amendment 13](https://barlaw.co.il/practice_areas/high-tech/cyber/client_updates/a-practical-guide-to-board-responsibility-and-dpo-appointment-under-amendment-13/) (28 July 2025). Whether the directive applies to a company is counsel's call.
- NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — the GOVERN function; ISO, [ISO/IEC 42001](https://www.iso.org/standard/42001) — management-system structure if a client later wants certification.
- Templates: [governance charter](../../templates/governance-charter.md), [AI intake register](../../templates/ai-intake-register.md).
- Earlier: [03.7 · The ROI model that survives finance](../module-03/lesson-07.md) and [03.8 · The roadmap](../module-03/lesson-08.md) (the portfolio gate). Previous: [04.6 · Which law applies to you](lesson-06.md). Next: [04.8 · Vendor and claim due diligence](lesson-08.md). Later: module 7 builds the incident runbook (07.5) and the operating rhythm (07.6).
