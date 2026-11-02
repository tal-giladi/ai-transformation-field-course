---
id: "09.2"
module: 9
minutes: 18
practice_minutes: 150
prerequisites: ["09.1", "02.2", "02.5", "02.7"]
objectives:
  - "Interview a process owner, a frontline handler and an affected claimant so that each can say what they know safely."
  - "Trace every interview claim to the data room and label it verified, reported or contradicted."
  - "Profile the exports you will rely on and state what each one cannot show."
  - "Write a findings memo that leads with the answer and flags anything live that needs action before the next meeting."
volatility: concept
sources:
  - title: "IBM Enterprise AI Transformation and Consulting Professional Certificate (Coursera) — course 3, Assess AI Readiness (verified vs reported evidence)"
    url: https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting
  - title: "Capital Market, Insurance and Savings Supervisor — circular 2016-9-9, Clarification and settlement of claims and handling of public inquiries (5 July 2016), s. 3 and s. 8(a)"
    url: https://www.gov.il/BlobFolder/dynamiccollectorresultitem/regulation-1101/he/regulation_h_2016-9-9.pdf
last_verified: "2026-11-02"
---

# 09.2 · Discovery

Two weeks to find out what is really happening in Meridian's claims: what slows them, what the AI that is already running does, and who it does it to. In this lesson you interview the head of claims, a senior handler and a claimant whose complaint reached the complaints officer, and you follow every claim they make into the data room. At the end you have a findings memo with evidence labels, and one finding that cannot wait for the committee.

## The situation

Sunday 8 – Thursday 19 November 2026. Ilana approved your charter on Sunday and presented her
proposal at Tuesday's management meeting "subject to the head of AI's plan". She expects your findings
on Thursday 19 November, before you write anything for the committee.

You have the data room, a list of people and two weeks. IBM's readiness course asks you to separate
verified evidence from what people report; at Meridian you produce both, and some of the most
important evidence comes from the person the systems are used on.

## What to do

### Step 1 — Prepare one guide, three conversations

Write an [interview guide](../../templates/interview-guide.md) as in [02.2](../module-02/lesson-02.md):
workflow questions ("take me through the last claim you closed"), the same-word test, and what you
must find out from each person.

The same-word test matters here because three words carry the whole engagement:

| Word | What the dashboard means | What a claimant means | Ask |
|---|---|---|---|
| "Handling time" | File complete → decision, SIU excluded | From my phone call to my money | "When does the clock start for you?" |
| "Complete" | The handler set the status | I sent everything you asked for | "How is 'file complete' set in practice?" |
| "Fraud" | Any SIU case ("fraud prevented") | Someone lying to the insurer | "When do you count a case as fraud?" |

Plan the order: the head of claims first (his answers shape your data questions), then a handler,
then a claimant.

### Step 2 — Interview the process owner and make it safe to talk

[Yusuf Darawshe](../../labs/module-09/personas/yusuf-vp-claims.md), VP Claims, will explain the process
well and stop at anything that sounds like criticism of colleagues or of the SIU, which reports to
him. Two moves get more:

- **Show him data instead of asking for opinions.** "Half the files need a second request" is his guess;
  you can come back with the real share and ask why.
- **Offer non-attribution before the sensitive question, not after.** "I'll look at the numbers
  myself; nothing you say goes into a paper with your name. What changed in the SIU queue since
  September, by centre?" A manager who is a member of the group a system disadvantages has extra
  reasons to stay quiet; your job is to make the data carry the finding, not him.

### Step 3 — Interview a handler about a real file

[Marina Kogan](../../labs/module-09/personas/marina-claims-handler.md) handles health and travel claims
with invoices from four continents. Ask her to open the last file she closed and walk you through it.
You get the failure modes your eval will need in 09.5 (US month/day dates, Russian month names, foreign
currencies, exempt dealers with no VAT) and the reason second document requests happen.

Expect shadow AI. Handlers who must read Georgian and Thai invoices in time will find a way. If you
ask "do you use ChatGPT?" you get "no". If you ask how she reads a Georgian invoice *on a normal day*,
after saying you are looking for a tool that is allowed, you may get the truth. Treat it as a demand
signal, not a disciplinary matter ([01.6](../module-01/lesson-06.md)).

### Step 4 — Interview the claimant

[Samira Abu-Ahmad](../../labs/module-09/personas/samira-claimant.md) complained on 12 October about her
motor claim. The complaints officer arranged a call. An interview with a person affected by a system
is not a service-recovery call and not a deposition:

1. Say who you are, why you called, and what you can and cannot do.
2. Ask for the story **in order**, contact by contact, and do not interrupt.
3. Ask what it cost her beyond the claim: time off work, a rental car, a second police visit.
4. Ask what she was told, and what she concluded from it.
5. Ask what an explanation would have to say to be useful to her.
6. Promise only what you can deliver, with a date and a name.

Her story gives you a claim to trace: a parked car, a phone report on 15 September, a list of documents,
then a police confirmation nobody had asked for at the start, then the garage's Arabic invoice
"unreadable", then "the system flagged your file". Paid on 29 October.

### Step 5 — Follow every claim into the data

An interview gives you a lead; the data room tells you whether it holds. Label each item as you go.

| What you heard | Where to check | What the data says | Label |
|---|---|---|---|
| "Half the files need a second request" (Yusuf) | `claims/doc_requests.csv` | 45.2% of claims have 2+ rounds, 14.1% have 3+; mean 1.62 rounds | Verified |
| "The list goes out late or incomplete" (Yusuf, Marina) | `doc_requests.csv` vs `claims_register_sample.csv` (`reported_date`) and the manual, 3.2 | Complete list on the day of the report for 5.6% of claims (median 4 days); **45.4%** of documents asked for in round 2 or later were on the standard day-one list | Verified |
| "The dashboard measures the fast part" (Yusuf) | Dashboard definitions; register | Confirmed by definition; measured in 09.3 | Verified (definition) |
| Translation with personal AI tools (Marina, if she told you) | `claims/crm_contacts.csv`, `contact_type` = handler_note | 12 notes, May–October, mention ChatGPT or Gemini for translating or drafting | Verified (12 notes in a sample: the practice is wider) |
| Samira's claim | `complaints/complaints_log_2026.csv` (12 Oct) → claim CL-2026-026307 → `claims/motor_claims_2026-07_to_10.csv` | Fraud Insight score 60, factors F03;F04;F05;F08;F09; band "refer"; SIU outcome no_finding; decision 25 Oct | Verified |
| "SIU is busier" (Yusuf) | `siu/siu_case_log.csv`, `referral_source` | 107 cases from `fraud_insight_auto` since 6 September (84 still open) | Verified |

The last two rows lead somewhere. Open `vendor/fraud-insight-config-export.csv`: F08 is "interpreter
required", F09 is "postal area on the risk-area list". Samira's score is 60 against a referral
threshold of 50; 25 of her points are her language and her postal area. Then a first pivot of the
motor extract (rows: `claimant_lang`; columns: before/after 6 September; values: share with
`siu_referred` = Y):

| | Before 6 Sep | After 6 Sep |
|---|---|---|
| Hebrew | 3.4% | 5.4% |
| Arabic | 3.2% | **21.0%** |

Before go-live, handlers referred both groups at the same rate. After, Arabic-speaking claimants are
referred four times as often, and a referral holds their payment. One pivot is not a bias test (09.4
does it properly, with intervals, other groups and the mechanism), but it is enough to know this is
not a theory.

The manual's day-one rule is not only Meridian's preference: the Supervisor's claims circular
(2016-9-9, s. 8(a)) expects the claimant to receive the list of required information and documents
as soon as possible after the first contact, and further documents to be requested within 14 business
days of the need becoming clear. You quote it as context; whether Meridian complies is for compliance
and counsel.

### Step 6 — Profile what you will rely on

Before you build on an export, write what it cannot show ([02.5](../module-02/lesson-05.md),
[data profile](../../templates/data-profile.md)):

- **Register:** a 1-in-40 sample (multiply counts by 40); `claimant_age_band` missing on 28% of agent
  claims (the agents' portal does not ask); 13 rows with region typed as "צפון" instead of "North".
- **CRM:** six months only (May–October), direct channels only (agents' claims never enter it); 31 of
  216 first-notice rows have no claim number (logged before it existed): join on policy.
- **Fraud labels:** the register's only fraud field is `fraud_flag`, set to SUSPECT on a referral. Outcomes live in the
  SIU's own spreadsheet.
- **Complaints:** summaries in Hebrew; topic codes in English.

### Step 7 — Write the memo, and do not sit on the urgent finding

Use the [findings memo](../../templates/findings-memo.md) from [02.7](../module-02/lesson-07.md):
answer first, then each finding with its evidence and label, then what it means. One finding is not
like the others: a live system is holding payments, disproportionately for one group, today. That
does not wait for the committee on 15 December. Write a short interim recommendation to Ilana (copy
the CRO, under the line you agreed in 09.1): what to switch off, how (a change request; ask the vendor
or the product owner what it takes), what stays, who confirms. [07.3](../module-07/lesson-03.md) on
delivering bad news upward applies: answer first, the finding once, evidence separate from inference.

## Watch out

- **Leading questions.** "Do the flags target Arab claimants?" makes Yusuf defensive and proves
  nothing. Ask what changed, by centre, and then look.
- **Quoting someone who asked not to be quoted.** Your memo cites data, not Yusuf. If the data did not
  confirm it, it is not a finding yet.
- **Promising the claimant an outcome.** You can promise a written answer by a date. You cannot promise
  compensation or a finding about discrimination.
- **Treating shadow AI as misconduct.** Twelve notes in a sample mean a team that needs a sanctioned
  tool. Find the need; the DPO decides the rules.
- **Mixing sample and population.** The register is 1-in-40; the motor extract, the SIU log and the
  complaints log are complete. Say which a number comes from.
- **Waiting for the memo cycle.** If something live harms people, the right time to say so is now, to
  the person who can switch it off.

## Your turn

### Inputs

- Personas: [Yusuf Darawshe](../../labs/module-09/personas/yusuf-vp-claims.md),
  [Marina Kogan](../../labs/module-09/personas/marina-claims-handler.md),
  [Samira Abu-Ahmad](../../labs/module-09/personas/samira-claimant.md); optional
  [Natalia Gurevich](../../labs/module-09/personas/natalia-chief-actuary.md). Pre-run transcripts in
  `labs/module-09/personas/transcripts/` (module download). Feedback: [coach prompt](../../labs/common/coach-prompt.md).
- Data room: `claims/` (register sample, document requests, CRM, motor extract), `siu/siu_case_log.csv`,
  `complaints/complaints_log_2026.csv`, `policies/claims-manual-excerpt.md`,
  `vendor/fraud-insight-config-export.csv`.
- Templates: [interview guide](../../templates/interview-guide.md), [data profile](../../templates/data-profile.md),
  [findings memo](../../templates/findings-memo.md).

### Steps

1. Write the interview guide: the three words, what you must find out from each person.
2. Run the three interviews (or read the transcripts and list what each interviewer missed). Coach each.
3. For every claim you heard, find the file that confirms or contradicts it; fill a table like Step 5's.
4. Find Samira's claim in the data and explain her score factor by factor.
5. Make the before/after pivot of SIU referrals by language from the motor extract.
6. Write the data-profile notes (what each export cannot show).
7. Write the findings memo (answer first, five to seven findings with labels) and, separately, the
   interim recommendation on anything live.

**Track B (Python).** `python baselines.py --section documents` reproduces the document-request
numbers, and `python bias_test.py` the referral table with 95% intervals. Python is worth it here
because you will re-run both on a newer export before the committee, and the numbers must come out
the same way twice.

### Time

150 minutes: 75 for interviews and coaching, 45 for the data checks and the pivot, 30 for the memo.

### Done when

- [ ] Every finding has evidence with a file name and a label (verified, reported, contradicted).
- [ ] At least one finding came from the claimant and is confirmed in the data.
- [ ] The memo leads with the answer in two or three sentences.
- [ ] Nothing in the memo is attributed to a person who asked for non-attribution.
- [ ] The interim recommendation says what to switch off, how, what stays, and who decides.
- [ ] The data profile says what each export cannot show.

<details><summary>Reference answer</summary>

The full memo is `labs/module-09/expert/02-findings-memo.md` (module download). Excerpts:

> **Answer first.** Claims are slow because documents are requested in rounds, not because intake is
> typed. The fraud score that went live with Kalanit 9.4 refers Arabic-speaking claimants to
> investigation four times as often as Hebrew-speaking ones, through two factors that stand in for
> nationality and place of residence; it should stop referring automatically now, before the
> committee. The winter pilot as proposed would scale both problems into the peak.

> **2. The wait is in the document chase** *(verified)*. 45.2% of claims need a second round, 14.1% a
> third. 45.4% of documents requested in round 2 or later were on the standard day-one list, and the
> complete list went out on the day of the report for only 5.6% of claims (manual 3.2 says same day).

> **3. Fraud Insight refers by language and area** *(verified)*. Every motor claim, July–October 2026
> (5,536): before 6 September, SIU referral 3.2% Arabic vs 3.4% Hebrew; after, 21.0% vs 5.4%. F08
> "interpreter required" fires on 90.3% of Arabic claims, F09 "risk area" on 68.4%. The claimant whose
> complaint I followed (CL-2026-026307) was referred with a score of 60 (threshold 50); 25 of her
> points were her language and her postal area; 44 days to payment; told "the system flagged your
> file" *(reported, the claimant)*.

> **6. AI already in use outside the inventory** *(verified)*: the two 9.4 modules, and handlers
> translating foreign documents with personal ChatGPT/Gemini accounts (12 handler notes in the CRM
> sample).

> **Interim recommendation.** Ilana, today, by change request: switch off Fraud Insight's auto-referral
> for motor claims and disable F08 and F09; keep the score visible to the SIU as a review aid only,
> with written reasons for any referral (manual 6.1). Release the payment hold on the 84 open
> auto-referred cases unless a handler records concrete grounds. Michael agrees this goes to the
> committee as an interim decision already taken.

**What the pre-run interviews missed:** Yusuf's view of who gets flagged (nobody made it safe);
Marina's translation practice (nobody asked how she reads a Georgian invoice today); what the claim
cost Samira (₪1,450 for a rental car) and that she almost gave up.

</details>

## References

- IBM, [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 3 (verified vs reported; named, not re-taught).
- Supervisor of the Capital Market, Insurance and Savings, [circular 2016-9-9, Clarification and settlement of claims](https://www.gov.il/BlobFolder/dynamiccollectorresultitem/regulation-1101/he/regulation_h_2016-9-9.pdf) (5 July 2016, Hebrew), s. 3 and s. 8(a). Compliance questions go to the compliance officer and counsel.
- Field kit: [02.2 · The discovery interview](../module-02/lesson-02.md), [02.5 · Profiling the data](../module-02/lesson-05.md), [02.7 · Writing a findings memo](../module-02/lesson-07.md), [01.6 · The shadow-AI census](../module-01/lesson-06.md), [07.3 · Delivering bad news upward](../module-07/lesson-03.md).
- Templates: [interview guide](../../templates/interview-guide.md), [data profile](../../templates/data-profile.md), [findings memo](../../templates/findings-memo.md). Coach: [coach prompt](../../labs/common/coach-prompt.md).
- Next: [09.3 · Diagnosis](lesson-03.md).
