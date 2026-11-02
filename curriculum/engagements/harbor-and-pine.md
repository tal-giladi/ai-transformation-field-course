# Harbor & Pine — writer's notes (never imported)

The warm-up organization for Stage 1 (modules 1–7). Every Stage 1 lesson practises on it. The data
room lives in `labs/common/harbor-and-pine/` so every module zip includes it.

## The company

- **Harbor & Pine Ltd.** (הארבור אנד פיין בע"מ), furniture and home-goods importer, founded 2009.
  ~120 employees. Revenue ~₪96M (2025). Imports from Vietnam, China, Turkey and Italy by sea
  container (Haifa and Ashdod ports). Sells B2C (website + showrooms in Tel Aviv and Haifa, ~70% of
  revenue) and B2B (hotels, offices, ~30%).
- Sites: head office and warehouse in Rishon LeZion; showrooms in Tel Aviv and Haifa.
- Systems: Priority ERP (orders, stock, purchasing); a cloud helpdesk ("Deskly", fictional) for
  support email and web form; a cloud phone system (call logs); Shopify-like web store ("StoreHub",
  fictional); Google Workspace; an HR SaaS ("PeopleWise", fictional) that added an "AI candidate
  match" feature in an auto-update in March 2026; a shipping-tracking spreadsheet the logistics team
  keeps by hand from the freight forwarder's emails. IT is one person plus an outside MSP.
- No works committee (too small and not unionised); labour law still applies.

## Who the learner is

Michal Peretz (COO) hired the learner as "Head of AI and Operations Improvement", reporting to her,
start date Monday 2 November 2026. The CEO, Yoav Ben-Ami (founder's son), came back from a
conference and told the board in September: "we'll have an AI customer-service bot and an AI
strategy within 90 days, and cut support cost by 40%". The board meets on 28 January 2027.

## Stated ask vs hidden truth

- **Stated ask (CEO):** a chatbot that replaces a big part of the 14-person support team, and an AI
  strategy for the board.
- **Hidden truth:** ~38% of support contacts are "where is my order?" (WISMO). They are caused by the
  delivery date promised at checkout, which comes from a fixed lead-time table in the web store and is
  never updated when a container is delayed. Logistics knows the real ETAs (in their tracking
  sheet) but nobody tells customers. The biggest, cheapest win is plain automation: a daily job that
  compares promised dates with container ETAs and emails customers proactively — no AI. A chatbot
  would answer WISMO with the same wrong date.
- The AI pilot that does make sense (module 5): support-email triage + draft replies for the
  remaining categories (damage claims, assembly questions, returns, B2B quotes), in Hebrew, Arabic,
  Russian and English, with a human sending every reply.
- **Second hidden layer:** support agents already use free ChatGPT to draft replies, pasting customer
  names, phone numbers and addresses (a privacy problem under the Privacy Protection Law and its
  Amendment 13). They do it because it saves time on Russian and Arabic replies. The lead (Olga) is
  the best agent on the team and the secret enthusiast — punish her and you lose the pilot's best ally.

## Planted findings (each must be discoverable from the data, never stated)

1. WISMO share ~38% of tickets; spikes follow container delays in `shipments.csv` by 3–10 days.
2. Promised delivery dates in `orders.csv` come from a fixed lead time per supplier country;
   actual delivery lags by a median of 11 days for Vietnam/China orders since June 2026.
3. Three baselines for "first response time": helpdesk export (median ~6.5 business-and-weekend
   hours… compute from timestamps), the CEO's KPI report (says "2 hours", business hours only,
   excludes the web form channel and weekends), the phone-system log (answered calls, minutes).
4. The helpdesk status "resolved" is set by the agent when they send a reply, not when the issue is
   solved; ~22% of "resolved" tickets get a follow-up from the same customer within 14 days
   (a new ticket, not a reopen — find by customer_id + order_id).
5. Category field: ~28% "Other/כללי"; categories were redefined on 1 July 2026 (old "Delivery" split
   into "Delivery status" and "Delivery damage") — a report definition change.
6. Duplicates: ~6% of tickets are the same customer emailing twice within an hour.
7. Damage claims: approval outcome recorded only in `damage-claims-log.csv`, kept by one person
   (Rina), missing for ~35% of claims (outcome never recorded → not a training label).
8. The handbook says "damage claims are reviewed by QA within 48 hours"; there is no QA role and no
   such step in the data (a step that exists only on paper).
9. Stale copy: `catalog/products-2023-shared-drive-copy.csv` on the shared drive; the ChatNest demo
   was built on it (wrong prices, discontinued items).
10. Shadow AI: proxy log shows chat.openai.com/chatgpt.com, gemini, claude.ai, deepl, a "Grammarly"
    extension, and an AI copy SaaS; expenses show "CopyGenie Pro" and ChatGPT Plus on personal cards
    (marketing, one buyer); browser-extension inventory shows an AI translation extension on 9
    machines; the HR SaaS release notes show the AI candidate-match feature turned on by default.
11. Counting rule trap: the ERP's "smart reorder" is a rules engine (min/max thresholds) marketed as
    AI; the accounting "auto-match" is rules. Not AI for the inventory.
12. Time sheets: support agents log time in three coarse buckets; the "email" bucket is
    ~70% of logged time; the team is at ~92% utilisation in Nov–Jan (peak season).
13. Finance: support cost ~₪3.4M/yr fully loaded; CFO's hurdle rate 12%; any project above
    ₪150k needs board approval.
14. The flawed AI-drafted findings memo (for 02.7) says WISMO is 15% (it counted only the new
    category since July), cites a "Gartner 2025 study" that does not exist, and misreads the KPI
    report's 2-hour figure as the median.
15. The previous consultant's roadmap (for 07.7) puts the chatbot first, assumes 70% deflection from
    the vendor deck, has no gates, and schedules everything in Q1 during peak season.

## The cast (persona pack)

| Persona | Role | Type | Hidden / unlock |
|---|---|---|---|
| Yoav Ben-Ami | CEO | sponsor's boss, board-facing | Already told the board "40%"; unlock: ask what he told the board, privately |
| Michal Peretz | COO, the sponsor | sponsor | Worried logistics is the real problem; unlock: ask what keeps her up at night about delivery |
| Ronit Avraham | CFO | sceptic, finance | Has a hurdle rate and template; burned by a 2022 CRM project; unlock: ask how the last big project was judged |
| Samir Haddad | Customer Service Manager | middle manager | Knows WISMO is the top driver; afraid of headcount cuts; unlock: promise of no attribution + ask for a normal day |
| Olga Petrenko | Senior support agent | frontline, secret enthusiast | Uses ChatGPT daily with customer data; unlock: show you are not hunting people, ask how she writes Russian replies so fast |
| Avi Mizrahi | IT manager (one-person IT) | IT/security | Knows the proxy shows AI sites; never acted; unlock: ask what the proxy logs |
| Tamar Shalev | Logistics manager | data steward / receiving team | Keeps the ETA sheet; knows promised dates are wrong; nobody asked; unlock: ask where ETA updates go |
| Noa Levi | Marketing director | process owner who adds scope | Keeps adding "while you're at it" items; uses CopyGenie on a personal card |
| Dana Katz | HR manager | HR, workforce | Didn't know the AI candidate match was turned on; worried about training time in peak season |
| Eitan Gross | ChatNest account executive | vendor AE | The 70% deflection was measured on US English retail with order tracking integrated |

Lessons that use them: 01.2 (Michal), 01.3 (Noa), 02.2 (Samir, Olga, Tamar), 03.5–03.6 (Yoav,
Ronit, Michal, Samir), 03.9 (Yoav), 04.8 (Eitan), 06.6 (Samir, Olga, Dana), 07.3 (Yoav), 07.4 (all
seniors).

## Timeline (data dates)

- Tickets, emails, orders, shipments: 1 May 2026 – 31 October 2026.
- Pilot usage export (06.4): weeks 1–8 after a pilot start of 1 February 2027 (synthetic future).
- Learner starts 2 November 2026. Board: 28 January 2027.

## Where each finding is planted

Data room: `labs/common/harbor-and-pine/` (built by `generate.py`, seed 20261102). Ground truth (true
category and language of every ticket and email, duplicates, follow-ups, order lags, claims with an
outcome) is in `curriculum/engagements/harbor-and-pine-answer-key/` (`python generate.py --answer-key
<dir>`); never link it from lessons. All numbers below were computed from the generated files with
spreadsheet-style operations (filter, pivot, lookup) unless marked *truth*. Paths are relative to the
data room. Where a number differs from the design notes above, the design intent is kept and the actual
value is given.

**Volumes for context.** `support/tickets.csv` 2,529 tickets, 1 May – 31 Oct 2026 (email 1,755, web
form 774); per month 272 / 327 / 425 / 448 / 487 / 570 (May → Oct). `support/phone-log.csv` 3,194 calls
(2,106 answered, 366 abandoned, 722 after hours). `orders/orders.csv` 3,134 orders (placed 15 Mar – 31
Oct). True languages: Hebrew 1,508 (59.6%), Arabic 353 (14.0%), English 352 (13.9%), Russian 316
(12.5%). The `language` column is auto-detected: 121 blank and 85 wrong codes (yi, fa, ur, uk, bg, nl,
de).

1. **WISMO share (~38%).** *Truth:* 964 of 2,529 tickets = **38.1%**; by month 7% / 25% / 44% / 39% / 47%
   / 47%; Jul–Oct ≈ 44%. Discoverable: (a) tag `macro_order_status` in `tickets.csv` `tags` = 791 tickets
   = **31.3%** (a lower bound: agents use the order-status macro on 85% of WISMO replies); (b) reading
   `support/emails.csv` (a random 600): 227 WISMO = **37.8%**; (c) web-form subjects with reason "סטטוס
   הזמנה / Order status": 269 of 774 web-form tickets = 34.8%; (d) phone IVR option 1 (order status) =
   41.3% of in-hours calls. The category field cannot give it (see 5): 317 WISMO tickets (43.9% of
   "Other/כללי") hide in Other. **Spikes follow container delays:** join `tickets.order_id` →
   `orders.container_no` → `shipments.csv`; for the 40 Vietnam/China containers with original ETA from
   June and a delay ≥ 7 days, WISMO tickets on their orders cluster a median **12 days after the
   container's original ETA** (per-container medians 10–15 days), i.e. 0–4 days after the promised dates
   pass. The design said "3–10 days after the delay"; measured from the original ETA it is 10–15.
2. **Promised dates from a fixed lead time; delivery lag.** `orders.csv`: `promised_delivery_date −
   date(order_created_at)` is constant per country: Vietnam 42, China 38, Turkey 21, Italy 28 days (also
   `orders/storehub-delivery-settings.csv`, last modified 2023-02-14 by noa.levi). `actual − promised`
   for Vietnam/China orders with promised date ≥ 1 June 2026 and delivered: **median 11 days** (mean 11.1,
   n = 1,106, 95% late); promised before June: median −3 (n = 308); Turkey/Italy, all: median −5
   (n = 1,102). By order date ≥ 1 June instead: median 12 (n = 800). `shipments.csv`: Vietnam/China
   containers with original ETA from June that have arrived: 41, of which 40 are ≥ 7 days late, median
   delay **15 days** (5–23). 164 orders were past their promised date and not delivered at export.
3. **Three first-response baselines.** (a) `tickets.csv`, `first_response_at − created_at`, wall-clock,
   all tickets with a response: **median 6.1 hours** (6.12; n = 2,319; mean 11.7); email 4.3 h, web form
   10.0 h; Q3 only 6.5 h. (b) `company/kpi-report-2026-q3.md`: **"2.0 hours"** = the *mean* of working
   hours (Sun–Thu 08:00–17:00) for Q3 **email-only** tickets **created Sun–Thu** (n = 718; exact 1.97;
   median of the same set 1.06). It excludes the web form and Friday/Saturday tickets; the definition is
   in footnote 1. Working-hours median for all channels and days: 1.25 h. (c) `phone-log.csv`, answered
   calls: **median wait 82 seconds** (1.4 min; mean 99 s = the KPI report's "1.7 min"); 14.8% of
   in-hours calls abandoned. The phone log is in UTC. Support hours are Sun–Thu 08:00–18:00 and Fri
   08:30–12:30 (handbook); the KPI counts only to 17:00.
4. **"Resolved" ≠ solved; follow-ups (~22%).** 1,880 of 2,314 resolved tickets (81.2%) have `resolved_at`
   within 5 minutes of `first_response_at` (the handbook tells agents to resolve on reply). Follow-up
   rule: same `requester_id` and same order, a new ticket created after `resolved_at` and within 14 days.
   Of 1,430 resolved tickets with an `order_id`: 335 = **23.4%** after normalising the order number (6%
   of order ids are typed by hand: `so26…`, `SO-26…`, `26…`, `#…`); 21.3% matching the raw text. As a
   share of all 2,314 resolved tickets: 14.5%. *Truth:* 253 follow-up tickets. Only ~8% of follow-ups
   carry the tag `2nd_contact`.
5. **Category field.** `tickets.category`: "Other/כללי" 722 = **28.5%**; blank 78 = 3.1%. Before 1 July
   the value is "Delivery" (120 tickets); from 1 July "Delivery status" (463) and "Delivery damage" (115).
   The change is documented only in the handbook's Addendum A. "Delivery" + "Delivery status" = 23.1% of
   all tickets.
6. **Duplicates (~6%).** Same `requester_id` with a second ticket within 60 minutes of the previous one:
   **157 tickets = 6.2%** (*truth:* 152 = 6.0%). 35% of true duplicates were merged (status `closed`, tags
   `duplicate merged`); the rest were answered twice.
7. **Damage claims: outcome missing.** `claims/damage-claims-log.csv`: 149 claims; column "החלטה"
   (decision) blank for **48 = 32.2%** (31.4% among claims opened by 30 Sep, so not just recent ones).
   Recorded: approved 55, partly approved 28, rejected 18. The log holds customer names and phone numbers
   on a shared drive.
8. **QA step on paper only.** `company/customer-service-handbook.md` §8: "Every claim is reviewed by QA
   within 48 hours." No QA role in `company/org-chart.md` or `people/headcount.csv`; no QA column in the
   claims log; decision date − opening date: median **8 days**, only 5% within 2 days. Olga and Samir
   (personas) say QA was cut in 2023.
9. **Stale catalogue.** `catalog/products-2023-shared-drive-copy.csv` (144 SKUs, Hebrew headers) vs
   `catalog/products.csv` (245 SKUs): 29 of the copy's items are now discontinued; 101 active items are
   missing from it; prices in the copy are lower (median 15.4% below current). The ChatNest demo
   (`vendors/chatnest-sales-deck.md`, slide 4) quotes the copy: Oslo 3-seat sofa grey **₪4,290** (current
   ₪4,990, SKU HP-SOF-1028) and recommends the Bergen dining table 180 oak at ₪3,450 (discontinued
   2025-08-01, HP-DTB-1097). Footnote 4: file received from marketing on 28 Sep 2026.
10. **Shadow AI.** `it/proxy-log.csv` (2,918 rows, 11–22 Oct): chatgpt.com from Customer Service 148
    requests (+12 chat.openai.com), Marketing 38, Purchasing 18; claude.ai Finance 5; gemini Customer
    Service 8, B2B 1; app.copygenie.io Marketing 54 (category "Uncategorized"); api.linguaflow.ai Customer
    Service 170, Showroom Sales 27, Logistics 15, Purchasing 9 ("Uncategorized"); capi.grammarly.com 161;
    www.deepl.com 38. Distinct generative-AI users: Customer Service 5, Marketing 2, Purchasing 1,
    Finance 1, B2B 1. Customer Service requests to chatgpt.com have large `bytes_out` (pasted text).
    `it/browser-extensions.csv`: LinguaFlow – AI Translate & Rewrite on **9** machines (6 Customer
    Service, 1 Purchasing, 1 showroom, 1 import coordinator), Grammarly 6, "ChatGPT Sidebar" 2.
    `it/expenses.csv`: CopyGenie Pro (Noa Levi, US$39 × 9 months = ₪1,298.70), ChatGPT Plus (Shir Barak
    ₪518, Igor Volkov ₪370), Midjourney (Shir, ₪111), Claude Pro (Natalia Gurevich, ₪74), all on personal
    cards. `it/peoplewise-release-notes-2026-03.md`: AI Candidate Match on by default, while
    `saas-list.csv` says PeopleWise AI "No". `support/emails.csv`: six agent replies carry chatbot traces —
    EM-32522 (Lina, Arabic preamble), EM-32680 (Daniel, "Certainly! Here's a polite…"), EM-34130 (Yana,
    "[Имя клиента]" left in), EM-34247 and EM-34408 (Olga, Russian preambles), EM-34587 (Olga, placeholder).
11. **Counting rule.** `it/saas-list.csv`: SmartStock AI ("AI-powered smart reorder", AI enabled Yes) and
    AutoRecon ("Intelligent auto-match", Yes); `it/smartstock-reorder-config.md` shows both are fixed rules
    (min/max with manual seasonality; four ordered matching rules). The design said "the ERP's smart
    reorder"; to avoid attributing a claim to a real ERP vendor it is a fictional add-on (Optimo Systems).
    RouteMaster ("not ML, per vendor"), Bitdefender's ML detection and NetGuard's URL categorisation are
    borderline cases for discussion.
12. **Time sheets.** `people/timesheets.csv` (14 people, weekly, 2 Nov 2025 – 25 Oct 2026): email bucket =
    **70.7%** of logged hours for the 13 non-manager staff (67.6% including the manager); utilisation
    (logged ÷ (contracted − absence)) **92.2% in Nov–Jan**, 82.5% Feb–Oct (83.3% May–Oct). For scale:
    `time_spent_min` is filled on 51% of tickets (median 9 min; Hebrew 8, Russian 10, Arabic 11) and sums
    to 235 hours, against ~6,990 email-bucket hours May–Oct: the bucket covers far more than ticket
    handling (chasing logistics, re-contacts), so per-ticket time needs a time study, not division.
13. **Finance.** `company/finance-summary.md` and `.csv`: customer service fully loaded ₪3.40M (FY2025:
    salaries 3.02M, licences 0.11M, allocation 0.27M); hurdle rate 12%; board approval above ₪150k over
    three years (CEO ₪50–150k); payback ≤ 24 months preferred; headcount savings count only with a named
    plan; planning rate ₪3.70/US$; FY2023 software write-off ₪860k (Ronit's CRM story).
    `people/headcount.csv` bands for the 14 support staff: 12 × ₪16–19k, 1 × ₪23–28k, 1 × ₪28–35k.
14. **Flawed AI memo.** `documents/findings-memo-ai-draft.md` (generated from the data): WISMO "only
    **18%**" (= "Delivery status" 463 ÷ all 2,529; the design said 15%; the new category since July over
    all six months gives 18.3% here), "median first response of 2 hours" (the KPI figure is a mean of
    working hours, email only), a "Gartner 2025 study of 400 retailers" that does not exist, "resolves
    100% of tickets" (status, not outcome), "every ticket has a category" (78 blank), and languages taken
    from the auto-detected field.
15. **Previous consultant's roadmap.** `documents/roadmap-previous-consultant.md`: chatbot first (Jan–Feb
    2027), the vendor's 70% deflection as an assumption, no gates, all seven initiatives in Q1 (peak
    season and the weakest cash quarter), "9,000 contacts a year" with no source (data: ~5,000 tickets +
    ~6,400 calls a year), PeopleWise AI recruiting switched on as a "benefit", payback "under 4 months".

**Other plants worth using.** The WISMO macro repeats the original promised date even after it has
passed (e.g. EM-32586, June). `documents/internal-emails-logistics-mailbox.md`: 187 Customer Service
emails to logistics@ in Jul–Sep; container LCLU3259917 (Haiphong → Haifa, ETA 27 Jul → 2 Aug → 7 Aug,
arrived 10 Aug) has 22 tickets on its orders. `orders/logistics-eta-tracking.csv` holds the same dates as
`shipments.csv`, kept by hand (mixed date formats, two containers entered twice — ORLU3326673 and
ADFU3996533 — a few containers never entered, one number typed with a space, footer "44 containers
delayed a week or more since April"). `vendors/deskly-ai-addon-terms.md` clauses to
flag: training on customer content unless opted out (§3.2), 24-month analytics retention (§3.4), US
storage (§5.1), Autopilot switchable by any admin (§1.2), liability capped at three months' fees (§4.3),
objection to sub-processors only by stopping use (§6.1), human review in the Philippines (Annex 1).
`vendors/linguaflow-translation-dpa.md` covers only the paid plan; the 9 installs are the free extension
(texts kept up to 18 months and used for training).

**Usage export (06.4).** `usage/ai-usage-export.csv` (1,778 rows, 1 Feb – 28 Mar 2027) +
`usage/hr-roster.csv`. Qualified event = `draft_inserted` (not `panel_opened`, which fires by itself).
Quiet non-adopters: Sergei Novikov, Moran Biton, Ahmad Jabareen — `draft_inserted` per week 16/21/31/2/0/
0/0/0, 34/24/14/6/0/0/0/0 and 29/31/28/3/0/0/0/0, while their raw event totals stay at 93–270 a week.
Not non-adoption: Hila Dahan (maternity leave from 21 Feb), Adi Golan (resigned, last day 4 Mar). Noa
Levi and Shir Barak hold licences with one event each. Olga Petrenko is the heaviest user; Tigist Mekonen
grows week by week.

**Personas and data.** Persona numbers match the data room: Samir (≈270 → 570 tickets a month, ~17 calls
a day, ~15% abandoned, KPI 2.0 h, CSAT 63%), Tamar (40 of 41 containers late since June, 5–23 days, 187
emails), Olga (≈130 of 316 Russian tickets). Persona-only facts, by design not in the data room: Michal's
₪120k H1 2027 budget, the origin of Yoav's 40%, Ronit's 2022 CRM story (only the write-off line is in the
data), Noa's 2024 refusal to lengthen the Vietnam lead time, the pre-2021 delay SMS, ChatNest's ≈38%
Israeli reference, and Olga's unanswered request to IT (the DPA's cover note dates it 2 Oct 2026).

## Added by the main session (2026-11-02)

16. **WhatsApp is the real channel.** `support/whatsapp-week-tally.csv`: one hand-kept week (Sun 18 –
    Thu 22 Oct 2026), 630 conversations, 123.75 estimated agent-hours, WISMO-type topics 43.8% (topic
    words listed in `generate.py`, `build_whatsapp_tally`). Deskly had 94 tickets that week, so
    roughly 87% of written contact never reaches the helpdesk or the KPI report; ~2,700 conversations
    a month. It reconciles the time sheets (agents log WhatsApp as "email", ~70% of time) with the low
    helpdesk volume. No export: the data sits on four shared phones (privacy and retention finding).
    Unlocks: Samir (channels / why so much "email" time), Olga (normal day, where damage photos arrive).
    Pilot implication (modules 3 and 5): the email pilot touches a minority of written contact; the
    bigger prerequisite is routing WhatsApp into the helpdesk (Deskly's WhatsApp channel), plain
    integration, not AI.
17. **Container frequency.** `company/company-profile.md` says "roughly 2 a week"; `shipments.csv` and
    the profile's own schedule make ~3 a week (a claim contradicted by the data; used in 01.5).
18. **Two order numbers.** WhatsApp tally `order_no` values are `HP-1xxxxx`: the web-store (StoreHub)
    order number customers see on their confirmation SMS. The ERP and every export use `SO26…`. The
    mapping lives only in StoreHub (no export in the data room), so WhatsApp cannot be joined to orders
    until someone gets a StoreHub order export. Samir knows ("customers quote the number from the SMS").

## Timeline for modules 3–7 (main session, 2026-11-02)

- Nov 2026: discovery (M1–M2); scoring workshop 26 Nov; findings memo 1 Dec; Yoav one-to-one 2 Dec;
  alignment session 10 Dec. Date fix + proactive delay emails (no AI) live mid-November.
- Dec 2026 – Jan 2027: pilot built and evaluated on a test set of 400 real emails (M5.1–5.5);
  ROI model to Ronit 14 Jan; steering meeting Tue 19 Jan 2027 (07.4, `steering-committee` sim)
  approves phase 1 with ₪60,000 now and ₪60,000 at the May gate; board 28 Jan 2027.
- 1 Feb 2027: WhatsApp routed into Deskly; shadow mode, then staged release (05.6); training 7–11 Feb
  (M6); `usage/ai-usage-export.csv` covers weeks 1–8 from 1 Feb.
- Mon 15 Mar 2027: the incident (07.5, `incident-tabletop` sim).
- May 2027 gate: scale / fix / stop (07.2), operating rhythm and handover (07.6, 07.9).
- Two temps every peak season (Nov–Jan), ~₪16,000 a month each (Samir's persona); the ROI case's
  cash rests on not hiring them next winter (03.7 marks it as the weakest assumption).
