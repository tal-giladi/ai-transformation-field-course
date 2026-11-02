---
id: "01.5"
module: 1
minutes: 18
practice_minutes: 75
prerequisites: ["01.4"]
objectives:
  - "Inventory a data room in under an hour: every file's source, period, size, owner and how it was produced."
  - "Sort every number in the narrative documents into verified, contradicted, claim to test or unverifiable, naming who said it, where and when."
  - "List what is missing and write access requests that ask for the minimum data, for a stated purpose, with an approver and a deletion date."
volatility: implementation
sources:
  - title: "Pearl Cohen — Israel: New Draft Guidelines on the Application of Privacy Law to AI (PPA draft, April 2025)"
    url: https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/
  - title: "IAPP — The new Israeli data security regulations: A tutorial"
    url: https://iapp.org/news/a/the-new-israeli-data-security-regulations-a-tutorial
  - title: "Barnea Jaffa Lande — Israel: Law and Practice (Chambers Global Practice Guide, TMT, 2020): outsourcing, Regulation 15 and transfers abroad"
    url: https://www.barlaw.co.il/wp-content/uploads/2020/02/011_ISRAEL-LP.pdf
last_verified: "2026-11-02"
---

# 01.5 · Access and the first-day data-room read

On your second day someone gives you a folder: exports, reports, a profile, a few contracts, a policy from 2021. Most people either drown in it or skim it and start believing the numbers in the slides. In this lesson you read a data room the way an auditor would on day one: what is here and where it came from, what is missing, and which numbers are verified and which are only claims. Then you ask for what is missing with an access request that a data owner can sign the same day.

## The situation

It is 3 November. Avi, the IT manager, has given you read access to the Harbor & Pine data room: 19 CSV exports and 17 documents (`labs/common/harbor-and-pine/`, with an `INDEX.md`). You have a 30-day question to answer — what is really happening in the work, the data and the AI already in use — and you need to know, before anything else, which of these files can carry that answer.

IBM's governance course asks for an "actor–source–date check" on every claim. Here you apply it to a whole data room in an afternoon, and you write down the result so that nobody, including you, mistakes a slide for a measurement.

> [!WARNING]
> In a real engagement the data room contains real people's personal data. Do not copy it to a
> personal device, and do not paste or upload it into an AI tool the organization has not approved
> for that data — including for your own analysis. The Harbor & Pine data room is synthetic, so you
> may use any tool on it here.

## What to do

### Step 1 — Inventory every file (30 minutes)

For each file write one line: what it is, the system or person that produced it, the period it covers, its size, and who owns it. Don't analyse yet.

**Track A.** Open each CSV (Excel: *Data → From Text/CSV*, UTF-8) and note rows, columns and the first and last date. Open each document and note its author and date from the first lines.

**Track B (Python).** With 19 exports, and the same job at the start of every engagement in this course, a script pays for itself on the first run. From `labs/module-01/`:

```bash
python first_read.py --csv first-read-files.csv
```

It prints each CSV's rows, columns, date range and share of blank cells, lists the documents, and flags hand-kept files with Hebrew headers. Excerpt for Harbor & Pine:

| File | Rows | First date | Last date | Blank cells |
|---|---|---|---|---|
| `support/tickets.csv` | 2,529 | 2026-05-01 | 2026-10-31 | 15.7% |
| `support/phone-log.csv` | 3,194 | 2026-05-01 | 2026-10-31 | 11.3% |
| `orders/orders.csv` | 3,134 | 2026-03-15 | 2026-12-12 | 1.5% |
| `orders/shipments.csv` | 112 | 2026-02-27 | 2026-12-17 | 8.4% |
| `orders/storehub-delivery-settings.csv` | 5 | 2023-02-14 | 2023-02-14 | 0% |
| `it/proxy-log.csv` | 2,918 | 2026-10-11 | 2026-10-22 | 0% |
| `orders/logistics-eta-tracking.csv` | 105 | (dates as text) | | 23.1% |

Already the dates tell stories: the orders file reaches into December (promised dates in the future), the proxy log covers only two weeks, and the web-store settings were last changed in February 2023.

### Step 2 — Mark each file's provenance

How a file was produced tells you how far to trust it. Five kinds:

| Provenance | Harbor & Pine examples | Trust |
|---|---|---|
| System export | tickets, phone log, orders, proxy log, extensions, expenses | High for what the system records; check definitions (what does "resolved" mean?) |
| Hand-kept file | logistics ETA sheet, damage-claims log, the 2023 catalogue copy on the shared drive | Often the real working truth — and often incomplete, duplicated or stale |
| Narrative document | KPI report, board minutes, company profile, handbook | Claims, until a system export confirms them |
| Vendor document | ChatNest deck, Deskly terms, LinguaFlow DPA, PeopleWise release notes | Interested party; read for what it commits to, not what it promises |
| Written for you | finance summary, IT's data-retention note | Useful and recent; still someone's view ("best of my knowledge") |

### Step 3 — List what is missing

Compare the room with the work. What would you expect for a company that sells online, imports by container and answers customers in four languages? The INDEX itself admits five gaps: the web store's own order export, call recordings, the delivery company's records, the contracts with Deskly and Gal-Ship, and anything from the showrooms. Add what you notice:

- Deskly's configuration: macros, automation rules, how "resolved" is set.
- StoreHub's checkout logic beyond five lead-time settings: how the promised date is calculated and shown.
- The board's business-case template (Ronit has it; the minority investor asked for it).
- Any record of who the company's privacy contact is, and whether its databases were reviewed after the 2025 amendment (IT's note lists both as open).

Call recordings are a special case: IT's note says CloudVoice deletes them after 30 days. Ask anyway, but write "may not exist for the period" next to it. Some gaps are findings in themselves.

### Step 4 — Sort the numbers: verified, contradicted, claim to test, unverifiable

Go through every narrative document and pull out each number or factual statement. For each, write **who** said it, **where**, **when**, and its **status**, with the file that checks it. Use the [data-room first read template](../../templates/data-room-first-read.md) (a spreadsheet version is `labs/module-01/data-room-first-read.csv` in the module download).

Four statuses, and only four:

- **Verified** — a system export gives the same number by the same definition.
- **Contradicted** — an export or another primary document gives a different number.
- **Claim to test** — plausible, but its definition or source needs checking; say in which lesson.
- **Unverifiable** — no data could confirm it; say who has an interest in it.

Worked examples:

| Claim | Who, where, when | Status | Checked against |
|---|---|---|---|
| "Tickets handled (email + web form): 1,360" in Q3 | Samir with Finance BI, KPI report, 6 Oct 2026 | Verified | `tickets.csv`: Jul 425 + Aug 448 + Sep 487 = 1,360 |
| "Calls offered 1,368; answered 84%" | KPI report | Verified | `phone-log.csv`, Q3 in-hours: 1,144 answered + 224 abandoned = 1,368; 83.6% |
| "Average first response time 2.0 hours" | KPI report | Claim to test | Footnote 1: business hours only, email only, tickets received on business days, average — test against `tickets.csv` in 02.4 |
| "Resolution rate 100%" | KPI report | Claim to test | Footnote 2: tickets in status "resolved" ÷ received; a status, not an outcome — test in 02.4 |
| "Customer service costs us ₪3.4 million a year" | CEO, board minutes, 24 Sep 2026 | Verified | `finance-summary.md`: FY2025 fully loaded ₪3,400,000 |
| "Cut support cost by 40%" | CEO, board minutes | Unverifiable (no basis given) | A director asked "target or forecast?" and got no answer |
| "ChatNest showed a demo built on our own catalogue in two days" | CEO, board minutes; vendor deck slide 4 | Claim to test | Which catalogue? Two exist: `products.csv` and a 2023 shared-drive copy — test in 04.8 |
| "Every serious retailer we met already runs an AI agent" | CEO, board minutes | Unverifiable | Source: vendors at a conference — interested parties |
| "About 250 SKUs (some discontinued)" | Company profile, Aug 2026 | Verified | `products.csv`: 245 SKUs, 29 discontinued |
| "Containers: roughly 2 a week" | Company profile | Contradicted | `shipments.csv`: 112 containers departing 27 Feb – 19 Nov 2026, about 3 a week (the profile's own schedule — Vietnam and China weekly, Turkey and Italy every two weeks — also makes 3) |
| PeopleWise: no AI features, AI enabled "No" | IT, `saas-list.csv` | Contradicted | `peoplewise-release-notes-2026-03.md`: AI Candidate Match "Enabled by default" since March 2026 — lesson 01.7 |
| "Every claim is reviewed by QA within 48 hours" | Customer-service handbook §8 | Claim to test | The org chart lists no role called QA — test in 02.3 |

Two rules while you do it. A number is not verified because another *narrative* document repeats it — the CEO's ₪3.4M is verified by the CFO's summary only because that summary is built from the P&L lines in `finance-summary.csv`. And a contradiction is not an accusation: the profile's "2 a week" is probably an old sentence nobody updated. You write it down because the next person will quote it.

### Step 5 — Ask for what is missing: the access request pack

Each missing item becomes a one-page request, using the [access request pack template](../../templates/access-request-pack.md). The data owner should be able to sign it in five minutes because everything they need to decide is on the page:

1. **What** — the dataset, the fields, the period. Ask for the minimum: the fields your question needs, not "everything".
2. **Why** — the question it answers, in one sentence, and which deliverable uses it.
3. **Form** — an export, read-only, not an admin login. Pseudonymised where you don't need names (the proxy log's user IDs already are; keep it that way).
4. **Who approves** — the business owner of the system (`it/saas-list.csv` names one for each), countersigned by your sponsor; IT executes.
5. **Where it lives and who sees it** — on the organization's drive, in a folder only you and named colleagues can open.
6. **Until when** — a deletion or return date, usually the end of the phase.
7. **Legal check** — whether counsel needs to look, and why.

**Israel first: when to involve counsel.** Three triggers come up in almost every first week:

- **Purpose.** Customer data is collected for stated purposes; Harbor & Pine's privacy notice (2022) lists processing orders, answering questions, invoices and marketing with consent — not analysing messages to design an AI system. The Privacy Protection Authority's draft guidance on AI (April 2025) says personal-data processing for AI needs a legal basis and recommends privacy by design and impact assessments. Whether your analysis fits is counsel's call; until then, ask for exports with the fewest personal fields.
- **Outside parties.** If you are a consultant, you are an outside service provider with access to the organization's databases. Regulation 15 of the Privacy Protection (Data Security) Regulations, 5777-2017 (תקנות הגנת הפרטיות (אבטחת מידע), התשע"ז-2017), in force since May 2018, and the PPA's 2011 outsourcing guidance set the contractual safeguards for that; the guidance prefers access to data that stays under the organization's control over handing over a copy. Counsel checks the agreement.
- **Abroad.** Uploading Israeli customer data to a service outside Israel is a transfer abroad under the Privacy Protection (Transfer of Data to Databases Abroad) Regulations, 5761-2001. It applies to the AI tool you are tempted to analyse with, too.

You are not deciding any of these. You are making sure each request names the trigger, so the right person decides before the data moves.

### Step 6 — Get it signed

Requests get signed when they arrive pre-filled, small and with the sponsor's support. Send them on day two, walk to the owner's desk if you can, offer the deletion date before they ask, and for systems outside your sponsor's line (StoreHub belongs to Noa) copy your sponsor and accept "not yet" as an answer you log, not a fight you start.

## Watch out

- **Believing the slide.** The KPI report's "2.0 hours" is true by its own definition and misleading as a headline. Read the footnotes first.
- **Asking for "everything".** It gets refused or delayed, and if it is granted you now hold data you cannot justify. Ask for fields that answer your question.
- **Admin logins instead of exports.** A login gives you more than you need, leaves no record of what you took, and makes you part of the system's security. Ask for exports.
- **Ignoring the hand-kept files.** The logistics ETA sheet and the claims log are messy, and they are where people actually work. They often hold the truth the systems miss.
- **Analysing customer data in an unapproved AI tool.** The quickest way to become your own shadow-AI finding. Use approved tools or synthetic copies.
- **Re-identifying pseudonymised data.** If a file comes pseudonymised, it stays that way unless management and counsel decide otherwise (01.6).
- **Calling a number verified because two documents agree.** Two narratives quoting each other are one source.

## Your turn

### Inputs

- The Harbor & Pine data room in the module download: [`labs/common/harbor-and-pine/INDEX.md`](../../labs/common/harbor-and-pine/INDEX.md) and every file it lists (skip `personas/` and `usage/`, which belong to later lessons).
- Templates: [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md); spreadsheet version `labs/module-01/data-room-first-read.csv`.
- Track B: `labs/module-01/first_read.py` ([lab README](../../labs/module-01/README.md)).

### Steps

1. Inventory every file (Step 1) and mark its provenance (Step 2).
2. List at least eight missing items, each with who would have it.
3. Build the claims register: at least ten numbers or factual statements from the narrative documents, each with who, where, when, status and the checking file. Check at least four against an export yourself.
4. Write three access requests: the web store's order export (from StoreHub), Deskly's configuration (macros and automations), and the delivery company's delivery records.
5. Write a five-line summary for Michal: what you can rely on, what you can't yet, and what you've asked for.

**Track B (Python).** Run `python first_read.py --csv first-read-files.csv` for step 1, then check two claims with a few lines of pandas (for example the Q3 ticket count and the SKU count).

### Time

75 minutes (Track B: about 60).

### Done when

- [ ] Every file has a line: what, source, period, size, owner, provenance.
- [ ] At least eight missing items, including at least one that may not exist at all.
- [ ] At least ten claims with actor, source, date and one of the four statuses; four checked by you against an export.
- [ ] Each access request has fields, period, purpose, approver, storage, deletion date and a legal-check line.
- [ ] No request asks for an admin login or "all data".

<details><summary>Reference answer</summary>

**Inventory (excerpt).** 19 CSVs and 17 documents. Exports: tickets (2,529, 1 May – 31 Oct 2026, Deskly, owner Samir), emails (600, a sample of tickets with full text), phone log (3,194, UTC), orders (3,134, placed 15 Mar – 31 Oct, Priority, owner Ronit), shipments (112, Gal-Ship portal, owner Tamar), proxy log (2,918, 11–22 Oct only, NetGuard via the MSP), browser extensions (173 rows on 83 devices, 28 Oct), expenses (310, Jan–Oct). Hand-kept: logistics ETA sheet (105 lines, Hebrew headers, dates as text), damage-claims log (149, Hebrew headers, Rina), 2023 catalogue copy (144 SKUs, shared drive). Settings: StoreHub lead times (5 rows, last modified 14 Feb 2023 by noa.levi).

**Missing (with owner).** Web-store order export (Noa/StoreHub); StoreHub checkout date logic (Noa); Deskly macros and automations (Samir); Deskly and Gal-Ship contracts (Ronit); delivery company's records (Tamar); showroom sales and service data (showroom managers, Yoav's line); call recordings (CloudVoice, deleted after 30 days — likely do not exist for the period); the finance business-case template (Ronit); who the privacy contact is and whether databases were reviewed after Amendment 13 (Michal, Ronit — IT doesn't know).

**Claims register.** The twelve rows in Step 4. Four self-checked: Q3 tickets 1,360 (verified), Q3 calls 1,368 / 83.6% (verified), SKUs 245 with 29 discontinued (verified), containers ~3 a week not 2 (contradicted).

**Access request — StoreHub order export (excerpt).** What: orders placed 15 Mar – 31 Oct 2026; fields order number, created date, promised delivery date shown at checkout, SKU, supplier country, delivery date, status; no names, addresses, phones or payment data. Why: to compare the date promised at checkout with the ERP's orders and container arrivals (findings memo, 1 Dec). Form: CSV export, read-only. Approver: Noa Levi (StoreHub owner), countersigned by Michal; executed by Noa's e-commerce manager. Storage: the programme folder on the company drive, access for me only. Deletion: 31 Jan 2027. Legal check: not needed if no personal fields are included; if order numbers can be linked to customers, ask counsel through Ronit.

**Access request — Deskly configuration.** What: list of macros with text, automation and SLA rules, status definitions and when each was changed. Why: to understand how "resolved" and first response are recorded (baselines, 02.4). Form: admin export or screenshots by Samir, no login for me. Approver: Samir, countersigned by Michal. Deletion: end of phase. Legal check: none (no personal data).

**Access request — delivery records.** What: delivery date, order number and outcome (delivered, failed, rescheduled) for May–Oct 2026, from the delivery company. Why: to verify actual delivery dates independently of the ERP. Form: CSV from the carrier, through Tamar. Approver: Tamar, countersigned by Michal; the carrier may need its own approval. Legal check: yes if the carrier sends addresses or phone numbers — ask for order numbers and dates only.

**Summary for Michal.** "I can rely on the system exports for volumes (tickets, calls, orders, containers). The KPI report's 2-hour response and 100% resolution use narrow definitions and need re-measuring; the 40% has no basis yet. Two documents contradict the data (container volume, PeopleWise's AI status). I've asked Noa for the web-store orders, Samir for Deskly's rules and Tamar for delivery records — all without customer names. Open: who our privacy contact is."

</details>

## References

- Pearl Cohen, [Israel: New Draft Guidelines on the Application of Privacy Law to AI](https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/) — legal basis, privacy by design, DPIAs (draft).
- IAPP, [The new Israeli data security regulations: a tutorial](https://iapp.org/news/a/the-new-israeli-data-security-regulations-a-tutorial) — in force 8 May 2018; security levels.
- Barnea Jaffa Lande, [Israel: Law and Practice (2020)](https://www.barlaw.co.il/wp-content/uploads/2020/02/011_ISRAEL-LP.pdf) — Regulation 15 and the PPA outsourcing guidance; transfers abroad.
- The course's [laws and guidance list](../../references/laws-and-guidance.md).
- Templates: [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md). Lab: [module 1 lab README](../../labs/module-01/README.md).
- Previous: [01.4 · The first-week plan and the 30-60-90](lesson-04.md). Next: [01.6 · The shadow-AI census](lesson-06.md).
