# Module 08 — notes for the main session

Written 2026-11-02 by the module 8 agent. Nothing committed. `node curriculum/tools/check-module.mjs 08` → 0 problems.

## For the sidebar (lesson titles = H1s)

- **Module 8 — Northwind Outfitters** (suggested; the plan has no module title)
  - 08.1 · The call
  - 08.2 · Discovery
  - 08.3 · Diagnosis
  - 08.4 · The hard part
  - 08.5 · Build: agent-assist on 2,000 tickets
  - 08.6 · Readout and debrief
  - Module quiz: `assessments/module-08-quiz.md`. Project: `projects/m08-northwind-outfitters.md`.

## Templates

No new templates. Every link goes to an existing file in `templates/`.

## Simulation presets proposed (none linked except the generic one)

Only `pilot-economics?preset=generic` is linked (08.5), with the instruction to type Northwind's inputs. Proposed `northwind` presets, numbers from `curriculum/engagements/module-08.md`:

1. **pilot-economics `northwind`** (08.5): volume 22,000 written tickets a month; automationRate 0.6; accuracy 0.8; minutesSaved 4.0; reviewMinutes 1.0; reworkMinutes 3.0; hourlyCost 88 (₪13,800 / 157 h); tokensIn 2,800, tokensOut 450 (two calls); priceIn 2, priceOut 10 (Sonnet 5.5 list); fx 3.136; fixedMonthly 12,000; buildCost 150,000. Result per `fieldkit.cost`: 352 net hours, ₪18,558 a month, breakeven 8.1 months; breakeven accuracy 67%; loses money at 2.0 review minutes.
2. **steering-committee `northwind`** (08.6): cast Gil (CEO, chair, weight 2, starts mood 2), Orly (sponsor, 1.5), Boris (CFO, 2), Meseret, Hila (counsel), Alexei; the sponsor-as-advocate branch fits Orly asking to "keep the bot for returns as a trial"; outcomes map to the three futures in the writer's notes.
3. **roi-defender `northwind`** (08.3): claims "half of support by Q2" (₪2.0M annualised to date), "AHT −30%", "containment 63%", "29 agents" (vendor), the consultant's "6,800 contacts avoided", "352 hours from agent-assist", "breakage not affected"; four ledgers as in 08.3.
4. **oversight-under-load `northwind`** (08.5): drafts per day ≈ 600 (13,200 a month / 22 days), 26 agents on the floor, wrong-decision rate 4.2% (hybrid, illustrative), check 1.1 min with source shown.
5. **discovery-interview `northwind`** (08.2) and **readiness-evidence-grader `northwind`** would also fit (KPI report vs export vs vendor dashboard is a natural verified/reported/contradicted set).

## Facts not verified / to check before publishing

- Moffatt v. Air Canada: the CRT decision and CanLII returned 403; facts and the CA$650.88 award are from Manatt and CTV ⚠️. Module 7's sources cite McCarthy Tétrault for the same case: consistent.
- Consumer Protection Law sections were read on Hebrew Wikisource, not the official consolidated text ⚠️. English section letters used: 14C (14ג), 14C1 (14ג1), 14E (14ה), 31A (31א).
- The "made to order" exception is stated via Kol Zchut without the exact provision; `pilot/policy-for-pilot.md` says "counsel to cite the exact provision".
- Whether opening the packaging limits cancellation is left to counsel in every text (sources conflict; one search result mentions a regulation 3 rule I could not open).
- Amharic, Arabic (including Arabizi) and Russian customer messages and agent replies in `data-room/textbank.py` and `pilot/negative-tests.csv` were written by the agent: a native-speaker read is worth doing, especially the Amharic (≈ 30 sentences, 12 tickets).
- Intercom and Zendesk prices are named as market reference points in 08.4 (checked 2 Nov 2026); Verbalo is fictional.

## Design decisions worth knowing

- The extract is a **1% customer sample** (× 100). Company: ≈ 60,000 orders a month, ₪548M revenue, 42 → 30 agents (Jun → Sep), 2025 support cost ₪8.95M, 2027 draft ₪6.09M with 21 agents from April. I first planned 2% and 58 → 41 agents but the per-agent load was unrealistically low; everything was regenerated and every file aligned.
- `data-room/generate.py` also writes `pilot/labels-2000.csv` (the labelling team's labels); the pilot split is in `pilot/sets.py` (seed 20261218). Determinism checked: two runs, identical hashes for all data files.
- The hidden truth involves the client's returns practice conflicting with its own terms of sale and, per counsel, possibly the Consumer Protection Law. Every lesson attributes legal readings to counsel and says "not legal advice". Fictional company; no real retailer portrayed.
- The LLM and hybrid evaluation numbers in 08.5 and `expert/05` are an illustrative worked example (no API key in the build), labelled as such, following module 5's precedent. Rules baseline, "today" and negative-test baseline numbers are real.
- Persona "Verbalo Assist US$39 per agent per month" is a fictional vendor price.
- `labs/module-08/discovery.py` imports numpy (installed with pandas; no new pin needed).

## Cross-module notes

- Harbor & Pine's `references/laws-and-guidance.md` has no Consumer Protection Law entry; suggested additions are at the end of `module-08-sources.md`. Modules 11 (municipality) and 14 (SaaS agent) may reuse the chatbot-liability material and the Air Canada sources.
- The plan's planted finding "a report definition changed near rollout" is in both 08.2 (AHT) and the Q3 report's contact definition; module 9's "three conflicting baselines" will feel similar: worth making module 9's mechanism different (systems, not definitions).
