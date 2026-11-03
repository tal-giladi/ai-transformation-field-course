---
id: "15.3"
module: 15
minutes: 16
practice_minutes: 100
prerequisites: ["15.2", "03.1", "03.3", "03.7", "03.9", "04.7"]
objectives:
  - "Build a portfolio baseline with one definition and an owner per measure, including the three numbers a board should see about AI governance."
  - "Name the binding constraint on getting AI into production with arithmetic, and screen the options — most of them not AI — against it."
  - "Label the register's claimed benefits as measured, directional or assumed, and separate money counted twice from money released."
  - "Write a one-page case for the sponsor and the CEO with one ask, the cost of waiting and what a no means."
volatility: concept
sources:
  - title: "Bank of Israel, Proper Conduct of Banking Business Directive 369, Management of Model Risk (English, 8/24): proportionality (§4), validation before use (§65)"
    url: https://www.boi.org.il/media/ggpbdtqp/369_en.pdf
  - title: "Bank of Israel, Circular 2792-06 (21 August 2024): phase-in for existing models (§12)"
    url: https://www.boi.org.il/media/tq1e3rqh/h2792_en.pdf
  - title: "IBM Lead AI Transformation Professional Certificate (Coursera): the binding constraint, pilot isn't scale, the CoE-bottleneck test"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-03"
---

# 15.3 · Diagnosis

The CEO's headline says the pilots are stuck. Your discovery says where: at a gate that holds one and a half AI systems a quarter, in a bank whose register counts some builds twice and misses the AI people actually use. In this lesson you turn the findings into a baseline the board can follow, name the binding constraint with arithmetic, screen the options (most of them are not AI), label the money, and write the one page you take to the CEO on 4 February. At the end you have a baseline sheet, the queue table, a screened opportunity map and a one-page case.

## The situation

Thursday 28 January 2027. The findings memo went to Dalit on the 21st; she read it twice and asked for "the one page for Avner" by Tuesday. You gave Mishov notice on the 28th (Dalit signed, Hagit was told first). The CFO wants comments by Sunday 31 January. The CEO's office has given you 30 minutes on Thursday 4 February.

In engagements so far, NN.3 measured a baseline for one process and picked a shortlist of use cases. At Crescent the thing you are diagnosing is the route to production itself, so the "use cases" on the opportunity map are mostly changes to how the bank decides. IBM's *binding constraint* is the idea; its CoE-bottleneck test asks whether a centre ships production outcomes. You are about to show the board that the planned centre would not, because the constraint is downstream of it.

## What to do

### Step 1 — A portfolio baseline with one definition per measure

Use the method of [02.4](../module-02/lesson-04.md) on the portfolio, not on a process. Each measure gets a definition, a source and an owner from now on:

| Measure | 31 Dec 2026 | Label | Definition / source / owner |
|---|---|---|---|
| Rows in the register | 43 | M | COO office register → AI CoE |
| Distinct builds | 40 | M | Rows sharing environment + test set = one build → AI CoE |
| In production through the approved route | 0 | M | Model Committee approval → MRM |
| In real use without approval | 3 known + 1 outside the register | M | Used on real matters at least weekly → AI CoE |
| Builds with a measured baseline | 22 of 43 rows | M | Register → model owner |
| AI submissions waiting / in validation | 15 / 2 (2 returned) | M | MRM queue → MRM |
| Median wait, longest | 193 days, 437 | M | Submission to 31 Dec → MRM |
| AI capacity | 1.5 full validations a quarter | M | MRM work plan → CRO |
| AI spend 2027 | ₪20.13M (₪0.42M counted twice) | M | Programme budget + register → CFO |

Then the **three numbers for the board** from [04.7](../module-04/lesson-07.md): reached production 0; decision time median 193 days, slowest the Branch FAQ at 437; declined 0. Read them together: a process that declines nothing is not reviewing, and one that approves nothing is being bypassed. Crescent's is both.

### Step 2 — Name the binding constraint with arithmetic

Show what each fix does to the queue, in MRM's units (3 AI slots a quarter):

| Design | Builds | To the central queue | Slots | Quarters |
|---|---:|---:|---:|---:|
| Today: all 40, full validation | 40 | 40 | 80 | 26.7 |
| A 16-person central build team, same gate | 40 | 40 | 80 | 26.7 (built faster, validated no faster) |
| Triage first (stop, merge, clean) | 26 | 26 | 52 | 17.3 |
| Triage + validation by risk tier (0.5 / 1 / 2) | 26 | 26 | 26 | 8.7 |
| Triage + decision rights by tier (only high to the queue) + templates | 26 | 6 | 12 | 2.7 |

The second row is the diagnosis in one line: adding builders upstream of a fixed gate makes the queue longer. Each later row is a decision someone else owns — the triage is the unit heads', the validation depth and the tier rule are the CRO's and the policy's. Directive 369 asks a bank to apply its requirements proportionately to a model's type, complexity and risk; Crescent's own policy applies full validation to everything. That is the constraint, and it is a policy, not a law.

The tier figures depend on the triage in 15.5 (12 low, 8 medium, 6 high of the 26 kept). The 1.5× effect of templates and an evaluation kit on validators' time is the simulation's assumption; label it.

> [!IMPORTANT]
> The 21 February 2027 phase-in (circular 2792-06, §12) applies to existing models in use. Whether the Branch FAQ, the call summaries or the dispute letters are "models in use" under the bank's policy is the CRO's call — but it is a question to put to her this week, not after the deadline.

### Step 3 — The opportunity map, screened

Use the [opportunity map](../../templates/opportunity-map.md) and the fast screen of [03.3](../module-03/lesson-03.md). At Crescent the options are mostly not AI:

| Option | Kind | Screen | Why |
|---|---|---|---|
| Decision rights and validation by risk tier | Policy | **Go** | The binding constraint |
| A catalogue of all AI in use, one owner each | Register | **Go** | The board's Q2 report and the survey answer need it |
| A shared platform on IT's landing zone | Infrastructure | **Go with a condition** | IT owns it; the Branch FAQ needs off the sandbox |
| Stop the weak, merge duplicates, clean copies | Portfolio | **Go** before contract dates | Frees slots and money |
| Take the kept builds through the new route in waves | AI, by tier | **Go** | The ten (and more) come from here |
| A 16-person central build team | Organisation | **Stop** | Adds to the wrong side of the gate |
| More validators only | Organisation | **Go with a condition** | Helps, but at full validation for all it still takes years; a contractor for the phase-in backlog is cheaper and faster |
| Cancel the assistant | Budget | **Stop** | Strands two of the best pilots; the usage figure has the wrong denominator |

### Step 4 — Label the money, and find what is counted twice

The register's `claimed_annual_benefit` adds up to **₪44.6M a year**. Before anyone quotes it:

- ₪1.9M of it is the same benefit claimed by two rows of the same build (the three copies).
- ₪12.55M comes from rows with no measured baseline; ₪7.4M from rows with a partial one.
- None of it is banked. Label the whole figure **assumed**, and the baselines **measured** only where the row says so and you have seen the source.

Do the same with the costs: ₪9.13M of unit AI lines in 2027, of which ₪420,000 is double-booked. The CFO's 15% (₪3.02M) is computed on a base that includes the double-booking. Point it out without scoring a point: "the base should be ₪19.71M; I'd still work to ₪3.02M".

Capacity vs cash ([03.7](../module-03/lesson-07.md)): the procedure assistant and the knowledge assistant free agents' minutes. That is capacity until the Contact Centre's staffing plan changes; it is not a line in the CFO's 15%.

### Step 5 — The one-page case

Use the [decision-ready case](../../templates/decision-ready-case.md) from [03.9](../module-03/lesson-09.md). One ask, labelled numbers, the cost of waiting, what a no means. Bring it to Dalit first (roleplay: [Dalit Ben-Ami](../../labs/module-15/personas/dalit-coo.md)) — she wrote the design you are about to replace, and she will carry it to Avner with you. Then the CEO (roleplay: [Avner Golan](../../labs/module-15/personas/avner-ceo.md); no-roleplay path: [the transcript](../../labs/module-15/personas/transcripts/avner-ceo.md)): find out exactly what he promised the board and what the board asked in return, and leave with a date, not a promise of ten.

> [!TIP]
> Avner said on 4 February that success is "customers and employees using AI the bank stands behind. Not a demo." Use his words on the front page. "Ten by December" is his number; "an AI use the bank stands behind" is his goal — and only the second survives the inventory.

## Watch out

- **A baseline without owners.** "Decision time" with no definition and no owner will be a different number every quarter. Write the definition now.
- **Diagnosing people.** "The committee is slow" and "units are slow" are both wrong; the rule is slow. Say it in slots.
- **Quoting the ₪44.6M.** It is the units' claim, partly counted twice, mostly unmeasured. Use it only labelled.
- **Arguing with the CFO's base in public.** Give him the corrected base privately and still meet his number.
- **A case with options instead of an ask.** The CEO has 30 minutes. One ask; the alternatives go in the appendix.
- **Promising the ten.** Promise a measure he can report every quarter.

## Your turn

### Inputs

- Your findings memo from 15.2; data room (module download): `ai/pilot-register-2026-12.csv`, `governance/mrm-workplan-2027.md`, `governance/model-review-queue-2026-12.csv`, `company/ai-programme-budget-2027.md`, `company/cfo-budget-review-2027-01-12.md`, `customers/complaints-monthly-2026.csv`.
- Personas: [Dalit](../../labs/module-15/personas/dalit-coo.md) and [Avner](../../labs/module-15/personas/avner-ceo.md), or [Avner's transcript](../../labs/module-15/personas/transcripts/avner-ceo.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [ROI model](../../templates/roi-model.md), [decision-ready case](../../templates/decision-ready-case.md).

### Steps

1. Build the baseline sheet: at least eight measures, each with a value, a label, a definition, a source and an owner; then the three numbers.
2. Build the queue table for at least four designs, and write the diagnosis in one sentence.
3. Fill and screen the opportunity map with at least six options, at least three of them not AI.
4. Label the claimed benefits and the costs: the total, the part counted twice, the part with no baseline.
5. Write the one-page case; walk Dalit through it; then meet Avner (or annotate his transcript).
6. Write your comments to the CFO (five lines): the base, the target, when the list comes.

### Time

100 minutes: 20 for the baseline, 15 for the queue table, 15 for the map, 10 for the money, 25 for the case, 15 for the two conversations.

### Done when

- [ ] Every measure has a definition and an owner; the three numbers are stated with the slowest item named.
- [ ] The queue table shows that a bigger central build team does not change the quarters, and what each fix does.
- [ ] The opportunity map has more non-AI options than AI ones, each screened with a reason.
- [ ] The ₪44.6M is labelled assumed, with the double count and the unmeasured part shown.
- [ ] The case has one ask, labelled numbers, the cost of waiting with dates, and what a no means.
- [ ] You left the CEO meeting with a date and a measure, not a promise of ten.

<details><summary>Reference answer</summary>

The full set is `labs/module-15/expert/03-baselines-and-case.md` (module download).

**Diagnosis in one sentence:** Crescent's pilots do not stall in the units; they stall at a gate that validates 1.5 AI systems a quarter because the bank's policy applies full validation to every AI use, and a central build team would add builders upstream of that gate.

**Queue table:** today 80 slots = 26.7 quarters; central team, same gate = 26.7; triaged full 52 = 17.3; triaged by tier 26 = 8.7; rights by tier with templates 12 = 2.7 (the 1.5× templates effect labelled assumed).

**Money:** claims ₪44.6M a year (assumed), of which ₪1.9M claimed twice and ₪12.55M with no baseline; unit lines ₪9.13M, of which ₪0.42M double-booked; CFO's base should be ₪19.71M, target kept at ₪3.02M.

**Case, front page (excerpt):** "Ask: on 15 March, decide how AI goes to production at Crescent — decision rights by risk tier, a hub-and-spoke CoE instead of a central build team, a catalogue first, and a triaged portfolio of 26 builds with 14 in production by March 2028. Why: the pilots stall at a gate that holds 1.5 AI systems a quarter for 40 builds (M); meanwhile AI runs without approval in branches, the contact centre and Cards (M), and the bank's survey answer says otherwise (M). Cost: within the 15%, with the assistant kept (D). What a no means: the queue stays at 1.5 a quarter, the shadow estate grows, and the board's first report has no inventory behind it. Cost of waiting: Mishov's 24-month renewal (notice given 28 January), Katvan AI 15 March, Kesher's generative features on by default in October."

**Comments to the CFO (31 January):** "Moshe, thank you. Two points before the list on 4 February: the base includes ₪420,000 budgeted twice (three pilots listed by two units), so it should be ₪19.71M; and the assistant hosts two of the bank's best-evidenced pilots, with 66% weekly use among trained users. I will still bring you ₪3.02M or more, from stopping, merging and the CoE's design, by 4 February."

**What the transcript's interviewer (Avner, 4 February) missed:** they asked what he told the board and what success means, but not what the board — or the chair — is worried about beyond the number, so the chair's question about the survey answer stayed hidden; and they never asked whether anything was promised outside the bank (the investor conference).

</details>

## References

- Bank of Israel, [Directive 369](https://www.boi.org.il/media/ggpbdtqp/369_en.pdf): proportionate application (§4), validation before use and documented compensating controls when it cannot be completed (§65).
- Bank of Israel, [Circular 2792-06](https://www.boi.org.il/media/tq1e3rqh/h2792_en.pdf), §12: in force 21 August 2025; existing material models within six months, other existing models within eighteen months.
- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution): binding constraint, "pilot isn't scale", the CoE-bottleneck test (named, not re-taught).
- Simulation (educational model): [Simulation: Operating model scaler](../../simulations/operating-model-scaler/index.html?preset=crescent) — try "today's set-up" now; you will design your own in 15.4.
- Field kit: [02.4 · Measuring a baseline](../module-02/lesson-04.md), [03.1 · Opportunity map](../module-03/lesson-01.md), [03.3 · The fast screen](../module-03/lesson-03.md), [03.7 · The ROI model](../module-03/lesson-07.md), [03.9 · The decision-ready case](../module-03/lesson-09.md), [04.7 · Governance that runs](../module-04/lesson-07.md).
- Templates: [opportunity map](../../templates/opportunity-map.md), [use-case scorecard](../../templates/use-case-scorecard.md), [ROI model](../../templates/roi-model.md), [decision-ready case](../../templates/decision-ready-case.md).
- Earlier: [15.2 · Discovery](lesson-02.md). Next: [15.4 · The hard part: an operating model that scales](lesson-04.md).
