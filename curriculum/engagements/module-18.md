# Tzurim Academic College — writer's notes for module 18, the capstone (never imported)

The unseen engagement. The learner runs the whole method with **no hints**: the lessons (18.1–18.3) give
the brief, the data room and the cast, and teach how to assemble, integrate and present the deliverable
set using earlier engagements as worked examples. Nothing in any lesson, the lab README, the INDEX or the
brief names a planted finding. The hidden truth and the expert's set reach the learner only in
`projects/m18-capstone.md`, inside `<details><summary>Open only after you have submitted your
deliverables</summary>`, and in `labs/module-18/expert/` (which 18.1 says plainly not to open early).
The data room is built by `labs/module-18/data-room/generate.py` (seed 20270207; standard library only;
run twice, byte-identical; 2.55 MB).

## The organization

- **Tzurim Academic College** (המכללה האקדמית צורים), fictional private (non-budgeted) college in the
  southern Shfela, founded 1996, operated by a public benefit company (חל"צ), recognised by the Council
  for Higher Education. Checked 3 Nov 2026: no real institution of that name (web search).
- 6,840 students (first degree 6,110, MBA 730); **712 staff** (236 administrative, 148 senior faculty,
  328 adjuncts). Revenue 2026 ₪231.6M (tuition ₪211.9M), surplus ₪6.4M. Tuition 2025-26: BUS/BEH
  ₪29,400, COM ₪28,200, IEM ₪32,400, CS ₪33,600, LLB ₪36,800.
- Tracks: regular, evening, Haredi track (separate classes). Students write in Hebrew, Arabic, Russian,
  English; replies are in Hebrew.
- Systems (fictional): **Rishum 2** SIS (in-house, Aug 2024; new student numbers `0yy######`); old SIS
  (8-digit numbers starting 1); finance ERP; **Tavla LMS** (Tavla Learning Ltd., fictional; release
  2026.2 turned on "Engagement Insights" by default); inquiry portal; admissions CRM with lead scoring;
  office suite with an AI assistant add-on (120 licences, March 2026); survey tool with open-text
  summaries. Vendor **Persevia Inc.** (fictional; checked 3 Nov 2026, no real company found).

## Who the learner is

An **independent consultant** (two-person practice), engaged by the CEO after the board session of 20
January 2027. Fixed fee ₪186,000 + VAT in three phases of four weeks with an exit after each. Reports to
the CEO; day-to-day through Tamar Weiss (VP Administration). Board meeting with one recommendation:
**Tuesday 4 May 2027**. Start: **Sunday 7 February 2027**. The CEO has told Persevia to start a free pilot
on 1 March and asked IT to prepare a three-year extract incl. accommodations flags by 25 February.

## Stated ask vs hidden truth

- **Stated ask (CEO, board 20 Jan 2027):** "Dropout jumped from 12% to almost 20%. Bring an AI
  early-warning system (Persevia) that predicts who will leave so advisers can save them; target 12%
  first-year dropout by 2029."
- **Hidden truth.** Tzurim does not have a prediction problem. It has **a broken measure** and **a process
  that pushes students out**, and **an AI risk score already running, unexamined**.
  1. **The measure.** Report query BI-07 (2019) counts every status except 10, 21, 41, 60 as dropout.
     Code 47 (reservist freeze, added 3 Nov 2024) and 33 (internal transfer) are counted. Cohort 2023's
     reservist freezes were coded 41 (excluded). True leaving (51/52/58): 11.1% (2023), 13.3% (2024),
     11.5% (2025) — flat, against the report's 12.2 → 19.5 → 17.7.
  2. **The block.** The ERP blocks exam registration when the balance exceeds ₪1,500 on the check date
     (4 Jan 2026), registration closes 7 days later (11 Jan), and the median block lasts **11 days**.
     **60% of blocked students** had a scholarship or reservist grant approved but **not yet posted**
     (the college's own monthly batch). Reservists blocked 61% vs 13% for others. 75% of blocked students
     were still blocked at registration close. First-years who missed registration because of a block
     left at **33.7%** vs 7.6% for unblocked first-years; **45% of first-year leavers** had missed
     registration through a block.
  3. **The queue.** Block inquiries go to the wrong unit (students pick "exams"): 48% of finance-resolved
     inquiries were first routed elsewhere; reassigned inquiries take a median 9 working days vs 3.
     Arabic inquiries: median 5 working days vs 3 for Hebrew, reopened 30% vs 11%, and 92% were answered
     in Hebrew.
  4. **AI already in use, unexamined.** Tavla's Engagement Insights (release 2026.2, on by default) scores
     every student; drivers include "reserve-duty absence" and "medical or learning accommodation on
     file" from the accommodations module. Haredi-track students red 58%, reservists 46%, regular 7%,
     with similar leaving rates (10.6%, 8.2%, 8.3%). Precision of red 12.5% against a base rate of 8.4%;
     30% of first-year leavers had gone before the score existed. Not in any inventory; no DPIA; the
     2022 privacy notice says nothing about profiling; the DPA with Tavla predates the feature.
  5. **The urgent finding.** On 16 Mar 2026 the head of Student Success sent the red list (288 students,
     names, numbers, reasons incl. 38 with a medical or learning accommodation and 125 with reserve duty)
     as an "anyone with the link" sheet to 61 lecturers (46 adjuncts); one forwarded it to TAs; the link
     still opened on 4 Feb 2027. Must go to the DPO and the VP Administration the same day.
  6. **The vendor.** Persevia's 85% is recall in the top 30% band on a US community-college cohort; its
     +4.1 points coincided with a statewide free-tuition programme; pilot terms: full three-year extract
     incl. accommodations flags to a US region, a licence to train on de-identified data that survives
     termination, automatic conversion to a 36-month subscription. The CEO promised to be "the first
     Israeli college" and a reference site.
  7. **A step on paper.** Early-contact procedure SS-03: first-years who failed or missed ≥ 2 semester A
     exams are called within 14 days of grades (1 Mar 2026). 637 eligible, 153 contacted (24%), 78
     within 14 days (12%). From 16 Mar, 53% of adviser contacts were driven by the red list; 15% of
     red-list calls ended with the student objecting.
  8. **Shadow AI.** Adjuncts: 63% weekly or daily AI users; 21 of 84 enter student work with names or
     numbers into personal tools. Student administration: ChatGPT and Google Translate for Arabic e-mails;
     17 administrative staff enter student personal details. HR's summary reported "65% never use AI" on
     administrative staff only. Lecturers' Wi-Fi shows AI-writing-detector traffic.
  9. **Detectors as evidence.** 19 of 46 integrity cases rest on an AI-detector score alone; 9 of the 19
     are students whose first language is not Hebrew; 6 of 8 appeals overturned (vs 0 of 1 for other
     evidence types).
  10. **Adoption already measured.** 120 office AI licences: 58 management, 22 academic heads, only 3 in
      student administration; 39 never used, 35 used ≥ 8 days in 30.
  11. **The join.** Finance exports student numbers as numbers: new-SIS numbers lose the leading zero.
      Naive join matches 1,906 of 6,128 accounts (cohort 2023 only); padded to 9 digits, all 6,128.
  12. **Value.** The CFO's block rule (Sept 2023) cut bad debt from ₪3.1M (2022) to ₪1.9M. Keeping the
      block for real arrears and stopping it for approved-but-unposted grants protects that and removes
      most blocks.

## Planted findings (where each is discoverable; never stated)

Paths relative to `labs/module-18/data-room/`.

| # | Area | Finding | Where |
|---|---|---|---|
| 1 | Data / value | Dropout measure counts freezes (47) and transfers (33) | `company/dropout-report-2026-12.md` note 1, `students/status-codes.csv` (47 added 2024-11-03), `students/registry-students-2023-2025.csv` |
| 2 | Discovery | Stated ask (prediction) is not the problem; blocks push students out | `finance/tuition-accounts-2025-26.csv`, `policies/tuition-regulations-2025-26.md` s. 5, 7, 8, `policies/academic-regulations-extract-2025-26.md` 4.2–4.4, registry |
| 3 | Discovery | Grant posting lag causes 60% of blocks; reservists blocked 61% | finance file (`scholarship_posted_date` > block date), `policies/reservist-students-policy-2025-26.md` |
| 4 | Discovery | Misrouting and Arabic service gap | `inquiries/student-inquiries-2025-26.csv`, `inquiries/inquiry-routing.md` |
| 5 | Governance | Tavla EI on by default, sensitive drivers, no inventory/DPIA/notice | `lms/tavla-release-notes-2026-2.md`, `lms/engagement-insights-export-2026-03-15.csv`, `it/systems-and-contracts.csv` (DPA 2022), `policies/student-privacy-notice-2022.md` |
| 6 | Governance (urgent) | Red list shared "anyone with the link", still open | `student-success/emails-red-list-2026-03.md`, `student-success/red-list-for-lecturers-2026-03-16.csv` |
| 7 | Governance | Persevia pilot terms: US region, training licence, auto-conversion; CEO said yes | `vendor/persevia-pilot-terms.md`, `vendor/emails-ceo-persevia-2027-01.md`, board minutes decision 2 |
| 8 | Value | Vendor ROI and case-study conditions | `vendor/persevia-proposal.md`, `vendor/persevia-case-study.md` footnotes |
| 9 | Fairness | EI flags Haredi and reservists with no higher leaving | EI export + registry + LMS activity |
| 10 | Step on paper | Early-contact procedure 24% / 12% | `student-success/early-contact-procedure-2024.md`, `student-success/adviser-contacts-2025-26.csv`, `students/exam-periods-first-year-2025-26.csv` |
| 11 | Shadow AI | Adjunct and admin use, student data in personal tools; HR summary excludes faculty | `people/staff-ai-survey-2026-06-responses.csv`, `people/staff-ai-survey-2026-06-summary.md`, `it/proxy-ai-summary-2026-06-to-09.csv` |
| 12 | Governance | Detector-only integrity cases; overturned on appeal | `academic/integrity-cases-2025-26.csv`, `policies/faculty-ai-guidance-draft-2025-09.md` item 3 |
| 13 | Adoption | Licences with managers, not the front office | `it/office-ai-assistant-usage-2026-10.csv`, `budget-2027-extract.md` line 6150 |
| 14 | Data | Leading-zero join | finance file vs registry |
| 15 | Adoption / workforce | Adjunct committee letter: consult first, paid training, no AI evaluation of lecturers; survey tool summarises course evaluations by default | `people/adjunct-committee-letter-2026-10-20.md`, `it/systems-and-contracts.csv` |
| 16 | Governance | Admissions CRM lead scoring and the survey tool's summaries: AI inside SaaS, not inventoried | `it/systems-and-contracts.csv` |
| 17 | Persona only | CFO knows the posting lag and the 2-person desk backlog | Avi |
| 18 | Persona only | Registrar reported the code-47 problem in Dec 2024; never fixed | Galina |
| 19 | Persona only | CEO promised Persevia a reference visit; already said yes | Yaron, Noa |
| 20 | Persona only | Student told by an adviser she was flagged "for medical accommodation" | Rawan |

## The cast (9)

| Persona | Role | Type | Hidden / unlock |
|---|---|---|---|
| Yaron Bar-Lev | CEO | Sponsor and owner of the ask | Told Persevia "yes" and promised a reference visit; told the board's finance committee "₪10M a year"; privately unsure the 19% is real ("the war"), afraid of looking like he makes excuses. Unlock: ask exactly what he said to Persevia; ask what would make him confident the number is right |
| Prof. Hanna Levkovich | President | Academic head, quiet sceptic | Opposes Persevia but will not fight Yaron openly; academic council left AI to syllabi because the deans could not agree; worried about detector cases. Unlock: frame as students' rights and academic due process; ask what she would need to support a "not yet" |
| Avi Golan | VP Finance | CFO | Introduced the block (2023); knows the reservist grant is posted in a monthly batch after the reservist desk verifies days and that the two-person desk has a backlog in block weeks; will not drop the block for real arrears. Unlock: ask what happens to a student whose grant is approved but not posted; separate arrears from timing |
| Samah Khoury | Head of Student Success | Middle manager, receiving team | Uses the red list since March; sent the open link; 5 working advisers can make about 150 meaningful contacts a week; early-contact procedure mostly not done; knows Haredi and reservist students are "always red". Unlock: non-attribution; ask how she decides whom to call this week |
| Galina Petrov | Registrar, head of student administration | Data steward | Reported in Dec 2024 (ticket to IT) that BI-07 counts code 47; never fixed; knows the leading-zero export; nobody asked her how the number is made. Unlock: ask how the dropout figure is computed, which codes count |
| Ofer Sasson | IT manager, information security officer | IT / CISO | Left Engagement Insights on (default) at Samah's request; DPA predates it; extract for Persevia half-ready; proxy data; the office AI licences. Unlock: ask what changed in Tavla in 2026; ask what he has prepared for Persevia |
| Dr. Yonatan Mekonen | Adjunct lecturer, chair of the adjunct committee | Union rep, secret enthusiast | Uses ChatGPT Plus for feedback on 180 assignments; colleagues paste names; received the red-list link; detector cases. Unlock: ask about his own marking week; promise not to attribute; ask what an approved tool would need |
| Rawan Haj-Yahya | Second-year BA-BUS student, union welfare officer | Person affected | Blocked Jan 2026 (municipal scholarship not posted); wrote in Arabic; Hebrew reply after 12 days; missed two exams; adviser called in March saying she was flagged and mentioned her dyslexia accommodation; knows friends who left. Unlock: ask what happened after the block; ask why the adviser called |
| Noa Ben-Ami | Persevia regional account executive | Vendor AE | Model trained on US institutions only; 85% conditions; needs accommodations flags; training licence; auto-conversion; Yaron's reference promise. Unlock: ask under what conditions 85% was measured; ask where data goes and what it is used for |

Transcripts leave hidden: Yaron's reference promise; Hanna's conditional support; Avi's monthly batch;
Samah's open link (she mentions "a sheet" but not the sharing setting); Galina's 2024 ticket; Ofer's
default-on decision; Yonatan's names-in-prompts; Rawan's accommodation remark; Noa's training licence.

## Timeline

- Data: cohorts 2023–2025; finance, exams, inquiries, contacts 2025-26; LMS Nov 2025–Mar 2026; EI score
  15 Mar 2026; statuses at 1 Oct 2026; survey Jun 2026; proxy Jun–Sep 2026; licences Oct 2026.
- 2023-09 block rule; 2024-08 Rishum 2; 2024-11-03 code 47; 2025-12 academic council AI decision;
  2026-01-04 block check; 2026-02-09 Tavla 2026.2; 2026-03-16 red list sent; 2026-10-20 adjunct letter;
  2026-12 dropout report; 2026-12-28 Persevia proposal; 2027-01-20 board; 2027-01-24 CEO's yes.
- Engagement: Sun 7 Feb 2027 start; Mon 8 Feb Yaron; red-list link escalated the first day it is read;
  25 Feb Persevia extract deadline; 1 Mar planned pilot start; phase 1 ends 4 Mar; phase 2 to 1 Apr
  (Noa Mon 15 Mar); phase 3 to 4 May; Passover 21–29 Apr 2027; pre-read Tue 20 Apr; rehearsal with
  the chosen executive Sun 2 May; **board Tue 4 May 2027**. Semester B 2026-27 block check about 6 Jun
  2027 (the first date the fast lane can show value). Six months later: November 2027.

## The expert path (labs/module-18/expert/)

One recommendation: **fix how Tzurim counts and how it pushes students out before buying prediction.**

1. Restate the measure: first-year leaving 11.5% (cohort 2025), freezes and transfers reported apart.
2. Block fast lane before the June 2027 check: approved-but-unposted grants never block (nightly feed
   from the reservist desk and scholarship approvals); arrangements decided in 3 working days; block
   inquiries routed straight to collections; advisers alerted (rule, no AI) when a first-year is blocked.
3. Pilot: inquiry triage + draft replies in the student's language, human sends; shadow from 9 May.
4. Pause Engagement Insights for outreach; DPIA, notice, fairness test before any re-enable.
5. Policy pack incl. an approved tool for staff on the college tenant, no detector-only cases.
6. Recommend-against: no Persevia pilot or contract in 2027; re-decide in 2028 on a PoC protocol.

Money from line 6800-110: **₪540,000** (fast lane ₪150k; inquiry pilot ₪135k; governance and DPIA
₪85k; approved staff tool and training ₪110k; measure and dashboard ₪30k; contingency ₪30k).

## Numbers (computed from the generated files)

Volumes: registry 6,760; finance 6,128; exam rows 4,326; inquiries 2,669; contacts 1,184; LMS rows
11,497; EI 2,231 (red 288, amber 722, green 1,221); red list 288; integrity 46; survey 276; licences 120;
proxy 180 rows; systems 9.

Value (directional): excess leavers associated with block-missed registration about 92 first-years (353
× (33.7 − 7.6)%), 38 second-years (281 × (17.1 − 3.7)%), 14 third-years (262 × (7.6 − 2.1)%) = 144 a
year in these cohorts. Contribution per retained student-year about 70% of tuition (CFO). First-year
about ₪42k remaining contribution, second-year about ₪21k, third about ₪5k → about ₪4.7M if all were
avoided; the expert assumes the fast lane removes 60% of block-missed registrations (the posting-lag
share) and credits half of the association: **about ₪1.4M a year, directional**, range ₪0.7–2.8M.
Persevia core 36 months: US$38,000 + 3 × 58,500 = US$213,500 ≈ ₪669,500 at ₪3.136 (about ₪223k a
year); its own claim (₪10.6M a year) uses gross tuition × 3 years × 120 students.

## The futures (reveal in projects/m18-capstone.md)

1. **The free pilot.** The extract goes to Persevia on 25 Feb; the board approves the subscription in May
   "to keep the momentum". In October the student union learns from a TA that the red list names
   accommodations; a complaint reaches the Privacy Protection Authority; the college pauses Persevia and
   Tavla EI at once. Advisers call 900 "at-risk" students in the autumn, a third of them reservists. The
   June and January blocks run as before; first-year leaving 12.1%; the report still says 18%.
2. **The expert path.** Measure restated on 4 May (11.5%); fast lane live for the June 2027 check: blocks
   in semester B 2027 fall from 643 to about 250, block-missed registrations by about 60%; cohort 2026's
   first-year leaving 9.9% (Oct 2027, one year, directional); the inquiry assistant live in September,
   Arabic replies in Arabic from 8% to 84%, reopen rate for Arabic 30% → 13%; EI off for outreach, DPIA
   done, re-enabled in December for advisers only without sensitive drivers; adjuncts get an approved tool
   and two paid hours; no detector-only cases. Persevia re-decision set for March 2028.
3. **Half-way.** The board approves the inquiry assistant (visible, cheap) and the policy pack, but Avi
   will not change the block before the 2028 budget and EI stays "because it's free". The assistant routes
   block inquiries faster but cannot lift blocks; leaving unchanged; EI keeps calling reservists.

**What decided which future:** whether the board's money went to the block process and the measure — not
to the visible tool — and whether the open red list and EI were stopped before anything new was added.
