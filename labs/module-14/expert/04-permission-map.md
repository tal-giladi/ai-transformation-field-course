# 04 · Agent permission map — Lumen Assist (and Renewal Rescue)

*Expert deliverable for lesson 14.4, using the [agent permission map](../../../templates/agent-permission-map.md)
template. v1, Thursday 7 January 2027. Owner: Maya Rosenthal (VP Product); operator: Head of AI Operations;
reviewed by Andrei Kogan (security) and Nurit Gal (privacy). Legal readings are Nurit's view, not legal advice.*

## 1. Agent card

| Field | Value |
|---|---|
| Purpose | Resolve routine account and billing questions inside Lumen Shifts, and hand everything else to a person with the conversation attached |
| Accountable owner / operator | Maya Rosenthal / Head of AI Operations (Support) |
| In scope at Lumen Live | Starter and Growth customers; Hebrew, English, Arabic, Russian; Israel, EU, US |
| Out of scope | Enterprise (opt-in later, read-only first); trial accounts get read and ticket only |
| Identity | Its own service identity `svc-lumen-assist`; scopes `accounts:read`, `billing:credit` (gateway-limited), `plans:write` (Starter/Growth), `users:2fa` (verified flow only), `email:send` (address on file only), `tickets:write`. No `data:delete`, no `data:export`. `svc-support-admin` is withdrawn from the agent |
| Model and prompt | Provider and model as contracted; prompt v8. Any change of model, prompt, tool or limit = re-run every must-refuse test before release |
| Knowledge | Help-centre revisions approved for the agent: policy articles (billing, plans, security, privacy) need Billing or Support approval **in every language**; the agent reads only the approved revision; auto-translation of policy articles is reviewed before it is published |
| Kill switch | Revoke `svc-lumen-assist` and drain the tool queue (one command, R&D on-call or Head of AI Ops); target under 30 minutes to no further tool execution; tested 14 January with Andrei (queued credit and email did not execute) |
| Log and audit trail | Full trace per conversation: customer message, sources read (article and revision), each tool call with arguments, approvals (who, when), result, identity; reviewed daily at 17:00 (20 minutes); kept 12 months, then aggregated (retention set with Nurit) |
| Disclosure | "You're chatting with Lumen Assist, an AI assistant…" in all four languages at the first message |
| Register | AI register entry AI-001 |

## 2. Actions

The target (stage 2, from week 3) is in the rung column; stage 1 differences are in bold.

| Action | Worst realistic case | Band | Last reversible moment | Rung | Limits | Enforced where | Approver, capacity | Must-refuse tests |
|---|---|---|---|---|---|---|---|---|
| Read account | Reads the wrong customer's data | easy | n/a (reads only) | 3 executes alone | Session-bound: only the signed-in customer's account | Tool layer (account id from the session, never from text) | — | — |
| Issue credit | Money paid on a false policy, an injection or a scripted burst | easy | Before the invoice run (Thursday 22:00) | 3 within limits (**stage 1: 1 approver**) | ≤ ₪300 each; ≤ ₪2,000 a day in total; 1 per customer a day; Starter and Growth | Credit gateway in the tool layer; billing already denies contract accounts | Shift lead, stage 1: ~11 a day × 2 min | N-01–03, N-09–11, N-13, N-16, N-17, N-19, N-20 |
| Change plan | A contract cut without the account lead; seats removed by mistake | window | Before billing syncs (48 h for contracts); next invoice for self-serve | 1 approver | Starter and Growth only; no move to or from Enterprise | Tool layer (plan and target checked) | Shift lead, ~6 a day × 2 min | N-07, N-08, N-18 |
| Reset 2FA | Account takeover; staff records exported | none | Before the attacker signs in (~30 min) | 3 only after verification | Only after a callback or confirmation link on the channel already on file; never on answers to questions | Verification service issues a one-time token the tool requires; the model cannot produce it | — | N-04, N-21 |
| Delete data | Years of schedules, staff and payroll records gone; records that had to be kept | none | The delete itself | 0 not granted | — (the agent opens a ticket to privacy-requests) | Scope not granted | DPO's process | N-05, N-14, N-15 |
| Email customer | Invoices with bank details or staff data sent outside the customer | none | The send | 3 within limits | Only to the admin email on the account; the tool takes no address argument | Tool layer | — | N-06, N-12 |
| Create ticket | None; it is how the agent says "not me" | easy | n/a | 3 executes alone | — | — | Support queue | — |

**Why each rung** (one line each, as presented to the executive staff):

- *Read account:* executes alone; reading is the agent's whole job and changes nothing.
- *Issue credit:* executes alone under a ₪300 cap, ₪2,000 a day and one credit per customer a day, Starter and
  Growth only: the routine ₪40–₪140 credits flow, everything bigger or stranger goes to a person, and anything
  wrong is caught before the invoice run. One approver for the first two weeks while the log builds evidence.
- *Change plan:* one approver, Starter and Growth only: six a day is cheap to approve, and Enterprise seats are a
  contract the account lead negotiates.
- *Reset 2FA:* executes alone, but only after verification on a channel already on file. The rule stops the
  urgent, plausible caller that a tired approver waves through.
- *Delete data:* not granted; deletion is a privacy process the DPO owns (identity, what must be kept,
  confirmation). The agent opens a ticket instead.
- *Email customer:* executes alone, only to the address already on the account. An address taken from a message
  or a file is exactly how data leaves.
- *Create ticket:* executes alone; without it, every refusal leaves the customer to start again.

## 3. Global controls

| Control | Product design | This map |
|---|---|---|
| Identity | Shared `svc-support-admin` | Own `svc-lumen-assist`, least scopes |
| Logging | Actions to the warehouse, weekly report | Full trace, daily review at 17:00 |
| Kill switch | Feature flag (hides the widget) | Revoke the identity and drain the queue; tested |
| Prompt rule | The only limit | Kept, as a bonus; never counted as a control in the tests |
| Knowledge | Every published article, any language | Approved revisions only, per language |
| Approvals | None | Credits (2 weeks) and plan changes; ~17 a day against ~30 |

## 4. Renewal Rescue: approved with guardrails

Decision (with Michal Biton and Shira Navon, 23 December): **keep it**, under these conditions, effective 10
January. Until then it runs with credits off and a plan filter (done 11 December).

| Action | Rung | Limits | Enforced where |
|---|---|---|---|
| Read usage and accounts | 3 | Growth plan only (by plan, not seat count) | Token scope and query; the token cannot read Enterprise accounts |
| Send email | 3 | Admin email on file; template with model-written personal paragraph; weekly sample of 10 read by Shira and Michal | Tool layer (no address argument) |
| Goodwill credit | 3 | ≤ ₪150; one per account per 90 days; ≤ ₪1,000 a night | Credit gateway per identity |

Identity `svc-renewal-rescue` (owner Shira, accountable Michal); kill switch: revoke the identity (Andrei or
Head of AI Ops), no laptop needed; register entry AI-002; must-refuse tests: an Enterprise account in the query
result, an annual account (amount must use the monthly bill), a second credit within 90 days, an address not on
file. Effect measured honestly: at-risk Growth renewals compared with a held-out 20% of flagged accounts that get
no email from February.

## 5. The fleet: rules that make the register real

1. **No token without a register entry** (owner, purpose, data, scopes, kill switch). Andrei's team issues
   tokens only against an entry; existing tokens are re-issued by 31 January or revoked.
2. **One identity per agent or automation.** `svc-support-admin` returns to its 2024 purpose (the Deskly sidebar)
   with scopes cut to what the sidebar uses; scripts get their own short-lived tokens.
3. **Offboarding includes tokens.** The 3 tokens whose creators left (`svc-support-admin`, `mkt-zapier`,
   `lumengpt-slack`) get new owners or are revoked by 31 January; `assist-worker-staging` loses production scopes
   (done 14 December).
4. **Anything that writes to customers or to what customers read** (the 5 in the fleet) has a permission map;
   the rest a one-line register entry.
5. **Monthly**: tokens without activity for 60 days are revoked; card expenses for AI and automation services are
   matched to the register (Finance flags unmatched ones).

## 6. Rules that reach the agent (Nurit's reading, for routing; not legal advice)

| Layer | What it means for Lumen Assist | Owner, action |
|---|---|---|
| Israel: Privacy Protection Law (חוק הגנת הפרטיות) as amended by Amendment 13 (in force 14 August 2025); Data Security Regulations (תקנות אבטחת מידע) | Lumen holds customers' staff data on their behalf; using conversations for a new purpose (fine-tuning) is a purpose question; an account takeover exposing staff records could be a severe security incident to report | Nurit: purpose review before any fine-tuning; retention for traces; incident criteria in the runbook |
| Israel: PPA draft guidance on AI (April 2025, still a draft) | The regulator's view of the direction for AI that processes personal data | Nurit: read against the design before GA |
| Customer DPA | Processing only to provide the Service (4.1); sub-processors listed with 30 days' notice (6.1); the LLM provider is not listed | Nurit: notice to customers; it needs to go out by 10 January for 9 February |
| EU AI Act, Annex III (as amended by Regulation (EU) 2026/1744) | A support agent for software admins is not in the Annex III list; the scheduling product's auto-allocation is a separate question | Nurit: Q1 note on auto-scheduling |
| EU AI Act, Article 50(1) and 50(5) | People must be told they are interacting with an AI system unless obvious, at the latest at the first interaction; applies from 2 August 2026; the Omnibus did not change 50(1) | Noam: disclosure in Arabic and Russian (done 14 December) |
| EU AI Act, Article 50(2) (machine-readable marking of AI-generated text) | Whether and how it applies to Assist's replies | Question to Nurit, with the provider's terms |
| OWASP Top 10 for LLM Applications 2025 and for Agentic Applications 2026 | LLM01 prompt injection, LLM06 excessive agency; agentic goal hijack, tool misuse, identity and privilege abuse, memory and context poisoning, human-agent trust exploitation | Me: each one has a must-refuse test or a red-team script (05) |

## 7. Shaked Clinics, section 7: draft answers (to Amir, 7 January; signed by Nurit and Amir)

- **7.1** Two AI systems have processed Shaked data: Lumen Assist is not enabled for Shaked (Enterprise is
  excluded); a customer-success email automation sent one AI-written email to Shaked's admin on 27 October 2026
  (a credit it attempted was refused by billing). That automation no longer selects Enterprise accounts.
  Internal tools (meeting notes, an internal assistant) are listed with the data they can see.
- **7.2** Yes; Enterprise customers are opted out by default; opt-in per system.
- **7.3** From 31 January every AI system acts under its own identity, listed in our register.
- **7.4** Attached: every AI action in Shaked's tenant, 90 days (two rows).
- **7.5** No AI system can delete data. 2FA changes require verification on a channel already on file; no AI
  system acts for Enterprise.
- **7.6** Shaked's data is not used to train or tune models; any change would be notified under clause 14.6.
- **7.7** One incident affecting customers (not Shaked): a replaced help article led to incorrect credits for 11
  days in November 2026; corrected, controls added (wording by Nurit).
- **7.8** Head of AI Operations, with the General Counsel (privacy) and the CISO (security).
