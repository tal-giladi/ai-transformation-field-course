---
id: "05.6"
module: 5
minutes: 18
practice_minutes: 75
prerequisites: ["05.5"]
objectives:
  - "Plan shadow mode on production data: what runs, what is hidden, what is compared, by whom, for how long, and what result moves it to the next stage."
  - "Write a staged release where each stage changes one thing (channel, mode, language) and has a yes/no condition to enter it."
  - "Define rollback per stage: who switches what off, how fast, and what cannot be undone."
  - "Complete a production-readiness checklist and refuse a go-live date that the checklist does not support."
volatility: implementation
sources:
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution (Coursera) — course 6 (pilot isn't scale, target operating envelope, non-compensable gates) and course 4 (last reversible moment, recoverability)"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
  - title: "NIST AI 600-1, Generative AI Profile (26 July 2024)"
    url: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
  - title: "OWASP GenAI Security Project — LLM01:2025 Prompt Injection (least privilege, human approval for privileged operations)"
    url: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
last_verified: "2026-11-02"
---

# 05.6 · Shadow mode, staged release and rollback

An offline test says the pilot works on last summer's emails. Production is a different place: new messages, a new channel, real queues, real reviewers and real customers on the other end. In this lesson you move Harbor & Pine's pilot into production without betting everything on one switch: shadow mode where the drafts run on live messages but nobody sees them, a staged release where each stage changes one thing and must earn the next, a rollback that has been rehearsed, and a production-readiness checklist that decides whether the go-live date holds. At the end you have the release plan for 1 February 2027 and a checklist with every line answered.

> [!WARNING]
> From this lesson on, the pilot touches real customers. A draft that is sent cannot be unsent. Every stage below assumes the human check of 05.5, a tested switch, and the incident runbook of lesson 07.5 ready before the first draft is shown.

## The situation

Tuesday 19 January 2027, after the steering committee. The committee approved the pilot's first stage within Michal's and Ronit's approval band, ahead of the board on 28 January, with two changes to the roadmap ([03.8](../module-03/lesson-08.md)), recorded as roadmap v1.1: Russian and Arabic drafts start with Hebrew and English instead of four weeks later, because the Russian and Arabic agents are the ones who went back to slow replies after the interim rule and would otherwise return to free chatbots; and every language gets a native-speaker spot check twice a week and its own stop rule. On Sunday 1 February the four WhatsApp numbers move into the helpdesk, so every written contact becomes a ticket for the first time. Training is 7–11 February (module 6).

IBM's leadership course warns that a pilot is not scale, and that a deployment is judged on its **target operating envelope**: which users, volume, channels, languages and autonomy, under which conditions. It also names the **last reversible moment**. Here you plan the release so that each widening of the envelope is a decision with evidence, and every step before "sent" stays reversible.

## What to do

### Step 1 — List what is new in production compared with the test

| What the offline test covered | What production adds | Where it is tested |
|---|---|---|
| Email and web form, May–October | WhatsApp: short messages, photos, voice notes, the web store's `HP-1…` order number instead of `SO26…` | Shadow mode on WhatsApp |
| Pre-date-fix messages | Customers who already had a delay email; fewer WISMO, more "you told me the 14th" | Weekly sample |
| Order context built by a script | Live lookups in Priority and the date-fix table; timeouts; orders not found | Dry run, then shadow |
| Raters at a desk | Agents between calls, in the queue, with the load rule | Staged release, timer |
| No customer sees anything | Customers receive replies | Spot audit, gate 1 (c) |

One line deserves a stop: WhatsApp customers quote the web store's order number from their confirmation text, and the mapping to the ERP's `SO26…` number exists only in the web store (finding 18). Without a lookup, a WhatsApp WISMO message gets no order context, and the draft can only ask for the order number, which the customer believes they already gave. Either the integration looks the number up in the web store, or WhatsApp WISMO drafts stay off. That is a production-readiness line, not a prompt fix.

### Step 2 — Plan shadow mode for what the test did not cover

Shadow mode runs the pilot on live messages and hides the output. Nothing changes for agents or customers; you get a measurement on the real stream.

- **What runs:** for every WhatsApp ticket from 1 February, the pilot produces category, flags and a draft, stored in a hidden field. Agents answer as they do today.
- **What is compared:** each day, Olga (Hebrew, Russian) and Lina (Arabic) take 30 WhatsApp tickets at random and rate the hidden draft against what the agent actually sent, with the 05.4 rubric, including whether the draft would have been safe to send.
- **What else is measured:** how many WhatsApp messages have no text (voice notes, photos only) and therefore no draft; how many have an order context; how many flags are raised.
- **How long:** two weeks (1–14 February), about 300 rated WhatsApp drafts.
- **Exit condition (yes/no):** acceptance at least 75% on WhatsApp drafts in each of Hebrew, Arabic and Russian with at least 50 rated per language; no safety issue that the negative tests did not already cover; the web-store order lookup returns an order for at least 90% of WhatsApp messages that quote an `HP-1…` number. Otherwise: stay in shadow, fix, two more weeks.

Shadow mode costs tokens and Olga's and Lina's time (about 30 ratings a day, 45 minutes), and nothing else. That is why it is the right place to learn about a new channel.

### Step 3 — Write the staged release: one change per stage

Each stage widens the envelope in one direction only, so that when something goes wrong you know which change caused it.

| Stage | From | What changes | Entry condition (yes/no) | Owner |
|---|---|---|---|---|
| 0. Offline replay | Dec–Jan | Test set and negative tests | Eval report: proceed (05.4) | Pilot lead |
| 1. On demand, email and web form | Sun 1 Feb | Agents can ask for a draft in the side panel; they insert it, edit it, send it. All four languages, language routing, 10% holdout | Readiness checklist complete; switch tested on 28 January; negative tests 24/24 on the production prompt | Samir |
| 1W. Shadow, WhatsApp | Sun 1 Feb | Drafts generated and hidden | WhatsApp routed into the helpdesk | Pilot lead |
| 2. On demand, WhatsApp | Sun 15 Feb (earliest) | WhatsApp drafts available in the panel | Shadow exit condition met | Samir |
| 3. Pre-filled drafts for two categories | After gate 1 (1 April) | WISMO and invoice drafts appear in the reply box without a click | Gate 1 met; those categories ≥ 85% accepted for four weeks; discard rate not falling towards zero | Samir, steering committee |
| — Never in this pilot | — | Sending without an agent | A new charter, a new eval, a new decision | — |

Stage 3 is a real increase in autonomy even though a person still sends: a pre-filled draft is easier to stamp than one you asked for. That is why it waits for gate 1, applies only where acceptance is high, and watches the discard rate (a falling discard rate with steady acceptance is the sign of stamping, 05.5).

### Step 4 — Define rollback per stage, and what cannot be rolled back

| Rollback | Who | How fast | Rehearsed |
|---|---|---|---|
| Drafts off for one channel or language | Samir or the pilot lead, in the helpdesk settings | Under a minute; new tickets get no draft | 28 January dry run |
| All drafts off | Samir, the pilot lead or Avi | Under a minute | 28 January dry run |
| Prompt back to the previous version | Pilot lead | Minutes (versions are kept; 05.7) | Before stage 1 |
| Model back to the previous pinned version | Pilot lead, Avi | Minutes, while the provider still serves it | Checked against the provider's retirement dates (05.7) |
| Stage 3 back to on demand | Samir | A setting | Before stage 3 |

What no switch undoes: **a reply already sent**. The last reversible moment is the agent's send button. For a wrong reply that went out, the fix is a correction to the customer, written by a person, and the incident runbook (lesson 07.5) decides who writes it, how fast, and whether the DPO must be told. Write that sentence into the release plan, so nobody believes "rollback" covers it.

### Step 5 — Fill the production-readiness checklist

The [production-readiness checklist](../../templates/production-readiness-checklist.md) has a line for everything that must be true before stage 1, each with evidence and an owner. Harbor & Pine's first pass on 20 January found four open lines:

| Area | Line | Status on 20 Jan | Owner, due |
|---|---|---|---|
| Evidence | Eval report: proceed; negative tests 24/24 on the production prompt version | Done (v1.3) | Pilot lead |
| Privacy | Counsel's answer on using past messages and on live processing (R-11); DPIA (04.4) signed; privacy notice updated (marking, 05.5) | **Open**: counsel's answer arrived 15 January (yes, pseudonymised, inside the approved tool); privacy notice update not yet published | Ronit, 29 Jan |
| Data boundary | Only the order context line and the message text reach the model; no payment, ID or health data (masked before the call) | Done | Avi |
| Security | Helpdesk: write drafts only, no send, no close; Priority: read only; keys in the integrator's vault; prompt-injection tests passed | Done | Avi |
| Integration | Switch per channel and language; load rule; holdout 10%; timeout 10 seconds → no draft, the agent writes as today | **Open**: load rule not built | Integrator, 28 Jan |
| WhatsApp | Web-store order lookup for `HP-1…` numbers | **Open**: StoreHub export access requested | Noa, Avi, 12 Feb |
| Review | Source beside the draft; "check these" lists; language routing; spot audit staffed | Done | Samir |
| Logging and monitoring | Logging spec and monitoring live (05.7); cost alert set | **Open**: 05.7 | Pilot lead, 29 Jan |
| People | Training booked 7–11 Feb; until then, drafts on demand only for the eight agents in the 28 January walkthrough | Done | Samir |
| Operations | Owner, business-hours support from the integrator, runbook, rollback rehearsed | Done (rehearsal 28 Jan) | Samir, Avi |

The checklist does not move the date; it decides whether the date holds. If the load rule or the logging is not live on 29 January, stage 1 starts with drafts for the eight trained agents only, or a week later. Write that consequence next to the open lines before anyone asks.

## Watch out

- **Switching on everything at once.** A wrong result after a big-bang release cannot be traced to a cause. One change per stage.
- **Shadow mode nobody looks at.** Hidden drafts that are never compared with what agents sent are just a token bill. Name the raters, the daily sample and the exit condition.
- **"Rollback" that only means the software.** The reply already sent is the part that matters to the customer. Plan the correction message and the runbook.
- **A readiness checklist filled in after go-live.** Its job is to stop the date. Fill it a week before, with owners and dates on the open lines.
- **Autonomy creeping in through convenience.** Pre-filling a draft, auto-applying a category or auto-closing a ticket are each a step up the ladder. Each needs its own condition.
- **A roadmap change made silently.** The committee moved Russian and Arabic forward; the roadmap's version and the reason change with it, and the stop rules per language carry the risk.

## Your turn

### Inputs

- Your charter ([05.1](lesson-01.md)), eval report ([05.4](lesson-04.md)) and human-review design ([05.5](lesson-05.md)); the roadmap from [03.8](../module-03/lesson-08.md).
- Data room (module download): `support/whatsapp-week-tally.csv` (WhatsApp volume, languages, order numbers), `vendors/deskly-ai-addon-terms.md` (for comparison: what the helpdesk's own AI add-on would switch on), `company/customer-service-handbook.md`.
- Template: [production-readiness checklist](../../templates/production-readiness-checklist.md).

### Steps

1. List what production adds to what the test covered (at least five lines), and mark any line that blocks a stage.
2. Plan shadow mode for WhatsApp: what runs, who compares, the daily sample, the length and the yes/no exit condition. Use the tally to estimate how many WhatsApp tickets a day arrive in each language and how many quote an `HP-1…` number.
3. Write the staged release table: each stage changes one thing and has an entry condition and an owner.
4. Write the rollback table, including the sentence about replies already sent.
5. Fill the production-readiness checklist for 1 February, with owners and dates on every open line and the consequence for the date.

### Time

75 minutes: 15 for what is new, 15 for shadow mode, 15 for the stages, 10 for rollback, 20 for the checklist.

### Done when

- [ ] Every difference between test and production is either tested in shadow mode, covered by a stage condition, or a readiness line.
- [ ] Shadow mode has named raters, a daily sample, a length and a yes/no exit condition.
- [ ] Each stage changes one thing and has an entry condition and an owner; no stage sends without a person.
- [ ] Rollback names who, how fast and when it was rehearsed, and says what cannot be undone.
- [ ] Every open readiness line has an owner, a date and a stated consequence for the go-live.

<details><summary>Reference answer</summary>

**Release plan — reply drafts — v1.0, 20 January 2027** (owner: Samir Haddad; author: pilot lead; approved: steering committee, 19 January; roadmap v1.1)

*What production adds:* WhatsApp (shorter messages, photos and voice notes with no text, `HP-1…` order numbers that match no ERP order without a web-store lookup); post-date-fix customers; live lookups with timeouts; real reviewers under load; customers receiving replies. Blocking: the web-store lookup blocks WhatsApp WISMO drafts (stage 2); the load rule blocks stage 1 for more than the eight trained agents.

*WhatsApp shadow (1–14 February):* from the one-week tally (630 conversations in five days, mostly Hebrew, with Russian and Arabic each a substantial minority), about 120 WhatsApp tickets a working day; Olga and Lina rate 30 a day (Hebrew, Russian, Arabic) against what was sent, about 300 in two weeks. Order numbers: the tally records one on 39.4% of conversations, none of them in the ERP format, so the lookup is tested on all of them. Exit: ≥ 75% accepted per language with ≥ 50 rated each; no new kind of safety issue; lookup success ≥ 90%.

*Stages:* as in Step 3. Stage 1 on Sunday 1 February for email and web form in four languages, drafts on demand, holdout 10%; stage 2 no earlier than 15 February; stage 3 only after gate 1 and only for WISMO and invoice; sending without an agent is out of this pilot.

*Rollback:* as in Step 4; rehearsed 28 January (drafts off for Arabic in 40 seconds; all off in under a minute; prompt v1.2 restored in five minutes). "A reply already sent cannot be rolled back: a wrong reply that reached a customer is corrected by a person under the incident runbook."

*Readiness on 29 January (second pass):* privacy notice published 27 January; load rule live 28 January; logging and monitoring live 29 January (05.7); web-store lookup still open (due 12 February). Decision: stage 1 goes ahead on 1 February for all agents with drafts on demand; stage 2 waits for the lookup, so WhatsApp WISMO drafts stay off until it works even if the shadow exit is met for other categories.

*What the usage export will later show (module 6):* drafts inserted from the first day of February by agents in all four languages, the heaviest user the Russian-speaking team lead; and, within weeks, three agents who stop inserting drafts while still opening the panel. The release plan's job ends where the adoption work of module 6 begins.

</details>

## References

- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 6 (pilot isn't scale, target operating envelope, gates) and course 4 (last reversible moment); named, not re-taught.
- NIST, [AI 600-1 Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) (deployment and monitoring actions for generative AI).
- OWASP GenAI Security Project, [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) (least privilege; human approval for privileged operations).
- Template: [production-readiness checklist](../../templates/production-readiness-checklist.md). Module 4: [DPIA for AI](../../templates/dpia-for-ai.md), [risk register](../../templates/risk-register.md).
- Earlier: [03.8 · The roadmap](../module-03/lesson-08.md), [05.5 · Human-in-the-loop design](lesson-05.md). Next: [05.7 · Before launch](lesson-07.md). Later: the adoption dashboard (lesson 06.4) and the incident tabletop (07.5).
