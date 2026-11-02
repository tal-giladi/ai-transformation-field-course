---
id: "05.5"
module: 5
minutes: 18
practice_minutes: 75
prerequisites: ["05.4"]
objectives:
  - "Test a human check against four conditions (information, authority, time, competence) and fix the one that fails."
  - "Run the capacity screen: review minutes per item × items per day against the reviewer-hours actually available, at peak."
  - "Design against the three reasons reviewers stop checking: flags that go nowhere, load, and a tool that is usually right."
  - "Write who is accountable when a wrong draft is sent, and how AI-drafted replies are marked inside and outside the company."
volatility: concept
sources:
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution (Coursera) — course 4, AI Governance, Risk, and Responsible Deployment (designed vs effective oversight, capacity screen)"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
  - title: "IBM Enterprise AI Transformation and Consulting (Coursera) — course 6, AI Governance, Risk, and Executive Communication (reviewer complacency, misattributed responsibility, detectability)"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Pearl Cohen — Israel: New Draft Guidelines on the Application of Privacy Law to AI (notify people when they interact with a bot; 4 May 2025)"
    url: https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/
  - title: "EU AI Act, Article 50 (transparency obligations; human review or editorial control exception in 50(4); applies from 2 August 2026) — AI Act Explorer"
    url: https://artificialintelligenceact.eu/article/50/
last_verified: "2026-11-02"
---

# 05.5 · Human-in-the-loop design that actually checks

"A human reviews every draft" is the most reassuring sentence in an AI proposal and the least tested. A reviewer who does not see the order data cannot catch a wrong date; one with 120 drafts and 4 hours cannot read them; one whose flags disappear stops raising them; and one reviewing a tool that is right nine times in ten starts trusting it the tenth time. In this lesson you test Harbor & Pine's review step against four conditions, size it with the capacity screen, design against the three reasons reviewers stop checking, decide who is accountable when a wrong draft goes out, and decide how drafted replies are marked. At the end you have a human-review design that the steering committee can see is a working control, not a sentence.

## The situation

Monday 11 January 2027. The eval report ([05.4](lesson-04.md)) recommends shadow mode from 1 February. Every gate-1 number depends on the review: acceptance is the reviewers' verdict, review time is their minutes, and "wrong replies reaching customers" is what they miss. The ROI model ([03.7](../module-03/lesson-07.md)) budgets 2 minutes per draft, 64 hours a month at peak, and calls the review "the biggest cost line". Samir will ask the steering committee on 19 January for the agents' time; Ronit will ask whether 2 minutes is real.

IBM's governance course calls this the gap between **designed** and **effective** oversight and gives the **capacity screen**; the consulting certificate adds **reviewer complacency** (two causes: flags with no consequence, and load on a usually-right system) and **misattributed responsibility**: a control is real only if the named person has the time, the source beside the draft, and the authority to stop it. Here you design all of it for one team.

## What to do

### Step 1 — Test the check against four conditions

For every human check, ask four questions. A "no" to any of them means the check is designed but will not be effective.

| Condition | The question | Harbor & Pine before the design |
|---|---|---|
| **Information** | Does the reviewer see what they need to judge the draft, beside it? | No: the draft would appear in the reply box; the order, the ETA and the customer's original message are three clicks away in Priority and Deskly |
| **Authority** | May they discard, change or stop it without justifying themselves to anyone? | Partly: they may discard, but the charter's switch belongs to Samir and you only |
| **Time** | Do they have the minutes a real check takes, on the busiest day? | Unknown until the capacity screen (Step 2) |
| **Competence** | Can they tell a right draft from a wrong one: language, product, policy? | Not for every language: Hebrew-only agents would review Arabic drafts in a busy hour |

### Step 2 — Run the capacity screen at peak

The screen compares the minutes a **real** check takes with the minutes people actually have:

- **Volume:** 3,200 written contacts a month at peak × 60% drafted ÷ 22 working days ≈ **90 drafts a day**, about 112 on a Sunday after the weekend.
- **Real check:** about 3 minutes when the reviewer has to look up the order and the ETA; about 2 minutes (1.95) when they are shown beside the draft. Screen: 60 ÷ 3 = **20 drafts per reviewer-hour**, or 60 ÷ 1.95 ≈ **31** with the source shown.
- **Need:** 90 × 3 = 270 minutes = **4.5 reviewer-hours a day** (5.6 on Sunday) without the source; 90 × 1.95 ≈ **2.9 hours** (3.7 on Sunday) with it.
- **Available:** Samir can give at most **6 agent-hours a day** to checking in peak season, at 92% utilisation.

Now compare with the money. The ROI model's 2 minutes a draft is 64 hours a month. A 3-minute check is 99 hours a month: 35 hours the case has not paid for, in the peak, from a team already at 92%. Showing the source beside the draft is therefore not a nice-to-have: it is what makes the business case's 2 minutes true. It goes into the integration scope (the helpdesk panel shows the original message, the order context line and the flags next to the draft), and gate 1 (b) measures it.

### Step 3 — Design against the three reasons reviewers stop checking

Reviewers rarely decide to stop checking. They drift, for three reasons, each with a design answer:

1. **Flags that go nowhere.** An agent marks a draft "wrong date" and nothing happens: the next day's drafts make the same mistake, and nobody tells them. After a week they stop marking, then stop looking. *Design:* every discard reason goes into a weekly prompt review (05.7), and on Thursday the team hears in one line what changed because of their marks ("dates in Russian drafts now come only from the order line: thanks to the 14 marks this week").
2. **Load.** When the queue is longer than the time, people stamp: they send the draft after a glance, because the queue is visible and a wrong draft is not. *Design:* a load rule: when the drafts waiting exceed what the day's review hours can check (the screen), new tickets get triage only and no draft, so agents write from scratch rather than stamp. Writing from scratch is slower and safe; stamping is fast and is the failure the gate measures.
3. **A tool that is usually right.** At 82% acceptance, a reviewer sees about one wrong draft in five; as the prompt improves to one in twenty, attention falls further, and the remaining errors are the subtle ones (a date in words, an Arabic register). *Design:* point verification where errors cluster instead of asking for general vigilance: a three-line "check these" list per category on the panel (WISMO: the date matches the order line; returns: no promise of money or deadline; damage: photos asked, nothing promised), and flagged drafts cannot be sent "as is" without opening the flag.

Try it in the simulation before you write it down. With the Harbor & Pine preset (90 drafts a day, 3 agents × 1.5 hours, one draft in five wrong, a 3-minute check), the educational model gives these results over two working weeks, out of about 181 wrong drafts:

| Design | Wrong replies reaching customers | Share caught | Reviewer-hours a day |
|---|---|---|---|
| As planned (no source shown, no flag feedback) | about 65 | 64% | 4.5 |
| Source shown beside the draft only | about 41 | 77% | 4.5 |
| Flag feedback only | about 37 | 80% | 4.5 |
| A fourth reviewer, nothing else changed | about 55 | 70% | 6.0 |
| **Source shown and flag feedback** | **about 9** | **95%** | **4.5** |

The target (at most 10 in two weeks within 6 agent-hours a day) is met only with both changes. More reviewers without them buys little: the model's vigilance falls when flags go nowhere, whatever the head count. And in the same model, a better tool with only one draft in twenty wrong, no feedback and no source, still lets about 19 through and catches only 57%: the usually-right tool is the hardest one to keep checking.

[Simulation: Oversight under load](../../simulations/oversight-under-load/index.html?preset=harbor)

### Step 4 — Make sure the reviewer is competent for this draft

- **Language:** Arabic drafts go only to Lina, Rami, Ahmad or Samir; Russian only to Olga, Yana or Sergei; English to Daniel or anyone who passes a short check; Hebrew to everyone. The helpdesk routes by the draft's reply language, not the customer's profile.
- **Product and policy:** the "check these" list per category, and the training session in module 6 (7–11 February) practises it on 20 real drafts, including five planted wrong ones.
- **Spot audit:** Olga (Russian, Hebrew) and Lina (Arabic) re-read 20 sent drafted replies per language per week. This is the gate-1 (c) sample and also how reviewers learn what they missed.

### Step 5 — Decide who is accountable when a wrong draft is sent

When a wrong reply reaches a customer, the easiest finding is "the agent should have caught it". If the agent had no source beside the draft, 112 drafts on a Sunday and an Arabic draft they could not read, that finding blames a person for a design failure; IBM's course calls the result misattributed responsibility. Write the rule before the first incident, into the review design and the incident runbook (lesson 07.5):

> When a drafted reply that reaches a customer is wrong, the review first answers four questions:
> did the reviewer have the information beside the draft, the time that day (load against the
> screen), the authority to discard or stop, and the language and training for this draft? If any
> answer is no, the finding is a design failure and the owner of the design fixes it. Only if all
> four are yes is it a review error, handled as coaching, never discipline for a first case.

This is also what Samir negotiated in the charter: override logs per language and week, never per agent. People who expect to be blamed for the tool's errors either stop using it or stop marking its mistakes.

### Step 6 — Decide how AI-drafted replies are marked

Two different questions:

- **Inside the company: always.** Every drafted ticket carries the rule-of-use fields (draft used as is / edited / discarded, prompt version, model). Without the mark you cannot audit an incident, measure acceptance or re-run the eval on what was actually sent.
- **To the customer: decide with counsel, and write the decision down.** The reply is sent by a named agent who read it, so the customer is not talking to a bot. The Privacy Protection Authority's draft AI guidance (2025, still a draft) expects organizations to tell people when they interact with a bot and to explain the purposes of AI processing. The EU AI Act's Article 50(4), which applies from 2 August 2026, requires deployers to disclose AI-generated text published to inform the public on matters of public interest, with an exception where a person reviewed it and holds editorial responsibility; Harbor & Pine sells in Israel and private replies to customers are not publications to the public, so it is unlikely to reach this pilot, which is a question for counsel, not you. A reasonable Harbor & Pine decision: the privacy notice (module 4) says that staff use an approved AI tool to help draft replies, which they check and send; no per-message label; the agent's name stays on every reply. Counsel confirms or changes it before 1 February.

### Step 7 — Write it as a human-review design

One page, with the [human-review design](../../templates/human-review-design.md) template: what is reviewed and by whom; what the reviewer sees; what to check per category; the capacity screen at peak with the hours it needs and who gives them; the load rule; authority (discard, flag, pause); competence (language routing, training, spot audit); the feedback loop; the accountability rule; marking. The steering committee should be able to see from it that the review is staffed and funded, not only promised.

## Watch out

- **"Human in the loop" with no numbers.** Without the capacity screen at peak, the loop is a hope. Minutes per real check × drafts a day, against hours someone has actually given.
- **Adding reviewers instead of fixing the design.** Without the source on screen and flags that lead somewhere, more people check badly together.
- **A review step that never discards.** If the discard rate falls towards zero while acceptance is 82% offline, nobody is reading. Watch the discard rate (05.7).
- **Blaming the last person.** Ask the four questions first. Most wrong replies trace to missing information, time or language, not to carelessness.
- **Marking decided by default.** Not deciding is a decision customers and regulators can read later. Write it down, with counsel's view.

## Your turn

### Inputs

- Your eval report from [05.4](lesson-04.md) and charter from [05.1](lesson-01.md); the ROI model's review line from [03.7](../module-03/lesson-07.md).
- Data room (module download): `company/customer-service-handbook.md` (languages, escalation), `people/timesheets.csv` (utilisation), `policies/privacy-notice.md`.
- Simulation: [Oversight under load](../../simulations/oversight-under-load/index.html?preset=harbor).
- Template: [human-review design](../../templates/human-review-design.md).

### Steps

1. Fill the four-condition table for the review as planned in the charter.
2. Run the capacity screen at peak, with and without the source beside the draft; compare with the ROI model's 64 hours.
3. Play the simulation: find a design that meets the target (≤ 10 wrong replies in two weeks, ≤ 6 agent-hours a day), then try a "better model" (lower the error rate) with feedback off and note what happens.
4. Write the three design answers to the three reasons reviewers stop checking.
5. Write the language routing, the "check these" lists for four categories, and the spot audit.
6. Write the accountability rule and the marking decision (with the question for counsel).
7. Put it on one page with the template.

### Time

75 minutes: 10 for the four conditions, 10 for the screen, 20 for the simulation, 20 for the design answers and routing, 15 for accountability, marking and the page.

### Done when

- [ ] Every condition (information, authority, time, competence) is answered yes by the design, or has a named fix.
- [ ] The capacity screen is computed at peak and on Sunday, and the hours it needs are given by a named person and match the ROI model, or the gap is stated.
- [ ] Each of the three reasons reviewers stop checking has a design answer that changes something on screen or in the routine.
- [ ] The accountability rule names the four questions asked before anyone is blamed.
- [ ] The marking decision is written down for inside and outside, with the question for counsel.

<details><summary>Reference answer</summary>

**Human-review design — reply drafts — v1.0, 14 January 2027** (owner: Samir Haddad; author: pilot lead)

| Part | Design |
|---|---|
| What is reviewed | Every draft, before sending, by the agent who sends it. Nothing is sent without a person pressing send |
| What the reviewer sees | Beside the draft: the customer's original message, the order context line (order, item, promised date, updated delivery date from the date fix), the flags with their reason, the model's one-line note. Facts that came from the order line are highlighted; `[CHECK: …]` markers block sending until filled |
| What to check (panel, per category) | WISMO: the date equals the order line; no passed promise. Returns: no money, fee or deadline promised. Damage: photos and order number asked, nothing promised. Complaint: apology without admitting fault, senior follow-up named |
| Capacity screen at peak | 90 drafts a day (112 Sunday); real check 1.95 min with the source shown → 2.9 h a day (3.7 Sunday); 64 h a month = the ROI model's line. Without the source: 4.5 h (5.6 Sunday), 99 h a month, 35 h unfunded. Samir gives up to 6 agent-hours a day |
| Load rule | When drafts waiting exceed the hours left that day ÷ 1.95 min, new tickets get triage only, no draft, until the queue is under it. The switch is automatic; Samir is told |
| Authority | Any agent discards or rewrites without giving a reason beyond the one-click field; any agent can add a flag; only Samir or Olga clear safety, legal, privacy or refund flags; Samir or the pilot lead switch drafts off per channel and language |
| Competence | Routing by reply language (Arabic: Lina, Rami, Ahmad, Samir; Russian: Olga, Yana, Sergei; English: Daniel and trained agents; Hebrew: all). Training 7–11 February with 20 real drafts, 5 of them wrong (module 6) |
| Feedback loop | Discard reasons reviewed weekly in the prompt review (05.7); Thursday one-line note to the team on what changed because of their marks |
| Spot audit | Olga and Lina re-read 20 sent drafted replies per language per week; the gate-1 (c) sample; findings shared without names |
| Accountability | The four questions (information, time, authority, competence) before any finding about a person; a "no" is a design failure, fixed by the owner; a first review error is coaching |
| Marking, inside | Rule-of-use fields on every drafted ticket, plus prompt version and model id |
| Marking, outside | Privacy notice says staff use an approved AI tool to help draft replies, which they check and send; no per-message label; the agent's name on every reply. Question to counsel (via Ronit, by 25 January): is this enough under the Privacy Protection Law and the PPA's draft AI guidance for an AI-assisted reply sent by a person? |

**Simulation (oversight-under-load, Harbor & Pine preset; an educational model):** as planned, about 65 wrong replies reach customers in two weeks; source shown and flag feedback together bring it to about 9 within 4.5 agent-hours a day, the only design that meets the target. A fourth reviewer alone gives about 55. With a "better model" (5% wrong), feedback off and no source: about 19 escape and only 57% are caught, a lower share than the worse model with a good design.

**What changed in the plan because of this lesson:** the source-beside-the-draft panel moved from "phase 2" into the integrator's first 14 days; the load rule was added to the charter's stop rules; the training session includes planted wrong drafts.

</details>

## References

- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 4 (designed vs effective oversight, capacity screen); [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 6 (reviewer complacency, misattributed responsibility, detectability). Named, not re-taught.
- Pearl Cohen, [Israel: new draft guidelines on the application of privacy law to AI](https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/) (draft). EU AI Act [Article 50](https://artificialintelligenceact.eu/article/50/) (AI Act Explorer). Not legal advice: the marking decision goes to counsel.
- Simulation: [oversight under load](../../simulations/oversight-under-load/index.html?preset=harbor). Template: [human-review design](../../templates/human-review-design.md).
- Earlier: [05.1 · The pilot charter](lesson-01.md) (rule of use), [05.4 · Evaluate](lesson-04.md). Next: [05.6 · Shadow mode and staged release](lesson-06.md). Later: the incident runbook (lesson 07.5) and training (06.2).
