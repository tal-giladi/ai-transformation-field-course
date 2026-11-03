"""Company and policy documents (Tzurim Academic College data room).

Reading this spoils the capstone: submit your deliverables first.
"""
from __future__ import annotations

from gen_common import PROGRAMMES, write_md

NAMES = {p[0]: p[1] for p in PROGRAMMES}


def company(fig: dict) -> None:
    write_md("company/college-profile.md", """
# Tzurim Academic College — profile (January 2027)

*Prepared by the CEO's office for the consultant's onboarding. Translated from Hebrew.*

**Tzurim Academic College** (המכללה האקדמית צורים) is a private academic college in the southern Shfela, founded in 1996 and operated by a public benefit company (חל"צ). It is recognised by the Council for Higher Education and is **not budgeted** by the Planning and Budgeting Committee: tuition pays for almost everything.

| | |
|---|---|
| Students (October 2026) | 6,840 (first degree 6,110; MBA 730) |
| Staff | 712: 236 administrative, 148 senior faculty, 328 adjunct lecturers on semester contracts |
| Programmes | BA Business Administration, BA Behavioural Sciences, BSc Computer Science, BSc Industrial Engineering and Management, BA Communication, LLB Law, MBA |
| Tracks | Regular (day), evening (working students), Haredi track (separate classes, afternoon timetable, BA-BUS, BA-BEH, BSC-CS, LLB) |
| Revenue 2026 | ₪231.6M, of which tuition ₪211.9M; operating surplus ₪6.4M |
| Tuition 2025-26 (per year) | BA-BUS, BA-BEH ₪29,400; BA-COM ₪28,200; BSC-IEM ₪32,400; BSC-CS ₪33,600; LLB ₪36,800 |
| Languages | Students write to the college in Hebrew, Arabic, Russian and English; replies are in Hebrew unless a staff member speaks the language |

**Systems.** Rishum 2, the student information system (SIS), built in-house and live since August 2024 (the old SIS is read-only); the finance ERP (tuition accounts, payment plans, collections); Tavla LMS (courses, submissions, grade book, the accommodations module); the inquiry portal (in-house); an admissions CRM; the office suite with an AI assistant add-on since March 2026.

**Units you will meet.** Student administration and the registrar; the exams office; finance (collections desk); the Student Success unit (advisers) and the accessibility unit and reservist desk, under the Dean of Students; IT; admissions.

**Context.** Since October 2023 a large share of students have served long periods of reserve duty. The college runs a reservist desk and a reservist grant (see `policies/reservist-students-policy-2025-26.md`).
""")
    write_md("company/org-chart.md", """
# Organization chart (January 2027)

```
Board of directors — chair Dr. Eitan Rozen (finance committee: three directors)
│
├── President (academic head) — Prof. Hanna Levkovich
│     ├── Academic council (deans, heads of programme)
│     ├── Deans of the six programmes + MBA director
│     └── Disciplinary committee (students)
│
└── CEO — Yaron Bar-Lev
      ├── VP Finance — Avi Golan
      │     ├── Accounting and payroll
      │     └── Collections desk (2 staff): tuition accounts, payment arrangements, blocks
      ├── VP Administration — Tamar Weiss
      │     ├── Registrar and student administration — Galina Petrov (31 staff, incl. the service centre)
      │     ├── Exams office (6)
      │     ├── IT — Ofer Sasson, IT manager and appointed information security officer (11)
      │     └── BI analyst (1, reports to IT)
      ├── Dean of Students — Dr. Lior Amsalem
      │     ├── Student Success unit — Samah Khoury (head) + 6 advisers (one on long leave)
      │     ├── Accessibility unit (3)
      │     └── Reservist desk (2, since 2024)
      ├── Admissions and marketing
      └── HR
External: Data protection officer (DPO), Adv. Michal Peled-Ronen, part-time, appointed January 2026.
Student union (אגודת הסטודנטים): chair and welfare officer.
Adjunct lecturers' committee: chair Dr. Yonatan Mekonen.
```
""")
    rows = "\n".join(f"| {k} {NAMES[k]} | {n:,} | {pct}% |" for k, (n, pct) in fig["by_programme_2025"].items())
    write_md("company/dropout-report-2026-12.md", f"""
# Annual report: first-year dropout (December 2026)

*Registrar's office, prepared by the BI analyst for the CEO and the board. Translated from Hebrew.*

## Headline

First-year dropout has risen sharply since 2023.

| Cohort (entered October) | Students | First-year dropout |
|---|---|---|
| 2021 | 2,140 | 12.9% |
| 2022 | 2,105 | 12.6% |
| 2023 | {fig[2023][0]:,} | {fig[2023][1]}% |
| 2024 | {fig[2024][0]:,} | {fig[2024][1]}% |
| 2025 | {fig[2025][0]:,} | {fig[2025][1]}% |

## Cohort 2025 by programme

| Programme | Students | First-year dropout |
|---|---|---|
{rows}

## Notes

1. Dropout = students of the cohort whose status on 1 October after their first year is not 10, 21, 41 or 60 (query BI-07, written 2019, unchanged).
2. Source: Rishum 2 (cohorts 2024 and later) and the old SIS (earlier cohorts), status snapshot on 1 October.
3. The sector comparison the board asked for is not available for private colleges.
""")
    write_md("company/board-minutes-2027-01-20-extract.md", """
# Board of directors — strategy session, 20 January 2027 (extract)

*Approved minutes, item 3 of 6. Translated from Hebrew.*

**Present:** Dr. Eitan Rozen (chair), five directors; Yaron Bar-Lev (CEO); Prof. Hanna Levkovich (President); Avi Golan (VP Finance); Tamar Weiss (VP Administration). Minutes: the company secretary.

**Item 3 — Student retention and the 2027–2029 strategic plan**

The CEO presented the registrar's December report: first-year dropout of 19.5% (cohort 2024) and 17.7% (cohort 2025), against 12.2% for cohort 2023. Every point of dropout costs the college about two million shekels of tuition a year. Competitors are investing in "AI-based student success". The CEO met Persevia, a US company whose platform "identifies 85% of students who will leave, eight weeks before they do", at an EdTech conference in Tel Aviv in December. Persevia offers a free pilot from March on the college's data.

The CEO proposed a target: **first-year dropout of 12% by 2029**, with an AI early-warning system as its centrepiece.

Discussion:
- A director asked what it costs. The VP Finance: the 2027 budget has a new line, "Digital transformation and AI" (₪1.2M), with no approved content yet. Any commitment above ₪250,000 or longer than one year comes to the board.
- The President said the academic side has to be part of any decision that touches how students are assessed or contacted.
- The chair: "We want this, but we must not end up in the newspaper. Student data is sensitive. Check it properly."

**Decisions:**
1. The CEO will engage an outside consultant to review the retention problem and the AI options and to bring **one recommendation** to the board on **Tuesday 4 May 2027**, with costs, risks and dates.
2. Any pilot with an outside vendor that uses student data is subject to the DPO's review before data is shared.
3. The 12% target will be confirmed on 4 May, together with the plan.
""")
    write_md("company/budget-2027-extract.md", """
# Budget 2027 — extract (approved by the board, 15 December 2026)

*VP Finance. ₪ thousands.*

| Line | Item | 2026 actual | 2027 budget | Note |
|---|---|---|---|---|
| 4100 | Tuition revenue | 211,900 | 214,800 | Assumes first-year dropout returns to 2023 level |
| 5210 | Student Success unit (head, 6 advisers, programmes) | 2,790 | 2,860 | One adviser on long leave from Nov 2026 |
| 5230 | Accessibility unit | 1,040 | 1,080 | |
| 5240 | Reservist desk and reservist grants | 6,950 | 7,400 | Grants ₪6.1M (2026) |
| 5410 | Collections desk | 590 | 620 | 2 staff |
| 5420 | Bad-debt provision | 1,900 | 1,900 | 2022: 3,100 (before the automatic exam-registration block) |
| 6100 | IT operating | 9,800 | 10,100 | |
| 6150 | Office AI assistant add-on (120 licences) | 140 | 170 | Bought March 2026 |
| 6800-110 | **Digital transformation and AI** | — | **1,200** | New; content to be approved |

**Rules (finance procedure 2-04):** any commitment above ₪250,000 or longer than twelve months needs board approval; investments should pay back within three academic years; the VP Finance and the CEO release funds from line 6800-110 together.
""")


def policies() -> None:
    write_md("policies/academic-regulations-extract-2025-26.md", """
# Academic regulations 2025-26 (תקנון לימודים) — extract

*Approved by the academic council, July 2025. Translated from Hebrew.*

**4.2 Exam registration.** Students register for each exam period in Rishum 2 by the registration close date published in the academic calendar (semester A 2025-26: 11 January 2026; semester B: 14 June 2026). A student with a financial block may not register (see the tuition regulations, s. 7).

**4.3 Late registration.** After the close date a student may register up to three working days before an exam, for a fee of ₪150 per exam, provided no block is in place.

**4.4 Not registered.** A student who did not register for an exam receives no grade in that period. Moed B (the second sitting) is open to students who registered for moed A, or with the exams office's approval for exceptional reasons. Otherwise the course must be repeated.

**4.7 Accommodations.** Exam accommodations (extra time, a separate room, a reader) are approved by the accessibility unit on the basis of a diagnosis or a medical document. The accessibility unit records approved accommodations in Tavla's accommodations module so that lecturers can apply them.

**4.9 Reserve duty.** Special exam dates and extensions for students on reserve duty: see the reservist students policy.

**6.3 Generative AI in assignments.** The use of generative AI by students is governed by each course syllabus (academic council decision 12/2025). Where the syllabus is silent, AI may not be used to produce graded work.

**6.5 Suspected misconduct.** A lecturer who suspects misconduct refers the case to the disciplinary committee with the evidence. The student is heard before any decision.
""")
    write_md("policies/tuition-regulations-2025-26.md", """
# Tuition regulations 2025-26 — extract

*Finance department. Translated from Hebrew.*

**3. Payment.** Tuition is paid by standing order (10 monthly payments), by credit card in up to 10 payments, in one payment, or under an approved payment arrangement.

**5. Scholarships and grants.** Scholarships and grants are credited to the student's account when the finance department records the funding body's payment or the grant committee's approval. Reservist grants are credited after the reservist desk verifies the reserve days, in a monthly batch.

**7. Financial block.** On the block-check date (14 days before each exam period) the finance ERP automatically places a block on exam registration for any student whose outstanding balance exceeds ₪1,500. The block is lifted when the balance falls below ₪1,500 or a payment arrangement is approved. Blocks are lifted by the collections desk.

**8. Payment arrangements.** A student may ask for a payment arrangement by inquiry to the finance department. Requests are answered within ten working days.

**9. Leaving the college.** A student who stops studying must give written notice; tuition is charged until the notice date.
""")
    write_md("policies/reservist-students-policy-2025-26.md", """
# Support for students on reserve duty, 2025-26

*Dean of Students. Translated from Hebrew. Based on the Council for Higher Education's framework for reservist students and the college's own decisions.*

- **Reservist desk** (2 staff): one address for every request. Students upload the reserve-service confirmation.
- **Exams:** a special exam date for an exam missed during service; extensions for assignments.
- **Freezing studies:** a student called up for a long period may freeze studies without losing a place (status 47 in Rishum 2, introduced November 2024). Returning students keep their credits.
- **Reservist grant:** ₪5,000–₪9,000 a year by days served, credited to the tuition account after verification (see the tuition regulations, s. 5).
- **Advisers:** the Student Success unit offers an adviser meeting to every returning reservist.
""")
    write_md("policies/it-acceptable-use-2019.md", """
# Acceptable use of IT resources (2019)

*IT department. Version 1.3, approved by the CEO, March 2019. Translated from Hebrew.*

1. College computers, accounts and networks are for college work.
2. Do not install software that IT has not approved.
3. Student and staff information is confidential. Do not send it outside the college except as your role requires.
4. Passwords are personal. Do not share accounts.
5. Use of personal cloud storage for college files requires the IT manager's approval.
6. IT may monitor the use of college systems for security purposes.
7. Breaches are handled under the disciplinary procedures.
""")
    write_md("policies/faculty-ai-guidance-draft-2025-09.md", """
# Guidance for faculty on generative AI — DRAFT

*Prepared by a working group of the academic council, September 2025. Status: not adopted. In December 2025 the academic council decided to leave the use of AI by students to each course syllabus (decision 12/2025) and to return to faculty guidance "later".*

1. Lecturers may use generative AI tools to prepare course materials.
2. Avoid entering identifying details of students into public AI tools.
3. AI detectors may help identify suspected use of AI in assignments.
4. State in every syllabus whether students may use AI and how they must declare it.
5. The college will consider providing an approved tool.
""")
    write_md("policies/student-privacy-notice-2022.md", """
# Privacy notice for students (2022)

*Published on the student portal. Translated from Hebrew.*

Tzurim Academic College collects the personal information you give us when you apply and while you study (identity and contact details, academic record, payments, and any documents you submit for accommodations or grants). We use it to administer your studies, to teach and assess you, to provide student services, to collect tuition, and for internal statistics.

We share information with service providers who operate our systems for us, with authorities as the law requires, and with funding bodies for scholarships you applied for.

Information is kept for as long as required for academic records. You may ask to see the information about you by writing to student administration.
""")
    write_md("student-success/early-contact-procedure-2024.md", """
# Student Success — early-contact procedure (2024)

*Procedure SS-03, approved by the Dean of Students, September 2024. Translated from Hebrew.*

1. **Who.** Every first-year student who failed, or did not sit, two or more semester A exams.
2. **When.** An adviser contacts the student within 14 days of the publication of semester A grades.
3. **How.** Phone call; if no answer, an SMS and a second call within a week.
4. **What.** Ask how the student is doing; offer tutoring, a study plan, a referral to the accessibility unit or finance where relevant.
5. **Record.** Every contact is recorded in the contact log with the trigger "early_contact".
6. **Report.** The head of Student Success reports coverage to the Dean of Students at the end of March.
""")


def build(fig: dict) -> None:
    company(fig)
    policies()
