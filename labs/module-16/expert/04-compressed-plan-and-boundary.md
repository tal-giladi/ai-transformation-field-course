# 04 · The compressed plan, the law for a small amuta and the data boundary — Open Hands

*Week 2, 22–26 November 2026. The hard part of this engagement is doing the whole method in 40 hours, with
free tools, around the most sensitive data a small organization can hold, with one person who does IT on
Tuesdays. This paper decides what shrinks, what cannot, and where each kind of data may go. It is not legal
advice: the open legal questions are listed for the volunteer lawyer at the end.*

## 1. What shrinks to an hour, and what you still cannot skip

| Method step (field kit) | Full size (Harbor & Pine) | Here | Why it can shrink | What you still cannot skip |
|---|---|---|---|---|
| Charter, scope, change control ([01.1](../../../lessons/module-01/lesson-01.md)–[01.3](../../../lessons/module-01/lesson-03.md)) | 2–3 days, a SOW | **1 page, 1 hour** | No fee, no contract to defend | The urgent-finding rule and "safely first" written down and signed |
| Stakeholder map ([02.1](../../../lessons/module-02/lesson-01.md)) | Half a day | **15 minutes** | 30 people; Ronit knows everyone | Putting the family and the funder on it |
| Shadow-AI census ([01.6](../../../lessons/module-01/lesson-06.md)) | Survey, proxy logs, expenses, a week | **Ronit's form + the card statement + 20 minutes at the staff meeting** | No proxy, no logs to read | Asking how people work, under non-attribution; the volunteers, whom the form missed |
| Interviews ([02.2](../../../lessons/module-02/lesson-02.md)) | 10–15 × 60 min | **7 × 30 min** | One person per role | The frontline worker, the volunteer and the **person affected** |
| Baseline ([02.4](../../../lessons/module-02/lesson-04.md)) | Exports, three systems | **One logged week + one more week asked for** | No systems to export from | Saying the logged week is a peak, not a baseline |
| Data profile ([02.5](../../../lessons/module-02/lesson-05.md)) | Days | **The sharing audit, read with Yossi, 2 hours** | Data lives in one Drive | Counting who can see what |
| Portfolio, scoring, ROI ([03.3](../../../lessons/module-03/lesson-03.md), [03.7](../../../lessons/module-03/lesson-07.md)) | Workshop, model, NPV | **One table, hours not shekels** | No investment to approve | The data gate; the "no AI" candidate |
| Policy pack ([04.1](../../../lessons/module-04/lesson-01.md)–[04.7](../../../lessons/module-04/lesson-07.md)) | 10 documents | **One page** | One tool family, one owner | The data boundary per data class and tool; who to ask |
| Vendor review ([04.3](../../../lessons/module-04/lesson-03.md)) | Questionnaire, 3 vendors | **The terms page of each tool already in use, 1 hour** | Free tools, take-it-or-leave-it terms | Reading the training-on-content clause and the conversion date |
| DPIA ([04.4](../../../lessons/module-04/lesson-04.md)) | Full template | **Half a page per workflow + questions to counsel** | Two workflows | Asking a lawyer the three questions below |
| Pilot and eval ([05.1](../../../lessons/module-05/lesson-01.md)–[05.4](../../../lessons/module-05/lesson-04.md)) | 2,000 items, harness | **10 + 12 items and 9 negative tests, rated by the users** | The users are the evaluators | Thresholds written before the run; the negative tests |
| Training and adoption ([06.2](../../../lessons/module-06/lesson-02.md), [06.4](../../../lessons/module-06/lesson-04.md)) | Session plan, dashboard | **One 45-minute staff meeting; 3 questions a month** | 30 people in one room | The sanctioned alternative on the same day as any "stop" |
| Readout, handover ([07.1](../../../lessons/module-07/lesson-01.md), [07.9](../../../lessons/module-07/lesson-09.md)) | Steering pack, binder | **20 minutes, one decision; a 15-minute monthly check** | One board, one owner | A named owner who can do it without you |

**The rule behind the table:** documents shrink; *contact with the people and the data* does not. Every step
that touches who can see what, what goes into which tool, and how the affected person is treated keeps its
full weight.

## 2. Which law applies to a 30-person amuta (and which does not)

Israel first. Sources are listed in the module's lessons; every line in the "open" column goes to counsel.

| Rule | Applies to Open Hands? | Notes |
|---|---|---|
| Privacy Protection Law, 5741-1981 (חוק הגנת הפרטיות), as amended by Amendment 13 (in force 14 Aug 2025) | **Yes, fully.** No exemption for nonprofits or small organizations was found | Purpose limitation, informed consent and notice, access rights, security, administrative fines |
| Database registration after Amendment 13 | **Probably not required** | Registration now covers data-trading databases and public bodies; the 2019 policy's registration line is out of date — counsel to confirm |
| Notification of databases with highly sensitive data on more than 100,000 people | **No** (≈ 440 families) | |
| DPO (privacy protection officer) duty | **Open** | Public bodies and **entities processing on their behalf**; data brokers; core activity of large-scale processing of highly sensitive data (no fixed number, per the PPA's final guidance of July 2026). Open Hands processes Kiryat Hadas referral data under a service agreement, and its core activity is sensitive data. Counsel |
| Privacy Protection (Data Security) Regulations, 5777-2017 | **Yes** | Medical or mental-condition information → medium security level, **unless** no more than ten authorized users (First Schedule, item 2) → basic. Today 46 accounts; 9 need it. Counsel to confirm the count and the level |
| Social Workers Law, 5756-1996, §8 professional confidentiality | **Yes**, for the six coordinators, Hana and anyone they share with | Disclosure only on written consent after the meaning is explained, or the listed exceptions. Whether an AI tool on Open Hands' own account is a "disclosure": counsel |
| Kiryat Hadas service agreement §7 | **Yes, by contract** | No transfer to third parties without written approval; security per the Regulations; incidents reported in 24 hours |
| PPA draft guidance on AI (April 2025) | **As guidance** | Same law across the AI lifecycle; transparency and management responsibility |
| Income Tax Ordinance §46 digital donation reporting (since 1 Jan 2026) | **Yes** | Why donor ID numbers exist; keep them in the receipts system and one restricted sheet |
| Registrar of Amutot, certificate of proper management | **Yes** (annual) | Context for the treasurer's caution, not an AI rule |
| GDPR | **Only for EU donors' data**, if any via the US Friends org | Not a factor in four weeks |

## 3. Free and cheap tools, checked against the vendors' own pages (3 November 2026)

| Offer | What it gives Open Hands | Checked | Use it? |
|---|---|---|---|
| **Google Workspace for Nonprofits** (already in use since 2019) | No cost, up to 2,000 users; the **Gemini app and NotebookLM** included; Workspace data protections (no training on customer data without permission; Gemini app chats and NotebookLM not reviewed by humans, for qualifying editions). **Not** included: Gemini inside Gmail/Docs/Drive side panel. Paid editions 70–75%+ off | Google nonprofit help pages; Workspace privacy hub (updated 6 Oct 2026); Israel eligible (amuta; verification by Goodstack) | **Yes: the default tool** |
| **Microsoft 365** | Business Basic free up to 300 users (web apps, Copilot Chat); Business Premium US$5.50/user/month paid yearly; Copilot add-on US$25.50; the Premium grant ended at renewal | Microsoft nonprofit offers page | **Keep 3 Premium seats for desktop Office; nothing else** |
| **ChatGPT Business (nonprofit)** | US$8/user/month annual (US$10 monthly), via Goodstack; Business data not used for training by default | Goodstack's OpenAI page; OpenAI help page blocked to the checker (⚠️ re-check) | **Not now**; decide in March for 2 development seats (₪602 a year) |
| **Claude for Nonprofits** | Up to 75% off Team and Enterprise (announced 2 Dec 2025), via Goodstack; excludes government, higher education, healthcare systems | Anthropic announcement; Anthropic Academy tutorial | **Alternative** to the line above |
| **TechSoup Israel** | Donated software (Yossi's 2022 note) | Could not confirm a current Israeli partner (2019 list: Rashi Foundation) | **Ask Mahut**; do not plan on it |
| **GrantGenie** (fictional) "Nonprofit Free Year" | Free until 31 Dec 2026, then US$49/month automatically; licence to train on uploaded content; US storage | Its terms, saved at sign-up | **Cancel; request deletion in writing** |
| Consumer accounts (personal ChatGPT, personal Gemini) | Free | Gemini consumer privacy hub: activity used to improve services incl. training when Keep Activity is on; reviewed chats kept up to 3 years | **Never for Open Hands information** |

Prices and eligibility change: whoever reads this after December 2026 checks the pages again.

## 4. The data boundary (what may go into which tool)

| Data class | Examples | Personal accounts | Open Hands Workspace (Gemini app, NotebookLM) | Paid nonprofit seats (later) | Never |
|---|---|---|---|---|---|
| **R1 Family — identifiable** | Case notes as written, referral forms, care sheets, case register, names, IDs, phones, towns + diagnoses, welfare status | No | **No** (stays in `Families`) | No | Any AI tool, until counsel answers §6 |
| **R2 Donor — personal** | Donor sheet, ID numbers, amounts, notes | No | No | No | Any AI tool; use a mail merge |
| **A1 Family — de-identified** | A note rewritten with roles ("the mother", "the child (8)"), no names, places, schools, hospitals, named diagnoses | No | **Yes, coordinators and Hana only, case-note helper only** | Not decided | Personal accounts |
| **A2 Consented stories** | Story bank texts approved by the family (consent v2, Part B) | No | Yes | Yes | Beyond the "may use" line |
| **G1 Organizational** | Boilerplate, outcomes framework, aggregated numbers, budgets, funders' templates | No | **Yes** | Yes | — |
| **G2 Public** | Website, published reports | Yes | Yes | Yes | — |

Three rules carry most of the weight: **work happens on work accounts**; **identifiable family and donor data
never goes into AI**; **anything sent outside Open Hands is read and signed by a person**.

## 5. Yossi's Tuesday (24 November, 13:00–17:00, done together)

1. Respite folder link: off (done 18 Nov). Care sheets shared only with the volunteers on Amir's list for
   the next two weekends; from December Amir prints one sheet per child, collected after the weekend.
2. `Families`: remove the 31 personal accounts, the 2 national-service volunteers and the 2 former staff;
   Ronit and Fatma move to `Intake` only. Result: 9 accounts.
3. Suspend Dana Klein's and Moshe Amar's Workspace accounts; transfer their files to Hana and Noa.
4. Donor sheet: domain-wide link off; editors Noa, Shira, Galina, Michael; Vova as viewer on an org
   account; ID numbers moved to a separate sheet only Galina and Noa can open; notes column cleaned of
   family and health details (Noa, by 1 Dec).
5. Second super-admin: Galina; recovery codes printed, in the safe, checked by Ronit.
6. Microsoft: 7 seats removed (renewal is annual: ask for a pro-rated credit; Galina follows up).
7. Dropbox cancelled; GrantGenie: Noa cancels, deletes the workspace and emails a deletion request.
8. One 15-minute check on the first Tuesday of each month (the list in 06).

## 6. Questions for the volunteer lawyer (2 hours, booked by Mahut for 26 November)

1. With 9 authorized users on the case files, is the database at the basic security level under the First
   Schedule, item 2, and what does Open Hands still have to do at that level?
2. Does processing Kiryat Hadas referral data make Open Hands an entity processing on behalf of a public
   body for the DPO duty, and does the agreement's §7.2 allow a cloud AI tool on Open Hands' own account to
   process de-identified referral notes?
3. Under the Social Workers Law §8, is de-identified text in Open Hands' own Workspace AI a disclosure? What
   should consent v3 say about digital and AI tools?
4. The September newsletter and the Q3 report: what should Open Hands do now (apology, removal, telling the
   funder), and does anything need to be reported?
5. Can the 2019 policy's registration line simply be removed?
