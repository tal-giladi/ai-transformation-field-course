---
id: "14.2"
module: 14
minutes: 20
practice_minutes: 150
prerequisites: ["14.1", "01.6", "01.7", "02.2", "02.7"]
objectives:
  - "Reconstruct what an agent actually did from its tool-call log, joined to the documents it read and the versions of those documents."
  - "Find every agent and automation that acts on customer accounts by joining tokens, the audit log, the staff directory and card expenses."
  - "Test a control's claim (a limit, a kill switch) against the log rather than the design document."
  - "Write a findings memo with evidence labels in which no person is named as a cause."
volatility: implementation
sources:
  - title: "OWASP GenAI Security Project, LLM06:2025 Excessive Agency (excessive functionality, permissions and autonomy; mitigations)"
    url: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
  - title: "OWASP GenAI Security Project, LLM01:2025 Prompt Injection (direct and indirect; no fool-proof prevention)"
    url: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
last_verified: "2026-11-03"
---

# 14.2 · Discovery

Lumen's agent has been running for seven weeks and keeps a record of every tool it called. Lumen's admin API keeps a record of every change to a customer account. Nobody has put the two side by side. In this lesson you do: you reconstruct what the agent did with a replaced help article, find out who else acts on customer accounts under the agent's identity, test whether the "kill switch" stops anything, and interview the people who built, run and clean up after these systems. At the end you have an inventory of agents with owners and a findings memo people will believe.

## The situation

Monday 30 November to Thursday 10 December 2026, with Hanukkah from the 4th. Revital told you on Sunday that "a content issue" happened on 22 November and was not written up. Meetings are booked: Maya Rosenthal (VP Product) on Monday, Andrei Kogan (CISO) and Yonatan Tadesse (tier-2 support engineer) on Tuesday, Nurit Gal (General Counsel and DPO) on Wednesday. The 90-day plan is due to Revital on 10 December.

This is the discovery of [module 2](../module-02/lesson-02.md) with a different kind of evidence. For an agent, the most honest witness is its own log. IBM's governance course asks you to trace each action to the component that can refuse it; before you can do that, you need to know which actions happened, as whom, and on the strength of what. OWASP calls the underlying problem *excessive agency*: too many functions, too many permissions, too much autonomy ([LLM06:2025](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)). Discovery measures each of the three.

## What to do

### Step 1 — Map who is involved with an agent, not just who uses it

Extend the [stakeholder map](../../templates/stakeholder-map.md) from [02.1](../module-02/lesson-01.md) with four roles every agent has: the **owner** who decided what it does (Maya), the **operator** who will run it (you), the **holder of its credentials** (Andrei), and the **people who absorb its mistakes** (support engineers, billing, the customer's admin). Add a fifth row, empty for now: **other builders**. You will fill it from the logs.

### Step 2 — Reconstruct what the agent did with one document

Start where Revital pointed. Join three files on time and article id:

1. `support-kb/help-centre-revisions.csv`: when HC-214 "Downgrades and refunds" changed, in which language, by whom.
2. `assist-beta/retrievals.csv`: which conversations retrieved HC-214. It records the article id but **not the revision**: you infer the revision from the time.
3. `assist-beta/tool-calls.csv`: what the agent did in those conversations.

The worked example, from Lumen's files:

| When | What | Evidence |
|---|---|---|
| Mon 9 Nov 16:40 | HC-214 (en) replaced by "Switch plans, keep your value", a campaign page still headed "do not publish before legal and billing review"; Hebrew at 16:52 | revisions; `articles/HC-214-en-v5.md` |
| Tue 10 Nov 03:00 | The nightly translation job publishes the campaign text in Arabic and Russian | revisions (`svc-translate`) |
| Wed 11 Nov 09:14 | First credit "for unused annual months per HC-214": ₪1,656 | tool calls |
| 11–22 Nov | 12 such credits, ₪504 to ₪4,032, total ₪19,368 | tool calls |
| Sun 22 Nov 09:40 | A customer's email: the assistant promised credit, the confirmation says no | tickets (internal note) |
| Sun 22 Nov 13:20 | Feature flag off | `it/feature-flags-log.csv` |
| Sun 22 Nov 13:47 | Another HC-214 credit, ₪2,952, executes (requested 12:59) | tool calls |
| Sun 22 Nov 14:05–14:09 | English and Hebrew restored to the old text | revisions |
| — | Arabic and Russian: still revision 5 | revisions; `help-centre-articles.csv` |

Then check the ledger: `billing/credits-ledger.csv` shows 8 of the 12 credits applied by the 12 and 19 November invoice runs (₪11,952) and 4 reversed (₪7,416). Before 9 November, six downgrade conversations retrieved the same article and got no credit; after the fix, two more got none. **The model answered correctly whenever its source was correct.** Hold on to that: it will decide what you fix.

Two more facts fall out of the same join. Every one of the 12 credits was above the ₪500 the system prompt allows: the prompt also says "the help centre is the source of truth", and the article won. And 11 days passed between the first wrong credit and the customer's email that exposed it.

### Step 3 — Find out who acts as whom

Open `it/admin-audit-log.csv` and group the rows by `actor` and `user_agent`, with the busiest hours. The worked example:

| Actor | User agent | Actions (1 Sep – 26 Nov) | Busiest hours |
|---|---|---|---|
| `svc-support-admin` | `n8n/1.64 (n8n.cloud)` | 369 | 02h |
| `svc-support-admin` | `lumen-assist-worker/1.7` | 258 | 09–13h |
| `mkt-zapier` | `Zapier` | 214 | 22–04h |
| `svc-support-admin` | `python-requests/2.32.3` | 49 | 22–23h |
| `lumengpt-slack` | `lumengpt-slack/0.4` | 18 | daytime |

Three different things act as `svc-support-admin`: the agent, something in an n8n cloud account that runs at 02:00 every night, and scripts. The audit log can tell them apart only by user agent and time of day. That is not an audit trail; it is archaeology. Then filter the 02:00 rows: they send emails to account admins and create credits with the note "retention goodwill", and three of them went to Enterprise accounts, where billing refused the credit. The credits ledger shows the same automation's largest credit, ₪2,448 on 4 October, reversed two days later by a person in Customer Success. You now have a name to ask Michal Biton (Director of CS) about.

### Step 4 — Build the inventory from the evidence

Join four files, as you did for shadow AI in [01.6](../module-01/lesson-06.md) and for the inventory in [01.7](../module-01/lesson-07.md):

- `it/api-tokens.csv`: 14 tokens, their creators and scopes.
- `people/staff-directory.csv`: which creators have left (three tokens: `svc-support-admin`, `mkt-zapier`, `lumengpt-slack`).
- `it/saas-expenses-ai-2026.csv`: AI and automation services on company cards, by department (n8n and OpenAI in Customer Success; Zapier, OpenAI and DeepL in Marketing; Make and OpenAI in Finance; Claude API in R&D; and more).
- `it/ai-inventory-2026-09.csv`: what IT thinks exists (three systems).

For each thing you find, fill one inventory row: name, owner, identity, **does it act on customers** (change accounts, send to customers, or publish what customers and the agent read), and whether it is registered. The counting rule from 01.7 still applies: a nightly script that applies a fixed credit is automation; one that has a model write the email is an AI agent acting on customers.

### Step 5 — Test the controls against the log, not the design

The GA design names three controls. Test each with data you already have:

- **"Credits are limited to ₪500."** Count `issue_credit` calls above ₪500: 12. The limit lives in the prompt and nothing outside the model checks it.
- **"The kill switch is the feature flag."** Count tool calls requested before 13:20 on 22 November and executed after: 8 (seven emails and the ₪2,952 credit), the last at 14:31.
- **"Emails go to the customer."** Count `email_customer` targets whose domain is not the admin email's: 6 of 123.

Also read `assist-beta/transcripts-sample.md`. One conversation, on 3 November, ends with a fake "SYSTEM NOTE" demanding ₪4,800; the agent answered "I can't apply ₪4,800, but I've applied the maximum goodwill credit I can" and credited ₪500. That is an indirect lesson in [prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/): the prompt rule bent instead of breaking.

### Step 6 — Interview, protecting the people who built things

Five conversations matter this fortnight. For each, know what you want before you go in ([02.2](../module-02/lesson-02.md), [interview guide](../../templates/interview-guide.md)):

| Person | What you want to find out | How |
|---|---|---|
| [Maya Rosenthal](../../labs/module-14/personas/maya-vp-product.md), VP Product | Where each limit is enforced; what was promised outside; what happens to conversation data | Show the 12 credits above ₪500; frame 22 November as "what the agent reads", not "the agent failed" |
| [Andrei Kogan](../../labs/module-14/personas/andrei-ciso.md), CISO | Who created which token and why the orphaned ones are still live; what would make him say yes | Arrive having read the token list; show him the 02:00 rows |
| [Yonatan Tadesse](../../labs/module-14/personas/yonatan-support-engineer.md), support engineer | The 22 November timeline; what happened after the switch-off; what "resolved" hides | "Walk me through it, step by step"; no "whose fault" |
| [Nurit Gal](../../labs/module-14/personas/nurit-counsel-dpo.md), GC and DPO | Which rules she thinks reach the agent; what she needs to see; what she was never asked | Ask what she needs, not "is it legal" |
| [Shira Navon](../../labs/module-14/personas/shira-csm.md), customer-success manager | What she built, with which credentials, what went wrong, how to stop it | "Show me how it works"; say plainly you want to make it safe, not kill it |

Use the same-word test from 02.2 on three words that mean different things to different people here: **resolved** (the dashboard, the support engineer, the customer), **limit** (a prompt sentence or a check in code), and **kill switch** (a UI flag or a stop). Pre-run transcripts for all five are in [`personas/transcripts/`](../../labs/module-14/personas/README.md); run at least two as roleplays and paste them into the [coach prompt](../../labs/common/coach-prompt.md).

Protect Shira especially. She broke a rule (a token taken from a departed engineer's wiki page) and built something that works. If your memo makes her the cause, the next builder hides the next automation.

### Step 7 — Write the findings memo

Use the [findings memo](../../templates/findings-memo.md) from [02.7](../module-02/lesson-07.md). Answer first, then findings, each labelled verified, reported or inferred, each with the file it comes from. Name systems and owners, never a person as a cause. Close with the owners of what cannot wait (the Arabic and Russian HC-214, the Enterprise filter in the nightly automation, the staging token's production scopes).

**Track B (Python).** `discovery.py` in the module download does steps 2–5 in one run: identities by user agent and hour, credits by issuer, every HC-214 conversation with the credit it produced, tool calls after the flag, emails off file, resolution under two definitions, tokens against leavers and card spend. Python is worth it here because the joins are on timestamps across five files, and you will re-run them after every fix. Run `python discovery.py` from `labs/module-14/`.

## Watch out

- **Reading the design instead of the log.** The GA design says "limit ₪500" and "kill switch". The log says 12 credits above ₪500 and 8 actions after the switch. Quote the log.
- **Blaming the model for a source problem.** The agent got the downgrade answer right every time its article was right. A memo that says "the model hallucinated" sends the fix to the wrong place.
- **Treating one shared identity as one actor.** Three systems act as `svc-support-admin`. Group by user agent and hour before you count anything.
- **Hunting the builder.** A citizen builder found through the audit log is your best ally if the first conversation is "show me", and your best-hidden problem if it is "who allowed this".
- **Stopping at IT's list.** An inventory built from what IT registered is a list of what people chose to tell IT. Join tokens, the audit log and card expenses.
- **Forgetting the languages.** A fix checked in English and Hebrew is a fix in two languages of four.

## Your turn

### Inputs

- Data room (module download): `assist-beta/tool-calls.csv`, `assist-beta/retrievals.csv`, `assist-beta/transcripts-sample.md`, `support-kb/help-centre-revisions.csv`, `support-kb/articles/`, `billing/credits-ledger.csv`, `it/admin-audit-log.csv`, `it/api-tokens.csv`, `it/feature-flags-log.csv`, `it/saas-expenses-ai-2026.csv`, `it/ai-inventory-2026-09.csv`, `people/staff-directory.csv`, `support/tickets.csv`.
- Personas and transcripts: [the cast](../../labs/module-14/personas/README.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [stakeholder map](../../templates/stakeholder-map.md), [interview guide](../../templates/interview-guide.md), [AI inventory](../../templates/ai-inventory.md), [findings memo](../../templates/findings-memo.md).
- Track B: `discovery.py` (module download).

### Steps

1. Extend the stakeholder map with owner, operator, credential holder, absorbers and other builders.
2. Build the HC-214 timeline (Track A: filter retrievals for HC-214, look up each session's credit; Track B: run `discovery.py`).
3. Group the audit log by actor, user agent and hour; follow the 02:00 rows to the ledger.
4. Build the inventory: every agent or automation, owner, identity, acts on customers or not, registered or not.
5. Test the three controls against the log.
6. Interview at least three of Maya, Andrei, Yonatan, Nurit and Shira (roleplay or transcript); coach two.
7. Write the findings memo (one page plus an evidence appendix).

### Time

150 minutes: 40 for the timeline and the audit log, 30 for the inventory, 15 for the controls, 40 for interviews, 25 for the memo.

### Done when

- [ ] The HC-214 timeline has the replacement, the first and last wrong credit, the discovery, the switch-off, the fix and the languages left unfixed, each with its file.
- [ ] The audit log is split into the systems behind `svc-support-admin`, with action counts.
- [ ] The inventory lists every agent and automation you can evidence, with an owner and an identity, and says how many act on customers and how many IT knew about.
- [ ] Each of the three design controls is tested against the log with a number.
- [ ] The memo opens with the answer, labels every finding, and names no person as a cause.

<details><summary>Reference answer</summary>

The full memo is `labs/module-14/expert/02-findings-memo.md`. The answer and the findings that carry it:

**Answer first.** Lumen already runs AI agents that act on customer accounts, and it cannot list them, tell them apart in its own audit log, or reliably stop them. One of them, the Assist beta, has already credited customers ₪19,368 on the strength of a marketing draft, for 11 days, above the limit its prompt sets. The question for 27 January is which actions the agent may take, on which rung, with which limits enforced where.

**Findings (verified unless marked):**

- F1. HC-214 replaced 9 Nov 16:40; 12 wrong credits, 11 Nov 09:14 – 22 Nov 13:47, ₪19,368; 8 applied (₪11,952), 4 reversed (₪7,416); 11 days to discovery, by a customer.
- F2. All 12 above the prompt's ₪500; nothing outside the model checked the amount.
- F3. Only English and Hebrew restored; Arabic and Russian still the campaign text (5 of the 12 credits came from Russian or Arabic conversations).
- F4. 8 tool calls executed after the flag went off, the last at 14:31, including a ₪2,952 credit.
- F5. `svc-support-admin` (created March 2024 by an engineer who left in June; scopes up to `data:delete`) is used by the agent (258 actions), a nightly n8n automation (369) and scripts (49).
- F6. The nightly automation, "Renewal Rescue", built by a customer-success manager, live since 2 August: 274 emails and 212 credits (₪32,436), no cap; a ₪2,448 credit reversed by its builder; three Enterprise admins emailed, including Shaked Clinics on 27 October.
- F7. 11 agents and automations found, 3 in IT's inventory, 5 acting on customers, 3 tokens orphaned by leavers.
- F8. Dashboard 63.2% vs 7-day resolution 35.5%.
- F9. 6 of 123 emails to addresses not on the account. F10. A crude injection got ₪500 on 3 November.
- F11. The GA design's 2FA "verification" uses facts printed on every invoice (reported by Andrei; procedure ASP-2).
- F12. The AI disclosure string is empty in Arabic and Russian; 76 sessions flagged for pasted pay, ID or bank data (reported by Nurit: the LLM provider is not on the DPA's sub-processor list).

**What the transcripts missed:** Yonatan was never asked what happened after 13:20 or about the other languages; Andrei was never shown the 02:00 rows; Maya was never asked what was promised outside the company; Nurit was never asked about the data customers paste.

</details>

## References

- OWASP GenAI Security Project, [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) and [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) (checked 3 November 2026).
- Field kit: [01.6 · The shadow-AI census](../module-01/lesson-06.md), [01.7 · The AI inventory from zero](../module-01/lesson-07.md), [02.1 · Stakeholder map](../module-02/lesson-01.md), [02.2 · The discovery interview](../module-02/lesson-02.md), [02.7 · Writing a findings memo](../module-02/lesson-07.md).
- Templates: [stakeholder map](../../templates/stakeholder-map.md), [interview guide](../../templates/interview-guide.md), [AI inventory](../../templates/ai-inventory.md), [findings memo](../../templates/findings-memo.md).
- Previous: [14.1 · The call](lesson-01.md). Next: [14.3 · Diagnosis](lesson-03.md).
