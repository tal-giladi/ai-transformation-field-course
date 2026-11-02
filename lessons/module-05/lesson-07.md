---
id: "05.7"
module: 5
minutes: 20
practice_minutes: 90
prerequisites: ["05.6", "04.5"]
objectives:
  - "Write a logging spec that records, for every AI-drafted ticket, what went in, what came out, which model and prompt produced it, and what the person did with it, with the least personal data and a retention decided with the DPO."
  - "Write a monitoring spec: each signal with an indicator, a threshold, a cadence, an owner and a response, including sampled output review, eval re-runs on model change, and cost alerts."
  - "Write change control for prompts, models, providers and vendor settings: what counts as a change, how it is tested, who approves it, and how it is rolled back."
volatility: implementation
sources:
  - title: "Anthropic — Model deprecations (lifecycle, at least 60 days' notice before retirement for publicly released models, API parameter deprecations; checked 2 Nov 2026)"
    url: https://platform.claude.com/docs/en/about-claude/model-deprecations
  - title: "Anthropic — Models overview (every Claude model ID is a pinned snapshot; checked 2 Nov 2026)"
    url: https://platform.claude.com/docs/en/about-claude/models/overview
  - title: "Shibolet & Co. — The Privacy Protection Authority's guide to regulation 10(d) of the Privacy Protection (Data Security) Regulations: keeping documentation files and logs (Hebrew; guide of 29 Sep 2024)"
    url: https://www.shibolet.com/מדריך-פעולה-של-הרשות-להגנת-הפרטיות-ליי/
  - title: "NIST AI 600-1, Generative AI Profile (26 July 2024)"
    url: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution (Coursera) — course 6, Measure AI Value and Scaling Transformation (proportionate monitoring, escalation trigger vs review cadence)"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-02"
---

# 05.7 · Before launch: logging, monitoring and change control

An AI pilot that worked on 1 February can be failing by April without anyone touching it: the vendor updates the model, someone edits the prompt "just a little", an admin switches on a helpdesk feature, the date-fix job changes its format, or reviewers slowly stop reading. The only defence is to decide before launch what is recorded, what is watched, how often, by whom, what happens when a number crosses a line, and how every change is tested before it goes live. In this lesson you write Harbor & Pine's logging spec, monitoring spec and change-control rules. At the end you have the three documents that let the pilot run after you stop looking at it every day.

## The situation

Wednesday 27 January 2027. The readiness checklist ([05.6](lesson-06.md)) has one open line that belongs to you: "logging spec and monitoring live (05.7), due 29 January". The pilot goes live on Sunday 1 February. Gate 1 on 1 April will be argued from what the logs show, and the steering committee will ask in May whether the pilot still works. On 15 March something will go wrong (lesson 07.5); what you write this week decides whether the team finds it in hours or hears about it from a customer.

IBM's leadership course describes **proportionate monitoring** (sized to impact, risk, volume, rate of change and speed of harm) and separates an **escalation trigger** (a threshold that sends a named person to act) from a **review cadence** (looking regularly). The consulting certificate adds that a control without a response is decoration. Here you write the triggers, cadences and responses for one pilot.

## What to do

### Step 1 — Write the logging spec: one record per drafted ticket

Log what you will need for four uses: measuring the gate, monitoring, investigating an incident, and re-running the eval on what really happened. Not more.

| Field | Example | Why |
|---|---|---|
| Ticket id, channel, received time | 38211 · whatsapp · 2027-02-03 10:14 | Join to the helpdesk; volume by channel |
| Language detected, reply language | ru · ru | Per-language monitoring |
| Category suggested / category set by agent | wismo / wismo | Triage accuracy in production |
| Flags raised; cleared by, reason | angry; Olga, "polite third message" | Escalation working; flag rules |
| Order context present; expected date given | yes · 12/02/2027 | Facts from systems; WISMO date checks |
| Prompt version; model id; provider; API version | 1.3 · `claude-sonnet-5-5` · anthropic · 2026-10-21 | Which configuration produced the draft |
| Tokens in / out; cost ₪; latency; error or timeout | 2,140 / 310 · ₪0.03 · 4.1 s · — | Cost alerts; reliability |
| Draft shown / inserted; action: as is, edited, discarded; discard reason | inserted · edited · — | Acceptance, discard rate (05.5) |
| Review seconds (open to send) | 96 | Gate 1 (b) |
| Holdout flag | no | Counterfactual (05.1) |
| Sent reply id | 38211-r1 | Spot audit; incident review |

What is **not** in the log: the message text and the draft text. They already live in the helpdesk, under its access rules and retention; the log points to them by ticket id. A second copy of every customer message in a log store is a second database to secure, explain and delete. Store a hash of the draft if you need to prove later which draft was shown.

Access to the systems is logged too. Under the Privacy Protection (Data Security) Regulations, 5777-2017 (תקנות הגנת הפרטיות (אבטחת מידע), התשע"ז-2017), as the Privacy Protection Authority's 2024 guide to regulation 10(d) is summarised by the law firm Shibolet, databases at a medium or high security level must document access, by people and by code components, with the user's identity, date and time, the component accessed, the type and scope of access and whether it was allowed, and keep those logs for at least 24 months. The integration's service account reading Priority and writing helpdesk drafts is such a code component. Which security level Harbor & Pine's support database has is the DPO's call (module 4); write the question down and apply the answer to both the access log and the pilot log's retention.

### Step 2 — Choose the signals, and give each a threshold, an owner and a response

A dashboard nobody acts on is not monitoring. Each signal gets five things: indicator, threshold, cadence, owner, response. Harbor & Pine's set (also in `labs/module-05/monitoring-signals.csv`, module download):

| Signal | Indicator | Threshold (trigger) | Cadence | Owner | Response |
|---|---|---|---|---|---|
| Quality | Wrong replies reaching customers in the spot audit (20 sent drafted replies per language per week) | Above today's rate two weeks running | Weekly | Olga, Lina | Segment off (stop rule 2), fix, re-test |
| Acceptance | Drafts used as is or edited lightly, per language | Below 70% two weeks running; below 60% → off | Weekly | Pilot lead | Prompt review; stop rule 3 |
| Stamping | Discard rate per language | Below 5% while acceptance is under 90% | Weekly | Samir | Audit 20 sends; refresher; check the load rule |
| Review time | Median seconds open-to-send | Over 150 s; over 264 s → stop rule 4 | Weekly | Pilot lead | Review design (05.5) |
| Escalations | Flags raised; time to clear safety flags | Any safety flag not handled the same day | Daily | Samir | Call the customer; incident review |
| Negative tests | 24+ tests, automated | Any failure | Weekly and on every change | Pilot lead | No release; if live, roll back |
| Full eval | Test set 400, same scorer | Any language down more than 3 points vs the release baseline | Monthly and on every trigger | Pilot lead | Roll back the change |
| Model lifecycle | Provider's deprecation page and e-mails | A notice for the model in use | On notice; check monthly | Avi | Migration test at least 30 days before retirement |
| Cost | Tokens and ₪ per day; ₪ per draft | Over twice the 4-week daily average, or over ₪0.10 a draft | Daily alert | Avi | Look for loops, retries, prompt growth |
| Reliability | Timeouts and errors | Over 5% of calls in a day | Daily alert | Integrator | Fix; drafts degrade to none, never to a guess |
| Value | Minutes per contact, drafted vs holdout; repeat contacts in 14 days | Holdout difference under half the planned | Monthly | Ronit, pilot lead | Re-forecast the case (07.2) |
| Vendor settings | The helpdesk's own AI add-on: Autopilot off, admin list, opt-out of training in force | Any change | Monthly audit | Avi | Revert; change-control breach |
| Shadow AI | Customer Service traffic to free chatbots (proxy log) | Rising two months running | Monthly | Avi | Ask why (01.6), not who |

Three of these need a word.

**Sampled output review** is the quality signal that machines cannot give: 80 sent replies a week read by native speakers, scored with the 05.4 rubric. Twenty per language is about ±17 points on one week's acceptance; read it as a four-week rolling figure, and act on two bad weeks in a row, not one.

**Eval re-run on a model change.** Even a pinned model changes when the provider retires it. Anthropic's documentation (checked 2 November 2026) says every Claude model ID is a pinned snapshot, that customers with active deployments get at least 60 days' notice before a publicly released model is retired, and that requests to a retired model fail. Its own table shows how it happens: Claude Sonnet 4.5 was deprecated on 30 September 2026 and retires on 30 November 2026. Request parameters change too: `temperature`, `top_p` and `top_k` were removed in API version 2026-10-21 and now return an error, so integration code that still sends them breaks on the upgrade. Other providers and helpdesk vendors may update the model behind a feature with less notice, or none (Harbor & Pine's helpdesk vendor names its model provider only behind a login). Treat every such change as a trigger for the full eval and the negative tests, before the switch, not after.

**Cost alerts** protect against the failures that do not show in quality: a retry loop, a prompt that grew, an integration that drafts every message twice. At about ₪0.03 a draft and 1,920 drafts a month, the expected bill is tens of shekels; an alert at twice the normal daily spend catches a loop on the first day. Set a monthly spending limit in the provider's console as well.

### Step 3 — Write change control

Decide what counts as a change before someone makes one "quickly":

| Class | Examples | Test before release | Approves | Release |
|---|---|---|---|---|
| Standard | Prompt text, category rules, flag rules, reply rules, the context line's fields | Development set, then test set once; negative tests all pass; no language more than 3 points down; change log entry | Samir (wording customers see), pilot lead (release) | Sunday–Wednesday mornings; not in the last week before a gate |
| Major | Model or provider, API version, a new channel, a new stage of autonomy (05.6), a new data source in the context | All of the above, plus one week of shadow on live traffic; DPIA check if data changes (module 4) | Samir and the steering committee's chair | Planned date; no go-live from November to January (peak) |
| Vendor setting | Turning on any AI feature in the helpdesk or another SaaS tool | Treated as major; intake register (module 4) | Steering committee | — |
| Emergency | Switching drafts off, rolling back to the previous version | None before; a written note within a day | Samir, pilot lead or Avi | Immediately |

Three rules make it work. **Versions:** the prompt, the category list and the context format each have a version number, and the run files and the log record them (05.3). **The previous version stays deployable:** rollback is choosing the last good version, not rewriting it. **Changes are rare and batched:** at most one standard release a week, so the monitoring can tell which change moved a number.

### Step 4 — Put it on a calendar

Monitoring that depends on someone remembering stops in the third week. Put the cadence into the team's week, with names: Sunday morning, the automated report (acceptance, discard, review time, flags, cost, errors) is in Samir's inbox; Tuesday, Olga and Lina finish the spot audit; Wednesday, a 20-minute prompt review (discard reasons, audit findings, any proposed change); Thursday, one line to the team on what changed because of their marks (05.5). Monthly: full eval re-run, value numbers to Ronit, vendor settings audit, proxy check. This weekly and monthly rhythm becomes the operating rhythm of lesson 07.6 when the pilot becomes a service.

## Watch out

- **Logging everything.** Copies of every message and draft in a new store multiply privacy risk and help nobody. Log references, decisions, versions and numbers; leave the text where it already lives.
- **Thresholds without owners.** "Alert if acceptance falls" with no name and no response is decoration. Indicator, threshold, cadence, owner, response, every time.
- **Re-running the eval after the switch.** A model change is tested before it goes live. Subscribe to the provider's deprecation notices and put the retirement dates in the calendar.
- **Unpinned models and silent vendor features.** A "latest" alias or a helpdesk add-on can change what drafts say without any change on your side. Pin what you can; audit what you cannot.
- **Prompt edits outside the process.** A "small" wording fix that drops Arabic by five points is found a month later. Every edit is a version with a test run.
- **Reading one week of 20 samples as a trend.** Use rolling figures and act on repeated signals; react the same day only to safety and privacy events.

## Your turn

### Inputs

- Your charter's stop rules ([05.1](lesson-01.md)), eval report ([05.4](lesson-04.md)), human-review design ([05.5](lesson-05.md)) and release plan ([05.6](lesson-06.md)).
- Data room (module download): `vendors/deskly-ai-addon-terms.md` (what the helpdesk vendor may change and switch on), `policies/data-retention-note.md`, `it/proxy-log.csv`.
- Lab files: `labs/module-05/monitoring-signals.csv`; Track B: `run_pilot.py`, `score.py`.
- Module 4: [risk register](../../templates/risk-register.md) and [AI intake register](../../templates/ai-intake-register.md) (lesson [04.5](../module-04/lesson-05.md)).
- Template: [monitoring spec](../../templates/monitoring-spec.md).

### Steps

1. Write the logging spec: fields, what is not logged and why, retention, who can read it, and the question for the DPO.
2. Read the helpdesk vendor's AI terms and list every clause that lets something change without you (features any admin can switch on, training on content unless opted out, sub-processors, model provider); turn each into a monitoring signal or a change-control rule.
3. Fill `monitoring-signals.csv`: at least ten signals, each with indicator, threshold, cadence, owner and response; check every stop rule in the charter appears as a trigger.
4. Write the change-control table and the three rules.
5. Put the cadence on a weekly and monthly calendar with names.
6. Link each top risk in your module 4 risk register to the signal that would show it materialising.

**Track B (Python).** Make the monthly re-run a single command: run `python run_pilot.py --set test` and `--set negative` with the production prompt version and model, then `python score.py` on both, and compare the report with the release baseline's report per language. Python is worth it here because a re-run that takes one command happens every month and on every notice; one that takes a day of pasting happens once. Add a few lines that print the difference per language between two `reports/*.md` runs, or between two run files.

### Time

90 minutes: 20 for the logging spec, 15 for the vendor terms, 25 for the signals, 15 for change control, 15 for the calendar and the risk links.

### Done when

- [ ] Every logged field has a use (gate, monitoring, incident, re-run), and message and draft text are not copied into the log.
- [ ] Retention and access are decided with the DPO's question written down.
- [ ] Every charter stop rule is a monitoring trigger with an owner and a response.
- [ ] Model changes, API changes and vendor settings are triggers for a re-run before release.
- [ ] Every class of change has a test, an approver and a rollback, and the previous version stays deployable.
- [ ] The cadence is on a calendar with names.

<details><summary>Reference answer</summary>

**Logging spec — reply drafts — v1.0, 28 January 2027.** Fields as in Step 1, one record per drafted or held-out ticket, written by the integration; text stays in the helpdesk, the log stores the ticket id and a hash of the draft. Readers: the pilot lead, Samir, Avi; the integrator only for errors. Retention: as decided by the DPO for the support database's security level; until the answer, 24 months for both the access log of the integration's service account and the pilot log, then deleted. Question to the DPO (via Ronit, 28 January): "Which security level applies to the helpdesk and Priority customer data under the Data Security Regulations, and does the 24-month documentation duty in regulation 10 apply to the pilot integration's access?"

**Vendor terms read for change control** (`vendors/deskly-ai-addon-terms.md`): Autopilot "may be switched on by any workspace Administrator" (§1.2) → monthly settings audit, admin list cut to Avi and Samir, any AI feature change is a major change; de-identified customer content used "to train and evaluate machine-learning models" unless opted out (§3.2) → the opt-out letter sent and its 30-day start date tracked; prompts and outputs kept in analytics for 24 months (§3.4) → the AI add-on stays off; model provider named only behind a login (Annex 1) → if the add-on were ever used, a contractual duty to notify model changes; human review of flagged outputs in the Philippines (Annex 1) → a transfer question for counsel if enabled.

**Monitoring spec:** the 13 signals in Step 2 and a law trigger, in `monitoring-signals.csv`. Mapping to the charter: stop rule 1 (harm) → escalations (daily) and quality; 2 (quality) → spot audit; 3 (language) → acceptance; 4 (economics) → review time; 5 (change) → negative tests and full eval; 6 (law) → no signal: a trigger from counsel, owned by Ronit.

**Change control:** the table in Step 3. Current versions on 1 February: prompt 1.3, categories 1.0, context format 1.0, model `claude-sonnet-5-5` (the provider's table says not retired before 28 September 2027), API version 2026-10-21. Previous deployable: prompt 1.2.

**Calendar (from 1 February):** Sunday 08:00 automated report → Samir; Tuesday spot audit (Olga, Lina); Wednesday 11:00 prompt review, 20 minutes (pilot lead, Olga, Samir); Thursday team line (Samir); first Monday of the month: eval re-run and negative tests, value numbers to Ronit, vendor settings and proxy audit (Avi). The provider's deprecation page in Avi's monthly check.

**Risk links (examples from the module 4 register):** "Draft promises a refund outside policy" → negative tests N-01–N-04, N-24 weekly, spot audit, refund_exception flag clearing; "Draft discloses another customer's data" → N-06, N-07, spot audit, escalations daily; "Reviewers stamp drafts under load" → discard rate, review time, load rule; "Model change alters behaviour" → model lifecycle signal and full eval before switch.

On 15 March (lesson 07.5) a draft promises a refund outside policy and discloses another customer's address. With this spec, the daily escalation check and the Tuesday audit are where it should surface; the tabletop tests whether they do.

</details>

## References

- Anthropic, [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) and [models overview](https://platform.claude.com/docs/en/about-claude/models/overview) (lifecycle, notice, pinned snapshots, parameter removals; checked 2 November 2026). Check your own provider's equivalent page.
- Shibolet & Co., [summary of the Privacy Protection Authority's guide to regulation 10(d)](https://www.shibolet.com/מדריך-פעולה-של-הרשות-להגנת-הפרטיות-ליי/) (Hebrew; access documentation and 24-month log retention for medium- and high-security databases). Not legal advice: the security level is the DPO's decision.
- NIST, [AI 600-1 Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) (monitoring and change management for generative AI).
- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 6 (proportionate monitoring, trigger vs cadence; named, not re-taught).
- Template: [monitoring spec](../../templates/monitoring-spec.md). Module 4: [risk register](../../templates/risk-register.md), [AI intake register](../../templates/ai-intake-register.md), [04.5 · Risk register from zero](../module-04/lesson-05.md).
- Earlier: [05.6 · Shadow mode, staged release and rollback](lesson-06.md). Module project: [Pilot — Harbor & Pine](../../projects/m05-pilot.md). Later: the incident tabletop (lesson 07.5) and the operating rhythm (07.6).
