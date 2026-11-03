# Lumen SaaS — writer's notes for module 14 (never imported)

The seventh Stage 2 engagement. The learner is **an internal hire: the new head of AI operations**,
reporting to the VP Support, in a 250-person Israeli B2B software company. The stated ask is "ship an AI
agent that resolves customer issues in the product". The hard part (14.4) is **agentic AI**: tool
permissions, the authority ladder, recoverability and the last reversible moment, identity and the audit
trail. 14.5 builds the **agent permission map**, the **negative tests** (every action the agent must
refuse), a **scripted red-team** and a **staged-autonomy plan**; Track B runs them in a small harness
against a mock agent (tool calls simulated, no real systems) with `fieldkit.llm` (mock provider proves it
runs). The data room is built by `labs/module-14/data-room/generate.py` (seed 20261129, standard library
only). The ground truth is only in this file. Never link it from lessons.

## The organization

- **Lumen SaaS Ltd.** (לומן), Tel Aviv (Yigal Alon Street), founded 2014 by Yaron Ben-David (CEO) and
  Eyal Dahan (VP R&D). **About 250 people.** Product: **Lumen Shifts**, shift scheduling, time clock and
  payroll-prep software for shift-based businesses (retail, clinics, logistics, restaurants, light
  industry). Sold to SMBs in **Israel, the EU and the US**.
- **About 3,100 business customers** on **Starter, Growth, Enterprise** (matches the `agent-authority`
  preset). Enterprise seats are contracts negotiated by the commercial account leads; Starter and Growth
  are self-serve with monthly or annual billing. Exact counts, seats, ARR by tier and country come from
  `customers/customers.csv` (filled into the profile by the generator).
- Product UI in Hebrew, English, Arabic and Russian. Support works Sunday–Thursday 08:00–18:00 Israel
  time plus an on-call engineer; widget open 24/7.
- Systems (fictional names): admin console and **Admin API** (service tokens with scopes); billing
  ("Pinkasit") with a **weekly invoice run on Thursday at 22:00** (credits can be reversed until the
  account's next invoice run); helpdesk ("Deskly", reused name); help centre (CMS, marketing can publish);
  feature flags ("Flagpole"). Lumen Assist is built on a commercial LLM API behind Lumen's own tool layer.
- Policies (match the preset): support **people** may credit up to **₪500** per case; above that the
  account manager; outage credits for enterprise are in the contract; enterprise seats are the commercial
  account lead's; deletion is a privacy process the DPO owns; 2FA resets only via a channel already on
  file; enterprise contract changes sync to billing **after 48 hours**; deletions are soft for **14
  days** in the admin console (but the Admin API's `DELETE` is hard — planted, see 14).

## Who the learner is

A new **Head of AI Operations**, started **Sunday 29 November 2026**, reporting to **Revital Azoulay,
VP Support** (the sponsor). The role was created after the CEO's October board update. Internal, not a
consultant: no fee, no exit clause, but a 90-day plan, a budget and a seat at the executive staff meeting
on the agent decision. Budget December 2026 – March 2027: **₪380,000** (contract platform engineer 12
weeks ₪210,000; external red-team exercise ₪60,000; tooling and model usage ₪40,000; shift-lead
training ₪20,000; reserve ₪50,000). What is new for an internal role (14.1): you will own whatever you
approve; you inherit what is already running; your peers (VP Product, CISO) are not your clients.

## Stated ask vs hidden truth

- **Stated ask.** The CEO told the board on 21 October 2026: Lumen Assist, "an AI agent that resolves
  customer issues inside the product", ships to every customer at **Lumen Live on Tuesday 9 February
  2027**, target **50% of support contacts resolved without a person by the end of Q2 2027**. VP Product
  Maya Rosenthal's GA design: all seven tools (read account, issue credit, change plan, reset 2FA, delete
  data, email customer, create ticket), each executing alone, a prompt rule for limits, **shared admin
  identity** (`svc-support-admin`), action log, no kill switch beyond a feature flag. This is the preset's
  `startConfig`. The executive staff decides GA scope on **Wednesday 27 January 2027**.
- **Hidden truth.** The question is not whether the model is smart enough. **Lumen already runs agents
  it cannot list, attribute or stop**, and one of them already did harm nobody wrote up.
  1. **The beta already failed, quietly.** In the closed beta (11 Oct – 26 Nov 2026, 420 opted-in
     Starter and Growth customers, tools: read account, issue credit with a ₪500 prompt rule, email
     customer to any address, create ticket; change plan added for Starter on 1 Nov) marketing replaced
     help article HC-214 "Downgrades and refunds" on **Monday 9 November 16:40** with a campaign draft
     promising credit for unused annual months. The agent retrieved it and credited annual downgraders.
     First wrong answer **Wednesday 11 November**; discovered **Sunday 22 November** by support engineer
     Yonatan Tadesse from Tavor Engineering's ticket: **11 days**. Article restored the same day. No
     postmortem; some credits had already been invoiced.
  2. **The kill switch is a UI flag.** The runbook's "kill switch" is the feature flag `assist_enabled`;
     it hides the widget but queued tool jobs keep running. On 22 November the flag went off at 13:20;
     agent tool calls continued until 14:31.
  3. **Shared identity, no attribution.** The agent, the CSM's bot and two engineers' scripts all act as
     `svc-support-admin` (created 2024 for a helpdesk integration; scopes include `data:delete`). The
     audit log cannot say who did what without user-agent and timing forensics.
  4. **An unattended agent built by a business user.** Shira Navon (customer-success manager) built
     **"Renewal Rescue"** in n8n cloud, live since **2 August 2026**: nightly at 02:00 it pulls Growth
     accounts renewing within 60 days whose usage fell, has an LLM write a personal email to the admin,
     sends it, and applies a "retention goodwill" credit of 10% of the monthly bill with no cap. It uses
     the shared token. It works (renewal of flagged accounts up vs before) but: one ₪2,448 credit (10% of
     the *annual* bill, a formula bug on annual accounts), it selected accounts by seat count and so
     emailed **three Enterprise admins**, including **Shaked Clinics**, offering "a lighter plan". Right
     answer: **approve with guardrails**, not stop.
  5. **A fleet nobody can list.** IT's AI inventory (September 2026) lists 3 items. The tokens, audit log
     and expenses show **11** agents and automations that touch customer data or accounts, **5 of them
     writing** to customer accounts; 3 tokens belong to people who have left.
  6. **The commercial stake.** Shaked Clinics (Enterprise, renewal 31 March 2027, the largest ACV in
     the file) sent a security questionnaire due **15 January 2027** asking to list every AI system with
     write access to its tenant, whether it can opt out, and for the audit trail. Lumen cannot answer
     truthfully today, and its own bot has already suggested a cheaper plan to Shaked's admin.
  7. **"61% resolved" counts closed widgets.** Product's beta dashboard counts any session the customer
     closed without asking for a person. With "no ticket and no new session on the same topic within 7
     days" it is 35.5%.
- **The honest answer.** Do not ship the demo configuration on 9 February. Ship at Lumen Live, to
  Starter and Growth only, the **permission map** (the preset's expert config as the week-3 target) with
  **staged autonomy**: weeks 1–2 read and tickets alone, credits and plan changes on one approver within
  the 30-a-day approval capacity, full trace and daily review; widen only on log evidence; delete and
  enterprise contracts stay with people; email to the address on file only; 2FA only after verification
  on file; the agent's **own identity**, a **tested kill switch** at the tool layer, **change control on
  help-centre documents** the agent reads; every must-refuse test before go-live and after every change.
  Enterprise: opt-in only, after the Shaked questionnaire is answered. Renewal Rescue: approved with
  guardrails (own identity, credit cap ₪150, Growth only by plan not seats, address on file, named owner,
  in the register, kill switch). The fleet: a register and owner for every token by 31 January, the
  leavers' tokens revoked. Answer Shaked truthfully. The 50% target restated as a measured resolution
  rate with a 7-day definition.

## Planted findings (each discoverable, never stated)

| # | Finding | Where |
|---|---|---|
| 1 | Replaced help article retrieved by the agent; wrong credits for 11 days | `support-kb/help-centre-revisions.csv`, `assist-beta/retrievals.csv`, `assist-beta/tool-calls.csv`, `billing/credits-ledger.csv`, `support/tickets.csv` |
| 2 | Kill switch exists only on paper (flag hides UI; jobs continue) | `product/assist-incident-runbook.md`, `it/feature-flags-log.csv`, `assist-beta/tool-calls.csv` |
| 3 | Shared admin identity for agent, bot and scripts | `it/api-tokens.csv`, `it/admin-audit-log.csv` |
| 4 | Unattended citizen-built agent (Renewal Rescue): nightly credits and emails, uncapped, the ₪2,448 credit, Enterprise admins emailed | `it/admin-audit-log.csv`, `billing/credits-ledger.csv`, `it/saas-expenses-ai-2026.csv`, `customers/customers.csv` |
| 5 | Fleet nobody can list: 3 in the inventory vs 11 in the evidence; leavers' tokens | `it/ai-inventory-2026-09.csv` vs tokens, audit log, expenses, `people/staff-directory.csv` |
| 6 | Shaked's questionnaire Lumen cannot answer; renewal at stake | `legal/shaked-security-questionnaire-2026-11.md`, `customers/enterprise-contracts.csv` |
| 7 | "Resolved" = widget closed; 7-day resolution far lower | `company/assist-beta-dashboard-2026-11.md` vs `assist-beta/sessions.csv` + `support/tickets.csv` |
| 8 | Email tool sent to addresses not on the account | `assist-beta/tool-calls.csv` vs `customers/customers.csv` (admin email domain) |
| 9 | Injection attempt that partly worked: the agent credited the prompt-rule maximum (₪500) to a trial account | `assist-beta/transcripts-sample.md`, `assist-beta/tool-calls.csv` |
| 10 | AI disclosure string missing in Arabic and Russian | `product/widget-strings.csv` |
| 11 | Staff pay data pasted into chats; conversation logs kept with no retention limit; plan to fine-tune on them | `assist-beta/sessions.csv` (`pii_flags`), `product/assist-ga-design.md`, `legal/customer-dpa-extract.md` |
| 12 | Approval capacity: one shift lead an hour a day ≈ 30 approvals | `people/support-shifts.csv`, `product/assist-ga-design.md` (assumes approvals are free) |
| 13 | A social-engineering 2FA attempt on the phone, refused by procedure | `support/tickets.csv`, `policies/account-security-procedure.md` |
| 14 | Admin console delete is soft (14 days) but the API delete is hard; the GA design uses the API | `policies/data-deletion-procedure.md`, `product/assist-ga-design.md` |
| 15 | Help-centre publishing: marketing can publish policy articles without support or billing review | `policies/help-centre-publishing.md`, revisions |

## The cast (persona pack)

| Persona | Role | Type | Hidden / unlock |
|---|---|---|---|
| Revital Azoulay | VP Support | Sponsor | Knew about the 22 Nov incident and chose not to write it up before Lumen Live ("I didn't want to give Maya's critics a weapon"); her team's headcount plan for 2027 already assumes 50% deflection (4 fewer hires). Unlock: "what has already gone wrong in the beta?"; "what does your 2027 plan assume?" |
| Maya Rosenthal | VP Product | Pusher | Promised Lumen Live to a reseller partner and the press; the design's "prompt rule" is the only limit; wants beta conversations to fine-tune. Unlock: what was promised externally; "where is the ₪500 limit enforced?"; data plans |
| Yaron Ben-David | CEO | Executive | Board was told 50%; investor update in March; would accept a narrower launch if it is framed as "first agent with an authority ladder" and Shaked is protected. Unlock: what the board actually needs; the Shaked number |
| Andrei Kogan | CISO | Security | Knows `svc-support-admin` exists and is over-scoped, never had time; wants to block all agents until Q3; does not know about Renewal Rescue. Unlock: token inventory; "what would make you say yes for Starter?" |
| Shira Navon | Customer-success manager | Citizen builder | Built Renewal Rescue; got the token from a departed engineer's wiki page; knows about the ₪2,448 credit (refunded it quietly); does not know it emailed Enterprise admins. Unlock: no blame + "show me how it works"; ask about the token; show the audit-log row for Shaked |
| Amir Haddad | Commercial account lead, Enterprise | Commercial account lead | Shaked renewal ₪ (largest ACV) at stake; procurement said "your own team offered us a cheaper plan"; Negev Retail wants to cut seats; wants Enterprise excluded from the agent entirely. Unlock: the questionnaire; "what did Shaked's procurement say?" |
| Yonatan Tadesse | Support engineer, tier 2 | Frontline | Found the stale article on 22 Nov; saw tool calls after the flag went off; refused a social-engineering 2FA call on 6 Nov; approves credits as backup shift lead. Unlock: "walk me through the 22nd"; "what happened after you switched it off?" |
| Nurit Gal | General counsel and DPO | Counsel | Never asked about the beta's data; the DPA allows processing "to provide the Service" only; Article 50 disclosure; deletion via API with no retention check. Names exposure; won't decide priority. Unlock: show the session log with pay data; ask about EU customers and disclosure |
| Svetlana Mor | Office manager and Lumen admin, Tavor Engineering (Growth) | The person affected | Was promised credit for unused months, got ₪1,100, then a reversal email with no explanation; pasted her staff pay table into the chat; uses the product in Russian and did not know the assistant was an AI. Unlock: ask what happened in her words; ask what language she uses |

Transcripts leave hidden: Revital's 2027 headcount assumption; Maya's promise to the reseller; Yaron's
investor update; Andrei's not knowing about Renewal Rescue (interviewer never shows him); Shira's ₪2,448
refund; Amir's Negev seat cut; Yonatan's post-flag tool calls and the unfixed Arabic and Russian article;
Nurit's concern about pasted staff data and retention, and the auto-scheduling question; Svetlana's language.

## Timeline

- 2024-03: `svc-support-admin` token created for a helpdesk integration (owner: an engineer who left in
  June 2026).
- 2026-08-02: Renewal Rescue live. 2026-09-14: IT AI inventory (3 items). 2026-10-04: ₪2,448 credit.
- 2026-10-11: closed beta starts (420 customers). 2026-10-21: board update ("50% by Q2").
- 2026-11-01: change plan tool added (Starter). 2026-11-06: 2FA social-engineering call refused.
- 2026-11-09 Mon 16:40: HC-214 replaced. 2026-11-11 Wed: first wrong answer. 11 Nov – 22 Nov: wrong credits.
- 2026-11-22 Sun: Tavor ticket → Yonatan finds it; flag off 13:20; tool calls until 14:31; article
  restored 14:05; billing reverses what is not yet invoiced.
- 2026-11-24: Shaked questionnaire received (due 15 Jan). 2026-11-26: beta data cut-off.
- **Sun 29 Nov 2026: learner starts (14.1).** 30 Nov – 10 Dec discovery (14.2; Hanukkah 4–12 Dec);
  Thu 17 Dec diagnosis to Revital (14.3); 20 Dec – 7 Jan the permission map (14.4); 10–21 Jan negative
  tests, red-team, staged plan (14.5); Fri 15 Jan Shaked answer due; Wed 27 Jan executive staff decides
  (14.6); Tue 9 Feb Lumen Live; Wed 31 Mar Shaked renewal. Six months later: August 2027.

## The futures (14.6 debrief)

1. **Ship the demo.** All seven tools at Lumen Live. Within a month: an urgent-caller 2FA reset on an
   enterprise admin (the Shaked pattern at another Enterprise customer), staff records exported, PPA
   notification and customer notices; a CSV-borne instruction emails invoices to a lookalike domain;
   credits from a second replaced article. Shaked does not renew. Agent switched off in April; it takes a
   release to stop it. Deflection never measured honestly.
2. **The permission map with staged autonomy (expert path).** Starter and Growth at Lumen Live with the
   map; weeks 1–2 on approvals (peak 27 a day, inside capacity); credits move to execute-alone under ₪300
   / ₪2,000 / one per customer in week 3 on log evidence; 7-day resolution rises from 35% to 49% by June;
   two must-refuse failures caught in regression tests after a prompt change; Renewal Rescue re-launched
   under its own identity; the register lists 11 agents, 3 retired; Shaked answered truthfully, opted out
   of the agent for the first year and renewed for three years. The board target restated as 7-day
   resolution.
3. **Freeze everything.** The CISO's "no agents until Q3" wins. Lumen Live shows a demo only. Renewal
   Rescue moves to Shira's personal Make account with a copied token; the fleet keeps growing out of
   sight; support hires the four people the plan cut; a competitor ships an assistant and two Growth
   resellers switch.

What decides it: whether the beta incident and the fleet reach the executive staff before 27 January,
and whether the decision is made per action rather than for "the agent".

## Additional findings added while building the data room

- **16. A prompt rule is not a limit.** All 12 wrong credits were above the system prompt's "never above
  ₪500" (₪504 – ₪4,032): the prompt also says "the help centre is the source of truth", and the article won.
  Nothing outside the model enforced the ₪500. (`tool-calls.csv`, `assist-system-prompt-v7.md`.)
- **17. The fix was incomplete.** On 22 November only the English and Hebrew HC-214 were restored. The Arabic
  and Russian versions are still the campaign text (`svc-translate`, 10 Nov 03:00, v5; index current_revision
  5). Four of the 12 wrong credits came from Russian conversations, one from Arabic.
- **18. The LLM provider is not a listed sub-processor** in the customer DPA (Annex B), and the GA design plans
  to fine-tune on conversations that contain staff pay and ID numbers (purpose limitation; route to the DPO).
- **19. Billing already enforces one limit outside the model**: credits on Enterprise contract accounts are
  denied by Pinkasit ("finance approval required") whoever asks — the one place complete mediation exists.
- **20. LumenGPT Slack bot** (R&D, token `tok_08`, creator left 15 Aug) exports customer staff lists into
  Slack on request (18 exports Sep–Nov).
- **21. Staging token with live scopes**: `tok_09 assist-worker-staging` holds `billing:credit plans:write
  email:send` on production, last used 9 Oct, expires 31 Dec.

## The fleet (the answer to "list every agent")

| # | Agent / automation | Owner | Evidence | Acts on customers? | In IT inventory? |
|---|---|---|---|---|---|
| 1 | Lumen Assist beta | Product (Maya / Noam) | tool calls, `tok_01` UA `lumen-assist-worker` | Yes: credits, plan changes, emails | Yes |
| 2 | Renewal Rescue (n8n + OpenAI) | CS (Shira) | `tok_01` UA `n8n`, 02:00; ledger "retention goodwill"; CS card expenses | Yes: credits, emails | No |
| 3 | Trial nurture (Zapier + OpenAI) | Marketing (creator left) | `tok_07`; Marketing card expenses | Yes: trial extensions, emails | No |
| 4 | Help-centre translation (`svc-translate` + DeepL) | Marketing | revisions; DeepL expense | Yes: publishes what customers and Assist read | No |
| 5 | Assist staging worker | Product | `tok_09` live scopes | Can (credits, plans, email) | No |
| 6 | LumenGPT Slack bot (Claude API) | R&D (creator left) | `tok_08`, account.export; R&D expense | Exports staff lists internally | No |
| 7 | Invoice dispute triage (Make + OpenAI) | Finance | `tok_10`; Finance expenses | Reads billing, writes tickets | No |
| 8 | Churn score notebook (Gemini) | Data | `tok_11`; Data expense | Reads accounts, usage, tickets | No |
| 9 | Support-ops ChatGPT Team workspace | Support | expense; AUP lists it | Customer exports pasted (approved tool) | No |
| 10 | Microsoft 365 Copilot pilot | IT | inventory | Internal email and documents | Yes |
| 11 | Meeting-notes AI | Sales | inventory; expense | Customer call recordings | Yes |

11 agents and automations, 3 in the inventory, 5 act on customers (1–5), 3 tokens whose creator has left
(`tok_01`, `tok_07`, `tok_08`). `svc-support-admin` (`tok_01`) is shared by Assist (258 audit actions),
Renewal Rescue (369) and engineers' scripts (49), and holds `data:delete`.

## Where each finding is planted (actual numbers, seed 20261129)

Computed from the generated files with `labs/module-14/discovery.py` and `stats.py`; all reproducible in a
spreadsheet. Paths relative to `labs/module-14/data-room/`.

- **Volumes.** Customers 3,100 active (Starter 1,640 / Growth 1,340 / Enterprise 120) + 42 trials + 75
  churned rows; ARR ₪50.5M (Starter ₪3.54M, Growth ₪24.23M, Enterprise ₪22.75M); Israel 2,101, EU 609, US
  390. Beta: 420 customers (IL 325, US 54, CY 24, GR 17) + 42 trials; 1,599 sessions (he 746, en 579, ru
  178, ar 96); 1,307 tool calls; 2,768 retrievals; 1,983 tickets; 826 credits; 1,778 audit rows.
- **Resolution.** Dashboard 63.2% ("no handoff"); 7-day (closed or abandoned, no ticket or repeat session
  on the same intent within 7 days) 35.5%. Outcomes: closed 630, abandoned 248, handoff 589, ticket 132.
  CSAT 3.8 on 210 ratings (13%).
- **HC-214.** v5 en 9 Nov 16:40 (maisa.hamdan, Marketing), he 16:52, ar/ru 10 Nov 03:00 (svc-translate);
  v6 en/he 22 Nov 14:05/14:09 (yonatan.tadesse); ar/ru still v5. 13 downgrade conversations in the window,
  12 credits (one handoff), ₪19,368; first credit 11 Nov 09:14 (AS-01083, ₪1,656); last 22 Nov 13:47
  (AS-01430, ₪2,952, after the flag). 8 applied by the 12 and 19 Nov invoice runs (₪11,952, left as
  goodwill); 4 reversed (₪7,416), Tavor's ₪1,104 on 23 Nov 09:12. 6 downgrade conversations before and 2
  after answered correctly (no credit). Discovery: ticket from Tavor 22 Nov 09:40, escalated 10:05.
- **Kill switch.** Flag off 13:20; 8 tool calls requested before and executed after (7 emails, 1 credit),
  last 14:31. No sessions between 13:20 and 16:00.
- **Prompt rule.** 12 beta credits above ₪500, all from HC-214.
- **Injection.** 3 sessions: 17 Oct (refused, ticket), 3 Nov trial account (₪500 "maximum" credited, applied
  on the 5 Nov run), 19 Nov (refused).
- **Email.** 6 of 123 sends to addresses not on the account (5 personal webmail, 1 accountant).
- **PII.** 76 sessions with PII flags (4.8%), incl. Tavor's pasted pay table.
- **Renewal Rescue.** 2 Aug – 26 Nov: 274 nightly emails; 212 credits ₪32,436 (10% of monthly bill; largest
  ₪2,448 on 4 Oct to C-10941, 85 seats, annual — reversed 6 Oct by shira.navon; next largest ₪530); 3
  Enterprise admins emailed (C-10083 9 Sep, Shaked C-10337 27 Oct, C-10329 15 Nov), their credits denied by
  billing. At-risk annual Growth renewals (active users −40% or worse): before 2 Aug 45.1% renewed (n=82),
  after 50.0% (n=46): directional, no control group.
- **Shaked.** C-10337, 2,600 seats, ₪13.50, modules ₪96,000, ACV ₪517,200 (largest), 36-month term ending
  31 Mar 2027, AI clause 14.6; questionnaire due 15 Jan. Negev Retail C-11021, 400 seats at ₪12.50, ACV
  ₪77,000; 2FA impersonation call 6 Nov 17:42 refused (callback to number on file).
- **Approvals.** Two shift leads, 30 minutes each per shift, 5 days: about 60 minutes a day = 30 approvals
  at 2 minutes (matches the preset's `approvalCapacity` 30).
