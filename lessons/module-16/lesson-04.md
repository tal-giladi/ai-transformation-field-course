---
id: "16.4"
module: 16
minutes: 22
practice_minutes: 120
prerequisites: ["16.3", "04.1", "04.2", "04.3", "04.4", "04.6"]
objectives:
  - "Decide, step by step, which parts of the method shrink to an hour in a four-week pro bono engagement and which keep their full weight."
  - "Map which Israeli privacy rules apply to a 30-person amuta holding health and welfare data, which do not, and which questions go to counsel."
  - "Verify free and nonprofit AI offers against the vendors' own pages, with dates, and choose the default tool."
  - "Write a data boundary per data class and tool, and an access fix the part-time IT person can do in one afternoon."
volatility: implementation
sources:
  - title: "Pearl Cohen, The Knesset enacts a comprehensive amendment to the Privacy Protection Law (Amendment 13: registration, notification, DPO, highly sensitive information)"
    url: https://www.pearlcohen.com/the-knesset-enacts-a-comprehensive-amendment-to-the-privacy-protection-law/
  - title: "Chambers Practice Guides, Data Protection & Privacy 2026: Israel (security levels, DPO categories, fines)"
    url: https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel
  - title: "Arnon, Tadmor-Levy, PPA publishes final guidance on the DPO appointment obligation under Amendment 13 (15 July 2026)"
    url: https://arnontl.com/news/ppa-publishes-final-guidance-on-the-dpo-appointment-obligation-under-amendment-13/
  - title: "Privacy Protection Authority, Privacy Protection (Data Security) Regulations, 5777-2017, English translation (First and Second Schedules)"
    url: https://www.gov.il/BlobFolder/legalinfo/data_security_regulation/en/5777%E2%80%932017.pdf
  - title: "Privacy Protection (Data Security) Regulations, Hebrew text (First Schedule item 2: \"אחד מאלה\")"
    url: https://dpoisrael.com/law/security-regulations/
  - title: "Social Workers Law, 5756-1996, English translation (IFSW): section 8, professional confidentiality"
    url: https://www.ifsw.org/wp-content/uploads/2021/03/Social-Workers-Law-1996-Israel.pdf
  - title: "Pearl Cohen, Israel: new draft guidelines on the application of privacy law to AI (PPA draft, consultation to 5 June 2025)"
    url: https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/
  - title: "Barnea Jaffa Lande, digital reporting of donations by Section 46 institutions from 1 January 2026 (13 November 2025)"
    url: https://barlaw.co.il/?p=61405
  - title: "Google for Nonprofits, eligibility guidelines (Israel: amuta, amuta with certificate of proper management, and other forms)"
    url: https://support.google.com/nonprofits/answer/3215869?hl=en
  - title: "Google for Nonprofits, AI features included in Google Workspace for Nonprofits"
    url: https://support.google.com/nonprofits/answer/16345471?hl=en
  - title: "Google Workspace, upgrade from Workspace for Nonprofits: discounts (updated 26 October 2026)"
    url: https://knowledge.workspace.google.com/admin/billing/upgrade-from-google-workspace-for-nonprofits
  - title: "Google Workspace, Generative AI in Google Workspace Privacy Hub (updated 6 October 2026)"
    url: https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub
  - title: "Google, Gemini Apps Privacy Hub (personal accounts, updated 26 October 2026)"
    url: https://support.google.com/gemini/answer/13594961
  - title: "Microsoft, Technology and software grants and discounts for nonprofits"
    url: https://www.microsoft.com/en-us/nonprofits/offers-for-nonprofits
  - title: "Goodstack, OpenAI nonprofit discount (ChatGPT Business US$8/user/month annual)"
    url: https://goodstack.org/software-discounts/openai
  - title: "Anthropic, Claude for Nonprofits (2 December 2025)"
    url: https://www.anthropic.com/news/claude-for-nonprofits
  - title: "Anthropic Academy, Getting started with Claude for nonprofits (eligibility, Goodstack)"
    url: https://academy.claude.com/tutorials/getting-started-with-claude-for-nonprofits
last_verified: "2026-11-03"
---

# 16.4 · The hard part: four weeks, no budget, sensitive data

This is the lesson the engagement is about. You have 40 hours, no money, one person who does IT on Tuesdays, and data about disabled children, their health and their families' welfare. You cannot run the method at full size, and you cannot skip the parts that protect the families. In this lesson you decide which steps shrink to an hour and which keep their weight, read which privacy rules apply to a small amuta, verify the free and nonprofit AI offers against the vendors' own pages, write the data boundary, and do the access fix with Yossi in one afternoon. At the end you have a compression table, a one-page legal map with questions for counsel, a verified offers table, a data boundary and Yossi's checklist, done.

## The situation

Week 2, Tuesday 24 November 2026, 13:00, Open Hands' office. Yossi closed the respite link last Wednesday after Amir confirmed this weekend's volunteers. This afternoon is the only half-day you have with him and the admin console. Tomorrow Ronit calls the funder; on Thursday you have two hours with Mahut's volunteer lawyer. Staff are still using personal accounts, because nobody has given them anything else.

Module 4 built the full policy pack ([04.1](../module-04/lesson-01.md)–[04.7](../module-04/lesson-07.md)): ten documents for a 120-person company. Open Hands needs the same protection on one page, and the same law, read for a 30-person amuta. IBM's governance course talks about proportionate, *tiered* control; here you find out what proportionate means when the data is the most sensitive there is and the organization is the smallest in the course.

## What to do

### Step 1 — Compress the method, and write down what you will not compress

Go through the Stage 1 method and give every step its size here. The full table is in the expert's paper; the shape of it is this:

| Step (field kit) | At Harbor & Pine | At Open Hands | What you still cannot skip |
|---|---|---|---|
| Charter, scope ([01.1](../module-01/lesson-01.md)–[01.3](../module-01/lesson-03.md)) | 2–3 days, a SOW | 1 page, 1 hour | The urgent-finding rule, "safely first" |
| Shadow-AI census ([01.6](../module-01/lesson-06.md)) | Survey, logs, expenses | Ronit's form, the card statement, 20 minutes at the staff meeting | Asking how people work, under non-attribution; the volunteers |
| Interviews ([02.2](../module-02/lesson-02.md)) | 10–15 × 60 min | 7 × 30 min | The frontline worker, the volunteer, **the person affected** |
| Baseline ([02.4](../module-02/lesson-04.md)) | Exports from three systems | One logged week + one scheduled | Saying the week is a peak |
| Portfolio, ROI ([03.3](../module-03/lesson-03.md), [03.7](../module-03/lesson-07.md)) | Workshop, model, NPV | One table, hours | The data gate; the "no AI" candidate |
| Policy pack ([04.1](../module-04/lesson-01.md)–[04.7](../module-04/lesson-07.md)) | 10 documents | One page | The boundary per data class and tool |
| Vendor review ([04.3](../module-04/lesson-03.md)) | Questionnaire, 3 vendors | The terms page of each tool in use, 1 hour | The training-on-content clause and the conversion date |
| DPIA ([04.4](../module-04/lesson-04.md)) | Full template | Half a page per workflow + counsel | Asking a lawyer the questions in Step 2 |
| Pilot and eval ([05.1](../module-05/lesson-01.md)–[05.4](../module-05/lesson-04.md)) | 2,000 items, harness | 10 + 12 items, 9 negative tests, rated by users | Thresholds before the run; negative tests |
| Training ([06.2](../module-06/lesson-02.md)) | Session plan | One 45-minute staff meeting | The sanctioned alternative on the same day as any "stop" |
| Handover ([07.9](../module-07/lesson-09.md)) | Binder, operating rhythm | 15 minutes a month for Yossi | A named owner who can do it without you |

**The rule behind it: documents shrink; contact with the people and the data does not.** Every step that touches who can see what, what goes into which tool, and how the affected family is treated keeps its full weight. Every step that produces a document for a reader who does not exist at a 30-person nonprofit (a scoring rubric, an NPV, a governance charter in six parts) shrinks to a table or a line.

### Step 2 — Read which law applies to a small amuta, and route the rest

Size does not switch privacy law off. Read it in three columns — applies, does not apply, open — and send the open column to counsel. This is not legal advice; it is the map you bring to the lawyer so two hours are enough.

**The Privacy Protection Law, 5741-1981** (חוק הגנת הפרטיות), as amended by Amendment 13 (in force 14 August 2025), applies in full. No exemption for nonprofits or small organizations appears in the summaries checked (Pearl Cohen; Chambers 2026). What Amendment 13 changed that matters here:

- **Registration** of databases was narrowed to databases whose main purpose is providing data to others commercially, and to public bodies (Pearl Cohen). Open Hands' 2019 policy still cites a registration number. Probably no longer required — **counsel to confirm** before anyone edits the policy.
- **Notification** to the Privacy Protection Authority applies to databases with highly sensitive information about more than 100,000 people. About 440 families: **not applicable**.
- **A privacy protection officer (DPO)** must be appointed by public bodies *and entities processing information on their behalf*, data brokers, and organizations whose core activities include large-scale processing of highly sensitive information. The PPA's final guidance (15 July 2026) set **no fixed number** for "large scale" (Arnon, Tadmor-Levy). Open Hands processes referral data for the Kiryat Hadas municipality under a service agreement, and its core activity is sensitive data. **Open: counsel.**
- **Administrative fines** are much larger than before; the Chambers guide describes fines of up to hundreds of thousands of shekels per security violation and more for governance violations.

**The Privacy Protection (Data Security) Regulations, 5777-2017** (תקנות הגנת הפרטיות (אבטחת מידע)) apply. Their First Schedule puts a database with "medical information or information regarding the person's mental condition" at the **medium** security level — but item 2 adds that a database meeting *one of* two conditions is at the **basic** level instead, the second being that "there are no more than ten users authorized by the database controller" (the PPA's English translation; the Hebrew text reads "אחד מאלה", one of these). Today the `Families` drive has 46 authorized accounts; 9 roles need it. Bringing it to 9 is good practice whatever the answer, and it may change the security level and with it the duties (procedures, audits, incident reporting). **Whether the count and the reading hold is counsel's call, not yours.** Do not tell the board "we are now at basic level".

**The Social Workers Law, 5756-1996** (חוק העובדים הסוציאליים), section 8, binds the coordinators to professional confidentiality: information received in professional work may be disclosed only with the person's written consent after its meaning was explained, or in listed exceptions. Whether pasting de-identified text into the organization's own Workspace AI is a "disclosure" is a question for counsel; whether pasting identifiable notes into a personal consumer account is a problem is not a hard question.

**The Kiryat Hadas service agreement**, §7, binds Open Hands by contract: referral information used only for the service, no transfer to third parties without the municipality's written approval, security according to the Regulations, incidents reported within 24 hours.

**The PPA's draft guidance on AI** (April 2025, consultation to 5 June 2025; still a draft per the course's reference list) says the same law applies across the AI lifecycle: transparency about AI processing, management responsibility, a policy for generative AI use, DPIAs. Treat it as the regulator's view of good practice.

**Context, not AI rules:** since 1 January 2026 Section 46 institutions report donations through the Tax Authority's digital system, with the donor's ID number on each receipt (Barnea Jaffa Lande) — which is why the donor sheet holds 851 ID numbers and why they must live somewhere narrower than a sheet 14 people can edit. Government support depends on the Registrar of Amutot's certificate of proper management; it explains the treasurer's dislike of surprises.

Write the open questions for the lawyer as yes/no questions where you can. Five are enough for two hours (see the reference answer).

### Step 3 — Verify the free and cheap offers on the vendors' own pages

Yossi's notes say "Gemini is not included for nonprofits" (2023) and "TechSoup Israel gives donated software" (2022). Noa says "ChatGPT Business is eight dollars a seat". All three are claims to test, and nonprofit offers change every year. Check each against the vendor's own page and write the date. Checked on 3 November 2026:

| Offer | What the vendor's page says | What it means for Open Hands |
|---|---|---|
| **Google Workspace for Nonprofits** | Israel is eligible (amuta, amuta with a certificate of proper management, and other forms; verification by Goodstack). No cost; the **Gemini app and NotebookLM** included. **Gemini inside Gmail and Docs is not** in the no-cost plan. Paid editions 70–75%+ off | Open Hands already has it. The default tool costs nothing and is already where the files are |
| **Workspace data terms** | Customer data not used to train models without permission; Gemini app chats and NotebookLM content not reviewed by humans, for qualifying editions | The same Gemini on a **personal** account: activity may train models, some chats reviewed by people and kept up to three years |
| **Microsoft 365 nonprofit** | Business Basic free to 300 users (web apps, Copilot Chat); Business Premium US$5.50/user/month paid yearly; Copilot add-on US$25.50 | Keep 3 Premium seats for desktop Office; the grant Yossi remembers no longer exists |
| **ChatGPT Business (nonprofit)** | US$8/user/month annual (US$10 monthly) via Goodstack (Goodstack's page; OpenAI's help page refused the checker — check it yourself) | A later option for 2 development seats: ₪602 a year |
| **Claude for Nonprofits** | Up to 75% off Team and Enterprise (2 December 2025); Goodstack; government, higher education and healthcare systems excluded | The same later option, from another vendor |
| **TechSoup Israel** | No current Israeli partner found (a 2019 network list named the Rashi Foundation) | Ask Mahut; do not plan on it |
| **GrantGenie** (fictional) | Free until 31 December, then US$49 a month automatically; a licence to train on uploaded content; US storage | Cancel and request deletion |

Three habits make this check reliable in an hour: open the **eligibility page for your country**, not the marketing page; find **what is not included** in the free plan (it is usually the feature people assume); and read the **conversion date and the content licence** of every "free for nonprofits" offer.

### Step 4 — Write the data boundary

Use the [data boundary](../../templates/data-boundary.md) and [tools and data classes](../../templates/tools-and-data-classes.md) templates from [04.2](../module-04/lesson-02.md), shrunk to one table. Classes come from the data room; tools from Step 3:

| Data class | Examples | Personal accounts | Open Hands Workspace (Gemini app, NotebookLM) | Paid nonprofit seats (later) |
|---|---|---|---|---|
| **R1 Family — identifiable** | Case notes as written, referral forms, care sheets, the case register, names, IDs, phones, towns with diagnoses, welfare status | No | **No** — stays in `Families` | No |
| **R2 Donor — personal** | The donor sheet, ID numbers, amounts, notes | No | No | No — a mail merge does it |
| **A1 Family — de-identified** | A note rewritten with roles ("the mother", "the child (8)"), no names, places, schools, hospitals, named diagnoses | No | **Coordinators and Hana only, case-note helper only** | Not decided |
| **A2 Consented stories** | Texts approved by the family (consent v2, Part B) | No | Yes | Yes |
| **G1 Organizational** | Boilerplate, outcomes framework, aggregated numbers, budgets | No | Yes | Yes |
| **G2 Public** | Website, published reports | Yes | Yes | Yes |

Three rules carry most of the weight, and they become the first lines of the policy page in 16.5: **work happens on work accounts; identifiable family and donor data never goes into AI; anything that leaves Open Hands is read and signed by a person.**

Why R1 stays out of AI even on the organization's own account, for now: three open counsel questions (security level, the municipal agreement's no-transfer clause, social workers' confidentiality) and the fact that the case-notes job can be done on de-identified text. When counsel answers, the boundary may widen. Write the condition down so it does not widen by habit.

### Step 5 — Fix access with Yossi in one afternoon, and give the alternative the same day

A "stop" without an alternative fails in a week, because the Adler-Haddad report is still due. Do both on the same afternoon. The checklist, sized to four hours, each item with who decides:

1. **Respite care sheets** (link closed last week): shared only with the next two weekends' volunteers on Amir's list. From December Amir prints one sheet per child and collects them after the weekend. *Decides: Ronit, Amir.*
2. **`Families`**: remove the 31 personal accounts, the 2 national-service volunteers and the 2 former staff; Ronit and the hotline worker move to the `Intake` folder only. Result: 9 accounts. *Decides: Hana.*
3. **Former staff**: suspend both Workspace accounts; transfer their files. *Yossi.*
4. **Donor sheet**: domain-wide link off; four editors; the treasurer as viewer on an organization account; ID numbers in a separate sheet only the bookkeeper and Noa can open; Noa cleans the notes column by 1 December. *Decides: Noa, Ronit.*
5. **Second super-admin**: Galina; recovery codes printed, in the safe, checked by Ronit. *Ronit.*
6. **Subscriptions**: Microsoft down to 3 seats (ask for a credit); Dropbox cancelled; GrantGenie cancelled with a deletion request. *Vova approved on the phone.*
7. **The alternative, today**: the Gemini app and NotebookLM on everyone's organization account (already included), with a one-line message from Ronit (see the reference answer).
8. **The monthly check** (first Tuesday, 15 minutes): the questions are in 16.6.

Do it together, in Hebrew, with Yossi's hands on the keyboard and yours on the list (persona: [Yossi Mizrahi](../../labs/module-16/personas/yossi-operations-it.md)). He will run it after you leave only if he did it himself.

### Step 6 — Design for one person who does IT on Tuesdays

Every choice in this lesson passes one test: **can Yossi keep it running in 15 minutes a month, and can somebody else do it if he is away?** That rules out a workflow with three connected services, a custom script on someone's laptop, or a paid tool only one person administers. It rules in: the tools Open Hands already has, instructions kept as text with a version line, a second administrator, a checklist on one page. The single point of failure you found in discovery (one admin, 2FA on a personal phone) is fixed in item 5 before anything new is built.

## Watch out

- **"We're small, so the law is light."** Size changed nothing found in the summaries; the number of authorized users might change the security level. Ask counsel; don't announce it.
- **Calling a free plan "safe" because it is free for nonprofits.** GrantGenie is free for nonprofits too. Read who may train on what you upload.
- **Assuming the free Workspace plan has everything.** Gemini in Gmail and Docs is not included; the Gemini app and NotebookLM are. Design for what is there.
- **Stopping without an alternative.** People who must deliver a report on the 15th will go back to their personal accounts by the 10th.
- **Fixing access alone.** If you change settings while Yossi watches, he will not hold the line when the next volunteer asks for access.
- **Compressing the people out.** The one step that never shrinks is talking to those who do the work and those it affects.

## Your turn

### Inputs

- Data room (module download): [`it/drive-sharing-audit.csv`](../../labs/module-16/data-room/it/drive-sharing-audit.csv), [`it/accounts-and-licences.csv`](../../labs/module-16/data-room/it/accounts-and-licences.csv), [`it/yossi-it-notes.md`](../../labs/module-16/data-room/it/yossi-it-notes.md), [`policies/municipal-service-agreement-extract.md`](../../labs/module-16/data-room/policies/municipal-service-agreement-extract.md), [`policies/privacy-and-confidentiality-policy-2019.md`](../../labs/module-16/data-room/policies/privacy-and-confidentiality-policy-2019.md), [`vendor/grantgenie-terms-extract.md`](../../labs/module-16/data-room/vendor/grantgenie-terms-extract.md), [`vendor/microsoft-renewal-notice.md`](../../labs/module-16/data-room/vendor/microsoft-renewal-notice.md), [`cases/case-notes-sample.csv`](../../labs/module-16/data-room/cases/case-notes-sample.csv).
- Persona: [Yossi Mizrahi](../../labs/module-16/personas/yossi-operations-it.md) or [his transcript](../../labs/module-16/personas/transcripts/yossi-operations-it.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [data boundary](../../templates/data-boundary.md), [tools and data classes](../../templates/tools-and-data-classes.md), [regulatory map](../../templates/regulatory-map.md), [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md) (answer five questions for GrantGenie), [DPIA for AI](../../templates/dpia-for-ai.md) (section headings only).

### Steps

1. Write your compression table: every Stage 1 step you would use, its size here, and what you will not skip.
2. Write the one-page legal map (applies / does not / open) and five questions for counsel.
3. Verify the offers yourself on today's date against the vendors' pages; note what changed since 3 November 2026.
4. Write the data boundary table and the three rules.
5. Write Yossi's checklist, with who decides each item; run it with him (roleplay) or annotate his transcript with what you would add.
6. Write Ronit's one-line message that gives staff the alternative the same day.

### Time

120 minutes: 20 for compression, 30 for the legal map, 25 for the offers, 20 for the boundary, 25 for the checklist and Yossi.

### Done when

- [ ] The compression table shrinks documents and keeps every step that touches people, access and the boundary.
- [ ] The legal map cites a source for every line, and nothing in it is stated as legal advice; the security level and the DPO duty are in the open column.
- [ ] Every offer has the vendor's page and the date you checked it, and says what is *not* included.
- [ ] The boundary covers identifiable family, donor, de-identified family, consented stories, organizational and public data, for each tool.
- [ ] Yossi's checklist fits one afternoon, gives the alternative the same day, and adds a second administrator.

<details><summary>Reference answer</summary>

The full paper is `labs/module-16/expert/04-compressed-plan-and-boundary.md`. The parts that carry the weight:

**Compression rule:** documents shrink; contact with the people and the data does not. Charter 1 page; census = Ronit's form + card statement + staff meeting; 7 × 30-minute interviews including a parent; one-table screen; one-page policy; vendor review = terms pages; DPIA = half a page + counsel; eval = 10 + 12 items and 9 negatives rated by users; training = one staff meeting; handover = 15 minutes a month.

**Legal map:**

| Rule | Applies? |
|---|---|
| Privacy Protection Law incl. Amendment 13 | Yes, fully; no small-organization exemption found |
| Registration | Probably not (counsel to confirm; the 2019 policy line is out of date) |
| Notification (more than 100,000 people) | No |
| DPO | Open (processing for Kiryat Hadas; sensitive data as core activity; no fixed "large scale" number) |
| Data Security Regulations | Yes; medium level for medical information unless no more than ten authorized users (First Schedule item 2) — counsel |
| Social Workers Law §8 | Yes; is AI on de-identified text a disclosure? Counsel |
| Kiryat Hadas agreement §7 | Yes, by contract (no transfer without approval; 24-hour incident report) |
| PPA AI draft guidance | As guidance |

**Questions for counsel:** (1) With 9 authorized users, is the case database at basic level, and what remains at that level? (2) Does processing Kiryat Hadas referrals trigger the DPO duty, and does §7.2 allow de-identified notes in Open Hands' own Workspace AI? (3) Under §8, is de-identified text in Workspace AI a disclosure; what should consent v3 say about digital tools? (4) What to do now about the September newsletter and the Q3 report? (5) Can the registration line be removed from the policy?

**Default tool:** Google Workspace for Nonprofits' Gemini app and NotebookLM, on organization accounts (₪0); no paid seats until March.

**Boundary:** R1 and R2 never into AI; A1 only in the case-note helper on organization accounts, coordinators and Hana only; A2 and G1 in the approved tools; personal accounts for nothing but public information.

**Yossi's afternoon (24 Nov):** link off (done 18 Nov); `Families` 46 → 9; former staff suspended; donor sheet 14 → 4 editors, IDs separated; Galina second super-admin, codes in the safe; Microsoft 10 → 3, Dropbox and GrantGenie cancelled; Ronit's message the same afternoon; monthly 15-minute check booked.

**Ronit's message:** "From today, work AI only on your @openhands-amuta.org.il account. No family names or donor details in any AI tool. The case-note helper comes next week. Questions: me or Yossi."

</details>

## References

- Amendment 13 and the Privacy Protection Law: [Pearl Cohen](https://www.pearlcohen.com/the-knesset-enacts-a-comprehensive-amendment-to-the-privacy-protection-law/); [Chambers Practice Guides, Israel 2026](https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel); the PPA's final DPO guidance of 15 July 2026 as reported by [Arnon, Tadmor-Levy](https://arnontl.com/news/ppa-publishes-final-guidance-on-the-dpo-appointment-obligation-under-amendment-13/). Secondary sources; the Hebrew statute and the PPA's Hebrew guidance are authoritative.
- [Privacy Protection (Data Security) Regulations, 5777-2017](https://www.gov.il/BlobFolder/legalinfo/data_security_regulation/en/5777%E2%80%932017.pdf) (PPA English translation) and the [Hebrew text](https://dpoisrael.com/law/security-regulations/), First Schedule item 2.
- [Social Workers Law, 5756-1996](https://www.ifsw.org/wp-content/uploads/2021/03/Social-Workers-Law-1996-Israel.pdf), section 8 (English translation).
- PPA draft guidance on AI: [Pearl Cohen](https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/). Section 46 digital donation reporting: [Barnea Jaffa Lande](https://barlaw.co.il/?p=61405).
- Offers (checked 3 November 2026): Google for Nonprofits [eligibility](https://support.google.com/nonprofits/answer/3215869?hl=en), [AI features](https://support.google.com/nonprofits/answer/16345471?hl=en), [discounts](https://knowledge.workspace.google.com/admin/billing/upgrade-from-google-workspace-for-nonprofits), [Workspace privacy hub](https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub), [Gemini personal-account privacy](https://support.google.com/gemini/answer/13594961); [Microsoft nonprofit offers](https://www.microsoft.com/en-us/nonprofits/offers-for-nonprofits); [Goodstack: OpenAI](https://goodstack.org/software-discounts/openai); Anthropic [Claude for Nonprofits](https://www.anthropic.com/news/claude-for-nonprofits) and [getting started](https://academy.claude.com/tutorials/getting-started-with-claude-for-nonprofits).
- Field kit: [04.1 · The AI acceptable-use policy](../module-04/lesson-01.md), [04.2 · Approved tools and data classes](../module-04/lesson-02.md), [04.3 · Vendor and tool review](../module-04/lesson-03.md), [04.4 · AI inventory, risk tiering and the DPIA](../module-04/lesson-04.md), [04.6 · Which law applies to you](../module-04/lesson-06.md).
- Templates: [data boundary](../../templates/data-boundary.md), [tools and data classes](../../templates/tools-and-data-classes.md), [regulatory map](../../templates/regulatory-map.md), [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md), [DPIA for AI](../../templates/dpia-for-ai.md).
- Earlier: [16.3 · Diagnosis](lesson-03.md). Next: [16.5 · Build: two workflows and the policy on one page](lesson-05.md).
