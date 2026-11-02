---
id: "11.2"
module: 11
minutes: 20
practice_minutes: 180
prerequisites: ["11.1", "02.1", "02.2", "02.4", "02.7", "01.6"]
objectives:
  - "Interview the front line, the hotline manager, the CIO and a resident so that the work, the definitions and the hidden tools come out, while protecting the people who speak."
  - "Measure what Givat Oren never measured: repeat contacts, callbacks actually made, the language residents are answered in, and pages that contradict the council's decision."
  - "Find the AI already talking to residents, and the decision letters that give no usable reason, from the data."
  - "Write a findings memo whose every finding carries a number, a source and a label."
volatility: implementation
sources:
  - title: "Administrative Procedure Amendment (Decisions and Reasons) Law, 5719-1958 (חוק לתיקון סדרי המינהל (החלטות והנמקות)), sections 1, 2, 2A, 6, Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/חוק_לתיקון_סדרי_המינהל_(החלטות_והנמקות)
  - title: "Freedom of Information Law, 5758-1998, Hebrew Wikisource"
    url: https://he.wikisource.org/wiki/חוק_חופש_המידע
  - title: "Israel National Digital Agency, Guide to the responsible use of AI in the public sector, v1.0, May 2026, Annex D (end users)"
    url: https://www.gov.il/BlobFolder/news/ai-guide/en/DL-57805%20AI%20Responsible%20User%20-%20English%20Guide%208.9.pdf
  - title: "IAPP, Israel marks a new era in privacy law: Amendment 13 (in force 14 August 2025)"
    url: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
last_verified: "2026-11-02"
---

# 11.2 · Discovery

The mayor's office thinks residents need a chatbot; the director-general wants to know why they don't get correct answers. Those are different questions, and only the second one can be answered from the work and the data. In this lesson you sit with the hotline and the permits desk, talk to a resident who was refused, ask the CIO what is really on the website, and measure five things nobody in Givat Oren has measured. At the end you have a findings memo with evidence labels for the director-general's Thursday note.

## The situation

Monday 30 November to Thursday 10 December 2026. Ronit Shemesh signed your mandate on Monday with one change ("any change, including an AI assistant"), approved pseudonymised exports and sent the division heads an email asking for content owners. Dmitri Kogan exported Moked 106's contacts (a 4% caller sample), the callbacks, the permits system's 2026 applications and the CMS inventory. The quality unit gave you its mystery-shopper calls from August and September. A clerk on the business-licensing desk sent you a short note about something called "Ruti".

This is module 2's method on a public service: [stakeholder map](../module-02/lesson-01.md), [interviews that get the work](../module-02/lesson-02.md), [baselines from exports](../module-02/lesson-04.md) and [a findings memo people believe](../module-02/lesson-07.md), with the [shadow-AI census](../module-01/lesson-06.md) folded in. IBM's consulting course calls a number "verified" only when you can trace it to a source and a definition; here half the numbers in the city's own report fail that test.

## What to do

### Step 1 — Map who knows what before you ask

Use the [stakeholder map](../../templates/stakeholder-map.md). For each person, what they know that nobody asks them, and what speaking costs them:

| Person | Knows | Risk to them if they speak |
|---|---|---|
| Larisa Gurevich, head of 106 | How FCR and the callback SLA are counted; who answers an Arabic caller at 16:00 | Her report's headline numbers |
| Tsega Mengistu, parking desk | What the desk really applies; what a refused resident reads | Admitting the desk applies an old rule; her own shortcuts |
| Dmitri Kogan, CIO | What is embedded in the site; what was counted for the FOI answer | IT's answer to a journalist |
| A refused resident | What the letter, the website and 106 told her, in what order | None, if you don't discuss her case |

Arrange the resident through the Resident Service Division, with her consent, and agree in advance that you will not discuss the outcome of her application: you cannot decide it.

### Step 2 — Interview for the work, and test the same words

The method is [02.2](../module-02/lesson-02.md): ask people to show you a normal case, not to describe the system. Three same-word tests matter here:

- **"Resolved."** Ask Larisa *exactly* how first-contact resolution is counted, after promising her that the definition story will not be attributed to her. The footnote says transfers, tickets and scheduled callbacks count. To a resident, "resolved" means somebody answered.
- **"Within SLA."** Scheduled, or done?
- **"Arabic service."** The language the resident chose in the menu, or the language of the agent who answered?

Interview Larisa (roleplay: [Larisa Gurevich](../../labs/module-11/personas/larisa-moked-head.md); [transcript](../../labs/module-11/personas/transcripts/larisa-moked-head.md)), sit at the desk with Tsega ([Tsega Mengistu](../../labs/module-11/personas/tsega-permits-clerk.md); [transcript](../../labs/module-11/personas/transcripts/tsega-permits-clerk.md)), call the resident ([Amal Nassar](../../labs/module-11/personas/amal-resident.md); [transcript](../../labs/module-11/personas/transcripts/amal-resident.md)) and ask the CIO what is on the site ([Dmitri Kogan](../../labs/module-11/personas/dmitri-cio.md); [transcript](../../labs/module-11/personas/transcripts/dmitri-cio.md)). Two questions that unlock the most: to Tsega, "what do you do with a leased car since July?" with the desk checklist in front of you; to Dmitri, "could a department put something on a page without you knowing?".

### Step 3 — Measure repeat contacts and the callbacks behind them

Nobody reports repeat contacts, so define one and say it every time you quote it: **a contact from the same caller, on the same topic, within 14 days of that caller's previous contact on it.** In `service/moked-contacts.csv`, sort by `caller_id`, `topic`, `opened_at`; flag a row when the two rows above match and the gap is under 14 days. Then split by topic family. "Permits family" here means parking permits, signs, cafés, events, skips, building archive, business licence and bulky waste.

Result on the extract (3,914 contacts, 1 June – 31 October, × 25 for the city):

| | Contacts | Repeat within 14 days |
|---|---|---|
| Permits family | 1,324 (33.8%) | **35.0%** |
| Other topics | 2,590 | 12.2% |

And the callbacks: join `service/callbacks.csv` on `contact_id` and compare `completed_at` with `promised_by_date`. Of 943 callbacks, **47.3% were made on time, 19.3% late, 33.4% never**; for the permits family 42.4% / 18.4% / 39.2% (n = 451). The report's "96% within SLA" counted the scheduling. Of the permits-family contacts the report counts as resolved, 34.3% were followed by a repeat.

### Step 4 — Measure the language residents are answered in

Compare `contact_language` with `served_language` for handled contacts:

| Chose | Handled | Answered in that language |
|---|---|---|
| Arabic | 748 | **39.7%** |
| Russian | 582 | 75.9% |
| Amharic | 146 | 26.7% |
| English | 106 | 89.6% |

Arabic callers who ended with a Hebrew-speaking agent waited a median 134 seconds on the phone, against 74 for Hebrew callers: the IVR overflow after 90 seconds is in the data. `service/moked-staffing-2026.csv`: 3 of 24 active agents speak Arabic; two language speakers left this year. In the mystery-shopper calls, 10 of 30 Arabic callers were answered in Arabic.

### Step 5 — Check every page against the decision that governs it

This is the step a chatbot project skips. Put `city/council-decision-fees-2025-12.md` beside each file in `content/site/` and mark it current or out of date:

- **9 of 24 permits pages are out of date.** Arabic: parking (₪90 and "leased cars not eligible"), bulky waste (₪120), events (14 days). Russian: parking, signs (₪245). English: parking, events. Hebrew: skips (₪60) and building archive (₪60).
- `content/cms-pages.csv`: six pages link `fee-table-2025.pdf`; 40.7% of 1,240 pages have no named owner; pages last changed before 2024: Arabic 70.8%, Russian 73.3%, English 80.0%, Hebrew 2.5%.

Then check whether the error reaches residents. The quality unit's mystery-shopper calls (`service/mystery-shopper-2026.csv`, 120 calls) join to the pilot's test questions by `question_id`; the test set (`pilot/test-set.csv`) says which rules changed in 2026. Agents were right on **74.4%** of questions whose rule did not change (n = 39) and **42.3%** where it did (n = 52); 21 answers stated an outdated figure. The error is not the agents': nobody told them.

### Step 6 — Read the decisions residents receive

`permits/applications-2026.csv` is complete for 2026. Four measures:

1. **Letter language:** all 2,300 letters were in Hebrew.
2. **Usable reasons:** of 293 parking-permit refusals, 151 (51.5%) carry R-07, "does not meet the criteria (section 3 of the procedure)". Refusals with R-07 bring **2.36** linked 106 contacts each; other codes about 1.05; approvals 0.16.
3. **A rule applied after it was abolished:** procedure PRK-4 made leased and company cars eligible with an employer letter from 1 July. Since then 63 such applications came with the letter; of the 55 decided, **33 were refused** (28 with R-07). The desk checklist (`permits/parking-permit-checklist-clerks.md`) is still version 3 of 2024. One of the 33 is Amal Nassar's, `2026-PRK-0945`.
4. **The cost of an old page:** event applications refused as late (R-08) are 48.8% of decided Arabic speakers' applications and 9.2% of Hebrew speakers': the Arabic page still says 14 days, the rule is 21.

The legal frame, so your memo uses the right words: the Administrative Procedure Amendment (Decisions and Reasons) Law, 5719-1958 (חוק לתיקון סדרי המינהל (החלטות והנמקות)) applies to local-authority employees; a refusal of a written request must state its reasons in writing (section 2A). Whether "section 3 of the procedure" meets that is the legal adviser's question, not yours. Your finding is what residents can and cannot do with the letter.

### Step 7 — Find the AI already talking to residents

Run the [shadow-AI census](../../templates/shadow-ai-survey.md) on what you have, before anyone asks you for an inventory:

- `content/cms-pages.csv`, column `script_embed`: a "botnest-widget" on three business-licensing pages.
- `chatbot/ruti-bot-log.csv` and `ruti-setup-notes.md`: "Ruti", built by a clerk in March on a free no-code platform with a private account, answering from the 2025 fee table and a 2024 guide. 640 conversations; every reply in Hebrew, including to 187 questions asked in Arabic, Russian or English; replies stating sign ₪245 (83), café ₪160 (62), events 14 days (62), "leased cars not eligible" (53), and an invented ₪1,200 restaurant licence fee (58); 46 messages contain a nine-digit number and 28 a mobile number.
- `governance/foi-response-2026-09-ai.md`: in September the city told a journalist it uses no AI.
- From the people, not the data: what staff use on their own phones (ask Tsega how she helps a resident who reads only Arabic).

Treat the clerk who built Ruti as a source, not a culprit: he built it because the phone line was impossible. The government's guide for public-sector end users says no personal or protected information goes into a third-party tool; the city's own procedure IS-07 says no embedded script without IT. Both were breached by a tool nobody gave an alternative to. Your memo asks for Ruti to be switched off properly (log exported, deletion requested from the platform), not for a disciplinary step.

**Track B (Python).** `python discovery.py` in `labs/module-11/` (module download) prints every number in steps 3–7 with its definition. Python is worth it here because the repeat-contact rule and the callback join are fiddly in a spreadsheet, and because the Resident Service Division will need exactly this script to report the new measures every month after February.

### Step 8 — Write the findings memo

Use the [findings memo](../../templates/findings-memo.md) and [02.7](../module-02/lesson-07.md): answer first, each finding with its number, source and label (measured, reported, inferred), what it means, what you need. Two rules for a municipal memo: write it so it can be released under the Freedom of Information Law without embarrassment to anyone named, and keep junior staff out of it by name.

## Watch out

- **Measuring the chatbot's market instead of the residents' problem.** "How many contacts could a bot take?" is the wrong first number. "Why do they call twice?" is the right one.
- **Accepting the report's definitions.** FCR and "within SLA" are true by their footnotes and misleading as service measures. Quote both, side by side.
- **Blaming the agents.** Agents gave old answers because nobody told them the rules changed. The finding is the missing content process.
- **Asking the resident to explain the rule back.** Amal knows what happened to her; she does not know "section 3". Let her tell it in order and ask what she needed.
- **Exposing the clerk who built Ruti.** The finding is the gap that made him build it. Name the tool, not the person, outside the director-general's office.
- **One average for all languages.** Arabic at 39.7% disappears inside an 80% "served in own language" average.

## Your turn

### Inputs

- Data room (module download): `service/` (all), `permits/` (all), `content/cms-pages.csv` and `content/site/`, `city/council-decision-fees-2025-12.md`, `chatbot/` (both), `governance/foi-log-2026.csv` and `foi-response-2026-09-ai.md`, `governance/information-security-procedure-2022-extract.md`; `../pilot/test-set.csv` for the mystery-shopper join.
- Personas: [Larisa](../../labs/module-11/personas/larisa-moked-head.md), [Tsega](../../labs/module-11/personas/tsega-permits-clerk.md), [Amal](../../labs/module-11/personas/amal-resident.md), [Dmitri](../../labs/module-11/personas/dmitri-cio.md), or their [transcripts](../../labs/module-11/personas/transcripts/); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [stakeholder map](../../templates/stakeholder-map.md), [interview guide](../../templates/interview-guide.md), [shadow-AI survey](../../templates/shadow-ai-survey.md), [findings memo](../../templates/findings-memo.md).

### Steps

1. Write the stakeholder map (four people at least, each with what they know and their risk).
2. Interview at least two of Larisa, Tsega, Amal and Dmitri (or read the transcripts and mark what was found and missed).
3. Measure repeat contacts (your definition written down), callbacks made, and service language.
4. Check every permits page against the council decision; count pages out of date by language.
5. Measure letters: language, R-07, leased cars refused since 1 July.
6. List the AI already in use, with evidence for each.
7. Write the findings memo (one page plus an evidence table).

**Track A (spreadsheet).** Repeats: sort the contacts by `caller_id`, `topic`, `opened_at`; in a new column `=AND(B3=B2, G3=G2, DATEVALUE(LEFT(C3,10))-DATEVALUE(LEFT(C2,10))<14)` (B = `caller_id`, C = `opened_at`, G = `topic`); average it per topic with a pivot. Callbacks: `=IF(E2="","never",IF(DATEVALUE(LEFT(E2,10))<=DATEVALUE(D2),"on time","late"))`.

**Track B (Python).** Run `python discovery.py`, check two of its numbers against your own spreadsheet, then use it for the memo's figures.

### Time

180 minutes: 20 for the map, 60 for two interviews, 50 for the measures, 20 for the page check, 30 for the memo.

### Done when

- [ ] Every number in the memo has a definition, a source file and a label.
- [ ] Repeat contacts, callbacks made and service language are measured and set beside the report's own figures.
- [ ] At least five out-of-date pages are named, with the figure they show and the figure the council decided.
- [ ] The memo names the AI already in use and asks for a proper switch-off and a corrected FOI answer, without naming the clerk.
- [ ] The letters finding says what a resident can and cannot do with "section 3", and routes the legal question to the legal adviser.

<details><summary>Reference answer</summary>

The full memo is `labs/module-11/expert/02-findings-memo.md` in the module download. Its spine:

**Answer first:** "Residents do not lack a chatbot. They lack one correct answer, in their language, and a reason they can use. About a third of Moked 106's work is permits-family questions, a third of those are the same resident coming back within two weeks, and many come back because the answer was out of date, in the wrong language, or a callback that never came. An assistant that reads today's website would repeat the outdated answers."

**Findings with numbers (M = measured, R = reported):**

| # | Finding | Evidence |
|---|---|---|
| 1 | 9 of 24 permits pages contradict the council's 2026 decision, mostly in Arabic, Russian, English | `content/site/` vs decision 2025/118 (M) |
| 2 | Agents right 74.4% where the rule did not change, 42.3% where it did | Mystery shopper, n = 39 / 52 (M) |
| 3 | FCR counts scheduled callbacks; 33.4% of callbacks never made (permits 39.2%) | Report footnote; `callbacks.csv` (M); Larisa (R) |
| 4 | Permits-family repeat contacts 35.0% vs 12.2% for other topics | `moked-contacts.csv` (M) |
| 5 | Arabic callers answered in Arabic 39.7%; median wait 134 s when moved to Hebrew | `moked-contacts.csv` (M) |
| 6 | All letters in Hebrew; R-07 on 151 of 293 parking refusals; 2.36 linked contacts each | `applications-2026.csv` (M) |
| 7 | 33 of 55 decided leased-car applications with the letter refused since 1 July; desk checklist v3 | `applications-2026.csv`, checklist (M); Tsega (R) |
| 8 | Arabic speakers' event applications refused as late 48.8% vs 9.2% (page says 14 days) | `applications-2026.csv` (M) |
| 9 | Ruti: 640 conversations, all replies in Hebrew, 433 with outdated or invented figures, 46 IDs | `ruti-bot-log.csv` (M) |
| 10 | The FOI answer "no AI" is wrong | CMS, Ruti, Dmitri (M, R) |

**What I need:** content owners named by 14 December; Ruti switched off by IT on Monday with the log exported and no action against the clerk; the legal adviser asked to correct the FOI answer; fifteen minutes at the 17 December forum.

**What the transcripts' interviewers missed:** Larisa was never asked what an agent looks at for a fee (the unofficial 2025 fee sheet) or whether anyone had tested agents' answers (the mystery shopper); Tsega was never asked how she helps a resident who reads only Arabic or Amharic (a free translation app on her personal phone, with car numbers and addresses pasted) or whether others use AI (Ruti); Amal was never asked whether she had tried the website's chatbot (Ruti told her, in Hebrew, that leased cars are not eligible) or whether she knew others in the same situation (at least five families); Dmitri was never asked what he counted as AI for the FOI answer (he left out the plate-reading cameras and machine translation).

</details>

## References

- [Administrative Procedure Amendment (Decisions and Reasons) Law, 5719-1958](https://he.wikisource.org/wiki/חוק_לתיקון_סדרי_המינהל_(החלטות_והנמקות)): applies to local-authority employees; reasons for a refusal in writing (sections 1, 2, 2A). Hebrew Wikisource; route every reading to the legal adviser.
- [Freedom of Information Law, 5758-1998](https://he.wikisource.org/wiki/חוק_חופש_המידע): why the memo is written to be releasable.
- Israel National Digital Agency, [Guide to the responsible use of AI in the public sector](https://www.gov.il/BlobFolder/news/ai-guide/en/DL-57805%20AI%20Responsible%20User%20-%20English%20Guide%208.9.pdf) (May 2026), Annex D: no protected information in third-party tools.
- IAPP, [Amendment 13](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform) (in force 14 August 2025): why residents' ID numbers on a free platform are the CISO's first call.
- Field kit: [01.6 · The shadow-AI census](../module-01/lesson-06.md), [02.1 · Stakeholder map](../module-02/lesson-01.md), [02.2 · The discovery interview](../module-02/lesson-02.md), [02.4 · Measuring a baseline from exports](../module-02/lesson-04.md), [02.7 · Writing a findings memo](../module-02/lesson-07.md).
- Templates: [stakeholder map](../../templates/stakeholder-map.md), [interview guide](../../templates/interview-guide.md), [shadow-AI survey](../../templates/shadow-ai-survey.md), [findings memo](../../templates/findings-memo.md).
- Earlier: [11.1 · The call](lesson-01.md). Next: [11.3 · Diagnosis](lesson-03.md).
