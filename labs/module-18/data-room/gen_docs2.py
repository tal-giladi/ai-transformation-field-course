"""Vendor, LMS, e-mail, people and finance documents (Tzurim Academic College data room).

Reading this spoils the capstone: submit your deliverables first.
"""
from __future__ import annotations

from gen_common import write_md


def vendor() -> None:
    write_md("vendor/persevia-proposal.md", """
# Persevia Student Success Cloud — proposal for Tzurim Academic College

*Persevia Inc., Austin, Texas. Sent by Noa Ben-Ami, Regional Account Executive, 28 December 2026.*

## Why Persevia

- **Predicts 85% of the students who will leave, on average eight weeks before they do.**
- Institutions using Persevia retain **3 to 5 percentage points more** first-year students.
- Advisers see one prioritised list every morning, with the reasons and a suggested action.
- Works with any SIS, ERP and LMS through a nightly export.

## Your return on investment

| | |
|---|---|
| First-year students | 2,310 |
| Students retained per year (5 points) | ≈ 120 |
| Tuition per student per year | ₪29,400 |
| Remaining years of study | 3 |
| **Tuition retained per year** | **≈ ₪10.6M** |

## Pricing (US$)

| Item | Price |
|---|---|
| Onboarding and integration (one-off) | $38,000 |
| Subscription | $9 per enrolled student per year, minimum 6,500 students ($58,500 a year) |
| Retention Desk module (case management for advisers, optional) | $22,000 a year |
| Term | 36 months, renews automatically for 12 months unless cancelled 90 days before the end |

## Free pilot, March–June 2027

We will run Persevia on your last three academic years of SIS, finance and LMS data at no cost, and present the at-risk list for your current students in April. The pilot converts to a subscription on 1 September 2027 unless cancelled 30 days before the pilot ends. See the pilot terms.

## Data

Hosted in Persevia's US cloud region (an EU region is available for a 15% surcharge). Data is encrypted in transit and at rest. SOC 2 Type II report available on request under NDA.
""")
    write_md("vendor/persevia-case-study.md", """
# Case study: a community college district in the US Midwest

*Persevia marketing, 2025. Name withheld at the customer's request.*

**The customer.** A community college district with about 38,000 students on four campuses; most students part-time; open admission.

**The challenge.** Fall-to-fall retention of first-time students had fallen to 51%.

**What they did.** From fall 2023 advisers worked from Persevia's daily risk list, built on attendance scans, LMS activity, financial-aid status and placement-test results.

**Results.**
- Fall-to-fall retention of first-time students rose from 51.0% (fall 2022 cohort) to 55.1% (fall 2023 cohort).
- Persevia's model identified 85% of students who left, on average eight weeks before they left.

*Footnotes.* (1) Recall measured on the held-out fall 2021 cohort: share of leavers who were in the top 30% of risk scores eight weeks before leaving. (2) Fall 2023 also saw the introduction of a statewide tuition-free community-college programme. (3) Results may vary.
""")
    write_md("vendor/persevia-pilot-terms.md", """
# Persevia pilot terms and data processing addendum — extract

*Sent with the proposal, 28 December 2026. Clause numbers as in the original.*

**2.1 Pilot data.** Customer will provide Persevia with SIS, finance and LMS extracts for the last three academic years for all enrolled and former students, including student identifiers sufficient to link records across systems, enrolment status, grades, payment status and balances, LMS activity, and accommodation and support flags where available.

**2.4 Conversion.** The pilot converts to a subscription under the proposal's pricing on the conversion date unless Customer cancels in writing at least 30 days before the end of the pilot.

**4.2 Processing location.** Customer Data is processed in Persevia's US region. Sub-processors are listed at persevia.example/subprocessors and may change on 30 days' notice.

**4.5 Model improvement.** Customer grants Persevia a non-exclusive licence to use Customer Data, after de-identification by Persevia, to improve and train Persevia's models and products for all customers. This licence survives termination.

**4.7 Retention.** Persevia retains Customer Data for 24 months after termination, then deletes it.

**6.1 Customer responsibilities.** Customer is responsible for providing all notices and obtaining all consents required by law for the processing of Customer Data by Persevia.
""")
    write_md("vendor/emails-ceo-persevia-2027-01.md", """
# E-mail thread: Persevia pilot (exported by the CEO's office, 3 February 2027)

**From:** Yaron Bar-Lev **To:** Noa Ben-Ami (Persevia) **Date:** Sun 24 Jan 2027, 21:40
Noa, great to meet you again in Tel Aviv. The board approved going ahead with a plan. We'd be proud to be the first Israeli college on Persevia, and happy to host visits from other colleges afterwards. Let's start the free pilot on 1 March. Ofer, our IT manager, will send you the data.

**From:** Noa Ben-Ami **To:** Yaron Bar-Lev **Cc:** Ofer Sasson **Date:** Mon 25 Jan 2027, 09:12
Wonderful news, Yaron! To start on 1 March we need the extract by 25 February: three years, all students, SIS (with ID numbers for matching), finance balances and blocks, LMS logs, and the accommodations flags — they are among our strongest predictors. I'll send the file specification today. The pilot terms are attached; a signature from you is enough.

**From:** Ofer Sasson **To:** Yaron Bar-Lev **Cc:** Tamar Weiss **Date:** Mon 25 Jan 2027, 11:03
We can produce it in about a week. Two questions before I do: the accommodations flags are medical and learning-disability information — do we need Michal (DPO) to look at this? And do we send ID numbers or our student numbers?

**From:** Yaron Bar-Lev **To:** Ofer Sasson **Cc:** Tamar Weiss **Date:** Mon 25 Jan 2027, 13:30
Let's not slow down. The consultant starts on 7 February and will look at it. Prepare the extract so we're ready.
""")


def lms_and_success() -> None:
    write_md("lms/tavla-release-notes-2026-2.md", """
# Tavla LMS — release 2026.2 (February 2026) — release notes extract

*Tavla Learning Ltd. Published to institution administrators, 9 February 2026.*

**New: Engagement Insights for every institution.** Engagement Insights gives each student a daily risk score (0–100) and a band (green, amber, red) with up to three drivers, so that student-success staff can reach out early. It is **enabled by default** for terms starting after 1 March 2026. Administrators can switch it off under *Settings → Insights*.

- Scores combine LMS activity (logins, time on task), submissions, forum participation and, where the Accommodations module is enabled, accommodation and absence signals.
- The model is trained on aggregated activity patterns across Tavla institutions.
- Scores and drivers can be exported to CSV and shared with staff roles you choose.

**Also in 2026.2:** AI quiz generator (opt-in, off by default); new grade-book filters; accessibility fixes.
""")
    write_md("student-success/emails-red-list-2026-03.md", """
# E-mail thread: Engagement Insights red list (exported for the consultant, 4 February 2027)

**From:** Samah Khoury **To:** first-year lecturers (distribution list, 61 recipients: 15 senior faculty, 46 adjunct lecturers) **Date:** Mon 16 Mar 2026, 08:05
Dear lecturers, Tavla now gives us a risk score for every first-year student. Here is the red list for your courses: [Google Sheet link]. The link is open to anyone with the link, so you don't need to log in. Please add a comment next to any student you are worried about. The advisers are calling everyone on the list over the coming weeks. Thank you! Samah

**From:** an adjunct lecturer (BA-BEH) **To:** Samah Khoury **Date:** Mon 16 Mar 2026, 10:41
Thanks. Is it OK that I can see the reason "medical or learning accommodation on file"? I didn't know some of these students had a diagnosis.

**From:** Samah Khoury **Date:** Mon 16 Mar 2026, 11:02
It's only for internal use, please don't share it.

**From:** an adjunct lecturer (BSC-CS) **Date:** Tue 17 Mar 2026, 19:20
Forwarded to my two TAs so they can keep an eye on these students in the labs.

**Note added by the VP Administration's assistant when assembling the data room, 4 February 2027:** the March link still opens without login; the sheet was last edited on 3 January 2027. The export of the sheet is `red-list-for-lecturers-2026-03-16.csv`.
""")
    write_md("inquiries/inquiry-routing.md", """
# Inquiry portal — categories and routing

*Student administration, 2024. Translated from Hebrew.*

The student picks a category when opening an inquiry. The portal routes it to a first unit by category. A unit that cannot resolve an inquiry reassigns it; the clock does not restart.

| Category (student's choice) | First unit |
|---|---|
| exams | exams office |
| finance | finance - collections |
| certificates | student administration |
| accommodations | accessibility unit |
| reserve duty | reservist desk |
| technical | IT helpdesk |
| academic | student administration |
| other | student administration |

**Student charter:** every inquiry is answered within five working days. Replies are written in Hebrew; English for international students.
""")


def people_and_finance() -> None:
    write_md("people/staff-ai-survey-2026-06-summary.md", """
# Staff survey on AI tools, June 2026 — summary

*HR, July 2026. Translated from Hebrew.*

276 staff answered (response rate 39%).

**Headline: 65% of staff never use AI tools** (n = 148). Faculty responses (senior faculty and adjunct lecturers) will be analysed separately with the academic side.

- Most common uses: writing e-mails and letters, summarising documents, Excel formulas.
- 86% do not know whether there are rules on AI at the college, or are not sure.
- Staff ask for training and for an approved tool.

**Recommendation:** extend the office AI assistant to more managers and run a training day in the autumn.

The raw responses are in `staff-ai-survey-2026-06-responses.csv`.
""")
    write_md("people/adjunct-committee-letter-2026-10-20.md", """
# Letter from the adjunct lecturers' committee

*20 October 2026. To: the CEO and the President. Translated from Hebrew.*

Dear Mr Bar-Lev, dear Prof. Levkovich,

The adjunct lecturers' committee asks for a meeting on AI at the college, before the college decides anything that affects our work.

1. **Workload.** An adjunct teaching three first-year courses marks 140 to 200 assignments a semester for the same pay. Lecturers are using AI tools on their own to keep up, with no guidance and no approved tool.
2. **Rules.** The academic council left AI to each syllabus. Lecturers do not know what they may put into which tool, or whether an AI detector's score may be used as evidence against a student.
3. **Evaluation of lecturers.** We have heard that course-evaluation comments are now summarised by AI. We ask that no AI tool be used to evaluate lecturers' teaching or to decide on contracts without agreement.
4. **Training.** Any training on AI should be paid time.

We are not against AI. We are against deciding about it without us.

Dr. Yonatan Mekonen, chair, on behalf of the committee
""")
    write_md("finance/collections-memo-2023-09.md", """
# Memo: automatic exam-registration block

*From: Avi Golan, VP Finance. To: management. 4 September 2023. Translated from Hebrew.*

From semester A 2023-24 the finance ERP will block exam registration automatically for any student whose balance exceeds ₪1,500 on the block-check date. Until now blocks were placed by hand and inconsistently, and bad debt reached ₪3.1M in 2022.

Expected effect: bad debt down by more than ₪1M a year; collections desk time freed from chasing.

Students will be told in the tuition regulations and by SMS before the check date. Students with a scholarship or grant in process should make sure it is recorded in time.

*Handwritten note added October 2026 (scanned):* "Bad debt 2025-26 ₪1.9M. Works. — A.G."
""")


def build() -> None:
    vendor()
    lms_and_success()
    people_and_finance()
