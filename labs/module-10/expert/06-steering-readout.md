# 06 · Steering readout, decision record and handover — Galil Health

Pre-read sent Thursday 14 January 2027; private session with Shlomit Sunday 17 January; steering committee
Tuesday 19 January, 09:00–10:00; handover Thursday 21 January.

## Front page

**One sentence.** Choose the scribe that passed Galil's own test in Hebrew, Arabic and Russian (Rishma,
hosted in Israel), start with twelve doctors in Nazareth and Karmiel in March once Fund A approves, and roll
out region by region only if the pilot passes on 6 May.

**Decision asked (to be minuted).**

1. Rishma Health named preferred vendor, subject to counsel's and the DPO's contract review, Fund A's approval,
   the cloud committee's approval and the staff committee's consultation.
2. A six-week pilot, 14 March – 20 April 2027, Nazareth and Karmiel, twelve doctors, with the stop rules in the
   pilot plan; budget ≈ ₪47,000.
3. Gate on 6 May 2027: rollout by region, Notara integration project, or stop.
4. From 1 February: no recording of visits on personal devices or public AI tools; no discipline for past use.
5. Nurses' own documentation: a separate evaluation in the second half of 2027.

**Recommend-against (on the front page).** Against signing any vendor for 120 seats by 31 December or before
Fund A approves, and specifically against ScribeWave on the quoted Standard plan: it failed Galil's test in
Arabic (word error 27%; 11.7 omissions per 100 notes) and with relatives (9.3 per 100); its plan lets it train
on de-identified recordings; audio is kept 90 days in the EU or the US; it refuses notice of model changes.
Also against MedNote's free year: correction took longer than writing a note today (6.0 vs 4.8 minutes), and
year two is unpriced.

**What a "no" means.** Doctors keep recording on consumer apps (about ten, by their own account; 6.9 GB of
uploads in four weeks); the 112 documentation minutes a doctor-day stay; the board hears "vendor not chosen".

**What it costs in 2027.** ≈ ₪0.9–1.1M including integration, inside the board's ₪1.6M. Capacity ≈ 600
doctor-hours a month at 30 minutes a doctor-day (assumed, measured in the pilot); cash only through
retention.

## Integration check (three contradictions found and fixed)

1. The pilot plan's first draft started on 1 March; Fund A's 45 days from 20 January end on 6 March. Fixed: 14
   March, after approval.
2. The case's capacity line (≈ 600 doctor-hours a month, ≈ ₪198,000 at ₪330 an hour) appeared in a draft board
   sentence as "₪2.4M saved a year". Removed: capacity, not cash.
3. The weekly audit of 10 notes per doctor (≈ 8 reviewer hours a week) had no hours in any budget. Added to the
   pilot budget (₪22,000 of clinician time) and to Wasim's team plan.

Checked and consistent: every PoC number in the pack matches `poc/review-sheet.csv`; the consent text and the
contract say the same thing about deletion and location; the staff-committee date is ≥ 30 days before the pilot.

## Rehearsal with the CEO (Sunday 17 January)

The hardest finding: *the vendor chosen at the demo failed Galil's test in the language of 38% of patients, the
quote would let it train on Galil's recordings, and the 31 December date could not have been met without Fund
A's approval, which Shlomit had told Fund A's director would be about recordings staying in Israel.*

First attempt opened with the PoC table; she defended the demo ("hundreds of hospitals") for ten minutes.
Second attempt opened with her own goal (doctors home at six, two posts filled by the summer), then Galil's
112 minutes and where they sit (mixed-language clinics), then the PoC in one line, then Fund A as a date, not a
reproach. She asked "so what do I tell the board?", and took the sentence: *"We chose on evidence from our own
clinics in Hebrew, Arabic and Russian; the vendor that looked best in the demo failed that test; twelve doctors
start in March, and the rest follow region by region if the pilot passes in May."* She asked that ScribeWave's
extended offer be kept as a fallback until 31 March.

## Decision record (Tuesday 19 January 2027)

| Item | Decision | Owner | Date |
|---|---|---|---|
| Preferred vendor | Rishma Health, Israel hosting, subject to the four conditions | Igor | — |
| Contract review; audio-and-record question to external counsel | Approved | Hagit | 3 Feb |
| Fund A approval; Fund B notice | Approved | Hagit | requested 20 Jan |
| Cloud committee reconvened; MOH report after signature | Approved | Igor | 27 Jan |
| Staff committee consultation | Approved | Suha with HR | 10 Feb |
| Pilot, Nazareth and Karmiel, stop rules | Approved | Wasim (clinical), Igor (operations) | 14 Mar – 20 Apr |
| Personal-device recording instruction and amnesty | Approved | Wasim | 1 Feb |
| Nurses' documentation evaluation | Deferred to H2 2027 | Suha | Sep 2027 |
| Gate | Rollout by region / integration / stop | Steering group | 6 May 2027 |

**Dissent, in the dissenter's words.** Shlomit: "Keep ScribeWave's March price on the table in case the funds
are slow." Recorded; no action beyond asking MedLink. Igor: "The Notara interface estimate is Notara's word,
not tested." Recorded as a risk with an owner (Igor) and a check before the gate.

## Handover (Thursday 21 January)

Owner: Igor; clinical owner: Wasim. The pack: charter, memo, baselines, RFP and answers, claim read-backs, PoC
protocol and results (`poc/`, `poc_score.py`), scoring sheet, contract terms, pilot plan with stop rules, the
documentation-time measure (`discovery.py`) for the gate, the decision record, the open questions for counsel.
Tested: Igor's analyst re-ran `discovery.py` and `poc_score.py` and reproduced the baseline and the PoC table.
One follow-up call on 29 April, before the gate.

**Which future this leads to:** the evidence path (future 3 in the debrief), *because* the deadline was tested
against the funds' contracts before anyone signed, and the CEO had a sentence for the board that did not
depend on the demo.
