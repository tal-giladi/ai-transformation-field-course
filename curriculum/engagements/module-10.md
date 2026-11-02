# Galil Health — writer's notes for module 10 (never imported)

The third Stage 2 engagement. The learner is an **outside consultant to the CIO** of a regional clinic
network that wants "an ambient scribe for every doctor". The hard part (10.4) is vendor selection: an
RFP, demos against evidence, clinical safety, privacy of health data and clinician adoption. 10.5 is a
decision, not a build: vendor scoring, contract terms and a clinician pilot plan. The interactive
practice is the `vendor-rfp` simulation, preset `galil`; every vendor, claim, demo condition, proof-of-
concept (PoC) result, term answer, price and the expert pick below match that preset
(`simulations/vendor-rfp/presets.js`). The data room is built by `labs/module-10/data-room/generate.py`
(seed 20261115); it also writes `labs/module-10/poc/`. Ground truth that learners never see is only in
this file.

## The organization

- **Galil Health** (גליל בריאות), a public-benefit company (חל"צ) founded 1998. **14 community clinics**
  in **5 regions** of the north: 10 primary-care clinics and 4 specialist centres (child development
  and paediatrics, women's health, diabetes and endocrinology, cardiology and internal medicine). It
  serves about 112,000 registered patients under service agreements with two health funds (names
  redacted in the copies the consultant gets: "Fund A", "Fund B"). Revenue ₪318M (2025). 540 staff.
- **Clinicians: about 120** (preset): 78 doctors and 42 nurses. 9 doctor vacancies; locum spend
  ₪2.1M in 2025.
- **Patients' languages** (appointment system, preferred language): roughly a third each Hebrew,
  Arabic and Russian (30 / 38 / 28%, other 3%: English, Amharic, Tigrinya), often with a relative in
  the room. **Notara** (fictional) is the clinic record system. **Two of five regions** (Upper Galilee,
  Kinneret) run Notara 7.4; the other three run 9.2.
- Regions and clinics (ids used in the data):
  Western Galilee: GH-AKK Akko (ar/he), GH-NAH Nahariya (he/ru), GH-NAHP Nahariya Child Development &
  Paediatrics (specialist). Karmiel–Misgav: GH-KRM Karmiel (ru/he), GH-MAJ Majd al-Krum (ar), GH-KRMW
  Karmiel Women's Health (specialist). Nazareth: GH-NAZ Nazareth (ar), GH-NOF Nof HaGalil (ru/he/ar),
  GH-NAZD Nazareth Diabetes & Endocrine Centre (specialist). Upper Galilee (Notara 7.4): GH-SAF Safed
  (he/ru), GH-HAT Hatzor HaGlilit (he/ru). Kinneret (Notara 7.4): GH-TIB Tiberias (he/ru), GH-MGR Maghar
  (ar), GH-TIBC Tiberias Cardiology & Internal Medicine (specialist).

## Who the learner is

Igor Shapiro (CIO) hired the learner as an independent consultant: 10 weeks, **Sunday 15 November
2026 – Thursday 21 January 2027**, fixed fee in three exitable phases: ₪62,000 Diagnose (15 Nov – 3
Dec; exit at the 3 December readout); ₪114,000 Select (6 Dec – 14 Jan: RFP, PoC, scoring, contract
terms, pilot plan; exit after the PoC results, Thursday 31 December); ₪22,000 Readout and handover
(17–21 Jan). ₪198,000 + VAT from the IT budget. PoC budget up to ₪75,000 (actors and a studio day
₪28,000; clinician reviewers ₪42,000; other ₪5,000), approved by the CIO; anything above to the CEO
(approval up to ₪300,000). Steering group: Shlomit Avraham (CEO, chair), Igor (sponsor), Dr. Wasim
Haddad (CMO), Eyal Dahan (CFO), Adv. Hagit Peretz (legal counsel and DPO), Suha Nasser (Head of
Nursing).

What changes for this entry role (10.1, pointing to 01.1 and 08.1): the sponsor is the CIO, not the
clinical owner; the clinical decision belongs to the CMO and the privacy decision to the DPO and
counsel; a consultant who "selects a vendor" has become a party, so the consultant designs and runs
the evidence and the organization selects. A medical setting adds the advisory boundary to clinical
safety (the CMO) and to the Ministry of Health and medical-device questions (counsel).

## Stated ask vs hidden truth

- **Stated ask (CEO, board 21 October 2026):** "An ambient scribe for every doctor by Q2 2027". The
  board approved up to ₪1.6M for 2027 "subject to the CEO's selection". The CEO prefers ScribeWave after
  its demo and holds a quote for 120 seats with a 12% discount if signed by 31 December 2026.
- **Hidden truth.**
  1. **The demo ranking is upside down.** The steering group's demo-day scorecards put ScribeWave and
     Kol Refua first (3.62 weighted) and Rishma last (2.92). On evidence the order reverses: Rishma
     3.92, ScribeWave 2.31, MedNote 2.31, Kol Refua 2.00. Every headline number except Rishma's was
     measured under conditions that do not match Galil (English, scripted, studio microphone, one
     speaker, US specialties; dictation, not conversation; self-measured in a partner clinic).
  2. **The burden sits in the languages, and the KPI hides it.** Notara's "visit language" field
     defaults to Hebrew, so the KPI report shows 78% Hebrew visits. The appointment system's preferred
     language shows a third each. Visits where the doctor does not speak the patient's language take
     longer to document and produce more after-hours work, and nurses interpret in many of them. A
     scribe that works only in Hebrew helps the doctors who need it least.
  3. **The deadline was never real.** Galil cannot sign by 31 December without breaching its own contracts: Fund A's
     service agreement requires its prior written approval (45 days) for any new processor of members'
     medical information and processing in Israel unless approved; Galil's own cloud process (MOH
     circular 2/2021, a cloud committee) exists on paper only; the patient privacy notice says data is
     kept in Israel. ScribeWave's reseller will move the discount to 31 March if asked.
  4. **AI scribing already happens, unsanctioned.** About a dozen doctors record visits on consumer
     apps on their own phones and paste summaries into Notara (survey free text, proxy and guest-Wi-Fi
     log, one 2026 incident). Doing nothing is not the zero-risk option.
  5. **Galil tried before.** A 2025 MedNote dictation trial (9 doctors, 2 clinics) faded to 2 users by
     week 8 and produced two documentation near misses; the CIO who ran it does not mention it.
  6. **The money is retention, not minutes.** Freed documentation time is capacity, not cash. The CFO's
     real cost is 9 doctor vacancies and ₪2.1M of locums; exit interviews cite after-hours notes.
- **The honest answer:** do not sign by 31 December; issue a proper RFP with measurement conditions and
  must-have terms; run a PoC on 90 synthetic visits in Galil's three languages; choose on evidence
  (Rishma, Israel hosting, all must-haves accepted), subject to the DPO and counsel, Fund A's approval
  and the cloud committee; a six-week clinician pilot in two clinics (Nazareth, Arabic; Karmiel,
  Russian/Hebrew) with a stop rule; consent wording by the CMO and the DPO; doctors first, nurses as a
  separate evaluated phase; give the shadow users a sanctioned path and a date.

## Planted findings (each discoverable, never stated)

| # | Finding | Where |
|---|---|---|
| 1 | Demo statistics measured under non-matching conditions | `vendors/*-deck.md`, `vendors/*-evaluation*.md`, demo notes; persona Yoni |
| 2 | Demo-day ranking reverses on evidence | `vendors/demo-day-scorecards.csv` vs PoC and documents |
| 3 | PoC changes the picture | `../poc/review-sheet.csv` |
| 4 | Language field defaults to Hebrew; real mix a third each | `notara/visits-sample.csv` (`visit_language` vs `patient_pref_language`), `company/kpi-report-2026-q3.md` |
| 5 | Missing baseline: documentation time never measured; "2 hours" is self-report and vendor | `company/kpi-report-2026-q3.md`, `people/clinician-survey-2026-10.csv`, `notara/visits-sample.csv` (`note_active_sec`, `after_hours_sec`) |
| 6 | Burden concentrates in language-mismatch visits; nurses interpret | `notara/visits-sample.csv` joined to `people/clinicians.csv`; persona Suha |
| 7 | Shadow AI: consumer recording apps, chatbots on workstations | `people/clinician-survey-2026-10.csv` free text, `it/proxy-ai-summary-2026-10.csv`, `quality/patient-safety-incidents.csv` (IN-2026-052); persona Elena |
| 8 | The 2025 dictation trial that faded; two near misses | `notara/mednote-dictation-trial-2025.csv`, `quality/patient-safety-incidents.csv` (IN-2025-031, IN-2025-044); personas Igor, Wasim |
| 9 | Fund A prior approval (45 days) and Israel processing | `legal/health-fund-agreements-extract.md`; persona Hagit |
| 10 | Cloud committee on paper only (circular 2/2021) | `it/cloud-committee-minutes-2022.md`; persona Hagit |
| 11 | Privacy notice says data stays in Israel; nothing on recording | `legal/patient-privacy-notice-2023.md` |
| 12 | ScribeWave quote is the standard plan (training on de-identified data); enterprise +18%; deadline movable | `vendors/scribewave-quote-2026-11.md`, `vendors/scribewave-dpa-extract.md`; persona Yoni |
| 13 | Kol Refua's "never leaves Israel" fails in the sub-processor annex | `vendors/kolrefua-dpa-extract.md` |
| 14 | MedNote: dictation numbers, preview, two regions on Notara 7.4, product-improvement clause, year two open | `vendors/mednote-*.md`, `legal/notara-master-agreement-extract.md`, `company/clinics.csv` |
| 15 | Retention, not minutes: vacancies, locums, exit interviews | `company/finance-summary.md`, `company/kpi-report-2026-q3.md`; persona Eyal |
| 16 | Staff-committee consultation before recording technology | `legal/staff-committee-agreement-extract.md`; persona Suha |

## The cast (persona pack, `labs/module-10/personas/`)

| Persona | Role | Type | Hidden / unlock |
|---|---|---|---|
| Igor Shapiro | CIO, sponsor | sponsor | Ran the 2025 dictation trial that faded (ask "tried before?"); signed the Notara master agreement with the product-improvement clause (ask what the Notara contract says about data); privately prefers MedNote for integration (ask what he'd pick alone) |
| Shlomit Avraham | CEO | owner of the ask | Told Fund A's regional director recordings would stay in Israel (ask what the funds know); quote is the standard plan, DPA unread (ask which plan); real worry is vacancies (ask what she must solve by summer) |
| Dr. Wasim Haddad | Chief Medical Officer, family doctor in Nazareth | clinician lead, sceptic | Signed off two near misses in the 2025 trial (ask about safety incidents); tolerates phone recording (non-attribution + how doctors cope); will lead PoC scripts (ask for help) |
| Adv. Hagit Peretz | Legal counsel and DPO | counsel / DPO | Fund A clauses (ask what other contracts govern patient data); cloud committee dormant (ask how cloud approvals work in practice); privacy notice says Israel (ask what patients were told); open: is audio part of the record? |
| Dr. Elena Volkova | Family doctor, Karmiel | frontline, secret enthusiast | Records visits on a consumer app for 8 months; ~10 colleagues do; the allergy incident (non-attribution + "show me a normal day's notes") |
| Suha Nasser | Head of Nursing | middle manager / nurses | Nurses interpret in mismatch visits (ask what happens when doctor and patient don't share a language); staff-committee consultation clause (ask about the committee / recordings and complaints) |
| Eyal Dahan | CFO | finance, sceptic | Locums ₪2.1M, 9 vacancies, exit interviews (ask what costs the burden drives); Notara renewal +9% letter (ask about Notara costs) |
| Yoni Mizrahi | Account executive, MedLink Systems (ScribeWave's Israeli reseller) | vendor AE | The 98% conditions; Hebrew beta on read speech; Arabic on Gulf dialects; standard plan trains on de-identified data; 90-day audio; EU/US; deadline movable to 31 March (ask exact conditions; ask which plan; ask whether the date can move) |
| Fatma Abu-Ras | Patient, 64, Majd al-Krum | person affected | Would agree to recording if told in Arabic who hears it and that it is deleted; would refuse "abroad" or to the fund; daughter's report of a stopped medicine missing from a note (let her tell a visit in order; ask what would make it OK) |

Transcripts leave hidden: Igor's MedNote preference; Shlomit's promise to Fund A; Wasim's tolerance of
phone recording; Hagit's privacy-notice point; Elena's allergy incident; Suha's committee clause;
Eyal's Notara uplift; Yoni's movable deadline; Fatma's "abroad" line.

## Timeline

- Data: visits 1 Sep – 31 Oct 2026 (8% random sample); survey 4–22 Oct 2026; proxy log weeks of 4 Oct –
  1 Nov 2026; incidents Jan 2025 – Oct 2026; dictation trial weeks 2 Mar – 21 May 2025.
- Wed 21 Oct board; demos Mon 26 Oct (ScribeWave), Wed 28 Oct (Kol Refua), Mon 2 Nov (MedNote), Thu 5
  Nov (Rishma); Mon 9 Nov Igor calls; Thu 12 Nov proposal signed; Sun 15 Nov start (10.1).
- 16–26 Nov discovery (10.2; Fatma Tue 24 Nov with consent arranged by the CMO); Thu 3 Dec phase-1
  readout (10.3, exit 1).
- Sun 6 Dec RFP to four vendors, answers due Sun 20 Dec; PoC scripts 25 Nov – 3 Dec; recording 8–10 Dec;
  each vendor runs each recording twice 13–20 Dec; six clinician reviewers 21–30 Dec; Thu 31 Dec PoC
  results and the "do not sign today" note (10.4, exit 2). ScribeWave's discount moved to 31 March
  2027 when Galil asked.
- 3–14 Jan 2027 scoring, contract terms, pilot plan (10.5). Tue 19 Jan steering committee (10.6); Thu
  21 Jan handover to Igor (owner) and Wasim (clinical owner).
- Twelve months later: January 2028.

## PoC design (matches the preset)

90 synthetic visits (30 Hebrew, 30 Arabic, 30 Russian), written by the CMO's team from real-shaped
scenarios, recorded by actors in clinic rooms with relatives and room noise. Each vendor processed each
recording twice (180 notes; Kol Refua produced no Arabic output, so 120). Six clinicians, two per
language, reviewed every note against the script's fact list. Counts are in `poc/review-sheet.csv`:

| Vendor | WER he / ar / ru % | Omitted relevant facts (count / notes; per 100) | Invented (per 100) | Minutes to correct |
|---|---|---|---|---|
| ScribeWave | 14 / 27 / 12 | 13 / 180; 7.2 | 5; 2.8 | 4.5 (he 3.9, ar 5.8, ru 3.8) |
| Kol Refua | 8 / — / 21 | 6 / 120; 5.0 | 1; 0.8 | 3.5 (he 2.9, ru 4.1) |
| MedNote | 19 / 31 / 26 | 20 / 180; 11.1 | 4; 2.2 | 6.0 |
| Rishma | 9 / 11 / 10 | 4 / 180; 2.2 (3 flagged unsure) | 1; 0.6 | 3.0 |

The preset rounds these to 7 / 5 / 11 / 2 omissions and 3 / 1 / 2 / 0.5 invented per 100 notes.

## Scores (preset; weights agreed before the demos and printed on the demo-day scorecards; weights evidence 2, safety 3, privacy 3, languages 2, integration 1, contract 2)

Demo impression: ScribeWave 3.62, Kol Refua 3.62, MedNote 3.54, Rishma 2.92. Evidence: Rishma 3.92,
ScribeWave 2.31, MedNote 2.31, Kol Refua 2.00. Must-haves: Rishma accepts all seven; ScribeWave refuses
retention, location, model change; Kol Refua refuses location; MedNote refuses no-training and model
change.

## Money

- ScribeWave quote: 120 seats × ₪1,150 a month standard plan = ₪1,656,000 a year; 12% off if signed by
  31 Dec = ₪1,457,280. Enterprise (no training) +18% = ₪1,357 a seat a month.
- Rishma: ₪1,300 a clinician a month, Israel hosting +8% = ₪1,404; 78 doctors = ₪1,314,144 a year;
  Notara interface project quoted by the Notara vendor ₪160,000; pilot (12 doctors × 6 weeks) ₪25,272
  licences plus clinician time (training 18 h, weekly audit 48 h at ₪330) ≈ ₪22,000; total ≈ ₪47,000.
- Doctor cost ₪52,000 a month fully loaded per FTE (≈ ₪330 an hour at 157 h). Board line for 2027 ₪1.6M.

## The futures (10.6 debrief; from the preset's "later" texts)

1. **Sign ScribeWave by 31 December (the CEO's path).** All 120 seats. Hebrew notes fine; Arabic-speaking
   doctors stopped using it in month three; the data-location question is still open with the DPO
   (and Fund A's approval request was filed after signature; Fund A asked Galil to suspend use for its members pending review); measured saving about 25 minutes a day,
   not two hours.
2. **MedNote, "free in year one" (the comfortable path).** Smooth where Notara was current; the two
   7.4 regions waited for the upgrade; doctors spent longer fixing conversation notes than writing
   their own; use fell to a few enthusiasts; year-two pricing arrived at ₪900 a clinician a month.
3. **Evidence, then a pilot (the expert path).** Rishma with Israel hosting, after counsel and the DPO,
   Fund A's approval and the cloud committee; six-week pilot in Nazareth and Karmiel; region-by-region
   rollout; Arabic-speaking clinics adopted fastest; integration took four months, not three; measured
   note time fell by about 35 minutes a day. The shadow apps stopped once doctors had a sanctioned tool; two of the nine vacancies were filled by the autumn (one doctor cited the scribe).

What decided which future happened: whether anyone asked how the demo numbers were measured before the
discount deadline, and whether the deadline was tested against the funds' contracts.

## Where each finding is planted (actual numbers)

Computed from the generated files (seed 20261115) with `labs/module-10/discovery.py` and `poc_score.py`;
reproducible in a spreadsheet with filters, pivots and lookups. Paths relative to
`labs/module-10/data-room/`.

**Volumes.** `notara/visits-sample.csv` 4,087 visits (8% random sample of doctor visits, 1 Sep – 31 Oct
2026); `notara/doctor-days.csv` 2,413 doctor-days with full visit counts (Sep 24,610, Oct 27,315 visits);
`people/clinicians.csv` 120 (78 doctors: 30 speak Arabic, 24 Russian, 38 English; 42 nurses: 20 Arabic, 12
Russian); `people/clinician-survey-2026-10.csv` 84 responses (60 of 78 doctors, 24 of 42 nurses);
`vendors/demo-day-scorecards.csv` 216 rows (9 raters × 4 vendors × 6 criteria); `poc/review-sheet.csv` 720
rows (660 scored, 60 Kol Refua Arabic "no_output").

4. **Language field.** Notara `visit_language`: he 77.1%, ar 12.8%, ru 9.0%, other 1.0% (the KPI table).
   `patient_pref_language`: ar 38.2%, he 30.1%, ru 28.4%, en 1.7%, am 0.9%, ti 0.7%. 1,921 of 2,857
   non-Hebrew visits (67%) are recorded as Hebrew. `relative_present` blank in 39.5%.
5. **Missing baseline.** KPI: "Documentation time per visit: not measured"; footnote cites vendors' "about
   2 hours". Measured: note window time median 4.22 min per visit (mean 4.83); 18.6% of visits have
   after-hours work; doctor-day documentation (visits × the doctor's mean note + after-hours time) median
   **112 min** (p75 136; mean 115), after hours median 10 min (mean 12). Survey (doctors, self-report):
   median 120 min a day; 2 evenings a week finishing notes. ScribeWave's "saves 2 hours a day" exceeds all
   measured documentation time. The KPI the network tracks is green: 98.1% of notes signed within 24 h.
6. **Mismatch.** Doctor does not speak the patient's preferred language in 1,138 of 4,087 visits
   (27.8%); interpreter there: relative 47.6%, nurse 27.9%, none 9.3%, blank 9.2%, phone 5.9%. Note time
   median 5.52 vs 3.85 min (+43%); after-hours share 33% vs 13%. Same-language visits: he 3.58, ar 3.97,
   ru 4.28 min (writing a Hebrew note after an Arabic or Russian visit). Mismatch by clinic: KRMW 57%,
   NAHP 51%, NOF 45%, TIB 42%, TIBC 38%, NAH 37%, AKK 33%, KRM 31%, HAT 31%, SAF 23%, NAZD 13%, NAZ / MAJ /
   MGR 1%. Nurses interpret in 7.8% of all visits; nurse survey: median 42 interpreting minutes a day.
7. **Shadow AI.** Survey `tools_used_for_notes`: notara_templates 43, other 22, none 18, dictation 1; 11
   comments mention a phone, an app or an AI tool. Firewall: consumer speech-to-text on guest Wi-Fi in 5
   clinics, upload over four weeks KRM 2,428 MB, NOF 1,748, SAF 1,170, NAH 1,032, AKK 507; ChatGPT on the
   clinic LAN in 9 clinics. Incident IN-2026-052 (Karmiel, 17 Sep 2026): allergy missing from a summary
   "from the phone".
8. **Trial.** Doctors dictating ≥ 10% of visits: weeks 1–4: 9; week 5: 6; week 6: 5; weeks 7–12: 2.
   Incidents IN-2025-031 (metformin / metoprolol) and IN-2025-044 (Eliquis said by the daughter).
2. **Demo vs evidence.** Demo-day weighted means: ScribeWave 3.62, Kol Refua 3.62, MedNote 3.54, Rishma
   2.92 (criterion means rounded; privacy 4.89 → 5 for Kol Refua, integration 4.89 → 5 for MedNote). Demo
   languages: ScribeWave en, Kol Refua he, MedNote he dictation, Rishma ar+he recorded.
3. **PoC** (`poc_score.py`): WER and minutes as in the PoC table above; omissions per 100 notes with
   Wilson 95% intervals: Rishma 2.2 (0.9–5.6), Kol Refua 5.0 (2.3–10.5), ScribeWave 7.2 (4.3–12.0),
   MedNote 11.1 (7.3–16.5); invented: 0.6 / 0.8 / 2.8 / 2.2. With a relative in the room: Rishma 3.7,
   Kol Refua 8.3, ScribeWave 9.3, MedNote 16.7 per 100 notes; alone: 0 / 0 / 4.2 / 2.8. Rishma's
   omission on P-38 run 2 (run 1 was correct) sits inside a passage it marked unsure: run-to-run variation.
   Must-haves refused: ScribeWave retention, location, modelChange; Kol Refua location; MedNote noTraining,
   modelChange; Rishma none.
