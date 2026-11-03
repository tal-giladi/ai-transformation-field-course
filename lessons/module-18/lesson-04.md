---
id: "18.4"
module: 18
minutes: 20
practice_minutes: 120
prerequisites: ["18.1", "01.1", "02.5", "04.2", "06.5"]
objectives:
  - "Decide whether a real engagement in your own workplace is possible at all, using a written go/no-go before you touch any data."
  - "Write a permission letter and a data-handling plan that the right people sign, and route every legal reading to counsel or the DPO."
  - "Interview colleagues without putting them at risk: consent, non-attribution and what you do with what you hear."
  - "Separate what you may take out of the organization from what you may not, and build a portfolio version from synthetic or anonymised material with written sign-off."
volatility: implementation
sources:
  - title: "Privacy Protection Law, 5741-1981 (חוק הגנת הפרטיות), Hebrew Wikisource: s. 2(8)–(9) breach of confidentiality and use for another purpose; s. 3 'information of special sensitivity'; s. 11 notice duty"
    url: https://he.wikisource.org/wiki/חוק_הגנת_הפרטיות
  - title: "IAPP, Israel marks a new era in privacy law: Amendment 13 ushers in sweeping reform (in force 14 August 2025)"
    url: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
  - title: "Chambers Practice Guides, Data Protection & Privacy 2026: Israel (secondary: Isakov tests, PPA Guideline 5/17 on workplace cameras, PPA 2025 anonymisation guidelines, purpose limitation)"
    url: https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel
  - title: "Commercial Torts Law, 5759-1999 (חוק עוולות מסחריות), Hebrew Wikisource: ss. 5–6, trade secrets"
    url: https://he.wikisource.org/wiki/חוק_עוולות_מסחריות
  - title: "Kol Zchut, protections from dismissal in collective agreements: the duty to consult workers' representatives in an organised workplace (updated 2 March 2025)"
    url: https://www.kolzchut.org.il/he/הגנות_מפיטורים_בהסכמים_קיבוציים
  - title: "GDPR Recital 26: pseudonymised vs anonymous data, 'means reasonably likely to be used' (gdpr-info.eu)"
    url: https://gdpr-info.eu/recitals/no-26/
last_verified: "2026-11-03"
---

# 18.4 · Optional: a real engagement in your own workplace

The method works on synthetic organizations because nobody can be hurt by them. In your own workplace the data is about real colleagues and customers, the documents belong to your employer, and the people you interview will still be there after you finish. This optional lesson is for learners who want to run the method for real: deciding whether it is possible, getting written permission, handling data and interviews so nobody is put at risk, and knowing what you may take out for your portfolio. At the end you have a go/no-go, a signed permission letter and data-handling plan (or a reasoned "no"), and a plan for the portfolio version.

> [!CAUTION]
> Do not open, copy, export or paste any real data, and do not interview anyone, until the permission letter in this lesson is signed by someone with the authority to sign it and your organization's privacy lead or DPO has answered your data questions in writing. Your employment contract, your organization's policies and Israeli law bind you whether or not you are "only doing a course exercise". Nothing in this lesson is legal advice: route every legal question to your organization's counsel or DPO, and if your organization has neither, do the capstone portfolio route instead.

## The situation

You finished the Tzurim capstone (or are doing it in parallel) and you want evidence from a real organization: yours. Perhaps you are the person who was told to "do AI" and this course was your preparation; perhaps you want a portfolio piece that is not synthetic. Both are good reasons. Both make the same mistake easy: treating access you already have as permission you were given.

You enter as an **internal lead with a day job**, as at Kinneret ([13.1](../module-13/lesson-01.md)): you have access and history, you are not neutral, and the people you will interview know you. [01.1](../module-01/lesson-01.md) taught what changes for each way in; this lesson adds what changes when the engagement is also your training exercise.

## What to do

### Step 1 — Go or no-go, before anything else

Answer these in writing. One "no" in the first four means you do the portfolio version from the capstone (Step 6) instead.

| Question | Why it matters |
|---|---|
| Is there a sponsor with authority over the units you would touch, who wants the answer? | Without one, the work is a private project with company data |
| Is there someone who can answer data-protection questions for the organization (a DPO, privacy lead or counsel)? | You must not decide lawfulness yourself |
| Can the work be done mostly on aggregate, sampled or de-identified data? | The less personal data you touch, the less can go wrong |
| Is there no live conflict around the area (layoffs, a labour dispute, a disciplinary process, litigation)? | Your work would be read as part of it |
| If the workplace is organised, can the workers' committee be told before interviews about changes to work? | Consultation comes before, not after ([06.5](../module-06/lesson-05.md)) |
| Do you have the time for it on top of your job, honestly? | A half-done engagement leaves expectations and data behind |

### Step 2 — Get permission in writing from the right people

Use the [permission letter and data-handling plan](../../labs/module-18/real-engagement/permission-and-data-plan.md) in the module download. The letter says what you will do, why, what you will look at, what you will **not** do, who sees what you write, what you take out, and that anyone named can stop it. Who signs depends on the organization; typically:

- **The sponsor**, with authority across the units involved (not only your own manager, if the work crosses departments).
- **The DPO or privacy lead**, on the data plan. Since Amendment 13 to the Privacy Protection Law came into force on 14 August 2025, more organizations must appoint a DPO and the Privacy Protection Authority has stronger enforcement powers; whether yours must, and what the DPO has to see, is the DPO's or counsel's question, not yours.
- **The information security officer**, where systems and exports are involved.
- **HR**, where the work touches how people work or data about employees; and **the workers' committee**, told in advance where the workplace is organised. In an organised workplace there is a duty to consult the workers' representatives in good faith at least before dismissals, even without a clause in the agreement; how far it reaches beyond that is a question for labour counsel.

Ask for the conditions to be written on the letter. "Approved, but no customer data" is a different engagement from "approved".

### Step 3 — Write the data-handling plan

The plan is one table: each dataset, its source, whether it is personal or sensitive, why you need it, the **minimum form** you will use, where it stays, which AI tool (if any) and under whose approval, and when it is deleted. Three points of Israeli law shape it (check each with your DPO):

- **Purpose.** The Privacy Protection Law (חוק הגנת הפרטיות, התשמ"א-1981) counts as an infringement of privacy the use of information about a person's private affairs, or passing it on, for a purpose other than the one it was given for (s. 2(9)), and breaching a duty of confidentiality about a person's private affairs set by an express or implied agreement (s. 2(8)). Data collected to run a service is not automatically available for your analysis; ask.
- **Information of special sensitivity.** The law's list (s. 3, as amended) includes, among others, health and medical information, genetic and biometric data, ethnic origin, criminal records, political opinions and religious beliefs, professional personality assessments, certain location data, salary data and financial activity, and information under a statutory confidentiality duty. Plan to use none of it; if you need some, the DPO approves the need in writing.
- **De-identified is not automatically anonymous.** A secondary practice guide reports that the Privacy Protection Authority's 2025 anonymisation guidelines treat data as outside the law only where re-identification is not possible with reasonable effort, and that anonymising is itself processing under the law. The EU's GDPR uses a similar test: identifiability is judged by "all the means reasonably likely to be used" (Recital 26). Removing names from a ticket export does not make it anonymous; free text, rare combinations and small groups re-identify people.

**AI tools.** Use only a tool your organization approved for that data class, under the organization's account and terms ([04.2](../module-04/lesson-02.md)). Never paste organization data into a personal account, however convenient, and never paste data of special sensitivity into any tool without the DPO's approval. If there is no approved tool, do the analysis without AI or on synthetic data.

### Step 4 — Interview colleagues without putting them at risk

Your interviewees are colleagues; some may report to you. The interview guide ([02.2](../module-02/lesson-02.md)) applies, with four additions:

1. **Say at the start** what the conversation is for, who will read what you write, and that you will not attribute anything to them by name without asking.
2. **Do not record** without explicit consent; take notes by role, not by name.
3. **Power runs both ways.** If you are their manager, someone else should run the interview, or you accept that you will hear less.
4. **Decide in advance what you do with what you hear.** If someone tells you about a practice that exposes personal data, breaks a safety rule or is unlawful, you do not keep it confidential "for the research": you follow the urgent-finding rule in your charter ([16.1](../module-16/lesson-01.md)) and protect the person who told you as far as you can.

If the engagement involves looking at colleagues' use of tools (usage logs, proxy data), aggregate by unit, never by person. Israeli labour case law (the *Isakov* ruling of the National Labour Court, 2011, as described in the secondary practice guide) tests an employer's access to employees' digital activity for legitimacy, proportionality and transparency; your analysis is the employer's processing too. The Privacy Protection Authority's guidance on workplace cameras is another reminder that monitoring individuals at work is tightly limited. None of that is your call to make: keep to aggregates and ask.

### Step 5 — Know what you may take out, and what you may not

| You may take out | You may not take out | Only with written approval |
|---|---|---|
| Your own templates, checklists and method notes, with nothing organization-specific in them | Any data: exports, samples, screenshots, transcripts | Ratios or trends indexed so the real numbers cannot be recovered |
| What you learned, in your own words | Internal documents, even "harmless" ones | A described case with the sector and size changed |
| A synthetic version of the engagement, built from scratch | Names, roles that identify a person, customer names | Quotes, fully de-identified, approved by the speaker |
| Your self-assessment against the rubric | Prices, contract terms, vendor quotes, plans, unreleased products | The organization's name as "a client", if it agrees |
| | Prompts or AI outputs that contain internal content | |

Two Israeli rules sit behind the middle column. Information that is not public, gives the organization a business advantage and is protected by reasonable measures can be a **trade secret** under the Commercial Torts Law (חוק עוולות מסחריות, התשנ"ט-1999, s. 5), and using one without consent in breach of a contractual duty or a duty of trust is misappropriation (s. 6(b)(2)). And your employment contract and the organization's policies almost certainly add confidentiality duties of their own. When in doubt, it stays.

### Step 6 — Build the portfolio version from synthetic or anonymised material

The safest portfolio piece from a real engagement contains no real data at all:

1. **Keep the method, replace the material.** Write synthetic data of the same shape (the course's data rooms are built this way: seeded generators, fictional names, real-shaped columns and messiness). Your findings become "a pattern like this", not "this company's numbers".
2. **Change what identifies the organization.** Sector, size, city, product, the order of events, unusual facts. Sector plus size plus city can be enough to identify an employer.
3. **Show your judgment, not their secrets.** A readiness assessment's structure and verdict logic, an eval report's design, a decision record's gates: these show what you can do.
4. **Get sign-off in writing** from the person who signed the permission letter, on the final piece, before anyone outside sees it. Lesson [18.5](lesson-05.md) turns it into a portfolio piece.

### Step 7 — Know when to stop

Stop that line of work and escalate the same day if you find an exposure of personal data, a safety risk, something that looks unlawful, or a person at risk because they spoke to you. Stop the whole engagement if the sponsor withdraws, the DPO says no, or a live conflict starts around it. Stopping cleanly — data deleted, people told, a short note of what you found to the sponsor — is a professional outcome, not a failure.

## Watch out

- **Access is not permission.** Being able to open a system as an employee does not make an analysis of it approved.
- **"It's only for a course."** Your duties of confidentiality and the law do not have a training exemption.
- **Personal AI accounts.** Pasting a real export into a personal chat account is the most common way this goes wrong.
- **"Anonymised" exports with free text.** Names removed, complaints and e-mails left in: people are identifiable from what they wrote.
- **Interviewing your own team about their work.** You will hear what they think you want; use someone else or accept the limit.
- **A portfolio piece shown before sign-off.** Once seen, it cannot be unseen; get the approval first.
- **Deciding the law yourself.** Write down the question, send it to the DPO or counsel, keep the answer.

## Your turn

### Inputs

- [Permission letter and data-handling plan](../../labs/module-18/real-engagement/permission-and-data-plan.md) (module download).
- Your organization's AI, IT and privacy policies; the name of its DPO, privacy lead or counsel; whether it has a workers' committee.
- Your capstone charter from [18.1](lesson-01.md), as a model.

### Steps

1. Write the go/no-go table for one real area of your workplace, with an honest answer and a reason for each question.
2. If any of the first four answers is "no": stop here, write two sentences on why, and plan the capstone-based portfolio piece in [18.5](lesson-05.md).
3. If go: fill the permission letter (one page), naming the signatories and the conditions you expect.
4. Fill the data-handling plan for every dataset you would need, with the minimum form and the deletion date; write the questions for the DPO.
5. Write the interview opening (what you will say in the first minute) and your rule for what you do with what you hear.
6. Fill the take-out table for this engagement, and the plan for the portfolio version.

### Time

120 minutes for the documents. The real engagement, if approved, takes four to six weeks part-time and is not counted here.

### Done when

- [ ] The go/no-go is written and honest, and a "no" leads to the capstone route rather than a workaround.
- [ ] The permission letter names the sponsor, the DPO or privacy lead, security, and HR or the workers' committee where relevant, with what you will not do and who can stop it.
- [ ] The data plan uses the minimum form of each dataset, no information of special sensitivity without written approval, and only tools approved for the data class.
- [ ] The interview opening states purpose, readers and non-attribution, and you have a written rule for what you hear.
- [ ] The take-out table puts every data item and internal document in "may not", and the portfolio plan uses synthetic or anonymised material with sign-off.
- [ ] Every legal question is written down and addressed to a named person, not answered by you.

<details><summary>Reference answer</summary>

A filled example for a fictional workplace: Galil Freight, a 300-person logistics company; the learner is the customer-service team lead.

**Go/no-go:** sponsor — yes, the COO, who owns customer service and billing; privacy — yes, an external DPO appointed in 2026; minimum data — yes, ticket metadata plus a 200-ticket sample with free text reviewed by the DPO; live conflict — no (but a reorganisation in logistics is rumoured: scope excludes logistics); workers' committee — none; time — six weeks at four hours a week, agreed with the COO. **Go**, scope customer service only.

**Permission letter (key lines):** "I will review how customer-service tickets are handled and where AI could help or should not, over six weeks, and give the COO a findings memo and a readiness assessment. I will not export data outside the company's systems, use any AI tool except the company's approved assistant under its account, record interviews, or draw conclusions about any employee's performance. Interviewees are not named. For my training portfolio I will write a synthetic version, which the COO reviews before it leaves." Signed by the COO; the DPO signed the data plan with the condition "free-text sample read only inside the company tenant; no customer names in notes".

**Data plan (excerpt):**

| Data | Personal? | Minimum form | Where | AI tool | Deleted |
|---|---|---|---|---|---|
| Ticket export, 6 months | Yes (customer names, e-mails in text) | Ticket id, category, channel, timestamps, resolution code; no free text | Company drive, restricted folder | None | 30 days after the memo |
| 200-ticket sample with text | Yes | Read in the tenant only; notes by category, no quotes | Company tenant | Approved assistant, DPO approval 12 Jan | Same |
| Interview notes (7) | Opinions | By role, not name | Company drive | None | After the memo is accepted |

**Questions sent to the DPO:** May ticket text be used for this analysis given the purpose it was collected for? May the approved assistant process the sample, and under which terms? What must be deleted and when?

**Take-out table:** may take — my checklists, the readiness structure, my self-score; may not — any ticket, screenshot, customer or employee name, volumes, the carrier contract; with approval — "handling time fell by about a third" as an indexed trend, and the case described as "a mid-sized B2B services company". **Portfolio plan:** a synthetic data room of 1,500 tickets with the same columns and failure patterns, generated from a seeded script; the COO reviews the final piece.

</details>

## References

- [Privacy Protection Law, 5741-1981](https://he.wikisource.org/wiki/חוק_הגנת_הפרטיות): s. 2(8)–(9), s. 3 (information of special sensitivity), s. 11 (notice duty). Hebrew Wikisource; check the current version with counsel.
- IAPP, [Amendment 13](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform) (in force 14 August 2025).
- Chambers, [Data Protection & Privacy 2026: Israel](https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel): a secondary source for the *Isakov* tests, the PPA's workplace-camera guidance and its 2025 anonymisation guidelines; read the primary texts before relying on them.
- [Commercial Torts Law, 5759-1999](https://he.wikisource.org/wiki/חוק_עוולות_מסחריות), ss. 5–6: trade secrets and misappropriation.
- Kol Zchut, [protections from dismissal in collective agreements](https://www.kolzchut.org.il/he/הגנות_מפיטורים_בהסכמים_קיבוציים): the duty to consult workers' representatives; its wider reach is for labour counsel.
- [GDPR Recital 26](https://gdpr-info.eu/recitals/no-26/): pseudonymised vs anonymous data (relevant where EU data is involved).
- Field kit: [01.1 · Three ways in](../module-01/lesson-01.md), [02.2 · The discovery interview](../module-02/lesson-02.md), [02.5 · Profiling the data](../module-02/lesson-05.md), [04.2 · Approved tools and data classes](../module-04/lesson-02.md), [06.5 · The comms pack](../module-06/lesson-05.md); [13.1 · The call](../module-13/lesson-01.md) (the internal lead), [16.1 · The call](../module-16/lesson-01.md) (urgent-finding rule).
- Next: [18.5 · Your practice kit and portfolio](lesson-05.md).
