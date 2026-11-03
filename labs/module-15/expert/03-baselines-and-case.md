# 03 · Baselines, the queue and the one-page case

*For Dalit Ben-Ami and Avner Golan, Thursday 4 February 2027. Labels: **M** measured, **D** directional, **A** assumed.*

## Portfolio baseline (31 December 2026)

| Measure | Value | Label | Definition and owner |
|---|---|---|---|
| Rows in the register | 43 | M | COO office register; owner from now on: AI CoE |
| Distinct builds | 40 | M | Rows sharing environment + test set = one build |
| In production through the approved route | 0 | M | Model Committee approval; owner MRM |
| In real use without approval | 3 known (Branch FAQ, call summaries into CRM, chatbot A/B) + 1 outside the register (dispute letters via a public API) | M | Used by staff or customers on real matters at least weekly |
| Builds with a measured baseline | 22 of 43 rows (16 none, 5 partial) | M | Register `baseline_measured` |
| AI submissions waiting | 19 (2 in validation) | M | MRM queue |
| Median wait | 193 days | M | Submission to 31 Dec 2026 |
| Decisions in 2026 (approved / declined) | 0 / 0 | M | Committee minutes |
| AI review capacity | 3 slots a quarter = 1.5 full validations | M | MRM work plan 2027 |
| AI spend 2027 | ₪20.13M (central ₪11.0M, units ₪9.13M incl. ₪0.42M counted twice) | M | Programme budget, register |

**The three numbers for the board (04.7), today:** reached production 0; decision time median 193 days (slowest: the Branch FAQ, 437); declined 0. A process that declines nothing is not reviewing; one that approves nothing is being bypassed — and it is.

## The queue, in arithmetic

| Design | Builds | To the central queue | Slots | Quarters at 3 slots |
|---|---:|---:|---:|---:|
| Today: everything, full validation | 40 | 40 | 80 | 26.7 |
| Triaged, full validation for all | 26 | 26 | 52 | 17.3 |
| Triaged, validation by tier (0.5 / 1 / 2) | 26 | 26 | 26 | 8.7 |
| Triaged, decision rights by tier (only high to the queue), templates | 26 | 6 | 12 | 2.7 |

(M from the register and MRM's plan; the 1.5× effect of templates and an evaluation kit on validators' time is the simulation's assumption, **A**.) A 16-person central build team adds builders to a queue that cannot validate what they build: in the simulation's terms, "today's set-up" ends 2027 with 2 pilots in production, 13 waiting and 2 shadow tools, and three years later with 7 in production, 29 waiting and 23 shadow tools (educational model).

## Opportunity map, screened (excerpt)

| Option | Kind | Data gate | Screen |
|---|---|---|---|
| Change the decision rights and the validation depth | Not AI: policy | — | **Go**: the binding constraint |
| A catalogue of all AI in use with one owner each | Not AI: register | Logs, contracts, people | **Go**: the supervisor and the board need it |
| A shared platform on IT's approved landing zone | Infrastructure | — | **Go with a condition**: IT owns it |
| Take the 26 kept builds through the new route | AI, by tier | Per build | **Go** in waves |
| Stop 10, merge 4 pairs, clean 3 double counts | Portfolio | Evals, contracts | **Go** before 15 March where contracts force it |
| A 16-person central build team | Org | — | **Stop**: adds to the wrong side of the queue |
| Cancel the assistant | Budget | Usage, dependencies | **Stop**: strands two of the best pilots |

## One-page case (front page)

**Ask.** On 15 March, decide how AI goes to production at Crescent: decision rights by risk tier, a hub-and-spoke CoE instead of a central build team, a catalogue first, and a triaged portfolio of 26 builds with 14 in production by March 2028.

**Why.** The pilots don't stall in the units; they stall at a gate that holds 1.5 AI systems a quarter for 40 builds (M). Meanwhile AI runs without approval in branches, the contact centre and Cards (M), and the bank's survey answer to the supervisor says otherwise (M).

**What it costs.** Within the 15%: the triage releases ₪2.74M of unit lines (₪1.56M stop, ₪0.76M merge, ₪0.42M counted twice) (M), less ₪0.18M of merge work (A); a hub of 10 instead of a central team of 16 releases about ₪1.0M of the central programme after funding the platform, the evaluation kit and the catalogue (D). Total about ₪3.56M against the CFO's ₪3.02M, with the assistant kept (D).

**What it gives.** 5 in production through the approved route by September 2027, 10 by December, 14 by March 2028 (D); a catalogue by 31 May the board and the supervisor can rely on (D); the three numbers every quarter (M once running).

**What a "no" means.** The board's design: the queue stays at 1.5 a quarter, the shadow estate grows, and the first report to the board's risk committee has no inventory behind it.

**Cost of waiting.** Mishov renews for 24 months on 31 March unless notice by 30 January (₪528,000 committed) (M); Katvan AI by 15 March (M); Kesher's generative features arrive on by default in October (R).
