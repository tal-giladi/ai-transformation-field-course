---
id: "11.4"
module: 11
minutes: 24
practice_minutes: 160
prerequisites: ["11.3", "04.6", "04.8", "06.5", "08.4"]
objectives:
  - "Turn a municipality's public-sector constraints — procurement, freedom of information, reasons for decisions, accessibility, languages, privacy, workers and government guidance — into design rules for a resident-facing assistant, each with its source and owner."
  - "Read the wrong-advice risk the way the MyCity case shows it, and design against it instead of disclaiming it."
  - "Bring the legal adviser questions he can answer, and record what is still open."
  - "Read back a vendor's claims and a 'free pilot', choose a procurement route before any supplier gets data, and consult the works committee before 106's work changes."
volatility: implementation
sources:
  - title: "Municipalities Ordinance, sections 197 and 203, Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/פקודת_העיריות
  - title: "Municipalities (Tenders) Regulations, 5748-1987: regulation 2 (monthly indexation), 3 (exemptions incl. 3(3), 3(4), 3(8), 3(15), 3(16)), 8 (limited tender; Oct 2021 amounts ₪145,500 and ₪710,600), Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/תקנות_העיריות_(מכרזים)
  - title: "Freedom of Information Law, 5758-1998: sections 2, 6, 7, 9, Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/חוק_חופש_המידע
  - title: "Administrative Procedure Amendment (Decisions and Reasons) Law, 5719-1958, Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/חוק_לתיקון_סדרי_המינהל_(החלטות_והנמקות)
  - title: "Equal Rights for Persons with Disabilities (Service Accessibility Adjustments) Regulations, 5773-2013: regulations 35, 35A (IS 5568 level AA; documents and forms), 35E (accessibility statement), Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/תקנות_שוויון_זכויות_לאנשים_עם_מוגבלות_(התאמות_נגישות_לשירות)
  - title: "Kol Zchut, website and app accessibility for people with disabilities (local authorities included; compensation up to ₪50,000 without proof of damage), updated 1 November 2026"
    url: https://www.kolzchut.org.il/he/הנגשת_אתרי_אינטרנט_ואפליקציות_לאנשים_עם_מוגבלות
  - title: "Standards Institution of Israel, SI 5568 Part 2: accessibility of digital documents, 28 September 2023"
    url: https://www.sii.org.il/he/lobby/standardization/standard-page?id=6753
  - title: "Basic Law: Israel as the Nation-State of the Jewish People (2018), section 4 (language), Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/חוק-יסוד:_ישראל_–_מדינת_הלאום_של_העם_היהודי
  - title: "HCJ 4112/99 Adalah v. City of Tel Aviv-Jaffa (25 July 2002), Versa (Cardozo) summary and English translation"
    url: https://versa.cardozo.yu.edu/node/541
  - title: "The Markup, 'NYC's AI Chatbot Tells Businesses to Break the Law', 29 March 2024"
    url: https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law
  - title: "The Markup and THE CITY, 'Mamdani to Kill the NYC AI Chatbot We Caught Telling Businesses to Break the Law', 30 January 2026 (updated 4 February 2026)"
    url: https://themarkup.org/artificial-intelligence/2026/01/30/mamdani-to-kill-the-nyc-ai-chatbot-we-caught-telling-businesses-to-break-the-law
  - title: "Israel National Digital Agency, Guide to the responsible use of AI in the public sector, v1.0, May 2026 (English translation)"
    url: https://www.gov.il/BlobFolder/news/ai-guide/en/DL-57805%20AI%20Responsible%20User%20-%20English%20Guide%208.9.pdf
  - title: "Barnea Jaffa Lande, client update: the duty to inform and consult in unionised workplaces (case law, not statute), 8 November 2015"
    url: https://barlaw.co.il/practice_areas/employment/client_updates/the-rise-of-employees-unionization-and-consultation-obligation-during-transactions/
  - title: "IAPP, Amendment 13 to Israel's Privacy Protection Law (in force 14 August 2025)"
    url: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
last_verified: "2026-11-02"
---

# 11.4 · The hard part

Every organization in this course is about one hard thing. Givat Oren's is that a city is not a company: it buys through tenders, answers to freedom-of-information requests, must give reasons for its decisions, must be accessible, serves residents in more than one language, and changes its workers' tasks only after consulting them. A chatbot that ignores any of these fails in public. In this lesson you turn each constraint into a design rule with its source and owner, read the wrong-advice risk through New York's MyCity chatbot, bring the legal adviser questions he can answer, read back the vendor's claims and its "free pilot", choose a procurement route and consult the works committee. At the end you have the constraints paper for the director-general on 7 January.

## The situation

Sunday 20 December 2026 to Thursday 7 January 2027. On 17 December the forum approved the knowledge pack, the new letters and the callback measures, and an internal test of an assistant for 106 agents, to be reported on 2 February. The finance committee re-labelled the ₪600,000 line on 22 December. The chief of staff accepted the plan "as long as the mayor has something on the 4th", and forwarded an email from CivicTalk asking for "the go-live date".

This week you see three people. Adv. Samer Haddad, the legal adviser, on Monday 21 December (roleplay: [Samer](../../labs/module-11/personas/samer-legal-adviser.md); [transcript](../../labs/module-11/personas/transcripts/samer-legal-adviser.md)); Moshe Azulay, chair of the works committee, on Wednesday 23 December ([Moshe](../../labs/module-11/personas/moshe-works-committee.md); [transcript](../../labs/module-11/personas/transcripts/moshe-works-committee.md)); and Liron Avital of CivicTalk on Monday 28 December ([Liron](../../labs/module-11/personas/liron-civictalk-ae.md); [transcript](../../labs/module-11/personas/transcripts/liron-civictalk-ae.md)).

The field kit has the moves: the [regulatory map](../module-04/lesson-06.md), [vendor and claim due diligence](../module-04/lesson-08.md), the [comms pack and works-council consultation](../module-06/lesson-05.md), and Northwind's [liability read](../module-08/lesson-04.md). What is new is that in a municipality these are not risks to manage after the decision; they decide the design.

## What to do

### Step 1 — Write the constraints map: source, meaning, design rule, owner

Use the [regulatory map](../../templates/regulatory-map.md) with one extra column, **the design rule**: what the constraint makes you build differently. Nine rows; the sources were checked on 2 November 2026, and every reading is the legal adviser's to confirm. This course is not legal advice.

**1. Procurement.** A municipality contracts for goods, services and works by public tender (Municipalities Ordinance, section 197) unless the Municipalities (Tenders) Regulations, 5748-1987 give an exemption. Below the amount in regulation 3(3) no tender is needed (the city's procedure still asks for price quotes); between that and the ceiling in regulation 8, a limited tender with four or six invited suppliers. The amounts are linked to the consumer price index and updated on the 16th of every month (regulation 2); the published text shows the October 2021 figures, ₪145,500 and ₪710,600, so ask the treasurer for today's. The exemptions most often raised for technology are special knowledge or expertise (3(8)), the only supplier in Israel confirmed by an expert (3(4)), and a company whose shareholders are a majority of local authorities, for management and supervision services (3(15)). A financial commitment binds the city only when the mayor and the treasurer sign it (Ordinance, section 203). **Design rule:** the internal test is a small purchase of model usage through the city's own cloud account; a production assistant is specified by the test and bought by tender or a recorded exemption the legal adviser approves; no supplier receives data or a promise before the route is chosen.

**2. Freedom of information.** Local authorities are public authorities under the Freedom of Information Law, 5758-1998 (section 2). Administrative guidelines that matter to the public must be available for inspection (section 6); requests are answered within 30 days, extendable (section 7); exemptions include internal deliberations (9(b)(4)) and trade secrets (9(b)(6)). **Design rule:** publish what the assistant is, what it answers from and how it was tested before anyone asks; correct the September answer that said the city uses no AI; write every note as if it will be released.

**3. Reasons for decisions.** The Administrative Procedure Amendment (Decisions and Reasons) Law, 5719-1958 applies to local-authority employees: a written request gets a written decision, and a refusal states its reasons in writing (sections 2, 2A); if not, the authority bears the burden of showing the decision was lawful (section 6). **Design rule:** the assistant never explains, predicts or reviews a resident's own decision; it routes to the department that must give the reasons. The letters (11.3, item C) carry the reason.

**4. Accessibility.** The Equal Rights for Persons with Disabilities (Service Accessibility Adjustments) Regulations, 5773-2013 require websites to meet Israeli Standard 5568 at level AA (regulation 35A(a)), documents and service forms to be accessible (35A(c)) and an accurate accessibility statement (35E). Kol Zchut (updated 1 November 2026) confirms local authorities are included and that a court may award up to ₪50,000 without proof of damage. **Design rule:** anything embedded on the site is part of the site: an external accessibility audit of any widget is a procurement requirement; fix the 2021 statement that says "all pages and documents are accessible".

**5. Languages.** Hebrew is the state language; Arabic has a special status, and the Basic Law: Israel as the Nation-State of the Jewish People (2018, section 4) says the status Arabic had in practice before it is not harmed. In 2002 the Supreme Court required Arabic on municipal signs in mixed cities (HCJ 4112/99 *Adalah v. Tel Aviv-Jaffa*), reasoning that a resident who cannot read Hebrew cannot use city services on equal terms. The legal adviser does not say the law requires a chatbot in Arabic; he says he will not sign off a service "in every language" that serves Arabic speakers worse than Hebrew speakers. **Design rule:** a language gate in the eval (Arabic results as good as Hebrew); Amharic routed to a person until it is tested; no machine translation of a Hebrew page presented as an Arabic answer.

**6. Wrong-advice risk.** Step 2.

**7. Privacy.** Residents' personal data under the Privacy Protection Law, 5741-1981 and its data-security regulations, with Amendment 13 in force since 14 August 2025 and far larger sanctions. **Design rule:** no personal data in the assistant's sources; it does not look anyone up; it never repeats an ID or a car number; logs stay on the city's tenant for a fixed period; the CISO approves. Ruti held ID numbers on a free platform: the deletion request is part of closing it.

**8. Workers.** Moked 106's 2019 local agreement requires informing the works committee in writing and consulting before changing work methods, technology or positions, with six hours' paid training for a new system. Beyond the agreement, Israeli labour courts have held that an employer in a unionised workplace must inform and consult the workers' representative about structural changes (a duty from case law, not statute; Barnea Jaffa Lande's 2015 client update). **Design rule:** consult before any proposal is fixed; the test measures answers, not agents; no individual monitoring; training before use; positions and grades are the director-general's and HR's to discuss.

**9. Government guidance.** The National Digital Agency's *Guide to the responsible use of AI in the public sector* (version 1.0, May 2026, with the Ministry of Justice's Office of Legal Counsel) sets a traffic-light method — green, yellow and red tracks by risk — and a **blue track** for limited, controlled experiments with defined duration, metrics and reporting; it asks for public transparency about AI systems and tells end users not to put protected information into third-party tools. It was written for public-sector entities and, as far as this course found, does not bind a municipality; the Ministry of Justice's legal guide on issues such as the duty to give reasons and transparency is still being drafted. **Design rule:** adopt it: the internal test as a yellow-track project with the director-general acting as Chief AI Officer; any public pilot as a blue-track experiment with its own metrics and end date.

(Israel signed the Council of Europe's Framework Convention on AI on 5 September 2024 and has not ratified it, the guide notes. The EU AI Act does not reach a city serving its own residents.)

### Step 2 — Read the wrong-advice risk through MyCity

In October 2023 New York City launched a chatbot, built on Microsoft's cloud, to help business owners with city rules. On 29 March 2024 The Markup published what it told people: that employers could take a cut of workers' tips, that landlords did not have to accept tenants with housing vouchers, that a business could refuse cash despite a 2020 city law; it also gave different answers to the same question. The city defended it as a pilot that would improve and added a disclaimer telling users not to treat its answers as legal or professional advice. In January 2026 the new mayor called it "functionally unusable"; on 4 February 2026 the city took it down ("beta test has ended"). It had reportedly cost close to US$600,000 to build.

Three lessons for Givat Oren, each a design rule:

- **A disclaimer does not make a wrong answer right.** MyCity kept answering after the disclaimer. A resident who builds a pergola because the bot said "usually exempt" has the fine, not the city's footnote. Rule: the assistant refuses whole classes of questions (exempt works, individual decisions, legal questions) and is tested on them.
- **An assistant is as right as the content it reads.** MyCity's errors were about rules; Givat Oren's website already contradicts the council in three languages. Rule: answer only from the owned, dated knowledge pack; show the source and its date in every answer.
- **"Public testing" tests on residents.** Rule: agents first, who "know when an answer smells wrong" (the head of 106); residents only after a second test on their real questions.

Who is speaking, if it goes wrong? At Northwind ([08.4](../module-08/lesson-04.md)) the answer was the company. For a city the question is sharper and open: are an assistant's answers "administrative guidelines" the public may rely on? Can a resident who relied on one claim against the city? The legal adviser does not know yet. His advice is the right one for a designer: "Don't design anything that assumes the answer either way."

### Step 3 — Bring the legal adviser questions he can answer

"Is the chatbot legal?" cannot be answered. Send five questions in writing a few days before, each framed as a decision:

1. Is an internal test with model usage bought by price quotes, below the regulation 3(3) amount, a tender matter?
2. What did CivicTalk receive, and does anything bind the city?
3. Must a public assistant serve Arabic speakers as well as Hebrew speakers, and how would you judge "as well"?
4. Is an assistant's answer an administrative guideline under section 6? Can a resident rely on it?
5. May we publish an AI-register entry, and what must it say?

Record his answers as "preliminary view, not an opinion", and what he will put in writing and by when. Then bring him what he did not know: Ruti, the plate-reading cameras and the translation vendor's machine translation, and ask, calmly, who checked the September FOI answer. The answer will be "IT said so"; the outcome you want is a correction this month, not a culprit.

### Step 4 — Read back the vendor's claims and the "free pilot"

Use the [claim read-back](../../templates/claim-read-back.md) from [04.8](../module-04/lesson-08.md). Open the meeting by saying, for the minutes, that nothing has been agreed and only the mayor and the treasurer can commit the city. Then ask, for each claim, under what conditions it was measured:

| Claim | Ask | What it turned out to mean | Read-back |
|---|---|---|---|
| "Trusted by 30 authorities" | How many use the chatbot itself, live, today? | Customers of any product, mostly forms | Ask for live chatbot references |
| "94% accuracy" | Who wrote the questions, in which languages, who scored them, against what? | (Ask; the transcript's interviewer did not) | Not evidence until answered |
| Arabic, Russian, English | What will it answer from? | The crawl of the site as it is; old pages win; machine translation where none | Fails the language gate on today's site |
| "WCAG compliant" | Can we see the external audit of the widget? | Self-declared | Audit required |
| "Framework, no tender" | Which framework, which scope? | FW-21/2024 covers digital forms and online payments | Not a route for a chatbot |
| "Free pilot" | What happens on day 91? | ₪14,500 + VAT a month, 36 months, auto-renewal: ₪522,000 | A commitment nobody authorised |

To practise reading demo claims against evidence before the meeting, the vendor simulation's generic scenario works (it is about another product; the move is the same):

[Simulation: Vendor RFP](../../simulations/vendor-rfp/index.html?preset=generic)

Ask what a fair test on your own questions would look like: Liron offers a paid proof of concept on a question set the city provides, about ₪38,000. That is the right kind of test, through the right kind of route, later.

### Step 5 — Choose the procurement route before anyone gets data

Write the route as three stages, each with its legal basis to be confirmed by the legal adviser and the treasurer:

1. **Now to February:** the internal test on the city's own cloud tenant; model usage by price quotes; no vendor; the test set and gates are the city's.
2. **March:** a public **request for information** (RFI) describing the need, the languages, the gates and the accessibility requirement; every supplier gets the same information and time.
3. **May:** if the internal pilot passes, a tender for production with the eval gates as the specification, an accessibility audit of the widget, no training on the city's data, data location, content owned by the city, exit and export.

### Step 6 — Consult the works committee before the proposal is fixed

Use the comms and consultation method of [06.5](../module-06/lesson-05.md). Go early, say truthfully that nothing is decided, ask what the workers would need for a tool to be acceptable, and put commitments where they belong: a letter from the **director-general**, not from you. Moshe's conditions in the transcript (no layoffs because of it, no cut in positions, paid training, no individual monitoring) are reasonable; only the director-general can promise the first two. Ask him why the workers are so afraid; the answer changes your comms plan.

### Step 7 — Write the constraints paper

One paper for the director-general on 7 January: the answer first (none of the constraints forbids an assistant; together they decide its shape), the constraints map with design rules, the legal adviser's preliminary views and open questions (attributed), the vendor read-back, the procurement route, and what was agreed with the works committee. Then send the legal adviser the draft AI-register entry (format in 11.5).

## Watch out

- **"Legal is blocking us."** The legal adviser names exposures; the design decides whether they materialise. Bring him decisions, not a product to approve.
- **Disclaimers as design.** MyCity had one. Refuse the dangerous classes of question and test the refusals.
- **"Free" as a procurement exemption.** It isn't one. Say in writing that nothing is agreed, and ask the vendor to delete what it crawled.
- **Arabic as a translation task.** A machine-translated Hebrew page is not service in Arabic, and an old Arabic page is worse than none. Make language a gate with numbers.
- **Promising the union what isn't yours.** "No layoffs" is the director-general's sentence. Yours is "the test measures answers, not people".
- **Treating the government guide as law, or ignoring it.** It is guidance written for public bodies, the best shared standard you have; say which parts you adopt.
- **Stating the tender threshold from memory.** It changes every month.

## Your turn

### Inputs

- Data room (module download): `procurement/` (all four files), `governance/` (all), `hr/` (both), `chatbot/ruti-setup-notes.md`, `content/cms-pages.csv`, `service/moked-staffing-2026.csv`, `permits/decision-letter-templates.md`.
- Your case (11.3) and findings memo (11.2).
- Personas: [Samer Haddad](../../labs/module-11/personas/samer-legal-adviser.md), [Moshe Azulay](../../labs/module-11/personas/moshe-works-committee.md), [Liron Avital](../../labs/module-11/personas/liron-civictalk-ae.md), or their [transcripts](../../labs/module-11/personas/transcripts/); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [regulatory map](../../templates/regulatory-map.md), [risk register](../../templates/risk-register.md), [claim read-back](../../templates/claim-read-back.md), [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md), [comms plan](../../templates/comms-plan.md), [decision-ready case](../../templates/decision-ready-case.md).

### Steps

1. Write the constraints map: nine rows, each with source, meaning, design rule and owner.
2. Write the MyCity read in five lines: what happened, what the city did, and the three design rules it gives you.
3. Send the legal adviser five written questions; interview him (or read the transcript); record preliminary views and open questions, attributed.
4. Interview the vendor (or read the transcript); write the claim read-back with the free pilot's real cost.
5. Write the procurement route in three stages, each with the basis to be confirmed.
6. Interview the works committee chair (or read the transcript); draft the director-general's letter to him.
7. Write the constraints paper.

### Time

160 minutes: 40 for the map, 15 for MyCity, 30 for the legal adviser, 25 for the vendor, 15 for the route, 20 for the works committee, 15 for the paper.

### Done when

- [ ] Every constraint has a source you can name, a design rule and an owner; no legal reading is in your own voice.
- [ ] The wrong-advice risk is handled by refusals and sources that are tested, not by a disclaimer.
- [ ] The legal adviser's open question on reliance is recorded as open.
- [ ] The vendor read-back states the conditions of every claim and the free pilot's cost over its term.
- [ ] The procurement route is chosen before any supplier gets data, and the vendor has been told in writing that nothing is agreed.
- [ ] The works committee was consulted before a proposal was fixed, and the commitments are in the director-general's letter.

<details><summary>Reference answer</summary>

The full paper is `labs/module-11/expert/04-public-sector-constraints.md` in the module download. Its spine:

**Answer first:** "None of the constraints forbids an assistant. Together they decide its shape: built and tested inside first, for agents; content the city owns and dates; answers that cite their source and refuse individual decisions; Arabic as good as Hebrew; a public register entry; a procurement route chosen before any vendor gets data; and the works committee consulted before 106's work changes. A public chatbot on 4 February fails five of the constraints."

**Design rules (one per constraint):** price quotes for the internal test, tender or recorded exemption for production (Ordinance ss.197, 203; Tenders Regulations regs 2, 3, 8); publish the register entry and correct the FOI answer (FOI Law ss.2, 6, 7); never explain an individual decision, route it (Decisions and Reasons Law ss.2, 2A, 6); audit any widget, fix the statement (regs 35A, 35E); a language gate, Amharic routed (Basic Law s.4; HCJ 4112/99, legal adviser's view); answer only from the owned pack, refuse exempt-works, individual and legal questions (MyCity); no personal data in sources, logs on the city's tenant (Privacy Protection Law, Amendment 13; IS-07); consult before change, no individual monitoring (2019 agreement; case law); yellow track internal, blue track for any public pilot (National Digital Agency guide, May 2026).

**Legal adviser (21 December, preliminary):** the internal test below the reg. 3(3) amount is price quotes; nothing binds the city with CivicTalk and a free pilot with city data raises equal treatment for a future tender (note sent 24 December); he will not sign off a service that serves Arabic worse; the FOI answer is corrected in writing (sent 31 December). **Open:** whether an assistant's answers are administrative guidelines residents may rely on.

**Vendor read-back:** 30 authorities = all products, 4 with the chatbot; "94%" = 200 Hebrew questions CivicTalk wrote from its own sample FAQ, scored by its staff, "accuracy" meaning the answer matched the FAQ text; "resolved" = no hand-over requested; answers from the crawl including old pages; machine translation where no page; accessibility self-declared; framework scope forms and payments; free pilot = ₪522,000 + VAT over 36 months, auto-renewing.

**Route:** internal test now; RFI in March; tender in May with the gates as the specification.

**Works committee (DG's letter, 29 December):** the test measures answers, not agents; no individual monitoring; six hours' paid training; the committee informed before each stage and invited to the forum item; positions and grades discussed with the DG and HR.

**What the transcripts' interviewers missed:** the legal adviser was never asked "what happens when an answer is wrong — can residents rely on it?", so his open question stayed hidden; Liron was never asked who wrote and scored the benchmark or how many authorities use the chatbot itself; Moshe was never asked why the workers are so afraid (a deputy mayor told 106 agents in 2024 that "the digital channel will let us cut shifts") or about grades for agents who maintain the answers.

</details>

## References

- [Municipalities Ordinance](https://he.wikisource.org/wiki/פקודת_העיריות), ss.197, 203; [Municipalities (Tenders) Regulations, 5748-1987](https://he.wikisource.org/wiki/תקנות_העיריות_(מכרזים)), regs 2, 3, 8. Hebrew Wikisource; confirm the current amounts with the treasurer.
- [Freedom of Information Law, 5758-1998](https://he.wikisource.org/wiki/חוק_חופש_המידע); [Administrative Procedure Amendment (Decisions and Reasons) Law, 5719-1958](https://he.wikisource.org/wiki/חוק_לתיקון_סדרי_המינהל_(החלטות_והנמקות)).
- [Service Accessibility Adjustments Regulations, 5773-2013](https://he.wikisource.org/wiki/תקנות_שוויון_זכויות_לאנשים_עם_מוגבלות_(התאמות_נגישות_לשירות)), regs 35–35F; Kol Zchut, [website accessibility](https://www.kolzchut.org.il/he/הנגשת_אתרי_אינטרנט_ואפליקציות_לאנשים_עם_מוגבלות) (updated 1 November 2026); SII, [SI 5568 Part 2](https://www.sii.org.il/he/lobby/standardization/standard-page?id=6753) (digital documents, 2023).
- [Basic Law: Israel as the Nation-State of the Jewish People](https://he.wikisource.org/wiki/חוק-יסוד:_ישראל_–_מדינת_הלאום_של_העם_היהודי), s.4; [HCJ 4112/99 Adalah v. Tel Aviv-Jaffa](https://versa.cardozo.yu.edu/node/541) (2002).
- The Markup, [NYC's AI chatbot tells businesses to break the law](https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law) (29 March 2024) and [Mamdani to kill the NYC AI chatbot](https://themarkup.org/artificial-intelligence/2026/01/30/mamdani-to-kill-the-nyc-ai-chatbot-we-caught-telling-businesses-to-break-the-law) (30 January 2026, updated 4 February 2026).
- Israel National Digital Agency, [Guide to the responsible use of AI in the public sector](https://www.gov.il/BlobFolder/news/ai-guide/en/DL-57805%20AI%20Responsible%20User%20-%20English%20Guide%208.9.pdf), v1.0, May 2026.
- Barnea Jaffa Lande, [duty to inform and consult in unionised workplaces](https://barlaw.co.il/practice_areas/employment/client_updates/the-rise-of-employees-unionization-and-consultation-obligation-during-transactions/) (2015); IAPP, [Amendment 13](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform). Not legal advice: route every reading to the legal adviser.
- Field kit: [04.6 · Which law applies to you](../module-04/lesson-06.md), [04.8 · Vendor and claim due diligence](../module-04/lesson-08.md), [06.5 · The comms pack](../module-06/lesson-05.md), [08.4 · The hard part (Northwind)](../module-08/lesson-04.md).
- Templates: [regulatory map](../../templates/regulatory-map.md), [risk register](../../templates/risk-register.md), [claim read-back](../../templates/claim-read-back.md), [vendor AI questionnaire](../../templates/vendor-ai-questionnaire.md), [comms plan](../../templates/comms-plan.md).
- Simulation: [Vendor RFP](../../simulations/vendor-rfp/index.html?preset=generic) (generic scenario: practise reading demo conditions against evidence).
- Earlier: [11.3 · Diagnosis](lesson-03.md). Next: [11.5 · Build: a permit-FAQ assistant, evaluated](lesson-05.md).
