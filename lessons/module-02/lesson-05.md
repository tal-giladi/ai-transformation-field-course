---
id: "02.5"
module: 2
minutes: 20
practice_minutes: 100
prerequisites: ["02.4"]
objectives:
  - "Profile a dataset for a named AI use: completeness of the needed fields, labels, duplicates, stale copies, representativeness and joinability, each with numerator and denominator."
  - "Decide whether an outcome label exists, and write the outcome-recording fix when it does not."
  - "Trace each dataset's chain of custody — origin, purpose collected for, whether that covers the new use, where access is enforced, who owns it — and route the permission question to counsel or the DPO under Israeli privacy law."
  - "Give each dataset a verdict: usable now, usable after a named fix, or not yet."
volatility: implementation
sources:
  - title: "Privacy Protection Law, 5741-1981 — English translation (WIPO Lex, 2014; Hebrew version controlling): section 2(9), section 8(b)"
    url: https://www.wipo.int/wipolex/en/text/347462
  - title: "E. B. N. Law — A Significant Legislative Change in the Israeli Privacy Law (Amendment 13): purpose principle, registration, definitions"
    url: https://www.ebnlaw.co.il/?p=21834
  - title: "Pearl Cohen — Major Amendment to Israeli Privacy Law Set to Take Effect (3 Aug 2025)"
    url: https://www.pearlcohen.com/major-amendment-to-israeli-privacy-law-set-to-take-effect/
  - title: "Pearl Cohen — Israel: New Draft Guidelines on the Application of Privacy Law to AI (4 May 2025)"
    url: https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/
  - title: "IAPP — The new Israeli data security regulations: A tutorial"
    url: https://iapp.org/news/a/the-new-israeli-data-security-regulations-a-tutorial
  - title: "GDPR Article 5 — Principles relating to processing of personal data (purpose limitation)"
    url: https://gdpr-info.eu/art-5-gdpr/
last_verified: "2026-11-02"
---

# 02.5 · Profiling the data: is it AI-ready?

"We have lots of data" is the most common sentence in an AI program and the least useful. Data is ready or not *for a use*: the same ticket export can carry a draft-reply pilot and fail completely as training data for a claims decision. In this lesson you profile Harbor & Pine's datasets against named uses: whether the fields are filled, whether the outcome was ever recorded, how much is duplicated, which copies are stale, whether the files join, where each came from and whether you may use it for this purpose under Israeli privacy law. At the end you have a data profile per dataset with a verdict — usable now, usable after a named fix, or not yet — and a short list of questions for counsel.

## The situation

Week 3, Thursday 19 November 2026. The baselines are done (02.4). In the interviews you heard three ideas that will come back in module 3: a bot or draft replies for support emails, help deciding damage claims faster, and the CEO's ChatNest demo "built on our own catalogue". Ronit asked: "Is our data good enough for any of this?" Avi asked: "Are we even allowed to use customer emails for that?"

Both are the right questions, and they are different questions. Ronit's is about fitness; Avi's is about permission. You answer the first with a profile and route the second to the people who decide it, with the facts they need.

IBM's readiness course separates fidelity (origin, currency, completeness, representativeness — for a named use), access and permission, and asks for a chain-of-custody read per data asset. Here you run both on real files, with Israel's privacy law as the permission layer.

> [!WARNING]
> Profiling means opening files full of customer names, phone numbers, addresses and messages. In a
> real engagement, profile inside the organization's environment, on an approved machine, and never
> upload the raw files to an AI tool the organization has not approved for that data. Harbor & Pine's
> data is synthetic, so any tool is fine here.

## What to do

### Step 1 — Name the use and the fields it needs

Write one line per use, and list only the fields the use needs:

| Use | Datasets | Fields that matter |
|---|---|---|
| A. Draft replies to support emails and web-form messages; an agent checks and sends | `support/emails.csv`, `support/tickets.csv`, `catalog/products.csv` | message text, language, category, the reply actually sent, whether the customer came back |
| B. Suggest a decision on damage claims | `claims/damage-claims-log.csv` | damage type, photos, amount, **decision**, decision date |
| C. Tell customers proactively when their container is late (no AI) | `orders/orders.csv`, `orders/shipments.csv`, `orders/logistics-eta-tracking.csv` | order, container, promised date, latest ETA |
| D. Answer product questions (price, availability) | `catalog/products.csv` and the shared-drive copy | SKU, price, status |
| E. Anything on WhatsApp | `support/whatsapp-week-tally.csv` | — |

### Step 2 — Completeness of the needed fields

For each field: filled share, distinct values, what "blank" and "other" really hide. From `tickets.csv` (2,529 rows):

| Field | Filled | Note |
|---|---|---|
| `language` | 95.2% | Auto-detected: 121 blank and 85 wrong codes (`yi`, `fa`, `de`, `ur`, `nl`, `uk`, `bg`) for a team that serves Hebrew, Arabic, Russian and English |
| `category` | 96.9% | 78 blank; "Other/כללי" 722 = 28.5%; "Delivery" split on 1 July into "Delivery status" and "Delivery damage" |
| `order_id` | 58.2% | 80 of 1,472 typed by hand in other formats (`so26…`, `SO-26…`, `SO 26…`, `#004521`, `26005704`) |
| `time_spent_min` | 50.7% | Timer used by about half the agents |
| `csat` | 19.0% | Survey answered by a fifth; good 317, bad 163 |

For use A this means: the language field cannot route replies without a check, the category field cannot be the label for triage, and a fifth of customers' satisfaction is all you have.

### Step 3 — The label question: was the outcome ever recorded?

An AI system that suggests, triages or decides needs examples where the right answer is known: the outcome, recorded consistently, by someone who knew. Ask of every use: *what record proves what the right answer was?*

- **Claims (use B).** The decision column `החלטה` is blank for **48 of 149 claims (32.2%)** — and 31.4% even among claims opened by 30 September, so it is not just recent claims waiting. The recorded ones: approved 55, partly approved 28, rejected 18, with no reason recorded. There is no outcome for a third of the cases and no reason for any: **no usable label**. The verdict is "not yet", and the fix is not a model; it is an outcome-recording routine (decision and reason on every claim, owner Samir, start date, eight weeks) before anyone revisits the idea.
- **Replies (use A).** The helpdesk's "resolved" is not an outcome: 1,880 of 2,314 resolved tickets (81.2%) were resolved within five minutes of the first reply, because the handbook says to resolve on reply. You can build a better outcome from the data: *the same customer wrote again about the same order within 14 days*. Normalise the order numbers first, then: **335 of 1,430 resolved tickets with an order (23.4%)** were followed by a new ticket. That is a label you can use, with its definition written down.
- **The replies themselves.** If the agents' sent replies become examples of good answers, check what they are. Many "where is my order" replies are the macro with a date that had already passed; those are examples of the problem, not of good answers. And six replies in `emails.csv` carry traces of a chatbot — a reply that begins "Certainly! Here's a polite, professional reply you can send:" (EM-32680), Arabic and Russian equivalents (EM-32522, EM-34408, EM-34247), placeholders like "[Имя клиента]" left in (EM-34130, EM-34587). Exclude AI-written replies from any test set: you would be testing a model against another model.

### Step 4 — Duplicates

Write the rule, then count. Same `requester_id` with a new ticket within 60 minutes of their previous one: **157 tickets (6.2%)**. Only 44 of them were merged; 113 were answered separately. Duplicates inflate volume baselines, and in a test set they let a model "see" the same case twice. Cross-channel duplicates — a customer who writes on WhatsApp and emails about the same order, as you saw in the sit-in — cannot be counted at all, because the WhatsApp tally has no join key (Step 6).

### Step 5 — Stale copies: who publishes, who reads

For every dataset that exists in more than one copy, ask who publishes it, how often, and how often the use reads it. A copy read more often than it is refreshed is stale.

- **Catalogue (use D).** `catalog/products.csv` (ERP, 245 SKUs, 29 discontinued) vs `catalog/products-2023-shared-drive-copy.csv` (144 SKUs, Hebrew headers): all 29 discontinued items are still in the copy; 101 active items are missing from it; the copy's prices are lower for 143 of 144 items, by a median of 12.7% of today's price. The ChatNest deck (`vendors/chatnest-sales-deck.md`, slide 4) answers "the Oslo 3-seat sofa in grey is **₪4,290**" — the copy's price; the ERP says ₪4,990. The demo "built on our own catalogue" was built on a stale copy. Any product-answer use must read the ERP, and the copies on the shared drive need an owner and a deletion date.
- **Container ETAs (use C).** `shipments.csv` (forwarder's portal export, weekly) vs Tamar's sheet (updated twice a week by hand): 95 container rows; two containers entered twice (ADFU3996533, ORLU3326673); seven numbers typed with a space; original-ETA dates in four formats (`dd/mm/yy`, `d.m`, `yyyy-mm-dd`, blank); three containers with an original ETA between May and October missing from the sheet. A daily delay notice should read the forwarder's export (or its email updates), with the sheet as a check, not the other way round.

### Step 6 — Joinability and representativeness

- **Joins.** Tickets join to orders only after normalising 5.4% of order numbers. The WhatsApp tally's `order_no` is filled on 248 of 630 rows (39.4%) and every one is in the format `HP-1xxxxx`, which matches **none** of the ERP's `SO26…` order numbers. Agents are typing some other number (a delivery note? a customer number?): ask Samir before assuming anything. Until then, WhatsApp cannot be joined to orders, containers or tickets.
- **Representativeness.** `emails.csv` holds 600 tickets, spread over the months roughly in proportion to the export (58 in May, 130 in October), so it represents the helpdesk — but not WhatsApp, where the tally's language mix is different (Russian about 22% of conversations, against 11.7% `ru` in the helpdesk's language field). And none of the data covers November–January, the peak. A test set built only from May–October helpdesk emails will not tell you how a pilot behaves in December or on WhatsApp.

### Step 7 — Chain of custody and permission

For each dataset write five links, in order: **origin → purpose it was collected for → does that purpose cover the new use → where access is enforced → who owns it today.** A chain that ends at "the system" or "nobody" is broken.

What Israeli law says, at the level you need to route the question:

- Under the Privacy Protection Law, 5741-1981 (חוק הגנת הפרטיות, התשמ"א-1981), using or passing on information about a person's private affairs for a purpose other than the one for which it was given is an infringement of privacy (section 2(9)), and information in a database may be used only for the purposes for which the database was set up (section 8(b), in the pre-2025 text).
- Amendment 13 (in force since August 2025) broadened the definitions of personal data and processing, kept a purpose principle — no processing for purposes other than those legally defined for the database — removed the duty to register most databases, and gave the Privacy Protection Authority (PPA) administrative fines.
- The PPA's draft guidance on AI (published spring 2025, still a draft) expects a legal basis for processing personal data in AI systems, an explanation of the purposes and methods of AI processing, data protection impact assessments, and generative-AI use policies.
- The Privacy Protection (Data Security) Regulations, 5777-2017 (in force since May 2018) set security levels and expect managed access control.
- GDPR (purpose limitation, Article 5(1)(b)) reaches an Israeli company only when it offers goods or services to people in the EU or monitors them; Harbor & Pine sells in Israel, so it is not the first layer here.

Harbor & Pine's privacy notice (`policies/privacy-notice.md`, 2022) says customer data is used to process and deliver orders, handle returns and claims, answer questions and complaints, send invoices and, with consent, marketing; calls "may be recorded for quality and training"; some providers store data outside Israel. IT's note (`policies/data-retention-note.md`) says helpdesk tickets are kept in Deskly (US/EU) "forever — no deletion rule set", the claims log is kept forever on the shared drive and also downloaded by Finance each quarter, and nobody knows whether the company's databases were reviewed after the 2025 changes.

You do not decide whether use A or B fits those purposes. You write the question so counsel or the DPO can answer it, and you minimise meanwhile:

| Dataset | Origin | Collected for | Question for counsel / DPO | Access enforced at | Owner today |
|---|---|---|---|---|---|
| Emails and tickets | Customers, via Deskly | Answering questions and complaints | May past messages be used to build and test a draft-reply tool, pseudonymised, in an approved tool? Does an AI vendor's processing go abroad? | Deskly roles | Samir |
| Claims log | Rina, by hand | Handling claims | Is a Google Sheet with names and phones on the shared drive, copied by Finance, acceptable under the security regulations? | Nobody: shared drive | Rina (in practice); "nobody decided" |
| WhatsApp conversations | Customers, on four shared phones | Not stated anywhere | Customer messages and damage photos on shared phones outside any system: what must change before anything else? | The phone's screen lock | Nobody |
| Orders, shipments | ERP; forwarder | Delivering orders | Use C (telling customers their own order is late) is inside "deliver your order"; confirm | Priority roles | Finance; Tamar |

### Step 8 — The verdict per dataset

One sentence each: usable now, usable after a named fix (owner, date), or not yet — and what would change it. Then the profile goes into the readiness assessment (02.6).

**Track B (Python).** Profiling six datasets by hand takes most of a day and has to be repeated whenever a fresh export arrives; a script makes it an afternoon and makes every number reproducible. From `labs/module-02/`:

```bash
python profile_data.py
```

It prints the completeness table, the category change, duplicates, typed order numbers, the follow-up label (23.4%), the claims label (32.2% blank), the catalogue comparison, the ETA-sheet checks and the WhatsApp tally's formats and join test. It uses `fieldkit.profile` (`profile`, `duplicates`, `share`).

## Watch out

- **"Is the data good?" without a use.** Fit for what? Name the use first.
- **Status fields as outcomes.** "Resolved", "closed", "approved" are clicks. Ask what record proves the outcome; build it from the data where you can (follow-ups), start recording it where you can't (claims).
- **Training or testing on AI-written examples.** Chatbot traces in the replies mean some "human" answers aren't. Find them and exclude them.
- **The convenient copy.** The shared-drive file is easier to open than the ERP. That is exactly how the vendor's demo got the wrong prices.
- **Assuming a join works.** Check that keys match before you plan anything on top of them; the tally's order numbers match nothing.
- **Deciding the legal question yourself.** "It's our customers' data, so we can use it" and "privacy law forbids AI" are both wrong ways to finish. Write the question, minimise, route it.
- **Copying personal data into your profile.** Profiles hold counts and shares, not names.

## Your turn

### Inputs

- In the module download: [`support/tickets.csv`](../../labs/common/harbor-and-pine/support/tickets.csv), [`support/emails.csv`](../../labs/common/harbor-and-pine/support/emails.csv), [`support/whatsapp-week-tally.csv`](../../labs/common/harbor-and-pine/support/whatsapp-week-tally.csv), [`claims/damage-claims-log.csv`](../../labs/common/harbor-and-pine/claims/damage-claims-log.csv), [`catalog/products.csv`](../../labs/common/harbor-and-pine/catalog/products.csv), [`catalog/products-2023-shared-drive-copy.csv`](../../labs/common/harbor-and-pine/catalog/products-2023-shared-drive-copy.csv), [`orders/shipments.csv`](../../labs/common/harbor-and-pine/orders/shipments.csv), [`orders/logistics-eta-tracking.csv`](../../labs/common/harbor-and-pine/orders/logistics-eta-tracking.csv), [`vendors/chatnest-sales-deck.md`](../../labs/common/harbor-and-pine/vendors/chatnest-sales-deck.md), [`policies/privacy-notice.md`](../../labs/common/harbor-and-pine/policies/privacy-notice.md), [`policies/data-retention-note.md`](../../labs/common/harbor-and-pine/policies/data-retention-note.md).
- Template: [data profile](../../templates/data-profile.md); spreadsheet version `labs/module-02/data-profile.csv` in the module download.
- Track B: `labs/module-02/profile_data.py` ([lab README](../../labs/module-02/README.md)).

### Steps

1. Write the five uses (A–E) and the fields each needs.
2. Profile `tickets.csv` for use A: completeness, the follow-up label, duplicates, typed order numbers.
3. Profile the claims log for use B, including the label question and the decision time.
4. Compare the two catalogues and check one ChatNest demo answer against the ERP.
5. Check the ETA sheet against `shipments.csv` for use C.
6. Test whether the WhatsApp tally joins to anything.
7. Write the chain of custody for four datasets and the questions for counsel or the DPO.
8. Give each dataset a verdict with what would change it.

**Track B (Python).** Run `python profile_data.py`; then add one check of your own (for example, the share of `emails.csv` replies that contain a date that had already passed when the reply was sent).

### Time

100 minutes (Track B: about 70).

### Done when

- [ ] Every use is named, with the fields it needs.
- [ ] Every percentage has its numerator and denominator.
- [ ] The label question is answered for uses A and B, with a constructed label for A and an outcome-recording fix for B.
- [ ] The stale catalogue copy is identified, with one demo answer traced to it.
- [ ] The WhatsApp join test is done and its result stated.
- [ ] Four chains of custody, with the permission questions written for counsel or the DPO, not answered by you.
- [ ] Each dataset has a verdict: usable now / after a named fix / not yet.

<details><summary>Reference answer</summary>

**Data profiles — Harbor & Pine — 19 November 2026.**

| Dataset → use | Key results | Verdict | What would change it |
|---|---|---|---|
| `tickets.csv` + `emails.csv` → A (draft replies) | Language auto-detected (121 blank, 85 wrong codes); category unusable as a label (28.5% Other, July redefinition); "resolved" = reply sent (81.2% within 5 min); constructed label: 23.4% of resolved tickets with an order get a follow-up within 14 days; 6.2% duplicates (113 of 157 answered twice); 6 replies with chatbot traces; 600 full texts spread over May–Oct | **Usable after fixes**: build the test set from `emails.csv` with true language and category coded by hand, chatbot-traced and passed-date macro replies excluded, names and phones pseudonymised; counsel confirms the purpose question | Counsel's answer; a test set of 200 coded messages (05.2) |
| Claims log → B (decision suggestions) | Decision blank 48 / 149 (32.2%; 31.4% of claims opened by 30 Sep); no reason field; median 8 days to decision; names and phones in every row, on the shared drive, copied by Finance | **Not yet** | Decision and reason recorded on every claim for eight weeks (Samir, from 1 Dec); a working copy without names and phones; access restricted |
| Orders + shipments + ETA sheet → C (delay notice, no AI) | Promised date = fixed lead time; forwarder export complete; the sheet has 2 duplicates, 7 typed with a space, 4 date formats, 3 containers missing (May–Oct) | **Usable now** from `orders.csv` + the forwarder's export; the sheet as a cross-check | — |
| Catalogue → D (product answers) | ERP current (245 SKUs); the 2023 shared-drive copy has 29 discontinued items, misses 101 active ones, prices a median 12.7% low; ChatNest's "₪4,290" Oslo sofa is ₪4,990 in the ERP | **Usable now from the ERP only**; delete or archive the copies (owner: Liat Dahan, merchandising, with Avi) | — |
| WhatsApp tally → E | One week; 4 date formats; language values in Hebrew words and codes; 44 topic labels; order number on 39.4% in a format that matches no ERP order (0 of 248) | **Not yet** for anything but sizing the channel | A channel decision (02.6); if WhatsApp stays, a business integration with a real export |

**Questions for counsel / the DPO (sent through Michal).** (1) May past support emails be used, pseudonymised, to build and test a draft-reply tool inside an approved tool, given the privacy notice's purposes? Does the vendor's processing involve a transfer abroad? (2) The claims log (names, phones) on a shared drive, copied quarterly by Finance: what access and retention rules apply? (3) Customer messages and damage photos on four shared WhatsApp phones: what must change, and how fast? (4) Has anyone reviewed the company's databases and the DPO question after Amendment 13 (IT's note says nobody knows)?

</details>

## References

- WIPO Lex, [Privacy Protection Law, 5741-1981](https://www.wipo.int/wipolex/en/text/347462) — unofficial English translation (2014; Hebrew version controlling): section 2(9), section 8(b).
- E. B. N. Law, [A significant legislative change in the Israeli privacy law](https://www.ebnlaw.co.il/?p=21834) — Amendment 13: purpose principle, registration narrowed, definitions, administrative sanctions.
- Pearl Cohen, [Major amendment to Israeli privacy law set to take effect](https://www.pearlcohen.com/major-amendment-to-israeli-privacy-law-set-to-take-effect/) — in force August 2025; registration limited; DPO duty.
- Pearl Cohen, [Israel: new draft guidelines on the application of privacy law to AI](https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/) — legal basis, transparency on AI processing, DPIAs (draft).
- IAPP, [The new Israeli data security regulations: a tutorial](https://iapp.org/news/a/the-new-israeli-data-security-regulations-a-tutorial) — in force 8 May 2018; security levels; access control.
- GDPR, [Article 5](https://gdpr-info.eu/art-5-gdpr/) — purpose limitation (for organizations GDPR reaches).
- The course's [laws and guidance list](../../references/laws-and-guidance.md). Template: [data profile](../../templates/data-profile.md).
- Previous: [02.4 · Measuring a baseline from exports](lesson-04.md). Next: [02.6 · The readiness assessment](lesson-06.md).
