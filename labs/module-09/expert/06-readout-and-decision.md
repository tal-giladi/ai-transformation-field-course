# Readout pack and decision record — AI in claims

*Joint session of the steering group and the risk management committee, Tuesday 26 January 2027,
16:00. Chair: Prof. Hanna Sela. Present: Avner Shamir (CEO), Ilana Bar-Lev (COO), Eran Paz (CFO),
Natalia Gurevich (Chief Actuary), Michael Ohana (CRO, secretary), Yusuf Darawshe (VP Claims); Head of
AI Transformation presenting. Templates: [steering pack](../../../templates/steering-pack.md),
[decision record](../../../templates/decision-record.md), [integration check](../../../templates/integration-check.md).*

## Page 1 — the recommendation

> **One recommendation:** make claimants wait less by asking for every document once, on day one, and
> help intake read documents only where it is measured to work. Concretely: keep the documents-list
> change live since 4 January; take the extraction pilot to shadow mode on 15 March (Hebrew, Russian,
> English; Arabic after it passes on production documents); keep Fraud Insight blocked until it is
> validated on confirmed fraud.
>
> **Recommend against:** Fraud Insight Pro (₪1.14M over three years) and Fraud Insight on home claims.
> **De-scope:** the winter pilot of 1 December, replaced by shadow mode after the peak.

**What it rests on** (labels: M measured, D directional, A assumed):

1. Claimants wait a median **32 days**; 12.8 of them chasing documents; 45% of later requests were on
   the day-one list (M).
2. Fraud Insight referred Arabic-speaking claimants at **3.87×** the rate of Hebrew-speaking ones
   through two proxy factors; auto-referral off since 22 November (M).
3. The pilot extractor met its five gates offline on 200 documents (95.4% of fields, every language ≥
   93%), Smart Intake met none (82.1%; Arabic 62.2%) (pilot: illustrative worked example; Smart
   Intake: M).
4. First three weeks of the documents list: second rounds on new claims 38% vs 45% (D, peak weeks, no
   holdout).

**What a "no" means:** Smart Intake stays as it is under its conditions; claimants keep waiting on
documents; the ₪20M is not pursued either way.

## Decisions requested

1. Approve shadow mode for the extraction pilot (₪60,000 of the ₪240,000; ₪95,000 already spent on
   the offline pilot).
2. Confirm Fraud Insight blocked; approve the validation plan (SIU outcomes recorded on every case
   from 1 February; re-test in Q1 2028 with 12 months of outcomes).
3. Ask BI to replace the dashboard's headline with the claimant's wait (closes internal audit's 2025
   finding 3).
4. Note the correction of the June statement (made 15 December) and the inventory entries AI-05,
   AI-06, AI-07 (sanctioned translation tool, live 18 January).

## Integration check (deliverable against deliverable)

| Claim in this pack | Traced to | Consistent? |
|---|---|---|
| Shadow from 15 March | Peak ends in February (baselines §3); Yusuf's review capacity from March | Yes |
| Handler checks every field | Human-review design; ₪180k value nets the check minute | Yes |
| Arabic after production re-test | Verdict G2; scanner replaced 1 March | Yes |
| No fraud benefit counted | Case §5; CFO's rule | Yes |
| DPIA before shadow | Committee condition; DPO | Due 1 March: **open** |

## Hardest finding, rehearsed with Ilana (21 January)

The finding most likely to be resisted: *the modules she left switched on in August caused the
referral disparity, and the ₪20M she gave the CEO has no source.* Rehearsed answer-first: "The
disparity came from a vendor default we did not review; it is off since 22 November; here is what we
changed so it cannot happen silently again (feature releases go through the AI intake register). The
₪20M was the vendor's figure; Natalia's measured range is ₪3–6M of leakage and we cannot yet show a
score that finds any of it." Ilana chose to tell the CEO herself on 22 January.

## Decision record DR-2027-01 — AI in claims — joint steering / risk committee, 26 January 2027

**Decision.** Extraction pilot: shadow mode from 15 March (he, ru, en; ar after re-test). Fraud
Insight: blocked; validation plan approved. Fraud Insight Pro and Fraud Insight on home: not now.
Dashboard: claimant's wait becomes the headline from the February report.

**Money.** ₪95,000 spent (offline pilot); ₪60,000 released for shadow mode; ₪85,000 held until the
May gate. Pro: ₪0.

**Evidence.** Findings memo (19 Nov), verdict (8 Dec), eval report (14 Jan); measured vs illustrative
labels as stated.

**Options considered.** Winter pilot as proposed: not chosen (peak; Smart Intake saves no time;
proxies). Buy Pro: not chosen (no validated benefit; ₪1.14M). Stop all AI in claims: not chosen (the
offline evidence supports a careful shadow run).

**Conditions.** DPIA signed and enterprise LLM agreement by 1 March (yes/no; no → shadow does not
start). May gate: gates G1–G5 on ≥ 1,000 production fields, ≥ 300 Arabic; rounds per claim measured
against the 1.62 baseline.

**Who can stop it.** VP Claims (operational), DPO (privacy), CRO (risk).

**Dissent.** The COO would have extended Smart Intake to home claims in January; recorded, not
followed (evidence: no net time saved).

**Next review.** 18 May 2027. Signed: Prof. Hanna Sela (chair); Ilana Bar-Lev (budget owner).
