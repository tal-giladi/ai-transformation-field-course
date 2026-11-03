---
id: "15.2"
module: 15
minutes: 19
practice_minutes: 150
prerequisites: ["15.1", "01.6", "01.7", "02.2", "02.5", "02.7"]
objectives:
  - "Interview the gatekeepers, two unit heads and the front line so that each tells you what only they know, while protecting the people who show you workarounds."
  - "Test a pilot register against contracts, evals, usage logs, card lines and the proxy, and count builds, duplicates, double counts, missing owners and AI in real use with numerators and denominators."
  - "Measure the review queue's capacity in the gatekeeper's own units and say what it means for 40 builds."
  - "Escalate a live data exposure the same day to its owners, and write a findings memo with evidence labels and the decisions that cannot wait."
volatility: implementation
sources:
  - title: "Bank of Israel, Proper Conduct of Banking Business Directive 369, Management of Model Risk (English, 8/24): model owner §24, model inventory §30–32, model identification §43"
    url: https://www.boi.org.il/media/ggpbdtqp/369_en.pdf
  - title: "Bank of Israel, Circular C-06-2799 (18 November 2024): Directive 364, third parties wider than service providers under 359A"
    url: https://boi.org.il/media/0gudtru2/h2799_en.pdf
  - title: "Bank of Israel, press release 17 May 2026: box from the review of the Israeli banking system for 2025, AI in banks (Hebrew)"
    url: https://boi.org.il/media/dwngxdzg/הודעה-לעיתונות-תיבה-מתוך-סקירת-מערכת-הבנקאות-בישראל-לשנת-2025-שתפורסם-בקרוב-שימוש-ב-aiהתפתחויות-בבנקים-בעולם-ובישראל.docx
  - title: "IAPP, Israel marks a new era in privacy law: Amendment 13 ushers in sweeping reform (13 August 2025)"
    url: https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform
  - title: "IBM Lead AI Transformation Professional Certificate (Coursera): ownership drift, single accountable owner"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-03"
---

# 15.2 · Discovery

You have three weeks to find out what the 43 rows really are, where the pilots stall, and what AI the bank uses that nobody listed. In this lesson you interview the CRO, the CIO, two unit heads, internal audit, compliance and a branch manager; you test the register against every other file in the data room; you measure the queue in the CRO's own units; you escalate a live exposure the day you find it; and you write the findings memo. At the end you have interview notes, a tested register, the queue arithmetic and a findings memo with evidence labels.

## The situation

Monday 11 January 2027. Dalit corrected your mandate on the 4th and sent the units a note asking them to make time for you. The access request came back in pieces: procurement's contract list, finance's card and expense lines, the CISO's office's proxy extract, MRM's inventory and work plan, IT's architecture notes and two usage exports. The CFO's budget memo arrives tomorrow. The findings memo is due on Thursday 21 January; the diagnosis with the CEO is on 4 February.

This is [module 2](../module-02/lesson-02.md) and the shadow-AI census of [01.6](../module-01/lesson-06.md) at bank scale. The difference: here the inventory is not a nice-to-have but a regulatory object. Directive 369 asks a bank to keep an inventory of all models in use, in development or recently discontinued, with one owner each, and to have active procedures for *identifying* models (§30–32, §43). IBM's operating-models course calls the gap *ownership drift*: governed by tool, exposed in decisions nobody owns.

## What to do

### Step 1 — Interview the gatekeepers before the units

Use the [interview guide](../../templates/interview-guide.md). What each person can tell you that no file can:

| Person | What you need | The question that opens it |
|---|---|---|
| [Dr. Irina Kogan](../../labs/module-15/personas/irina-cro.md), CRO | Capacity in her units; what she would accept; people risk | "How many review slots, and how are they split?" Then show her the arithmetic, never "Risk is the bottleneck" |
| [Nir Ashkenazi](../../labs/module-15/personas/nir-cio.md), CIO | Where each pilot runs; what production costs; what IT already has | "What runs on the assistant's tenant, and what happens if it ends?" |
| [Karim Haddad](../../labs/module-15/personas/karim-cards.md), Cards | Evidence per pilot; how work is done while pilots wait | "How are dispute letters written today?" — after you offer a route in, not a threat |
| [Hagit Mor](../../labs/module-15/personas/hagit-retail.md), Retail | The complaint build's evidence and contract; the Branch FAQ's real use | "When does the Mishov contract renew?" and "has the FAQ ever been wrong?" |
| [Tsega Alemu](../../labs/module-15/personas/tsega-internal-audit.md), internal audit | What she would test; when she will next look | "What would you test?" and "what does your 2027 plan cover?" |
| [Adv. Lina Nassar](../../labs/module-15/personas/lina-compliance.md), CCO | What the bank told the supervisor and on what basis; open questions | "What did the survey answer rest on?" |
| [Olga Petrenko](../../labs/module-15/personas/olga-branch.md), branch manager | A real day with the FAQ; how customers get letters in their language | At a teller's desk, after "no names leave this room" |

Two rules from [02.2](../module-02/lesson-02.md) matter more here than anywhere. **Protect the people who show you workarounds**: Karim's team lead and Olga's tellers did what the process made impossible; if they are punished the next workaround is better hidden. **Run the same-word test**: "pilot", "production", "usage" and "owner" each mean something different in Cards, in Risk and in the CFO's memo.

### Step 2 — Test the register against everything else

The register is 43 rows typed by 14 units: unit names in three forms, dates in four formats, money as `248000`, `₪248,000` or `248k`. Clean it first ([02.5](../module-02/lesson-05.md)), then test each column against another source:

- **Same build, two rows.** Sort by `environment` and `test_set`. Three pairs share both and have identical eval rows: MTG-01/OPS-04 (`docai-mtg-sbx`), TRS-01/PRV-03 (`trs-llm-sbx`), FIN-02/OPS-05 (`matchpoint-fin`). Each is budgeted in both units: ₪420,000 counted twice in 2027. 43 rows are **40 builds**.
- **Same task, two builds.** Read the descriptions in Hebrew and English side by side. Complaint summaries: RET-01 "סיכום תלונות חכם" on Mishov and CRD-01 "Complaint summaries — Cards" on Bahir. Credit memos: SME-01 "טיוטת בקשת אשראי לעסקים" and CORP-01. KYC document checks: SME-02 and CMP-01 "בדיקת מסמכי הכר את הלקוח". Conversation summaries: CC-01 calls and DIG-02 chats. And in `ai/intake-requests-2026.csv`, Retail asks for branch call summaries — a fifth.
- **Owners.** Join `business_owner` to `people/staff-directory-extract.csv`: PRV-02's owner left on 15 September 2026. CC-01's owner is "Revital Cohen / Tom Erez" — two owners, which Directive 369 §24 does not allow.
- **Dependencies.** `depends_on` is empty on all 43 rows. `ai/architecture-notes.md` says OPS-02 (procedure assistant) and CC-02 (knowledge assistant) are built in the Tzofen agent studio, on indexes inside the tenant, and are deleted 30 days after the subscription ends. Two pilots depend on OPS-01, and the register cannot see it.
- **Evidence.** Join `ai/eval-summaries.csv`: compare each pilot's latest value with its own threshold (mind the direction: a false-accept rate must be *below* its threshold). Sixteen rows have no measured baseline.

> [!NOTE]
> A duplicate is the same task on the same kind of data in two units: one build could serve both. The same *pattern* on different content (five question-and-answer assistants over five different document sets) is not a duplicate; it is a candidate for a shared template. You will need the difference in 15.5.

### Step 3 — Find AI in real use, and AI outside the register

Follow [01.6](../module-01/lesson-06.md) and [01.7](../module-01/lesson-07.md):

- **Usage logs.** `branches/branch-faq-usage-2026-q4.csv`: 31 branches, a median of 2,072 questions a week in October–December. The architecture notes say it runs on the Ananim sandbox, whose contract says "pilots only, no production use". Thumbs-down jumps from 4.9% over the quarter to 9.0% in 8–26 November: the fee table was out of date (`branches/branch-managers-forum-2026-11-minutes.md`). That is production, on a sandbox, without approval, with a content-ownership failure.
- **Register notes.** CC-01: "since Aug the summary is copied into the Kesher note by a macro". DIG-01: "live for 2% of web visitors (A/B) since November", while the committee minutes say the chatbot was returned in November.
- **Card and expense lines.** `finance/card-and-expense-software-2026.csv`: "LLMHUB \*API USAGE" on a Cards team lead's corporate card every month since April (nine lines, ₪13,741); "AIWRITERPRO MONTHLY" claimed by three people in Digital marketing as "software subscription (personal account)" (₪2,144). Neither vendor is in the contracts list.
- **Proxy.** `security/proxy-ai-hosts-2026-q4.csv`: the Cards disputes subnet uploaded about 127 MB to `api.llmhub.io` in Q4, "allowed (uncategorised)"; Contact Centre agents used a free translator 2,342 times; branch PCs tried a public chat site 924 times (blocked). The policy (§6) and the survey answer (4.2) say public generative AI is blocked.

Put the uses in one table with a numerator and a denominator each. Then compare with what the bank told the supervisor (`governance/bsd-ai-survey-response-2026-extract.md`): 3.1 "a central inventory... with its business owner", 3.4 "no AI application is in production with customers", 4.2 "blocked". In May 2026 the Bank of Israel published a summary of its AI-governance survey: frameworks and initial policies exist, gaps remain at the cross-cutting level. Crescent's own answers look stronger than its files.

### Step 4 — Measure the queue in the gatekeeper's units

`governance/mrm-workplan-2027.md` and Irina give you the unit of capacity: a *review slot*, about ten validator-days. MRM has about 12 a quarter: 6 for the Directive 369 phase-in of existing non-material models (61 not yet compliant, deadline 21 February 2027), 3 for annual reviews, 3 for AI. Full validation of one AI system takes 2 slots. So:

- AI capacity: 3 ÷ 2 = **1.5 AI systems a quarter**.
- Today's rule on 40 builds: 40 × 2 = 80 slots ÷ 3 = **26.7 quarters**.
- The queue (`governance/model-review-queue-2026-12.csv`): 19 submissions, 2 in validation, 2 returned, 15 waiting; median wait **193 days**, longest **437** (the Branch FAQ). The minutes: five meetings in 2026, 0 approved, 0 declined.

Write it in Irina's units and show it to her before anyone else. A number she recognises is a number she can act on.

### Step 5 — Read the assistant's usage with the right denominator

The CFO's memo (12 January) proposes cancelling the assistant (₪2.4M, the biggest single line) because "December usage was 16% of seats". `ai/assistant-usage-2026.csv` gives three denominators:

| Denominator | December weekly active | Share |
|---|---:|---:|
| Seats assigned (1,600 from 1 December) | 250 | 16% |
| Users onboarded (380) | 250 | 66% |
| Pilot teams, October–November (Operations 120, Contact Centre 110) | 89 and 75 | 74% and 68% |

Each is true; only the last two say whether the tool is used by the people who were trained. Add the architecture notes (two pilots inside it) and you have a finding, not an opinion.

### Step 6 — Escalate the same day what cannot wait

Customer names, card digits and transaction details going to a public API every working day is not a finding to hold for the memo. Escalate it the day you see it — to the CISO's office, the DPO and the CIO, whose decision it is — with a proposal that does not push the team onto phones: stop sending identifiers now, move the letters onto the approved route under the pilot that already passed its own test (CRD-03), block the host once that is live. Tell Karim it is a route in. Directive 364 asks banks to map every third party that holds their information assets; a public API on a team lead's card is one.

Then list the dates that decide things before 15 March: `procurement/vendor-contracts-ai.csv` shows Mishov (Retail's complaint vendor) renewing for 24 months on 31 March unless notice by **30 January**; Kesher CRM by 2 March, with generative features switched on by default in release 27.1; Katvan AI by 15 March.

**Track B (Python).** `discovery.py` in the module folder does Steps 2–5 in one run: it cleans the register's formats, finds rows that share an environment and a test set, lists owners who have left and rows with two owners, counts the Branch FAQ's weekly questions, finds AI merchants with no contract and unsanctioned hosts with uploads, computes the queue arithmetic and the three denominators, and lists auto-renewals with notice dates. Python is worth it here because the register will be refreshed every quarter and the same joins must be re-run with the same rules; by hand they take an afternoon and come out slightly different each time.

```bash
cd labs/module-15
python discovery.py
```

### Step 7 — Write the findings memo

Use the [findings memo](../../templates/findings-memo.md) from [02.7](../module-02/lesson-07.md): the answer first, each finding with a label (measured, reported, inference) and its source, no names of people who spoke in confidence, and "what I need decided" with dates. Two decisions cannot wait for 4 February: notice to Mishov by 30 January (it keeps the complaint-tool choice open), and the reply to the CFO by 31 January.

## Watch out

- **Counting rows as builds.** Three rows are copies. Count what was built, by environment and test set.
- **Calling every overlap a duplicate.** Five Q&A assistants on five content sets are a pattern, not a duplicate; merging them loses five content owners.
- **Blaming the shadow builders.** Cards built around a gate that never opened. Bring them in; record what management knew and decided.
- **Reporting "Risk is the bottleneck".** The rule is the bottleneck, and the CRO wrote the rule with the COO's office. Arithmetic in her units gets you a partner; blame gets you a defender.
- **Taking the CFO's 16% at face value — or attacking it.** Show all three denominators and let the numbers argue.
- **Holding the exposure for the memo.** Same day, to its owners, with a route that keeps the work going.

## Your turn

### Inputs

- Data room (module download): `ai/` (all), `governance/` (all), `branches/`, `finance/card-and-expense-software-2026.csv`, `security/proxy-ai-hosts-2026-q4.csv`, `procurement/vendor-contracts-ai.csv`, `people/`, `company/cfo-budget-review-2027-01-12.md`.
- Personas: at least four of [Irina](../../labs/module-15/personas/irina-cro.md), [Nir](../../labs/module-15/personas/nir-cio.md), [Karim](../../labs/module-15/personas/karim-cards.md), [Hagit](../../labs/module-15/personas/hagit-retail.md), [Tsega](../../labs/module-15/personas/tsega-internal-audit.md), [Lina](../../labs/module-15/personas/lina-compliance.md), [Olga](../../labs/module-15/personas/olga-branch.md), or their [transcripts](../../labs/module-15/personas/transcripts/); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [interview guide](../../templates/interview-guide.md), [shadow-AI survey](../../templates/shadow-ai-survey.md), [AI inventory](../../templates/ai-inventory.md), [data profile](../../templates/data-profile.md), [findings memo](../../templates/findings-memo.md).

### Steps

1. Interview at least four people (Irina and Karim among them), or read their transcripts and list for each what the interviewer missed and which question would have opened it.
2. Clean the register and test it: builds, double counts with their budget, duplicates by task, owners, dependencies, evidence against thresholds, baselines.
3. Build the table of AI in real use and AI outside the register, each with a source and a number; compare it with the survey answers.
4. Compute the queue in slots and quarters; write it as you would show it to the CRO.
5. Compute the assistant's usage with three denominators.
6. Write the same-day escalation (to whom, what, the interim route) and the list of contract dates before 15 March.
7. Write the findings memo, at most two pages, ending with the decisions that cannot wait.

**Track B (Python):** run `discovery.py` and check every number in your memo against its output; where you differ, find out why (a date format, a currency, a row you counted twice).

### Time

150 minutes: 50 for the interviews, 40 for the register and the logs, 15 for the queue and the denominators, 10 for the escalation, 35 for the memo.

### Done when

- [ ] Your memo counts 40 builds from 43 rows and names the three copies, the four duplicate pairs, the missing owner and the two-owner row.
- [ ] Every AI use outside the register has a source (card, expense, proxy) and a number, and the memo compares them with the survey answers.
- [ ] The queue is expressed in review slots and quarters, with the median and longest wait.
- [ ] The assistant's usage appears with at least two denominators, and its two dependents are named.
- [ ] The exposure was escalated the day you found it, to its owners, with an interim route.
- [ ] No person who showed you a workaround is named in the memo.
- [ ] The memo ends with the decisions due before 4 February and their dates.

<details><summary>Reference answer</summary>

The full memo is `labs/module-15/expert/02-findings-memo.md` (module download). Its answer first:

> "Forty pilots and nothing in production" is wrong in both directions. There are fewer real pilots than 40, and more AI in real use than none. The pilots do not reach production because the route to production has room for one and a half AI systems a quarter, not because the units are slow; while they wait, some of them went live anyway, outside any inventory, and so did tools nobody registered.

**Numbers you should have (from `discovery.py`):** 43 rows; stages Pilot 34, POC 6, extended 1, on hold 1, rollout 1; baseline measured 22 Y / 16 N / 5 partial; `depends_on` filled 0. Copies: MTG-01/OPS-04, TRS-01/PRV-03, FIN-02/OPS-05, ₪420,000 double-booked. Owner left: PRV-02 (Ariel Mizrahi). Two owners: CC-01. Branch FAQ: 31 branches, median 2,072 questions a week, thumbs-down 4.9%. Outside the register: LLMHUB API ₪13,741 (9 lines, April–December) and 126,950 KB uploaded from the Cards disputes subnet in Q4; AIWRITERPRO ₪2,144 (three claimants); free translator 2,342 requests; blocked public chat attempts 924 (branches), 390 (Digital), 205 (Treasury). Queue: 19 submissions (15 waiting, 2 in validation, 2 returned), median 193 days, longest 437 (RET-03); 1.5 AI systems a quarter; 80 slots = 26.7 quarters. Model inventory: 142 models, 61 non-material not yet compliant with the 21 February phase-in, 0 generative entries. Assistant: 250 / 1,600 = 16%; 250 / 380 = 66%; pilot teams 0.74 and 0.68. Contracts: Mishov notice by 30 January (+24 months, ₪264,000 a year), Hatama AI 20 January, Kesher 2 March, Katvan AI 15 March; Kishron Rank already renewed on 15 December without a DPA.

**Escalation (13 January):** to the CISO's office, the DPO and the CIO. Their decision: host blocked from 1 February; names and card digits out of prompts from 14 January; letters moved onto CRD-03 on the approved sandbox with the DPO's approval by 31 January. Karim told it is a route in.

**What the transcripts' interviewers missed:** Irina's — asked about capacity, not people, so the head of MRM's fintech offer stayed hidden. Nir's — never asked what IT already has, so the ₪1.1M approved landing zone stayed hidden, nor about public AI traffic or the CRM renewal. Karim's — asked how letters are written before offering a route in, so he closed the subject. Hagit's — compared evaluations but never asked about the contract, so the 30 January auto-renewal stayed hidden. Tsega's — asked how she would count, not when she would next look, so the Q2 audit stayed hidden. Lina's — asked about the survey but not what it rested on, so her doubt and her wish to correct it stayed hidden. Olga's — never promised that no names would leave the room, so the personal phones stayed hidden.

</details>

## References

- Bank of Israel, [Directive 369](https://www.boi.org.il/media/ggpbdtqp/369_en.pdf): one owner per model and no joint ownership (§24), the model inventory and its minimum fields (§30–32), active identification of models (§43).
- Bank of Israel, [Circular C-06-2799](https://boi.org.il/media/0gudtru2/h2799_en.pdf): Directive 364; "third party" is wider than "service provider" under 359A, and all third parties must be mapped.
- Bank of Israel, [press release of 17 May 2026](https://boi.org.il/media/dwngxdzg/הודעה-לעיתונות-תיבה-מתוך-סקירת-מערכת-הבנקאות-בישראל-לשנת-2025-שתפורסם-בקרוב-שימוש-ב-aiהתפתחויות-בבנקים-בעולם-ובישראל.docx) (Hebrew): the AI-governance maturity survey; gaps remain at the cross-cutting level.
- IAPP, [Amendment 13](https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform) (in force 14 August 2025). Questions about customer data in any tool go to the DPO.
- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution): ownership drift, single accountable owner (named, not re-taught).
- Field kit: [01.6 · The shadow-AI census](../module-01/lesson-06.md), [01.7 · The AI inventory from zero](../module-01/lesson-07.md), [02.2 · The discovery interview](../module-02/lesson-02.md), [02.5 · Profiling the data](../module-02/lesson-05.md), [02.7 · Writing a findings memo](../module-02/lesson-07.md).
- Templates: [interview guide](../../templates/interview-guide.md), [shadow-AI survey](../../templates/shadow-ai-survey.md), [AI inventory](../../templates/ai-inventory.md), [data profile](../../templates/data-profile.md), [findings memo](../../templates/findings-memo.md).
- Earlier: [15.1 · The call](lesson-01.md). Next: [15.3 · Diagnosis](lesson-03.md).
