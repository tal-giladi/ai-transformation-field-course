# 05 · Vendor scoring, contract terms and the clinician pilot plan — Galil Health

Decision paper for the steering committee of Tuesday 19 January 2027. Written 3–14 January.

## Recommendation

Name **Rishma Health, hosted in Israel,** as Galil's preferred vendor for doctors' visit documentation,
**subject to** counsel's and the DPO's review of the contract, Fund A's written approval, the cloud
committee's approval and the staff committee's consultation; run a **six-week clinician pilot in Nazareth and
Karmiel** from 14 March 2027 with the stop rules below; decide on rollout at a gate on 6 May 2027.

## Scoring: the demo against the evidence

Weights locked 3 December: evidence 2, safety 3, privacy 3, languages 2, integration 1, contract 2 (total 13).
Demo scores are the steering group's demo-day means; evidence scores are mine, from the documents, the RFP
answers and the PoC, each with its reason.

| Criterion (weight) | ScribeWave demo → evidence | Kol Refua | MedNote for Notara | Rishma Health |
|---|---|---|---|---|
| Evidence (2) | 4 → **2** internal scripted English; self-reported survey | 3 → **2** self-measured, 40 visits, shareholder clinic | 3 → **2** dictation figures; ambient "preview" | 3 → **4** independent, conversations, Arabic included; Israeli references |
| Safety (3) | 4 → **3** 7.2 omissions per 100; safety contact; no unsure-marking | 3 → **2** no safety case; no unsure-marking | 3 → **2** 11.1 omissions; correction slower than writing | 3 → **4** safety case and hazard log; 2.2 omissions, 3 of 4 flagged |
| Privacy (3) | 3 → **2** Standard plan trains on data; 90-day audio; EU/US | 5 → **2** US speech API in the annex | 4 → **3** Israel, but "product improvement" clause stays | 3 → **4** every data term accepted; Israel at +8% |
| Languages (2) | 4 → **2** Arabic WER 27% | 4 → **2** no Arabic; Russian 21% | 3 → **1** worst in all three | 3 → **4** 9 / 11 / 10% |
| Integration (1) | 4 → **3** FHIR connector, Notara interface project | 3 → **2** no Notara experience | 5 → **5** inside Notara (two regions need 7.4 → 9.2) | 2 → **3** interface project ≈ 3 months |
| Contract (2) | 3 → **2** refuses model-change notice; annual list prices | 3 → **2** 18 months' funding, no escrow | 4 → **2** year two open; refuses model notice | 3 → **4** exit, model change, audit; no price lock |
| **Weighted** | 3.62 → **2.31** | 3.62 → **2.00** | 3.54 → **2.31** | 2.92 → **3.92** |
| Must-haves refused | retention, location, model change | location | no training, model change | none |

The demo order (ScribeWave = Kol Refua > MedNote > Rishma) reverses on evidence. Even with Rishma's
integration score at 1, it stays first (3.77); no weight change a reasonable steering group would make moves
another vendor ahead, and every other vendor refuses at least one must-have anyway.

## Three-year cost, 78 doctors (assumptions stated)

| | Year 1 | Years 1–3 | Notes |
|---|---|---|---|
| Rishma, Israel hosting (₪1,300 + 8% = ₪1,404 a doctor a month) | ₪1,314,144 + integration ₪160,000 | ≈ ₪4.22M | Indexation assumed 3% a year (to be capped in the contract); integration estimate is Notara's |
| ScribeWave Enterprise (needed for no training; ₪1,357) | ₪1,270,152 | ≈ ₪4.09M incl. integration | Still refuses retention, location, model change |
| MedNote for Notara | ₪0 in 2027 | Unknown | Year two "to be agreed"; Notara renewal +9% from July 2027; 7.4 regions need ₪420,000 upgrade |
| Kol Refua (₪600, three-year lock) | ₪561,600 + integration | ≈ ₪1.84M | No Arabic; audio to a US API |

2027 cash for the recommended path (pilot from March, regions from the summer): about ₪0.9–1.1M including
integration, inside the board's ₪1.6M line. Value: capacity of about 600 doctor-hours a month at 30 minutes a
doctor-day (assumed); cash only through retention, about four to five posts a year to pay for itself (assumed;
the CFO's test). The pilot measures direction, not the retention effect.

## Contract terms (Galil negotiates; I prepared)

Must-haves, all accepted in Rishma's RFP answer: T1–T7 as in the RFP. Then, to negotiate:

1. **Retention by instruction.** 30 days by default, but Galil may instruct another period once counsel
   answers whether audio is part of the medical record.
2. **Incident reporting within 12 hours** to Galil (Galil reports to Fund A within 24 under Appendix D.7).
3. **Intended purpose.** Transcription and note drafting for clinician review only; no feature that suggests
   diagnoses, treatment or codes without Galil's written approval and a regulatory review first.
4. **Pilot exit.** Terminate after the pilot without penalty if a stop rule is triggered or the gate says no.
5. **No minimum seats.** 12 seats in the pilot, then per region.
6. **Indexation capped** (CPI, at most 4% a year); Israel-hosting surcharge fixed for three years.
7. **Integration.** A three-party plan with Notara Systems; milestones; fees held until the interface works on
   both Notara 9.2 and 7.4.
8. **Change of control.** Exit right and data return if Rishma is acquired.

## Steps before signing (owners and dates)

| Step | Owner | By |
|---|---|---|
| Contract, DPA and sub-processor list reviewed; open question on audio and the record to external counsel | Hagit | 3 Feb |
| Fund A approval requested (45 days); Fund B notified (30 days) | Hagit | 20 Jan → by 6 Mar |
| Cloud committee reconvened; policy adopted; risk assessment of this use; if rated high risk, the Ministry's sector committee's opinion first (counsel to check timing) | Igor, Hagit | 27 Jan |
| Report the new cloud use to the Ministry of Health's information-security officer within 30 days of signing (circular 2/2021) | Igor | after signature |
| Vendor's intended purpose and regulatory status in writing; counsel decides whether to consult the Ministry's medical devices division (AMAR) | Hagit | 3 Feb |
| Patient privacy notice updated (recordings, location, deletion) in four languages | Hagit, Wasim | 28 Feb |
| Consent wording agreed (below) | Wasim, Hagit | 28 Feb |
| Staff committee informed in writing; consultation meeting (nurses present in recorded visits are recorded) | Suha, HR | 10 Feb (≥ 30 days before 14 Mar) |
| Sign the pilot-phase contract | Shlomit | after Fund A approves |

## Clinician pilot plan

**Where and who.** Nazareth (Arabic; Notara 9.2) and Karmiel (Russian and Hebrew; 9.2; mismatch 31%; the
largest consumer-app uploads). Six volunteer doctors in each, twelve in all. Comparison: doctors in Akko and
Tiberias (similar language mix), read from the Notara audit log with no extra work for them. Nurses' own
visits are not in phase 1.

**When.** Set-up and training 7–11 March; pilot Sunday 14 March – Tuesday 20 April 2027 (six weeks, ending
before Passover); gate Thursday 6 May. The note is copied from Rishma into Notara during the pilot; the
integration project starts only after the gate.

**What is measured** (baseline: the same doctors, 1 Sep – 31 Oct 2026, from the audit log):

| Measure | How | Gate threshold |
|---|---|---|
| Documentation minutes per doctor-day (in hours + after hours) | Notara audit log, vs baseline and comparison | ≥ 20 minutes less than the comparison |
| Omissions and invented findings | CMO's reviewers audit 10 scribe notes per doctor per week against the audio (kept 30 days) | Omissions ≤ 3 per 100 overall, ≤ 5 per language; invented ≤ 1 |
| Use | Share of eligible visits with the scribe, weeks 4–6 | ≥ 60% |
| Patients | Opt-out rate; complaints | Opt-out ≤ 15%; no complaint about recording upheld |
| Doctors | Weekly two-question pulse (evenings finishing notes; would you keep it?) | Direction, not a threshold |

**Stop rules (written by Wasim).** Any harm attributable to a scribe note: stop at once and review. Audited
omissions above 5 per 100 in any language for two consecutive weeks: stop that language. A model change
without notice: stop. A data incident: stop, and Galil notifies Fund A within 24 hours. Opt-out above 30% in a
clinic: pause and review the consent conversation.

**Consent (draft for Wasim and Hagit; spoken by the doctor, poster in four languages).** "I'd like to use a
tool that listens to our conversation so I can write your notes correctly and look at you instead of the
screen. Only I see the draft, and I check it before it goes into your file. The recording is kept in Israel,
is not sent to your health fund or anyone else, and is deleted within 30 days. You can say no; your visit will
be exactly the same." (Shaped by a patient's conditions in discovery: explained by the doctor, in her
language, who hears it, deleted, and free to refuse.)

**Shadow recording.** From 1 February: an instruction to stop recording visits on personal devices or public
AI tools, with no discipline for past use (aligned with the Ministry of Health's line on public generative-AI
tools, as counsel reads it); pilot doctors switch on 14 March; everyone else is told the date their region
gets the approved tool.

**Budget.** Licences 12 × ₪1,404 × 1.5 months = ₪25,272; clinician time (training 18 h, audit reviews 48 h at
₪330) ≈ ₪22,000; total ≈ ₪47,000 (CEO approval).
