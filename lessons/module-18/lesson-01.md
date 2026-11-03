---
id: "18.1"
module: 18
minutes: 18
practice_minutes: 180
prerequisites: ["01.1", "01.2", "01.5", "02.1", "07.9", "16.1"]
objectives:
  - "Plan a whole engagement on one page before reading deeply: phases, exits, the deliverables each phase owes and the date each method step happens."
  - "Get a mandate from a sponsor who has already chosen a solution, with the objective read back and the stated ask recorded as the claim you test."
  - "Run the first-day read on an unseen data room and sort what you find into verified, contradicted, claim to test and unverifiable, without anyone telling you what matters."
  - "Write down your working hypotheses and what evidence would disprove each, before your first interview."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): seven courses ending in a capstone advisory package for a realistic company"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "IAPP, Israel marks a new era in privacy law: Amendment 13 ushers in sweeping reform (in force 14 August 2025)"
    url: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
  - title: "Privacy Protection Law, 5741-1981 (חוק הגנת הפרטיות), Hebrew Wikisource: section 2(9), use for another purpose"
    url: https://he.wikisource.org/wiki/חוק_הגנת_הפרטיות
last_verified: "2026-11-03"
---

# 18.1 · The unseen org

This is the engagement nobody walks you through. A private academic college has asked for an AI early-warning system that predicts which students will drop out; the board wants one recommendation in twelve weeks. You get the brief, a data room, nine people and the method you have practised in ten organizations, and no hints about what is going on. In this lesson you plan the whole engagement, get the mandate, read the data room on the first day and write down what you think before you look further. At the end you have a charter, a first-read sheet, an access request, an engagement plan to the board date and a hypotheses log.

## The situation

Sunday 7 February 2027. You run a two-person AI transformation practice. Tzurim Academic College, a fictional private college in the southern Shfela with about 6,840 students and 712 staff, has engaged you for a fixed fee of ₪186,000 in three four-week phases, with an exit after each. On 20 January the CEO, Yaron Bar-Lev, told the board that first-year dropout had jumped from 12% to almost 20% and proposed an AI early-warning system from a US vendor, with a free pilot from March. The board asked for an outside review and one recommendation on Tuesday 4 May 2027. Read the [engagement brief](../../labs/module-18/brief.md) in the module download now, before anything else in this lesson.

What is different from modules 8–17:

- **No lesson tells you what to look at.** In each earlier engagement, NN.2 pointed you at the files and the people that mattered and NN.4 named the hard part. Here you decide. Deciding what to read, whom to meet and what to ignore is the skill being tested.
- **No hidden truth until you submit.** The project page has a reveal block and the module download has an `expert/` folder. **Opening either before you submit your deliverables wastes the capstone.** You get one unseen engagement in this course; a debrief only teaches you something if your work was done without it. The same goes for the data room's `generate.py` and its `.py` parts: they contain the answer.
- **The whole deliverable set, together.** Charter, findings memo, readiness assessment, portfolio and ROI, roadmap, policy pack, pilot and eval, adoption plan, decision-ready case, decision record, handover and a recorded presentation, consistent with each other. Lesson [18.2](lesson-02.md) checks them against each other; [18.3](lesson-03.md) is the presentation.

IBM's consulting certificate ends in a capstone too: an advisory package for a realistic company built from a brief and a partial data room. Here the data room is real-shaped, the people answer back, and the pilot has to run.

## What to do

### Step 1 — Plan the whole engagement on one page first

In the earlier engagements the lessons paced you. Now the calendar does. Before you read deeply, lay the method over the twelve weeks, so that the expensive steps (interviews, the pilot, the integration check, the rehearsal) have dates and the phase exits have deliverables.

A worked example of the shape, from Kinneret Plastics ([13.1](../module-13/lesson-01.md)), where the internal lead had about eleven weeks from the ask to the management meeting: week 1 mandate and first read; weeks 2–3 discovery including a night on the floor; weeks 4–5 diagnosis and the one-page case to the CFO; weeks 6–7 the readiness bar (written before the vendor presented) and the verdict; weeks 8–10 the audit and the pilot; week 11 the readout, the integration check and the rehearsal with the owner. Two lessons from that plan carry over: the bar for any vendor was dated before the vendor's evidence arrived, and the rehearsal with the person who made the ask had its own slot, not the last evening.

For Tzurim, your plan answers:

| Question | Where you decide it |
|---|---|
| What does each phase owe the client at its exit (4 March, 1 April, 4 May)? | Charter, payment schedule |
| Which method steps happen in which week? (discovery 02.1–02.7, portfolio 03.1–03.9, guardrails 04.1–04.8, pilot 05.1–05.7, adoption 06.1–06.5, readout 07.1–07.9) | Engagement plan |
| When must the readiness bar for any AI option be written, and against which external date? | Engagement plan |
| When does the pilot's test set exist, and when do the thresholds get dated? | Pilot charter (05.1) |
| What falls on holidays or exam periods? (Passover 2027 is 21–29 April) | Engagement plan |
| Where are the rehearsal and the pre-read? | Engagement plan |

A phase exit is a real risk for an outside consultant: the client can stop after phase 1. Make each exit leave the client with something it can use even if you never come back ([01.1](../module-01/lesson-01.md) on phases you can exit).

### Step 2 — Write down what your entry role changes

Fill the entry-role table from [01.1](../module-01/lesson-01.md) for this engagement: who gave the ask (the CEO, in front of the board, with a vendor already named), who decides (the board; the CEO and the VP Finance release the money), what your position allows (you can say "not yet" without losing a job, and you can be stopped after phase 1), what the data access is (exports through the VP Administration; you are an outside processor under a data processing addendum), and who else claims a say (the brief mentions the President). Each row becomes a line of the charter.

### Step 3 — Get the mandate from a sponsor who has chosen a solution

The method is [01.2](../module-01/lesson-02.md): the objective in the sponsor's words, read back, and "done" defined before anyone looks at evidence. Two objectives exist and the charter holds both:

- **The stated ask**, recorded as *the claim this work tests*: the CEO's sentence from the brief, with his number and his vendor in it.
- **The objective** you propose for him to correct: the board's question, in the board's terms, with the AI option as one of the things tested.

Interview Yaron (roleplay: [Yaron Bar-Lev](../../labs/module-18/personas/yaron-ceo.md); no-roleplay path: [the transcript](../../labs/module-18/personas/transcripts/yaron-ceo.md)), then run the transcript through the [coach prompt](../../labs/common/coach-prompt.md) with the persona's checklist. A sponsor who has picked a vendor will push to start it "in parallel". Decide before the meeting what you will say about the pilot date, and put it in writing afterwards: the brief tells you what the board decided about vendor pilots and student data.

Write an **urgent-finding rule** into the charter before you open any data, as at Open Hands ([16.1](../module-16/lesson-01.md)): who hears about an exposure of personal information, or anything else that cannot wait for a readout, how and when. Every engagement that touches personal data needs one; a college's data is about thousands of young adults, some of it sensitive by nature.

### Step 4 — Read the data room on the first day

Follow [01.5](../module-01/lesson-05.md): inventory every file with its provenance, list what is missing, and sort every headline statement you find into **verified** (you saw it in data or a signed document), **contradicted** (another file says otherwise), **claim to test** (someone asserts it; the data could check it) and **unverifiable** (nothing in the room can check it yet). Start from the data room's [INDEX](../../labs/module-18/data-room/INDEX.md); it describes files, not findings.

Three rules for an unseen room:

1. **Read the footnotes and the column headers before the headlines.** Definitions, dates and units live there.
2. **Note every number that appears in two files.** If the two disagree, that is your first lead; if they agree, check whether one was copied from the other.
3. **Note every document's date against the events it should reflect.** A policy written before a system existed cannot govern it.

Your first read will be incomplete. That is fine; it is a list of what to test, not a conclusion.

### Step 5 — Decide whom to meet, and in what order

The brief gives you the sponsor on day 2. The rest of the [cast](../../labs/module-18/personas/README.md) is your call. Use the [stakeholder map](../../templates/stakeholder-map.md) from [02.1](../module-02/lesson-01.md), and sequence by three questions:

- **Who makes the numbers?** The people who produce a report know how it is made; ask them how, not whether it is right.
- **Who do the processes touch?** The people at the end of a process see where it breaks. Somebody affected by the decisions belongs in discovery, not only in the comms plan.
- **Who can stop it later?** Finance, the academic side, the workers' representatives, the data protection officer. Meet them before anything is fixed.

Plan the interviews with the [interview guide](../../templates/interview-guide.md) ([02.2](../module-02/lesson-02.md)): workflow questions, the same-word test, and how you protect people who tell you something uncomfortable. Remember that the transcripts are a competent but hurried interviewer's; each one leaves something unasked.

### Step 6 — Write your hypotheses down before the first interview

An unseen engagement tempts you to find what you expected. Protect yourself with a **hypotheses log**: a short table you write now and update after every interview and every analysis.

| # | Hypothesis | Evidence that would support it | Evidence that would disprove it | Status / date |
|---|---|---|---|---|
| H1 | [your hypothesis] | [which file, which person] | [which result would make you drop it] | open, 7 Feb |

Write at least one hypothesis that *agrees* with the sponsor and at least one that does not. Writing the disproving evidence first is the point: it stops you reading every new fact as support.

### Step 7 — Send the access request and the first-week plan

Use the [access request pack](../../templates/access-request-pack.md): what you still need, from whom, in what form (aggregate or row-level, which fields), and why. Ask for definitions and logs as well as data. Then a [first-week plan](../../templates/30-60-90-plan.md) that names, for each meeting, what you want to find out. End the week with a short note to the sponsor: what you are doing, the date he gets an answer, nothing you have not earned.

## Watch out

- **Opening the expert folder "just to see the format".** The format is in the templates. The expert folder is the answer; once read, it cannot be unread.
- **Answering the stated ask.** Planning the vendor pilot's evaluation in week 1 accepts the CEO's framing before you know whether prediction is the problem. Keep the ask as a claim.
- **Planning by template instead of by question.** Twelve templates filled at equal depth is a lot of paper and little judgment. Decide which two or three questions decide the board's answer, and spend most of your hours there.
- **Leaving the pilot for the last two weeks.** A test set, dated thresholds and a shadow-mode decision take time; put the pilot's dates in the plan on day 1.
- **Meeting only managers.** The people who make the numbers and the people the processes touch are where findings come from.
- **Treating a transcript as complete.** Each one leaves at least one thing unasked. If you do not roleplay, mark what you would have asked.
- **Skipping the urgent-finding rule because it seems unlikely.** You write it so you do not have to decide what to do at 17:00 on a Sunday.

## Your turn

### Inputs

- [Engagement brief](../../labs/module-18/brief.md) and the [data room INDEX](../../labs/module-18/data-room/INDEX.md) (module download).
- Persona: [Yaron Bar-Lev](../../labs/module-18/personas/yaron-ceo.md), or his [transcript](../../labs/module-18/personas/transcripts/yaron-ceo.md); [coach prompt](../../labs/common/coach-prompt.md); the [cast](../../labs/module-18/personas/README.md).
- Templates: [engagement charter](../../templates/engagement-charter.md), [scope boundary](../../templates/scope-boundary.md), [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md), [stakeholder map](../../templates/stakeholder-map.md), [30-60-90 plan](../../templates/30-60-90-plan.md).
- [Capstone checklist](../../labs/module-18/capstone-checklist.csv) (module download).

### Steps

1. Write the one-page engagement plan from 7 February to 4 May: phases and exits, each method step's week, the date the readiness bar is written, the pilot's dates, the pre-read, the rehearsal.
2. Fill the entry-role table (five rows).
3. Interview Yaron (or annotate his transcript with what was missed). Read the objective back; agree "done"; settle what happens to the vendor pilot while you work.
4. Write the charter: objective, the stated ask as a claim, done, scope with reasons, advisory boundary with named roles, urgent-finding rule, reporting rhythm.
5. Do the first read of the whole data room: every file with provenance; at least ten statements sorted with evidence; what is missing.
6. Write the hypotheses log (at least five, with disproving evidence), the access request, the first-week plan and a note to Yaron of at most six lines.

### Time

180 minutes: 20 for the engagement plan, 15 for the entry role, 30 for the sponsor interview and coaching, 30 for the charter, 50 for the first read, 35 for the hypotheses, the access request, the plan and the note.

### Done when

- [ ] The engagement plan dates every method step, the readiness bar, the pilot's test set and thresholds, the pre-read and the rehearsal, and each phase exit leaves the client something usable.
- [ ] The objective is the sponsor's, read back, in the board's terms; the stated ask appears as the claim tested.
- [ ] "Done" includes labelled numbers, owners and dates, and a rule on vendor data sharing consistent with the board's decision.
- [ ] The charter has an urgent-finding rule with names and a same-day route.
- [ ] At least ten statements are sorted with the file and the reason; at least one is "contradicted" or explains why none was found.
- [ ] The hypotheses log has at least five hypotheses, one that agrees with the sponsor and one that does not, each with disproving evidence written first.
- [ ] You have not opened `expert/`, the project's reveal block or any `.py` file in the data room.

<details><summary>Reference answer</summary>

This reference covers only what a strong consultant writes before discovery: it contains no findings from the data room. The expert's full set opens after you submit (see the [capstone project](../../projects/m18-capstone.md)).

**Engagement plan (excerpt).** Phase 1 (7 Feb – 4 Mar, exit: findings memo and a written position on the vendor pilot): week 1 mandate, first read, access request; weeks 2–3 interviews with the people who make the numbers, the people the processes touch and the ones who can stop it; week 4 profiling and baselines, findings memo. Phase 2 (7 Mar – 1 Apr, exit: readiness assessment, scored portfolio, ROI, roadmap draft, policy pack draft): readiness bar written by 1 March, before any vendor call; vendor meeting mid-March; netting with finance. Phase 3 (4 Apr – 4 May, exit: pilot eval, adoption plan, case, presentation): test set built and thresholds dated by 6 April; eval by 20 April; integration check 15–19 April; pre-read 20 April (before Passover); rehearsal with the executive most likely to resist on Sunday 2 May; board 4 May.

**Objective (as read back to Yaron, his correction in italics):** "By 4 May, find out why first-year students leave Tzurim and what would make fewer of them leave, test whether an AI early-warning system such as Persevia would do that better than other options, and bring the board one recommendation with costs, risks and dates *that the board can track every semester*."

**Stated ask tested:** "Dropout rose from 12% to almost 20%; an AI early-warning system (Persevia) will bring first-year dropout to 12% by 2029."

**Done:** one recommendation minuted with owners and dates; every number labelled measured, directional or assumed, and every headline figure's definition stated by its owner; any AI option judged against criteria written before the vendor's evidence; no student data to any vendor before the DPO's written review (board decision 2); any exposure of personal data reported the same day.

**Urgent-finding rule:** "Any exposure of personal information I see: phone Tamar Weiss (VP Administration) and the DPO the same day; written note within 24 hours; I do not investigate further on my own."

**Scope:** first-degree students admitted 2023–2025, first-year leaving above all; every process that touches a first-year between admission and the second year; every AI system in use or proposed that touches students or staff; AI policy and governance. Out: MBA, teaching quality and curriculum (the academic council's), replacing core systems.

**Hypotheses log (excerpt; disproving evidence first):**

| # | Hypothesis | Would disprove it |
|---|---|---|
| H1 | First-year leaving really rose between cohorts 2023 and 2025 (agrees with the sponsor) | Recomputing the figure from the registry, status by status, does not reproduce the report's trend |
| H2 | Advisers could keep more students if they knew earlier who was at risk (agrees) | Leavers were already known to the college through some other process, or advisers cannot act on the main reasons for leaving |
| H3 | Something the college itself does pushes students out (does not agree) | No college process step precedes leaving more often than chance |
| H4 | The vendor's evidence transfers to an Israeli private college (agrees) | The case study's population, measure or conditions differ materially |
| H5 | AI is already used on student data somewhere without rules (neutral) | The inventory, the proxy, the survey and the systems list show no AI use touching student data |

**Note to Yaron (six lines):** "Yaron — the work is aimed at what you asked the board for: fewer first-year students leaving, proven. This week I meet the people who produce the numbers and run the student processes. Nothing goes to any vendor until the DPO has reviewed the terms, as the board decided; you get my view on the pilot by 18 February. By 4 May the board gets one page it can approve. Next note: 25 February."

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): its capstone advisory package (named, not re-taught).
- IAPP, [Israel marks a new era in privacy law: Amendment 13](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform): in force 14 August 2025; why student data gets an urgent-finding rule. Route legal questions to the DPO.
- [Privacy Protection Law, 5741-1981](https://he.wikisource.org/wiki/חוק_הגנת_הפרטיות), section 2(9): using information for a purpose other than the one it was given for. Hebrew Wikisource; check the current version.
- Field kit: [01.1 · Three ways in](../module-01/lesson-01.md), [01.2 · Getting a real mandate](../module-01/lesson-02.md), [01.5 · The first-day data-room read](../module-01/lesson-05.md), [02.1 · Stakeholder map](../module-02/lesson-01.md), [02.2 · The discovery interview](../module-02/lesson-02.md), [07.9 · Handover](../module-07/lesson-09.md); [16.1 · The call](../module-16/lesson-01.md) (urgent-finding rule).
- Templates: [engagement charter](../../templates/engagement-charter.md), [scope boundary](../../templates/scope-boundary.md), [data-room first read](../../templates/data-room-first-read.md), [access request pack](../../templates/access-request-pack.md), [stakeholder map](../../templates/stakeholder-map.md), [interview guide](../../templates/interview-guide.md), [30-60-90 plan](../../templates/30-60-90-plan.md).
- Capstone: [the project and rubric](../../projects/m18-capstone.md). Next: [18.2 · The full deliverable set and the integration check](lesson-02.md).
