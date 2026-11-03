---
id: "17.4"
module: 17
minutes: 20
practice_minutes: 120
prerequisites: ["17.3", "07.7", "04.5", "06.5", "07.2"]
objectives:
  - "Write stop/keep audit rules before opening the list of systems, so every decision follows evidence rather than the sponsor's attachment or the board's alarm."
  - "Pressure-test an inherited programme's promises and next steps, sorting wrong assumptions from fragile dependencies, each with a disposition and an owner."
  - "Test the controls the programme relied on and record which ones existed only on paper."
  - "Plan how trust is rebuilt with each audience — board, operations, works committee, customer, vendor — by one kept promise first, and agree the plan with both principals."
volatility: implementation
sources:
  - title: "Histadrut, 'AIG Israel workers' committee declare labour dispute over AI' (August 2026)"
    url: https://global.histadrut.org.il/news/aig-israel-workers-committee-declare-labour-dispute-over-ai/
  - title: "EU AI Act, Annex III, point 4 (employment and workers' management: monitoring and evaluating performance and behaviour) — AI Act Explorer"
    url: https://artificialintelligenceact.eu/annex/3/
  - title: "AI Act Explorer, 'Digital Omnibus on AI', Regulation (EU) 2026/1744: Annex III high-risk obligations from 2 December 2027"
    url: https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/
  - title: "law.co.il, 'Monitoring employees' email severely restricted' (Isakov Inbar, National Labour Court, 8 February 2011)"
    url: https://www.law.co.il/en/articles/2011/04/25/monitoring-employees-email-severely-restricted/
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): pressure-testing the roadmap; wrong vs fragile"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-03"
---

# 17.4 · The hard part: a turnaround

A turnaround is not a new strategy; it is putting things in the right order while the old programme is still running, a customer is still angry and the board still doesn't believe you. In this lesson you fix the audit rules before you look at the list, pressure-test what the inherited programme promised and planned next, test the controls it relied on, plan how each audience gets one kept promise before you ask it for anything, and agree the plan with both principals. At the end you have dated audit rules, a pressure-test log, a control test, a trust-repair plan and the record of what the two principals agreed.

## The situation

Thursday 24 June 2027, 10:00, the CEO's meeting room, one hour with Ofer and Ilana together for the first time since the protocol. Since the case on Sunday ([17.3](lesson-03.md)): the incident is reopened and contained; the vendor has sent part of its logs and an offer; the works committee's letter has still not been answered in writing; the region notice must go by Thursday 1 July. Ofer wants to keep the platform and "show what the North can become". Two directors have asked Ilana whether the company should "switch it all off".

IBM's governance course gives you the unearned green and the control-credibility test; its roadmap course gives you pressure-testing and the difference between a wrong assumption and a fragile one. In a turnaround they all apply at once, to someone else's programme, with the person who signed it in the room.

## What to do

### Step 1 — Put the three jobs in order

Write the plan's spine in three lines, and hold to the order:

1. **Stop the harm.** The incident; the review that exists only on paper; monitoring of drivers that nobody agreed.
2. **Stop paying for what nobody uses.** Seats, pilots and licences with no users.
3. **Keep and prove what works.** With an owner and one measure each.

Order matters because each audience is watching for a different signal. The board needs to see harm handled before anything is kept; the operations teams need to see unused tools stopped before anything new arrives; the CEO needs to see something kept before he can accept the rest.

### Step 2 — Fix the audit rules before you open the list

The CEO wants the platform kept; two directors want everything stopped. If you look at the systems first, every decision will be read as taking a side. Write the rules first, date them, and send them to both principals before the inventory is complete (the expert did it on Sunday 13 June):

| Rule | Applies when | Action |
|---|---|---|
| R1 Harm open | An open incident, or harm to customers or people not yet bounded | Suspend the part that causes it until written conditions are met |
| R2 No basis | People monitored without the consultation the collective agreement requires, or data sent where no agreement covers it | Stop, or bring in if the work is needed |
| R3 Not used | Active below 10% of billed for 60 days | Stop, or reduce to active users plus 10% |
| R4 Value measured | A comparison exists and the risk is controlled | Keep, with a named owner |
| R5 Value plausible | Unmeasured, risk controlled | Keep under test: 90 days, a measure agreed now |
| R6 Outside the register | Found in licences, cards, proxy, tickets | Register, then apply R1–R5 |

Two properties make the rules defensible. They apply **per system and per region**, never to "the programme" — which is what lets you keep the North's route tool and stop the South's in the same paper. And each action names **the contract step it needs**, so a "stop" that the contract does not allow until August is written as such, not promised for July.

### Step 3 — Pressure-test what the inherited programme promised and planned

Use [07.7](../module-07/lesson-07.md) and the [pressure-test log](../../templates/pressure-test-log.md). Read the March deck (`company/board-deck-ai-programme-2027-03-25.md`) as if it has already failed — including slide 5, "Next", which nobody has cancelled. For each promise: what breaks, for whom, when; wrong (false today) or fragile (true today, may change); a disposition; an owner. A worked excerpt:

| Promise | What breaks | Type | Disposition | Owner |
|---|---|---|---|---|
| "4 regions live" | The board decides on a scope that doesn't exist; ₪0.89M a year for unused seats | Wrong | Correct in the brief; reduce under MSA 7.4 by 1 July | CEO |
| "Every declaration reviewed" | Customers and Customs carry errors nobody sees | Wrong | Measure review time; KPI back to 9–10; 5% QA | Head of customs brokerage |
| Route learns from Vantage's data | Plans keep using 2021–23 roads | Fragile (feed broken) | Fix the feed; retrain; trigger: overrides above 20% in a depot | IT, North |
| Vendor releases are safe | A release changed matching without notice | Fragile | Releases to a test tenant first; enforce MSA 4.3 notice | IT |
| Next: auto-submit low-risk declarations in Q3 | Removes the only control while the error rate is 7% | Wrong | Remove until two QA quarters under 2% | Head of customs brokerage |
| Next: driver score and cameras in Europe in Q3 | GDPR, the EU AI Act's high-risk list and the same grievance in Rotterdam | Wrong | Remove | COO |

The last line needs a source. The EU AI Act lists as high-risk, in Annex III point 4(b), AI systems intended "to monitor and evaluate the performance and behaviour of persons" in work relationships; Vantage Europe's drivers are in the EU. The Digital Omnibus (Regulation (EU) 2026/1744) moved the obligations for Annex III systems to 2 December 2027. Whether the driver score falls under 4(b), and what Vantage Europe must do as a deployer, is for EU counsel; that it should not be rolled out in the meantime is your recommendation.

### Step 4 — Test the controls the programme relied on

Use [04.5](../module-04/lesson-05.md) and the [risk register](../../templates/risk-register.md). Every green in the inherited programme is unearned until tested. List the controls the register and deck relied on, and what you found:

| Control as described | Test | Result |
|---|---|---|
| "Licensed agent reviews every declaration" | Seconds on the approval screen; re-checked sample | Paper only: 19 s median, 7.0% material errors |
| "Dispatcher approves every plan" | Override log, late stops | Real in the North (29% overridden); the South's dispatchers approved by stopping the tool |
| Vendor change notice (MSA 4.3) | Release history vs notice received | Not applied: notice the same morning |
| Retraining from telematics | Feed tickets | Not running since 14 November |
| Incident process | Record vs logs; legal branch | No privacy branch; closed on the vendor's word |
| "Hand-over to an agent on request" (Assist) | Sessions handed to a person | Real: 49% handed over |

[Simulation: Risk register tester](../../simulations/risk-register-tester/index.html?preset=harbor)

The simulation is Harbor & Pine's preset: practise earning the green with a limited testing budget, then use the same discipline on the six controls above.

### Step 5 — Plan trust repair by audience: one kept promise first

Trust does not come back from a message. It comes back when an audience sees one promise kept before it is asked for anything. For each:

| Audience | What broke | First promise kept, by when |
|---|---|---|
| Board | Told seven systems, four regions, ₪6.2M, no incidents | Incident status note on 10 June (kept); every number labelled in the pre-read |
| Customer (Gefen) | Documents seen by others; declarations wrong; a month without an answer | Written account with named owners by Thursday 24 June; pre-fill off for its files from 21 June |
| Customs brokerage | A KPI that made the review impossible | KPI back to 9–10 from 27 June; invoice beside the pre-fill |
| Drivers and the works committee | Cameras and a score without consultation; a hearing | Written answer to the March letter; the score off everywhere; both by 1 July |
| Operations, South and Centre | Called "failed to adopt"; asked to report a scope that wasn't there | Their seats off the invoice; the South's manager and two dispatchers on the routing review |
| Vendor | Its numbers used as Vantage's | Written requests under the agreement's clauses; then a remediation plan |

The works committee deserves care. Clause 14 of the collective agreement (`people/collective-agreement-extract.md`) requires written notice and consultation before technology that monitors drivers, and bars disciplinary use of its data without agreement; the committee has voted to declare a dispute if cameras or scores return. Works committees in Israel do act on AI: in August 2026 the workers' committee at AIG Israel declared a labour dispute demanding that AI deployment be regulated through the collective agreement. Israeli labour case law has long set the frame for monitoring — in *Isakov Inbar* (National Labour Court, 2011) the court required a clear policy, transparency and proportionality before an employer may monitor employees' e-mail. What the clause and the case law require of Vantage is for HR and counsel; your plan commits to **consult before any change, not after**, and asks the committee what drivers would keep. Interview [Tesfaye Worku](../../labs/module-17/personas/tesfaye-works-committee.md) and [Rania Haj-Yahia](../../labs/module-17/personas/rania-south-ops.md) with that commitment on the table.

### Step 6 — Agree it with both principals in one hour

Design the meeting ([07.4](../module-07/lesson-04.md)) around the decisions only they can take: the incident reopened and its closure criteria; the audit rules and their first draft; who signs the region notice and by when; how the 14 April note travels (to the chair as a fact, after the CEO has read it, per protocol line 2); who owns the register until a permanent head of AI starts. Give each principal one thing that is theirs: the CEO keeps the North and a September re-measurement; the chair gets numbers the committee can test.

Rehearse the hardest moment with [Ofer Lavi](../../labs/module-17/personas/ofer-ceo.md): telling him the 14 April note goes to the chair. Lead with the protocol he signed, not with the note. Run the transcript through the [coach prompt](../../labs/common/coach-prompt.md).

## Watch out

- **Judging the programme as a whole.** "Keep Tzir" and "switch it all off" are both wrong answers to a question nobody should ask. Apply the rules per system and per region.
- **Opening the list before the rules.** Rules written after you have seen the systems look like reasons for decisions you had already made.
- **A "stop" the contract doesn't allow.** Write the contract step and the date it takes effect; don't promise the board July savings that start in October.
- **Announcing trust.** A message to the works committee before the score is switched off confirms their letter. Do the thing, then write.
- **Leaving the inherited "next" slide alive.** Auto-submit and cameras in Europe are still somebody's plan until you remove them in writing.
- **Answering the labour or EU questions yourself.** Cite clause 14, the case law and Annex III so HR and counsel know what to check; the reading is theirs.
- **Letting one principal hear the plan first.** The meeting with both is where the plan becomes theirs.

## Your turn

### Inputs

- Your findings memo (17.2) and case (17.3).
- The [data room](../../labs/module-17/data-room/INDEX.md) (module download): `company/board-deck-ai-programme-2027-03-25.md`, `vendor/tzir-msa-extract.md`, `people/works-committee-letter-2027-03-03.md`, `people/collective-agreement-extract.md`, `ai/tzir-route-model-card.md`, `incident/it-tickets-ai.csv`.
- Personas: [Tesfaye Worku](../../labs/module-17/personas/tesfaye-works-committee.md), [Rania Haj-Yahia](../../labs/module-17/personas/rania-south-ops.md), [Ofer Lavi](../../labs/module-17/personas/ofer-ceo.md) (or their transcripts); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [pressure-test log](../../templates/pressure-test-log.md), [risk register](../../templates/risk-register.md), [comms plan](../../templates/comms-plan.md), [decision record](../../templates/decision-record.md).

### Steps

1. Write the three-line spine (harm, paying, keep and prove).
2. Write and date the audit rules; say which ones apply per region.
3. Pressure-test the March deck, including its "Next" slide: at least six lines with type, disposition and owner.
4. Test at least five controls the programme relied on; mark each real or paper only, with the evidence.
5. Write the trust-repair plan: for each of six audiences, what broke and the first promise kept, with a date.
6. Interview Tesfaye (committing to consult before any change) and Rania; note what each would accept.
7. Write the agenda for the hour with both principals: the decisions, who takes each, what each principal gets. Rehearse telling Ofer that the 14 April note goes to the chair.

### Time

120 minutes: 10 for the spine, 15 for the rules, 25 for the pressure test, 15 for the control test, 20 for the trust plan, 25 for the two interviews, 10 for the agenda and rehearsal.

### Done when

- [ ] The audit rules are dated before the inventory was complete and apply per system and region.
- [ ] The pressure-test log covers the deck's promises and its "Next" slide, each wrong or fragile, with a disposition and owner.
- [ ] At least five controls are tested and the paper-only ones named with evidence.
- [ ] Every audience in the trust plan has a first promise that is kept before it is asked for anything, with a date.
- [ ] The works committee was promised consultation before change, and its conditions are recorded.
- [ ] The agenda for both principals lists decisions and owners, and how the 14 April note travels.

<details><summary>Reference answer</summary>

The full version is `labs/module-17/expert/04-turnaround-plan-and-pressure-test.md` (module download).

**Rules:** R1–R6 as in Step 2, fixed Sunday 13 June, applied per system and region; each action with an owner, a date and the contract step.

**Pressure-test log (10 lines; excerpt):** "4 regions live" wrong → reduce by 1 July (CEO); "every declaration reviewed" wrong → KPI 9–10, 5% QA (Shlomo); "₪6.2M" wrong → restate to ≈ ₪0.76M (CFO); "0 incidents" wrong → list every incident since January; retraining fragile → fix the feed, trigger at overrides above 20% (IT, Fadi); vendor releases fragile → test tenant, MSA 4.3 notice enforced (Dmitri); auto-submit in Q3 wrong → removed until two QA quarters under 2%; score and cameras in Europe wrong → removed (Annex III 4(b), GDPR, EU counsel); one owner for everything fragile → one business owner per system; Assist 35% deflection wrong → 90-day test.

**Controls:** review paper only (19 s, 7.0%); dispatcher approval real in the North; change notice not applied; retraining not running; incident process without a privacy branch; Assist hand-over real.

**Trust plan:** board — status note 10 June (kept), labelled pre-read; Gefen — written account 24 June, pre-fill off from 21 June; customs — KPI back from 27 June; works committee — written answer and the score off by 1 July, joint committee under clause 14.4 in July; South and Centre — seats off, Rania and two dispatchers on the routing review; vendor — written requests, then a remediation plan.

**Tesfaye (when consultation was promised first):** the committee would agree to route planning in all regions with no individual scores, no in-cab camera, location data kept 30 days and seen only by dispatch, the safety officer and the driver, no disciplinary use, overrides not held against drivers, drivers on the redesign. **Rania:** would try again if the tool knows today's roads, dispatchers decide, no scores.

**Agreed on 24 June (with both):** incident reopened 14 June and closure criteria in paper 05; the audit's first draft accepted with two changes (Route North "keep and fix"; Assist "keep under test"); notice for Ofer's signature by 30 June, sent 1 July, Ilana informed; the 14 April note retrieved on 22 June, read by Ofer with you on 23 June, to the chair as a fact; Svetlana owns the register until the head of AI starts.

</details>

## References

- Histadrut, [AIG Israel workers' committee declare labour dispute over AI](https://global.histadrut.org.il/news/aig-israel-workers-committee-declare-labour-dispute-over-ai/) (August 2026): a works committee demanding that AI be regulated through the collective agreement.
- law.co.il, [Monitoring employees' email severely restricted](https://www.law.co.il/en/articles/2011/04/25/monitoring-employees-email-severely-restricted/): *Isakov Inbar*, National Labour Court, 8 February 2011 — policy, transparency, proportionality before monitoring.
- AI Act Explorer, [Annex III](https://artificialintelligenceact.eu/annex/3/), point 4(b), and [Digital Omnibus on AI](https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/): Annex III obligations from 2 December 2027. Read on EUR-Lex before relying on it; Vantage Europe's position is EU counsel's.
- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): pressure-testing, wrong vs fragile (named, not re-taught).
- [Simulation: Risk register tester](../../simulations/risk-register-tester/index.html?preset=harbor) (Harbor & Pine's preset; educational model).
- Field kit: [04.5 · Risk register from zero](../module-04/lesson-05.md), [06.5 · The comms pack](../module-06/lesson-05.md), [07.2 · Scale, fix or stop](../module-07/lesson-02.md), [07.4 · The steering meeting](../module-07/lesson-04.md), [07.7 · Pressure-test a roadmap](../module-07/lesson-07.md).
- Templates: [pressure-test log](../../templates/pressure-test-log.md), [risk register](../../templates/risk-register.md), [comms plan](../../templates/comms-plan.md), [decision record](../../templates/decision-record.md).
- Earlier: [17.3 · Diagnosis](lesson-03.md). Next: [17.5 · Decide: the stop/keep audit and the incident closed](lesson-05.md).
