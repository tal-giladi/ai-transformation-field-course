---
id: "02.4"
module: 2
minutes: 20
practice_minutes: 100
prerequisites: ["02.3"]
objectives:
  - "Write a baseline as a definition card (event, population, clock, statistic, period, source) before computing it."
  - "Measure volumes and first-response time from a helpdesk export, a phone log and a hand tally, and explain why each system gives a different baseline."
  - "Estimate a share that no field records by reading a random sample, with a 95% interval."
  - "Design a two-week time study that gives per-item handling time where time sheets and timers cannot."
volatility: implementation
sources:
  - title: "NIST/SEMATECH e-Handbook of Statistical Methods — Confidence intervals for proportions (7.2.4.1)"
    url: https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm
  - title: "Microsoft Support — NETWORKDAYS.INTL function (weekend codes)"
    url: https://support.microsoft.com/en-us/office/networkdays-intl-function-a9b26239-4f20-46a1-9ab8-4e925bfd5e28
last_verified: "2026-11-02"
---

# 02.4 · Measuring a baseline from exports

Every claim your program will make later — faster replies, fewer contacts, hours saved — is a difference from a baseline. If the baseline is the wrong number, or a number nobody can reproduce, the claim is worthless however good the pilot is. In this lesson you measure Harbor & Pine's support baselines yourself from four sources that disagree: the helpdesk export, the CEO's KPI report, the phone log and the agents' one-week WhatsApp tally. You also measure the delivery promise that drives the contacts, estimate a share no field records by reading a sample, and design a time study for handling time. At the end you have a one-page baseline sheet in which every number has a definition, a source and an n.

## The situation

Week 3, Wednesday 18 November 2026. Ronit, the CFO, asked a simple question when you met her: "What is the number today, and how will I know it moved?" The CEO's KPI report says first response is 2.0 hours, on target. Samir told you weekends and the web form are not in it. The agents' tally from October counted 630 WhatsApp conversations in five days, a channel no report includes. The time sheets say email is 70% of the team's time.

Four systems, four pictures. If you pick one without saying how it was made, the pilot will be judged against a number that means something different from what everyone thinks.

IBM's value course asks for a baseline and a credible comparator before any benefit claim, and never shows how to measure one. Here you measure it, from the exports.

## What to do

### Step 1 — Write the definition card before you compute

A baseline is not a number; it is a number plus the rule that produced it. Write the rule first:

| Field | Example: first response |
|---|---|
| Event that starts the clock | Ticket created (`created_at`) |
| Event that stops it | First agent reply (`first_response_at`) |
| Population | Which channels, which days, which statuses (spam out?) |
| Clock | Wall clock, or working hours (which days, which hours) |
| Statistic | Median, 90th percentile, mean — and why |
| Period | Which months; seasonal? |
| Source and n | File, export date, number of items |

Prefer the median and the 90th percentile for waiting times: a few tickets left over a weekend pull the mean far from what a typical customer experiences, and the 90th percentile shows the bad tail customers remember.

### Step 2 — Volumes: what comes in, where, and when

From `support/tickets.csv` and `support/phone-log.csv` (the phone log is in UTC; convert to Israel time before you group by month or hour):

| Month 2026 | Email | Web form | Tickets | Calls in hours | Answered | Abandoned | After hours |
|---|---|---|---|---|---|---|---|
| May | 188 | 84 | 272 | 293 | 276 | 17 | 88 |
| Jun | 225 | 102 | 327 | 310 | 283 | 27 | 86 |
| Jul | 295 | 130 | 425 | 402 | 344 | 58 | 88 |
| Aug | 314 | 134 | 448 | 476 | 406 | 70 | 123 |
| Sep | 335 | 152 | 487 | 490 | 394 | 96 | 186 |
| Oct | 398 | 172 | 570 | 501 | 403 | 98 | 151 |

Then the channel nobody exports. The WhatsApp tally (`support/whatsapp-week-tally.csv`) covers Sunday 18 to Thursday 22 October: **630 conversations** by 12 agents, **124 estimated agent-hours**. The helpdesk received **94 tickets** in the same five days. Scaled up (× 52/12) the tally suggests about 2,700 WhatsApp conversations a month against about 450–570 helpdesk tickets.

That one comparison changes the picture: most written work is on WhatsApp. It also explains the time sheets: in the week of 18 October the 13 non-manager staff logged 280 hours in the "email" bucket, which holds all written work, and only 94 tickets reached the helpdesk.

Write the tally's limits next to it every time: one week, chosen by the manager, in the October rise; minutes estimated in multiples of 5; topics in the agents' own words; no timestamps of when the customer wrote or got an answer; a busy agent may forget to tally.

### Step 3 — First response: four definitions, four numbers

Compute the same idea four ways from `support/tickets.csv` (n = 2,319 tickets with a reply):

| Definition | n | Median | p90 | Mean |
|---|---|---|---|---|
| KPI report's definition: Q3, email, received Sun–Thu, working hours 08:00–17:00 | 718 | 1.06 h | 3.91 h | **1.97 h** |
| All tickets, all days, working hours | 2,319 | 1.26 h | 4.67 h | 2.10 h |
| All tickets, all days, wall clock | 2,319 | **6.12 h** | 33.6 h | 11.7 h |
| Email only, wall clock | 1,574 | 4.33 h | 26.7 h | 10.9 h |
| Web form only, wall clock | 745 | 9.95 h | 39.3 h | 13.5 h |

And from the other systems:

- **Phone** (`phone-log.csv`): answered calls waited a median of **82 seconds** (mean 99 s, which is the KPI report's "1.7 min"); **14.8%** of in-hours calls were abandoned; 722 calls came after hours.
- **WhatsApp tally**: no first-response time at all. The tally has no time the customer wrote and no time of the reply; 72% of rows give only "morning", "noon" or "afternoon".

So the KPI's "2.0 hours" is correct by its own definition: it reproduces as 1.97. It is also not the customer's wait. A customer who fills in the web form on Thursday afternoon waits a median of about ten hours by the clock, and the KPI never sees them. Report both, labelled, and agree with Michal and Ronit which one the program will be judged on. A pilot measured on the wall clock and compared with the KPI's working-hours mean would "improve" or "worsen" by a factor of three without anything changing.

**Track A.** Timestamps carry a time-zone suffix (`+03:00`). Add a column `=DATEVALUE(LEFT(B2,10))+TIMEVALUE(MID(B2,12,8))` for each timestamp; they are already Israel local time. Wall-clock hours: `=(K2-B2)*24`. Working hours with Friday–Saturday weekends: use `NETWORKDAYS.INTL` with weekend code `7` (Friday, Saturday), for example the standard pattern `=(NETWORKDAYS.INTL(B2,K2,7)-1)*(9/24) + IF(NETWORKDAYS.INTL(K2,K2,7), MEDIAN(MOD(K2,1),17/24,8/24), 17/24) - MEDIAN(NETWORKDAYS.INTL(B2,B2,7)*MOD(B2,1),17/24,8/24)` then ×24. Pivot by channel with median (Excel: use a helper with `MEDIAN(IF(...))`, or Google Sheets' `MEDIAN(FILTER(...))`).

### Step 4 — The share of "where is my order?": five signals, one range

No field in any system says "WISMO". The category field cannot, because "Delivery" was split on 1 July (handbook Addendum A) and 28.5% of tickets sit in "Other/כללי". So you triangulate:

| Signal | Count | Share | Why it is high or low |
|---|---|---|---|
| Helpdesk tag `macro_order_status` | 791 / 2,529 | 31.3% | Lower bound: only tickets where the macro was used; the best agents skip it |
| Helpdesk category "Delivery" + "Delivery status" | 583 / 2,529 | 23.1% | Too low (WISMO in "Other") and mixed (pre-July "Delivery" includes damage) |
| Web-form reason "סטטוס הזמנה / Order status" | 269 / 774 | 34.8% | Customer's own choice of reason; web form only |
| Phone IVR option 1 (order status), in hours | 1,022 / 2,472 | 41.3% | Caller's own choice; phone only |
| WhatsApp tally, delivery-date topics | 276 / 630 | 43.8% | One week in October, agents' labels |

Stated honestly: **between a third and a half of contacts, about two in five, are "where is my order?"**, highest on the channels where the customer chooses the reason (phone, WhatsApp) and in the months after June. That is a usable baseline; "31.3%" or "23.1%" alone would not be.

### Step 5 — When no field holds it: read a random sample

To get closer than a range for the helpdesk, read the messages. `support/emails.csv` holds the full text of 600 tickets; reading all of them takes a day, so start with a random sample and code each message yourself ("where is my order", "damage", "other"). The sampling error of a share $p$ from $n$ items is about

$$\pm 1.96\sqrt{\frac{p(1-p)}{n}}$$

With $n = 100$ and $p \approx 0.35$ that is about ±9 percentage points; $n = 400$ gives about ±5. The NIST handbook notes that this normal approximation is weak when counts are very small and recommends the Wilson interval then; for shares between 20% and 80% with $n \ge 100$ it is fine. Draw the sample at random (a random-number column, sort, take the first 100), never "the first 100 rows", which are all from May. Reading all 600, as one reviewer did, gives 227 WISMO = 37.8%.

### Step 6 — The delivery promise: the baseline behind the contacts

The contacts have a cause you can measure directly, in `orders/orders.csv` and `orders/shipments.csv`:

- **The promise is a constant.** `promised_delivery_date − order date` is exactly 42 days for Vietnam, 38 for China, 21 for Turkey, 28 for Italy, for every order — the table in `orders/storehub-delivery-settings.csv`, last changed 14 February 2023.
- **The lateness.** Vietnam and China orders promised from 1 June and delivered: **median 11 days late, 95% late** (n = 1,106). Promised before June: median 3 days early. Turkey and Italy: median 5 days early. At the export date, **164 orders** were past their promised date and not delivered.
- **The contacts follow the containers.** Join tickets to orders (normalise the hand-typed order numbers first: `so26…`, `SO-26…`, `#…`), orders to containers, containers to `shipments.csv`. For the 43 Vietnam/China containers with an original ETA from June and a delay of a week or more (median delay 14 days), WISMO-tagged tickets on their orders arrive a median of **12 days after the container's original ETA** — for most containers between 10 and 13 days. That is the days-later wave Michal and Samir describe, measured.

### Step 7 — Handling time needs a time study

None of the sources gives a trustworthy minutes-per-item:

- The Deskly timer is filled on 51% of tickets (median 9 minutes), by the agents who choose to use it.
- The tally's minutes are estimates in multiples of 5 (median 10): rounding and recall bias.
- The time sheets have three coarse buckets.
- Your sit-in (02.3) timed 24 items: valuable, too small.

Design a light study that the team can run in peak season: two weeks in December, four agents (including one Russian and one Arabic speaker), the Deskly timer on for every ticket, and a WhatsApp log with start and end times for every conversation; at least 30 items per task type per language. Agree it with Samir as a measurement of the work, not of people, and report only medians per task and language.

### Step 8 — Write the baseline sheet

One card per baseline: definition, number, n, period, source, limits, and who agreed it. Send it to Michal and Ronit with one sentence: "These are the numbers we will measure any change against; please confirm or correct the definitions."

**Track B (Python).** Python is worth it here because the same baselines must be re-run every month on fresh exports, the working-hours calculation is painful in a spreadsheet, and the container join links three files with hand-typed keys. From `labs/module-02/`:

```bash
python baseline.py
```

It prints all the tables above: volumes, the four first-response definitions, the five WISMO signals, a random sample of 100 with its interval, where agent time goes, the delivery promise and the wave after container delays. It uses `fieldkit.baseline` (`elapsed_hours`, `working_hours`, `summarize`, `sample`).

## Watch out

- **A number without its definition.** "2 hours" is meaningless without population, clock and statistic. Write the card first.
- **Comparing across definitions.** A pilot measured on the wall clock against a working-hours baseline proves nothing. Measure before and after the same way.
- **The mean for waiting times.** It is pulled by weekends; use median and p90.
- **Taking the category field as truth.** A re-definition mid-period (1 July) and a 28.5% "Other" make it a weak signal. Triangulate.
- **Treating a tally like an export.** One manager-chosen week of estimates. Use it, say so, and design a better measurement.
- **Ignoring time zones.** The phone log is UTC; the others are Israel time with an offset. Mixing them shifts calls across days and hours.
- **The first 100 rows as a "sample".** They are all from May. Sample at random.
- **Measuring only the symptom.** The contacts have a measurable cause: the promised date. Baseline it too; it will be the first thing to change.

## Your turn

### Inputs

- In the module download: [`support/tickets.csv`](../../labs/common/harbor-and-pine/support/tickets.csv), [`support/phone-log.csv`](../../labs/common/harbor-and-pine/support/phone-log.csv), [`support/whatsapp-week-tally.csv`](../../labs/common/harbor-and-pine/support/whatsapp-week-tally.csv), [`support/emails.csv`](../../labs/common/harbor-and-pine/support/emails.csv), [`company/kpi-report-2026-q3.md`](../../labs/common/harbor-and-pine/company/kpi-report-2026-q3.md), [`people/timesheets.csv`](../../labs/common/harbor-and-pine/people/timesheets.csv), [`orders/orders.csv`](../../labs/common/harbor-and-pine/orders/orders.csv), [`orders/shipments.csv`](../../labs/common/harbor-and-pine/orders/shipments.csv), [`orders/storehub-delivery-settings.csv`](../../labs/common/harbor-and-pine/orders/storehub-delivery-settings.csv).
- Track B: `labs/module-02/baseline.py` ([lab README](../../labs/module-02/README.md)).

### Steps

1. Write definition cards for: monthly contact volume (per channel), first response, WISMO share, delivery lateness.
2. Compute volumes per month and channel, and the tally week against the helpdesk the same five days.
3. Reproduce the KPI report's 2.0 hours from the export, then compute the wall-clock median and p90 for all tickets and per channel.
4. Compute the five WISMO signals and state the range.
5. Draw a random sample of 100 tickets from `emails.csv`, code them, and give your share with its 95% interval.
6. Measure the promised lead times and the lateness for Vietnam/China orders from June.
7. Write a two-week time-study design (who, what, how long, what is reported).
8. Put it all on one baseline sheet with a cover sentence to Michal and Ronit.

**Track B (Python).** Run `python baseline.py`, check that its numbers match yours for steps 2–6, then change one definition (for example working hours to 08:00–18:00, the handbook's hours) and see how much the result moves.

### Time

100 minutes (Track B: about 60).

### Done when

- [ ] Every baseline has a definition card: start, stop, population, clock, statistic, period, source, n.
- [ ] The KPI's 2.0 hours is reproduced and shown next to the wall-clock median and p90.
- [ ] The WISMO share is a range from at least four signals, each with why it is high or low.
- [ ] The tally's numbers carry their limits.
- [ ] The sample share has a 95% interval.
- [ ] The delivery lateness is measured by country and period.
- [ ] The time study names who, how long, the minimum items per task and language, and what will be reported.

<details><summary>Reference answer</summary>

**Baseline sheet — Harbor & Pine Customer Service — 18 November 2026.** Sources: exports of 31 October 2026; tally of 18–22 October.

| # | Baseline | Definition | Value | n, period, source | Limits |
|---|---|---|---|---|---|
| B1 | Helpdesk volume | Tickets created, email + web form, spam included | 272 (May) → 570 (Oct) a month | 2,529, May–Oct, `tickets.csv` | Spam 5.4% |
| B2 | Phone volume | Calls in opening hours (answered + abandoned) | 293 (May) → 501 (Oct) a month; 722 after hours in total | 3,194, `phone-log.csv` (UTC) | — |
| B3 | WhatsApp volume | Conversations tallied by agents | 630 in 5 days (~2,700 a month); 124 est. agent-hours | 1 week, `whatsapp-week-tally.csv` | Hand tally; estimates; one week |
| B4 | First response (KPI) | Working hours Sun–Thu 08–17, Q3, email received on business days, mean | 1.97 h (median 1.06) | 718 | Excludes web form, weekends |
| B5 | First response (customer) | Wall clock, all channels, all days, median / p90 | 6.1 h / 33.6 h (email 4.3 h, web form 10.0 h) | 2,319, May–Oct | Helpdesk only; WhatsApp unmeasured |
| B6 | Phone wait | Answered calls, wait seconds, median; abandoned share in hours | 82 s; 14.8% abandoned | 2,106 answered | — |
| B7 | WISMO share | Five signals | 31% (macro, lower bound) – 44% (WhatsApp); emails read 37.8% | see Step 4 | Category field unusable |
| B8 | Delivery promise | Promised − order date | VN 42, CN 38, TR 21, IT 28 days, fixed since 14 Feb 2023 | 3,134 orders | — |
| B9 | Delivery lateness | Actual − promised, VN/CN promised from 1 June, delivered | median +11 days, 95% late | 1,106 | 164 overdue undelivered at export |
| B10 | Contact wave | WISMO-tagged tickets after a delayed container's original ETA | median 12 days (most containers 10–13) | 651 tickets, 43 containers | Tag is a lower bound |
| B11 | Handling time | Minutes per item by task and language | Not measured — time study 6–17 Dec | — | Timer on 51%; tally estimates |

**Sample.** One random draw of 100 (seed 7 in `baseline.py`) had the order-status macro on 36 tickets: 36% (95% interval 27–45%), against 31.3% in the full export — the interval covers the truth, and shows why 100 is the minimum.

**Time study.** 6–17 December (two weeks, inside peak by necessity, agreed with Samir); Olga, Hila, Lina, Daniel volunteer; Deskly timer on for every ticket; a WhatsApp log with start and end time per conversation on phones 2 and 4; at least 30 items per task (WISMO, damage first answer, booking, other) per language (he, ru, ar); reported as medians per task and language, never per person.

**Cover sentence.** "Michal, Ronit — these eleven numbers are what any change will be measured against. B4 is the KPI as reported; B5 is what the customer experiences; I suggest we report both. Please confirm the definitions by 24 November."

</details>

## References

- NIST/SEMATECH, [Confidence intervals for proportions](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) — the normal approximation and the Wilson interval for small counts.
- Microsoft Support, [NETWORKDAYS.INTL](https://support.microsoft.com/en-us/office/networkdays-intl-function-a9b26239-4f20-46a1-9ab8-4e925bfd5e28) — weekend code 7 = Friday and Saturday (checked 2 November 2026).
- Lab: `labs/module-02/baseline.py`, [module 2 lab README](../../labs/module-02/README.md); field kit helpers in [`labs/common/README.md`](../../labs/common/README.md).
- Previous: [02.3 · Process walk and task inventory](lesson-03.md). Next: [02.5 · Profiling the data](lesson-05.md). Related: [01.5 · Access and the first-day data-room read](../module-01/lesson-05.md) (the KPI as a claim to test).
