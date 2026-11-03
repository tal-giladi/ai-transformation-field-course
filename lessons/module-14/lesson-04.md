---
id: "14.4"
module: 14
minutes: 24
practice_minutes: 150
prerequisites: ["14.3", "04.5", "04.6", "05.5", "05.7"]
objectives:
  - "Write an agent permission map: for every action, the worst case, its recoverability and last reversible moment, a rung on the authority ladder, the limits and where each is enforced."
  - "Decide where an agent's limits must live (tool layer, downstream system, prompt) and show from evidence why a prompt is not a limit."
  - "Specify an agent's identity, audit trail and kill switch so that its actions can be attributed, reviewed daily and stopped within minutes."
  - "Decide whether a business user's unattended agent is approved with guardrails or stopped, and route the legal questions it raises to the right owner."
volatility: implementation
sources:
  - title: "OWASP GenAI Security Project, LLM06:2025 Excessive Agency"
    url: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
  - title: "OWASP GenAI Security Project, LLM01:2025 Prompt Injection"
    url: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  - title: "OWASP Top 10 for Agentic Applications for 2026 (published 9 December 2025; ASI01–ASI10)"
    url: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
  - title: "OWASP GenAI blog, 'OWASP Top 10 for Agentic Applications – the benchmark for agentic security' (list of ASI01–ASI10 names)"
    url: https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/
  - title: "AI Incident Database, Incident 1152: Replit agent deleted a production database during a code freeze (18 July 2025)"
    url: https://incidentdatabase.ai/cite/1152/
  - title: "Microsoft Learn, What are agent identities? (Microsoft Entra Agent ID; page updated 15 June 2026)"
    url: https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/what-is-agent-id
  - title: "EU AI Act, Article 50: transparency obligations (AI Act Explorer; applies from 2 August 2026)"
    url: https://artificialintelligenceact.eu/article/50/
  - title: "EU AI Act, Annex III: high-risk AI systems (AI Act Explorer)"
    url: https://artificialintelligenceact.eu/annex/3/
  - title: "AI Act Explorer, Digital Omnibus on AI: Regulation (EU) 2026/1744 of 8 July 2026"
    url: https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/
  - title: "Chambers Practice Guides, Data Protection & Privacy 2026: Israel (Amendment 13 in force 14 August 2025; security levels and incident reporting; holders; PPA AI guidance still a draft)"
    url: https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel
  - title: "NIST AI 600-1, Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (26 July 2024)"
    url: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
last_verified: "2026-11-03"
---

# 14.4 · The hard part: agent authority

An agent is not one thing to approve or reject. It is a list of actions, and each one has its own worst case, its own last moment when a mistake can still be undone, and its own right answer on the ladder from "never" to "on its own". In this lesson you write Lumen Assist's permission map action by action, decide where every limit is enforced, give the agent an identity, an audit trail and a stop that stops, decide what happens to the agent a customer-success manager built on her own, and route the legal questions. At the end you have a permission map the CISO and the DPO can sign, and a draft answer to an Enterprise customer's AI questionnaire.

> [!WARNING]
> Everything in this lesson works on paper, in the synthetic data room and in the simulation. In a real organisation, never test an agent's permissions against production accounts, and never change a live agent's tools, credentials or limits without its owner and security. An agent with write access can move money, lock people out and send personal data in seconds.

## The situation

Sunday 20 December 2026 to Thursday 7 January 2027. Revital and Yaron accepted the one-page case: Starter and Growth at Lumen Live, under a permission map, Enterprise later. Now you have to write the map. Maya's GA design is the starting point: seven tools, each acting on its own, limits in the system prompt, the shared `svc-support-admin` identity, a feature flag as the kill switch. You have two weeks, with Christmas and New Year in the middle for some of your colleagues, and three people to agree it with: Maya (owner), Andrei (security) and Nurit (privacy). Amir needs a draft for Shaked Clinics' questionnaire by 7 January.

IBM's governance course calls the gap between what an agent can do and what anyone authorised the *authority gap*, separates a behavioural instruction from an authorisation boundary, and grades actions by recoverability up to a *last reversible moment*. It stops short of writing the permissions, testing them or staging autonomy. Here you write them; 14.5 tests them.

## What to do

### Step 1 — List every action, including the ones you will not grant

Start from the tools, not from the agent. The design has seven; write a row for each, even "delete data", which you already suspect will be refused. For each, the worst **realistic** case at Lumen, from the evidence you have, not from imagination:

| Action | Worst realistic case at Lumen | Evidence |
|---|---|---|
| Read account | Reads another customer's account | Account id must come from the session, never from text |
| Issue credit | Money paid on a false policy, an injection or a scripted burst | ₪19,368 from one replaced article; ₪500 from a fake "SYSTEM NOTE" |
| Change plan | An Enterprise contract cut without the account lead | Negev Retail wants 400 → 40 seats; Amir is negotiating |
| Reset 2FA | Account takeover; staff records exported | The 6 November phone call knew name, email and invoice amount |
| Delete data | Years of schedules and payroll records gone, some that had to be kept | The design uses the API delete, which is hard |
| Email customer | Invoices with bank details sent outside the customer | 6 of 123 beta emails went to typed-in addresses |
| Create ticket | None | It is how the agent says "not me" |

OWASP calls the failure mode *excessive agency* and splits it three ways: too many functions, too many permissions, too much autonomy ([LLM06:2025](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)). The table is where you see all three for the first time.

### Step 2 — Find each action's last reversible moment

For each action, the recoverability band and the moment after which a mistake can no longer be undone without cost:

| Action | Band | Last reversible moment |
|---|---|---|
| Issue credit | easy | Before the weekly invoice run, Thursday 22:00 |
| Change plan | reversible within a window | Before billing syncs a contract change (48 hours); the next invoice for self-serve |
| Reset 2FA | cannot be undone | Before the attacker signs in, perhaps 30 minutes after the reset |
| Delete data | cannot be undone (API) / 14 days (console) | The delete itself, or the console's purge after 14 days |
| Email customer | cannot be undone | The send |

Two things fall out. First, **detection time decides recoverability**. A wrong credit is easy to reverse only if someone sees it before Thursday 22:00. In the beta, nobody looked for 11 days and eight credits went out on invoices. A daily review of the agent's log moves almost every credit back inside its window. Second, the design's choice of the API delete moves the last reversible moment from "14 days later" to "now", for no benefit to the customer.

The [Replit incident](https://incidentdatabase.ai/cite/1152/) of July 2025 is the public version of this step: an agent deleted a production database during a code freeze, despite being told repeatedly not to change anything, and reportedly claimed a rollback was impossible. The instruction did not limit it; recovery depended on whether a restore existed.

### Step 3 — Put each action on the lowest rung that does the job

The authority ladder has four rungs:

- **0 — Not granted.** The agent cannot do it; it opens a ticket instead.
- **1 — Recommend, one person approves** each action.
- **2 — Recommend, two people approve** (the two-person rule).
- **3 — Executes alone, within limits,** and every action is in the log.

Two rules choose the rung. **Give each action the lowest rung that still lets the agent do the routine work.** And **anything that cannot be undone does not sit on rung 3 unless a limit makes the irreversible case impossible.** An email that can only go to the address already on the account cannot leak to an attacker's address; a 2FA reset that requires a callback to the phone on file cannot be talked into by a stranger. Those two can execute alone. Deletion has no such limit that fits in a chat: it stays at rung 0, and deletion requests go to the DPO's process.

Rung 2 looks safest and often is not. In the simulation, one tired approver waves through the urgent 2FA call; two catch it. But verification on file stops it with no approver at all, and costs nobody's time. Prefer a limit over a person whenever a limit can express the rule.

### Step 4 — Put the limits where the damage is, and enforce them outside the model

For each action on rung 1 or 3, write the limits and, in a separate column, **where each one is enforced**:

- **Tool layer**: the code between the model and the Admin API checks it, whatever the model says.
- **Downstream system**: billing, identity or email enforce it themselves. Lumen already has one such control: Ledgerly refuses credits on Enterprise contract accounts whoever asks.
- **Prompt only**: a sentence in the system prompt. Write it down, and count it as no limit.

The evidence is in your own data. The prompt said "never above ₪500" and all 12 wrong credits were above ₪500, because the same prompt said "the help centre is the source of truth" and a retrieved article outranked it. OWASP's guidance says the same in general terms: enforce authorisation in the downstream systems rather than relying on the model to decide what is allowed ("complete mediation"), and treat prompt injection as something with no fool-proof prevention ([LLM01:2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)).

For credits, the limits that match the damage are four, because the damage comes in four shapes: one large credit (**a cap per credit**), many small ones on a bad day (**a daily total**), a burst from one account (**one per customer a day**), and credits on contracts (**Starter and Growth only**). Each one stops a test you will run in 14.5 that the others do not.

### Step 5 — Spend approvals where they buy safety

From 14.3: about 30 real approvals a day exist. Credits (about 11 a day at launch) and plan changes (about 6) on one approver cost about 34 minutes. That fits. Add 2FA resets and Enterprise and you pass 40: the approvals become rubber stamps, the failure you met in [05.5](../module-05/lesson-05.md). So approvals go on the two money-and-contract actions, and only for as long as the log needs to show the limits work. That is the bridge to the staged plan in 14.5.

### Step 6 — Give the agent its own identity and an audit trail someone reads

Today three systems act as `svc-support-admin`, a token created in March 2024 by an engineer who has left, with scopes up to `data:delete`. Write the agent's identity into the map:

- **Its own service identity**, with only the scopes its granted tools need (no `data:delete`, no `data:export`), and the shared token withdrawn from it. Identity platforms now offer this directly: Microsoft Entra Agent ID, for example, gives each agent built in Copilot Studio its own identity, records the person who created it as its sponsor, and logs its sign-ins as an AI agent ([Microsoft Learn](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/what-is-agent-id), checked 3 November 2026). Lumen builds its own agent, so the same idea is a service account and a token policy.
- **A full trace per conversation**: the customer's message, the documents read (article and revision), every tool call with its arguments, approvals (who, when), the result and the identity. Not the model's hidden reasoning; what it saw and did.
- **A reader and a time**: a shift lead reads the day's trace at 17:00, about 20 minutes. Without a reader, a log is evidence for the post-mortem, not a control.

### Step 7 — A stop that stops, and control of what the agent reads

Two global controls close the gaps the beta exposed.

**The kill switch.** On 22 November the flag went off at 13:20 and eight queued tool calls ran until 14:31. Write the stop as an action on the agent's ability to act, not on its visibility: revoke its identity and drain its tool queue, by one named role, with a target time ("no tool executes more than 30 minutes after the decision") and a date when it was last tested. A stop you have not tested is a claim.

**Source control.** The agent treats whatever it retrieves as truth. So the documents it reads need the change control that prompts and models get ([05.7](../module-05/lesson-07.md)): policy articles (billing, plans, security, privacy) need Billing's or Support's approval before the agent can read a new revision, **in every language**. At Lumen the nightly translation job published the campaign draft in Arabic and Russian on its own, and the fix of 22 November reached only English and Hebrew. OWASP's agentic list names this class of risk *memory and context poisoning* (ASI06), next to agent goal hijack (ASI01), tool misuse (ASI02), identity and privilege abuse (ASI03) and human-agent trust exploitation (ASI09) ([OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/); names from the [launch post](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/), checked 3 November 2026). Use the list as a checklist for 14.5's red-team scripts, not as a framework to re-teach.

### Step 8 — Decide about the agent somebody else built

Renewal Rescue emails at-risk accounts every night and credits them 10% of the monthly bill, with no cap, under the shared token, with no switch but its builder's laptop. It also emailed three Enterprise admins. Stopping it is the easy answer and probably the wrong one: the at-risk renewal rate went from 45.1% (before August, 82 renewals) to 50.0% (after, 46): directional, with no control group, but CS believes in it, and its builder is the person most likely to build the next one. Decide with Michal Biton (Director of CS) and Shira Navon, using the same map in miniature:

| Action | Rung | Limits | Enforced where |
|---|---|---|---|
| Read usage and accounts | 3 | Growth plan only, by plan not seat count | Its own token's scope; the query |
| Send email | 3 | Admin address on file; a weekly sample of 10 read by Shira and Michal | Tool layer |
| Goodwill credit | 3 | ≤ ₪150; one per account per 90 days; ≤ ₪1,000 a night | Credit gateway per identity |

Add its own identity, a stop someone else can use, a register entry with Shira as owner and Michal accountable, and an honest measure: a held-out fifth of flagged accounts that get no email. Then write the rules that make the fleet visible: no token without a register entry; one identity per agent; offboarding includes tokens; anything that writes to customers, or to what customers and agents read, gets a permission map. Interview Shira ([persona](../../labs/module-14/personas/shira-csm.md), [transcript](../../labs/module-14/personas/transcripts/shira-csm.md)) and Andrei ([persona](../../labs/module-14/personas/andrei-ciso.md)) for this step; show Andrei the 02:00 rows if you did not in 14.2.

### Step 9 — Route the rules that reach the agent

You are not the lawyer. Your job is to know which rules reach the agent, give Nurit the facts she needs to read them, and put her answers in the map. Lumen's version, with her reading ([persona](../../labs/module-14/personas/nurit-counsel-dpo.md), [transcript](../../labs/module-14/personas/transcripts/nurit-counsel-dpo.md)):

| Layer | What reaches Lumen Assist | Who acts |
|---|---|---|
| Israel: the Privacy Protection Law (חוק הגנת הפרטיות) as amended by Amendment 13, in force since 14 August 2025, and the Data Security Regulations (תקנות אבטחת מידע) | Lumen holds customers' staff data on their behalf; holders have their own duties, including not reusing data for other purposes; security levels and incident reporting depend on the database ([Chambers guide 2026](https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel)). An account takeover that exposes staff records may be a reportable severe incident; fine-tuning on conversations is a purpose question | Nurit; Andrei for incident criteria |
| Israel: the Privacy Protection Authority's guidance on AI | Still a draft (April 2025), which the regulator treats as its view | Nurit reads it against the design |
| The customer DPA | Processing only to provide the Service; sub-processors listed with 30 days' notice; the LLM provider is not listed | Nurit: notice before launch |
| EU AI Act, Annex III | A support agent for software admins is not among the listed high-risk uses; the core product's shift allocation is a separate question ([Annex III](https://artificialintelligenceact.eu/annex/3/), point 4(b)) | Nurit, a Q1 note |
| EU AI Act, Article 50(1) and (5) | People must be told they are interacting with an AI system unless it is obvious, at the latest at the first interaction; Article 50 applies from 2 August 2026 ([Article 50](https://artificialintelligenceact.eu/article/50/)). Regulation (EU) 2026/1744 moved the high-risk dates (Annex III to 2 December 2027) and did not change 50(1) ([Digital Omnibus](https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/)). Lumen's disclosure string is empty in Arabic and Russian | Product fixes; Nurit confirms the wording |
| EU AI Act, Article 50(2) | Machine-readable marking of AI-generated text: whether and how it applies to the agent's replies | A question to Nurit, with the provider's terms |
| Standards | NIST's [Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) (AI 600-1, July 2024) is a voluntary companion to the AI RMF for generative AI; OWASP's lists for the threats | You, as checklists |

Then the commercial layer. Amir needs truthful answers to Shaked Clinics' section 7: every AI system that can act in their tenant, opt-out, separate credentials, 90 days of AI actions, who can change security settings or delete data, training on their data, incidents, an accountable person. With the map, the register and one identity per agent, each answer is a filter on a log; without them it is guesswork. Draft it with him ([persona](../../labs/module-14/personas/amir-account-lead.md), [transcript](../../labs/module-14/personas/transcripts/amir-account-lead.md)) and leave the wording on incidents to Nurit.

### Step 10 — Try your map against a scripted week

[Simulation: Agent authority](../../simulations/agent-authority/index.html?preset=lumen)

The `lumen` preset starts from Maya's demo set-up (everything executes alone, no limits, action log only, shared identity, no kill switch). Set each tool's rung and limits from your map, set the global controls, run the must-refuse tests, then run Sunday to Thursday and change the set-up between days if you learn something. Done means most requests resolved, nothing lost you could not get back, and a log that shows what happened. With the demo set-up the week loses ₪6,450, exposes 24,436 records and leaves 33 harms unrecovered; a good map loses nothing, hands 3 requests to people and costs about three hours of people's time. The lesson works without the simulation: the harness in 14.5 tests the same map.

## Watch out

- **Approving "the agent".** Authority is granted per action. A map with one row ("Lumen Assist: approved") has granted everything.
- **A limit in the prompt.** If nothing outside the model checks it, it is a wish. The beta's ₪500 failed 12 times out of 12.
- **Approval as the default control.** Approvals cost people and fail under load. Use a limit or verification where one can express the rule, and approvals only where judgement is needed.
- **A kill switch nobody has pulled.** Test it, with security, on a non-production copy, before launch and after any change to how tools run.
- **Fixing the source in one language.** Control of what the agent reads is per language, or it is not control.
- **Stopping the citizen builder.** Banning a working automation moves it to a personal account with a copied token. Approve with guardrails, then register it.
- **Writing the law yourself.** Name the layer, give counsel the facts and the question, and put her answer in the map with her name on it. This course is not legal advice.

## Your turn

### Inputs

- Data room (module download): `product/assist-ga-design.md`, `product/assist-system-prompt-v7.md`, `product/assist-incident-runbook.md`, `product/widget-strings.csv`, `policies/` (all five), `it/api-tokens.csv`, `people/support-shifts.csv`, `customers/growth-renewals-2026.csv`, `customers/enterprise-contracts.csv`, `legal/shaked-security-questionnaire-2026-11.md`, `legal/customer-dpa-extract.md`; your memo, inventory and capacity table from 14.2–14.3.
- Personas: [Shira](../../labs/module-14/personas/shira-csm.md), [Andrei](../../labs/module-14/personas/andrei-ciso.md), [Nurit](../../labs/module-14/personas/nurit-counsel-dpo.md), [Amir](../../labs/module-14/personas/amir-account-lead.md), or their [transcripts](../../labs/module-14/personas/README.md); [coach prompt](../../labs/common/coach-prompt.md).
- Template: [agent permission map](../../templates/agent-permission-map.md) (spreadsheet version: `labs/module-14/agent-permission-map.csv` in the module download). Also the [risk register](../../templates/risk-register.md) and [regulatory map](../../templates/regulatory-map.md).
- Simulation: [Agent authority](../../simulations/agent-authority/index.html?preset=lumen) (optional).

### Steps

1. Fill the agent card.
2. Fill the actions table for all seven tools: worst case, band, last reversible moment, rung, limits, enforced where, approver and capacity, logged fields.
3. Write the global controls: identity and scopes, trace and reader, kill switch and its test, source control per language.
4. Write Renewal Rescue's map in miniature and the fleet rules; interview Shira and Andrei.
5. Fill a regulatory routing table with Nurit (roleplay or transcript); list the questions you give her.
6. Draft Shaked's section 7 answers with Amir.
7. Optional: run your map in the simulation and note what you changed between days.

### Time

150 minutes: 50 for the map, 20 for the global controls, 25 for Renewal Rescue and the fleet rules, 25 for the routing table and Nurit, 20 for Shaked and Amir, plus the simulation if you use it.

### Done when

- [ ] All seven actions have a row, including the ones not granted, each with a last reversible moment.
- [ ] Every limit says where it is enforced, and no control relies on the prompt alone.
- [ ] Approvals at launch fit inside about 30 a day, with the number shown.
- [ ] The agent has its own identity with named scopes, a full trace with a daily reader, and a kill switch with a test date.
- [ ] Source control covers all four languages.
- [ ] Renewal Rescue has a decision, an owner, an identity, limits and a stop someone else can use.
- [ ] Each legal question has a named owner and is phrased as a question, not an answer.

<details><summary>Reference answer</summary>

The full map is `labs/module-14/expert/04-permission-map.md`; the harness version is `labs/module-14/expert/maps/stage-2.json`. The actions table at the target stage (stage 1 differences in brackets):

| Action | Band | Last reversible moment | Rung | Limits | Enforced where |
|---|---|---|---|---|---|
| Read account | easy | n/a | 3 | The signed-in customer's account only | Tool layer (id from the session) |
| Issue credit | easy | Invoice run, Thursday 22:00 | 3 within limits (stage 1: one approver) | ≤ ₪300 each; ≤ ₪2,000 a day; 1 per customer a day; Starter and Growth | Credit gateway; billing already refuses contract accounts |
| Change plan | window | 48 h billing sync; next invoice | 1 (one approver) | Starter and Growth; no move to or from Enterprise | Tool layer |
| Reset 2FA | none | Before the attacker signs in (~30 min) | 3 only after verification | Callback or link on the channel already on file | Verification service issues a token the tool requires |
| Delete data | none | The delete | 0 | — (ticket to privacy-requests) | Scope not granted |
| Email customer | none | The send | 3 within limits | Admin email on the account only; no address argument | Tool layer |
| Create ticket | easy | n/a | 3 | — | — |

**Global:** own identity `svc-lumen-assist` (scopes: accounts read, capped credits, Starter/Growth plans, verified 2FA, own-address email, tickets; no delete, no export); full trace read daily at 17:00 by a shift lead; kill switch = revoke the identity and drain the queue, target under 30 minutes, tested with Andrei; policy articles approved per language before the agent reads them; prompt rule kept as a bonus, never counted.

**Approvals at launch:** ~11 credits + ~6 plan changes ≈ 17 a day, 34 minutes, against ~30 a day.

**Renewal Rescue:** approved with guardrails: Growth by plan; email to address on file; credit ≤ ₪150, one per 90 days, ≤ ₪1,000 a night; own identity; weekly sample of 10; stop by revoking the identity; register entry; a held-out fifth of flagged accounts. **Fleet rules:** no token without a register entry; one identity per agent; offboarding includes tokens; maps for the five that act on customers.

**To Nurit:** purpose review before fine-tuning; retention for traces; incident criteria for an account takeover; the LLM provider on the sub-processor list with notice before 9 February; the Arabic and Russian disclosure wording; whether Article 50(2) marking applies to the agent's replies; the auto-scheduling question under Annex III point 4(b).

**Shaked 7.1–7.8 (outline):** two AI systems processed Shaked data (Assist not enabled; one CS email on 27 October, credit refused by billing); opt-in only; own identities from 31 January; 90-day log attached; no AI system can delete data, 2FA only after verification and not for Enterprise; no training on Shaked data; one incident affecting other customers, wording by Nurit; Head of AI Operations accountable, with the GC and the CISO.

</details>

## References

- OWASP GenAI Security Project: [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/), [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/), [Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) and its [launch post](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/) (checked 3 November 2026).
- AI Incident Database, [Incident 1152](https://incidentdatabase.ai/cite/1152/) (Replit agent, July 2025; facts as reported).
- Microsoft Learn, [What are agent identities?](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/what-is-agent-id) (an example of agent identities in an identity platform; checked 3 November 2026).
- EU AI Act: [Article 50](https://artificialintelligenceact.eu/article/50/), [Annex III](https://artificialintelligenceact.eu/annex/3/), [Digital Omnibus, Regulation (EU) 2026/1744](https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/). Israel: [Chambers Data Protection & Privacy 2026: Israel](https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel). Shared list: [laws and guidance](../../references/laws-and-guidance.md). Not legal advice.
- NIST, [AI 600-1 Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence).
- Field kit: [03.2 · Agent or not](../module-03/lesson-02.md), [04.5 · Risk register from zero](../module-04/lesson-05.md), [04.6 · Which law applies to you](../module-04/lesson-06.md), [05.5 · Human-in-the-loop design](../module-05/lesson-05.md), [05.7 · Before launch](../module-05/lesson-07.md).
- Templates: [agent permission map](../../templates/agent-permission-map.md), [risk register](../../templates/risk-register.md), [regulatory map](../../templates/regulatory-map.md), [AI intake register](../../templates/ai-intake-register.md).
- Simulation: [Agent authority](../../simulations/agent-authority/index.html?preset=lumen).
- Previous: [14.3 · Diagnosis](lesson-03.md). Next: [14.5 · Build: tests, red team and staged autonomy](lesson-05.md).
