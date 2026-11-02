---
id: "09.6"
module: 9
minutes: 20
practice_minutes: 110
prerequisites: ["09.5", "07.1", "07.2", "07.3", "07.4"]
objectives:
  - "Build a readout pack with one recommendation, a recommend-against and a de-scope, every number labelled."
  - "Check every claim in the pack against the deliverable it comes from before the meeting."
  - "Rehearse the hardest finding with the stakeholder most likely to resist it, and record the decision with its dissent."
  - "Compare your deliverables with the expert's and the hidden truth, and score them against the rubric."
volatility: concept
sources:
  - title: "IBM Lead AI Transformation (Coursera) — course 4 (ship / ship with conditions / wait; decision record with dissent) and course 6, Measure AI Value and Scaling Transformation"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
  - title: "IBM Enterprise AI Transformation and Consulting (Coursera) — course 6, AI Governance, Risk, and Executive Communication"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-02"
---

# 09.6 · Readout and debrief

Twelve weeks after the call, you stand in front of a joint session of the steering group and the risk committee with a recommendation your sponsor did not ask for. In this lesson you build the readout pack, check that every claim in it traces to evidence, rehearse the hardest finding with the person most likely to resist it, and write the decision record. Then you open what was really going on at Meridian and see three ways the next six months went. At the end you have a readout pack, a decision record, and an honest score of your own work against the expert's.

## The situation

Tuesday 26 January 2027, 16:00, the board room. Present: Prof. Hanna Sela (chair of the risk
committee), Avner Shamir (CEO), Ilana Bar-Lev (COO), Eran Paz (CFO), Natalia Gurevich (Chief Actuary),
Michael Ohana (CRO, secretary) and Yusuf Darawshe (VP Claims). Since 4 January intake sends the
complete documents list on day one, in the claimant's language; three weeks of data, during storm
season, with no holdout. Your pilot eval and verdict went out on 14 January.

The CEO still has "₪20M" in his head, from October. The chair has read the complaint file of
CL-2026-026307. IBM's governance course ends with ship, ship with conditions or wait, and a decision
record that keeps the dissent; its value course ends with scale, sustain or retire. Here you bring both
to the same table, and then find out what happened next.

## What to do

### Step 1 — Build the readout pack around one recommendation

Use the [steering pack](../../templates/steering-pack.md) from [07.1](../module-07/lesson-01.md). Page
one carries:

- **One recommendation,** in a sentence a board member can repeat: *make claimants wait less by asking
  for every document once, on day one, and help intake read documents only where it is measured to
  work.*
- **A recommend-against** with its reason: Fraud Insight Pro (₪1.14M over three years) and Fraud Insight
  on home claims.
- **A de-scope:** the winter pilot of 1 December, replaced by shadow mode after the peak.
- **Three numbers, each labelled** measured, directional or assumed (the course's labels; IBM's value
  course uses the same idea): the claimant's 32-day median wait and its 12.8-day document chase
  (measured); the 3.87× referral disparity (measured); the pilot's offline result (in this course, an
  illustrative worked example; in your engagement, your own measured run).
- **What a "no" means:** Smart Intake stays under its conditions; claimants keep waiting on documents;
  the ₪20M is not pursued either way.

### Step 2 — Run the integration check before anyone else does

The [integration check](../../templates/integration-check.md) traces every claim in the pack to the
deliverable that supports it, and every human control to the line that pays for it:

| Claim in the pack | Traced to | Consistent? |
|---|---|---|
| Shadow mode from 15 March | Peak ends in February (09.3); Yusuf's capacity from March | Yes |
| A handler checks every field | Human-review design; the value line nets the checking minute | Yes |
| Arabic pre-fill only after a production re-test | Verdict G2 (09.5); Haifa scanner replaced 1 March | Yes |
| No fraud benefit counted | Case (09.3); the CFO's rule | Yes |
| DPIA before shadow mode | Committee condition (09.4); DPO | Open: due 1 March |
| "Second rounds down to 38%" | Three weeks of new claims after 4 January | Directional only: peak weeks, no holdout. Say so |

The last row is the kind of number that gets you in trouble: it is good news, it is early, and it is
not a controlled comparison. Label it, or leave it out.

### Step 3 — Rehearse the hardest finding with the person most likely to resist it

The hardest finding is not the disparity; it is who it implicates. Ilana left the 9.4 modules on in
August without the assessment the committee minuted, and she told the CEO "₪20M". [07.3](../module-07/lesson-03.md)
gave you the method: answer first, the finding once, evidence separate from inference, live options.
Roleplay it with [Ilana](../../labs/module-09/personas/ilana-coo.md) before the meeting, then run the
[coach prompt](../../labs/common/coach-prompt.md) on your transcript.

A version that works:

> "The disparity came from a vendor default nobody reviewed; it has been off since 22 November. So it
> cannot happen silently again, feature releases now go through the AI intake register before they
> are switched on. The ₪20M was the vendor's figure: Natalia's measured range for leakage is ₪3–6M, and
> we cannot yet show a score that finds any of it. I suggest you tell Avner yourself before Tuesday."

What does not work: softening it until it is untrue ("some adjustments were made"), or making it
personal in front of the CEO.

### Step 4 — Prepare for each person at the table

| Who | Will ask | Your answer, in one line |
|---|---|---|
| Prof. Sela (chair) | "What was the claimant told, and what is she told now?" | The sentence from 09.4; Samira received a written explanation in Arabic, the ₪1,450 rental and an apology |
| CEO | "Where is my ₪20M?" | It never existed; confirmed fraud is ₪2.34M a year to date and was found by handlers |
| CFO | "What do we spend, and what comes back?" | ₪95k spent, ₪60k now, ₪85k held to May; capacity, not cash |
| Chief Actuary | "Which numbers are measured?" | The labels on page one |
| CRO | "Who can stop it?" | VP Claims (operations), DPO (privacy), CRO (risk), named in the record |
| VP Claims | "Who reviews in March?" | Two team leads at four hours a week, agreed on 19 January |

Rehearse the steering meeting itself as in [07.4](../module-07/lesson-04.md), with the persona files of
the people at the table.

### Step 5 — Write the decision record

The [decision record](../../templates/decision-record.md) from [07.2](../module-07/lesson-02.md): the
decision per system, the money released and held, the evidence with labels, the options considered and
why not, yes/no conditions for the next gate, who can stop it, the dissent, the next review date,
signed by the chair and the budget owner.

### Step 6 — Debrief: compare and score

Open the expert's deliverables (module download, `labs/module-09/expert/`) and score each of yours with
the rubric in the [module project](../../projects/m09-meridian-mutual.md). Then open the hidden truth
and the futures below, in that order.

<details><summary>The hidden truth (open after your readout)</summary>

**The stated ask was a solution to the wrong problem.** "Automate claims intake and spot fraud" aimed at
the 2.5 days of intake and at a fraud figure nobody had measured. What was really going on:

1. **Claimants waited on documents, not on typing.** A median 32 days, of which 12.8 chasing documents;
   45% of later requests asked for documents on the day-one list; the list went out the same day for
   5.6% of claims. Intake staff waited for agents to send "everything"; the travel-medical list never
   asked for a translated report. The fix needed no AI.
2. **The dashboard measured the regulatory clock and was read as the claimant's wait.** Internal audit
   had said so in 2025 (finding 3, report IA-2025-07, open and overdue). Team leads set "file complete"
   late, and the 10.5 days looked fine because the slow part was outside it.
3. **The "AI" fraud score was a weighted rules list, live without approval, and it discriminated through
   proxies.** Ilana told the CIO in August to "leave the modules on, they're included"; the 30-day
   opt-out passed; the committee's action 6.1 was never done; the June statement became false on 6
   September. The vendor's Israel template carried F08 "interpreter required" and F09 "risk area",
   chosen in 2019–2021 because they correlated with SIU *referrals*. Of the 65 Arabic-speaking
   claimants auto-referred July–October, 3 had actually committed fraud; of 33 Hebrew-speaking, 20 had. Yusuf had
   heard it from Haifa handlers in September and said it only in a corridor.
4. **"Fraud prevented" counted deductibles and people who gave up.** Samira's ₪1,950 deductible is in
   the ₪6.77M. 111 claimants withdrew this year, some of them after long investigations. Samira almost
   did; she also paid ₪1,450 for a rental car nobody told her she could claim.
5. **Smart Intake was tested under conditions that were not Meridian's** (typed Hebrew forms at 300 dpi),
   failed on Eastern Arabic digits, copied diagnoses into a field every claims user sees, sent documents
   to Frankfurt without the DPO knowing, and saved no time.
6. **Handlers had already solved the language problem themselves,** with personal ChatGPT and Gemini
   accounts, sometimes with unredacted email attachments; the DPO said "no" once in September and
   nothing followed.
7. **The pilot window was the peak.** Nothing tested in January would have been tested at all.

</details>

<details><summary>Six months later: three futures (July 2027)</summary>

**1. "Switch it all on" — the proposal as written.** Smart Intake goes to all centres and Fraud Insight
to home claims on 1 December; Pro is signed on 28 December (₪1.14M). Storm week, 3–7 January: home
referrals jump, the SIU queue triples, temporary clerks re-key Arabic invoices by hand. The dashboard
shows 19 days in January; claimants wait over 50. Complaints about investigations triple; the
Authority's public inquiries unit asks Meridian to explain the rise. In April an Arab civil-rights
organisation files a motion to certify a class action under the Prohibition of Discrimination Law.
Internal audit rates AI governance unsatisfactory in May; Fraud Insight is switched off the same month.
Confirmed fraud is unchanged; the ₪20M is quietly dropped, and so is the "48-hour claims" campaign.

**2. The expert path (this module's reference answers).** Auto-referral off on 22 November; F08, F09
and F13 disabled; the 15 December committee blocks Fraud Insight, puts Smart Intake under conditions,
says no to Pro and corrects the June statement. The documents list goes out complete on day one from 4
January. The extraction pilot runs in shadow mode from 15 March (Hebrew, Russian, English), Arabic from
May after the digit fix and the new Haifa scanner. By July: document rounds per claim 1.62 → 1.27; the
claimant's median wait 32 → 23 days; the Arabic/Hebrew referral ratio 1.1; confirmed fraud 19% of
closed SIU cases, because referrals now have reasons. The CFO books no fraud savings and about 2,300
handler hours of capacity, used to drop two of the six winter temps next year. The dashboard's headline
is the claimant's wait; internal audit closes finding 3. Samira gets a written explanation in Arabic,
the ₪1,450 and an apology; she does not withdraw her complaint, but she tells the complaints officer
"at least someone answered".

**3. Half-way.** The committee approves Smart Intake for the winter "with monitoring" and keeps Fraud
Insight with the referral threshold raised to 60. The proxies stay in: the Arabic referral ratio is
still 3.4×. In April a Claims QA sample finds ₪180,000 of overpayments keyed from wrong pre-filled
amounts on Arabic invoices. Internal audit's Q2 finding forces both modules off in June. The documents
list, which needed no AI, never got anyone's attention, and the claimant's wait is unchanged. The
committee stops trusting the AI programme's papers; the 2028 budget is cut by half.

**What made the difference** between futures 1 and 2 was not a better model. It was a baseline that
measured the claimant, an outcome test run on data the company already had, a vendor's claims read back
under their real conditions, an interim decision taken the week the evidence was clear, and a
recommendation that put the no-AI fix first.

</details>

## Watch out

- **A pack with three recommendations.** The committee will pick the easiest. One recommendation; the
  rest are conditions, de-scopes or recommend-againsts.
- **Early good news without a label.** Three weeks of fewer second rounds, in storm season, with no
  holdout, is directional. Say it is.
- **Protecting the sponsor by blurring the finding.** Give her the chance to tell it herself; do not
  make it untrue.
- **A decision record without dissent.** Record Ilana's view on Smart Intake, by name, and why it was
  not followed.
- **Reading the hidden truth before your readout.** The debrief only teaches if you committed first.
- **Scoring yourself on the numbers.** Score on the method: the expert's LLM numbers are illustrative;
  your structure, labels and honesty are what the rubric grades.

## Your turn

### Inputs

- Your deliverables from 09.1–09.5.
- Personas: [Ilana Bar-Lev](../../labs/module-09/personas/ilana-coo.md) for the rehearsal; for the
  meeting, the [cast](../../labs/module-09/personas/README.md) (Ilana, Michael, Natalia, Yusuf; the chair
  asks about the claimant). [Coach prompt](../../labs/common/coach-prompt.md).
- Templates: [steering pack](../../templates/steering-pack.md), [integration check](../../templates/integration-check.md),
  [decision record](../../templates/decision-record.md).
- Expert deliverables (open in Step 6): `labs/module-09/expert/` (module download).
- Rubric: [module project](../../projects/m09-meridian-mutual.md).

### Steps

1. Write page one: one recommendation, a recommend-against, a de-scope, three labelled numbers, what a
   "no" means, the decisions requested.
2. Run the integration check over your five earlier deliverables; fix or label what does not trace.
3. Rehearse the hardest finding with Ilana (roleplay, 15 minutes); coach it; rewrite your opening lines.
4. Prepare one-line answers for each person at the table.
5. Write the decision record, with conditions, stop authority and dissent.
6. Score your deliverables against the rubric; then read the expert's; then open the hidden truth and
   the futures. Write three sentences: what you found, what you missed, what you would do first next
   time.

### Time

110 minutes: 25 for page one, 20 for the integration check, 25 for the rehearsal and coach, 15 for the
decision record, 25 for the debrief.

### Done when

- [ ] Page one has one recommendation, one recommend-against, one de-scope and three labelled numbers.
- [ ] Every claim in the pack traces to a deliverable; anything early or uncontrolled is labelled.
- [ ] The hardest finding was rehearsed with Ilana and coached; the opening is answer first and true.
- [ ] The decision record has money released and held, yes/no conditions, who can stop it and the dissent.
- [ ] You scored your work with the rubric before reading the hidden truth, and wrote what you missed.

<details><summary>Reference answer</summary>

Full version: `labs/module-09/expert/06-readout-and-decision.md` (module download).

> **One recommendation:** make claimants wait less by asking for every document once, on day one, and
> help intake read documents only where it is measured to work. Concretely: keep the documents-list
> change live since 4 January; take the extraction pilot to shadow mode on 15 March (Hebrew, Russian,
> English; Arabic after it passes on production documents); keep Fraud Insight blocked until it is
> validated on confirmed fraud.
>
> **Recommend against:** Fraud Insight Pro (₪1.14M over three years) and Fraud Insight on home claims.
> **De-scope:** the winter pilot of 1 December, replaced by shadow mode after the peak.
>
> **What it rests on.** (1) Claimants wait a median 32 days; 12.8 of them chasing documents; 45% of
> later requests were on the day-one list (*measured*). (2) Fraud Insight referred Arabic-speaking
> claimants at 3.87× the rate of Hebrew-speaking ones through two proxy factors; auto-referral off since
> 22 November (*measured*). (3) The pilot extractor met its five gates offline (95.4% of fields; every
> language ≥ 93%); Smart Intake met none (82.1%; Arabic 62.2%) (*pilot: illustrative worked example;
> Smart Intake: measured*). (4) First three weeks of the documents list: second rounds on new claims 38%
> vs 45% (*directional: peak weeks, no holdout*).

**Decision record DR-2027-01 (extract).** Extraction pilot: shadow mode from 15 March (he, ru, en; ar
after re-test). Fraud Insight: blocked; validation plan approved (SIU outcomes recorded on every case from
1 February; re-test with 12 months of outcomes). Pro and home: not now. Money: ₪95,000 spent; ₪60,000
released; ₪85,000 held until the May gate. Conditions: DPIA and enterprise LLM agreement by 1 March (no →
shadow does not start). Who can stop it: VP Claims, DPO, CRO. Dissent: the COO would have extended Smart
Intake to home claims in January; not followed (no net time saved). Next review 18 May 2027. Signed:
Prof. Hanna Sela; Ilana Bar-Lev.

**Rehearsal outcome.** Ilana chose to tell the CEO herself on 22 January.

</details>

## References

- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), courses 4 and 6, and [Enterprise AI Transformation and Consulting](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 6 (named, not re-taught).
- Field kit: [07.1 · The steering pack](../module-07/lesson-01.md), [07.2 · Scale, fix or stop](../module-07/lesson-02.md), [07.3 · Delivering bad news upward](../module-07/lesson-03.md), [07.4 · The steering meeting](../module-07/lesson-04.md), [07.9 · Handover](../module-07/lesson-09.md).
- Templates: [steering pack](../../templates/steering-pack.md), [integration check](../../templates/integration-check.md), [decision record](../../templates/decision-record.md).
- Earlier in this engagement: [09.1](lesson-01.md), [09.2](lesson-02.md), [09.3](lesson-03.md), [09.4](lesson-04.md), [09.5](lesson-05.md). Project: [Meridian Mutual](../../projects/m09-meridian-mutual.md).
