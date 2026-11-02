---
id: "09.1"
module: 9
minutes: 16
practice_minutes: 80
prerequisites: ["01.1", "01.2", "01.4", "01.5"]
objectives:
  - "Separate the claims in a sponsor's proposal from what the data room verifies, on the first day."
  - "Write the objective in the sponsor's words, read it back, and map who decides what in a regulated insurer."
  - "Write an internal lead's engagement charter that separates what is already live from what is proposed."
  - "Plan the first week so that every stakeholder who can stop the work is heard before the first paper."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 1, The AI Transformation Advisor (framing and scoping an engagement)"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution (Coursera) — course 4, AI Governance, Risk, and Responsible Deployment"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
  - title: "Inter-ministerial team, Artificial intelligence in the financial sector — final report (December 2025; Bank of Israel, CMISA, ISA, Ministries of Justice and Finance, Competition Authority)"
    url: https://www.boi.org.il/media/rh0bejl4/aireport.pdf
last_verified: "2026-11-02"
---

# 09.1 · The call

Meridian Mutual, a mid-size Israeli insurer, hired you as its first Head of AI Transformation. On your fourth day the COO hands you a proposal she has already half-sold: automate claims intake and spot fraud with tools the claims system delivered in September, in a pilot that starts in four weeks. In this lesson you read the data room before you react, get the objective in her words, find out who can say yes and who can say stop, and write the charter and first-week plan. At the end you have a charter that keeps the decision open, and a first week that reaches everyone who could stop you.

## The situation

Wednesday 4 November 2026, 08:30, the COO's office. You started on Sunday 1 November, reporting to
Ilana Bar-Lev, COO. Above you on AI risk sits the board's risk management committee; its secretary is
the Chief Risk Officer. Ilana gives you draft 2 of her proposal and a deadline: "Tell me by Sunday how
you'll run it." She presents it at the management meeting on Tuesday 10 November; the committee meets
on 15 December.

This is module 1 again, from a different seat. In module 1 you were the person who was handed AI at a
120-person importer; here you are a hired executive in a supervised company, with a committee above
you and a vendor already inside. IBM's advisor course calls this step framing and scoping the
engagement; this lesson does it with the real files. Read the [engagement brief](../../labs/module-09/brief.md)
and the data room's `INDEX.md` (in the module download) before you go on.

## What to do

### Step 1 — Read the room before you react to the proposal

Do the first-day read from [01.5](../module-01/lesson-05.md) with the
[data-room first read](../../templates/data-room-first-read.md) template. Sort every number in the
proposal into *verified* (you can see where it comes from and it means what it says), *reported*
(someone says so) and *claim* (someone selling something says so). At Meridian, by Sunday:

| Number in the proposal | Where it comes from | First read |
|---|---|---|
| "Average claim handling time 10.5 days" | BI dashboard, October | Reported. The definitions say: from status "file complete" to "decision", claims under SIU handling excluded. That is not the claimant's wait. |
| "Handling time −30%, to 7.3 days" | Ilana, from the 10.5 | A target on a definition nobody has checked |
| "Smart Intake 97.4% field accuracy" | Kalanit release notes | Claim. Footnote 1: 500 typed Hebrew motor forms at 300 dpi in Kalanit's lab |
| "The SIU prevented ₪6,770,153 this year" | Dashboard | Reported. Definition: claimed minus paid on SIU cases closed, whatever the outcome |
| "₪20M a year of fraud" | Kalanit's email of 20 October | Claim. "Industry studies put fraud at around 10% of claims paid", no source |
| "No AI makes or supports decisions on claims" | Risk committee minutes, 15 June | Contradicted: Fraud Insight has scored every motor claim since 6 September (the register's `fi_score` column starts that day) |

Then list what is **missing**: a cycle time from first notice to payment; confirmed fraud by case
(the register only has a SUSPECT flag); the logic of the fraud score; any assessment of the 9.4
modules (the minutes' action 6.1 promised one "before use"); the DPO's view; agents' first-notice
dates (agents' claims never enter the CRM); CRM history before May 2026. A missing document is a
finding about how the organization governs itself, not only a gap in your folder.

### Step 2 — Get the objective in her words and read it back

[01.2](../module-01/lesson-02.md) taught the sponsor conversation. Ilana's proposal is a solution
("Smart Intake everywhere, Fraud Insight on home, buy Pro"). Ask what would be different if it worked,
and for whom. Her answer in the pre-run interview: claimants paid sooner, fewer chasing calls, agents
in the North stop complaining, a "48-hour claims" advertising campaign in the spring, and "money" from
fraud.

Read it back as an outcome you can measure, not as the proposal:

> "So the outcome is: claimants paid sooner and fewer chasing calls, without more cost, shown before
> the spring campaign; and fraud we catch that we don't catch today. If I find a faster way to that
> than the pilot, you want to hear it, first, from me."

Two things just happened. The pilot became one possible route, and fraud became something that has
to be *caught*, which later lets you count only confirmed fraud.

### Step 3 — Map who decides what

An internal lead in a regulated company has less authority than the title suggests. Write it down:

| Decision | Who decides | Where it is written |
|---|---|---|
| Pilot money up to ₪250,000 | COO with the CFO | `finance-summary.md` |
| Fraud Insight Pro (₪380,000 × 3 years = ₪1.14M) | Board | Finance approval levels |
| Any AI use that "makes or materially supports a decision about a customer's claim" | Risk management committee, **before production** | AI policy, rules 2 and 3.2 |
| AI features delivered inside existing software | Same as a new AI system | AI policy, rule 3.3 |
| Configuration of a live Kalanit module | Business owner by change request | Kalanit agreement, 7.3 |
| Privacy | DPO advises; General Counsel for anti-discrimination law | Org chart |

The table already shows a problem nobody has said aloud: two high-impact uses (by the policy's own
words) have been in production since 6 September without the committee's approval. You do not raise
it as an accusation in the first meeting. You write the decision-rights table, and the gap is visible
on it.

The inter-ministerial report on AI in the Israeli financial sector (December 2025) is useful framing
here: responsibility for an AI system stays with the financial institution that operates it, even
when a vendor built it. It is a set of recommendations, not a binding instruction; Meridian's own AI
policy is what binds you.

### Step 4 — Know what changes because you are internal

[01.1](../module-01/lesson-01.md) compared the three ways in. For an internal head of AI:

- **No exit points.** A consultant can leave after phase one. You will own whatever is approved for
  years, including the things you did not stop.
- **Independence has to be built.** The committee needs to hear from someone who is not only the
  project's owner. Ask for a dotted line to the CRO on AI risk, with the reason, in the first meeting.
- **Your sponsor's proposal is already promised upward.** She has a management meeting on Tuesday.
  Your job is to keep the decision open without humiliating her, and to agree now how bad news reaches
  her: before anyone else, never first in front of the CEO.
- **Access is easier, but not free.** You can walk the floor; data still goes through the DPO, as
  pseudonymised extracts.

### Step 5 — Scope: separate what is live from what is proposed

The proposal mixes three things: two modules already running, an extension of them, and a purchase.
Your charter treats them separately, because the committee must decide about the live ones whatever
happens to the pilot.

| In scope | Out of scope (for now), and why |
|---|---|
| Non-bodily-injury claims: motor property, home, health, travel | Bodily injury and compulsory motor (a litigation unit, a different process) |
| The live modules: Smart Intake (motor, two centres) and Fraud Insight (all motor) | The website chatbot and call transcription (already in the inventory, other owners) |
| The proposal: extension, Pro, the winter pilot | Underwriting and pricing (not asked; would bring other rules) |
| An offline pilot on pseudonymised documents | Anything live during December–February until the evidence says so |

### Step 6 — Plan the first week around the people who can stop you

Use the [30-60-90 / first-week plan](../../templates/30-60-90-plan.md) from [01.4](../module-01/lesson-04.md).
Build the list from the decision-rights table, not from Ilana's calendar: the VP Claims (process owner),
a frontline handler, the SIU, BI (the dashboard), the Chief Actuary, the CRO, the DPO, internal audit,
a claimant, the vendor. The [stakeholder map](../../templates/stakeholder-map.md) from
[02.1](../module-02/lesson-01.md) helps you order them. Put the ones whose answers change your
questions first (Claims, BI), the vendor last (you want your own numbers before you hear his).

### Step 7 — Write the charter

Use the [engagement charter](../../templates/engagement-charter.md) template, adapted for an internal
lead (no fee, no exit clauses; a reporting rule and a line to the CRO instead). One page for the
objective, scope, decision rights, deliverables with dates, how you work, and risks; the first-week
plan and the first-day read as annexes.

## Watch out

- **Accepting the pilot as the scope.** The ask is a solution. Charter the outcome and the decision;
  the pilot is one option. If you charter "deliver the winter pilot", every later finding becomes an
  obstacle to your own charter.
- **Using the vendor's numbers as baselines.** 97.4%, AUC 0.81 and ₪20M are claims until you know what
  they were measured on. Write them in the "claim" column on day one.
- **Forgetting what is already live.** The committee's first question will be about September, not
  December. If your charter is only about the pilot, you have scoped yourself out of the biggest risk.
- **Promising the committee a "yes".** You can promise evidence by a date. The committee decides.
- **Leaving the bad-news rule implicit.** Agree it in the first meeting: what you tell her, how fast,
  and that she hears it first.
- **Interviewing only the sponsor's allies.** Internal audit, the DPO and a claimant are not optional
  in an insurer.

## Your turn

### Inputs

- [Engagement brief](../../labs/module-09/brief.md) and the data room in the module download:
  `INDEX.md`, `company/`, `plans/pilot-proposal-2026-11.md`, `reports/claims-kpi-dashboard-2026-10.md`,
  `policies/ai-policy-2026.md`, `governance/` (minutes, inventory), `vendor/kalanit-claims-9.4-release-notes.md`,
  `vendor/email-kalanit-fraud-insight-pro-2026-10-20.md`.
- Persona: [Ilana Bar-Lev](../../labs/module-09/personas/ilana-coo.md) (or the
  [pre-run transcript](../../labs/module-09/personas/transcripts/ilana-coo.md)); feedback with the
  [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [data-room first read](../../templates/data-room-first-read.md),
  [engagement charter](../../templates/engagement-charter.md), [30-60-90 plan](../../templates/30-60-90-plan.md).

### Steps

1. Do the first-day read: every number in the proposal and the dashboard sorted into verified,
   reported, claim or contradicted, with the file it comes from; then a list of what is missing.
2. Interview Ilana (roleplay, 20–30 minutes). Find out: the objective in her words; who decides what;
   how the 9.4 modules came to be switched on; what the CEO and the board have already heard; how she
   wants bad news. Read the objective back. Run the coach prompt on your transcript.
3. Write the decision-rights table from the policy, the minutes, the finance summary and the agreement.
4. Write the charter (one page plus annexes): objective as read back, scope with reasons, decision
   rights, deliverables and dates up to the committee, how you work (reporting, the line to the CRO,
   data access), risks.
5. Write the first-week plan: who, why, in what order, what you need from each.

### Time

80 minutes: 20 for the first read, 25 for the interview and coach, 10 for decision rights, 25 for the
charter and first-week plan.

### Done when

- [ ] Every number in the proposal has a label and a source; at least one is marked contradicted.
- [ ] The objective is in the sponsor's words and describes an outcome, not a tool.
- [ ] The charter separates the live modules from the proposal and names the committee's role for both.
- [ ] Decision rights are written with the document each comes from.
- [ ] The first week includes internal audit, the DPO and a claimant, and puts the vendor last.
- [ ] There is a written rule for how bad news reaches the sponsor.

<details><summary>Reference answer</summary>

The full charter is in the module download: `labs/module-09/expert/01-charter-and-first-week.md`.
Excerpts:

**Objective (read back on 4 November).** "Claimants paid sooner and fewer chasing calls, without more
cost, shown before the spring campaign; and catch fraud we don't catch today." Agreed: the outcome is
the claimant's wait and the cost of handling, measured end to end; fraud counts when it is confirmed.

**What the charter commits to.** Evidence for a decision, not the winter pilot: by 15 December a
deployment verdict on what is live and what is proposed; by late January a tested pilot and a
recommendation. The pilot's shape may change; Ilana hears first.

**First-day read (extract).**

| Claim | Status |
|---|---|
| Handling time 10.5 days, 96.0% within 30 | Reported: starts at "file complete", excludes SIU |
| Fraud prevented ₪6,770,153 YTD | Reported: claimed − paid on all closed SIU cases |
| Smart Intake 97.4% | Claim: lab, typed Hebrew forms |
| Fraud Insight AUC 0.81 | Claim: label is the SUSPECT flag (footnote 2) |
| ₪20M a year | Claim: no source |
| "No AI makes or supports claims decisions" (15 June) | Contradicted by the 9.4 go-live, 6 September |

Missing: a first-notice-to-payment cycle time; confirmed fraud by case; the fraud score's logic; the
assessment promised in action 6.1; the DPO's view of Smart Intake; agents' first-notice dates; CRM
before May 2026.

**How I work.** Weekly to Ilana (Thursday) and the same day for anything urgent; never first in front
of the CEO. Dotted line to the CRO on AI risk. Data through the DPO, pseudonymised, every extract
logged.

**First week.** Sun: charter, first read, interview guide. Mon: claims process walk with Yusuf
Darawshe. Tue: health and travel desk (Marina Kogan), one hour listening in the contact centre. Wed:
SIU and BI (dashboard definitions). Thu: first read to Ilana; claimant call arranged by the complaints
officer. Following week: Chief Actuary, CRO, DPO, internal audit; Kalanit last.

**What the pre-run interview missed.** Who decided to leave the modules on (Ilana did, in August, and
action 6.1 was never done), and that the CEO has already heard "₪20M". Both come back in 09.4 and 09.6.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 1 (framing and scoping; named, not re-taught); IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 4.
- Inter-ministerial team, [AI in the financial sector, final report](https://www.boi.org.il/media/rh0bejl4/aireport.pdf) (December 2025, Hebrew): responsibility stays with the institution; recommendations, not binding.
- Field kit: [01.1 · Three ways in](../module-01/lesson-01.md), [01.2 · Getting a real mandate](../module-01/lesson-02.md), [01.4 · The first-week plan](../module-01/lesson-04.md), [01.5 · Access and the first-day data-room read](../module-01/lesson-05.md), [02.1 · Stakeholder map](../module-02/lesson-01.md).
- Templates: [data-room first read](../../templates/data-room-first-read.md), [engagement charter](../../templates/engagement-charter.md), [30-60-90 plan](../../templates/30-60-90-plan.md), [stakeholder map](../../templates/stakeholder-map.md).
- Next: [09.2 · Discovery](lesson-02.md).
