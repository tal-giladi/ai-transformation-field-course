# 02 · Findings memo

*Expert deliverable. To: Yaron Bar-Lev; steering group (Hanna Levkovich, Avi Golan, Tamar Weiss, Lior Amsalem). Thursday 4 March 2027, end of phase 1. Evidence labels: **M** measured from the data room (reproducible), **R** reported by a named role, **D** directional (inference from measured data), **A** assumed.*

## The answer first

Tzurim does not have a prediction problem. The dropout figure the board saw counts students who froze their studies for reserve duty and students who moved to another programme in the college; on a consistent definition, first-year leaving has been flat at 11–13% for three cohorts. What does push students out is visible already: the college blocks exam registration for balances that are often its own unposted grants, takes a median of eleven days to lift the block while registration closes after seven, and routes and answers the resulting inquiries slowly, worst in Arabic. Meanwhile an AI risk score is already running unexamined, flags reservists and Haredi-track students at five to eight times the rate of others with no higher leaving rate, and its list with health-related reasons was shared through an open link.

## Findings

### F1 · The headline number counts students who did not leave (M)

| Cohort | Report (BI-07) | Left the college (51, 52, 58) | Reservist freeze (47) | Transfer (33) | Other freeze (41, excluded by BI-07) |
|---|---|---|---|---|---|
| 2023 | 12.2% | 11.1% | — (coded 41) | 1.1% | 5.3% |
| 2024 | 19.5% | 13.3% | 4.4% | 1.8% | 1.1% |
| 2025 | 17.7% | 11.5% | 4.4% | 1.8% | 1.3% |

Source: `students/registry-students-2023-2025.csv`, `status_after_year1`; `students/status-codes.csv` (47 added 3 November 2024); report note 1. Galina Petrov (R) opened a ticket in December 2024 asking to exclude 47; it was not done. **Consequence:** the 12% target is already met on a consistent measure of leaving; the board needs a new measure and a new target. **Owner:** registrar, with the BI analyst.

### F2 · The exam-registration block is the largest visible exit (M, D)

- 1,194 of 6,128 students (19.5%) were blocked at the semester A check on 4 January 2026; median block 11 days; registration closed 7 days after the check; **75%** of blocked students were still blocked at registration close (M, `finance/tuition-accounts-2025-26.csv`).
- **60%** of blocked students (718) had a scholarship or grant approved but posted after the check date (M). Reservists were blocked at 61.4%, others at 13.2% (M). Avi Golan (R): reservist grants post in a monthly batch after the desk verifies days; the collections desk is two people and arrangements take two to three weeks in January against ten working days in the regulations.
- First-years who missed registration because of a block left at **33.7%**, against 7.6% for unblocked first-years and 6.0% for those unblocked in time (M). **45%** of first-year leavers in 2025-26 had missed registration through a block (M). Second-years: 17.1% vs 3.7%.
- The association is strong; causation is not proven (D): students in financial trouble leave more for other reasons too. But 60% of these blocks are timing, not debt.

### F3 · Inquiries go to the wrong desk, and Arabic waits longest (M)

2,669 inquiries (`inquiries/student-inquiries-2025-26.csv`): 26.9% reassigned; reassigned ones close in a median 9 working days vs 3; of inquiries finance resolved, 48% were first sent elsewhere (students pick "exams" when they cannot register). Arabic inquiries: median 5 working days vs 3 for Hebrew, reopened 30% vs 11%, and 92% answered in Hebrew. Volumes peak in January (988) and June (567), the block months. Galina Petrov (R): two Arabic speakers "when they are free"; staff paste Arabic e-mails into public tools.

### F4 · An AI risk score already runs, unexamined (M, R)

Tavla release 2026.2 switched Engagement Insights on by default (`lms/tavla-release-notes-2026-2.md`); 2,231 first-years scored on 15 March 2026. Red: Haredi track 58.1%, reservists 45.7%, regular 6.9% — first-year leaving 10.6%, 8.2%, 8.3% (M). Red precision 12.5% against a base rate of 8.4%; it caught 36 of 187 later leavers (19%), and 30% of the year's leavers had already gone before the score existed (M). Drivers include "reserve-duty absence" and "medical or learning accommodation on file" from the accommodations module (M). Not in any inventory; no DPIA; the Tavla DPA (2022) predates it (`it/systems-and-contracts.csv`); the 2022 privacy notice says nothing about profiling (M). Ofer Sasson (R) left it on at the unit's request.

### F5 · The red list was shared openly (M) — escalated 7 February

288 students with names, numbers and reasons (38 with a medical or learning accommodation, 125 with reserve duty) shared on 16 March 2026 with 61 lecturers as an open link, forwarded to TAs, still open on 4 February 2027. Closed on 7 February; the DPO is assessing. Reported here, not decided here.

### F6 · Advising runs on the list, not on the procedure (M, R)

Procedure SS-03: 637 first-years eligible; 153 contacted (24%), 78 within the 14 days (12%). From 16 March, 53% of contacts came from the red list; 15% of red-list calls ended with the student objecting (`student-success/adviser-contacts-2025-26.csv`). Advisers cannot lift a block (R, Samah Khoury). Capacity about 150 meaningful contacts a week in peak weeks (R).

### F7 · The vendor's evidence does not transfer, and its terms are the risk (M, R)

85% = recall in the top 30% on one held-out cohort at one US community college; the +4.1 points coincided with a statewide free-tuition programme (case study, footnotes). Pilot terms: three years incl. accommodations flags and identifiers, US region, a licence to train on de-identified data that survives termination, 24 months' retention, automatic conversion (2.1, 4.2, 4.5, 4.7, 2.4). The CEO wrote "let's start on 1 March" and offered reference visits (M, e-mail of 24 January). No non-US customer (R, Noa Ben-Ami, 15 March — added at v1.1).

### F8 · Shadow AI is where the work is heaviest (M)

Survey (276): administrative 65.5% never use AI; adjuncts 10.7% never, 63.1% weekly or daily; 21 of 84 adjuncts enter student work with names or numbers into personal tools; 17 administrative staff enter student personal details. HR's "65% never" covers administrative staff only. Proxy: the lecturers' Wi-Fi is the largest AI user; student administration uses ChatGPT and translators. 120 office AI licences: 58 management, 3 in student administration; 39 never used, 35 used 8+ days in 30 (`it/office-ai-assistant-usage-2026-10.csv`).

### F9 · Detector scores are used as evidence (M, R)

19 of 46 integrity cases rest on an AI-detector score alone; 9 of the 19 students' first language is not Hebrew; 6 of 8 appeals overturned (M, `academic/integrity-cases-2025-26.csv`). The faculty guidance draft says detectors "may help"; it was never adopted.

### F10 · AI inside software nobody counts (M)

Admissions CRM "predictive score"; survey tool open-text summaries on by default, with no DPA; Tavla's AI quiz generator (off). Adjunct committee (R, letter): no AI to evaluate lecturers without agreement.

### F11 · The data joins only if you know how (M)

Finance exports student numbers as numbers: new-SIS numbers lose the leading zero. A naive join matches 1,906 of 6,128 accounts; padded to nine digits, all 6,128. Any vendor's "three years of data" would have been joined wrong.

## What I did not find

No evidence that teaching quality drives first-year leaving (not examined: out of scope). No evidence that Haredi or Arabic-speaking students leave more once blocks are accounted for (D; small groups).

## People protected

No adviser, lecturer, service-centre employee or student is named in this memo. The open sheet is described as a unit's practice, not one person's error; the fix is a setting and a rule.
