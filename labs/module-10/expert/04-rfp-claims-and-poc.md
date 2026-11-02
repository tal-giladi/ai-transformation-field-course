# 04 · RFP, claim read-backs and the proof of concept — Galil Health

## The RFP as sent (Sunday 6 December 2026, excerpt)

Built on the [RFP for AI vendors](../../../templates/rfp-for-ai-vendors.md) template. Sent by Igor to the four
vendors; single point of contact Igor; answers due Sunday 20 December.

**Our conditions.** 14 clinics; 78 doctors; ≈ 26,000 doctor visits a month. Patients' preferred language:
Arabic 38%, Hebrew 30%, Russian 28%, other 3%; Galilee Arabic (urban, rural, Druze). Relatives in many visits,
often speaking for the patient about medicines. Ordinary consultation rooms (air conditioning, corridors,
children). Notes written in Hebrew in Notara: 9.2 in three regions, 7.4 in two. Patient information is
health information; Galil's health-fund agreements govern who may process it and where.

**Criteria and weights, locked 3 December by the steering group** (the criteria agreed before the first demo and
printed on the demo-day scorecards, re-confirmed unchanged after the readout): demo vs evidence ×2,
clinical safety ×3, privacy and data ×3, Hebrew/Arabic/Russian ×2, integration ×1, contract and exit ×2. The
demo is not scored again.

**Claims.** For every number in your materials: sample (real or scripted, n), what was measured, language
and specialty mix, who measured it, when, which version.

**Proof of concept.** 90 synthetic visits (30 per language) recorded by actors in Galil's rooms, delivered 13
December under an NDA for synthetic data; each vendor processes each recording twice and returns the notes
by 20 December; six Galil clinicians review every note against the script's fact list. No cost to vendors
beyond their time; no cost to Galil from vendors.

**Must-have terms** (refusal of any one excludes the vendor): T1 no training or improvement on our audio,
transcripts or notes, de-identified included; T2 audio deleted within 30 days of the note being signed,
with Galil able to instruct another period; T3 storage and processing in Israel or where Galil's DPO
approves in writing; T4 full sub-processor list, notice, right to object; T5 data returned in a standard
format, certified deletion, six months' transition; T6 notice before model changes and a re-run on Galil's
test set; T7 a named clinical safety officer and incident reporting to Galil within 12 hours (Galil must
notify Fund A within 24). Nice to have: T8 certification and audit rights; T9 a three-year price lock.

**Documents.** DPA and sub-processor list; security report or certificate; clinical safety case and hazard
log; **the product's intended purpose and regulatory status in writing** (does any feature suggest diagnoses,
codes or treatment?); independent evaluations; three references in conditions like ours; three-year price.

## Claim read-backs (decision first)

**Decision (9 December):** no vendor's headline number is evidence for Galil; Rishma's omission claim is the
only one worth relying on, and only as a hypothesis for the PoC.

| Claim (where) | Conditions | Who chose them | Fit to Galil | Rating |
|---|---|---|---|---|
| ScribeWave "98% accuracy" (slide 4) | 200 scripted English visits; orthopaedics, dermatology, urgent care; studio mic; one speaker; US accents; transcript words | Vendor | None of language, setting, speakers, specialty or measure | Not yet supportable |
| ScribeWave "2 hours a day" (slide 5) | Survey, 60 early adopters, 2 US systems, self-reported, no comparison | Vendor | Exceeds Galil's measured 112 min | Contradicted for Galil |
| ScribeWave "30+ languages incl. Hebrew, Arabic" (slide 6) | Hebrew beta on read-aloud text; Arabic MSA and Gulf | Vendor | Galilee dialects, conversation | Not yet supportable |
| Kol Refua "96% in Hebrew" (slide 3) | 40 visits, partner clinic (a shareholder), 2 doctors, Hebrew, self-measured | Vendor | Hebrew only; no Arabic | Worth testing (Hebrew) |
| Kol Refua "never leaves Israel" (slide 5) | DPA Annex B: US speech-recognition API | — | Audio goes to the US | Contradicted |
| Kol Refua "Arabic next quarter" | Roadmap slide | Vendor | 38% of patients | Not yet supportable |
| MedNote "95% accurate" (release notes) | Dictation, one clinician to the mic, Notara internal, Hebrew | Vendor | Ambient mode is a different task, "preview" | Not yet supportable |
| MedNote "zero integration" (offer) | True on 9.2 | Vendor | Two regions on 7.4; ≈ ₪420,000, 4 months | Contradicted in part |
| Rishma "2.1% omissions" (slide 3) | 1,200 consented primary-care visits, four languages incl. Arabic, real rooms, independent university hospital, v3.2 | Independent | Close; Hebrew not in the evaluation; version | Worth testing further |
| Rishma "40–70 min a day" (slide 5) | Time-and-motion sub-study with a comparison group | Independent | Different health system | Worth testing (pilot) |

**Hop trace (ScribeWave 98%):** board minute → deck slide 4 → footnote "internal benchmark" → no report
provided by MedLink when asked (9 December). Dead end at the vendor.

**Counterparty:** Kol Refua: 30 people, 18 months of funding, no escrow (hedge: exit clause, export tested,
or exclude). MedNote: incumbent leverage (year two open; Notara renewal +9% from July 2027).

## Proof-of-concept protocol (signed by Igor and Wasim, 3 December, before any result)

| Measure | Definition | Threshold |
|---|---|---|
| Output in every language | A usable note for each recording; word error rate on the transcript | Notes in all three; WER ≤ 15% in each |
| Omissions | Facts from the script's list missing or wrong in the note, per 100 notes | ≤ 3 overall and ≤ 5 in each language |
| Invented findings | Findings not said in the visit, per 100 notes | ≤ 1 |
| Correction time | Reviewer's timed minutes to a signable note | ≤ 4.0 (today's mean note time is 4.8) |
| Must-have terms | RFP answers | All accepted |

Decision rule: a vendor that misses any threshold is not taken to the clinician pilot. The PoC is small
(180 notes a vendor): read rates with their intervals, and treat a pass as "fit to pilot", not "safe".

## Results (31 December; `poc/review-sheet.csv`, `poc_score.py`)

| Vendor | WER he / ar / ru | Omissions per 100 (95% CI) | Per language (he / ar / ru) | Invented per 100 | Min to correct | Must-haves refused | Verdict |
|---|---|---|---|---|---|---|---|
| ScribeWave | 14 / **27** / 12 | **7.2** (4.3–12.0) | **6.7** / **11.7** / 3.3 | **2.8** | **4.5** | retention, location, model change | Fails |
| Kol Refua | 8 / **no output** / **21** | **5.0** (2.3–10.5) | 3.3 / — / **6.7** | 0.8 | 3.5 | location | Fails |
| MedNote for Notara | **19 / 31 / 26** | **11.1** (7.3–16.5) | **10.0 / 13.3 / 10.0** | **2.2** | **6.0** | no training, model change | Fails |
| Rishma Health | 9 / 11 / 10 | 2.2 (0.9–5.6) | 1.7 / 3.3 / 1.7 | 0.6 | 3.0 | none | Passes |

Bold = misses a threshold. Three things the table alone does not say:

1. **Relatives.** With a relative in the room, omissions per 100 notes: Rishma 3.7, Kol Refua 8.3,
   ScribeWave 9.3, MedNote 16.7; alone 0 / 0 / 4.2 / 2.8. The demos had no relatives.
2. **Flags.** Three of Rishma's four omissions sat inside a passage it had marked unsure; the doctor would
   have been asked to confirm. No other vendor marks uncertainty.
3. **Runs differ.** Rishma got P-38 right on run 1 and missed the stopped medicine on run 2 (flagged). The
   same recording can give different notes: the pilot audits real notes, not a demo.

## Note to the CEO and CIO, Thursday 31 December 2026 (exit point 2)

"Don't sign today. The vendor that led the demos failed Galil's test in Arabic and on relatives, and its
quoted plan lets it train on our recordings and keep them 90 days in the EU or the US. Rishma, which demoed
worst, is the only vendor that passed every threshold and accepts every must-have term. MedLink has agreed in
writing to hold its price until 31 March. Counsel will send Fund A the approval request as soon as the
steering group names a vendor on 19 January."
