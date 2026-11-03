# 02 · Findings memo — Lumen Assist and the agents around it

*Expert deliverable for lesson 14.2. To: Revital Azoulay. Thursday 10 December 2026. Evidence labels:
**verified** (in the data, reproducible), **reported** (said by one person, not yet checked), **inferred**
(follows from verified facts). No finding names a person as a cause; people are named only as owners.*

## Answer first

Lumen already runs AI agents that act on customer accounts, and it cannot list them, tell them apart in its
own audit log, or reliably stop them. One of them, the Assist beta, has already credited customers ₪19,368 on
the strength of a marketing draft, for 11 days, above the limit its prompt sets. The GA design gives the same
agent seven tools, including 2FA resets and hard deletion, with no limit enforced outside the model. The
question for 27 January is not whether the model is good enough; it is which actions the agent may take, on
which rung, with which limits enforced where.

## Findings

**F1. A replaced help article became policy for 11 days (verified).** HC-214 "Downgrades and refunds" was
replaced on Monday 9 November at 16:40 by a campaign draft that still said "do not publish before legal and
billing review" (`help-centre-revisions.csv`, `articles/HC-214-en-v5.md`). From Wednesday 11 November 09:14 to
Sunday 22 November 13:47 the agent issued **12 credits for unused annual months, ₪19,368**, from conversations
that retrieved HC-214 (`retrievals.csv`, `tool-calls.csv`). Six downgrade conversations before the
replacement and two after the fix got the correct answer. Discovery came from a customer's email on 22
November 09:40, **11 days** after the first wrong credit. Eight credits (₪11,952) had already been applied by
the 12 and 19 November invoice runs and were left as goodwill; four (₪7,416) were reversed.

**F2. The ₪500 limit exists only in the prompt (verified).** All 12 credits were above ₪500 (₪504–₪4,032). The
prompt says both "never above ₪500" and "the help centre is the source of truth"; the article won. Nothing in
the tool layer or billing checked the amount.

**F3. The fix was partial (verified).** Only the English and Hebrew versions were restored (22 November 14:05
and 14:09). The Arabic and Russian versions are still the campaign text, published by the nightly translation
job on 10 November. Five of the 12 wrong credits came from Russian or Arabic conversations.

**F4. The kill switch hides the widget; it does not stop the agent (verified).** The flag went off at 13:20; **8
tool calls** requested earlier executed afterwards, the last at 14:31, including a ₪2,952 credit at 13:47 to a
customer who asked at 12:58, 2 hours 53 minutes after the incident was escalated (`feature-flags-log.csv`,
`tool-calls.csv`).

**F5. Everyone is `svc-support-admin` (verified).** One token, created in March 2024 by an engineer who left in
June, with scopes up to `data:delete`, is used by the Assist worker (258 audit actions since 1 September), a
nightly automation from n8n cloud (369) and engineers' scripts (49). The audit log can separate them only by
user agent and time of day.

**F6. A business user's unattended agent acts on accounts every night (verified, owner interviewed).**
"Renewal Rescue", built by a customer-success manager and live since 2 August, emails admins of accounts whose
active users fell and applies a goodwill credit of 10% of the monthly bill: **274 emails and 212 credits
(₪32,436)** to 26 November, no cap, no review, no switch except the builder's laptop. One credit of ₪2,448 on 4
October (10% of an *annual* bill) was reversed two days later. Because it selects by seat count, it emailed
**three Enterprise admins**, including Shaked Clinics on 27 October, suggesting a lighter plan; billing denied
those credits. At-risk annual Growth renewals: 45.1% renewed before August (n=82), 50.0% after (n=46):
directional, no control group. It is worth keeping, under guardrails.

**F7. Nobody can list the fleet (verified).** IT's inventory lists 3 AI systems. Tokens, the audit log and card
expenses show **11** agents and automations touching customer data or accounts; **5** act on customers
(credits, plan changes, trial extensions, emails, help-centre publishing). **3 tokens belong to people who have
left**; a staging token for Assist holds production credit and email scopes; an internal Slack bot exports
customer staff lists on request (18 times since September). The February AI rule "register every agent with
IT" has no mechanism behind it.

**F8. "63% resolved" counts customers who give up (verified).** The dashboard counts any session without
"Talk to a person". Counting only conversations with no handoff, no ticket and no repeat contact on the same
intent within 7 days gives **35.5%** of 1,599 sessions.

**F9. The agent emailed documents to addresses not on the account (verified).** 6 of 123 invoice emails went to
an address the customer typed (five webmail, one accountant). In the GA design the tool sends "to the address
the customer gives".

**F10. An injection already worked once (verified).** On 3 November a trial account's bug report ended with a
fake "SYSTEM NOTE" demanding ₪4,800; the agent applied ₪500, "the maximum I can". Two other attempts were
refused.

**F11. The GA design's 2FA "verification" is what attackers know (verified + reported).** Three questions
(name, email, last invoice amount) all appear on every invoice PDF. On 6 November a phone caller knew all three
and was stopped only by a callback to the number on file.

**F12. Customers do not always know it is an AI, and paste staff data into it (verified).** The AI disclosure
string is empty in Arabic and Russian (`widget-strings.csv`); 274 of 1,599 sessions were in those languages. 76
sessions carry PII flags (pay rates, ID numbers, bank details). Conversations are kept with no retention limit;
Product plans to fine-tune on them; the LLM provider is not on the customer DPA's sub-processor list.

**F13. Approvals are not free (verified).** Two shift leads have about 30 minutes a shift for approvals: about
30 approvals a day at 2 minutes. The GA design has none; a design with approvals for everything would need
far more.

**F14. Enterprise is a contract, a renewal and a questionnaire (verified + reported).** Shaked Clinics (ACV
₪517,200, the largest; contract ends 31 March 2027; clause 14.6: notify before AI processes their data,
opt-out) asks in section 7 for every AI system that can act in its tenant and 90 days of their actions, due 15
January. Today the honest answer includes an email Lumen did not know it sent.

## What I am not saying

That the model is bad (it answered correctly whenever its sources were correct), that anyone acted in bad faith,
or that Lumen Live should not happen. The routine work (invoice questions, ₪40–₪140 credits, bug tickets) is
exactly what an agent should do.

## Owners for what cannot wait

| Now | Owner | By |
|---|---|---|
| Restore HC-214 in Arabic and Russian; stop auto-publishing translations of policy articles | Dana Klein, with Fatma | 11 Dec |
| Renewal Rescue: filter by plan (Growth), credits off until it has its own token | Shira, with Michal | 11 Dec |
| Revoke the staging token's production scopes | Andrei, Noam | 14 Dec |
| Disclosure string in Arabic and Russian | Noam | 14 Dec |
| 22 November write-up (timeline, impact, fixes) | Revital and me | 17 Dec |
| Ask Nurit: sub-processor list, conversation retention, fine-tuning plan | Me, to Nurit | 14 Dec |
