---
id: "12.2"
module: 12
minutes: 20
practice_minutes: 180
prerequisites: ["12.1", "01.6", "02.2", "02.4", "02.7"]
objectives:
  - "Interview partners and associates in a law firm so that associates can tell you what they actually do without being identified."
  - "Measure AI use from the proxy log, expenses and DLP alerts, and set it against what the firm's own survey says."
  - "Measure the research share of lawyers' time from time-entry narratives where the activity codes hide it, and show who already pays for research through write-offs."
  - "Check a research memo's citations against the firm's corpus and write a findings memo whose every finding is labelled measured, reported or inferred."
volatility: implementation
sources:
  - title: "IAPP, Israel marks a new era in privacy law: Amendment 13 ushers in sweeping reform (in force 14 August 2025)"
    url: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
  - title: "Calcalist, 17 September 2026: the Israel Bar Association's ethics committee issues an expanded opinion on AI (verification, confidentiality, informed consent, agents)"
    url: https://www.calcalist.co.il/local_news/article/bkqvhskyfe
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): the same-word test; verified vs reported findings"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
last_verified: "2026-11-02"
---

# 12.2 · Discovery

The partners are arguing about a tool. The associates are already using tools, and the firm's own records hide both that and the work a tool would change. In this lesson you interview people who will only talk if they are safe, measure AI use from the logs rather than the survey, find the research time the activity codes hide, check a real memo's citations against the firm's corpus, and write the findings memo. At the end you have a findings memo with every finding labelled and nobody named.

## The situation

Monday 16 November to Thursday 26 November 2026. Your charter is agreed, Yoav has told the supervising partners which associates you will meet, and you have the data room. The readout to the management committee is on Thursday 3 December, the first exit point.

Two things are different from a company. First, associates depend on partners for their careers in a way employees rarely depend on a single manager; anything that can be traced to them can end a path to partnership. Second, lawyers are trained to say the defensible thing. "We never put client information in AI tools" is a sentence a lawyer can say in good faith while not knowing what the person at the next desk does at 23:00.

IBM's consulting certificate gives you the *same-word test* and the split between *verified* and *reported* findings. At Atlas & Rowe the words that mean different things to different people are "research", "checked", "anonymised" and "current".

## What to do

### Step 1 — Decide whom you ask what, and how you protect them

Use the [stakeholder map](../../templates/stakeholder-map.md) from [02.1](../module-02/lesson-01.md). For each person, one line on what only they know:

| Person | What only they know | Protection |
|---|---|---|
| Noa Friedman (partner, Tech & IP) | What her group uses today and since when | Promise not to use it for blame; she is a partner, but her associates are not |
| Tamar Golan (knowledge management) | Which precedents are stale; what the vendor would index | She has been ignored; credit her by name if she wants it |
| Karim Nassar (senior associate, litigation) | How research is really done and checked; what nearly went wrong | Nothing attributed; never ask for a colleague's name |
| Yana Petrenko (junior, International desk) | What a junior does alone at night | The hardest case: explain how notes are used before any question |
| IT (proxy, DLP) and finance (expenses) | What the logs show | Ask for extracts by user ID, not names |

Write in your notes how you will report: by group or role, never by person, and minimum group sizes so that "the one Russian-speaking junior on the International desk" is not a group of one.

### Step 2 — Interview for the work, and run the same-word test

Use the [interview guide](../../templates/interview-guide.md) and [02.2](../module-02/lesson-02.md). Ask for the last real task, step by step, not for opinions about AI. Then test the four words:

- **"Research"**: Karim means opening rulings and checking appeals; a partner reading a bill means the line coded RES; finance means nothing, because it has no such category.
- **"Checked"**: Shmuel means "read in pencil"; an associate at 23:00 means "it looked right".
- **"Anonymised"**: the survey and Noa's draft policy mean "client name removed"; the ethics committee's 2026 opinion, as reported, treats anonymisation as not enough on its own, because a deal can be identified from its terms.
- **"Current"**: in the precedent bank it is the default value of a field, not a review.

Run three interviews (roleplay or transcript): [Karim](../../labs/module-12/personas/karim-senior-associate.md) ([transcript](../../labs/module-12/personas/transcripts/karim-senior-associate.md)), [Yana](../../labs/module-12/personas/yana-junior-associate.md) ([transcript](../../labs/module-12/personas/transcripts/yana-junior-associate.md)) and [Tamar](../../labs/module-12/personas/tamar-km.md) ([transcript](../../labs/module-12/personas/transcripts/tamar-km.md)); add [Noa](../../labs/module-12/personas/noa-tech-partner.md) ([transcript](../../labs/module-12/personas/transcripts/noa-tech-partner.md)) if you have time. Then run each through the [coach prompt](../../labs/common/coach-prompt.md).

### Step 3 — Measure AI use from the logs, not the survey

This is the shadow-AI census from [01.6](../module-01/lesson-06.md), on four sources that disagree:

| Source | What it shows | Atlas & Rowe |
|---|---|---|
| `surveys/ai-use-survey-2026-10.csv` | What 47 of 90 lawyers chose to say | Weekly or daily use 28%; "never put client information in" 89%; nobody answered "yes" |
| `it/proxy-ai-domains-2026-09-10.csv` | Office and VPN traffic to AI sites, by user, 1 Sep – 31 Oct | 52 lawyers (43 of 64 associates, 9 of 26 partners) plus 11 staff; 27 lawyers uploaded 171 files |
| `finance/expense-claims-software-2026.csv` | What the firm pays for | 58 "ChatGPT Plus" claims, ₪4,225, six people in Tech & IP, approved by their partner |
| `it/dlp-alerts-2026.csv` | When a client marker left the building | A client-confidential draft SPA on 3 September; three more client-marker alerts in October, still open |

Join the proxy log to `people/lawyers.csv` on `user_id` = `lawyer_id` to count by role and group. Read the limits aloud in your memo: the proxy sees only office and VPN traffic, not phones or home networks, so 52 is a floor. One interview will tell you why it is a floor.

### Step 4 — Find the research the codes hide

The firm records time in six-minute units with an activity code. If you count the code `RES`, research looks marginal. Read the narratives instead. In a spreadsheet, add a column to `billing/time-entries-2026-q3.csv` that is 1 when the narrative contains "research", "case law", "precedent", "rulings", "פסיקה" (case law), "מחקר" (research), "תקדימים" (precedents) or "פסקי דין" (judgments):

```text
=IF(SUMPRODUCT(--ISNUMBER(SEARCH({"research","case law","precedent","rulings","פסיקה","מחקר","תקדימים","פסקי דין"},J2)))>0,1,0)
```

Then pivot hours by role and by that flag, and compare with the `RES` code. The result on the extract (three groups, 40 lawyers, July–September):

| | Hours | Coded RES | Research by narrative |
|---|---|---|---|
| Associates | 10,417 | 6.2% | **25.2%** |
| Partners | 4,055 | 3.7% | 5.1% |

And who pays for research, on matters that are not fixed-fee (`written_off_hours` ÷ `hours`): **RES lines 40.0% written off**, research recorded as drafting or review 12.0%, everything else 4.3%. The story behind the numbers comes from Step 2: partners cut research lines at billing review, so associates code research as drafting. Two consequences for the AI decision: the work a research tool changes is about four times larger than the codes say, and much of its cost is already borne by the firm, not the client.

**Track B (Python).** `python discovery.py` (in the module download, `labs/module-12/`) computes this table, the write-offs, the proxy-versus-survey counts, the knowledge-bank review state and the NDA history in one run. Python is worth it here because the narrative flag is a pattern you will refine (Hebrew prefixes, new phrases) and re-run every time you change it.

### Step 5 — Check one real memo against the corpus

The data room has one research memo exported with its reviewers' comments: `research/memo-non-compete-draft-v2.md`. A partner wrote "good, send to the client today" the morning after it was drafted. Check its four citations yourself against `knowledge/corpus/` (open each file and read the numbered paragraph):

| Point | Citation | What you find |
|---|---|---|
| 1 | FCR-2020-460 ¶3 | Exists and says it; but FCR-2022-390 ¶4 reverses it on this point |
| 2 | FCR-2022-318 ¶6 | **No such document** in the corpus (or, per the comment, anywhere) |
| 3 | FCR-2021-124 ¶5 | Exists; says the **opposite**: payment supports enforcement "but does not make it valid on its own" |
| 4 | FCR-2025-049 ¶3 | Exists and supports the claim |

All rulings in the corpus are fictional; what matters is the pattern, which is the one courts have sanctioned in New York and criticised in Israel: an invented authority, a reversed one presented as current, and a real one misstated, approved by a busy supervisor. Do not try to find out who drafted it. Report it to Yoav as a near miss, and route it to Orit (12.4).

### Step 6 — Read the knowledge bank the tool would search

From `km/precedent-bank-index.csv`: 1,180 documents; **71% have never been reviewed**; a few hundred documents carry most of the use (the top 300 = 86% of uses in the last 12 months); 105 documents tagged privacy are still "current" and were last reviewed (if ever) before Amendment 13 to the Privacy Protection Law (תיקון 13 לחוק הגנת הפרטיות) came into force on 14 August 2025. In the 78-document research export, compare the index's status with what the documents themselves say ("We therefore reverse…", "This replaces the earlier note…"): the index marks 2 of the 13 stale documents.

### Step 7 — Write the findings memo

Use the [findings memo](../../templates/findings-memo.md) from [02.7](../module-02/lesson-07.md). Answer first. Each finding labelled **measured** (from a file you name), **reported** (interviews, unattributed) or **inferred**, with its consequence and its owner. No names. A finding about a person is a finding about a system: "a memo with an invented citation was approved for sending" is about the checking step, not the junior.

## Watch out

- **Believing the survey.** Lawyers answer surveys defensibly. The proxy, the expenses and the DLP log are behaviour; the survey is what people chose to say. Use both and label both.
- **Treating the proxy count as the total.** It misses phones and home networks. Say "at least".
- **Naming the junior.** The near miss is the most persuasive fact you have. It is worthless if it ends a career, and you will never hear another one.
- **Counting codes.** A code is a billing convention. The narrative is closer to the work, and the interview tells you why they differ.
- **Calling it a breach.** "A client-confidential document was uploaded to a consumer AI site" is a fact. Whether it breached confidentiality or privilege is Orit's question.
- **Skipping the knowledge bank.** A research tool searches what is there. If you discover the bank is stale only in the pilot, you have tested the wrong thing.

## Your turn

### Inputs

- Data room (module download): `billing/time-entries-2026-q3.csv`, `people/lawyers.csv`, `it/proxy-ai-domains-2026-09-10.csv`, `it/dlp-alerts-2026.csv`, `finance/expense-claims-software-2026.csv`, `surveys/ai-use-survey-2026-10.csv`, `km/precedent-bank-index.csv`, `knowledge/corpus/`, `research/memo-non-compete-draft-v2.md`, `risk/ethics-log-2026.csv`.
- Personas: [Karim](../../labs/module-12/personas/karim-senior-associate.md), [Yana](../../labs/module-12/personas/yana-junior-associate.md), [Tamar](../../labs/module-12/personas/tamar-km.md), [Noa](../../labs/module-12/personas/noa-tech-partner.md), with transcripts in `labs/module-12/personas/transcripts/`; [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [stakeholder map](../../templates/stakeholder-map.md), [interview guide](../../templates/interview-guide.md), [shadow-AI survey](../../templates/shadow-ai-survey.md), [findings memo](../../templates/findings-memo.md).

### Steps

1. Write the stakeholder map with a protection line per person and your reporting rule.
2. Interview at least three people (roleplay or transcripts); run each through the coach.
3. Build the AI-use table from the four sources, with limits stated.
4. Flag research in the time entries; compute the research share by role and the write-off rates.
5. Check the memo's four citations against the corpus.
6. Profile the knowledge bank: never reviewed, privacy documents since Amendment 13, the stale documents in the research export.
7. Write the findings memo (answer first; every finding labelled; no names).

**Track B (Python).** `python discovery.py` for steps 3, 4 and 6; then check your spreadsheet numbers against it.

### Time

180 minutes: 60 for interviews, 30 for the AI-use table, 30 for the time entries, 15 for the memo check, 15 for the bank, 30 for the findings memo.

### Done when

- [ ] Every interview opened by saying how notes are used; nothing in your memo identifies an associate.
- [ ] The AI-use finding sets logs against the survey and says the proxy count is a floor.
- [ ] Research is measured from narratives (≈ 25% of associate hours, not ≈ 6%), with write-off rates by type of line.
- [ ] Each of the memo's four citations is marked exists / reversed / misstated / supports, and the near miss is routed, not attributed.
- [ ] The knowledge-bank finding gives the never-reviewed share and the stale documents the index misses.
- [ ] Every finding is labelled measured, reported or inferred, with a consequence and an owner.

<details><summary>Reference answer</summary>

The full memo is `labs/module-12/expert/02-findings-memo.md`. Its spine:

**Answer first:** the firm is not choosing whether to use AI; it is already in client work without a rule, consent or a check, a fabricated citation nearly reached a client, the knowledge base is mostly unreviewed, and on half the fees time saved is fees lost. The question is the order.

**Measured:** 52 lawyers on AI sites (43 of 64 associates, 9 partners), 27 uploaded 171 files, against a survey where 89% say no client information goes in; a client-confidential draft SPA uploaded on 3 September, three client-marker alerts open; 58 ChatGPT Plus claims in Tech & IP (₪4,225 in 2026); research 25.2% of associate hours by narrative vs 6.2% coded; RES lines written off 40.0% vs 4.3% for other work; associates at 81% of target; 71% of the bank never reviewed; 105 privacy documents not reviewed since Amendment 13; 13 stale documents in the research export, 2 marked.

**The memo:** point 1 reversed (FCR-2020-460 by FCR-2022-390), point 2 invented (FCR-2022-318), point 3 opposite (FCR-2021-124 ¶5), point 4 sound.

**Reported (unattributed):** research is coded as drafting because research lines are cut; checking a citation properly takes about ten minutes; juniors use free tools at night; an error was caught by a person, not a control, and not reported.

**What the transcripts' interviewers missed:** Karim's own use on his phone (why the proxy count is a floor); Yana's uploads of Russian client documents to translation tools (the June DLP alert and the April ethics-log entry point to it); Tamar's offer of what a review would take.

</details>

## References

- IAPP, [Amendment 13 to Israel's Privacy Protection Law](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform) (in force 14 August 2025): why pre-August 2025 privacy precedents need review. The content of that review is counsel's.
- Calcalist, [the Bar Association ethics committee's expanded AI opinion](https://www.calcalist.co.il/local_news/article/bkqvhskyfe) (17 September 2026): background for the same-word test on "anonymised"; read it with the ethics partner in 12.4.
- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): same-word test, verified vs reported (named, not re-taught).
- Field kit: [01.6 · The shadow-AI census](../module-01/lesson-06.md), [02.1 · Stakeholder map](../module-02/lesson-01.md), [02.2 · The discovery interview](../module-02/lesson-02.md), [02.4 · Measuring a baseline](../module-02/lesson-04.md), [02.7 · The findings memo](../module-02/lesson-07.md).
- Templates: [stakeholder map](../../templates/stakeholder-map.md), [interview guide](../../templates/interview-guide.md), [shadow-AI survey](../../templates/shadow-ai-survey.md), [findings memo](../../templates/findings-memo.md).
- Earlier: [12.1 · The call](lesson-01.md). Next: [12.3 · Diagnosis](lesson-03.md).
