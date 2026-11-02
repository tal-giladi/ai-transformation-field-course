---
id: "11.3"
module: 11
minutes: 18
practice_minutes: 150
prerequisites: ["11.2", "03.1", "03.3", "03.7", "03.9"]
objectives:
  - "Build a baseline sheet for a public service in which every number has a definition, a source, a label and an owner who will report it after you."
  - "Map and screen Givat Oren's candidates, including the mayor's chatbot, and name the ones that are plain content and letter work, not AI."
  - "Net the case the way a treasurer and a comptroller will: capacity is not cash, and the value of correct answers is not hours."
  - "Write a one-page case for the management forum that asks for decisions the forum can actually take, including what to do with a budget line it did not ask for."
volatility: implementation
sources:
  - title: "Claude pricing: Sonnet 5.5 US$2 / US$10 per million input / output tokens (checked 2 November 2026)"
    url: https://claude.com/pricing
  - title: "Bank of Israel, representative exchange rate API (US$ = ₪3.136, 2 November 2026)"
    url: https://boi.org.il/PublicApi/GetExchangeRate?key=USD
  - title: "Municipalities (Tenders) Regulations, 5748-1987, regulation 3(3) (small purchases), Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/תקנות_העיריות_(מכרזים)
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): fast screen, net the claim, decision-ready case"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-02"
---

# 11.3 · Diagnosis

The findings say residents are missing one correct answer and a usable reason; the mayor's office still expects a chatbot, and a ₪600,000 line with that name goes to the council on 22 December. Before then you have fifteen minutes at the management forum. In this lesson you build the baseline sheet, map and screen the candidates (the mayor's included), put an honest value on each, and write a one-page case that asks the forum for decisions it can take this week. At the end you have a shortlist with measured baselines and a case for 17 December.

## The situation

Sunday 13 to Thursday 17 December 2026. Your findings memo went to Ronit Shemesh on 10 December. She replied with two lines: "Agreed on Ruti, done on Monday. Bring me something the forum can decide on the 17th, and something Eyal can live with." Three division heads answered her owners email; one did not. The council's finance committee meets on 20 December to prepare the budget vote.

This is module 3 compressed: the [opportunity map](../module-03/lesson-01.md), the [fast screen](../module-03/lesson-03.md), the [ROI model that survives finance](../module-03/lesson-07.md) and the [decision-ready case](../module-03/lesson-09.md). IBM would call step 4 *netting the claim*; in a municipality the ledgers are different (no revenue, budget lines instead of profit, a comptroller instead of a board), and the value that matters most is not on any of them.

## What to do

### Step 1 — The baseline sheet: one row per number, with an owner after you

At Northwind ([08.3](../module-08/lesson-03.md)) the baseline sheet was evidence for a decision. Here it is also the start of a public reporting habit: every number needs an **owner who will report it after you**, or it will vanish when you go back to the website.

| Measure | Definition | Value | Label | Owner from February |
|---|---|---|---|---|
| Permits-family contacts | Topic in the permits family; 4% caller sample × 25 | ≈ 6,600 a month (33.8% of ≈ 19,570) | Measured | Head of 106 |
| Repeat contacts, permits family | Same caller, same topic, within 14 days | 35.0% (other topics 12.2%) | Measured | Head of 106, monthly |
| Callbacks made by the promised date | `completed_at` ≤ `promised_by_date` | 47.3%; permits family 42.4% | Measured | Division heads, reported by 106 |
| Answered in the chosen language | Handled contacts | ar 39.7%, ru 75.9%, am 26.7%, en 89.6% | Measured | Head of Resident Service |
| Right answer on the phone | Quality unit's mystery-shopper coding | 54.2% (n = 120); 42.3% where the rule changed | Measured, small n | Quality unit, quarterly |
| Permits pages out of date | Page vs council decision 2025/118 | 9 of 24 | Measured | Each division's content owner |
| Refusals with a usable reason | Letter names the condition, the document, the objection route | 0 of 417 | Measured | Head of Licensing and Permits |
| Cost of an agent hour | Budget line 1612-410 ÷ 26 staff ÷ ≈ 1,884 working hours | ≈ ₪130 | Directional | Treasurer |
| Cost of a contact | ≈ 3.7 minutes of handling at ₪130 an hour | ≈ ₪8 | Directional | Treasurer |

Notice what is not here: any number from the vendor. "94% accuracy" and "70% resolved without a human" are claims to test in 11.4, not baselines.

### Step 2 — Map the candidates, including the one you were handed

Use the [opportunity map](../../templates/opportunity-map.md) with its three feeds ([03.1](../module-03/lesson-01.md)): requests from the work, AI already in use, and top-down goals. In Givat Oren:

| Candidate | Feed | Type |
|---|---|---|
| A. Public chatbot on today's website (the mayor's office; CivicTalk's proposal) | Top-down | Generate, alone, residents |
| B. One owned, dated knowledge pack for permits and fees, published in four languages | Findings 1, 2, 7, 8 | **Not AI** |
| C. Decision letters that name the condition, the document and the objection route, in the applicant's language | Findings 6, 7; the resident | **Not AI** |
| D. Callbacks measured on completion; repeat contacts reported monthly | Findings 3, 4 | **Not AI** |
| E. An assistant for 106 agents: answers only from B, cites its source, refuses individual cases, four languages | Request (head of 106: "for my agents first") | Generate, a person checks |
| F. An approved translation tool for the permits desk | AI already in use (a clerk's phone) | Generate, a person checks |
| G. Ruti | AI already in use | Generate, alone |

Three of the strongest candidates are not AI. Say so on the map: the forum needs to see that you looked for the cheapest fix first.

### Step 3 — Screen each one, with the data gate first

Use the [use-case scorecard](../../templates/use-case-scorecard.md) and the seven questions of [03.3](../module-03/lesson-03.md). The data gate decides most of it:

- **A fails the data gate.** It would answer from a website where 9 of 24 permits pages are wrong, mostly in the languages the city most needs to serve; in Arabic it would answer from 2023 pages or from machine translation of Hebrew. There is no content owner, no procurement route and no test. **Stop for now**, with the condition that would change it (B done, E passed, a procurement route).
- **B, C, D pass.** They need owners and a few weeks, not money. **Go.**
- **E: go with a condition.** It depends on B (it can only be as right as the pack), on a test on the city's own questions, and on consulting the works committee before agents' work changes.
- **F: go with a condition** after C and the CISO's approval of a tool.
- **G: stop now** (done on 14 December).

### Step 4 — Net the claim the way the treasurer and the comptroller will

The mayor's office has no number, only a promise: "24/7, every language". Net it anyway, because the forum will ask what the ₪600,000 buys.

**A, the public chatbot.** It does not remove contacts if residents call to check what it said (the MyCity lesson in 11.4). Its errors land where the city is already weakest: a resident who asks in Arabic gets the 2023 Arabic page. Its price after the "free" period is ₪14,500 + VAT a month for 36 months, ₪522,000, before any content work.

**E, the agent assistant, in hours.** With `fieldkit.cost.pilot_value` (or the simulation below): 6,600 permits-family contacts a month, the assistant used on 70%, right 90% of the time, 1.5 minutes saved on a right answer (no searching), 0.3 minutes to read it, 3 minutes to fix a wrong one, ₪130 an hour, model cost ≈ ₪0.022 a question (about 2,600 tokens in and 180 out at Claude Sonnet 5.5's list price of US$2 / US$10 per million, checked 2 November 2026, at ₪3.136 per US$), ₪6,000 a month of fixed cost (the owner's time and re-tests). Result: **about 58 net hours a month, ≈ ₪1,400 of capacity after fixed cost**; at 0.6 review minutes or 80% accuracy it loses money.

[Simulation: Pilot economics](../../simulations/pilot-economics/index.html?preset=generic)

(The `generic` scenario is a different organization: type Givat Oren's inputs in.)

**B + C + D, in contacts.** If they bring permits-family repeats from 35% to 20% (**assumed**; nobody has measured the effect of a correct page), about 990 fewer contacts a month, ≈ 61 agent hours, ≈ ₪8,000 of capacity. Capacity, not cash: no agent's job changes, and you have promised the works committee as much.

So the honest statement is: **the case is not hours.** It is that the city stops telling residents rules the council changed, serves Arabic speakers as well as Hebrew speakers, gives reasons people can act on, and can show the comptroller a measure that means what it says. Write that, plainly, as the first line of value.

**The budget line.** You cannot spend it and should not ask for it. You can recommend what it should be called before the council votes: "resident information and language service", with its use decided at the 2 February forum. Two Arabic-speaking agents for 106 cost about ₪492,000 a year loaded; that is a use the data supports and a chatbot licence is not.

**Track B (Python).** `python case_model.py` in `labs/module-11/` (module download) prints both calculations above with `fieldkit.cost`; change one input at a time (`--review 0.6`, `--use 0.5`, `--repeat-after 0.25`) and keep the printout as the case's appendix. Python is worth it here because the treasurer will ask "what if agents only use it half the time?" in the meeting.

### Step 5 — Write the one-page case

Use the [decision-ready case](../../templates/decision-ready-case.md) from [03.9](../module-03/lesson-09.md). Ask only for decisions the forum can take:

1. The director-general names content owners in four divisions with a publication date.
2. The forum approves B, C and D.
3. The forum approves an internal test of E on the city's own questions, reported on 2 February.
4. The forum asks the finance committee to re-label line 1611-780 before the vote.

Then what each costs, what it is worth (labelled), what "no" means, and **a draft sentence for the mayor** that is true on 4 February. The last item is what makes the case survivable for the chief of staff.

## Watch out

- **Netting only the vendor.** Your own candidates need netting too: B's value is assumed until the repeat rate moves.
- **Turning capacity into savings.** Sixty hours a month are not a budget line, and every agent already reads "efficiency" as "fewer of us".
- **Asking the forum to decide what it cannot.** The forum cannot sign a contract or vote a budget. It can name owners, approve internal work and ask the finance committee.
- **Leaving the mayor's office empty-handed.** A case that only says "stop" makes the chief of staff go to the vendor directly. Give him a sentence.
- **Burying the not-AI candidates.** If content, letters and callbacks are the biggest lever, they lead the page, even in a project called "AI".

## Your turn

### Inputs

- Your findings memo (11.2) and the numbers behind it; `labs/module-11/discovery.py` (Track B).
- Data room (module download): `city/budget-2027-draft-extract.md`, `service/moked-kpi-report-2026-q3.md`, `procurement/civictalk-proposal.md`.
- Persona: [Ronit Shemesh](../../labs/module-11/personas/ronit-director-general.md) (to test the case) or [her transcript](../../labs/module-11/personas/transcripts/ronit-director-general.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [ROI model](../../templates/roi-model.md), [decision-ready case](../../templates/decision-ready-case.md).

### Steps

1. Build the baseline sheet (at least eight rows) with a definition, label and future owner for each.
2. Map at least six candidates from the three feeds; mark which are not AI.
3. Screen each with the data gate; give go / go with a condition / stop, with the condition.
4. Net A and E (hours, cost, what they do to residents' answers); state B–D's value with its label.
5. Write the one-page case with four decisions, costs, value, what "no" means and the mayor's sentence.
6. Test it on Ronit (roleplay ten minutes) and change what she would not sign.

### Time

150 minutes: 30 for the sheet, 30 for the map and screen, 40 for the netting, 35 for the case, 15 for the test.

### Done when

- [ ] Every baseline has a definition, a label and an owner who will report it after February.
- [ ] At least two non-AI candidates are on the shortlist, and the public chatbot has a stop with the condition that would reverse it.
- [ ] No hours appear as cash; the case's first value line is about correct answers, not time.
- [ ] The case asks only for decisions the forum can take, and has a true sentence for the mayor.

<details><summary>Reference answer</summary>

The full case is `labs/module-11/expert/03-baselines-and-case.md` in the module download.

**Shortlist:** B knowledge pack (go), C letters (go), D callback and repeat measures (go), E agent assistant (go with condition: B first, tested on our questions, works committee consulted), F approved translation tool (go with condition, after C), A public chatbot (stop for now: data gate fails; reverses when B is published, E passes, and a procurement route exists), G Ruti (stopped 14 December).

**Decision asked on 17 December:** owners named in four divisions with publication on 1 March; B, C, D approved; an internal test of E reported on 2 February; line 1611-780 re-labelled "resident information and language service", ₪600,000, use decided on 2 February.

**Value, labelled:** correct answers in four languages and usable reasons (the case); B–D ≈ 990 fewer contacts a month, ≈ 61 agent hours (assumed reduction from 35% to 20%); E ≈ 58 net hours, ≈ ₪1,400 a month after fixed cost, negative at 0.6 review minutes (directional). Capacity, not cash.

**Cost:** B ≈ 120 editor hours plus 4 × 20 owner hours and a translation order within line 1611-751; C a Rishuyit template change (≈ 10 IT days) and one reviewed translation of eight letters; D none; E's test ≈ ₪150 a month of model usage by price quotes, plus your time.

**What "no" means:** the site keeps the 2025 rules in three languages; the desk keeps refusing leased cars under an abolished rule; any chatbot launched in February repeats both.

**The mayor's sentence (draft for Eyal):** "From 1 March: every answer from the city in your language, every refusal with its reason, every callback measured. And we are testing an assistant for our 106 team, in four languages, live when it passes."

</details>

## References

- Anthropic, [Claude pricing](https://claude.com/pricing) (list prices, checked 2 November 2026); Bank of Israel, [representative rate](https://boi.org.il/PublicApi/GetExchangeRate?key=USD) (₪3.136, 2 November 2026). Check your own provider and date the price.
- [Municipalities (Tenders) Regulations, 5748-1987](https://he.wikisource.org/wiki/תקנות_העיריות_(מכרזים)): why a small internal test can be bought by price quotes (regulation 3(3); confirm the current indexed amount with the treasurer).
- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): fast screen, net the claim, decision-ready case (named, not re-taught).
- Field kit: [03.1 · Opportunity map](../module-03/lesson-01.md), [03.3 · The fast screen](../module-03/lesson-03.md), [03.7 · The ROI model that survives finance](../module-03/lesson-07.md), [03.9 · The decision-ready case](../module-03/lesson-09.md).
- Templates: [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [ROI model](../../templates/roi-model.md), [decision-ready case](../../templates/decision-ready-case.md).
- Simulation: [Pilot economics](../../simulations/pilot-economics/index.html?preset=generic) (generic scenario; enter Givat Oren's inputs).
- Earlier: [11.2 · Discovery](lesson-02.md). Next: [11.4 · The hard part](lesson-04.md).
