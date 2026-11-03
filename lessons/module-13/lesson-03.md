---
id: "13.3"
module: 13
minutes: 18
practice_minutes: 120
prerequisites: ["13.2", "03.1", "03.3", "03.7", "03.9"]
objectives:
  - "Build a baseline sheet where every measure has one definition, a label and an owner who will report it after you."
  - "Map the opportunities against the losses, including the non-AI ones, and screen each with a data gate."
  - "Net the vendor's claim and your own candidates with the CFO's numbers, separating lost contribution, overtime and capacity."
  - "Write a one-page case that asks for a staged decision with a stop rule."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): identifying and prioritising opportunities; business cases and ROI models"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Organisation of Labour Supervision (Safety Management Programme) Regulations, 5773-2013 (תקנות ארגון הפיקוח על העבודה (תכנית לניהול הבטיחות)), regs 1 and 5, Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/תקנות_ארגון_הפיקוח_על_העבודה_(תכנית_לניהול_הבטיחות)
  - title: "Claude pricing page (Sonnet 5.5 US$2 / US$10 per million tokens), checked 3 November 2026"
    url: https://claude.com/pricing
last_verified: "2026-11-03"
---

# 13.3 · Diagnosis

Your findings say the loss is mostly moulds at night and that nobody records what failed. Now you have to turn that into something the CFO can fund and the CEO can say yes to: baselines with one definition and an owner, a map of what could reduce the loss (AI and not), a screen that tests each option against the data it needs, a netted number for each, and a one-page case. In this lesson you build all four. At the end you have the case you take to Dalia and Orit on Thursday 11 February.

## The situation

Sunday 31 January to Thursday 11 February 2027. The memo went to Dalia on 28 January; she showed the Plant G section to Eli herself, and he took it better than expected. Amnon has read the first page and asked one question: "So what will fix Arava?" Predictiva presents on 15 February. Orit has given you 45 minutes on 11 February.

This is module 3 compressed: the [opportunity map](../module-03/lesson-01.md), the [fast screen](../module-03/lesson-03.md), the [ROI model that survives finance](../module-03/lesson-07.md) and the [decision-ready case](../module-03/lesson-09.md). IBM's consulting certificate asks for the absorption capacity of the receiving team and the expected cost of errors; here the receiving team is a night shift with one technician, and the expected cost of an error includes a burnt heater and a missing lockout step.

## What to do

### Step 1 — A baseline sheet with one definition per measure

Every number the decision will rest on gets a definition, a value, a label and a future owner. A measure without an owner is gone the week you go back to your day job. The core of Kinneret's sheet:

| Measure | Definition | 2026 | Label | Owner from April |
|---|---|---|---|---|
| Unplanned downtime | ProdTrack stops except PM, SETUP, NO_ORDER; stop to restart | 11,932 h (moulds 5,479; machine 2,840; waiting 1,538; material 1,051) | M (split D) | Dalia, Eli |
| Night mould stops | MOULD stops starting 22:45–06:45 | 229 stops, 3,255 h, mean 14.2 h | M | Fadi Khoury (tooling) |
| MTTR | Stop to production restart, both plants | K 5.7 h, G 5.8 h | M | Operations excellence |
| PM done | PMs closed **with labour recorded** ÷ scheduled | 92.4% (reported 96.7%) | M | Vladimir Kaplan |
| Breakdowns with a failure mode | Code not blank, not 99 | 14.2% (K); 0 (G) | M | Vladimir Kaplan, Shlomi Biton |
| Night calls | Supervisors' log | 78 (Mar–Dec); median 42 min waiting | M | Tigist Wondimu |
| Arava OTIF | The customer's measure | 81% | M (customer's) | Danny Golan |

Two changes of definition are themselves deliverables: MTTR on one definition at both plants, and PM counted with labour. Put them in the April deck, with the old figure beside the new one for three months, so nobody thinks performance changed overnight.

### Step 2 — Map the opportunities against the losses

Use the [opportunity map](../../templates/opportunity-map.md). Start from the losses, not from the technologies, and include candidates that use no AI at all:

- **Moulds at night (3,255 h):** a toolmaker on call, first-response training for technicians on hot-runner and water faults, spare thermocouple and heater kits, a written rule (with quality) on running a mould with a cavity closed, shot counters on the hot-runner moulds so mould PMs can be planned.
- **Machine faults (2,840 h):** restore the six deferred PMs; threshold alarms on the three machines that already have sensors (K22's failure was visible for three weeks); sensors on the machines with most machine-fault hours; Predictiva on all 40 machines.
- **Waiting (1,538 h) and night knowledge:** the night-call log says technicians wait for answers; a maintenance-manual assistant in their languages; a parts view that is true.
- **Data for any of it:** a common register incl. moulds; failure recording at the machine in three languages.
- **Quality and Arava:** QA cover for first-article approval at night (the October short shots were night restarts).

### Step 3 — Screen with a data gate

Use the [use-case scorecard](../../templates/use-case-scorecard.md) and its data gate from [03.3](../module-03/lesson-03.md): does the data the option needs exist, in the form it needs, today? For Predictiva the gate is the vendor's own: 12 months of coded failures and at least 30 per failure mode. Kinneret has 73 usable labels in 2026 and no mode above 12. It fails the gate. The night mould rule needs ProdTrack and tooling's records; it passes. The manual assistant needs the manuals and procedures, curated; it passes after curation.

### Step 4 — Net every option with the CFO's numbers

Ask Orit what an hour costs; don't take the vendor's revenue-per-hour. Her answer (roleplay: [Orit Navon](../../labs/module-13/personas/orit-cfo.md); [transcript](../../labs/module-13/personas/transcripts/orit-cfo.md)): about **₪310** of lost contribution when the machine is on a fully loaded job, which was about 40% of machine hours in 2026; the rest is recovered with overtime or another machine. Value the recovered 60% at the overtime it costs: ₪95 a machine-hour is your assumption until Orit confirms it. Blended: 0.4 × 310 + 0.6 × 95 ≈ **₪181 an unplanned hour**, directional.

Now net the vendor at its own best figure, before any doubt about it:

| | Predictiva at its best claim | Night mould response |
|---|---|---|
| Hours it can touch | Machine faults, 2,840 h (moulds are not covered) | Night mould stops, 3,255 h |
| Effect | 50% → 1,420 h | Night mean 14.2 → 8 h → about 1,420 h |
| Value a year | ≈ ₪257k (D) | ≈ ₪257k (D) |
| Cost | US$60,000 + US$95 × 40 assets × 36 months = US$196,800 → ₪617,165 at ₪3.136; + kits and installation ₪410,600 → **≈ ₪1.03M over 3 years, ₪343k a year** | ≈ ₪130k (on-call allowance, training, kits, shot counters) |
| When | After 12 months of coded data and a 90-day learning period: 2028 at the earliest | From April |
| Data gate | Fails | Passes |

Even if Predictiva worked exactly as advertised, it would cost more a year than it returns, and not before 2028. The same number of hours is available from the night rule, this quarter, for a fraction of the cost. That is not an argument against AI; it is an argument about order.

Two more lines matter to a CFO:

- **Capacity is not cash.** The assistant may save technicians and the maintenance manager some hours; the night calls cost 64 hours of machine waiting in ten months. Label them capacity. The assistant's case is correct, safe answers in the technician's language and less dependence on one person who plans to retire, not money.
- **Cost of an assistant answer.** About 11,500 input and 250 output tokens a question with the whole pack in context: at the listed Sonnet 5.5 price (US$2 / US$10 per million tokens) about US$0.026, ₪0.08 a question. Three hundred questions a month cost less than ₪30. The cost is in curating and owning the pack, not in tokens.

[Simulation: Pilot economics](../../simulations/pilot-economics/index.html?preset=generic)

### Step 5 — The one-page case

Use the [decision-ready case](../../templates/decision-ready-case.md). One decision, a front page anyone can read in two minutes, and the evidence behind it:

- **Decision asked:** release ₪730,000 of line 7400-210 in three stages: the Arava actions, the data foundation, a manual-assistant pilot; do not sign with the vendor in 2027; re-decide predictive maintenance in January 2028.
- **Why:** the loss is mostly moulds and waiting; predictive maintenance needs records Kinneret does not keep and covers a quarter of the loss.
- **What it buys:** the night mould response ₪130k; parts ₪40k; assistant ₪45k; register and recording ₪305k; sensors on eight machines ₪140k; contingency ₪70k.
- **Payback:** the night mould response and the six PMs ≈ ₪329k a year against ₪130k (D). The foundation and the safety items are infrastructure and compliance: no payback is claimed for them, and you say so. (The safety management programme regulations already require a list of items needing periodic tests and of procedures with their update dates; the register work serves that too.)
- **Stages and stop rule:** stage 1 to 30 April, stage 2 to 30 June, stage 3 to 31 December; if fewer than half of breakdown work orders carry a failure mode on 30 June, stage 2 recording spend stops.

## Watch out

- **Valuing every hour at the vendor's revenue per hour.** Ask the CFO; most hours are recovered at overtime cost.
- **A map with only AI on it.** At Kinneret the cheapest hours are a toolmaker's phone number and a rule written with quality.
- **Netting the vendor at your own pessimism.** Net it at its own best claim first; if it fails there, the argument is over without a fight.
- **Freed hours shown as savings.** Capacity, labelled.
- **Asking for the whole line at once.** Stages, gates and a stop rule are what lets a cautious CFO say yes.
- **Forgetting Arava.** The CEO asked "what will fix Arava?" The case answers that question first.

## Your turn

### Inputs

- Your findings memo from 13.2; the [data room](../../labs/module-13/data-room/INDEX.md) (module download): `company/budget-2027-extract.md`, `company/arava-letter-2026-12-14.md`, `vendor/predictiva-proposal.md`, `vendor/predictiva-onboarding-guide-extract.md`, `production/downtime-events-2026.csv`, `maintenance/night-calls-2026.csv`.
- Persona: [Orit Navon](../../labs/module-13/personas/orit-cfo.md) or her [transcript](../../labs/module-13/personas/transcripts/orit-cfo.md); [Dalia Mizrahi](../../labs/module-13/personas/dalia-vp-operations.md) for the case review; [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [ROI model](../../templates/roi-model.md), [decision-ready case](../../templates/decision-ready-case.md).

### Steps

1. Build the baseline sheet: at least seven measures, each with a definition, a 2026 value, a label and an owner from April.
2. Map at least eight candidates against the losses, at least four of them without AI.
3. Screen each with the data gate; write the verdict per candidate.
4. Interview Orit (or read the transcript); net Predictiva at its best claim and your top two candidates with her numbers.
5. Write the one-page case with stages, a stop rule and what the CEO can tell Arava.

Python is not worth it here: the case is a dozen numbers you must be able to explain line by line; a spreadsheet keeps them visible. Re-use `discovery.py` from 13.2 for the inputs.

### Time

120 minutes: 25 for the baselines, 25 for the map and screen, 30 for the netting and the CFO, 40 for the case.

### Done when

- [ ] MTTR and PM compliance are each on one definition, with the old figure shown beside the new.
- [ ] The map includes non-AI candidates and every candidate has a data-gate verdict.
- [ ] The vendor is netted at its own best claim, with the CFO's cost of an hour and the exchange rate stated.
- [ ] Freed hours are labelled capacity; no saving is claimed for the foundation.
- [ ] The case asks for stages with gates and a stop rule, and answers "what will fix Arava?"

<details><summary>Reference answer</summary>

The full set is `labs/module-13/expert/03-baselines-and-case.md` (module download).

**Screen (excerpt):** Predictiva on 40 machines — fails the data gate (73 usable labels, none of 30 per mode, 3 machines with sensors), best-case ≈ ₪257k a year against ₪343k a year, from 2028: **not yet**. Night mould response — passes, ≈ 1,420 h ≈ ₪257k a year for ₪130k: **do now**. Six PMs restored and measured with labour — ≈ 400 h ≈ ₪72k: **do now**. Parts view — small hours, removes a wrong source: **do now**. Manual assistant — value is safe answers in four languages, not hours: **pilot**. Register and recording; sensors on eight machines: **foundation**. Scrap-based early warning: **2028, with the predictive-maintenance re-decision**. QA cover for night first articles: **route to Rotem**.

**Case front page:** "Release ₪730,000 of line 7400-210 in three stages for the Arava actions, the maintenance data foundation and a manual-assistant pilot; do not sign with Predictiva in 2027; re-decide in January 2028. Night mould response and the six PMs pay back in under six months (directional); the foundation and the safety items are infrastructure and compliance, with no payback claimed. Stop rule: under half of breakdowns coded on 30 June stops stage 2 recording spend. For Arava: target OTIF 92% in Q3, 95% in Q4."

**What the transcript's interviewer missed:** they never asked Orit what she would need to release money, so her condition — a baseline, stage gates with dates, an owner per stage and a stop rule — only surfaces in 13.6. The case above happens to meet it; ask, don't guess.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): opportunity identification, absorption capacity, business cases (named, not re-taught).
- [Organisation of Labour Supervision (Safety Management Programme) Regulations, 5773-2013](https://he.wikisource.org/wiki/תקנות_ארגון_הפיקוח_על_העבודה_(תכנית_לניהול_הבטיחות)): who needs a programme (factories with 50+ workers), the list of items needing periodic safety tests and of procedures with update dates (reg. 5).
- [Claude pricing](https://claude.com/pricing): Sonnet 5.5 at US$2 input and US$10 output per million tokens, checked 3 November 2026. Prices change; check your provider's page before quoting. Exchange rate: ₪3.136 per US$ (Bank of Israel representative rate, 2 November 2026, used throughout the course).
- Field kit: [03.1 · The opportunity map](../module-03/lesson-01.md), [03.3 · The fast screen](../module-03/lesson-03.md), [03.7 · The ROI model that survives finance](../module-03/lesson-07.md), [03.9 · The decision-ready case](../module-03/lesson-09.md).
- Templates: [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [ROI model](../../templates/roi-model.md), [decision-ready case](../../templates/decision-ready-case.md).
- Next: [13.4 · The hard part: not yet, and fund the foundation](lesson-04.md).
