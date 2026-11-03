# 03 · Baselines, the fleet and the shortlist

*Expert deliverable for lesson 14.3. To: Revital Azoulay; 20 minutes with Yaron Ben-David. Thursday 17 December
2026. Labels: **measured** (from the data room, reproducible), **directional** (measured on a small or biased
sample), **assumed** (a number we chose and will replace).*

## 1. Resolution: one definition, measured

| Definition | Beta, 11 Oct – 26 Nov (1,599 sessions) | Label |
|---|---|---|
| Dashboard: session ended without "Talk to a person" | 63.2% | measured, but counts abandoned sessions and bug tickets |
| **7-day resolution:** closed or abandoned, and no ticket and no new session on the same intent within 7 days | **35.5%** | measured |

By intent (7-day): invoice questions 50.2% (448 sessions), credits 46.5% (187), notifications 40.0% (60), payroll
32.3% (164), how-to 31.6% (354), plan changes 22.5% (142), bugs 9.8% (153, correctly handed to engineering),
2FA 4.3% (70, the agent cannot reset). By language: Hebrew 37.3%, Russian 35.4%, English 33.7%, Arabic 33.3%.

**The trap in the best number:** downgrade questions "resolved" 81.0% in 7 days, because customers who were
wrongly credited did not come back. A resolution rate needs a quality check beside it: a weekly sample of
resolved conversations read against policy (20 a week, 20 minutes of a shift lead).

**The target restated:** "50% resolved without a person by end of Q2" becomes "7-day resolution from 35.5% to
45% by 30 June 2027, with no rise in wrong actions found in the weekly sample". 45% is **assumed**: it is what
moving credits and Starter plan changes to the agent and fixing the how-to articles would give if they behave
like invoice questions; the monthly gate checks it.

## 2. What the agent would carry at GA, and what people would carry

| Item | Per working day | Label |
|---|---|---|
| Beta sessions | 42 (420 customers + trials) | measured |
| Beta handoffs to people | 15.7 | measured |
| GA agent requests, Starter and Growth (Product's projection) | ~80: 50 look-ups, 11 credits, 6 plan changes, 3 2FA resets, 10 bug tickets | directional |
| Approvals if credits and plan changes need one approver (stage 1) | ~17 × 2 min = 34 min | directional |
| Approval capacity (two shift leads, 30 min a shift) | ~60 min = 30 approvals | measured (shift plan) |
| Daily review of the full trace | 20 min | assumed |
| A handed-off request | 12 min of a person | assumed (support's estimate) |

Approvals for every action that changes something (credits, plan changes, 2FA resets) would be about 20 a day
for Starter and Growth, and about 40 with Enterprise: over the 30-a-day capacity, i.e. rubber stamps. Approvals have to be spent where they buy safety: money and plan changes,
for two weeks.

## 3. The fleet (inventory, 17 December)

| # | Agent / automation | Owner | Acts on customers? | Identity | In IT inventory |
|---|---|---|---|---|---|
| 1 | Lumen Assist beta | Product | Credits, plan changes, emails | shared `svc-support-admin` | yes |
| 2 | Renewal Rescue (n8n + OpenAI) | CS | Credits, emails | shared `svc-support-admin` | no |
| 3 | Trial nurture (Zapier + OpenAI) | Marketing (creator left) | Trial extensions, emails | `mkt-zapier` | no |
| 4 | Help-centre translation (DeepL) | Marketing | Publishes what customers and Assist read | `svc-translate` | no |
| 5 | Assist staging worker | Product | Can credit, change plans, email (production scopes) | `assist-worker-staging` | no |
| 6 | LumenGPT Slack bot (Claude API) | R&D (creator left) | Exports customer staff lists into Slack | `lumengpt-slack` | no |
| 7 | Invoice dispute triage (Make + OpenAI) | Finance | Reads billing, writes tickets | `finance-make` | no |
| 8 | Churn score notebook (Gemini) | Data | Reads accounts, usage, tickets | `churn-score` | no |
| 9 | Support-ops ChatGPT Team workspace | Support | Customer exports pasted by staff | none (approved tool) | no |
| 10 | Microsoft 365 Copilot pilot | IT | Internal email and documents | user identities | yes |
| 11 | Meeting-notes AI | Sales | Customer call recordings | vendor | yes |

11 found, 3 registered, 5 acting on customers, 3 tokens orphaned by leavers. Card spend on AI and automation
services January–November: about ₪31,950 across 7 departments (`saas-expenses-ai-2026.csv`).

## 4. The real bottleneck

Not the model's accuracy: it answered correctly whenever its sources were right. The bottleneck is **authority
and visibility**: no per-action limits outside the model, one shared identity, no inventory, no change control
on what agents read, a stop that does not stop. Every candidate below depends on fixing that first.

## 5. Shortlist (agentic opportunity frame and fast screen, 03.2–03.3)

| Candidate | Verdict | Condition |
|---|---|---|
| A. Lumen Assist GA for Starter and Growth with a permission map and staged autonomy | **Go with conditions** | Own identity; limits in the tool layer; tested kill switch; source control; disclosure in four languages; must-refuse tests pass |
| B. The fleet register and per-agent identities (no AI: a register, token policy, offboarding) | **Go** | Owner: Andrei with me; every token tied to a register entry by 31 January |
| C. Renewal Rescue | **Go with guardrails** | Own token, Growth by plan, cap, address on file, weekly sample, a switch others can use |
| D. Assist for Enterprise | **Not yet** | Opt-in per customer after Shaked's questionnaire is answered; read-only first |
| E. Agent deletion and agent 2FA resets without verification | **Never delegate** | Deletion stays the DPO's process; 2FA only after verification on file |

## 6. One-page case (to Revital and Yaron)

**Ask:** launch Lumen Assist at Lumen Live for Starter and Growth under a permission map, money on approval for
two weeks, then wider on evidence; Enterprise later by opt-in.
**Measured:** 7-day resolution 35.5%; ₪19,368 credited from one replaced article in 11 days; 8 actions after the
"kill switch"; 11 agents, 3 registered. **Directional:** ~80 requests a day at GA; 17 approvals a day in stage
1. **Assumed:** 45% 7-day resolution by end of June.
**Cost:** the budgeted engineer (identity, tool-layer limits, kill switch, source approval: about 6 of the 12
weeks); about 1 hour a day of shift-lead time in weeks 1–2 (approvals plus review), then 20 minutes.
**Cost of waiting:** none of the fixes depends on 9 February, but every week the shared token, the orphaned tokens
and the Arabic and Russian HC-214 stay as they are is a week of exposure without a launch to show for it.
**What a "no" means:** Lumen Live shows a demo; the beta continues as it is (which is the riskier option).
