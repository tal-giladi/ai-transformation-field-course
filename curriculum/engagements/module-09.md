# Meridian Mutual — writer's notes for module 09 (never imported)

The second Stage 2 engagement. The learner is an **internal** lead this time: Meridian's new Head of
AI Transformation, reporting to the COO, with the board's risk management committee above. The
hard part is a **regulated deployment verdict**. The data room is in `labs/module-09/data-room/`
(built by `generate.py`, seed 20261115); lab scripts in `labs/module-09/`. Ground truth for writers:
`curriculum/engagements/module-09-answer-key/` (`python generate.py --answer-key <dir>`); never link
it from lessons. Every number below was produced by the generator and the lab scripts on
2026-11-02 and is reproducible.

## The company

- **Meridian Mutual Insurance Company Ltd.** (מרידיאן הדדית חברה לביטוח בע"מ), founded 1957 as a mutual
  aid fund of a transport workers' cooperative, an insurance company since 1979, subsidiary of
  Meridian Holdings. Supervised by the Capital Market, Insurance and Savings Authority (CMISA).
  ~1,050 employees. Gross premiums 2025 ₪3.4bn (motor 1.45, home 0.52, health 1.10, travel 0.18,
  other 0.15). ~70% sold through agents.
- Claims division (VP Claims Yusuf Darawshe): 212 people, four centres (Ramat Gan: Center/Tel Aviv
  motor and home plus all health and travel; Haifa: North; Jerusalem; Beer Sheva: South). SIU of 7
  plus two external firms. Non-bodily-injury claims: population 73,172 claims reported 1 Nov 2024 –
  31 Oct 2026 (≈36,800 in 2025; ₪281M paid in 2025).
- Systems (fictional): Kalanit Claims (vendor Kalanit Systems Ltd., Herzliya; release 9.4 live Sun
  6 Sep 2026), CRM "Kesher" (six-month export window), ERP payments (runs Monday and Thursday), DMS
  with OCR text layer, BI warehouse.
- Planning numbers (CFO): handler hour ₪145, intake clerk ₪110, NPV at 10%, approval levels
  ₪250k COO / ₪1M CEO / board above; risk committee for anything touching customer decisions;
  planning FX ₪3.70/US$. AI programme 2027 ₪1.6M approved in principle (26 Oct 2026). Pilot ask
  ₪240,000.

## Who the learner is

Internal Head of AI Transformation since **Sunday 1 November 2026**, reporting to COO Ilana Bar-Lev.
Internal lead (01.1): line authority over nothing but a small budget; influence through the COO and
the risk committee; permanent (no exit point, but the "consultant's independence" has to be built:
dotted line to the CRO for AI risk, agreed in the charter); access is easier than a consultant's
but the DPO still requires pseudonymised extracts; the learner will own what they recommend for
years. Day-one access: the data room, the people, read-only Kalanit test environment from week 2.

## Stated ask vs hidden truth

- **Stated ask (Ilana):** "Automate claims intake and spot fraud." Her draft proposal: a winter pilot
  1 Dec 2026 – 28 Feb 2027: Smart Intake for all motor and home claims in all centres, Fraud Insight
  extended to home, Fraud Insight Pro bought (₪380k/yr × 3 years, 15% off if signed by 31 Dec);
  targets intake keying −60%, handling time −30% (10.5 → 7.3 days), "₪20M fraud a year identified".
- **Hidden truth.**
  1. **The slow part is the document chase, not the typing.** Of a claimant's wait (reported →
     last indemnity payment, median **32 days**, sample, paid in 2026), the segments (claims decided
     Jan–Oct 2026) are: intake 2.5 days median, first request 1.1, **document chase 12.8 (mean 18.5)**,
     file complete → decision 8.3, decision → payment 1.6. 45.2% of claims need a second round of
     documents, 14.1% a third; **45.4% of documents asked for in round 2+ were on the standard day-one
     list**; the complete list goes out on the day of the report for only **5.6%** of claims (median 4
     days) although the manual (3.2) says same day. Median wait: 1 round 24 days, 2 rounds 41, 3+ 60.
     Keying costs 5.5 min/claim (₪488k/yr); finding missing documents 6.8 min/claim (₪606k/yr).
  2. **The dashboard measures the regulatory clock, not the claimant's wait.** "Average handling time
     10.5 days, 96.0% within 30 days" = file complete → decision, SIU claims excluded. Three baselines:
     10.5 (dashboard mean; on the sample mean 10.6, median 8.1, n=743), **Kalanit registered → closed
     median 41.1 days** (n=787), **claimant's wait 32 days** (n=696; 25 on the CRM's direct-channel
     subset, n=165). An internal audit
     finding (2025) asked for an end-to-end KPI; overdue.
  3. **The "AI" fraud score is a weighted rules list already in production, and it is proxy
     discrimination.** Kalanit 9.4 switched Fraud Insight on by default for all motor claims on 6 Sep
     (opt-out window passed unused; the June risk-committee action 6.1 "assessment before use" never
     happened; the June management statement "no AI makes or supports claims decisions" is now
     false). 14 factors from the vendor's Israel template; **F08 "interpreter required" (+10) and F09
     "risk area" (+15)** are proxies for nationality/ethnicity and place of residence (both protected
     grounds under the Prohibition of Discrimination in Products and Services Law, which covers
     insurance). Auto-referral at ≥50 holds payment. Motor referral rates (complete extract, Jul–Oct
     2026): before go-live Arabic 3.2% vs Hebrew 3.4% (ratio 0.93); after: **Arabic 21.0% vs Hebrew
     5.4% (3.87×)**; postal area on the risk list 25.9% vs 5.3% (4.92×); North 13.5% vs Center 6.6%.
     F08 fires on 90.3% of Arabic claims, F09 on 68.4%. Without F08/F09, Arabic auto-referrals fall
     from 65 to 4 (Hebrew 33 → 31). Truth (answer key, extract period): of 65 Arabic auto-referrals 3
     are fraud; of 33 Hebrew, 20.
  4. **Labels record suspicion, not fraud.** The vendor's "78% at 10% referral, AUC 0.81" back-test
     used the SUSPECT flag (= SIU referral) as the label. Of closed handler referrals (since Jul 2025)
     only 12.6% were confirmed fraud (174/1,385); Fraud Insight auto-referrals: 2 of 23 closed (84
     still open). "Fraud prevented" ₪6.77M YTD = claimed − paid on all closed SIU cases, of which
     confirmed fraud ₪2.34M, no finding ₪2.90M (mostly deductibles and partial payments), claimant
     withdrew ₪1.54M (111 cases). The ₪20M is the vendor's "10% of claims paid" industry figure × ₪281M
     × two-thirds; no source.
  5. **Smart Intake is not saving time and is not equal.** Time study: with Smart Intake keying 3.5 +
     checking 3.3 min vs 6.7 keying without. On the 240-document set: Smart Intake **82.1%** field
     accuracy on the 200 test documents (Arabic 62.2%, Hebrew 88.6%, Russian 80.0%, English 91.2%),
     Haifa scanner 67.0%; a no-AI rules baseline gets **86.7%** (Arabic 84.4%). 37 of 83 wrong values
     carry confidence ≥ 0.80 (not highlighted). Hebrew email PDFs 96.8%: the conditions of the vendor's
     97.4% claim. Smart Intake copies diagnoses into the free-text notes (37 test documents; 45 in all),
     and sends documents to an EU (Frankfurt) cloud sub-processor the DPO never reviewed.
  6. **Shadow AI.** Health and travel handlers translate foreign medical invoices and draft Arabic
     replies with personal ChatGPT/Gemini (12 handler notes in the CRM sample, May–Oct 2026).
  7. **Seasonal peak.** The proposed pilot window is the busiest quarter: January 2026 ≈ 5,110
     claims registered vs ≈ 2,500 in summer; home claims ×4–5 in storm weeks (12–16 Jan 2025,
     28 Dec 2025 – 1 Jan 2026); intake lag median 6.7 days in Jan 2026 vs 1.6; dashboard handling
     time 13.8–14.6 days in Feb–Mar 2026.

## Planted findings and where they are

| # | Finding | Where (discoverable, never stated) |
|---|---|---|
| P1 | Three baselines for cycle time | dashboard (`reports/`), `claims_register_sample.csv`, `crm_contacts.csv` + `claim_payments.csv`; `baselines.py` |
| P2 | Dashboard excludes SIU and starts at "file complete" | dashboard definitions; register; Yusuf, Tamar |
| P3 | Day-one list only on paper; 45% of later requests were on the standard list | `doc_requests.csv` vs `claims-manual-excerpt.md` 3.2 |
| P4 | Seasonal peak overlaps pilot | dashboard by month; register; `pilot-proposal` window |
| P5 | AI features inside a vendor release, on by default, never assessed | release notes, agreement 7.3, minutes action 6.1, AI inventory (4 entries), register `fi_*`/`smart_intake` from 6 Sep |
| P6 | Fraud score = weighted rules with proxies | `fraud-insight-config-export.csv`, `risk-areas-v3.csv`, motor extract; `bias_test.py` |
| P7 | Labels = suspicion | release notes footnote 2; SIU log outcomes; Natalia, Gil |
| P8 | "Fraud prevented" is not savings; ₪20M unsourced | dashboard definition, SIU log, finance summary, Kalanit email |
| P9 | Smart Intake: lab claim vs reality; group gap; diagnoses; no time saved | release notes footnote 1, `smart_intake_output.csv`, time study |
| P10 | Shadow AI translation | `crm_contacts.csv` handler notes; Marina, Rana |
| P11 | June statement now false; committee not told | minutes; Michael |
| P12 | Messy data: agent-channel age band missing (28%), Hebrew "צפון" in region (13 rows), CRM FNOL rows without claim number (31 of 216), CRM covers six months and direct channels only | register, CRM |
| P13 | Claimant not told reasons; letters in Hebrew; out-of-pocket rental | Samira; complaints log (CL-2026-026307, PN entry 12 Oct) |

## The claimant's claim (fixed record)

Samira Abu-Ahmad, **CL-2026-026307**: motor own damage, loss Mon 14 Sep 2026 17:00 (car hit while
parked outside her school), first call Tue 15 Sep 09:41, registered Thu 17 Sep 11:05, postal area N-07
(on the risk list), Arabic correspondence, interpreter flag Y, age band 55-64, non-network garage in
her town, two prior claims (windscreen 2024, parking scrape 2025), claimed ₪16,480. Fraud Insight 60
= F03 15 + F04 10 + F05 10 + F08 10 + F09 15 → auto-referral 17 Sep 11:19 (SIU-03). Requests: 20 Sep
(standard five), 1 Oct (police confirmation — not on the own-damage list; she had to file a police
report to get it — and photos again), 12 Oct (garage estimate again, "unreadable": Eastern Arabic
digits; and a statement of events). Complaint 12 Oct ("told the computer flagged the file"). SIU
closed no finding 22 Oct; decision 25 Oct; ₪14,530 paid to the garage Thu 29 Oct. 44 days from first
call to payment. Out of pocket: ₪1,450 car rental (not claimed; she was never told she could). Letters
arrived in Hebrew.

## Cast and unlocks

| Persona | Role | Type | Hidden facts (unlock) |
|---|---|---|---|
| Ilana Bar-Lev | COO | Sponsor | Told the CIO in August to leave the 9.4 modules on ("included in maintenance"); did not bring them to the committee (ask who decided to switch them on, or show action 6.1). Already told the CEO "₪20M" during the October budget round (ask what the CEO/board already heard). CEO wants a "48-hour claims" campaign by spring; the agents' association complained (ask why now) |
| Yusuf Darawshe | VP Claims | Middle manager / process owner | Team leads set "file complete" late and push follow-up requests; he knows the dashboard flatters (ask how file complete is set in practice, or show the request data). Haifa handlers say the amber badges and referrals land on Arab claimants; he raised it with the SIU head verbally only; fears being seen as defending fraud (non-attribution + ask what changed in the SIU queue since September). The 6 winter temps start training 6 Dec; no capacity for a pilot in Dec–Feb (ask what December–February looks like) |
| Natalia Gurevich | Chief Actuary | Finance / sceptic | Her 2025 note: confirmed fraud ≈0.4% of claims by count; real leakage maybe 1–2% of paid, ₪3–6M; "10%" is a marketing number (ask how she would estimate leakage). Uses reported → final payment for reserving (ask which cycle time she uses). Emailed the CIO in August that the back-test label is the SUSPECT flag; no answer (ask whether anyone validated the vendor's numbers) |
| Michael Ohana | Chief Risk Officer | Risk / compliance, sceptic | Knows the June statement is false since 6 Sep; waiting for "the AI person" to own the correction (ask whether the committee knows Fraud Insight is live). Tempted to call Fraud Insight "not AI" under the policy definition (ask how he classifies it and why). Compliance logged two complaints forwarded by the CMISA public inquiries unit in October about "investigation without explanation" (ask about complaints mentioning the SIU or the regulator) |
| Tamar Weiss | Head of Internal Audit | Internal audit | 2025 audit "Claims SLA reporting" finding 3 (KPI excludes SIU, starts at file complete; end-to-end KPI by Q2 2026) open and overdue (ask about previous audits of claims KPIs). 9.4 change record ticks "no new functionality enabled" (ask how 9.4 went through change management). Will not sign off the learner's work (independence) |
| Dr. Rana Haj-Yahia | Senior counsel, privacy; DPO | Legal / DPO | Never told about Smart Intake's Frankfurt processing; the Annex C notice went to the CIO office only; diagnoses copied to free-text notes visible to all claims users (ask whether she reviewed 9.4 / where documents are processed). Agreement 9.2 lets Kalanit train on anonymised customer data; she objected at renewal, overruled (ask about data-use terms). A handler asked her in September whether ChatGPT may be used to translate; she said no; nothing followed (ask about public AI tools). EEA point: a claimant sending their own foreign invoice is outside the 2023 EEA regulations; an assistance company receiving it from an EEA hospital may not be — route to her |
| Marina Kogan | Senior claims handler, health & travel, Ramat Gan | Frontline, secret enthusiast | She and about ten colleagues paste foreign invoices and Arabic letters into personal ChatGPT/Gemini; email attachments are not always redacted (ask how she handles a Georgian invoice on a normal day + non-attribution). The travel-medical standard list lacks "medical report in Hebrew or English", so a second round is almost certain; intake waits for the agent to "send everything" before the list goes out (ask why second requests happen). Wants a sanctioned tool |
| Samira Abu-Ahmad | Claimant, 58, teacher, Lower Galilee | Person affected | Told "the computer flagged your file"; assumes it is because she is Arab; wants the reason (ask her to go through each contact). Paid ₪1,450 for a rental car; never told she could claim it (ask what it cost her beyond the repair). Almost withdrew; her son said it was not worth it (ask whether she thought of giving up) |
| Gil Navon | Account executive, Kalanit Systems | Vendor AE | 97.4% = 500 typed Hebrew forms at 300 dpi; Eastern Arabic digits a known issue, fix in 9.6 (Q2 2027) (ask under what conditions / Arabic). Fraud Insight is a weighted rules library, no learning; IL template weights from consortium data 2019–2021, never re-validated for Meridian; F08/F09 "correlated with SIU referrals" (ask how the score is computed / where weights come from). AUC label = SUSPECT flag (ask what "fraud-flagged" means). Configuration can be changed any day by a free change request (ask "can we switch auto-referral off today?"). Quarter target depends on Pro by 31 Dec |

Lessons: 09.1 (Ilana), 09.2 (Yusuf, Marina, Samira; Natalia optional), 09.3 (Natalia, Yusuf), 09.4
(Michael, Rana, Gil, Tamar), 09.5 (Marina as reviewer, Rana for minimisation), 09.6 (Ilana:
hardest-finding rehearsal; risk committee chaired by Prof. Hanna Sela with Michael, Natalia, Eran,
Yusuf).

## Timeline

- Data: claims reported 1 Nov 2024 – 31 Oct 2026, exported Wed 4 Nov 2026. Motor extract 1 Jul –
  31 Oct 2026. SIU log from 1 Jul 2025. CRM May–Oct 2026. Complaints Jan–Oct 2026 (to 4 Nov).
- 15 Jun 2026 risk committee (policy; statement; action 6.1). 22 Jun board approves AI policy.
  3 Aug Annex C notice. 10 Aug 9.4 release notes. 6 Sep go-live (Sunday). 9 Sep opt-out window
  closed. 20 Oct Kalanit email. 26 Oct board: AI programme ₪1.6M in principle; risk committee deferred
  the AI inventory item to 15 Dec. 1 Nov learner starts; Ilana's proposal draft 2.
- **Wed 4 Nov: the call** (09.1). Sun 8 Nov charter and first-week plan. Tue 10 Nov management
  meeting (Ilana presents the proposal "subject to the head of AI's plan"). 8–19 Nov discovery
  (09.2); Thu 19 Nov findings memo, with an **urgent interim recommendation** (switch off
  auto-referral, keep the badge with written reasons). 22–26 Nov diagnosis (09.3): one-page case to
  Ilana Thu 26 Nov. 30 Nov – 10 Dec deployment verdict (09.4): pre-read Tue 8 Dec; **risk committee
  Tue 15 Dec**. 16 Dec – 14 Jan offline pilot build and eval (09.5) on the data room (nothing live
  during the peak). **Tue 26 Jan 2027: readout to a joint steering / risk committee session** (09.6).
- Six months later: July 2027.

## The futures (09.6 debrief)

1. **Switch it all on (Ilana's proposal as written).** Smart Intake in all centres and Fraud Insight on
   home from 1 Dec; Pro signed 28 Dec (₪1.14M over three years). Storm week 3–7 Jan 2027: home
   referrals jump, SIU queue triples, temps re-key Arabic invoices; January handling time 19 days on
   the dashboard, claimants' wait over 50 days. Complaints about investigations triple; the CMISA
   public inquiries unit asks Meridian to explain the rise; an Arab civil-rights NGO files a motion to
   certify a class action under the Prohibition of Discrimination Law (April). Internal audit rates
   AI governance "unsatisfactory" (May). Fraud Insight is switched off in May; confirmed fraud is
   unchanged; the ₪20M is quietly dropped. The CEO's "48 hours" campaign is cancelled.
2. **Expert path.** On 22 Nov, after the interim memo, Ilana signs a change request: auto-referral
   off, F08/F09/F13 disabled, the score shown to SIU only as a review aid with written reasons. The
   15 Dec committee: Fraud Insight **block** (until re-validated on confirmed outcomes with an outcome
   test by group), Smart Intake **flag → ship with conditions after the peak** (minimisation fix,
   Arabic digits, Haifa scanner, per-language thresholds), Pro **not now**; the June statement is
   corrected in the minutes. From 4 Jan a no-AI fix: the complete documents list at first notice
   (agent portal mandatory fields + intake checklist) and Arabic letters. The extraction pilot runs in
   shadow mode from 15 March (Hebrew, Russian, English), Arabic from May after the digit fix. By July:
   rounds per claim 1.62 → 1.27, claimants' wait median 32 → 23 days, Arabic/Hebrew referral ratio
   1.1, confirmed fraud 19% of closed SIU cases. The CFO books no fraud "savings", ≈2,300 handler
   hours of capacity. Samira gets a written explanation in Arabic, the ₪1,450 and an apology.
3. **Half-way.** The committee approves Smart Intake for the winter "with monitoring" and keeps Fraud
   Insight with the threshold raised to 60. The proxies stay: the Arabic referral ratio is still
   3.4×. Arabic invoices keyed from wrong pre-fills cause ₪180k of overpayments found in an April
   QA sample. Internal audit's Q2 finding forces both off in June. The learner's credibility with the
   committee is gone; the documents-list fix, which needed no AI, never got attention.

## Regulation used (verified 2026-11-02; sources in `curriculum/inbox/module-09-sources.md`)

- Israel: Supervisor's circular 2016-9-9 "Clarification and settlement of claims and handling of
  public inquiries" (5 Jul 2016): principles (s. 3), documents list at first contact (8(a)(1)(d)),
  additional documents within 14 business days (8(a)(6)), notice within 30 days of having all
  documents (8(b)), continued-clarification notice every 90 days, main findings of an investigation
  report (annex s. 6(c)). Prohibition of Discrimination in Products, Services and Entry into Places of
  Entertainment and Public Places Law, 5761-2000: s. 3(a) grounds incl. nationality, country of
  origin, religion, age; s. 3(a1) place of residence; "public service" includes insurance; s. 3(d)(1)
  exception (as quoted in the inter-ministerial report). Equal Rights for Persons with Disabilities
  Law s. 19לה (insurance; reasoned notice). Inter-ministerial team final report on AI in the financial
  sector (Dec 2025): risk-based, explainability general/specific, human involvement for high-impact,
  outcome testing for proxies, responsibility stays with the supervised entity, existing CMISA
  framework (consolidated circular: risk management incl. model risk, outsourcing chapter). PPL
  Amendment 13 (health data = special sensitivity; DPO), PPA draft AI guidance (Apr 2025), Data
  Security Regulations, transfer regulations, 2023 EEA regulations.
- **EU AI Act: decided not applicable to this engagement.** Meridian has no EU establishment, sells to
  Israeli residents, and the outputs are used in Israel (Art. 2(1)); claims handling and fraud
  detection are not in Annex III (5(b) excludes fraud detection from credit scoring; 5(c) covers only
  life and health insurance risk assessment and pricing). Note for 09.4: if Meridian ever priced
  health cover for EU residents with AI, Annex III 5(c) and the 2 Dec 2027 date (Reg. 2026/1744) would
  matter. Used only as a benchmark vocabulary.
- US four-fifths rule (29 CFR 1607.4(D)) named as the origin of the 0.80 screen; not law in Israel.
