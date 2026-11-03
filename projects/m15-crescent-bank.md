# Crescent Bank

Run the whole engagement at Crescent Bank, a fictional Israeli bank with about 4,000 people, 14 business units and 58 branches, as the newly appointed head of its AI centre of excellence, reporting to the COO. The CEO told the board "we have 40 pilots and nothing in production" and the board approved a 16-person central team. Your job is to find out what the 40 really are and why none reach production, design how AI should get to production in a regulated bank, triage the portfolio, meet a 15% budget cut without cutting the wrong thing, and bring one recommendation and a 12-month plan to the Management Committee. This is module 15's practical: one integrated deliverable set, every document consistent with every other.

## The brief

Read [the engagement brief](../labs/module-15/brief.md) (in the module download). In short: you start on Sunday 3 January 2027; the sponsor is Dalit Ben-Ami, COO; the CFO's budget review arrives on 12 January; the diagnosis goes to the CEO on 4 February; the Model Committee meets on 18 February; the Management Committee decides on Monday 15 March; the board revises the budget on 30 March. The central AI programme is ₪11.0M for 2027; the CFO wants 15% off all AI spend. The data room is `labs/module-15/data-room/` (start with its [INDEX](../labs/module-15/data-room/INDEX.md)); the people are in `labs/module-15/personas/` ([the cast](../labs/module-15/personas/README.md)); the triage sheet and the Track B scripts are in `labs/module-15/`.

## Deliverables

| # | Deliverable | Template | Lesson |
|---|---|---|---|
| 1 | **Mandate memo** for the sponsor (objective read back, the CEO's headline as a claim, done, scope set to every AI use, entry-role table, advisory boundary), first-read sheet, access request, three-week plan, note to the CEO | [engagement charter](../templates/engagement-charter.md), [scope boundary](../templates/scope-boundary.md), [data-room first read](../templates/data-room-first-read.md), [access request pack](../templates/access-request-pack.md), [30-60-90 plan](../templates/30-60-90-plan.md) | [15.1](../lessons/module-15/lesson-01.md) |
| 2 | **Findings memo** with evidence labels: the register tested (builds, copies, duplicates, owners, dependencies, evidence), AI in real use and outside the register, the queue in review slots, the assistant's denominators, contract dates; the same-day escalation | [findings memo](../templates/findings-memo.md), [AI inventory](../templates/ai-inventory.md), [shadow-AI survey](../templates/shadow-ai-survey.md), [interview guide](../templates/interview-guide.md) | [15.2](../lessons/module-15/lesson-02.md) |
| 3 | **Portfolio baseline** with one definition and owner per measure and the three numbers; the **queue table**; a screened **opportunity map**; labelled money; the **one-page case** | [opportunity map](../templates/opportunity-map.md), [ROI model](../templates/roi-model.md), [decision-ready case](../templates/decision-ready-case.md) | [15.3](../lessons/module-15/lesson-03.md) |
| 4 | **Operating-model paper**: the model the bank runs today, the archetype chosen on evidence, the hub–spoke line and sizes, the tier rule and decision table, the review queue, the three paved roads and the catalogue's fields, the route in, AI policy v2 outline, a simulation run | [governance charter](../templates/governance-charter.md), [AI intake register](../templates/ai-intake-register.md), [regulatory map](../templates/regulatory-map.md), [operating rhythm](../templates/operating-rhythm.md) | [15.4](../lessons/module-15/lesson-04.md) |
| 5 | **Portfolio triage** of all 43 rows with dated rules; stop and merge lists with evidence, one owner and dates; dependencies and the assistant decision; review load and 2027 money; the **12-month scale plan** with gates | [use-case scorecard](../templates/use-case-scorecard.md), [decision record](../templates/decision-record.md), [roadmap](../templates/roadmap.md), [phase-1 plan](../templates/phase-1-plan.md) | [15.5](../lessons/module-15/lesson-05.md) |
| 6 | **Readout** (one recommendation, two recommend-againsts, the CEO's sentence for the board), **integration check**, notes of the **rehearsal** with the CEO, **decision record** with a stop rule, **handover** | [steering pack](../templates/steering-pack.md), [integration check](../templates/integration-check.md), [decision record](../templates/decision-record.md), [handover pack](../templates/handover-pack.md) | [15.6](../lessons/module-15/lesson-06.md) |

## Steps

1. Read the brief and the INDEX; fill the entry-role table; meet Dalit; write the mandate memo, the first read, the access request, the plan and the note (15.1).
2. Interview at least four of Irina, Nir, Karim, Hagit, Tsega, Lina and Olga; test the register against the other files; find AI in use and outside the register; compute the queue and the denominators; escalate the exposure; write the findings memo (15.2; Track B: `discovery.py`).
3. Build the baseline and the three numbers; the queue table; screen the options; label the money; write the case; walk Dalit and Avner through it; reply to the CFO (15.3).
4. Describe today's model; compare the archetypes; draw the hub–spoke line; write and test the tier rule; size the queue; specify the roads and the catalogue; design the route in; pre-wire with Irina and Lina; run the simulation (15.4).
5. Write and date the triage rules; triage the 43 rows; stops, merges with one owner, dependencies, the assistant; the load and the money; the 12-month plan; play it in the simulation (15.5; Track B: `triage.py`).
6. Write the readout; run the integration check; rehearse with Avner twice; run the meeting; write the decision record and the handover (15.6).
7. Score your set with the rubric below **before** you open the hidden truth and the expert set in 15.6; then compare.

Time: about 4 hours beyond the lessons' own exercises, most of it in steps 5–7.

## Self-assessment rubric

| Criterion | What "strong" looks like | What "weak" looks like |
|---|---|---|
| Entry and mandate | The objective is the sponsor's, read back with her correction; "40 pilots and nothing in production" recorded as the claim tested; scope is every AI use; the regulatory boundary names the CRO, CCO, DPO, CIO and counsel | "Ten by December" promised; the register taken as the inventory; regulatory questions answered by the CoE |
| Discovery | 40 builds counted from 43 rows; copies, duplicates and patterns told apart; owners and dependencies tested; AI in use and outside the register each with a source and a number; people who showed workarounds protected | Rows counted as pilots; every overlap called a duplicate; shadow builders named or blamed |
| Queue and money | The queue in review slots and quarters in the CRO's units; the three numbers; the claimed ₪44.6M labelled assumed; the double-booking found; the assistant read with the right denominators | "Risk is the bottleneck"; benefits quoted unlabelled; the CFO's 16% accepted or attacked without the other denominators |
| Escalation | The customer-data exposure escalated the same day to the CISO's office, the DPO and the CIO, with an interim route that keeps the work going | Held for the memo, handled quietly, or punished |
| Operating model | Today's model named; archetypes compared on the bank's evidence; constants in the hub, variables in the spokes; the hub sized, not 16 builders | A smaller central team that still builds and decides everything; a midpoint labelled hub-and-spoke |
| Decision rights and model risk | A checkable tier rule owned by MRM, tested on real builds; only high risk uses central slots; medium reviewed against hub standards with MRM's critical review; anyone can stop; Directive 369 read by the CRO, not imported from US guidance | Tiers by the unit's own label; the CoE owns the rule; one gate for everything, or units decide high risk |
| Paved roads and the route in | Platform, evaluation kit and catalogue each with an owner, a date and a first user; the catalogue's fields include those of Directive 369 §32; shadow builds, perma-pilots and vendor AI brought onto the road with interim controls | Roads as slides; shadow tools shut down; vendor AI ignored |
| Triage and plan | Rules dated before the list; every row actioned with evidence; merges with one owner chosen by evidence and the other unit's needs kept; dependencies found before any cut; the 15% met with the assistant kept; a plan with yes/no gates and numbers per quarter | Stops by vote or by claimed benefit; joint ownership; the assistant cut; dates without gates; the simulation's numbers used as the plan |
| Recommendation | One recommendation; the two recommend-againsts on the front page with measured evidence; a sentence the CEO can say to the board; the hardest finding delivered privately from his own words | A menu of designs; the board's design attacked without an alternative; the CEO corrected in front of his committee |
| Follow-through | A decision record with owners, a stop rule, re-decision dates, the assistant's condition and dissent; a handover to the business, risk, IT and build owners with the dates you stop | "Approved, details to follow"; you keep everything; no condition for re-deciding |

## Model answer

<details><summary>Model answer</summary>

The expert's deliverable set is in the module download, `labs/module-15/expert/` ([README](../labs/module-15/expert/README.md)):

- [01 · Mandate memo and first week](../labs/module-15/expert/01-charter-and-first-week.md)
- [02 · Findings memo](../labs/module-15/expert/02-findings-memo.md)
- [03 · Baselines, the queue and the one-page case](../labs/module-15/expert/03-baselines-and-case.md)
- [04 · Operating model](../labs/module-15/expert/04-operating-model.md)
- [05 · Portfolio triage and the 12-month scale plan](../labs/module-15/expert/05-triage-and-scale-plan.md)
- [06 · Readout, decision record and handover](../labs/module-15/expert/06-steering-readout.md)

Every count, sum and share computed from the data room is real and reproducible with `discovery.py` and `triage.py`; the simulation figures come from the operating-model scaler's `crescent` preset and are an educational model. Lesson 15.6 reveals what was really going on at Crescent and three futures; read them only after scoring yourself.

</details>
