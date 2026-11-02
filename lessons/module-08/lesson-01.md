---
id: "08.1"
module: 8
minutes: 16
practice_minutes: 90
prerequisites: ["01.1", "01.2", "01.5", "07.9"]
objectives:
  - "Write down what changes when you enter as an outside consultant rather than an internal hire, and turn each change into a line of the engagement charter."
  - "Read back the sponsor's objective, fix what done means, and place exit points and change control in a statement of work."
  - "Run the first-day data-room read on Northwind's files and sort the headline numbers into verified, contradicted, claim to test and unverifiable."
  - "Plan the first week so the floor, the definitions and the person with the ask are reached before the first readout."
volatility: implementation
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): engagement form, advisory boundary, first-day data-room read"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "IAPP, Israel marks a new era in privacy law: Amendment 13 ushers in sweeping reform (in force 14 August 2025; DPO appointments; PPA sanctions)"
    url: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
  - title: "Bank of Israel, representative exchange rate API (US$ = ₪3.136, 2 November 2026)"
    url: https://boi.org.il/PublicApi/GetExchangeRate?key=USD
last_verified: "2026-11-02"
---

# 08.1 · The call

Northwind Outfitters' COO wants an outsider to tell her company, with its own data, what to do about a chatbot its CEO has already promised the board. You have done this before at Harbor & Pine, but from inside. This time you are a consultant with a fixed fee, ten weeks and no authority of your own, and the decision you were hired to inform is already half-taken. In this lesson you write the engagement charter with its statement of work, read the data room on day one, and plan the first week. At the end you have a signed-ready charter, a first-read sheet and a five-day plan.

## The situation

Sunday 8 November 2026, 08:30, Northwind's head office in Petah Tikva. Read the [engagement brief](../../labs/module-08/brief.md) first (in the module download). In short: Northwind sells outdoor gear online, 450 employees, about 60,000 orders a month. On 21 September the CEO, Gil Shachar, told the board that the Verbalo chatbot (live on web chat since 15 June) would let customer-service cost fall by half by Q2 2027. The fund that owns 35% wrote it into the 2027 budget: 21 agents from April. The team has already gone from 42 agents to 30.

Orly Ben-David, the COO, called you on 2 November. Her words: "I need someone from outside to tell us what to do next, with evidence, by the January board. I can't be the one who says it." She signed your proposal on 5 November: three phases, ₪222,000 + VAT, 8 November to 14 January.

You have met this structure before. IBM's consulting certificate calls the commercial shape of an engagement its *form* and the line between what you answer and what you route its *advisory boundary*; lesson [01.1](../module-01/lesson-01.md) turned both into documents. Here you write them for real, for a client who can stop paying you at each gate.

## What to do

### Step 1 — Write down what being outside changes

At Harbor & Pine you were the COO's employee. At Northwind you are her supplier. Use the table from [01.1](../module-01/lesson-01.md) and fill in this column for Northwind before you write anything else:

| | What it means here | What you write into the charter |
|---|---|---|
| **Authority** | None. Agents, BI and legal do not report to you; you ask through Orly | "Requests to staff go through or with the sponsor"; a weekly one-page note |
| **The person with the ask** | Gil made the promise; Orly hired you. Gil may see you as Orly's weapon against his plan | A private session with Gil before every steering meeting; no finding reaches him first in a room |
| **Money and clock** | A fixed fee in three phases; the contract ends 14 January whether or not the work is "done" | Exit points; a named Northwind owner from week 1, not week 10 |
| **Access** | An NDA, a data-processing agreement, a Northwind laptop, pseudonymised extracts; no live systems | An access request on day 2 for what the extract lacks |
| **Independence** | It is what Orly is paying for. It is also why she can end the engagement on 26 November | Recommend against early and privately; never let a "no" reach the steering group cold |

The last row is the one people get wrong in both directions. Some consultants protect the next invoice and soften everything; others confuse independence with saying hard things in public. Both lose the client. Independence means the finding is not negotiable and the delivery is.

### Step 2 — Read back the objective and fix "done"

The method is [01.2](../module-01/lesson-02.md): the objective in the sponsor's words, read back, then the definition of done. Two objectives exist here, and the charter must hold both without pretending they are the same:

- **Orly's** (signed): "A recommendation, backed by Northwind's own data, on how AI should be used in customer service in 2027, and a tested pilot if one is justified."
- **Gil's** (board minute): "A chatbot that replaces half of support by Q2."

Write Orly's as the objective and Gil's as "the stated ask this engagement tests". Then make "done" checkable: a minuted decision by the steering group on 12 January, each piece of evidence labelled measured, directional or assumed; a named Northwind owner who accepts the handover on 14 January; and, if a pilot is justified, an offline evaluation on Northwind's own tickets against thresholds agreed before the run.

### Step 3 — Put the exits and change control into the statement of work

The brief already has three phases. Your job is to make the exits real: say what is delivered at each, who decides whether to continue, and what happens to the money. Write it as a table in the charter (the [engagement charter](../../templates/engagement-charter.md) template has the SOW outline) and add the [scope boundary](../../templates/scope-boundary.md) from [01.3](../module-01/lesson-03.md): in, out, with a reason each. For Northwind the hard calls are:

- **The returns process.** Is it in scope? It belongs to the warehouse, not to customer service. Put it in "as far as it drives contact", or you will discover in week 2 that the biggest driver is out of scope.
- **Legal opinions.** Out, routed to counsel by name. You will find things that look unlawful; you will not say they are.
- **Vendor negotiation.** You prepare; Northwind negotiates. A consultant who negotiates with the CEO's chosen vendor has just become a party.

### Step 4 — Read the data room on the first day

Follow [01.5](../module-01/lesson-05.md): inventory every file, mark where it came from, list what is missing, and sort the numbers. Open the data room's [INDEX](../../labs/module-08/data-room/INDEX.md). Two facts change how you read everything else:

- The exports are a **1% customer sample**: all orders, returns, contacts and logged-in chatbot sessions of a random 1% of customers. Multiply counts by 100. BI chose customers, not contacts, so one customer's journey across channels stays whole. You will need that in 08.2.
- The 2,000 written tickets are a **separate, company-wide random extract** for September–October, with the agent's actual reply.

Then sort the headline numbers. A worked example from Northwind's own files:

| Number | Where it is | Sort | Why |
|---|---|---|---|
| "AHT down 30%" | Board minute; Q3 report | **Contradicted** | Q2 footnote: AHT includes after-contact work; Q3 footnote: agent handling time only. Not the same measure |
| "Containment above 60%" | Board minute; Q3 report (63%) | **Claim to test** | Footnote 4: "as reported by Verbalo's dashboard"; definition in the order form §3 |
| "Headcount 42 → 30, no drop in service" | Board minute; headcount file | Headcount **verified**; "no drop" **contradicted** | Q3 report: median written first response 3.6 h (July) → 8.1 h (September) |
| Returns "within 14 days … store credit" | Returns page | **Contradicted** by Northwind's own terms | Terms of sale §9: money back, fee 5% or ₪100 |
| "Inspection within 2 business days" | Warehouse SOP | **Claim to test** | `returns.csv` has received and inspected dates |
| "Repeat-contact rate" | Q3 report | **Unverifiable** (nobody measured it) | "Not tracked" |
| 62% containment, "29 agents" | Vendor deck | **Claim to test** | Slide 3: 40 questions, English, sandbox |

What is missing: any evaluation of the chatbot, 2025 contact data, the BI definition change log, legal's review of the returns page (the contract-review log says one exists), live system access. Those go into the [access request pack](../../templates/access-request-pack.md).

### Step 5 — Plan the first week around three things

A consultant's first week has to reach the floor, the definitions and the person with the ask, because those are the three places the stated ask can be tested. Use the [30-60-90 plan](../../templates/30-60-90-plan.md) from [01.4](../module-01/lesson-04.md), shortened to ten weeks, and a day-by-day first week:

- **The floor before the peak.** Black Friday is 27 November; after that nobody on the floor has two hours for you. Book the WhatsApp desk in week 1.
- **The definitions.** Every number in the first-read sheet that is "contradicted" or "claim to test" needs its owner: BI for AHT and contacts, Verbalo for containment, the warehouse for inspection.
- **The CEO before the first readout.** Orly's offer of "after Black Friday" puts Gil after the 26 November readout. Ask for fifteen minutes before it; if you cannot get them, write in the charter that the readout goes to Gil privately first.

### Step 6 — Agree it with the sponsor

Sit with Orly (roleplay: [Orly Ben-David](../../labs/module-08/personas/orly-coo.md); no-roleplay path: [the transcript](../../labs/module-08/personas/transcripts/orly-coo.md)). What you want out of the conversation: the objective read back and agreed; done, exits and change control agreed; time with Gil requested; and anything she knows about returns and refunds, because she runs the warehouse too. Ask about the work, not about the bot. Afterwards paste the transcript into the [coach prompt](../../labs/common/coach-prompt.md) with the persona's checklist.

## Watch out

- **Writing Gil's ask as your objective.** Then the engagement can only succeed by delivering a chatbot. Write it as the claim you test.
- **Exits on paper only.** If nobody has said out loud that you may recommend stopping at 26 November, the exit is decoration. Say it in the first meeting, as Orly's choice and yours.
- **Scope that leaves out the cause.** At Harbor & Pine the cause sat in logistics; here it sits in returns. "As far as it drives contact" keeps it in without taking over the warehouse.
- **Accepting the sample as the company.** 2,075 contact rows look small. They are 1%. State it on every number you quote until 08.3.
- **Meeting the CEO last.** A consultant who first meets the CEO in the steering room with a finding about his slide has chosen a fight, not a decision. If the calendar forbids it, write the risk down and mitigate it.
- **Promising outcomes to win the next phase.** The fixed fee protects you from that temptation only if you let it.

## Your turn

### Inputs

- [Engagement brief](../../labs/module-08/brief.md) and the [data room](../../labs/module-08/data-room/INDEX.md) (module download): especially `company/board-update-2026-09.md`, the two KPI reports, `people/cs-headcount-2026.csv`, `policies/`, `vendor/verbalo-order-form.md`, `legal/contract-review-log.csv`.
- Persona: [Orly Ben-David](../../labs/module-08/personas/orly-coo.md) or [her transcript](../../labs/module-08/personas/transcripts/orly-coo.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [engagement charter](../../templates/engagement-charter.md), [scope boundary](../../templates/scope-boundary.md), [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md), [30-60-90 plan](../../templates/30-60-90-plan.md).

### Steps

1. Fill the "what being outside changes" table for Northwind (five rows).
2. Interview Orly (or read the transcript and mark what the interviewer found and missed). Read the objective back; agree done, exits, change control.
3. Write the charter: objective, the stated ask as a claim, done, entry-role table, scope summary, SOW table with exits, advisory boundary with named people.
4. Do the first read: list every file, mark provenance, and sort at least eight headline numbers (verified, contradicted, claim to test, unverifiable) with the evidence.
5. Write the access request for what is missing.
6. Write the first-week plan, day by day, and the risks to the engagement.

### Time

90 minutes: 20 for the interview, 30 for the charter, 25 for the first read, 15 for the plan and the access request.

### Done when

- [ ] The objective is Orly's, read back; Gil's ask appears as the claim the engagement tests.
- [ ] "Done" is a minuted decision, a named owner and, if justified, a pilot evaluated against thresholds set beforehand.
- [ ] The SOW has three phases with an exit, a deliverable and a decider at each; change control names the COO.
- [ ] The advisory boundary names counsel, HR, IT and the privacy owner for the questions you will not answer.
- [ ] At least eight numbers are sorted with their evidence, including the AHT figure and containment.
- [ ] The first week reaches the floor, the KPI definitions and the CEO (or names the risk if the CEO cannot be reached).

<details><summary>Reference answer</summary>

The full expert version is in the module download, `labs/module-08/expert/01-engagement-charter.md`. Key parts:

**Objective (Orly, read back 8 November):** "A recommendation, backed by Northwind's own data, on how AI should be used in customer service in 2027, and a tested pilot if one is justified." Added at read-back: "something that survives the board and the fund". **Stated ask tested:** "a chatbot that replaces half of support by Q2 2027" (board, 21 September).

**Done:** steering decision 12 January with labelled evidence; Meseret Tadesse (or a named team lead) accepts the handover on 14 January; any pilot evaluated offline against thresholds agreed before the run.

**SOW:** Diagnose 8–26 Nov, ₪72,000, exit at the 26 November readout; Decide and build 29 Nov – 7 Jan, ₪126,000, exit after the decision paper on 3 December; Readout and handover 10–14 Jan, ₪24,000. Changes by written request signed by the COO.

**First read (excerpt, numbers from the files):**

| Number | Sort | Evidence |
|---|---|---|
| AHT down 30% (5.6 vs 8.0 min) | Contradicted | Q2 vs Q3 footnote 2: definition changed |
| Containment 63% (Q3) | Claim to test | Verbalo dashboard; order form §3 "Resolution" = no escalation |
| 42 → 30 agents | Verified | `cs-headcount-2026.csv`: 6 + 3 not renewed, 3 resignations not replaced |
| "No drop in service" | Contradicted | Median written first response 3.6 h (Jul) → 8.1 h (Sep); phone wait 124 s → 219 s |
| Contacts per 100 orders 58.7 vs 50.7 | Verified, but the definition changed too | Q3 counts agent contacts only |
| Returns: store credit, 10% + ₪39 | Contradicted by Northwind's terms §9 | Money back, fee 5% or ₪100 |
| Club: 30 days, refund | Contradicts the returns page | Trail Club terms 5.2 |
| Inspection in 2 business days | Claim to test | SOP-WH-07 step 2 vs `returns.csv` |
| Repeat-contact rate | Unverifiable | "Not tracked" |
| 62% containment, 29 agents | Claim to test | Vendor deck slide 3: 40 English questions, sandbox |

**Missing, requested on day 2:** BI's KPI change log; any chatbot evaluation; counsel's review of the returns page (LR-2026-011); a read-only helpdesk sandbox for phase 2; 2025 monthly contact totals.

**First week:** Sun Orly and the first read; Mon Alexei (definitions) and Meseret; Tue two hours on the WhatsApp desk; Wed first cut of repeats and refund time; Thu Boris and the weekly note. Gil: 15 minutes requested before 26 November; if refused, the readout goes to him privately on the morning of the 26th.

**What the transcript's interviewer missed:** they never asked Orly what she herself thinks the real problem is, so her view of the bot stayed hidden; and they did not ask about the team's state before Black Friday.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): engagement form, advisory boundary, first-day read (named, not re-taught).
- IAPP, [Amendment 13 to Israel's Privacy Protection Law](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform) (in force 14 August 2025): why the data-processing agreement and the privacy owner belong in the charter. Route the specifics to counsel.
- Bank of Israel, [representative exchange rate](https://boi.org.il/PublicApi/GetExchangeRate?key=USD) (₪3.136 per US$ on 2 November 2026), used for Verbalo's US$ prices throughout the module.
- Field kit: [01.1 · Three ways in](../module-01/lesson-01.md), [01.2 · Getting a real mandate](../module-01/lesson-02.md), [01.3 · Scope boundary](../module-01/lesson-03.md), [01.4 · The first-week plan](../module-01/lesson-04.md), [01.5 · The first-day data-room read](../module-01/lesson-05.md).
- Templates: [engagement charter](../../templates/engagement-charter.md), [scope boundary](../../templates/scope-boundary.md), [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md), [30-60-90 plan](../../templates/30-60-90-plan.md).
- Next: [08.2 · Discovery](lesson-02.md).
