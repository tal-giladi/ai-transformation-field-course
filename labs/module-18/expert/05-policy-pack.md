# 05 · Policy pack

*Expert deliverable. Drafted 14–25 March 2027 with Tamar Weiss, Ofer Sasson and the DPO (Adv. Michal Peled-Ronen); academic parts with Prof. Hanna Levkovich; consulted with the adjunct committee on 23 March. Adopted by management 18 May 2027 (see `09`). Legal readings are the DPO's and counsel's, not the consultant's.*

## 1. AI inventory (v1.0, 25 March 2027)

| # | System / use | Kind | Where it runs | Data | Decides or shapes | Owner | Status |
|---|---|---|---|---|---|---|---|
| 1 | Tavla Engagement Insights | Prediction inside SaaS, on by default since 2026.2 | Vendor, EU | LMS activity, submissions, accommodations and absence signals | Which students advisers call | Dean of Students | Outreach use paused 18 Mar; DPIA open |
| 2 | Red-list sheet (export of #1) | Copy of #1 | Personal cloud sheet | Names, numbers, reasons | Lecturers' view of students | Dean of Students | Closed 7 Feb; DPO assessing |
| 3 | Admissions CRM "predictive score" | Prediction inside SaaS | Vendor, US | Applicant data | Which applicants are called first | Head of admissions | DPO review by June |
| 4 | Survey tool open-text summaries | Generative AI inside SaaS, on by default | Vendor, US; no DPA | Course-evaluation comments | Summaries read by heads of programme | Quality unit | Switched off 25 Mar until DPA and agreement with adjuncts |
| 5 | Office AI assistant add-on | Generative assistant | Vendor cloud, college tenant | Staff documents and mail | Drafts | IT | 120 licences; 40 to be reallocated |
| 6 | Office suite's included chat assistant | Generative assistant | College tenant, data terms | Staff prompts | Drafts | IT | Approved tool for all staff from May |
| 7 | Public AI tools on personal accounts | Shadow | Vendors | Incl. student work and personal details | Feedback, translation, drafts | — | Restricted (see 3) |
| 8 | AI-writing detectors (free web) | Classification | Vendors | Student assignments | Misconduct referrals | — | Not evidence (academic council 25 May) |
| 9 | Persevia (proposed) | Prediction platform | Vendor, US | Three years of student data | Outreach | CEO | Not yet; re-decide March 2028 |
| 10 | Inquiry triage and drafting pilot (proposed) | Generative assist | College tenant | Inquiry text, student number | Routing and draft; staff send | Registrar | Pilot, `06` |

The capability view (what the college can do with AI) and the legal register (`9` below) are kept separately.

## 2. Acceptable-use policy (one page, summary)

1. Use the approved tools (#6, and #5 where licensed) for college work. Public tools on personal accounts may be used only for material with no personal data and nothing confidential.
2. Never enter into any AI tool: national ID numbers, health or disability information, reserve-duty details, disciplinary matters, or a student's work together with the student's name or number — except in a tool and use the DPO has approved for that data.
3. A human reads, checks and owns everything an AI drafts before it reaches a student. Say "drafted with AI assistance" where the college's template asks for it.
4. No AI output may decide or be the only evidence for any decision about a student (admission, grade, misconduct, status, money).
5. AI-detector scores are not evidence of misconduct (academic council decision, 25 May 2027).
6. No AI tool may be used to evaluate a lecturer's teaching or to decide on contracts without agreement with the adjunct committee and the senior staff.
7. New AI tools and AI features that arrive in existing software go through the intake register (`8` below) before use.
8. Questions: your manager; data questions to the DPO; incidents to IT the same day.

## 3. Approved and restricted uses (excerpt)

| Use | Status | Condition |
|---|---|---|
| Drafting course materials with the approved tool | Approved | No student data |
| Feedback on assignments with the approved tool | Approved with conditions | Remove names and numbers; lecturer edits; students told in the syllabus |
| Translating a student's inquiry and drafting a reply | Approved in the pilot only | Pilot workflow, staff send |
| Summarising course evaluations | Restricted | Only after agreement with the adjunct committee and a DPA |
| Risk scores for outreach | Restricted | Only after the DPIA and the gates in `04` |
| Detector scores in misconduct cases | Prohibited as evidence | May prompt a conversation, never a referral alone |

## 4. Tools and data classes

| Data class | Examples | Approved tool (#6) | Pilot (#10) | Public tools |
|---|---|---|---|---|
| Public | Regulations, course descriptions | Yes | Yes | Yes |
| Internal | Procedures, timetables | Yes | Yes | No |
| Student personal | Name, number, grades, balances, inquiry text | Only as the role requires | Yes (number and text only) | No |
| Sensitive | Health, disability, accommodations, reserve duty, discipline | No | No (routed to a person) | No |
| Identifiers | National ID numbers | No | No | No |

## 5. Vendor read-back

| Claim or term | What it means | What we accept |
|---|---|---|
| "85% of leavers, eight weeks early" (Persevia) | Recall in the top 30% band, one US college, one held-out cohort | Not as evidence for Tzurim |
| "+3–5 points retention" | Before-after in a year with a statewide free-tuition programme | Not as evidence |
| Pilot data: three years incl. accommodations and identifiers | Health data and identifiers to a US region | No |
| 4.5 Training licence surviving termination | Our students' data improves other customers' models | No |
| 2.4 Automatic conversion; 36 months with renewal | Board rule: no commitments > 12 months without the board | No |
| Tavla 2026.2 "enabled by default" | A new processing purpose under a 2022 DPA | Paused; DPA addendum and DPIA required |

## 6. DPIA summary — Tavla Engagement Insights (DPO, draft 8 April 2027)

Purpose: identify first-year students for adviser outreach. Data: LMS activity, submissions, accommodations and absence signals. Necessity: not shown — the main exit (blocks) is not visible to the score. Proportionality: sensitive drivers not necessary. Fairness: Haredi-track and reservist students flagged 5–8× more without higher leaving (`02`, F4). Transparency: none (2022 notice). Security: export shared openly (#2). **DPO's conclusion:** outreach use stays paused; re-assess in December 2027 if the drivers from the accommodations module are removed, a fairness test passes, the notice is updated and the DPA is amended.

## 7. Risk register (top 8)

| Risk | Likelihood / impact | Control | Tested? | Owner |
|---|---|---|---|---|
| Sensitive student data shared beyond need (lists, exports) | High / high | Sharing settings restricted; exports of #1 disabled; AUP 2 | Yes: 7 Feb link test; IT re-check monthly | IT |
| Student data to a vendor abroad without basis | Medium / high | Intake register; DPO sign-off; board decision 2 | Yes: Persevia extract held | DPO |
| A score treated as a judgment about a student | Medium / high | AUP 4; outreach paused | Partly | Dean of Students |
| Detector-only misconduct findings | High / medium | Academic council rule | From 25 May | President |
| Inquiry drafts with wrong information sent to students | Medium / medium | Staff send; gates; negative tests | Yes, `06` | Registrar |
| Fast lane raises bad debt | Low / medium | Block kept for arrears; gate | June 2027 | VP Finance |
| Lecturers see new rules as surveillance | Medium / medium | Consultation; no usage monitoring of individuals | 23 Mar meeting | HR |
| AI features arriving in SaaS updates unseen | High / medium | Release-note review in the intake register | Monthly | IT |

## 8. Governance charter (short) and intake register

**Purpose:** decide which AI uses run at Tzurim and keep them safe. **Members:** VP Administration (chair), Dean of Students, a dean named by the President, IT manager, DPO (advisory), a representative of the adjunct committee (for uses that affect lecturers). **Decides:** intake, tiering, pauses; the board decides spend above ₪250,000 or longer than 12 months. **Cadence:** monthly, 45 minutes; intake within two weeks. **Three numbers for the board each semester:** uses in production, median days from intake to decision, uses declined and why. **Link:** the risk register feeds the board's audit committee.

**Intake register fields:** owner; what it does; where it runs; data classes touched; whether it decides or shapes anything about a student or lecturer; vendor terms (training, region, retention); overlaps with existing tools; DPIA needed (yes/no and why); decision and date.

## 9. Regulatory map (Israel first)

| Instrument | Why it reaches Tzurim | Actor | What to do | Check with |
|---|---|---|---|---|
| Privacy Protection Law, 5741-1981, incl. Amendment 13 (in force August 2025) | Student and staff databases; profiling; DPO duty; notice | Database controller | Notice update; DPIA practice; DPO involvement | DPO |
| Privacy Protection (Data Security) Regulations, 5777-2017 | Security level of student databases; access control; incidents | Controller, security officer | Access to exports; incident procedure for #2 | IT, DPO |
| Privacy Protection (Transfer of Data to Databases Abroad) Regulations, 5761-2001 | Vendor clouds in the US and EU | Controller | Basis for any transfer; vendor terms | DPO |
| PPA draft guidance on AI (April 2025) | Transparency, management responsibility, DPIA for AI | Controller | Follow as good practice | DPO |
| Student Rights Law, 5767-2007 (חוק זכויות הסטודנט) | s. 4: no discrimination by origin, religion, residence and other grounds in admission and tracks; s. 19A: accommodations for students on reserve duty | Institution | Fairness test before any score is used on students; reservist accommodations and grant timing | Counsel |
| Council for Higher Education frameworks (reservist students) | Reservist support the college implements | Institution | Grant timing, special dates | Dean of Students |
| EU GDPR / AI Act | Only for EU students or EU-market products; Annex III lists education uses as high-risk for providers and deployers in the EU | — | Not applicable today; note for any EU programme | Counsel |
