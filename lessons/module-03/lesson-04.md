---
id: "03.4"
module: 3
minutes: 18
practice_minutes: 60
prerequisites: ["03.3"]
objectives:
  - "Lock weighted scoring criteria with anchored ratings before opening the candidate list, and write them so a scorer can state them with the list closed."
  - "Net the expected cost of errors from each candidate's benefit before rating its value."
  - "Break effort into four parts (data, integration, regulation, adoption), each with an owner and a reshape move."
  - "Ask each receiving team what it can absorb and choose a portfolio of at most three that fits."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 2, Identify and Prioritize AI Opportunities (value–effort lens, portfolio)"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "IBM Lead AI Transformation: Strategy, Governance & Execution Professional Certificate (Coursera) — course 2, Build Your AI Leadership Strategy (value–feasibility–risk sort)"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-02"
---

# 03.4 · Scoring with evidence, not opinions

A scoring grid looks objective and is easy to bend: change a weight after you see where the CEO's idea lands, call a vendor's case study "evidence", forget that a wrong answer costs money, and assume the team that must absorb the change has time. In this lesson you lock the criteria before you open the list, score each candidate on its evidence, net the expected cost of its errors, break its effort into four parts and ask the receiving teams what they can take. At the end you have a portfolio of three for Harbor & Pine and a score sheet that survives the question "why did you rank it that way?".

## The situation

Tuesday 24 November 2026. Your fast screen ([03.3](lesson-03.md)) went to Michal and Ronit yesterday. On Thursday you run the scoring workshop with Yoav, Michal, Ronit and Samir ([03.5](lesson-05.md)). Before that you need two things: criteria the room will accept, and your own scored version, so you know where the evidence points before opinions start.

Two IBM certificates name this step: the value–feasibility–risk sort, with the warning that "the real value is the weight-setting conversation", and the consulting version's locked criteria, four-part effort, absorption capacity and the direction of the expensive error. Here you do all of it on nine Harbor & Pine cards.

## What to do

### Step 1 — Lock the criteria before anyone opens the list

Write three weights and the rules, date them, and get them agreed by the people who own value, money and risk: here Michal (operations), Ronit (finance) and, because the output reaches customers, Samir (who runs the work). Lock them on Tuesday, before the workshop shows the cards.

| Criterion | Weight | 1 means | 3 means | 5 means |
|---|---|---|---|---|
| Value (after netting errors) | 40% | Under ₪2,000 a month net, or no measured basis | ₪3,000–10,000 net, partly measured | Over ₪12,000 net, measured, tied to the sponsor's objective |
| Feasibility | 30% | Needs data that does not exist or a large integration; unknown builder | Known builder, one integration, within the CEO's approval band | Days of work, existing data, within the department's band |
| Risk (5 = worst) | 30% | Internal, reversible, a person checks everything | Reaches customers after a person's check | Decides about people or money without a person, or irreversible |

And the rules:

1. Net the expected cost of errors from the benefit before rating value.
2. Benefits that are only claimed, not measured, count at half value.
3. Ask every receiving team what it can absorb before committing.

Two rules you deliberately leave out, and say so: no bonus for the CEO's announced priority, and a vendor's published case study is not measured evidence. The test that the criteria are really locked: Ronit can state them on Thursday with the list closed.

### Step 2 — Score each card on its evidence

Each card is a claim with an evidence level: measured (counted in your data), mixed, or claim only. Rate each dimension 1–5 against the anchors and write one line of reason. Then check the card's own numbers against your data: a card is a proposer's case, and proposers round up. Two of the nine Harbor & Pine cards state volumes the data room does not support (Step 6).

### Step 3 — Net the expected cost of errors

Every candidate is wrong sometimes. Expected monthly error cost = items a month × error rate × cost per error. Subtract it before you rate value. Which error is expensive depends on the business: a wrong delay date costs a re-contact; a wrongly rejected damage claim costs a consumer complaint and a customer; an unfair applicant ranking can cost a discrimination claim.

| Card | Claimed benefit ₪/month | Error cost ₪/month | Net ₪/month | Evidence |
|---|---|---|---|---|
| Promised-date fix + delay emails | 16,000 | 210 × 2% × 60 = 252 | 15,748 | measured |
| Support reply drafts | 10,000 | 1,920 × 1.5% × 120 = 3,456 | 6,544 | mixed |
| B2B quote drafts | 8,750 | 140 × 4% × 900 = 5,040 | 3,710 | measured |
| Assembly answers | 8,200 | 430 × 5% × 300 = 6,450 | 1,750 | mixed |
| Marketing copy | 2,600 | 300 × 2% × 250 = 1,500 | 1,100 | claim |
| ChatNest chatbot | 113,000 | 4,200 × 10% × 150 = 63,000 | 50,000 | claim (vendor) |
| "AI" smart reorder | 25,000 | 1,800 × 3% × 160 = 8,640 | 16,360 | claim (vendor) |
| Damage-claim decisions | 3,250 | 260 × 12% × 1,200 = 37,440 | −34,190 | mixed |
| PeopleWise candidate match | 2,000 | 120 × 1% × 20,000 = 24,000 | −22,000 | claim (vendor) |

Two cards go negative once errors are counted. The chatbot still shows ₪50,000 a month, but it is a vendor claim (half value under rule 2) built on a 70% that was measured elsewhere, and the 10% error rate is the vendor's too.

### Step 4 — Break effort into four parts

"Effort: medium" hides where the work is. Split it, give each part an owner, and look for a reshape move that makes the hard part easier:

| Part | What it asks | Reply drafts at Harbor & Pine | Reshape move |
|---|---|---|---|
| Data condition | Are the inputs clean, labelled, current? | Medium: language field wrong or blank for about 8% of tickets; WhatsApp not in the helpdesk | Detect language in the pipeline; route WhatsApp first |
| Integration surface | How many systems, read or write? | Medium: helpdesk (draft only), Priority and ETA data (read) | Nightly ETA export instead of a live link in phase 1 |
| Regulatory and compliance burden | Which approvals and reviews? | Medium: customer personal data in a third-party model; DPO view; approved tool | Data boundary and an approved tool from module 4 |
| Adoption resistance | Will the people change how they work? | Low–medium: agents drafted with free ChatGPT until the interim rule and want an approved tool; fear of headcount cuts | Olga as champion; no headcount talk (Samir's condition) |

The parts often show that the "hard" candidate is hard in only one place, and that the fix is outside AI (moving WhatsApp, a data boundary), which makes it a condition rather than a reason to drop it.

### Step 5 — Ask the receiving team what it can absorb

Every change costs the receiving team hours: training, checking, new steps. Ask the team lead for a number, in hours a month, and add up what your portfolio asks of each team. At Harbor & Pine (the leads' answers in the simulation):

| Team | Can absorb a month | Asked of it by |
|---|---|---|
| Support (Samir) | 30 hours until February, about double after | Reply drafts 25, assembly answers 20, chatbot 60 |
| Logistics (Tamar) | 12 hours | Date fix 4 |
| B2B sales (Yaniv Carmi's team) | 20 hours | Quote drafts 10 |
| Claims desk (Rina) | 4 hours | Damage-claim decisions 12 |

Support cannot take the drafts and the assembly answers together before February (45 > 30), and it cannot take the chatbot at all this winter. That is a sequencing fact, not a scoring one: it decides which support candidate goes first and when.

### Step 6 — Read the ranking, then choose at most three

With weights 40/30/30 and the three rules, the scores are (value is halved for claim-only cards):

| Card | Value | Feas. | Risk | Score |
|---|---|---|---|---|
| Promised-date fix | 5 | 5 | 1 | 100 |
| Reply drafts | 4 | 4 | 2 | 80 |
| B2B quote drafts | 3 | 4 | 3 | 66 |
| Marketing copy | 2 (→1) | 5 | 2 | 62 |
| Assembly answers | 3 | 2 | 3 | 54 |
| Smart reorder | 1 (→0.5) | 3 | 3 | 40 |
| PeopleWise match | 1 (→0.5) | 5 | 5 | 40 |
| Chatbot | 2 (→1) | 2 | 4 | 32 |
| Damage-claim decisions | 1 | 1 | 5 | 20 |

Read it backward before you accept it. Marketing copy scores close to the quotes, but the screen already said it is a tool-approval decision, not a project; it does not take a portfolio slot. Assembly answers would overload support before February. The chatbot is last, and the reason is written in its evidence column, not in anyone's opinion.

The portfolio: **(1) the promised-date fix with proactive delay emails (plain automation, no AI); (2) reply drafts for all written contact once WhatsApp is routed into the helpdesk, from February, a person sending every reply; (3) B2B quote drafts with prices read from Priority.** It is a deliberate mix: a quick, cheap, measured win; one larger AI bet; one smaller AI bet in a different team.

And check the cards against the data before you present them. The damage-claims card says "about 260 claims a month"; the claims log has 149 in six months, about 25 a month. The assembly card says assembly questions are "about 9% of tickets" and 540 a month; the tickets show about 6% (about 25 a month in the helpdesk, more on WhatsApp). Neither changes the portfolio, but quoting either number in the workshop would cost you credibility the first time Ronit checks it.

[Simulation: Portfolio sorter](../../simulations/portfolio-sorter/index.html?preset=harbor)

## Watch out

- **Setting weights after seeing the list.** If the weights change once the CEO's idea lands fourth, the grid is decoration. Lock them, date them, and if someone wants a change, record it as a change with its effect on every card.
- **Everything in the top right.** When every card scores 3–4, the anchors are missing. Use the full range, and demand evidence for every 5.
- **A vendor case study as evidence.** It is a claim about another customer. Count it as a claim.
- **Value without errors.** A candidate that is right 88% of the time on decisions that cost ₪1,200 when wrong is not a saving.
- **Not asking the receiving team.** A portfolio the team cannot absorb fails in the rollout, not in the business case, and it fails on the team.
- **Averaging the scorers.** In the workshop, discuss where scorers diverge; that is where the missing evidence is (03.5).

## Your turn

### Inputs

- Your screen from [03.3](lesson-03.md) and frames from [03.2](lesson-02.md).
- Simulation: [portfolio sorter, Harbor & Pine preset](../../simulations/portfolio-sorter/index.html?preset=harbor). No simulation: use the nine cards in Steps 3 and 5 of this lesson and the spreadsheet `labs/module-03/use-case-scorecard.csv` (module download).
- Data room: `claims/damage-claims-log.csv`, `support/tickets.csv`, `support/whatsapp-week-tally.csv` to check card volumes.
- Template: [use-case scorecard](../../templates/use-case-scorecard.md), part B.

### Steps

1. Write your criteria: three weights, anchors for 1, 3 and 5, the rules you lock and the two you refuse. Date them.
2. In the simulation, lock them, then open and score all nine cards. Net each card's error cost before you rate value.
3. Fill the four-part effort for your top three, each part with an owner and a reshape move.
4. Ask every team in your portfolio what it can absorb; adjust the portfolio or its timing if a team is over.
5. Commit, read the debrief and the hidden truths. Write down every card where your rating differed from the expert's by 2 or more, and why.
6. Check two card volumes against the data room and note what you find.

### Time

60 minutes: 10 to lock criteria, 30 to score, 10 for effort and absorption, 10 for the debrief notes.

### Done when

- [ ] The criteria are written, dated and locked before any card is scored, with anchors for 1, 3 and 5.
- [ ] Every card has three ratings with a one-line reason; claimed benefits are marked as such.
- [ ] Every portfolio card has its error cost netted and its effort split into four parts with owners.
- [ ] You asked every receiving team in your portfolio, and no team is over its number at the time its candidate starts.
- [ ] Your portfolio has at most three cards, and you can say in one sentence why each other card is out.
- [ ] You found at least one card whose volume the data room does not support.

<details><summary>Reference answer</summary>

**Criteria, locked 24 Nov 2026 (Michal, Ronit, Samir):** value 40%, feasibility 30%, risk 30%; anchors as in Step 1; rules: net errors, claims at half value, ask capacity. Refused: CEO bonus, vendor case study as measured.

**Scores and portfolio:** as in Step 6. Portfolio: date fix (100), reply drafts (80), B2B quote drafts (66).

**Why each other card is out (one sentence each):**

- Marketing copy (62): a tool and data-boundary decision for module 4, not a funded project; Noa already pays for one.
- Assembly answers (54): a good second wave for support, after the drafts pilot builds the review routine and the manuals are cleaned; support cannot absorb it before February.
- Smart reorder (40): min/max rules sold as AI, and the case study was a grocery distributor with weekly deliveries, not 60-day sea containers.
- PeopleWise match (40): already switched on by an update; it belongs in the AI inventory and risk review, switched off until reviewed.
- Chatbot (32): the 70% was measured on US English retail with order tracking; here it would quote the wrong promised date from a stale catalogue; reconsider after the date fix, on Harbor & Pine's own data.
- Damage-claim decisions (20): no recorded outcomes for about a third of claims, and every error lands on a customer.

**Four-part effort for the portfolio:**

| | Data | Integration | Regulatory | Adoption |
|---|---|---|---|---|
| Date fix | Medium: hand-kept sheet, fix the format (Tamar) | Low: Priority read, one field write, email (Avi) | Low: notice texts to customers (Samir approves) | Low, but Noa must agree to change the lead times (you, with Yoav) |
| Reply drafts | Medium (Samir) | Medium (integrator) | Medium: DPO view, approved tool (module 4) | Low–medium (Olga as champion) |
| Quote drafts | Medium: price agreements in personal sheets (Yaniv) | Medium: Priority read (integrator) | Low | Low (Yaniv) |

**Absorption:** support 25 of 30 hours (drafts only, from February, when capacity doubles); logistics 4 of 12; sales 10 of 20. All fit.

**Hidden truths worth writing down from the debrief:** the date fix needed no AI and roughly halved WISMO contacts within six weeks; the drafts pilot worked once the source (the customer's message and the order) was shown beside each draft; reading prices from Priority cut wrong prices in quotes to under 1% and doubled the quote card's net benefit.

**Card volumes that the data does not support:** damage claims ("260 a month" vs about 25 in the log); assembly ("9% of tickets, 540 a month" vs about 6%).

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 2, modules on the value–effort lens and the prioritized portfolio (locked criteria, effort decomposition, absorption capacity, direction of the expensive error; named, not re-taught).
- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 2 "Build Your AI Leadership Strategy" (value–feasibility–risk sort, clustering trap).
- Simulation: [portfolio sorter](../../simulations/portfolio-sorter/index.html?preset=harbor).
- Template: [use-case scorecard](../../templates/use-case-scorecard.md).
- Next: [03.5 · Running the scoring workshop](lesson-05.md).
