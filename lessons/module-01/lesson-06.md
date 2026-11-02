---
id: "01.6"
module: 1
minutes: 20
practice_minutes: 90
prerequisites: ["01.5"]
objectives:
  - "Run a shadow-AI census from five sources (survey, proxy log, browser extensions, expenses and SaaS list, interviews) plus traces in the work itself, reported by department, never by name."
  - "Measure AI use in a proxy log with a host list rather than a category filter, and read bytes sent as a sign of pasted content."
  - "Turn the census into needs, risks and an interim AI rule the sponsor can approve within days."
volatility: implementation
sources:
  - title: "law.co.il (Haim Ravia) — Monitoring employees' email severely restricted (Isakov Inbar, National Labour Court, 8 Feb 2011)"
    url: https://www.law.co.il/en/articles/2011/04/25/monitoring-employees-email-severely-restricted/
  - title: "Google — Gemini Apps Privacy Hub (human review, 'don't enter confidential information')"
    url: https://support.google.com/gemini/answer/13594961
  - title: "Anthropic — Updates to Consumer Terms and Privacy Policy (28 Aug 2025)"
    url: https://www.anthropic.com/news/updates-to-our-consumer-terms
  - title: "Pearl Cohen — Israel: New Draft Guidelines on the Application of Privacy Law to AI (PPA draft, April 2025)"
    url: https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/
last_verified: "2026-11-02"
---

# 01.6 · The shadow-AI census

In almost every organization people already use AI tools nobody approved, usually because the tools help with a real job. A census finds out who uses what, for which work, with which data, and why — without turning into a hunt. In this lesson you combine five sources and the traces AI leaves in the work itself, measure use by department in Harbor & Pine's exports, and turn the result into an interim rule your sponsor can approve in week two. At the end you have a census table, a summary for the sponsor and the interim rule.

## The situation

It is 4 November. Your 30-day question includes "the AI already in use", and two things you heard this week make it urgent: Noa told you marketing pays for CopyGenie and ChatGPT Plus on personal cards and pastes product information and sometimes customer reviews into them (01.3), and Avi admits the proxy shows "a lot of chatgpt.com from Customer Service". Customer Service handles names, phone numbers, addresses and order details in four languages. Your 30-60-90 plan gives Michal a decision on an interim AI rule by 12 November.

IBM's consulting course observes that most people use AI as a "thought partner" in a chat window, well below what licences suggest; it does not say how to find that use. This is how.

## What to do

### Step 1 — Set the frame before you collect anything

Say out loud, to the sponsor and then to everyone you ask, what the census is for:

> We are finding out which AI tools people already use and for what, so that we can approve good ones
> and set sensible rules. Results are reported by department, not by person. Nobody will be
> disciplined for use before the rules exist.

Get Michal to agree to the last sentence in writing before you start. Without it, the people you most need — the ones who found the tools useful — will stop talking to you.

**Israel first: employees' privacy.** Proxy logs, extension inventories and expense claims are personal data about employees. Israel's National Labour Court, in *Isakov Inbar* (8 February 2011), set strict limits on employer monitoring of employees' email: a clear policy brought to employees' attention, defined permitted uses, and less intrusive means before more intrusive ones. Harbor & Pine's 2021 IT policy tells employees that internet use is logged and filtered (`it/it-policy-2021.md` §5); it says nothing about AI or about identifying individuals from the logs. So: analyse by department; keep pseudonymised IDs pseudonymised; and if anyone wants names, that is a decision for management with counsel and HR, not for you or IT. You don't need names to write rules.

### Step 2 — Use five sources, because each one misses something

| Source | What it shows | What it misses | Harbor & Pine file |
|---|---|---|---|
| Survey | What people use and *why*, in their words | Under-reports what people fear admitting | (you run it: [shadow-AI survey](../../templates/shadow-ai-survey.md)) |
| Web proxy log | Which AI sites, from which department, how often, how much is sent | Phones, home use, new tools the category list doesn't know | `it/proxy-log.csv` (11–22 Oct) |
| Browser extensions | Installed AI add-ons and what they may read | Whether they are used | `it/browser-extensions.csv` (28 Oct) |
| Expenses and the SaaS list | Paid subscriptions, AI features inside paid tools | Free tools; anything paid privately | `it/expenses.csv`, `it/saas-list.csv` |
| Interviews | Workarounds, needs, the story behind the numbers | What people won't say to someone new | Avi, Noa, Samir, Olga |
| The work itself | AI-drafted text left in real outputs | Careful users | `support/emails.csv` |

Run at least four. Triangulation is the point: the proxy says *that*, the survey and interviews say *why*, the work says *with what data*.

### Step 3 — Read the proxy log with a host list, not a category filter

The obvious move — filter `url_category` to "Generative AI" — finds 230 of 2,918 requests and misses most of the story. Build a **host list** of AI services and filter on `dest_host` instead. At Harbor & Pine two of the busiest AI hosts are "Uncategorized" (api.linguaflow.ai, app.copygenie.io) and Grammarly is filed under "Business".

**Track A.** In a spreadsheet, add a column that marks a row as AI when `dest_host` is on your list, then a pivot table: rows = host and department, values = count of requests, distinct count of `user_id`, median of `bytes_out`.

**Track B (Python).** The host list is the part you will maintain and re-run every quarter, so script it. From `labs/module-01/`:

```bash
python census.py
```

Result for 11–22 October (706 of 2,918 requests go to AI tools):

| Tool | Department | Requests | Distinct users | Median bytes sent |
|---|---|---|---|---|
| ChatGPT (chatgpt.com, chat.openai.com) | Customer Service | 160 | 4 | 5,965 |
| ChatGPT | Marketing & E-commerce | 38 | 2 | 2,737 |
| ChatGPT | Purchasing | 18 | 1 | 2,857 |
| Gemini | Customer Service | 8 | 1 | 1,771 |
| Claude | Finance | 5 | 1 | 15,276 |
| CopyGenie | Marketing & E-commerce | 54 | 2 | 2,803 |
| LinguaFlow | Customer Service | 170 | 6 | 1,462 |
| LinguaFlow | Showroom Sales / Logistics / Purchasing | 27 / 15 / 9 | 2 / 1 / 1 | ~1,400–1,600 |
| Grammarly | Marketing / Customer Service / B2B | 75 / 57 / 29 | 2 / 1 / 1 | 700–900 |
| DeepL | Customer Service / Purchasing | 32 / 6 | 2 / 1 | ~1,700–1,900 |
| PeopleWise AI match | HR | 2 | 2 | 1,633 |

**Read bytes sent as a signal of pasted content.** A typical request to Google Docs sends a median of 2,287 bytes. Customer Service's requests to ChatGPT send a median of about 6,000 — consistent with pasting whole customer emails. Finance's five requests to Claude send over 15,000 bytes each: someone is pasting large blocks, and in Finance that may be financial data. These are signals, not proof; they tell you which conversations to have.

The last row is a different kind of finding: `match-ai.peoplewise.io` means the HR system's AI feature is being called. Hold it for lesson 01.7.

### Step 4 — Read the extension inventory for permissions, not just names

Filter `extension_name` for AI tools and count *machines* by department. LinguaFlow – AI Translate & Rewrite is on **9** machines (6 in Customer Service, 1 each in Purchasing, Logistics and the Tel Aviv showroom); Grammarly on 6 (one of them the COO's); "ChatGPT Sidebar" on 2. Then read the `permissions` column: LinguaFlow can "read and change all your data on all websites" plus the clipboard. On a support agent's machine that includes every Deskly page with customer details on it. All were installed from the Chrome Web Store; the 2021 IT policy requires IT approval for software, and nobody has decided whether extensions count.

### Step 5 — Search expenses by merchant, not by category

Filter `merchant` for AI vendors. Category won't do: the same CopyGenie subscription is filed as "Software" five times and "Marketing tools" four times. Harbor & Pine, January–October 2026:

| Tool | Department | Claims | ₪ | Paid by |
|---|---|---|---|---|
| CopyGenie Pro (US$39/month) | Marketing | 9 (Feb–Oct) | 1,298.70 | Personal card, reimbursed |
| ChatGPT Plus (US$20/month) | Marketing | 7 (Apr–Oct) | 518.00 | Personal card, reimbursed |
| ChatGPT Plus | Purchasing | 5 (Jun–Oct) | 370.00 | Personal card, reimbursed |
| Midjourney | Marketing | 1 | 111.00 | Personal card, reimbursed |
| Claude Pro | Finance | 1 | 74.00 | Personal card, reimbursed |
| **Total** | | **23** | **2,371.70** | |

Amounts are converted at the company's ₪3.70 per US$ in the claims. Notice the approvers: managers, including the CEO, signed these claims. "Shadow" AI is often in plain sight; nobody connected the expense line to a data question.

### Step 6 — Look for AI in the work itself

People who draft with a chatbot sometimes paste its whole answer. Search the replies in `support/emails.csv` (a sample of 600 tickets with full text) for assistant preambles and unfilled placeholders in the team's four languages: "Certainly! Here's a polite…", "بالتأكيد! إليك…" (Arabic: "Certainly! Here is…"), "Конечно! Вот…" (Russian: "Of course! Here is…"), "Вот улучшенная версия…" ("Here is an improved version…"), "[Имя клиента]" ("[Customer name]"). `census.py` does this; in a spreadsheet, filter `reply_body` with "contains".

Six of the 600 replies carry such traces (EM-32522, EM-32680, EM-34130, EM-34247, EM-34408, EM-34587): one English, one Arabic, four Russian. Customers received text that began "Of course! Here is a polite and professional reply to the customer in Russian". Report it as "six replies in a sample of 600, mostly Russian" — not by agent. The language pattern is the finding: the tools are filling a real gap in writing Russian and Arabic replies quickly.

### Step 7 — Run the survey and the interviews

Send the [shadow-AI survey](../../templates/shadow-ai-survey.md) to all staff through HR, anonymous, in Hebrew, Arabic, Russian and English, with the amnesty sentence at the top. Eight questions, five minutes — it is peak season. Then interview the people the data points to:

- **Avi (IT):** the sources and their limits ([persona](../../labs/common/harbor-and-pine/personas/avi-it-manager.md); no roleplay: [pre-run transcript](../../labs/module-01/avi-it-interview-transcript.md)). Ask what the proxy shows, whether anyone has *asked* IT for an AI tool, and whether existing software has added AI features.
- **Samir and Olga (Customer Service):** why agents use ChatGPT and LinguaFlow — what job it does for them (module 2 goes deeper).
- **Noa (Marketing):** already done in 01.3.

### Step 8 — Write the census: needs first, then risks, then actions

The census table has one row per tool × department: users, what they use it for, what data goes in, the plan or terms it runs under, risk, and action. Two columns decide the risk:

- **What data goes in.** Customer personal data (names, phones, addresses, order details) is the top of the scale; product copy is the bottom.
- **Which terms the tool runs under.** Consumer plans and business plans of the same tool are different products. Google's Gemini Apps privacy hub says some chats are reviewed by human reviewers and asks users not to enter confidential information. Anthropic's consumer terms (Free, Pro, Max) allow training on chats if the user opts in, with five-year retention, and exclude the commercial (Claude for Work) plans. LinguaFlow's own DPA (`vendors/linguaflow-translation-dpa.md`) says it covers only the Business plan; under its consumer terms, texts from the free extension may be kept for up to 18 months and used for training. Check each tool's current terms before you rate it.

Then write the **interim rule** for Michal to approve — four lines, in the team's languages:

> 1. Do not put customer or employee personal details (names, phone numbers, addresses, order or
>    claim details) into any AI tool the company has not approved.
> 2. You may keep using AI to draft and translate text that contains no personal details.
> 3. An approved tool for drafting and translation is coming by [date]. Until then, ask Olga or Samir
>    if you're unsure.
> 4. Tell us what you use (survey link). No one will be disciplined for use before this rule.

Rule 3 is the one that makes the rule work. The census shows a real need (Russian and Arabic replies, supplier emails, marketing copy); a ban without an alternative pushes use onto phones, where no log will ever show it. The approved tool, its data class and the full policy are module 4's job — the interim rule just has to hold until then.

## Watch out

- **Turning the census into a hunt.** The first person disciplined ends the census; nobody will answer the survey honestly again. Departments, not names, and the amnesty in writing.
- **Filtering by category.** Proxies and expense systems classify late and inconsistently. Maintain a host list and a merchant list.
- **De-anonymising "just to check".** If IT can map IDs to names, the temptation is real. It is a management decision with counsel and HR, and the rules don't need it.
- **Counting installs as use, or requests as people.** Nine LinguaFlow installs is not nine users; 170 requests may be six people. Report each measure as what it is.
- **A ban with no alternative.** It moves use to personal phones and removes your only signal.
- **Ignoring paid-in-plain-sight tools.** Approved expense claims are still shadow AI if nobody looked at what data goes into the tool.
- **Treating the census as a one-off.** New tools appear monthly. Keep the host list and re-run it each quarter.

## Your turn

### Inputs

- Data room (module download): `it/proxy-log.csv`, `it/browser-extensions.csv`, `it/expenses.csv`, `it/saas-list.csv`, `it/it-policy-2021.md`, `support/emails.csv`, `vendors/linguaflow-translation-dpa.md` ([INDEX](../../labs/common/harbor-and-pine/INDEX.md)).
- Persona: [Avi Mizrahi, IT manager](../../labs/common/harbor-and-pine/personas/avi-it-manager.md), or the [pre-run transcript](../../labs/module-01/avi-it-interview-transcript.md); [coach prompt](../../labs/common/coach-prompt.md).
- Templates: [shadow-AI survey](../../templates/shadow-ai-survey.md); census table: `labs/module-01/shadow-ai-census.csv`.
- Track B: `labs/module-01/census.py` ([lab README](../../labs/module-01/README.md)).

### Steps

1. Write the frame (Step 1) as the first lines of your census.
2. Interview Avi for 15 minutes (or read the transcript and list what the interviewer did not ask).
3. Proxy: build your host list and the pivot by tool × department (requests, distinct users, median bytes sent).
4. Extensions: AI extensions by department, with their permissions.
5. Expenses: AI subscriptions by tool and department, with totals and how they were paid.
6. Emails: count replies with chatbot traces, by language.
7. Adapt the survey for Harbor & Pine (languages, amnesty, eight questions).
8. Fill the census table, then write a five-line summary for Michal and the four-line interim rule.

**Track B (Python).** Run `census.py`, add one host you think is missing to `AI_HOSTS`, and re-run. Say in one line why scripting the census is worth it here.

### Time

90 minutes (Track B: about 70).

### Done when

- [ ] Every number is reported by department or language, never by person.
- [ ] The proxy count comes from a host list, and you can name at least two AI hosts a category filter would miss.
- [ ] Extensions are counted by machine, with their permissions; expenses by merchant, with totals.
- [ ] You found the chatbot traces in the email replies and named the language pattern.
- [ ] Each census row has data-in, terms, risk and action.
- [ ] The interim rule has four lines, includes an approved alternative with a date, and states the amnesty.
- [ ] You know (from the interview or the data room) whether anyone has already asked IT for an AI tool.

<details><summary>Reference answer</summary>

**Census table (excerpt).**

| Tool | Departments (users / machines) | Used for | Data going in | Terms | Risk | Action |
|---|---|---|---|---|---|---|
| ChatGPT (free and Plus) | Customer Service 4 users, 160 req.; Marketing 2; Purchasing 1 | Drafting replies, esp. Russian and Arabic; copy; supplier emails | Customer emails with names, phones, order numbers (CS) | Consumer plans; Plus on personal cards | High (CS) | Interim rule now; approved drafting tool; module 4 data classes |
| LinguaFlow free extension | 9 machines (6 CS); 221 req. from 10 users in 4 departments | Translating and rewriting replies and supplier emails | Whatever is on screen or clipboard, incl. Deskly pages | Consumer terms: texts kept up to 18 months, used for training | High | Interim rule; decide on LinguaFlow Business (Olga's request of 2 Oct, unanswered) |
| CopyGenie Pro | Marketing 2 users, 54 req. | Product and campaign copy | Product info, sometimes customer reviews | Unknown; personal card since Feb | Medium | Ask Noa for terms; reviews without names only |
| Claude (Pro) | Finance 1 user, 5 large requests | Unknown — large pastes | Possibly financial data | Consumer plan, one month paid in Aug | Medium, unknown | Conversation with Ronit |
| Gemini | CS 1 user, B2B 1 | Drafting | Likely customer text | Personal or Workspace? Check | Medium | Check whether via company Workspace |
| Grammarly | 6 machines incl. COO; 161 req. | English writing | Text in any web page | Unknown plan | Low–medium | Inventory; terms check |
| DeepL | CS, Purchasing | Translation | Customer and supplier text | Unknown plan | Medium | Covered by the approved-tool decision |
| PeopleWise AI match | HR (2 calls) | Candidate ranking | Candidates' CVs | Vendor feature, on by default | High (decisions about people) | Lesson 01.7 |

**Summary for Michal.** "In two weeks of proxy data, a quarter of web requests (706 of 2,918) went to AI tools. Customer Service uses ChatGPT and a free translation extension daily, mainly to write Russian and Arabic replies faster, and pastes customer emails into them; six replies in a sample of 600 still carry the chatbot's own words. Marketing, Purchasing and Finance pay for AI tools on personal cards (₪2,372 since January, approved as expenses). Nobody has broken a rule — we never wrote one — and Olga asked IT for a proper translation tool on 2 October. I recommend the four-line interim rule below, approved by 12 November, and a decision on one approved drafting and translation tool before December."

**What the transcript missed.** The interviewer never asked whether anyone had asked IT for an AI tool (Avi would have mentioned Olga's unanswered request of 2 October for LinguaFlow Business, which the data room's DPA cover note also shows) or whether existing software had added AI features (PeopleWise — "that's news to me").

</details>

## References

- *Isakov Inbar v. Commissioner for Women's Labour*, National Labour Court, 8 February 2011 — summary by [law.co.il](https://www.law.co.il/en/articles/2011/04/25/monitoring-employees-email-severely-restricted/) (the judgment is in Hebrew; ask counsel before relying on it).
- Google, [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961); Anthropic, [Updates to Consumer Terms](https://www.anthropic.com/news/updates-to-our-consumer-terms) — consumer vs commercial terms, checked 2 November 2026.
- Pearl Cohen, [Israel: New Draft Guidelines on the Application of Privacy Law to AI](https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/) — the PPA's draft recommends generative-AI use policies.
- Template: [shadow-AI survey](../../templates/shadow-ai-survey.md). Lab: [module 1 lab README](../../labs/module-01/README.md).
- Later: module 4 turns the interim rule into the acceptable-use policy and approved-tools list.
- Previous: [01.5 · Access and the first-day data-room read](lesson-05.md). Next: [01.7 · The AI inventory from zero](lesson-07.md).
