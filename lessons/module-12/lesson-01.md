---
id: "12.1"
module: 12
minutes: 16
practice_minutes: 90
prerequisites: ["01.1", "01.2", "01.3", "01.5", "08.1"]
objectives:
  - "Write down what changes when the client is a partnership of owners rather than a company with a CEO, and turn each change into a line of the engagement charter."
  - "Read back the managing partner's objective and write the vendor proposal as the question the engagement answers, not as its objective."
  - "Run the first-day data-room read on Atlas & Rowe's files and sort the headline numbers into verified, contradicted, claim to test and unverifiable."
  - "Draw the advisory boundary for a consultant who is not a lawyer, naming who answers each ethics and privilege question."
volatility: implementation
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): engagement form, advisory boundary, first-day data-room read"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Harvey: AI software for legal and professional services (product site; no public prices; checked 2 November 2026)"
    url: https://www.harvey.ai/
  - title: "Thomson Reuters, CoCounsel Legal (product page; research and drafting grounded in Westlaw and Practical Law; prices by plan or sales; checked 2 November 2026)"
    url: https://legal.thomsonreuters.com/en/products/cocounsel-legal
  - title: "Legora: collaborative AI for lawyers (product site; demo only, no public prices; checked 2 November 2026)"
    url: https://legora.com/
  - title: "Bank of Israel, representative exchange rate API (US$ = ₪3.136, 2 November 2026)"
    url: https://boi.org.il/PublicApi/GetExchangeRate?key=USD
last_verified: "2026-11-02"
---

# 12.1 · The call

A Tel Aviv law firm's managing partner wants an outsider to tell twenty-six partners what to buy, because half of them want a legal-AI platform before a discount expires and the other half think it will invent cases and cost them clients. You are a consultant again, but this client has no CEO: the owners vote, and you are not a lawyer in a building full of them. In this lesson you write the engagement charter, read the data room on day one, and draw the line between what you answer and what goes to the firm's ethics partner. At the end you have a charter, a first-read sheet and a first-week plan.

## The situation

Sunday 15 November 2026, 08:30, Menachem Begin Road, Tel Aviv. Read the [engagement brief](../../labs/module-12/brief.md) first (in the module download). Atlas & Rowe has 90 lawyers, 26 of them partners, and billed about ₪151M in 2025, roughly half of it by the hour. On 22 October partner Noa Friedman proposed signing Parshan AI (a fictional vendor) for all 90 lawyers for 24 months, with a 20% discount if signed by 31 December. The founding partner of the litigation group, Shmuel Atlas, opposed. A straw poll split 11 to 9 with 4 abstaining, and the partners deferred the vote to Thursday 14 January 2027.

Yoav Dagan, the managing partner, called you on 3 November. In his words: "Everyone wants Harvey or CoCounsel, or now this Israeli one. I need someone who isn't a partner to tell the partnership what to buy, with our own numbers. I can't be the one, I have to chair the vote." He signed your proposal on 5 November: three phases, ₪180,000 + VAT.

The products he names are real and you will meet them in the market: [Harvey](https://www.harvey.ai/), Thomson Reuters' [CoCounsel Legal](https://legal.thomsonreuters.com/en/products/cocounsel-legal) and [Legora](https://legora.com/), among others. None publishes a price list (checked 2 November 2026); you buy them through sales and a proof of concept. The vendor in this story, Parshan AI, is fictional so that it can play a role.

IBM's consulting certificate calls the shape of an engagement its *form* and the line between what you answer and what you route the *advisory boundary*. You wrote both at Northwind in [08.1](../module-08/lesson-01.md). Here both change, because the client is a partnership and the subject is the client's own profession.

## What to do

### Step 1 — Write down what a partnership changes

At Northwind the CEO owned the ask and could overrule everyone. Here nobody can. Fill this table before you write the charter (the general version is in [01.1](../module-01/lesson-01.md)):

| | What it means at Atlas & Rowe | What you write into the charter |
|---|---|---|
| **Who decides** | The partners' meeting, one vote each. Yoav chairs and cannot campaign | "The decision belongs to the partners' meeting of 14 January"; the management committee prepares it |
| **The people with the ask** | Two: Noa (for) and Shmuel (against). Each will read you as the other's weapon | One-to-one time with both before any paper; neither sees a finding first in a room |
| **Owners, not employees** | A partner's billed hours partly decide her pay. A recommendation touches income, not only workflow | You describe effects on fees by practice; you do not design compensation (out of scope, named owner) |
| **Clock** | The vendor's discount date (31 December) arrives before the vote | The decision paper on 17 December says what to do about the discount; the date does not decide by default |
| **Access** | Client files are confidential and privileged; you may not see them | Pseudonymised extracts only; the research corpus with client identifiers removed; nothing privileged requested |
| **Your expertise** | You are not a lawyer. Everyone in the room is | Advisory boundary: ethics, privilege, consent and billing rules go to the ethics partner |

The fourth row is new. In a company, a tool that saves time is a cost question. In a firm that bills by the hour, it can lower some partners' income while raising others'. You will not fix that, but if you do not see it, you will not understand the vote.

### Step 2 — Read back the objective, and demote the product

The method is [01.2](../module-01/lesson-02.md). Read Yoav's objective back word for word: "Advise the partnership, on the firm's own data, how Atlas & Rowe should use AI in its legal work from 2027, what to buy if anything, and on what terms; test it on our own material."

Then write the stated ask, "should we sign Parshan?", as the **question the work answers**, not as the objective. If "buy Parshan or not" is the objective, the engagement can only end in a purchase decision, and every other finding (how lawyers already use AI, what the knowledge base looks like, what clients will pay) becomes a footnote. Say this to Yoav plainly; most managing partners agree when they hear it, because it protects them from being the person who bought or blocked the tool.

"Done" in checkable form: a paper the partners vote on, with one recommendation and every number labelled measured, directional or assumed; a decision minuted with an owner and a date for each part; if a pilot is justified, an evaluation on the firm's own documents against thresholds dated before the run; a named owner who accepts the handover.

### Step 3 — Exits, scope and the advisory boundary

Write the statement of work with its exits (3 December after the diagnosis; 17 December after the decision paper) using the [engagement charter](../../templates/engagement-charter.md) and the [scope boundary](../../templates/scope-boundary.md) from [01.3](../module-01/lesson-03.md). Three scope calls matter here:

- **Knowledge management is in**, as far as an AI tool would search it. A research tool is only as good as the documents behind it; leaving the precedent bank out of scope is like leaving the returns policy out at Northwind.
- **Pricing and billing are in**, as far as AI changes them. Compensation is out, with an owner: the management committee.
- **Legal and ethics opinions are out.** You will find things that look like confidentiality problems. You describe the facts and route them; you do not say "this breaches privilege".

The advisory boundary in a law firm is personal: the people you would route to are partners you will also interview. Name them: Orit Levinson (general counsel and ethics partner) for confidentiality, privilege, client consent and what may be billed, and through her outside ethics counsel; the managing partner and the finance director for client negotiations; IT and its managed service provider for security.

### Step 4 — Read the data room on the first day

Follow [01.5](../module-01/lesson-05.md) and open the data room's [INDEX](../../labs/module-12/data-room/INDEX.md). Two facts change how you read everything:

- The **time entries** cover one quarter and three groups (Litigation, Tech & IP, the International desk), 40 lawyers. They are the firm's own record of work, so they carry its conventions. Treat the activity codes as a claim until you have read the narratives.
- The **research corpus** is not the whole precedent bank. It is the 78 documents the head of knowledge management exported on 2 November for the vendor's proof of concept: fictional rulings, firm memos and clause notes, with numbered paragraphs. It is what any research tool would actually search.

Then sort the headline numbers. A worked example from Atlas & Rowe's files:

| Number | Where | Sort | Why |
|---|---|---|---|
| "Lawyers save 6.2 hours a week" | Minutes; vendor deck slide 3 | **Claim to test** | Footnote: self-reported survey, 212 lawyers at 9 US and UK firms |
| "₪23.3M of capacity for ₪0.4M" | Minutes | **Contradicted in form** | Hours × billing rate treated as money; finance says associates are at about 81% of target |
| "Zero hallucinations" | Deck slide 4 | **Claim to test** | The demo used 12 English questions on US law; the PoC ran on firm documents on 2 November |
| Fees ₪151.1M, realisation 87% | Finance summary | **Verified** | `billing/matters.csv` adds up to it |
| Associates at 81% of target | Finance summary | **Verified** | `people/lawyers.csv` |
| "Associates use ChatGPT anyway" | Minutes | **Reported** | The proxy log and the survey can test it |
| Precedent status "current" | KM index | **Claim to test** | Status defaults to current on upload |
| Research share of lawyers' time | Time entries | **Unverifiable from the codes alone** | Codes and narratives may disagree (12.2) |

What is missing: the vendor's PoC outputs, the closure notes of the data-loss-prevention alerts, any measure of time per research task, any AI policy, and any record of client consent. Put them in the [access request pack](../../templates/access-request-pack.md). Do not ask for client files: you do not need them, and asking signals that you do not understand where you are.

### Step 5 — Plan the first week around both camps

Use the [30-60-90 plan](../../templates/30-60-90-plan.md) from [01.4](../module-01/lesson-04.md), shortened to eight and a half weeks. Week 1 must reach:

- **Finance** (Eli Ben-Hamo): the money question is half the decision.
- **Knowledge** (Tamar Golan): what any tool would search.
- **Ethics** (Orit Levinson): what you will be routing to her for eight weeks.
- **Both camps**: Noa this week; Shmuel before the 3 December readout at the latest.
- **Associates**, with their supervising partners told. Yoav will hesitate ("the partners will want to know who you're talking to"); agree to tell each partner whom you meet and to keep what people say unattributed.

### Step 6 — Agree it with the sponsor

Sit with Yoav (roleplay: [Yoav Dagan](../../labs/module-12/personas/yoav-managing-partner.md); no-roleplay path: [the transcript](../../labs/module-12/personas/transcripts/yoav-managing-partner.md)). What you want from the conversation: the objective read back; done, exits and change control agreed; access to associates; a private preview before each committee; and whatever he knows about pressure from the vendor and from clients. Ask about commitments and about clients, not about AI. Afterwards paste the transcript into the [coach prompt](../../labs/common/coach-prompt.md) with the persona's checklist.

## Watch out

- **Making the product the objective.** "Should we buy Parshan" is a question the engagement answers. Written as the objective, it hides everything else you will find.
- **Taking a side by calendar.** Meeting Noa in week 1 and Shmuel in week 4 tells the partnership who you work for. Book both early.
- **Playing lawyer.** You will be tempted to say "that's a privilege problem". Describe the fact, name the owner, and stop. Your credibility in a room of lawyers rests on knowing where your expertise ends.
- **Asking for client files.** You do not need them to answer the question. Pseudonymised extracts and a research corpus with identifiers removed are enough, and asking for more makes the ethics partner your opponent.
- **Letting the discount date decide.** A deadline set by a vendor is a negotiating position. Put it in the decision paper as a question with an answer, not as a constraint on your work.
- **Ignoring how partners are paid.** You will not change it, but a vote that splits by practice type usually has an income reason.

## Your turn

### Inputs

- [Engagement brief](../../labs/module-12/brief.md) and the [data room](../../labs/module-12/data-room/INDEX.md) (module download): especially `firm/partners-meeting-2026-10-22-minutes.md`, `firm/finance-summary-2026.md`, `people/lawyers.csv`, `vendor/parshan-demo-deck.md`, `km/precedent-bank-index.csv`.
- Persona: [Yoav Dagan](../../labs/module-12/personas/yoav-managing-partner.md) or [his transcript](../../labs/module-12/personas/transcripts/yoav-managing-partner.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [engagement charter](../../templates/engagement-charter.md), [scope boundary](../../templates/scope-boundary.md), [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md), [30-60-90 plan](../../templates/30-60-90-plan.md).

### Steps

1. Fill the "what a partnership changes" table (six rows) for Atlas & Rowe.
2. Interview Yoav (or read the transcript and mark what the interviewer found and missed). Read back the objective; agree done, exits, change control, access to associates.
3. Write the charter: objective, the stated ask as the question answered, done, entry-role table, scope summary, SOW with exits, advisory boundary with named people.
4. Do the first read: list every file, mark provenance, and sort at least eight headline numbers with their evidence.
5. Write the access request for what is missing.
6. Write the first-week plan and the risks to the engagement.

### Time

90 minutes: 20 for the interview, 30 for the charter, 25 for the first read, 15 for the plan and access request.

### Done when

- [ ] The objective is Yoav's, read back; "sign Parshan?" appears as the question the work answers.
- [ ] "Done" is a voted paper with labelled evidence, minuted owners and dates, a pre-dated pilot evaluation if any, and a named handover owner.
- [ ] The SOW has three phases with an exit, a deliverable and a decider at each.
- [ ] The advisory boundary names the ethics partner (and outside ethics counsel) for confidentiality, privilege, consent and billing rules, and requests no client files.
- [ ] At least eight numbers are sorted with evidence, including the 6.2 hours, the ₪23.3M and "zero hallucinations".
- [ ] Week 1 reaches finance, knowledge, ethics and both camps, with associates' partners informed.

<details><summary>Reference answer</summary>

The full expert version is in the module download, `labs/module-12/expert/01-engagement-charter.md`. Key parts:

**Objective (Yoav, read back 15 November):** "Advise the partnership, on the firm's own data, how Atlas & Rowe should use AI in its legal work from 2027, what to buy if anything, and on what terms; test it on our own material." **Question answered:** whether to sign Parshan for 90 seats for 24 months before 31 December.

**Done:** a paper the partners vote on 14 January with one recommendation and labelled numbers; owners and dates minuted for each part; any pilot evaluated on the firm's corpus against thresholds dated before the run; a named owner (proposed: Orit Levinson for rule and consent, Tamar Golan for knowledge).

**SOW:** Diagnose 15 Nov – 3 Dec, ₪64,000, exit at the readout; Decide and build 6 Dec – 7 Jan, ₪96,000, exit after the decision paper of 17 December; Readout 10–14 Jan, ₪20,000. Changes by written request signed by the managing partner.

**Advisory boundary:** confidentiality, privilege, consent, incidents, what may be billed → Orit Levinson and outside ethics counsel; client negotiations → Yoav and Eli; compensation → management committee; security → IT and the managed service provider. No client files requested.

**First read (excerpt):** 6.2 h claim to test (self-reported, other firms); ₪23.3M contradicted in form (hours treated as money; associates at 81% of target); "zero hallucinations" claim to test (PoC outputs requested); fees and realisation verified; "associates use ChatGPT anyway" reported, testable in the proxy log; precedent status claim to test.

**First week:** Sun Yoav; Mon Eli; Tue Tamar; Wed Orit; Thu Noa and the time-entry profile; Shmuel booked for 1 December; associates in week 2 with partners informed.

**What the transcript's interviewer missed:** they never asked how partners are paid or why the vote splits the way it does, so the compensation reason (15% of a partner's points depend on personal billed hours) stayed hidden. They found the vendor pressure ("I may have been too encouraging") and Carmel's 15% request.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): engagement form, advisory boundary, first-day read (named, not re-taught).
- The legal-AI market, as vendors describe themselves (checked 2 November 2026; no public prices): [Harvey](https://www.harvey.ai/), [CoCounsel Legal](https://legal.thomsonreuters.com/en/products/cocounsel-legal), [Legora](https://legora.com/). Parshan AI in this module is fictional.
- Bank of Israel, [representative exchange rate](https://boi.org.il/PublicApi/GetExchangeRate?key=USD) (₪3.136 per US$ on 2 November 2026), used for Parshan's US$ prices throughout the module.
- Field kit: [01.1 · Three ways in](../module-01/lesson-01.md), [01.2 · Getting a real mandate](../module-01/lesson-02.md), [01.3 · Scope boundary](../module-01/lesson-03.md), [01.4 · The first-week plan](../module-01/lesson-04.md), [01.5 · The first-day data-room read](../module-01/lesson-05.md); the first consultant engagement: [08.1 · The call](../module-08/lesson-01.md).
- Templates: [engagement charter](../../templates/engagement-charter.md), [scope boundary](../../templates/scope-boundary.md), [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md), [30-60-90 plan](../../templates/30-60-90-plan.md).
- Next: [12.2 · Discovery](lesson-02.md).
