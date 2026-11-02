---
id: "01.3"
module: 1
minutes: 16
practice_minutes: 60
prerequisites: ["01.2"]
objectives:
  - "Write a scope boundary whose every inclusion and exclusion carries a reason drawn from the objective or a finding."
  - "Decide whether a new request is a refinement or an expansion, using five yes/no questions."
  - "Run a change-request route: log, assess, decide, and tell the requester, without losing their goodwill."
  - "Get the boundary acknowledged in writing by the people who can change it."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 1, module 'Framing and Scoping the Engagement'"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-02"
---

# 01.3 · Scope boundary and change control

Every department head you meet in your first week will have an AI idea, and most of them are good ideas. If you accept them all, phase one has no shape and nothing finishes by January; if you refuse them without reasons, you lose the people you need. In this lesson you turn the sponsor's objective into a scope test, write a boundary with a reason for every line, sort new requests into refinement or expansion, and set up the change-request route — practising on the marketing director, who adds one more idea after every answer.

## The situation

Your objective is confirmed (lesson 01.2): on 28 January the board sees one thing that works, a six-month plan it believes, numbers the CFO has signed, and the operations teams' trust intact; the bot is a means to "fewer angry customers and a support cost that doesn't keep rising".

On 5 November you meet Noa Levi, Marketing Director. She owns the web store (StoreHub), reports to the CEO rather than to your sponsor, loves the AI push, and wants marketing visible in it. She is generous, quick and persuasive, and she will keep saying "while you're at it".

IBM's advisor course orders the work as objective → scope → boundary, and asks whether each later request is a refinement or an expansion. Here you write the boundary, the test and the form that make those words work in a real week.

## What to do

### Step 1 — Turn the objective into a scope test

A boundary is only as good as the rule behind it. Write the rule first, in one sentence the sponsor would sign. For Harbor & Pine:

> Phase one (to 28 January) includes work that (a) reduces angry customer contacts or the cost of
> handling them, (b) deals with a risk we must handle now, or (c) is needed to measure or prove
> (a) and (b). Everything else goes on the request list with a review date.

Every line of the boundary then answers to this sentence. "It's a good idea" is not a reason; "it does not touch customer contacts or support cost" is.

### Step 2 — Write inclusions and exclusions, each with a reason

Use the [scope boundary template](../../templates/scope-boundary.md). Three columns matter: the item, in or out, and **the reason**, which comes from the objective or from something you found. Add a fourth for items that are not yours to change but that you need to *look at*:

| Item | In / out / read-only | Reason |
|---|---|---|
| Customer-service contacts: email, web form, phone | In | Test (a): the objective |
| Existing AI use in the company (shadow AI, AI inside SaaS) | In | Test (b): customer data may already be in free tools |
| Minimum guardrails: interim rule, approved tool, AI inventory | In | Test (b) |
| Baselines and data exports for customer service and delivery | In | Test (c) |
| Delivery-date promise shown at checkout (StoreHub) | Read-only | Many contacts may be about delivery dates; StoreHub belongs to marketing, so changes are Noa's and Yoav's decision |
| Sales chatbot on the website | Out (request list) | Aims at conversion, not support contacts; revisit if a customer-facing platform is chosen |
| Vendor selection and contracts | Out | Not before the evidence; no vendor commitments in November |
| Headcount decisions | Out | Not this programme's decision; CEO with HR and the labour lawyer |

Write exclusions as "not now, because …, reviewed on …" wherever that is true. "No" without a date sounds like "never", and people fight "never".

### Step 3 — Get it acknowledged by the people who can change it

A boundary nobody signed is a draft. Get written acknowledgement from:

- **The sponsor** (Michal) for the whole boundary — an email reply "agreed" is enough; record the date in the document.
- **The owner of each by-request area** for the lines that touch it. Noa owns the web store and reports to Yoav, so the "read-only" line on StoreHub and the out-of-scope marketing items need Noa's acknowledgement and Yoav's sight. Copy Yoav on the summary; one line from him ("fine") is worth a meeting.

If someone refuses to acknowledge, you have learned something important: the scope is contested. Take it to the sponsor that week rather than discovering it in January.

### Step 4 — Refinement or expansion? Five questions

When a request arrives mid-phase, ask five yes/no questions:

1. Does it serve the same objective?
2. Does it affect the same users or customers?
3. Does it use the same data and systems?
4. Is it the same deliverable, done deeper or better?
5. Does it fit inside the agreed time and money without dropping anything?

All five "yes": **refinement** — do it inside the phase and note it. Any "no": **expansion** — it goes through a change request, however small. Examples at Harbor & Pine:

- "Test the email triage on Arabic and Russian tickets too" — same objective, customers, data and deliverable; refinement (the tickets are already in scope).
- "Translate the whole website into Arabic and Russian" — different deliverable and system, new legal and checkout work; expansion.
- "Add the phone channel to the baseline" — same objective and customers, new data source (CloudVoice), and a day of work; question 5 decides. If it fits, refinement; if it displaces something, a change request.

### Step 5 — Set up the change-request route

The route has four parts, and the requester must see all four:

1. **Log.** Every request goes into one list (the [change request template](../../templates/change-request.md) has a log and a form; a spreadsheet version is in the module download, `labs/module-01/change-request-log.csv`). Nothing disappears.
2. **Assess.** You fill a short form within a week: the problem behind the request, who benefits, rough size, link to the objective, what it would displace.
3. **Decide.** The sponsor decides, at the weekly check-in for small items and at a monthly review for anything that needs money or another department. For items in the CEO's area, the CEO and the sponsor decide together.
4. **Tell.** The requester hears the decision and the reason, and the review date if it is "not now".

At Harbor & Pine: you assess; Michal decides; marketing items go to the first monthly review with Yoav, in December, and the request list is reviewed again in February when the peak season ends.

### Step 6 — Run the conversation with the scope-adder

People who keep adding scope are usually enthusiasts, not opponents. The technique that works with Noa:

1. **Write every idea down where she can see it.** "I'm writing each idea down so nothing gets lost." It lowers the pressure to win now.
2. **Ask for the problem behind each idea**, not the feature. "What's wrong with the descriptions today?" often reveals what matters.
3. **Show the test before you apply it.** "Phase one is in scope only if it reduces customer contacts or support cost, or is a risk we must deal with now. Does that sound fair?"
4. **Give each "out" a reason and a date.** "On the list, reviewed in February, with a note that it links to the support-languages work."
5. **Hold the line once more, kindly.** She will test it ("but this one is tiny"). Size is not the test; the objective and what it displaces are. If it is tiny and outside, she may well do it herself within the guardrails you will publish in week two.
6. **Use the conversation for discovery too.** Ask which AI tools her team already uses and how they pay (01.6), and who decides the delivery date at checkout. Both answers matter more to your engagement than any of her requests.

### Step 7 — Worked example: Noa's requests, logged

From the pre-run transcript (`personas/transcripts/noa-marketing.md`):

| # | Request | Refinement / expansion | Decision | Reason given to Noa | Review |
|---|---|---|---|---|---|
| CR-01 | AI product descriptions for all SKUs | — (already running) | Not a project: record in the AI inventory | StoreHub's feature is on and Shir checks the output; it needs an inventory line and an owner, not a programme | 01.7 |
| CR-02 | Sales chatbot on the website | Expansion | Out of phase 1 | Aims at conversion, not support contacts; the platform question comes up anyway if a support bot is considered | Feb 2027 |
| CR-03 | AI-personalised email campaigns (MailPost) | Expansion | Out of phase 1; inventory | Marketing outcome; MailPost's AI features go in the inventory | Feb 2027 |
| CR-04 | Instagram content with AI images | Expansion | Out of phase 1 | Marketing cost, not support | Feb 2027 |
| CR-05 | Translate the website into Arabic and Russian | Expansion | Out of phase 1; linked to support languages | New deliverable, system and legal review; may reduce contacts from Arabic and Russian speakers — measure first | Feb 2027 |
| CR-06 | AI "room designer" | Expansion | Out | No link to the objective | Feb 2027 |

The interviewer did two things well: wrote every idea down and showed the test before applying it. They also asked which AI tools marketing uses and how they are paid for, and learned about CopyGenie and ChatGPT Plus on personal cards. What they did not ask: **who decides the delivery date at checkout**, and **which catalogue file was sent to the chatbot vendor**. You will want both answers soon.

## Watch out

- **"No" without a reason or a date.** It reads as "marketing doesn't matter". Every exclusion gets a reason from the objective and a review date.
- **"Yes" to stay liked.** Each accepted idea takes days you promised elsewhere. If the sponsor didn't decide it, it is not in scope.
- **A boundary that lives in your head.** Unwritten boundaries move every time someone senior asks. Write it, get it acknowledged, date it.
- **Treating every refinement as a change request.** If the five questions all say yes, just do it; a form for every small improvement makes you the bureaucrat people route around.
- **"Phase one and a half".** Inventing a half-phase to avoid saying "not now" creates a commitment nobody resourced. Promise only what you can: "your use case will be in that discussion".
- **Requests that disappear.** The fastest way to lose a requester's trust is a request that was never answered. The log is public; every line has a status.
- **Forgetting whose decision it is.** Items in the CEO's area need the CEO's sight, even if your sponsor agrees.

## Your turn

### Inputs

- Persona: [Noa Levi, Marketing Director](../../labs/common/harbor-and-pine/personas/noa-marketing.md) (paste the prompt into a new chat without reading it first). No roleplay: the [pre-run transcript](../../labs/common/harbor-and-pine/personas/transcripts/noa-marketing.md).
- Coach: [coach prompt](../../labs/common/coach-prompt.md) with Noa's "After the interview" checklist.
- Your charter from 01.2; `company/org-chart.md`; `it/saas-list.csv` (who owns StoreHub, MailPost, Canva).
- Templates: [scope boundary](../../templates/scope-boundary.md), [change request](../../templates/change-request.md); the log as a spreadsheet: `labs/module-01/change-request-log.csv` in the module download.

### Steps

1. Write the scope test (Step 1) in one sentence.
2. Interview Noa for 20 minutes to agree the scope of phase one for marketing. Log every idea she raises. Try to find out which AI tools her team uses, who decides the checkout delivery date, and which catalogue file went to the vendor.
3. Run the coach on your transcript.
4. Write the scope boundary: at least eight lines, each with in / out / read-only and a reason.
5. Fill the change-request log with every request Noa made, and one full change-request form for the website translation.
6. Write the two-line acknowledgement request you send to Michal (copy Noa and Yoav).

### Time

60 minutes.

### Done when

- [ ] The scope test is one sentence the sponsor could sign.
- [ ] Every boundary line has a reason taken from the objective or a finding, and every "out" has a review date.
- [ ] Each of Noa's requests is in the log with refinement/expansion, decision, reason and review date.
- [ ] The full change request names what it would displace and who decides.
- [ ] The acknowledgement goes to the sponsor and, for marketing lines, to Noa with Yoav in copy.
- [ ] You found out at least one of: marketing's AI tools and how they are paid; who sets the checkout date; which catalogue file the vendor received.

<details><summary>Reference answer</summary>

**Scope test.** As in Step 1.

**Scope boundary, phase 1 (to 28 January 2027).**

| Item | Status | Reason |
|---|---|---|
| Customer-service contacts (email, web form, phone): volumes, causes, handling cost | In | The objective |
| Shadow AI and AI inside SaaS, company-wide | In | Risk now: customer data may be in free tools |
| Interim AI rule, one approved tool, AI inventory | In | Risk now |
| Exports and baselines: Deskly, CloudVoice, Priority orders, logistics tracking | In | Needed to measure |
| Delivery-date promise at checkout (StoreHub lead-time table) | Read-only | Likely driver of contacts; owned by marketing, changes decided by Noa and Yoav |
| Marketing's AI use (CopyGenie, ChatGPT Plus, StoreHub descriptions, MailPost, Canva) | In for census and inventory only | Risk now; not a delivery project |
| Sales chatbot, AI emails, AI images, room designer, website translation | Out, request list | Not support contacts or cost; review February 2027 |
| Vendor selection, contracts | Out | No commitments before the evidence (sponsor's rule) |
| Headcount decisions | Out | CEO, HR and the labour lawyer |
| Showrooms and B2B sales processes | Out, except contacts that reach support | Outside the sponsor's line; revisit in phase 2 |

**Change-request log:** CR-01 to CR-06 as in the Step 7 table.

**Full change request — CR-05, website translation into Arabic and Russian.** Requester: Noa Levi, 5 Nov 2026. Problem behind it: Arabic- and Russian-speaking customers are poorly served online; Noa believes a large market is missed. Who benefits: those customers, marketing (conversion), possibly support (fewer clarifying contacts). Link to objective: indirect — the helpdesk's auto-detected language field marks 12.9% of tickets Arabic and 11.7% Russian (a field to be checked in 02.5); unknown how many contacts are caused by language. Size: content for ~250 SKUs and all site pages, StoreHub configuration, legal review of terms and privacy notice in two languages; weeks, not days. Displaces: the support-language work in the pilot, if done in phase 1. Refinement or expansion: expansion (new deliverable, system, legal work). Assessment: not phase 1; measure in discovery how many Arabic and Russian contacts a translated site would prevent. Recommendation: "not now, review February 2027 with the contact data", sent to Noa with the log on 6 November. Decision: Michal and Yoav at the monthly review on 10 December; Noa told by email the next day.

**Acknowledgement request.** "Michal — attached the phase-1 scope boundary (one page) and the request log. Please reply 'agreed' or correct; Noa and Yoav copied for the marketing lines. Next review of the request list: 10 December."

**What a stronger interview adds.** Asked who decides the delivery date at checkout, Noa admits, defensively, that marketing set the lead-time table in StoreHub in February 2023 (42 days Vietnam, 38 China, 21 Turkey, 28 Italy) and refused Tamar's 2024 request to add a week for Vietnam because "every extra week at checkout costs us about 4% of orders" — her own estimate, never tested. The data room confirms the table: `orders/storehub-delivery-settings.csv`, last modified 14 February 2023 by noa.levi. Asked which file went to ChatNest, she says it was "products 2023" from the shared drive and she never checked whether it was current. Both go into your notes, not into her scope.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 1, "Framing and Scoping the Engagement" (objective → scope → boundary; refinement vs expansion — named, not re-taught).
- Persona and transcript: [Noa Levi](../../labs/common/harbor-and-pine/personas/noa-marketing.md), [transcript](../../labs/common/harbor-and-pine/personas/transcripts/noa-marketing.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [scope boundary](../../templates/scope-boundary.md), [change request](../../templates/change-request.md).
- Previous: [01.2 · Getting a real mandate](lesson-02.md). Next: [01.4 · The first-week plan and the 30-60-90](lesson-04.md).
