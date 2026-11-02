# Agent-assist pilot: charter and offline eval report

Expert deliverable for lesson 08.5. Charter v1.0 signed 17 December 2026 (Orly, Meseret, Hila for the
policy text); eval report v1.0, Thursday 7 January 2027. Templates: [pilot
charter](../../../templates/pilot-charter.md), [test-set spec](../../../templates/test-set-spec.md),
[eval report](../../../templates/eval-report.md), [human-review design](../../../templates/human-review-design.md).

> [!NOTE]
> The **rules baseline, "today" and negative-test numbers are real**: run the commands in
> `labs/module-08/README.md` and you get them exactly. The **LLM and hybrid figures are an illustrative
> worked example** from the course's story (the team's runs of prompt v1.2 with a mid-tier model on 28
> December – 4 January, rated 4–6 January); they were not measured by the course authors and describe no
> real model. Your run will differ.

## Part 1 — Pilot charter (summary)

**Hypothesis.** For written contact (email, web form, WhatsApp), a draft whose decision comes from rules
on order data and whose wording comes from an LLM, checked and sent by an agent, gives answers
consistent with policy v2 in all four languages, with review time low enough to free capacity.

**Scope.** Written tickets in Hebrew, Arabic, Russian, English; Amharic and any other language go to a
person. Not the phone; not the chatbot. Offline only until the steering decision.

**Rule of use.** The draft may propose a decision and an amount; only the agent may send. The agent may
change anything; every change of decision is logged with a reason. Escalation flags go to the team
lead the same day. No draft goes out unread.

**Thresholds for "go to shadow mode" (agreed 17 December, before any run):**

| # | Threshold | Why |
|---|---|---|
| G1 | Decision right on ≥ 92% of returns tickets in the test set, ≥ 88% in every language | Today 55.6%; rules alone 79.6% |
| G2 | Fee right on ≥ 95% of tickets where a fee is due | Money |
| G3 | Escalation recall ≥ 95% | Legal threats and injuries must reach a person |
| G4 | 0 banned phrases (store credit only, 10%, "30 days full refund") | The old policies must not leak |
| G5 | All 12 negative tests pass | Each is a known failure |
| G6 | Drafts accepted (as-is or light edit) ≥ 75% overall, ≥ 70% per language, rated blind by native speakers | Value |
| G7 | Median review ≤ 1.5 minutes in shadow mode (offline rating time is directional only) | Below 2.0 the pilot loses money (pilot-economics) |

**Stop rules.** Any banned phrase or wrong refund sent to a customer in shadow mode → pause and re-test;
policy v2 not published by 1 February → the pilot does not go live.

**Value measurement plan.** Indicator the budget owner reviews: cost per order (Boris). Paired quality
metric: repeat-contact rate (BI's new measure). Counterfactual: phased release by desk (Hebrew desks
first; Arabic and Russian desks two weeks later); measure for 8 weeks.

## Part 2 — Test set

2,000 written tickets (1 Sep – 31 Oct 2026, company-wide, random), split with a fixed seed into 300 for
development and 1,700 frozen for test; 200 of the test tickets form the spreadsheet (Track A) set.
Labels: intent, language, decision and fee under policy v2, escalation, today's reply coded; labelled by
two agents per language, disagreements adjudicated by Meseret with Hila on policy questions. Plus 12
negative tests written by hand (injection, a claimed bot promise, French, the four-month rule with and
without a conversation, a personalised item with a defect, an injury, another person's data, a lawful
fee disputed, a late delivery, Amharic, a deletion request). Personal details were removed before
labelling. Not covered: phone, attachments (photos), follow-ups after a draft was sent.

## Part 3 — Eval report

**Verdict.** **Go to shadow mode** on 1 February for the hybrid design (the model reads and writes, rules
decide), Hebrew and English desks first, Arabic and Russian from 15 February after 100 native-rated
drafts each; **on condition** that policy v2 is published by 1 February. The model-decides design (LLM
alone) is rejected: it misses G1 and G2.

**Decision and fee (test set, returns tickets n = 691).**

| Design | Decision right | ar | he | ru | en | Fee right | Label |
|---|---|---|---|---|---|---|---|
| Today (agents' replies, coded) | 55.6% | 65.2% | 54.7% | 54.8% | 46.2% | — | measured |
| Rules only (keywords + rules + templates) | 79.6% | 91.3% | 78.8% | 72.6% | 76.9% | 80.6% | measured |
| LLM decides (prompt v1.2) | 87.4% | 85.9% | 88.2% | 84.5% | 88.5% | 85.3% | illustrative |
| **Hybrid: LLM reads and writes, rules decide** | **95.8%** | 95.7% | 96.3% | 94.0% | 96.2% | 97.5% | illustrative |

Rules alone fail when the keywords miss a paraphrase ("the money hasn't reached my account") and send the
ticket to "n/a" (60 of 307 cancellations, 40 of 183 defects). The LLM alone computes fees wrongly on
round prices and applies the four-month rule to web orders. Hybrid errors: 18 of 29 are late deliveries
the order dates do not show, 7 are "opened" items the customer describes as used.

**Intent:** rules 78.4% (measured); hybrid 94.6% (illustrative). **Escalation recall:** rules 68.2%
(58 of 85, measured); hybrid 96.5% (82 of 85, illustrative; missed: two Arabizi legal threats, one
"I'll go to small claims" in Russian). **Banned phrases:** rules 0, hybrid 0, LLM alone 3 (repeated the
customer's "30 days"); today 140 of 1,700 agent replies (measured). **Negative tests:** rules 3 of 12
(measured); hybrid v1.1 10 of 12 (N-02 confirmed the bot's 30-day promise; N-08 offered to "check with
the neighbour's order"), v1.2 adds "never confirm a promise the customer says someone else made" and
"never discuss another customer's order": 12 of 12 (illustrative).

**Drafts rated blind (illustrative).** 260 hybrid drafts (he 100, ar 60, ru 60, en 40) and 40 real agent
replies mixed in; raters: Nadia's desk (ar), the Russian desk lead (ru), two Hebrew agents, the English
desk lead.

| Language | Rated | Accepted (as is + light edit) | Safety issues |
|---|---|---|---|
| Hebrew | 100 | 84% | 1 |
| Arabic | 60 | 73% | 1 (standard Arabic to a dialect message, judged cold) |
| Russian | 60 | 78% | 1 (formal register missed) |
| English | 40 | 85% | 0 |
| **All** | **260** | **81%** | **3** |

Agents' real replies in the blind set: 52% accepted; 13 of 19 rejections were policy errors. Median
rating time 1.1 minutes (a rater at a desk: directional for review time).

**Cost.** Two calls a ticket, about 2,800 tokens in and 450 out: at Claude Sonnet 5.5 list prices
(US$2 / US$10 per million, checked 2 November 2026) and ₪3.136 per US$, ≈ ₪0.032 a ticket, ≈ ₪420 a
month for 13,200 drafted tickets. Not decisive.

**Time (pilot-economics, assumptions labelled).** 22,000 written tickets a month, 60% drafted, 80%
accepted, 4.0 minutes saved per accepted draft (assumed, to be timed in shadow mode), 1.0 review minute,
3.0 rework minutes, ₪88 an hour, ₪12,000 a month fixed: **352 net hours, ≈ ₪18,600 a month of capacity**,
breakeven on a ₪150,000 build in 8.1 months. Breakeven acceptance 67%; at 2.0 review minutes the pilot
loses money. Capacity, not cash, until the April gate decides what the hours are for.

**Gates.**

| Gate | Result | Label | Production must still show |
|---|---|---|---|
| G1 | 95.8%; lowest language ru 94.0% | illustrative (on the frozen test set) | Weekly sample of sent replies vs policy |
| G2 | 97.5% | illustrative | Fee check on every drafted refund |
| G3 | 96.5% | illustrative | Every flag reaches a team lead the same day |
| G4 | 0 | illustrative | Automatic check on every draft |
| G5 | 12 of 12 (v1.2) | illustrative | Re-run on every prompt or model change |
| G6 | 81%; ar 73% | illustrative | 100 native-rated drafts per language in shadow mode |
| G7 | 1.1 min rating time | directional | Timer in the helpdesk |

**Not tested:** phone; photos; volume at peak; reviewers under load; customers' reactions; drafts after
policy v2 is live with customers (repeat-contact effect).
