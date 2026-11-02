---
id: "10.4"
module: 10
minutes: 24
practice_minutes: 210
prerequisites: ["10.3", "04.3", "04.4", "04.6", "04.8"]
objectives:
  - "Write an RFP that fixes criteria and weights, states the organization's conditions, asks how every claim was measured, makes a proof of concept part of the bid and lists must-have terms."
  - "Read back each vendor's headline claims under their measurement conditions and say which, if any, are evidence for this organization."
  - "Prepare the privacy, health-regulation and medical-device questions for counsel and the DPO, Israel first, without answering them yourself."
  - "Design a proof of concept on synthetic visits with thresholds fixed before results, and read its results with their uncertainty."
volatility: implementation
sources:
  - title: "Privacy Protection Law, 5741-1981, as amended (Hebrew Wikisource): section 3 'information of special sensitivity' incl. health information; section 17B1 privacy protection officer"
    url: https://he.wikisource.org/wiki/חוק_הגנת_הפרטיות
  - title: "IAPP, Israel marks a new era in privacy law: Amendment 13 (in force 14 August 2025; sanctions higher for sensitive data)"
    url: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
  - title: "Privacy Protection (Data Security) Regulations, 5777-2017 (Hebrew Wikisource): security levels, First and Second Schedules, regulation 11(d) serious incidents, regulation 15 outsourcing"
    url: https://he.wikisource.org/wiki/תקנות_הגנת_הפרטיות_(אבטחת_מידע)
  - title: "Patient's Rights Law, 5756-1996 (Hebrew Wikisource): sections 2, 17, 19, 20"
    url: https://he.wikisource.org/wiki/חוק_זכויות_החולה
  - title: "Ministry of Health, director-general's circular 2/2021, 'Use of cloud computing in the health system' (21 February 2021)"
    url: https://www.gov.il/BlobFolder/policy/mk02-2021/he/files_circulars_mk_mk02_2021.pdf
  - title: "Mako, 5 March 2026: Ministry of Health emergency directive limiting generative-AI use in health organizations"
    url: https://www.mako.co.il/news-lifestyle/2026_q1/Article-1fc042e638dbc91027.htm
  - title: "Medical Equipment Law, 5772-2012 (Hebrew Wikisource): section 1 definition, section 2 registration before manufacture or marketing"
    url: https://he.wikisource.org/wiki/חוק_ציוד_רפואי
  - title: "MHRA, Ambient voice technology-enabled products (guidance, 29 July 2026): intended purpose decides device status"
    url: https://www.gov.uk/government/publications/ambient-voice-technology-enabled-products/ambient-voice-technology-enabled-products
  - title: "Eavesdropping Law, 5739-1979 (Hebrew Wikisource): section 1 definition"
    url: https://he.wikisource.org/wiki/חוק_האזנת_סתר
last_verified: "2026-11-02"
---

# 10.4 · The hard part: choosing on evidence

Galil's whole engagement turns on one move: choosing a vendor on evidence from Galil's own conditions instead of on the demo that impressed the steering group. In this lesson you write the RFP, read back every vendor's headline claims under the conditions they were measured in, prepare the privacy, health-regulation and medical-device questions for counsel, and design and read a proof of concept on 90 synthetic visits in Hebrew, Arabic and Russian. At the end you have the RFP, four claim read-backs, a regulatory map for counsel, the proof-of-concept results and the note that tells the CEO not to sign on 31 December.

> [!WARNING]
> Patient recordings are health information. In this engagement, as in any real one, no real patient's audio or record goes to a vendor for a test: the proof of concept uses synthetic visits written from real-shaped scenarios and recorded by actors, under an NDA, and nothing moves before counsel and the DPO agree. Never upload real visits to a trial account "to see how it does".

## The situation

Friday 4 to Thursday 31 December 2026. On 3 December the steering group approved option B: an RFP to the four vendors, a proof of concept (PoC) on synthetic visits, results on 31 December, and a request to MedLink to hold its price. Shlomit agreed "as long as I have something real on the 31st".

This month you see three people. Adv. Hagit Peretz, counsel and DPO, whom you met in week 1 ([persona](../../labs/module-10/personas/hagit-counsel-dpo.md); [transcript](../../labs/module-10/personas/transcripts/hagit-counsel-dpo.md)), to agree the RFP's data terms. Dr. Wasim Haddad, whose team writes the PoC scripts ([persona](../../labs/module-10/personas/wasim-cmo.md)). And Yoni Mizrahi of MedLink, ScribeWave's reseller, who asked for a call on 9 December "to plan the rollout" ([persona](../../labs/module-10/personas/yoni-scribewave-ae.md); [transcript](../../labs/module-10/personas/transcripts/yoni-scribewave-ae.md)).

The field kit has the parts: [vendor and tool review](../module-04/lesson-03.md), the [DPIA](../module-04/lesson-04.md), the [regulatory map](../module-04/lesson-06.md) and [vendor and claim due diligence](../module-04/lesson-08.md). IBM's consulting certificate calls the core of it *due diligence on claims and vendors*; here you do it for four vendors at once, in a regulated setting, against a deadline the CEO cares about.

## What to do

### Step 1 — Lock the criteria and the weights, and say when they were set

Galil's steering group agreed six criteria and weights before the first demo and printed them on its demo-day scorecards: demo vs evidence ×2, clinical safety ×3, privacy and data ×3, Hebrew/Arabic/Russian ×2, integration ×1, contract and exit ×2. They are reasonable for a clinic network: safety and privacy weigh most; integration, though it is Igor's headache, weighs least because it can be solved with money and time.

Re-confirm them on 3 December, in writing, before any RFP answer or PoC result exists ([03.4](../module-03/lesson-04.md) calls this the criteria lock). Write one sentence beside them: *agreed before the demos on 26 October and not changed after them.* If anyone proposes a change now that the demos have been seen, record who and why: a weight moved after a demo is a vote for that demo. For each criterion add what a 5 and a 1 look like. And decide now that **the demo is not scored again**: the demo-day scores stay on file as what the demos suggested, and the evidence scores are made separately.

### Step 2 — Write the RFP

Use the [RFP for AI vendors](../../templates/rfp-for-ai-vendors.md) template. Igor's draft (`vendors/rfp-draft-v0.md`) asks for "accuracy %", "languages supported", "do you comply with Israeli privacy law? Please confirm in writing". Each of those questions invites the answer you already have. Replace them:

| Igor's draft asks | The RFP asks instead |
|---|---|
| "What is your accuracy (%)?" | For every number you want us to rely on: sample (real or scripted, n), what was measured, language and specialty mix, who measured it, when, which version |
| "Which languages do you support?" | Our conditions: Arabic 38%, Hebrew 30%, Russian 28%; Galilee dialects; relatives in many visits; notes written in Hebrew. Your evidence in conditions like these |
| "Do you integrate with Notara?" | Notara 9.2 in three regions and 7.4 in two: what works on each, through which interface, at what cost and time |
| "Do you comply with Israeli privacy law?" | Your answer to each must-have term (accept, refuse, propose), your DPA and full sub-processor list, and your product's intended purpose and regulatory status in writing |
| "Price for 120 users" | Price per clinician for three years; no minimum seats; Israel hosting priced separately |

Then three sections Igor's draft lacks:

- **The proof of concept as part of the bid.** 90 synthetic visits, 30 per language, delivered 13 December; each vendor processes each recording twice; Galil's clinicians review every note; results 31 December. A vendor that declines is not shortlisted.
- **Must-have terms**, each with a one-line reason. Galil's seven: no training or improvement on Galil's audio, transcripts or notes, de-identified included; audio deleted within 30 days of signing the note (Galil may instruct another period); storage and processing in Israel or where the DPO approves in writing; full sub-processor list, notice, right to object; notice before model changes and a re-run on Galil's test set; a named clinical safety officer and incident reporting within 12 hours (Galil must tell Fund A within 24); exit with data return, certified deletion and six months' transition. Nice to have: certification and audit rights; a three-year price lock.
- **Process rules.** One point of contact (Igor); no side meetings with the CEO or clinicians; answers become part of the contract.

### Step 3 — Read back every claim under its conditions

This is the "demo conditions" reveal. Use the [claim read-back](../../templates/claim-read-back.md) and [04.8](../module-04/lesson-08.md): each claim, its five measurement conditions, who chose them, the fit with Galil, a rating. The vendors' own documents carry most of the answers in their footnotes:

| Claim (where) | Conditions | Fit to Galil | Rating |
|---|---|---|---|
| ScribeWave "98% transcription accuracy" (deck slide 4) | 200 **scripted English** visits (orthopaedics, dermatology, urgent care), **studio microphone**, **one speaker at a time**, US accents; words in the transcript, not facts in the note | None of language, setting, speakers, specialty or measure | Not yet supportable |
| ScribeWave "saves 2 hours a day" (slide 5) | Survey of 60 early adopters at two US systems, self-reported, no comparison group | Larger than Galil's measured 112 minutes | Contradicted for Galil |
| ScribeWave "30+ languages incl. Hebrew, Arabic" (slide 6) | Hebrew a beta model tested on **read-aloud text**; Arabic tested on Modern Standard and **Gulf** Arabic | Galilee dialects, conversation, relatives | Not yet supportable |
| Kol Refua "96% in Hebrew" (slide 3) | 40 visits, its partner clinic (whose holding company is an investor), two doctors, self-measured | Hebrew only | Worth testing (Hebrew) |
| Kol Refua "your data never leaves Israel" (slide 5) | Its own DPA, Annex B: a **US speech-recognition API** | The audio goes to the US | Contradicted |
| Kol Refua "Arabic next quarter" | A roadmap slide | 38% of patients | Not yet supportable |
| MedNote "95% accurate" (release notes) | **Dictation**: one clinician speaking to the microphone; Notara's internal test; ambient mode is a "preview" | A conversation is a harder task | Not yet supportable |
| MedNote "zero integration effort" (offer) | True on Notara 9.2 | Two regions on 7.4 (≈ ₪420,000 and four months to upgrade) | Contradicted in part |
| Rishma "omits a relevant fact in 2.1% of notes" (slide 3) | **Independent** university-hospital evaluation, 1,200 consented primary-care **conversations** in four languages **including Arabic**, real rooms, every note reviewed by a clinician; version 3.2; Hebrew not included | Close to Galil's, except Hebrew and version | Worth testing further |

Look at the pattern. The three vendors who demoed best measured their numbers under conditions they chose and Galil does not have. The vendor that demoed worst is the only one whose number was measured independently, on conversations like Galil's. At no point do you need to say a vendor lied: the footnotes say it.

Then interview Yoni. What you need out of him: the conditions of each number in his words, what "supports Hebrew and Arabic" means, which plan the quote is for and what it lets ScribeWave do with recordings, and whether the 31 December date can move. Ask exact questions ("on what visits, in what language, with how many speakers, measured by whom?"); a vague "how accurate is it?" gets "98% in hundreds of hospitals". In the transcript the interviewer gets everything except the last point: they never ask whether the date can move. It can, to 31 March, if Galil asks in writing.

Add one sentence on counterparty risk per vendor: Kol Refua has 30 people and 18 months of funding with no escrow; MedNote's "free in year one" arrives as Notara announces a 9% increase from July 2027.

### Step 4 — Prepare the legal and regulatory questions for counsel

You do not decide any of this. You prepare the facts and the questions so Hagit and, where she wants it, external counsel can decide quickly. Israel first; each item with its source and owner, in the [regulatory map](../../templates/regulatory-map.md):

**Privacy of health information.** Under the Privacy Protection Law, 5741-1981 (חוק הגנת הפרטיות) as amended by Amendment 13 (in force 14 August 2025), health information is listed in the definition of "information of special sensitivity" (section 3). Amendment 13 also made appointing a privacy protection officer mandatory for some bodies, including those whose main activity involves large-scale processing of sensitive information (section 17B1); Galil appointed Hagit in August 2025. The Privacy Protection Authority's sanctions are higher where sensitive data is involved (IAPP's summary).

**Security of the databases.** The Privacy Protection (Data Security) Regulations, 5777-2017 (תקנות הגנת הפרטיות (אבטחת מידע)) put databases with medical information at the medium security level (First Schedule) and at the high level when they hold data on 100,000 people or more or have more than 100 authorised users (Second Schedule); Galil has about 112,000 registered patients, so ask Hagit which level its databases are at. Regulation 15 requires the database owner, before engaging an outside party with access to the database, to examine the security risks of the engagement, to put specific terms in the agreement (including what data may be processed, for how long, and how it is returned or destroyed at the end, with a report at least once a year), and to supervise compliance. Regulation 11(d) requires immediate notice to the Registrar of a serious security incident.

**Medical confidentiality and the record.** The Patient's Rights Law, 5756-1996 (חוק זכויות החולה): the clinician documents the treatment in the medical record and is responsible for it (section 17; a clinician's personal notes are not part of the record); staff keep everything they learn about a patient confidential (section 19); disclosure to third parties only in the listed cases, limited to what is needed (section 20). Counsel's open question goes here: is the audio, or the full transcript, part of the record, or a working file Galil may delete once the note is signed? Don't build anything that assumes either answer: make retention something Galil can instruct.

**The Ministry of Health's cloud rules.** Director-general's circular 2/2021, "Use of cloud computing in the health system" (21 February 2021), applies to a "health organization", defined as a clinic, a health fund or a hospital. It requires an organizational cloud committee (with legal, information security, the privacy officer and IT), a cloud policy approved by management, a risk assessment for each application, minimum contract terms (including controls over the provider's sub-processors, incident reports, and return or deletion of the data at the end), cloud in a country that meets the data-transfer regulations, an opinion of the Ministry's sector committee for applications assessed as high-risk, and a report to the Ministry's information-security officer within 30 days of signing (sections 3–8). Galil's committee met once, in 2022. Ask Hagit to confirm the circular's current status: it was the version available on gov.il when this lesson was written.

**Data abroad.** The circular points to the Privacy Protection (Transfer of Data to Databases Abroad) Regulations, 5761-2001, for where cloud may be. ScribeWave hosts in the EU or the US; Rishma in the EU by default, Israel at extra cost; Kol Refua's audio goes to a US API. Which, if any, is acceptable is Hagit's call with external counsel.

**Public generative AI.** In March 2026, during the war with Iran, the Ministry of Health's information-security and cyber officer ordered health organizations to cut their use of public generative-AI tools at once and banned entering patient data into them; approved enterprise platforms used under internal procedures were exempt (as reported by Mako on 5 March 2026; the directive was temporary and its current status needs checking). Relevant twice: to the consumer apps doctors use today, and to how an approved scribe must be set up.

**The health funds.** Fund A's agreement, Appendix D.4–D.5: prior written approval (45 days) before any outside party processes its members' medical information, and processing in Israel unless approved; Fund B: 30 days' notice. This is a contract, not a law, and it is on the critical path.

**Is a scribe a medical device?** Under the Medical Equipment Law, 5772-2012 (חוק ציוד רפואי), medical equipment, which includes a device used for medical treatment and software needed to operate it, may be manufactured or marketed only once registered (section 2); "medical treatment" takes the Patient's Rights Law definition, which includes diagnosis (section 2 of that law). Registration is handled by the Ministry of Health's medical devices division (AMAR). Whether a given scribe is medical equipment depends on what it is for. The clearest recent statement anywhere is the UK regulator's: in guidance of 29 July 2026, the MHRA says an ambient voice product that transcribes or summarises a consultation for the clinician to review, drafts letters, or suggests codes for review is not a medical device by that alone, while one intended to suggest diagnoses or treatment, or to act without the clinician, is. It is not Israeli law; it is a good set of questions. Ask every vendor for its intended purpose and regulatory status in writing; ScribeWave's "suggested billing codes" and any "insights" feature are what counsel will look at; whether to consult AMAR is Hagit's decision.

**Recording the visit.** The Eavesdropping Law, 5739-1979 (חוק האזנת סתר) defines eavesdropping as listening without the consent of any party to the conversation (section 1); the doctor is a party. That does not settle how patients are told and asked: Fatma's conditions (explained in Arabic by the doctor, who hears it, deleted, free to refuse) go to Hagit and Wasim for the consent wording in 10.5.

EU and US last: Rishma is a European company and its own obligations under EU law are its own; ask for its regulatory position in writing and let counsel read it. Galil, a deployer in Israel, does not need you to map the EU AI Act for it.

### Step 5 — Design the proof of concept before anyone runs it

Use the [vendor PoC protocol](../../templates/vendor-poc-protocol.md) and the [test-set spec](../../templates/test-set-spec.md) from [05.2](../module-05/lesson-02.md). Wasim's team writes the scripts; you write the protocol; Igor and Wasim sign it on 3 December, before any result exists.

- **The visits.** 90 synthetic visits, 30 per language, from real-shaped scenarios (primary care and the four specialist centres). Each script has a list of the 8–15 clinically relevant facts the note must carry. Deliberately include Galil's hard cases: a medicine change said by a relative, code-switching, drug brand names, Galilee dialects (urban, rural, Druze), Russian with Hebrew loanwords, Arabic- and Russian-accented Hebrew. Actors play doctor, patient and relatives in two of Galil's rooms, with air conditioning, a corridor or a child in the room. No real patient takes part.
- **The runs.** Each vendor processes each recording twice, a day apart. Generative tools can give different notes for the same audio; two runs show it.
- **The review.** Six clinicians, two per language, compare each note with the fact list, blind to the vendor where the format allows. They count omitted relevant facts, invented findings, passages the tool marked unsure, and time how long it takes to bring the note to a signable state. Word error rate is computed on the transcript.
- **Thresholds, fixed before results.** A usable note in every language with word error ≤ 15% in each; omissions ≤ 3 per 100 notes overall and ≤ 5 in each language; invented findings ≤ 1 per 100; correction ≤ 4.0 minutes (today's mean note time is 4.8); every must-have term accepted. A vendor that misses any threshold does not go to the clinician pilot.
- **Honesty about size.** 180 notes per vendor detects big differences, not small ones. Report every rate with its count and a 95% interval, and treat a pass as "fit to pilot", never "safe".

### Step 6 — Read the results

The results came back on 30 December (module download, `labs/module-10/poc/`: `review-sheet.csv`, one row per note; `rfp-responses.csv`; `sample-notes.md`). In a spreadsheet: a pivot of `review-sheet.csv` by vendor and language, summing `omitted_relevant` and `invented` and counting notes, averaging `wer_pct` and `minutes_to_correct`.

| Vendor | Word error he / ar / ru (%) | Omissions per 100 notes (95% interval) | Invented per 100 | Minutes to correct | Must-haves refused |
|---|---|---|---|---|---|
| ScribeWave | 14 / **27** / 12 | **7.2** (4.3–12.0); Arabic **11.7** | **2.8** | **4.5** | retention, location, model change |
| Kol Refua | 8 / **no output** / **21** | **5.0** (2.3–10.5); Russian **6.7** | 0.8 | 3.5 | location |
| MedNote for Notara | **19 / 31 / 26** | **11.1** (7.3–16.5) | **2.2** | **6.0** | no training, model change |
| Rishma Health | 9 / 11 / 10 | 2.2 (0.9–5.6); each language ≤ 3.3 | 0.6 | 3.0 | none |

Bold misses a threshold. Only Rishma passes. Three things the table alone does not say:

1. **Relatives.** Omissions per 100 notes with a relative in the room: Rishma 3.7, Kol Refua 8.3, ScribeWave 9.3, MedNote 16.7. Without: 0, 0, 4.2, 2.8. The demos had no relatives.
2. **Unsure-marking.** Three of Rishma's four omissions sat inside a passage it had marked unsure, so the doctor would have been asked to confirm. No other vendor marks uncertainty at all. Visit P-38 in `sample-notes.md` shows the difference: a daughter says in Arabic that her mother stopped her blood-pressure pill; ScribeWave writes "continues antihypertensives", MedNote writes "[unclear]", Kol Refua returns nothing, Rishma writes the stop and asks the doctor to confirm.
3. **Runs differ.** Rishma got P-38 right on run 1 and missed the stop on run 2 (flagged). The same recording can produce different notes. That is why the pilot audits real notes every week.

The intervals matter: Rishma's 2.2 per 100 could be anything from about 1 to 6, and its interval overlaps ScribeWave's. The PoC is strong evidence that MedNote and ScribeWave in Arabic are not fit, and good enough evidence to take Rishma to a pilot. It is not proof that Rishma is safe.

Practice the whole move (score, ask for conditions, run the PoC, choose terms) in the simulation, an educational model of this decision with the same four vendors:

[Simulation: Vendor RFP](../../simulations/vendor-rfp/index.html?preset=galil)

**Track B (Python).** `python poc_score.py` in `labs/module-10/` prints the table above with Wilson intervals, the breakdown by language and by relatives, and the must-haves refused. Python is worth it here because the intervals are tedious by hand and the same script re-scores the pilot's weekly audits and any re-test after a vendor's model change.

### Step 7 — Write the 31 December note, and test the deadline

Exit point 2 is a short note to Shlomit and Igor, answer first: don't sign today; the vendor that led the demos failed Galil's test in Arabic and with relatives, and its quoted plan lets it train on Galil's recordings and keep them 90 days in the EU or the US; Rishma, which demoed worst, is the only vendor that passed every threshold and accepts every must-have term; the decision goes to the steering group on 19 January. Before you send it, ask MedLink in writing whether the price can be held. It can, to 31 March. The deadline was never a reason to sign.

## Watch out

- **An RFP that asks for adjectives.** "Accuracy %", "languages supported" and "confirm you comply" get you a number, a list and a yes. Ask for conditions, documents and answers to terms.
- **Scoring the demo again.** Once the demo is in the evidence score, the evidence can't correct it.
- **Calling a vendor a liar.** You don't need to. "Measured on 200 scripted English visits with a studio microphone" is enough.
- **Doing counsel's job.** You list the rules, the facts and the questions. "Unlawful", "allowed", "a medical device": those words are counsel's.
- **Thresholds after results.** If you set them after seeing the table, the PoC proves whatever you wanted.
- **Treating a small PoC as proof.** 180 notes picks out the clearly unfit. It does not make the winner safe; the pilot's audit does that work.
- **Accepting the deadline.** Ask whether it can move before it becomes an argument.

## Your turn

### Inputs

- Data room (module download): `vendors/` (all four vendors' decks, DPAs, the quote, the offer, the evaluation summary, the safety case, `rfp-draft-v0.md`, `demo-day-scorecards.csv`), `legal/` (all four files), `it/cloud-committee-minutes-2022.md`, `quality/patient-safety-incidents.csv`.
- The PoC results (module download): `labs/module-10/poc/` (`README.md`, `visits-90.csv`, `review-sheet.csv`, `rfp-responses.csv`, `sample-notes.md`).
- Personas: [Hagit Peretz](../../labs/module-10/personas/hagit-counsel-dpo.md), [Yoni Mizrahi](../../labs/module-10/personas/yoni-scribewave-ae.md), [Wasim Haddad](../../labs/module-10/personas/wasim-cmo.md), or their [transcripts](../../labs/module-10/personas/transcripts/); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [claim read-back](../../templates/claim-read-back.md), [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md), [vendor PoC protocol](../../templates/vendor-poc-protocol.md), [test-set spec](../../templates/test-set-spec.md), [regulatory map](../../templates/regulatory-map.md), [DPIA for AI](../../templates/dpia-for-ai.md), [RFP for AI vendors](../../templates/rfp-for-ai-vendors.md).
- Track B: `labs/module-10/poc_score.py`.

### Steps

1. Lock the criteria and weights with what a 5 and a 1 look like; write the sentence about when they were set.
2. Rewrite Igor's draft into an RFP: conditions, claims table, PoC as part of the bid, seven must-haves with reasons, documents, process rules.
3. Write the claim read-back for all four vendors from their documents; interview Yoni (or read the transcript) and add what you learn, including whether the deadline can move.
4. Interview Hagit (or read the transcript) and write the regulatory map: each rule or contract, its source, the question for counsel, the owner. No legal conclusions of your own.
5. Write the PoC protocol: visits, runs, review, thresholds, size and intervals; date it before results.
6. Score the PoC from `review-sheet.csv` (spreadsheet or `poc_score.py`); apply the thresholds; read the relatives, unsure-marking and run-to-run results.
7. Run the simulation's `galil` preset once, then write the 31 December note.

### Time

210 minutes: 20 for the lock, 45 for the RFP, 40 for the read-backs and Yoni, 35 for Hagit and the regulatory map, 25 for the protocol, 30 for the results, 15 for the note.

### Done when

- [ ] Criteria and weights are locked and dated, with the note that they were agreed before the demos and not changed after them; the demo is not re-scored.
- [ ] The RFP asks for measurement conditions, makes the PoC part of the bid, lists seven must-have terms with reasons and asks for intended purpose and regulatory status in writing.
- [ ] Each vendor has a read-back with conditions, fit and rating, and the one vendor whose claim was measured independently is identified.
- [ ] The regulatory map covers health information under the Privacy Protection Law, the Data Security Regulations, the Patient's Rights Law, the Ministry's cloud circular, the funds' agreements and the medical-device question, each routed to counsel or the DPO.
- [ ] The PoC thresholds are dated before the results, and every rate is reported with its count.
- [ ] The 31 December note says "don't sign today" with the evidence, and the deadline has been tested.

<details><summary>Reference answer</summary>

The full set is `labs/module-10/expert/04-rfp-claims-and-poc.md` in the module download. The parts that carry the weight:

**Read-back decision (9 December):** no vendor's headline number is evidence for Galil; Rishma's omission claim (independent, 1,200 conversations, Arabic included) is the only one worth relying on, as a hypothesis for the PoC. ScribeWave 98%: scripted English, studio, one speaker, transcript words, internal; "2 hours": self-reported survey; Hebrew beta on read speech; Arabic MSA and Gulf. Kol Refua "never leaves Israel": contradicted by its Annex B. MedNote 95%: dictation; "zero integration": not on Notara 7.4.

**Yoni (from the transcript):** confirmed every condition when asked exactly; quote is the Standard plan (training on de-identified data; Enterprise +18%); 90 days' audio; EU or US; continuous model updates. *Missed:* whether the date can move. It can, to 31 March 2027, on a written request.

**Regulatory map (excerpt; owner Hagit unless stated):** health information = special sensitivity (Privacy Protection Law s. 3, Amendment 13) → contract terms, DPIA; Data Security Regulations: security level (medical information; 112,000 patients) and regulation 15 before engaging the vendor; Patient's Rights Law ss. 17, 19, 20: the record, confidentiality, disclosure; open: audio as part of the record (external counsel); MOH circular 2/2021: committee, risk assessment, contract terms, report within 30 days (Igor and Hagit); transfer-abroad regulations: EU/US hosting; March 2026 directive: status to check; Fund A D.4–D.5, 45 days; Fund B 30 days; Medical Equipment Law and AMAR: vendors' intended purpose in writing; MHRA guidance as the comparator; Eavesdropping Law s. 1: the doctor is a party; consent wording to Wasim and Hagit.

**PoC protocol (signed 3 December) and results (30 December):** thresholds as in Step 5. Only Rishma passes: word error 9 / 11 / 10%; omissions 4 in 180 notes (2.2 per 100, interval 0.9–5.6), three of them flagged unsure; invented 1 in 180; 3.0 minutes to correct; all seven must-haves accepted. ScribeWave fails on Arabic (27%; 11.7 omissions per 100), overall omissions (7.2), invention (2.8), correction (4.5) and three must-haves. Kol Refua produced no Arabic and fails on location. MedNote fails on every quality threshold and two must-haves.

**31 December note:** "Don't sign today. The vendor that led the demos failed Galil's test in Arabic and on relatives, and its quoted plan lets it train on our recordings and keep them 90 days in the EU or the US. Rishma, which demoed worst, is the only vendor that passed every threshold and accepts every must-have term. MedLink has agreed in writing to hold its price until 31 March. Counsel will send Fund A the approval request as soon as the steering group names a vendor on 19 January."

**What the Hagit transcript missed:** the patient privacy notice (March 2023) promises patients their information is stored in Israel and says nothing about recordings; it must change before any pilot.

</details>

## References

- [Privacy Protection Law, 5741-1981](https://he.wikisource.org/wiki/חוק_הגנת_הפרטיות) (sections 3 and 17B1) and IAPP on [Amendment 13](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform); [Privacy Protection (Data Security) Regulations, 5777-2017](https://he.wikisource.org/wiki/תקנות_הגנת_הפרטיות_(אבטחת_מידע)) (regulations 1, 11, 15 and the schedules); [Patient's Rights Law, 5756-1996](https://he.wikisource.org/wiki/חוק_זכויות_החולה) (sections 2, 17, 19, 20). Wikisource is not the official text: counsel checks the official version.
- Ministry of Health, [director-general's circular 2/2021 on cloud computing](https://www.gov.il/BlobFolder/policy/mk02-2021/he/files_circulars_mk_mk02_2021.pdf) (21 February 2021); Mako on the [March 2026 emergency directive on generative AI](https://www.mako.co.il/news-lifestyle/2026_q1/Article-1fc042e638dbc91027.htm). Check both for later versions before relying on them.
- [Medical Equipment Law, 5772-2012](https://he.wikisource.org/wiki/חוק_ציוד_רפואי); MHRA, [Ambient voice technology-enabled products](https://www.gov.uk/government/publications/ambient-voice-technology-enabled-products/ambient-voice-technology-enabled-products) (29 July 2026), a UK comparator, not Israeli law; [Eavesdropping Law, 5739-1979](https://he.wikisource.org/wiki/חוק_האזנת_סתר).
- Field kit: [04.3 · Vendor and tool review](../module-04/lesson-03.md), [04.4 · AI inventory, risk tiering and the DPIA](../module-04/lesson-04.md), [04.6 · Which law applies to you](../module-04/lesson-06.md), [04.8 · Vendor and claim due diligence](../module-04/lesson-08.md), [05.2 · Building the test set](../module-05/lesson-02.md).
- Templates: [claim read-back](../../templates/claim-read-back.md), [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md), [vendor PoC protocol](../../templates/vendor-poc-protocol.md), [test-set spec](../../templates/test-set-spec.md), [regulatory map](../../templates/regulatory-map.md), [DPIA for AI](../../templates/dpia-for-ai.md), [RFP for AI vendors](../../templates/rfp-for-ai-vendors.md).
- Simulation: [Vendor RFP](../../simulations/vendor-rfp/index.html?preset=galil).
- Earlier: [10.3 · Diagnosis](lesson-03.md). Next: [10.5 · Decide: scoring, contract terms and the clinician pilot](lesson-05.md).
