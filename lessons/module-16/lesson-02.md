---
id: "16.2"
module: 16
minutes: 18
practice_minutes: 120
prerequisites: ["16.1", "01.6", "02.2", "02.5", "02.7"]
objectives:
  - "Run a shadow-AI census in a 20-minute staff meeting and seven 30-minute interviews, protecting the people who tell you what they really do."
  - "Count who can see family and donor information from a Drive sharing export, and name which roles need it."
  - "Interview the person affected — a parent — in a way that respects her, and carry her words into the findings without exposing her."
  - "Write a same-day note for an urgent exposure and a two-page findings memo with measured, reported and inferred labels."
volatility: implementation
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera): due diligence on claims and signals"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Google, Gemini Apps Privacy Hub (personal accounts): activity used to improve services incl. training; reviewed chats kept up to three years (updated 26 October 2026)"
    url: https://support.google.com/gemini/answer/13594961
  - title: "Google Workspace, Generative AI in Google Workspace Privacy Hub (updated 6 October 2026)"
    url: https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub
  - title: "Social Workers Law, 5756-1996, English translation (IFSW): section 8, professional confidentiality"
    url: https://www.ifsw.org/wp-content/uploads/2021/03/Social-Workers-Law-1996-Israel.pdf
last_verified: "2026-11-03"
---

# 16.2 · Discovery

Discovery at a 30-person nonprofit takes days, not weeks, because there are only seven or eight people whose work you need to see — and because you cannot afford more. In this lesson you turn a staff meeting into a census, interview the people who write, the person who controls access, a volunteer and a parent, count who can see family information from one export, and write the findings memo. At the end you have interview notes, an access count, a same-day note to the executive director and a findings memo with every claim labelled.

## The situation

Week 1, Monday 16 – Thursday 19 November. Ronit gave you 20 minutes at the Monday staff meeting and booked Noa (development), Samah (senior coordinator, in Shefa-'Amr), Yossi (operations and IT, Tuesday) and Vova (treasurer, by phone). You asked for Etti, a long-time respite volunteer, and, through Samah, a parent. Your budget for the week is 12 hours, three of them already spent on the first read.

[02.2](../module-02/lesson-02.md) taught the discovery interview and the same-word test; [01.6](../module-01/lesson-06.md) the shadow-AI census; [02.5](../module-02/lesson-05.md) whether you may use data for a purpose. IBM's consulting certificate calls the habit you need most here *due diligence on claims*: every number you were handed — "half my week", "only coordinators see family files", "no budget" — gets traced to where it came from before you repeat it.

## What to do

### Step 1 — Turn the staff meeting into the census

Ronit's own form ([`it/staff-ai-survey-2026-10.csv`](../../labs/module-16/data-room/it/staff-ai-survey-2026-10.csv)) already tells you a lot: 22 of 30 answered; 18 use AI; among them 11 on a personal account and 4 on "both"; 3 pasted family information "with details", 4 "prefer not to say". Read the non-response and the "prefer not to say" as signal: at least 7 people are unsure whether what they do is allowed. Volunteers were never asked.

You do not need a better survey. You need people to show you their work. Use the 20 minutes like this:

1. **Who you are** (2 minutes): a volunteer for four weeks, not an auditor; nothing is attributed by name.
2. **What you are looking for** (3 minutes): "where the writing hurts" — not "who uses AI".
3. **One sentence that changes the room:** "If you already use AI to get through the reports, you are not in trouble; you are the person I most need to talk to."
4. **Ask for an invitation, not an answer**: "Who would show me, in 20 minutes, how they did the last quarterly report?" Write down names.
5. Ask Liat to send volunteers the same question in WhatsApp, one line, and to tell you who answers.

### Step 2 — Interview by asking to be shown

Seven interviews of 30 minutes, in an order that follows the information: development and a coordinator first (they do the writing), Yossi next (he can tell you where the data sits), then a volunteer, the treasurer and, if she agrees, a parent. For each person, the move that works is the same: **ask them to walk you through the last time they did the task**, step by step, with the tools in front of them. "Do you use ChatGPT?" gets "sometimes". "Show me how you wrote the Bar-Natan proposal" gets the tool, the account, what went in, and who pays.

Before any question about tools, agree what will and will not be attributed. With social workers, say why: they are bound by professional confidentiality under the Social Workers Law, 5756-1996 (חוק העובדים הסוציאליים), section 8, and a coordinator who pasted notes into her personal account knows it. She will tell you only if she believes you are trying to fix the work, not to find a culprit.

What the four writing and IT interviews give you, if you ask for the work (personas: [Noa](../../labs/module-16/personas/noa-development.md), [Samah](../../labs/module-16/personas/samah-coordinator.md), [Yossi](../../labs/module-16/personas/yossi-operations-it.md), [Etti](../../labs/module-16/personas/etti-volunteer.md)):

- **How the funder narratives are really written**: notes in Hebrew, thinking in Arabic, English for the foundation — on a personal Gemini account, pasted with first names and diagnoses, at night.
- **Where donor data went**: the same question asked as "how did you build the Giving Tuesday segments?" rather than "do you upload data?".
- **How volunteers get information**: the care-sheet link pinned in every WhatsApp group; medication changes typed with the child's name.
- **What happens when someone leaves**: nothing.

Why personal accounts matter is not abstract. Google's own privacy page for personal Gemini accounts says activity is used to improve its services, including training models, while "Keep Activity" is on, and that a subset of chats is reviewed by people and kept for up to three years. The same chats on an organization's Workspace account fall under Workspace terms: not used for training without permission and not reviewed by humans. The tool is the same; the account decides the exposure.

### Step 3 — Count who can see what, with Yossi

Open [`it/drive-sharing-audit.csv`](../../labs/module-16/data-room/it/drive-sharing-audit.csv) with Yossi on Tuesday and count, in a pivot table, principals per item and type. Then compare with [`people/staff.csv`](../../labs/module-16/data-room/people/staff.csv) (roles) and [`people/volunteers.csv`](../../labs/module-16/data-room/people/volunteers.csv) (status, confidentiality form). Worked example:

| Item | What it holds | Accounts | Who | Roles that need it |
|---|---|---|---|---|
| `Families` (shared drive) | Case notes, intake, referrals, committee letters | **46** | 13 organization accounts (11 staff, 2 national-service volunteers), 2 **former staff**, **31 personal** (a long-time volunteer, 7 active and **23 inactive** volunteers) | **9**: six coordinators, the head of family services, the rights advisor, the intake coordinator |
| `Families/Respite (weekend care sheets)` | Each child's medication, allergies, behaviour plan | Anyone with the link (since **14 August 2024**) + 37 volunteers by email | | The volunteers of the next weekend |
| `Donors 2026 (master)` | 1,134 donors; ID numbers on file for 851; 37 notes about a donor's child, diagnosis, welfare or bereavement | **14 editors** + anyone at the domain with the link can edit | 9 organization accounts, **5 personal**: three phone-a-thon volunteers, the treasurer, and a **former staff member's private Gmail** | Development and the bookkeeper |

Ten items in all are open to anyone with the link: the respite folder, its eight care sheets and the volunteer list. Of the 38 volunteers with any access, 21 have no confidentiality form on file.

The point of counting is not the shock value. It is that each number becomes a specific action for Yossi in 16.4, and one of them — the number of authorized users of a database holding medical information — changes which security level of the Data Security Regulations Open Hands is arguably at. You will read that in 16.4.

### Step 4 — Follow the money

Two files tell you what the stated ask got wrong about "no budget": the [card statement](../../labs/module-16/data-room/finance/card-statement-2026.csv) and the [accounts list](../../labs/module-16/data-room/it/accounts-and-licences.csv). Filter software merchants. Ten Microsoft 365 Business Premium seats were renewed at the nonprofit price on 14 October (₪2,072) after the grant ended; three were used in the last 90 days, two are assigned to former staff. ChatGPT Plus has been charged monthly since March and coded "Office supplies". A GrantGenie account on a personal email has a card on file and a free year that ends on 31 December. Dropbox has not been used since 2024. Lesson 16.3 turns this into money; for now, write each line as a finding with its source.

### Step 5 — Meet the person affected

A parent agreed, through Samah and with Ronit's introduction, to meet you in the Shefa-'Amr room for an hour before her son's school bus comes home (persona: [Lina Mansour](../../labs/module-16/personas/lina-parent.md); transcript: [here](../../labs/module-16/personas/transcripts/lina-parent.md)). This interview is different from the others, and the persona is written to react to how you treat her:

- **Introduce yourself honestly**: a volunteer, not from the welfare office or National Insurance; nothing she says changes her family's support.
- **Her language.** If you do not speak Arabic, ask her which language she prefers and whether she would like Samah to stay; do not bring an interpreter she has not agreed to.
- **Her story first, in order.** Ask about her son before anything about information, consent or technology. If you open with "data", she will end the meeting, and she would be right.
- **Promise nothing on Open Hands' behalf.** Promise only what you control: that Ronit will hear her words.
- **Ask what would have made it OK.** It is the question that turns a complaint into a design requirement.

In the worked example she found her son's story — first name, age, town, school and syndrome — in the September newsletter through a neighbour; nobody had asked her; her daughter was teased at school. She is not against stories; she wants to read the text first, in Arabic, and decide what stays out. She wants to know who can see her son's file, and she wants an apology in Arabic from someone senior. Each of those is a line in the policy page you write in 16.5.

### Step 6 — Write the same-day note when it is urgent

The urgent-finding rule from 16.1 applies the moment you see the respite link on Tuesday. Three lines, by phone first and then in writing: what is exposed, since when, and what you propose with whom and when. Worked example:

> Ronit — the respite care sheets (children's medication, allergies, behaviour plans) are open to anyone who has the link, since August 2024, and the link is pinned in every weekend WhatsApp group. 23 former volunteers still have access to `Families`. Yossi and I can close both without stopping this weekend's respite: Amir confirms who needs the sheets. Can I go ahead?

### Step 7 — Write the findings memo

Two pages, using the [findings memo](../../templates/findings-memo.md) from [02.7](../module-02/lesson-07.md): one sentence on top, a table of findings with evidence and a label each — **measured** (you counted it), **reported** (someone told you), **inferred** (your reading) — then what you are not saying. At Open Hands, "what you are not saying" carries weight: that anyone broke the law (counsel), that anyone should be blamed (they used what they had), that AI is the problem (the access problems predate it).

**Track B (Python).** Optional here; the data room is small enough for a spreadsheet. If you prefer, `python discovery.py access donors survey money` (in the module download, `labs/module-16/`) prints every count above with its numerator and denominator, which helps when you re-run the count on the first Tuesday of every month after the fix.

## Watch out

- **Asking "do you use AI?"** You will get the survey's answer again. Ask to be shown the last piece of work.
- **Naming people in the memo.** "A coordinator pastes notes into her personal account" is a finding. Her name in the memo ends discovery for everyone else.
- **Banning before offering.** If your first act is "stop using Gemini", the reports are still due on the 15th and people will hide it. The sanctioned alternative comes the same day as the stop (16.4).
- **Treating the parent as a source.** She is the person the rules exist for. Her words go into the memo with her agreement and without her name.
- **Fixing it yourself.** Your guest account cannot and should not change sharing. Yossi changes it, on Ronit's yes.
- **Counting accounts without roles.** "46 accounts" alarms; "46 accounts, 9 roles need it" tells Yossi what to do.

## Your turn

### Inputs

- Data room (module download): [`it/drive-sharing-audit.csv`](../../labs/module-16/data-room/it/drive-sharing-audit.csv), [`people/staff.csv`](../../labs/module-16/data-room/people/staff.csv), [`people/volunteers.csv`](../../labs/module-16/data-room/people/volunteers.csv), [`it/staff-ai-survey-2026-10.csv`](../../labs/module-16/data-room/it/staff-ai-survey-2026-10.csv), [`fundraising/donors.csv`](../../labs/module-16/data-room/fundraising/donors.csv), [`finance/card-statement-2026.csv`](../../labs/module-16/data-room/finance/card-statement-2026.csv), [`it/accounts-and-licences.csv`](../../labs/module-16/data-room/it/accounts-and-licences.csv), [`policies/volunteer-handbook-extract.md`](../../labs/module-16/data-room/policies/volunteer-handbook-extract.md), [`comms/newsletter-2026-09.md`](../../labs/module-16/data-room/comms/newsletter-2026-09.md), [`policies/consent-form-v1-2019.md`](../../labs/module-16/data-room/policies/consent-form-v1-2019.md), [`cases/case-register.csv`](../../labs/module-16/data-room/cases/case-register.csv).
- Personas and transcripts: [the cast](../../labs/module-16/personas/README.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [interview guide](../../templates/interview-guide.md), [stakeholder map](../../templates/stakeholder-map.md), [shadow-AI survey](../../templates/shadow-ai-survey.md), [findings memo](../../templates/findings-memo.md).

### Steps

1. Write the 20-minute staff-meeting script (Step 1).
2. Interview at least four people: Samah or Noa, Yossi, Etti or Vova, and Lina (roleplay, or read the transcripts and mark what was missed). Coach at least two.
3. Count access to `Families`, the respite folder and the donor sheet, by principal type and by the roles that need it.
4. List the money lines from the card statement and accounts list.
5. Write the same-day note.
6. Write the findings memo: one sentence, at least eight findings with evidence and a label each, what you are not saying.

### Time

120 minutes: 60 for four interviews and coaching, 25 for the access count and money lines, 35 for the note and memo.

### Done when

- [ ] Every interview opened with non-attribution and asked to be shown a real piece of work.
- [ ] You found out, from people, which accounts are used for funder narratives, letters and donor work.
- [ ] The access table has accounts, who they are and the roles that need access, for all three items.
- [ ] The parent's experience is in the memo in her words, with her agreement, without her name.
- [ ] The same-day note says what, since when, and what you propose with whom.
- [ ] Every finding in the memo has evidence and one of the three labels; nobody is named.

<details><summary>Reference answer</summary>

The full memo is `labs/module-16/expert/02-findings-memo.md`. The one sentence and the findings that carry the weight:

**One sentence:** Open Hands is already using AI with family and donor information on personal accounts, its shared drive is open far wider than its policy says, and most of the writing burden comes from one funder's template — so the first step is closing access and giving people a safe alternative, and the biggest time saving is a conversation with the funder, not a tool.

| # | Finding | Evidence | Label |
|---|---|---|---|
| 1 | Family details go into personal AI accounts to produce English funder narratives and Arabic letters | Survey 18 of 22 use AI, 15 personal or both, 3 "with details", 4 "prefer not to say"; two coordinators describe it | Measured + reported |
| 2 | Donor information went into a consumer AI tool and a free grant tool | Card: ChatGPT Plus since March coded office supplies; GrantGenie on a personal email, 23 documents uploaded | Measured; contents reported |
| 3 | `Families` has 46 accounts; 9 roles need it | 13 org, 2 former staff, 31 personal (23 inactive volunteers) | Measured |
| 4 | Care sheets open to anyone with the link since 14 Aug 2024 | Sharing audit | Measured |
| 5 | Donor sheet: 14 editors, 5 personal incl. a former staff member's Gmail; IDs for 851; 37 sensitive notes | Audit; donor extract | Measured |
| 6 | Consent does not cover what is done: 292 families (67%) on v1 with no story clause; an identifiable story in the newsletter; the Q3 report names children, towns, diagnoses | Case register; newsletter; Q3 extract; a parent | Measured + reported |
| 7 | WhatsApp groups carry children's names, medication changes and photos, and outlive the weekend | Handbook; a volunteer | Reported |
| 8 | Microsoft grant ended; 10 seats paid, 3 used | Renewal notice; accounts; ₪2,072 | Measured |
| 9 | One super-admin with 2FA on a personal phone; no offboarding; two former staff accounts active | Accounts; IT notes; interview | Measured + reported |
| 10 | Kiryat Hadas referral data held under a no-transfer clause and 24-hour incident reporting | Service agreement §7 | Measured (text) |

**What the parent said (with her agreement, no name):** she found her son's story through a neighbour; nobody asked her; she would agree to a story she has read first, in Arabic; she wants to know who can see his file and an apology from someone senior, in Arabic.

**What the transcripts' interviewers missed:** Noa's upload of the donor sheet and the GrantGenie account (they never asked how the Giving Tuesday segments were built); Samah's two weeks a quarter; Yossi's single admin and 2FA on his phone; Etti's old WhatsApp groups and what she can see in the drive; Lina's willingness to have a story told on her terms.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting): due diligence on claims (named, not re-taught).
- Google, [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961) (personal accounts, updated 26 October 2026) and [Generative AI in Google Workspace Privacy Hub](https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub) (updated 6 October 2026): why the account, not the tool, decides the exposure. Checked 3 November 2026.
- [Social Workers Law, 5756-1996](https://www.ifsw.org/wp-content/uploads/2021/03/Social-Workers-Law-1996-Israel.pdf), section 8 (English translation): professional confidentiality.
- Field kit: [01.6 · The shadow-AI census](../module-01/lesson-06.md), [02.2 · The discovery interview](../module-02/lesson-02.md), [02.5 · Profiling the data](../module-02/lesson-05.md), [02.7 · Writing a findings memo people believe](../module-02/lesson-07.md).
- Templates: [interview guide](../../templates/interview-guide.md), [stakeholder map](../../templates/stakeholder-map.md), [shadow-AI survey](../../templates/shadow-ai-survey.md), [findings memo](../../templates/findings-memo.md).
- Earlier: [16.1 · The call](lesson-01.md). Next: [16.3 · Diagnosis](lesson-03.md).
