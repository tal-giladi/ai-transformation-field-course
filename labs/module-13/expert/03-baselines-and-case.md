# 03 · Baselines, opportunity map and the one-page case

For Dalia Mizrahi and Orit Navon, Thursday 11 February 2027. Labels: **M** measured, **D** directional, **A** assumed. Money: CFO's figures (labelled), ₪3.136 per US$.

## Baseline sheet

| Measure | Definition | 2026 value | Label | Owner from April |
|---|---|---|---|---|
| Unplanned downtime | ProdTrack stops, all reasons except PM, SETUP, NO_ORDER; stop to restart | 11,932 h (moulds 5,479; machine 2,840; waiting 1,538; material 1,051; other 1,024) | M (split by reason: D) | Dalia (K), Eli (G) |
| Night mould stops | MOULD stops starting 22:45–06:45 | 229 stops, 3,255 h, mean 14.2 h (day 4.0 h) | M | Fadi Khoury |
| MTTR, one definition | Stop to production restart (ProdTrack), both plants | Plant K 5.7 h, Plant G 5.8 h | M | Operations excellence |
| PM done | PM work orders closed **with labour recorded** ÷ scheduled | 92.4% (reported 96.7%) | M | Vladimir Kaplan |
| Breakdown WOs with a failure mode | Code not blank, not 99 | 14.2% Plant K; 0 Plant G | M | Vladimir Kaplan, Shlomi Biton |
| Night calls to the maintenance manager | Supervisors' log | 78 (Mar–Dec), median 42 min machine waiting | M | Tigist Wondimu |
| Parts list accuracy | Drive list rows whose number is active and bin matches the ERP | 0 of 268 | M | Avi Malka |
| Arava OTIF | Arava's measure | 81% | M (customer) | Danny Golan |

**What an hour costs (CFO, D):** ₪310 lost contribution on a fully loaded job (about 40% of hours); the rest is recovered with overtime, which I value at ₪95 per machine-hour (A, to confirm with Orit). Blended: about **₪181 per unplanned hour** (D). Freed technician hours are capacity, not cash.

## Opportunity map and screen

| # | Candidate | AI? | Addresses | Best-case effect (D) | 2027 cost | Data gate | Verdict |
|---|---|---|---|---|---|---|---|
| A | Predictiva platform on 40 machines | Yes (ML) | Machine faults, 24% | Vendor's 50% of 2,840 h = 1,420 h ≈ ₪257k a year, from 2028 at the earliest | ₪1.03M over 3 years (₪343k a year) + labelling we cannot do | **Fails**: 8.5% usable labels, no mode with 30 events, 3 machines with sensors | **Not yet** |
| B | Night mould response: toolmaker on call, first-response training on hot runners and water, spare kits, a written "cavity closed" rule with QA, shot counters on 60 hot-runner moulds | No | Moulds at night | Night mean 14.2 → 8 h: about 1,420 h ≈ ₪257k a year | ₪130k | Passes (ProdTrack) | **Do now** (Arava plan) |
| C | Restore the six machines' PMs; PM measured with labour | No | Machine faults on six machines | Q4 excess ≈ 28 stops a quarter, about 400 h a year ≈ ₪72k | Within budget | Passes | **Do now** |
| D | Parts: live ERP view on maintenance tablets, delete the drive copy, bin labels, critical spares | No | Waiting for parts | Small in hours (32 WOs, night calls); removes a wrong source | ₪40k | Passes | **Do now** |
| E | Maintenance-manual assistant for technicians (four languages, cites the source, refuses unsafe steps) | Yes (GenAI) | Night knowledge, safety | 64 h a year of machine waiting (small); the value is correct, safe answers and less dependence on one person | ₪45k | Passes after curation | **Pilot** |
| F | Common asset register (incl. moulds, crosswalk) + failure and outcome recording at the machine, four languages, a short failure-mode list | No (LLM optional for back-coding) | Everything later | Enabler; no direct hours | ₪305k | — | **Foundation** |
| G | Threshold alarms on K21–K23 now; sensors and historian on the 8 machines with most machine-fault hours (32% of them) | No | Machine faults on 8 machines | Directional; and the data a 2028 decision needs | ₪140k | — | **Foundation** |
| H | Early warning from quality's scrap codes | Later, maybe ML | Process drift | Unknown | Analysis only | Partly | **2028, with A** |
| I | QA cover for first-article approval at night | No | Arava quality | Arava's two October complaints | Rotem's call | — | **Route to Rotem** |

## One-page case (as sent)

**Decision asked on 23 March:** release ₪730,000 of line 7400-210 in three stages for the maintenance foundation, the Arava actions and a manual-assistant pilot; do not sign with Predictiva in 2027; re-decide predictive maintenance in January 2028.

**Why not predictive maintenance now:** it would watch the quarter of our downtime that is machine faults, on data we do not record; even at the vendor's own best figure it returns about ₪257k a year against ₪343k a year of cost, and not before 2028.

**What the ₪730k buys:** B ₪130k, D ₪40k, E ₪45k, F ₪305k (register ₪45k, recording ₪260k), G ₪140k, contingency ₪70k. C is within the maintenance budget.

**Payback (D):** B + C ≈ ₪329k a year against ₪130k: under 6 months. The foundation (F, G) and the safety items (translations, crane) are infrastructure and compliance: no payback claimed; they are the condition for any AI decision in 2028.

**Stages and stop rule:** Stage 1 (to 30 April): register, protocol with the works committee, recording live at Plant K, B and D running — ₪260k. Stage 2 (to 30 June): Plant G on MaintPro, sensors on 8 machines, assistant pilot evaluated — ₪330k. Stage 3 (to 31 December): ₪140k. **Stop rule:** if fewer than half of breakdown work orders carry a failure mode by 30 June, stop stage 2 spending on recording and review with the works committee.

**Arava (D):** B, C and I target the causes behind the late and short-shot shipments; target OTIF 92% in Q3 2027, 95% in Q4.
