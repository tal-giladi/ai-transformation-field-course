# 03 · Readiness assessment

*Expert deliverable. Thursday 11 March 2027. The bar for an AI early-warning system was written on 1 March, before the vendor call on 15 March. Every line is dated and marked **verified** (seen in data or documents) or **reported** (told by a role).*

## The bar for a student risk score (written 1 March 2027)

A risk score that triggers contact with students may be used at Tzurim when all of these hold:

1. **Outcome label:** "left the college" defined and signed by its owner, separate from freezes and transfers.
2. **History:** two or more cohorts with that label, joinable across SIS, finance and LMS without loss.
3. **Lever:** for the main reasons students leave, the college can act after a flag (advisers or units can change the outcome).
4. **Capacity:** the flagged volume fits adviser capacity at peak.
5. **Fairness:** flag rates and precision per track, language and reservist status tested before use; no group flagged at more than 1.5× its leaving-rate ratio without a reason.
6. **Lawful basis and transparency:** DPIA done; students told; sensitive data (health, reserve duty) excluded unless the DPO approves a need.
7. **Data boundary:** no identifiable student data leaves Israel or the EU; no vendor training rights.

## Dimensions

| Dimension | Evidence | Status | Verified / reported, date | Consequence | Owner |
|---|---|---|---|---|---|
| Outcome definition | BI-07 counts 47 and 33; no signed definition | Not met | Verified 9 Feb | No AI can learn "dropout" from this label | Registrar |
| History and joins | Three cohorts in the extract; join loses 69% of accounts unless padded | Met with a fix | Verified 10 Feb | Fixable in a day; must be in any extract spec | IT (BI analyst) |
| Lever | 45% of first-year leavers missed registration through a block; advisers cannot lift blocks | Not met for a list; met for a process fix | Verified 18 Feb; reported (Samah) 9 Feb | A list without the lever adds calls, not students | VP Finance, Dean of Students |
| Capacity | ~150 meaningful contacts a week at peak; Tavla flagged 288 red + 722 amber in one cohort | Partly met | Reported 9 Feb; verified 18 Feb | Any list must be capped and ranked | Head of Student Success |
| Fairness | Tavla: Haredi 58% red, reservists 46%, regular 7%, similar leaving | Not met | Verified 18 Feb | Stop use for outreach until fixed | Dean of Students, DPO |
| Lawful basis, transparency | No DPIA, 2022 notice, accommodations in drivers, open sheet | Not met | Verified 7–18 Feb | DPO's assessment; notice before any use | DPO |
| Data boundary | Persevia: US region, training licence | Not met | Verified 7 Feb (terms); reported 15 Mar (Noa) | Terms unacceptable as written | CEO, DPO |
| Inquiry data for a pilot | 2,669 inquiries with text, resolving unit, dates, reply language; four languages | Met | Verified 18 Feb | Ready for a routing-and-drafting pilot | Registrar |
| Governance | 2019 IT policy; faculty draft not adopted; no inventory | Not met | Verified 7 Feb | Week-two guardrails needed | VP Administration |
| People | Adjunct committee asks for consultation; staff want an approved tool | Met as willingness | Reported 15 Feb (Yonatan), survey verified | Consultation before rules | HR, President |

## Verdict per use

| Use | Verdict | What would change it | Re-decision |
|---|---|---|---|
| Vendor early-warning system (Persevia) | **Not yet** | Criteria 1–7 met; a proof of concept on de-identified Tzurim data, EU or Israel region, no training licence, compared with a simple rule | March 2028 |
| Tavla Engagement Insights for outreach | **Stop now** (pause the outreach use; keep scores invisible to staff) | DPIA; sensitive drivers removed; fairness test passed; notice | December 2027 earliest |
| Rule-based alert to advisers (first-year blocked at the check date; missed two exams) | **Proceed** | — | Review after June 2027 check |
| Inquiry triage and drafting assistant (staff send) | **Proceed to pilot** with gates | Gates in `06` | Shadow from 9 May |
| Staff use of an approved general assistant | **Proceed** with the policy pack | — | Review September 2027 |
