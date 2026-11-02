---
id: "03.2"
module: 3
minutes: 18
practice_minutes: 70
prerequisites: ["03.1"]
objectives:
  - "Map a candidate workflow step by step from the data room, with the owner, system and trigger of each step."
  - "Simplify the workflow before choosing any technology, and name the steps the change removes."
  - "Decide per step between plain automation, generation, an agent and a person, and justify each choice."
  - "Write an agentic opportunity frame: who builds it, what it connects to with which permissions, who checks it, and the upkeep it creates."
volatility: implementation
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 4, Design AI Transformation Roadmaps (workflow and agent opportunities)"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "n8n Docs — Schedule Trigger node"
    url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/
  - title: "Zendesk Help — Adding WhatsApp channels to the Agent Workspace"
    url: https://support.zendesk.com/hc/en-us/articles/4408842821786-Adding-WhatsApp-channels-to-the-Agent-Workspace
  - title: "Meta for Developers — WhatsApp Business Platform, template fundamentals"
    url: https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview
last_verified: "2026-11-02"
---

# 03.2 · Agent or not

"Use an AI agent" has become the default answer to every workflow question, and it is usually the wrong one. Most steps in a real workflow are rules that ordinary automation already handles, a few need a model to read or write language, and very few need software that chooses its own next step. In this lesson you map a Harbor & Pine workflow step by step, simplify it, decide per step what should do it, and write the result as an agentic opportunity frame. One of the two candidates you frame ends as "plain automation, no AI", and that is the most valuable result in the module.

## The situation

Thursday 19 November 2026. Your opportunity map ([03.1](lesson-01.md)) has fifteen rows. Before you screen and score them, the two biggest need a closer look, because their shape decides their cost and their risk. Row 1 (tell customers before the promised date passes) came from discovery. Row 3 (draft replies for agents) came from the support team and from the free ChatGPT use you found in module 1. Yoav, meanwhile, has forwarded you a LinkedIn post titled "Agents will run your customer service in 2027" with the comment "this is what I want".

IBM's roadmap course frames this as intervention fit and the "agentic surface": map first, simplify, match each step to rules, prediction, generation or an agent, and keep agents only for the steps that need judgment. Here you do it on Harbor & Pine's real files.

## What to do

### Step 1 — Map the workflow as it runs today, from the data

Walk one case end to end, then confirm every step against a file or a person. For "where is my order?" the files tell the story without anyone's opinion:

| # | Step today | Who / system | Trigger | Evidence |
|---|---|---|---|---|
| 1 | Customer orders; checkout shows a promised date = order date + a fixed lead time per supplier country (Vietnam 42 days, China 38, Turkey 21, Italy 28) | StoreHub, set by marketing | Order placed | `orders/storehub-delivery-settings.csv` (last changed 14 Feb 2023 by noa.levi) |
| 2 | Purchasing puts the container number on the order line | Priority, purchasing | Order allocated | `orders/orders.csv` (`container_no`) |
| 3 | The forwarder sends ETA changes by email and in a weekly portal export | Gal-Ship | Vessel delay | `orders/shipments.csv` (original, revised, latest ETA) |
| 4 | Tamar copies ETA changes into her own sheet, twice a week | Logistics, Google Sheet | Email arrives | `orders/logistics-eta-tracking.csv` |
| 5 | Nothing else happens: the order's promised date and the customer are never updated | — | — | Tamar: "They go into my sheet. That's it." |
| 6 | The promised date passes; the customer writes or calls | Customer → WhatsApp, email, phone | Date passed | WISMO tickets cluster a median 12 days after the container's original ETA |
| 7 | The agent sends the order-status saved reply, which repeats the original promised date | Deskly macro | Ticket | `support/emails.csv` (e.g. EM-32586, June) |
| 8 | The agent emails logistics to ask; an import coordinator answers | logistics@ mailbox | Customer chases | 187 emails from Customer Service in Jul–Sep (`documents/internal-emails-logistics-mailbox.md`) |
| 9 | The agent replies again; about one customer in four writes again within 14 days | Agent | Answer from logistics | Follow-up rate from your baseline (02.4) |

A process you can walk on paper like this, with an owner and a trigger on every step, is a candidate. If step 4 or 5 had been "somebody probably tells them", you would not be ready to decide anything.

### Step 2 — Simplify before you choose any technology

Ask of every step: does it need to exist? Steps 7, 8 and 9 exist only because step 5 does nothing. Fix step 5 and they shrink or vanish; automating them (a bot that answers step 6 faster, a tool that drafts step 8's email) would make waste faster.

Then ask where the truth lives. There are two ETA sources: the forwarder's weekly export (complete, but up to a week old) and Tamar's sheet (updated twice a week from emails, but kept by hand, with mixed date formats, two containers entered twice, a few never entered and one number typed with a space). Simplifying means choosing one, fixing its format, and checking it against the other, not building something clever that reads both.

The simplified workflow: (a) correct the lead-time table so new promises are realistic; (b) once a day, compare each open order's promised date with the latest ETA of its container plus the usual time to the customer; (c) when the promise will be missed, send the customer the new date before they ask and record it on the order; (d) give Tamar a short daily list of exceptions (orders with no container, containers missing from the sheet, mismatches with the forwarder's export).

### Step 3 — Decide per step: plain automation, generation, agent or person

Four kinds of worker, chosen by how much judgment the step needs and how often it recurs:

| Kind | Use it when | Not when |
|---|---|---|
| **Plain automation** (rules, integrations, scheduled jobs) | The rule can be written down and checked: compare, look up, copy, send a fixed text | The input is free language that no rule can read |
| **Generation** (a model reads or writes language) | Reading a free-text message, drafting text that varies with the case, translating | A fact (a price, a date, a policy) could come from a system instead |
| **Agent** (a model that chooses its next step and tool) | A goal pursued across several steps where the next step depends on what the last one found, the actions are reversible, and every decision point has a named owner | The order of steps is fixed; any step acts on customers or money without a person |
| **Person** | Judgment with consequences, exceptions, accountability | The step is pure copying |

For the date workflow:

| Step | Kind | Why |
|---|---|---|
| (a) Correct the lead-time table | Person (Noa decides), then a one-off setting | A business decision about what to promise; Tamar asked for it in 2024 and it was refused |
| (b) Daily comparison | Plain automation | The rule is "latest ETA + customs, warehouse and booking time (about 7 days) later than the promised date" |
| (c) Notify the customer | Plain automation with fixed texts in Hebrew, Arabic, Russian and English, written once by people and approved by Samir | The message is the same for every customer except the date and order number; a model would add risk and nothing else |
| (d) Exceptions list | Plain automation, read by a person (Tamar) | The judgment is in fixing the sheet, not in finding the gaps |

Result: **plain automation, no AI.** The only step where a model could do something is reading ETAs out of the forwarder's emails, and simplification removed it: the export and the sheet already hold them.

### Step 4 — Name who builds it, what it connects to and who checks it

A frame without these is a wish. For the date workflow:

- **Builder:** Avi (IT) with the outside service provider, or the company's Priority partner. Tamar's estimate is "a week of someone who knows Priority". A workflow tool can run it: n8n's Schedule Trigger, for example, runs a workflow every N days at a set time or on a cron expression (checked on n8n's documentation, 2 November 2026); a scheduled script on the Priority side works as well.
- **Connections and permissions:** Priority orders (read; write only the revised-date field), Tamar's sheet (read), the forwarder's export (read), company email (send, from a no-reply address with the four approved texts only), StoreHub (one setting, changed by Noa).
- **Checks:** a dry run for two weeks that sends every notice to an internal mailbox Samir reads; Tamar's daily exceptions list; a weekly count of notices sent and WISMO contacts received.
- **Upkeep and residue:** Tamar keeps the sheet in a fixed format (dates as dates, one row per container, numbers without spaces), about an hour a week. When the forwarder changes its export format, the job breaks loudly, not silently. This residue goes on the ledger line.

Why email and not WhatsApp, where most customers write? A business message sent to a WhatsApp user outside an open customer-service window must be an approved template (Meta's WhatsApp Business Platform documentation, checked 2 November 2026). That is possible, but it adds an approval step and depends on routing WhatsApp into the helpdesk first. Start with email; add WhatsApp templates in the second phase.

### Step 5 — When an agent would be right

So that "no agent" is a reasoned answer rather than a prejudice, write down what would change it. An agent earns its place when a goal needs several steps whose order depends on what each step finds (check the forwarder's portal; if silent, read the latest email thread; if the container is at port, ask customs status; then decide whom to tell), when the steps recur often enough to be worth it, when every action is reversible or held for a person, and when each decision point has an owner. At Harbor & Pine none of today's candidates has that shape. Several narrow automations and one generation step each cost less, fail more visibly and can be switched off one at a time.

## Watch out

- **Framing the tool before the workflow.** "Where could an agent help?" produces agents. "What are the steps, and which ones need to exist?" produces a cheaper answer. Map first.
- **Automating waste.** A faster reply to a question that should never have been asked (step 6) is still waste. Look for the upstream step that creates the volume.
- **A model doing a lookup.** Prices, dates, stock and policy terms come from systems. Let the model write around them, never produce them. In the B2B quote trial a model wrote the prices itself and got 4% of them wrong.
- **Two sources of truth, silently merged.** Pick the system of record, fix its format, and check it against the other. Record the choice in the frame.
- **Forgetting the residue.** People reformatting their work so a job can read it is real work with a cost; put it on the ledger line and agree it with the person (Tamar), not about them.
- **"No AI" sounding like failure.** In front of a CEO who wants AI, "plain automation" can feel like bad news. Frame it as the fastest result and as what makes any later AI honest: a bot or a draft that quotes the updated ETA is right; one that quotes the old promise is not.

## Your turn

### Inputs

- Your opportunity map from [03.1](lesson-01.md), rows 3 (reply drafts) and 5 (B2B quotes).
- Data room (in the module download, `labs/common/harbor-and-pine/`): `support/emails.csv`, `support/tickets.csv`, `support/whatsapp-week-tally.csv`, `orders/orders.csv`, `orders/logistics-eta-tracking.csv`, `company/customer-service-handbook.md`, `vendors/deskly-ai-addon-terms.md`.
- Personas, if you want to check a step: [Tamar Shalev](../../labs/common/harbor-and-pine/personas/tamar-logistics.md) (logistics), [Olga Petrenko](../../labs/common/harbor-and-pine/personas/olga-support-agent.md) (support). Feedback: [coach prompt](../../labs/common/coach-prompt.md).
- Template: [agentic opportunity frame](../../templates/agentic-opportunity-frame.md).

### Steps

1. Map the reply workflow for a written contact as it runs today (WhatsApp and helpdesk), at least seven steps, each with owner, system, trigger and evidence.
2. Simplify: name the steps that should not exist or that another fix removes.
3. Decide per step: plain automation, generation, agent or person, with the reason.
4. Write the frame: builder, connections with permissions, checks, upkeep and residue, and what would make you choose an agent.
5. Do the same, shorter, for B2B quotes.
6. Write one sentence for each candidate that you could say to Yoav.

### Time

70 minutes: 30 for the reply workflow, 20 for quotes, 20 to write the frames.

### Done when

- [ ] Each step in the maps has an owner, a system and a trigger, and at least half cite a file.
- [ ] The simplification names at least two steps that are removed or replaced by a non-AI fix.
- [ ] Every price, date or policy fact in the new workflow comes from a system, not from a model.
- [ ] Each frame lists connections with the permission (read, write draft, send) and says who checks each output.
- [ ] Each frame says why it is or is not an agent.
- [ ] The residue and upkeep are named with an owner.

<details><summary>Reference answer</summary>

**Frame A — reply drafts for written contacts (Harbor & Pine, 19 Nov 2026)**

*Today:* (1) a customer writes on one of four shared WhatsApp phones or by email/web form; (2) WhatsApp stays on the phone, email becomes a Deskly ticket; (3) the agent reads, often finds the order by asking the customer for the number; (4) for WISMO, uses the macro with the old date or emails logistics; (5) writes the reply; until the interim rule of 12 November, Russian and Arabic replies were often drafted in free ChatGPT with the customer's name and address pasted in (`support/emails.csv` shows chatbot traces in six replies), and since then a careful Russian reply takes about 13 minutes instead of 5; (6) sets "resolved" on sending; (7) the customer writes again in about a quarter of cases with an order.

*Simplify:* route WhatsApp into the helpdesk so every contact is a ticket (a plain integration; real helpdesks do this through the WhatsApp Business Platform, for example Zendesk requires an approved WhatsApp Business Account and a number that is moved off the mobile app, as its help page says, checked 2 Nov 2026); let the date fix remove most step-4 chasing; give agents an approved tool so the free-chatbot workaround does not return (module 4).

*Per step:*

| Step | Kind | Note |
|---|---|---|
| Message arrives as a ticket (all channels) | Plain automation | Prerequisite integration |
| Suggest merging duplicates (same customer within 60 minutes) | Plain automation | Rule from finding 6 |
| Detect language and topic | Generation (classification) | The auto-detected language field is wrong or blank in about 8% of tickets |
| Look up the order, status and latest ETA | Plain automation | From Priority and the ETA data, never from the model |
| Draft the reply in the customer's language, with the looked-up facts and the relevant policy text | Generation | The only step that writes |
| Review, edit and send | Person (agent) | Customer's message, order and ETA shown beside the draft |
| Log accepted / edited / rejected | Plain automation | Feeds the evaluation (module 5) |

*Builder:* an integrator or the helpdesk's AI add-on, decided after vendor review (module 4: the Deskly add-on's terms train on customer content unless you opt out and store data in the US). *Connections:* helpdesk read and write-draft only, **no send permission**; Priority and ETA data read-only. *Checks:* the agent on every reply; Olga samples 1 in 10 Arabic and Russian replies. *Residue:* agents click accepted/edited (seconds); Olga's sampling, about 100 hours a year. *Agent?* No: the order of steps is fixed and the only consequential action, sending, stays with a person.

**Frame B — B2B quotes.** (1) Request email to an account manager → (2) extract items, quantities, address (generation) → (3) match to SKUs (generation suggests, person confirms) → (4) prices, agreed discounts, stock and lead times from Priority (plain integration; the model never writes a price) → (5) quote document from the standard template (plain) → (6) cover email draft (generation) → (7) account manager checks and sends (person). Builder: integrator; connections: mailbox read, Priority read, draft-only output. Residue: Yaniv's team keeps customer price agreements in Priority, not in their own spreadsheets. Not an agent: fixed order, a person sends.

**Frame C (the worked example) — the date fix:** plain automation, no AI, as in Steps 3–4.

**Sentences for Yoav.** Date fix: "The fastest way to fewer angry customers is a daily job that tells them the real date before they ask; it needs no AI, it can run before the board, and it makes every later bot honest." Drafts: "AI writes the first draft of every reply in the customer's language, from the real order data, and an agent sends it: faster replies, no bot talking to customers on its own." Quotes: "AI prepares the hotel quotes from the request; every price comes from Priority and an account manager sends it."

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 4 "Design AI Transformation Roadmaps", module on workflow and agent opportunities (intervention fit, agentic surface; named, not re-taught).
- n8n, [Schedule Trigger node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/) (checked 2 Nov 2026).
- Zendesk, [Adding WhatsApp channels to the Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408842821786-Adding-WhatsApp-channels-to-the-Agent-Workspace) (checked 2 Nov 2026; an example of how a real helpdesk takes in WhatsApp).
- Meta, [WhatsApp template fundamentals](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview) (checked 2 Nov 2026).
- Template: [agentic opportunity frame](../../templates/agentic-opportunity-frame.md).
- Earlier: [02.3 · Process walk and task inventory](../module-02/lesson-03.md). Next: [03.3 · The fast screen](lesson-03.md). Later: building the drafts pilot in module 5 (lesson 05.3).
