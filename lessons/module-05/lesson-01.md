---
id: "05.1"
module: 5
minutes: 18
practice_minutes: 90
prerequisites: ["03.9"]
objectives:
  - "Write a pilot charter whose hypothesis, scope, thresholds and stop rules can each be answered yes or no, and whose thresholds match the business case's gates."
  - "Write a rule of use: what the AI output may decide, who may override it, and how every override is logged."
  - "Design a value measurement plan with an indicator the budget owner already reviews, a baseline taken with the same instrument as every later reading, a quality metric paired with every efficiency metric, and a counterfactual."
  - "Decide how long the pilot must run, and what share of use must be reached, before its value numbers are read."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 1, The AI Transformation Advisor (rule of use); course 5, AI Business Cases and ROI Models (value metrics)"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution Professional Certificate (Coursera) — course 6, Measure AI Value and Scaling Transformation (credible counterfactual, pilot isn't scale)"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-02"
---

# 05.1 · The pilot charter

A pilot without a charter becomes a demo that never ends: nobody agreed what it was meant to prove, so every result can be read as success, and nobody can stop it without losing face. In this lesson you write the charter for Harbor & Pine's reply-drafts pilot before anything is built: the hypothesis in one sentence, what is in and out, the thresholds that decide gate 1, the rules that stop it early, the owner, and the rule of use that says what the AI may and may not decide. Then you write the value measurement plan that tells Ronit, in April, whether the hours were real. At the end you have both documents, signed by Michal and Samir.

## The situation

Monday 7 December 2026. The scoring workshop chose reply drafts as one of three bets, the ROI model is in progress ([03.7](../module-03/lesson-07.md)) and the alignment session is on Thursday. The time study runs from 6 to 17 December ([02.4](../module-02/lesson-04.md)), the test set has to be built this month ([05.2](lesson-02.md)), and the board decides on 28 January ([03.9](../module-03/lesson-09.md)). If you start building without a charter, three things will happen: the gates in the business case and the pilot's own success criteria will drift apart; Samir will hear "pilot" as "the first step of the 40% cut"; and in April nobody will be able to say whether the hours saved were caused by the drafts or by the date fix that went live in January.

Two IBM ideas meet here. The consulting certificate's **rule of use** (what the output may decide, who may override, how the override is recorded) is one of the three foundations of any AI deployment. The leadership certificate's **credible counterfactual** and **"pilot isn't scale"** say that a pilot's numbers mean something only against what would have happened without it, under conditions like the real ones. Here you write both into documents a team can run.

## What to do

### Step 1 — Write the hypothesis as one falsifiable sentence

A hypothesis names the change, the population, the effect, the guardrail and the decision it feeds. Test it by asking: "what result would make us say no?" If nothing would, it is a slogan.

> **If** support agents get an AI draft, in the customer's language, with facts from Priority and the logistics ETA, for every written contact (email and web form now, WhatsApp once it is routed into the helpdesk), **then** the median agent time per written contact falls enough to free at least 109 hours a month at peak volume, **without** more wrong replies reaching customers or more repeat contacts than today, **so that** the November 2027 – January 2028 peak can run without the two seasonal temps.

Each part comes from somewhere you can point to: 109 hours from the ROI model's peak month ([03.7](../module-03/lesson-07.md), Step 2), "no more wrong replies than today" from gate 1 (c), the temps from claim 7. The charter does not invent a second set of numbers.

### Step 2 — Draw the scope with reasons

| In | Out (and why) |
|---|---|
| Triage: one category of eleven, language, flags | Sending anything without an agent (no autonomy until the error rate is measured in production) |
| A draft reply for every written contact in Hebrew, Arabic, Russian, English | Phone calls (no text; a different pilot) |
| Email and web form from 1 February; WhatsApp once it is a helpdesk channel | WhatsApp on the four shared phones (no system, no log, no data boundary) |
| "Where is my order?" drafts that quote the updated ETA from the date fix | Damage-claim decisions (no recorded outcomes yet; re-screen 4 March) |
| Read access to Priority orders and the forwarder export; write access to helpdesk drafts only | Prices, stock or lead times written by the model (they come from systems, or `[CHECK: …]`) |
| All 14 support staff, after training (7–11 February, module 6) | B2B quotes (a separate bet with its own data precondition) |

The scope is also a promise to Samir. "Drafts for agents, agents send" is written in, and "replacing agents" is written out, in the same document Michal signs.

### Step 3 — Copy the thresholds from the gates, do not invent new ones

The charter's success thresholds are the gate-1 conditions of the business case, word for word, so the pilot team and the board look at the same four numbers on 1 April 2027:

| # | Threshold (gate 1, 1 April 2027) | Instrument |
|---|---|---|
| a | At least 80% of drafts accepted with no or light edits, on at least 400 real messages in Hebrew, Arabic, Russian and English, and at least 70% in each language | Agent's mark on each draft in the helpdesk (rule of use, Step 6), checked against a weekly sample |
| b | Median review time 2.5 minutes or less | Helpdesk timer from opening the draft to sending, on all drafted tickets |
| c | Wrong replies reaching customers no higher than today's measured rate | Weekly sample of sent replies, scored with the same sheet used to measure "today" in 05.4 |
| d | Measured net hours from the pilot at peak volume, plus the date fix's measured reduction in WISMO hours, cover at least 320 hours a month (one temp covered at 160) | Minutes per contact × volume, from the value measurement plan below |

Before the board, the offline evaluation on the 400-message test set ([05.4](lesson-04.md)) gives the first reading of (a) and (c). It is **directional**: real messages, but no real reviewer under real load. Only the production readings in February and March count for the gate.

### Step 4 — Write stop rules before you need them

A stop rule says what ends the pilot, or part of it, early, and who decides. Written in December, it is a design decision; invented in March, it looks like an excuse or a cover-up.

1. **Harm.** Any reply caused by a draft that reaches a customer and discloses another person's data, promises money outside policy, or mishandles a safety report: the pilot owner or Samir switches drafts off the same day and opens the incident runbook (lesson 07.5).
2. **Quality.** Wrong replies reaching customers above today's rate in two consecutive weekly samples: that channel or language goes back to no drafts until fixed and re-tested.
3. **Language.** Acceptance below 60% in one language for two consecutive weeks: drafts off in that language; the others continue.
4. **Economics.** Median review time above 4.4 minutes, the point at which the pilot-economics model says it saves nothing: stop and redesign the review.
5. **Change.** Any change of prompt, model or category list that fails the negative tests or drops a language by more than three points on the test set is not released (lesson 05.7).
6. **Law.** If counsel answers that the past messages may not be used for this purpose (question R-11, due 15 January), the test set built from them is deleted and rebuilt from consented or fresh data before anything continues.

### Step 5 — Name one owner, and the people around them

One accountable owner, not a committee: **Samir Haddad**, because the drafts change his team's work and he decides when to switch them off. Around him: Michal (sponsor, money, the temps decision), you (pilot lead: test set, prompt, evaluation, monitoring), Avi with the integrator (connection, access, logs), Olga (labelling, native-speaker spot checks for Russian), Lina (Arabic spot checks), Ronit (the value numbers), and counsel or the DPO through Ronit (purpose, data boundary, DPIA from module 4).

### Step 6 — Write the rule of use

The rule of use is the part of the charter people will actually meet every day. Three questions, three answers:

**What may the output decide?** Nothing on its own. It *proposes* a category (the agent confirms or changes it), a draft (the agent edits and sends it, or discards it), and flags (which route the ticket to a senior agent). It never sends, never closes a ticket, never changes an order, and never sets a date, a price or an amount.

**Who may override it?** Any agent may change the category, rewrite or discard the draft, and add a flag. Only Samir or Olga may clear a `safety`, `legal_threat`, `privacy_request` or `refund_exception` flag, because clearing it means deciding that the case is routine.

**How is an override logged?** Three helpdesk fields on every drafted ticket, filled in one click: *draft used as is / edited / discarded*; for "discarded", a reason (wrong fact, wrong language or register, tone, promises something, missing information, other); and, automatically, the category the AI suggested next to the category the agent set. A cleared flag records who cleared it and why.

Two sentences go into the charter in plain words, for the team: "An override is information, not a mistake. Discarding a wrong draft is the job; sending one is the error we measure." The logged overrides are the evaluation data for gate 1 and the monitoring in 05.7, so they must be cheap to record and safe to record.

### Step 7 — Write the value measurement plan

The plan answers Ronit's question before she asks it: how will you know in April that the hours were real, and not the date fix, the post-peak drop, or wishful timing?

1. **Indicator the budget owner already reviews.** Ronit reviews the support cost line, the temp and overtime lines and the quarterly KPI report. The plan's headline indicator is the one that feeds the temps decision: *agent hours needed per month at peak volume*, computed as minutes per written contact × contacts. It lands in the temp line, which Ronit already reads.
2. **A target that can be missed.** At least 109 net hours a month at peak volume (the hypothesis), with the gate-1 thresholds (a)–(d).
3. **Baseline, same instrument as every later reading.** Minutes per written reply, by category and language, from the December time study (four volunteers, Deskly timer on every ticket, at least 30 items per task and language). Until it reports, the only figure is the Deskly timer where agents use it: median 9 minutes (Hebrew 8, Russian 10, Arabic 11) on 51% of tickets, May–October, a biased sample of agents who chose to time themselves. In February the same timer, on every drafted ticket, gives the later readings. Never compare a time-study median with a self-reported estimate.
4. **A quality metric paired with every efficiency metric.** If handling time falls because agents send drafts without reading them, a paired metric must move the wrong way and show it:
   - minutes per contact ↔ **wrong replies reaching customers** (weekly sample);
   - acceptance rate ↔ **repeat contact within 14 days** (same customer, same order; 23.4% of resolved tickets with an order today, 02.4);
   - review time ↔ **share of drafts discarded** (a review that never discards is not a review).
5. **Counterfactual.** The date fix went live in January and will cut WISMO volume whatever the drafts do, so total hours cannot be compared before and after. Three designs, from strongest to weakest, that fit a 14-person team:
   - **Random holdout:** 10% of eligible tickets, chosen at random by the integration, get no draft until gate 1. The same agents, the same weeks, the same mix: the difference in minutes per contact is the drafts' effect. Cheapest and cleanest; tell the team it exists and why.
   - **Phased rollout:** WhatsApp joins two weeks after email; for those two weeks WhatsApp contacts handled by the same agents without drafts are the comparison.
   - **Before and after per category:** minutes per contact by category and language, before (time study) and after (timer), never totals. Weakest: the peak, the new channel and learning all move at once.
   Matched teams (one group of agents with drafts, one without) do not work here: language groups of three people are too small and too different.
6. **Fidelity label.** With the holdout, the effect is **attributed**; with before-and-after only, **directional**. Say which in the gate-1 report.
7. **Adoption gate.** Value numbers are read only after drafts are inserted on at least 60% of eligible tickets for two consecutive weeks. Below that you are measuring a tool nobody uses (lesson 06.4 builds the dashboard).
8. **How long.** Two weeks of learning excluded, then six weeks of measurement before 1 April: at Harbor & Pine's February–March volume that is well over 400 drafts in each of Hebrew and Russian; Arabic and English need the whole period to pass 400 together, so the per-language threshold uses the confidence interval from 05.2, not the point estimate.
9. **Second-order measures.** Russian and Arabic replies sent in Hebrew (today 1.4% of replies, 05.4); agents' return to free chatbots (proxy log, monthly, as in 01.6); CSAT on drafted vs holdout tickets.

## Watch out

- **Thresholds that differ from the business case.** If the charter says "75% acceptance" and the board pack says "80%", whoever reads the result chooses the number that suits them. Copy the gates; change both together or neither.
- **A rule of use that only says "human in the loop".** Name what the AI may decide (nothing alone), who overrides what, and the three fields that log it. "The human checks" is not a control until 05.5 shows the human has the time, the information and the authority.
- **Stop rules written after the first bad week.** They will look like an excuse. Write them now, with an owner, and rehearse who presses the switch.
- **A baseline nobody can reproduce.** A self-reported "about 10 minutes" against a measured 6 minutes later is a fake saving. Same instrument, same definition, same population, before and after.
- **Measuring the date fix and calling it the pilot.** WISMO volume falls in January for reasons that have nothing to do with drafts. Per-contact minutes and a holdout separate the two.
- **Efficiency without its pair.** Faster replies with more repeat contacts are a cost moved to next week. Every efficiency number in the gate-1 report sits next to its quality pair.

## Your turn

### Inputs

- The ROI model and gates from [03.7](../module-03/lesson-07.md), the roadmap from [03.8](../module-03/lesson-08.md), the board ask from [03.9](../module-03/lesson-09.md), the time-study design from [02.4](../module-02/lesson-04.md).
- Data room (module download, `labs/common/harbor-and-pine/`): `support/tickets.csv` (timer, follow-ups), `company/customer-service-handbook.md` (today's routine, escalation rules), `company/finance-summary.md`.
- Persona: [Samir Haddad](../../labs/common/harbor-and-pine/personas/samir-cs-manager.md). Start the chat with: "It is 7 December 2026. We have worked together since November; you trust me. Today we agree the rules for the drafts pilot." Find out: who he wants to be able to switch it off, which flags he wants to clear himself, what he fears the logged overrides will be used for. No roleplay: read the pre-run transcript `labs/module-05/samir-rule-of-use-transcript.md` (module download). Feedback: [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [pilot charter](../../templates/pilot-charter.md) and [value measurement plan](../../templates/value-measurement-plan.md).

### Steps

1. Write the hypothesis in one sentence and test it: what result would make you say no?
2. Fill the scope table with a reason for every "out".
3. Copy gate 1 (a)–(d) into the thresholds, each with its instrument.
4. Write at least five stop rules, each with a trigger, an action and who decides.
5. Name the owner and the supporting roles.
6. Run the conversation with Samir (or read the transcript), then write the rule of use: decide, override, log.
7. Fill the value measurement plan: indicator, target, baseline, paired metrics, counterfactual with its fidelity label, adoption gate, duration, second-order measures.

### Time

90 minutes: 25 for the hypothesis, scope and thresholds, 15 for stop rules and owner, 20 for the conversation with Samir and the rule of use, 30 for the value measurement plan.

### Done when

- [ ] The hypothesis names change, population, effect, guardrail and decision, and you can say which result would falsify it.
- [ ] Every threshold is a gate-1 condition from the business case, with its instrument.
- [ ] Every stop rule has a trigger, an action and a person.
- [ ] The rule of use says what the output may decide, who may override what, and the fields that log an override.
- [ ] Every efficiency metric has a paired quality metric; the counterfactual is named with its fidelity label.
- [ ] The adoption gate and the measurement period are written down before the pilot starts.

<details><summary>Reference answer</summary>

**Pilot charter — reply drafts for written contact, Harbor & Pine — v1.0, 8 December 2026** (signed: Michal Peretz, sponsor; Samir Haddad, owner)

*Hypothesis:* as in Step 1. Falsified if, on 1 April, any of (a)–(c) fails, or if the holdout shows no difference in minutes per contact.

*Scope:* as in Step 2. Change requests through the route in [01.3](../module-01/lesson-03.md); Noa's request on 9 December to "also draft the Instagram replies" is logged as CR-07 and parked.

*Thresholds:* gate 1 (a)–(d), copied from ROI model v3; the offline test set (05.4) is a directional pre-check, not the gate.

*Stop rules:* the six in Step 4. Switch: a helpdesk setting that turns drafts off per channel and language, held by Samir and the pilot lead; tested on 28 January in a dry run.

*Owner:* Samir. Pilot lead: you. Technical: Avi and the integrator. Language checks: Olga (Russian), Lina (Arabic), Daniel (English), the pilot lead and Samir (Hebrew). Privacy: counsel through Ronit; DPIA and data boundary from module 4.

*Rule of use:* as in Step 6, including "only Samir or Olga clears a safety, legal, privacy or refund flag" and the three logging fields. Added after the conversation with Samir: "Override logs are reported per language and per week, never per agent, and are not used in performance reviews." (He agreed to the logging only with this line.)

**Value measurement plan — v1.0, 8 December 2026** (owner: pilot lead; reader: Ronit)

| Item | Entry |
|---|---|
| Indicator the budget owner reviews | Agent hours needed per month at peak volume → the temp line in the support budget |
| Target | ≥ 109 net hours a month at peak; gate 1 (a)–(d) on 1 April 2027 |
| Baseline | Time study 6–17 December, median minutes per written reply by category and language; until then the Deskly timer: median 9 min (he 8, ru 10, ar 11), 51% of tickets, self-selected |
| Later readings | Deskly timer on every drafted and holdout ticket, February–March |
| Paired quality metrics | Wrong replies reaching customers (weekly sample of 80 sent replies, 20 per language); repeat contact within 14 days (23.4% today on resolved tickets with an order); discard rate |
| Counterfactual | Random 10% holdout until gate 1 (attributed); WhatsApp's first two weeks without drafts (directional) |
| Adoption gate | Drafts inserted on ≥ 60% of eligible tickets for two consecutive weeks before value is read |
| Duration | 1–14 February excluded as learning; 15 February – 28 March measured; report 1 April |
| Second-order | Replies in the wrong language (1.4% today); free-chatbot traffic from Customer Service (proxy log, monthly); CSAT drafted vs holdout |
| Fidelity label in the gate report | Attributed (holdout) for minutes per contact; directional for the hours at peak, which multiply by a forecast volume |

**What the transcript leaves open:** the interviewer never asked Samir what happens to the holdout tickets in the peak if the team is drowning. Asked, he would want the right to end the holdout early. Write it down as a condition (Samir may end the holdout if the queue exceeds two days, and the gate report then says "directional").

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 1 (rule of use as a foundation) and course 5 (value metrics, paired quality metric, adoption gate); IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 6 (credible counterfactual, pilot isn't scale). Named, not re-taught.
- Templates: [pilot charter](../../templates/pilot-charter.md), [value measurement plan](../../templates/value-measurement-plan.md), [ROI model](../../templates/roi-model.md).
- Persona: [Samir Haddad](../../labs/common/harbor-and-pine/personas/samir-cs-manager.md); [coach prompt](../../labs/common/coach-prompt.md).
- Earlier: [03.7 · The ROI model](../module-03/lesson-07.md), [03.8 · The roadmap](../module-03/lesson-08.md), [02.4 · Measuring a baseline](../module-02/lesson-04.md). Next: [05.2 · Building the test set](lesson-02.md). Later: the adoption dashboard (lesson 06.4) and scale, fix or stop (07.2).
