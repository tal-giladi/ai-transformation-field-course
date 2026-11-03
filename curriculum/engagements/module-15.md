# Crescent Bank — writer's notes for module 15 (never imported)

The seventh engagement and the first one about **scale, not a single use case**. The learner is the
newly appointed **head of the AI Centre of Excellence**, an outside hire reporting to the COO, in a
4,000-person bank with 14 business units, 40 AI pilots and nothing (officially) in production. The
hard part (15.4) is the operating model: central CoE vs federated vs hub-and-spoke, decision rights by
risk, a central review queue with limited slots, paved roads and model risk management under Bank of
Israel Proper Conduct of Banking Business Directive 369. The build-or-decide (15.5) is a portfolio
triage of the 40 pilots (Track B genuinely helps), the operating-model design and a 12-month scale
plan. The data room is `labs/module-15/data-room/` (built by `generate.py`, seed 20270103).

Binding: `simulations/operating-model-scaler/presets.js`, preset `crescent`. The 14 units, the 40
pilots (names, themes, risk tiers, the 10 weak ones, the two dependents of the assistant), the four
duplicate pairs, the money scale (₪11M a year central AI programme, ₪150,000 a review slot a quarter,
3 slots today, full validation of every model, central team ₪1.2M / hub ₪0.8M a quarter, platform
₪2.4M, templates ₪200,000, catalogue ₪150,000) and the expert answers (hub-and-spoke from the start,
decisions by risk tier, validation by tier, all three paved roads, adopt the shadow builds, merge the
complaints duplicate under Cards, answer the supervisor from the catalogue, a contractor for the
validation gap, cut across the board and keep the assistant, retrain the drifting model, route vendor
features by risk) are the preset's. Where the engagement differs from the simulation, see
"Differences from the simulation" below and `curriculum/inbox/module-15-notes.md`.

## The bank

- **Crescent Bank Ltd.** (בנק הסהר בע"מ), fictional. Founded 1972 as a regional bank in Haifa; head
  office in Ramat Gan since 2004; 58 branches (north and centre), about 1.1M customers, about 4,000
  staff, balance sheet about ₪96bn. Mid-sized, listed, supervised by the Bank of Israel's Banking
  Supervision Department. Customers and staff speak Hebrew, Arabic, Russian, English and Amharic.
- **14 business units** (the preset's): Retail Banking, Mortgages, Cards & Payments, SME Banking,
  Corporate Banking, Private Banking, Treasury & Markets, Credit Risk, Compliance & AML, Operations,
  Contact Centre, Digital Channels, HR, Finance.
- **Systems** (fictional names): core banking "Atid" (mainframe), CRM "Kesher 360" (a SaaS CRM, vendor
  release 27.1 in October 2027 enables generative features — the preset's Q3 2029 wave is earlier
  in the data room only as a roadmap line, not an event), data warehouse "Mizrah", the bank-wide
  assistant "Tzofen Assist" (fictional enterprise assistant, licensed per seat in ₪).
- **AI governance today:** AI policy v1 (June 2025): every AI use is a "model", goes to the Model
  Committee (chaired by the CRO) and needs full independent validation by Model Risk Management
  before any use with real data. The Model Risk Management unit is a head and **two validators**, who
  also carry about 140 traditional models and the Directive 369 phase-in for existing non-material
  models (21 February 2027). Three AI review slots a quarter are set aside in the 2027 work plan
  (one full validation = 2 slots, so 1.5 AI models a quarter).

## Who the learner is, and what changes

Head of the AI CoE (ראש מרכז המצוינות לבינה מלאכותית), hired from a fintech, started **Sunday 3
January 2027**. Reports to Dalit Ben-Ami, COO, who sponsored the CoE at the board. The board approved
(24 November 2026) a **central CoE** of 16 FTE and a ₪11.0M central AI programme for 2027; nobody but
the learner has been hired. Entry role (15.1, pointing to 01.1): an internal leader who is new, senior
on paper and powerless in practice: no line authority over the 14 unit heads, no right to stop a
pilot, a budget mostly committed to a design the board approved before they arrived, a CRO who owns
the gate, and a regulator watching. Differs from Kinneret (internal lead with history) and Northwind
(outside consultant): the learner will run whatever they design; their first move is to make the
design the board approved negotiable without saying the board was wrong.

## Stated ask vs hidden truth

- **Stated ask (CEO Avner Golan at the board, 24 Nov 2026, repeated by Dalit on day one):** "We have
  40 pilots and nothing in production." The board minute adds the CEO's promise: "at least ten in
  production by December 2027", and the remedy already chosen: a bigger central CoE "to industrialise
  the pilots".
- **Hidden truth.**
  1. **The bottleneck is decision rights, not delivery capacity.** One committee, full validation of
     every AI use regardless of risk, two validators who also own the Directive 369 phase-in for ~140
     traditional models. The AI queue gets 3 slots a quarter: 1.5 full validations. At that rate the
     40 pilots need 80 slot-quarters of work: about 27 quarters. A bigger central build team makes
     the queue longer, not shorter.
  2. **"Nothing in production" is false, and that is the real risk.** Because the gate is
     impassable, "pilot" became a status that never ends: the Branch FAQ assistant answers about 2,070
     questions a week in 31 branches (15 months "in pilot", on a sandbox whose contract says "no production use"), Contact Centre call summaries are pasted
     into the CRM notes of real customers, and Cards sends dispute letters drafted through a public
     LLM API paid on a corporate card (a shadow build). Digital writes marketing copy on personal
     subscriptions reimbursed as "software". None is in any inventory.
  3. **The 40 is not 40.** The register the CoE inherited has 43 rows: 3 are the same build counted
     twice under different names (and budgeted twice); 4 pairs are genuine duplicate builds in two
     units (complaints, credit memos, KYC documents, call summaries — and Retail has just asked for a
     fifth: branch call summaries); 10 would fail any proper review. About 26 builds are worth taking
     forward.
  4. **The CFO's cut would cut the wrong thing.** The 15% cut list (12 Jan 2027) leads with the
     bank-wide assistant (₪2.4M, the biggest single line) because "usage is 16%": December's weekly
     active users divided by the 1,600 seats activated on 1 December, not by the 380 onboarded users (66%) or the pilot teams (about 70%).
     Two later initiatives — the Operations procedure assistant and the Contact Centre knowledge
     assistant, both among the best-evidenced pilots — run inside the assistant (its agent studio,
     its retrieval index, its licences). The register's dependency column is blank for both.
  5. **The bank told its supervisor something that is not true.** In its 2026 answer to the Banking
     Supervision Department's AI-governance survey Crescent wrote that "a central inventory of AI
     applications with an owner for each" exists. It is the pilot list: no owners for some, joint
     owners for one, no shadow tools, no vendor-embedded AI.
  6. **The approved design recreates the problem.** A 16-FTE central CoE that builds and a single
     queue that decides is the simulation's "today" path: slow, a growing backlog, shadow builds.
- **The honest answer:** hub-and-spoke from Q2 2027 with **decision rights by risk tier** (low on the
  paved road decided in the unit; medium with hub standards and the evaluation kit, signed by the
  unit's model owner and checked by the hub; high to independent validation and the Model Committee),
  **validation by tier** (proportionality is in Directive 369 itself), three paved roads (platform,
  templates and evaluation kit, the catalogue — the catalogue first, because the supervisor will ask),
  **stop the 10 weak pilots, merge the 4 duplicate pairs** (complaints under Cards, credit memos under
  Corporate, KYC under Compliance & AML, call summaries under Contact Centre), clean the 3 double
  counts, bring the shadow builds in rather than shut them down, register the perma-pilots and put
  them through the route by tier, **keep the assistant** (staged: dependents' users first), cover the
  CFO's ₪3.02M from the triage and the switch to a hub, and a validation contractor for the 369
  backlog. CEO's "ten by December" restated as "14 in production by March 2028 through the new route,
  with the three numbers to the board every quarter".

## Planted findings (each discoverable, never stated)

| # | Finding | Where |
|---|---|---|
| 1 | Duplicate builds in two units: complaints (Retail, Cards) on two vendors; credit memos (SME, Corporate); KYC documents (SME, Compliance & AML); call summaries (Contact Centre, Digital) + Retail's new request | `ai/pilot-register-2026-12.csv` (descriptions, vendors), `ai/architecture-notes.md`, `ai/intake-requests-2026.csv`, `procurement/vendor-contracts-ai.csv` |
| 2 | Bank-wide assistant on the CFO's cut list while two later initiatives depend on it | `company/cfo-budget-review-2027-01-12.md`, `ai/assistant-usage-2026.csv`, `ai/architecture-notes.md`, register `depends_on` blank |
| 3 | Pilots counted twice under different names (3 rows), budgeted twice | register (`contract_id`, `environment`, `test_set_file`), `procurement/vendor-contracts-ai.csv` |
| 4 | A pilot with no owner (owner left in September); a pilot with joint owners (Directive 369 §24 forbids joint ownership) | register, `people/staff-directory-extract.csv` |
| 5 | Vendor contract auto-renewing: Retail's complaint vendor renews for 24 months on 31 March 2027 unless notice by 30 January | `procurement/vendor-contracts-ai.csv` |
| 6 | Model risk "team" of two validators; 369 phase-in backlog; 3 AI slots a quarter | `governance/mrm-workplan-2027.md`, `governance/model-inventory-2026-12.csv` |
| 7 | The review queue: 19 AI submissions, none approved, none declined, median wait 193 days, longest 437 (the Branch FAQ) | `governance/model-review-queue-2026-12.csv`, `governance/model-committee-minutes-2026.md` |
| 8 | Perma-pilots in real use: Branch FAQ (31 branches), call summaries into CRM notes, Cards dispute letters | `branches/branch-faq-usage-2026.csv`, register notes, `ai/architecture-notes.md`, proxy log |
| 9 | Shadow builds: Cards on a public LLM API paid by corporate card; Digital on personal subscriptions | `finance/card-and-expense-ai-2026.csv`, `security/proxy-ai-hosts-2026-q4.csv` |
| 10 | The 10 weak pilots (no test set, failed thresholds, bias features, wrong answers, no users, a rules engine labelled AI) | `ai/eval-summaries.csv`, register |
| 11 | Missing baselines: most pilots' benefits are claims | register `baseline_measured` |
| 12 | A step only on paper: the policy's monthly Model Committee and quarterly pilot review | `governance/ai-policy-v1-2025.md` vs minutes |
| 13 | The supervisor was told an inventory exists | `governance/bsd-ai-survey-response-2026-extract.md` |
| 14 | The "16% usage" denominator | `ai/assistant-usage-2026.csv` vs CFO memo |
| 15 | Where the AI people already sit (spokes exist in 6 units; most contractors) | `people/ai-people-by-unit.csv` |
| 16 | Branch staff use personal phones for customer letters in Arabic and Russian | Olga persona only (not in any log) |

## The cast (persona pack)

| Persona | Role | Type | Hidden / unlock |
|---|---|---|---|
| Avner Golan | CEO | CEO, owner of the ask | Promised the board "ten by December"; the chair asked him privately why the supervisor's survey answer was "so confident"; he would accept "fewer, real" if he can show the board a number every quarter. Unlock: what exactly he told the board, and what the chair asked |
| Dalit Ben-Ami | COO, sponsor, your manager | Sponsor | Wrote the central-CoE design herself with a consultancy in October; doubts it; the assistant is hers (Operations reports to her) and she has not defended it to the CFO. Unlock: who designed the CoE; what she would change if it were not her paper |
| Dr. Irina Kogan | CRO, chairs the Model Committee | CRO / model-risk head | Two validators, 61 traditional models not yet compliant with the 21 Feb 2027 phase-in; would accept tiering if the policy, not she, says so; knows the head of validation has an offer from a fintech. Unlock: show her the queue arithmetic; ask about people risk in her unit |
| Nir Ashkenazi | CIO | CIO / IT | Has an unused ₪1.1M "AI landing zone" in IT capex; knows the call summaries are pasted into Kesher notes via a macro; the assistant's tenant hosts the two dependents. Unlock: ask what runs on the assistant tenant; ask about the landing zone |
| Hagit Mor | Head of Retail Banking | Unit head with a duplicate build | Her complaint-summary vendor auto-renews unless notice by 30 Jan; her build has no test set; asked for branch call summaries too. Unlock: ask when the contract renews; ask to see her eval |
| Karim Haddad | Head of Cards & Payments | Unit head who shadow-built | Dispute letters via a public LLM API on a team lead's corporate card since April 2026, ~1,400 letters a month; customer names and card numbers' last four in prompts; his complaint build is the better one. Unlock: promise of a route in, not a punishment; ask how dispute letters are written today |
| Tsega Alemu | Chief Internal Auditor | Internal audit | 2027 plan has an audit of 369 compliance in Q2 that will include AI; she will report perma-pilots as "models in use without validation". Unlock: ask what her 2027 plan covers; ask how she would count a pilot in daily use |
| Adv. Lina Nassar | Chief Compliance Officer and head of regulatory liaison | Compliance / regulator-facing | Wrote the survey answer from the pilot list; expects a supervisory follow-up on AI governance in 2027; would rather correct the record proactively. Unlock: ask what the bank told the supervisor and on what basis |
| Olga Petrenko | Branch manager, Haifa Hadar | Frontline | The Branch FAQ is used every day for fee and procedure questions; staff draft letters in Arabic and Russian on personal phones with a public chatbot; one wrong fee answer in November. Unlock: no names, and ask how a real customer question is answered at the desk |

Transcripts leave hidden: Avner's chair conversation; Dalit's authorship of the design; Irina's people
risk (the resignation offer); Nir's landing zone; Hagit's auto-renewal; Karim's customer data in
prompts; Tsega's Q2 audit; Lina's willingness to correct the record; Olga's personal phones.

## Timeline

- Data: pilot register as of 31 Dec 2026; assistant usage May–Dec 2026; Branch FAQ usage Oct–Dec
  2026; proxy Q4 2026; card and expenses 2026; committee minutes 2026.
- 24 Nov 2026 board approves the central CoE and ₪11.0M; Sun 3 Jan 2027 you start (15.1); 4–21 Jan
  discovery (15.2); Tue 12 Jan CFO's cut list; **Sat 30 Jan notice deadline for Retail's vendor**;
  Thu 4 Feb diagnosis to Dalit and Avner (15.3); Thu 18 Feb Model Committee — operating-model design
  (15.4); **Sun 21 Feb Directive 369 phase-in for existing non-material models** (from the circular);
  1–10 Mar triage and scale plan (15.5); **Mon 15 Mar 2027 management committee** decides (15.6);
  Tue 30 Mar board (budget revision with the 15% cut). The 12-month plan runs April 2027 – March 2028.
- Twelve months later: March 2028.

## The futures (15.6 debrief)

1. **A bigger centre.** The board's design goes ahead: 16 FTE hired, Model Committee doubled to 6
   slots, full validation kept, the CFO cuts the assistant. By March 2028: 5 in production (the
   simulation's "central with more slots", 4 quarters), a backlog of 7 and growing, Cards' shadow tool
   still running, two more found; the procedure and knowledge assistants stalled; ₪8.9M spent. In Q1
   2028 the supervisor asks for the model inventory and validation evidence; the bank sends the
   procurement vendor list.
2. **Let the units run.** Avner, frustrated in June, gives unit heads go-live rights with a light check.
   By March 2028 nearly all 40 are live in some form, including the 10 weak ones; four duplicate pairs
   on six vendors; five incidents (the chatbot quoting a cancelled fee, CV screening ranking applicants
   from two towns lower, a valuation check approving a stale valuation…); internal audit's Q2 report
   lists 23 models in use without validation. Fast, duplicated and risky (simulation: federated).
3. **Hub-and-spoke, decided by risk (the expert path).** Hub of 10 under the head of the CoE; spokes
   in six units; the policy rewritten with three tiers; catalogue live in May; platform (on the CIO's
   landing zone) in September; 10 stopped, 4 merged, 3 double counts cleaned, shadow builds registered
   and moved; assistant kept and staged; a validation contractor for six months; the record corrected
   with the supervisor by the CCO in April. By March 2028: **17 in production** (the plan committed 14),
   backlog 7 high-risk items with dates, median decision time 41 days, 0 shadow tools known, 1 minor
   incident, central programme spend ₪10.2M against a plan of ₪10.0M (the validation contractor extended by three months, approved).
   The simulation's expert run reaches 26 by the end of 2027 because it has no procurement, DPIA or
   works-council time; the lesson says so.

What decided it: whether decision rights followed risk instead of status, and whether the catalogue
(not the build team) came first.

## Differences from the simulation (also in the notes inbox)

- The sim fires its events over 2027–2029; the engagement finds the shadow builds, the complaints
  duplicate and the budget cut in January 2027 (the cut list is the 2027 budget review, not Q3 2028).
- The sim's money is the central programme only (no licences, no unit pilot budgets); the engagement
  adds the unit AI lines (about ₪7.3M) so the CFO's cut and the triage savings can be seen.
- The sim's expert reaches 26 in production after four quarters; the engagement's plan commits to 14
  by March 2028 and future 3 shows 17.
- The sim has three validators leaving in Q2 2028; the engagement's unit is a head and two validators,
  and the head's fintech offer is a hidden fact in Irina's persona (the people risk is visible now).

## Where each finding is planted (actual numbers)

Computed from the generated files (seed 20270103) with `labs/module-15/discovery.py` and `triage.py`;
reproducible in a spreadsheet with filters, pivots and lookups. Paths relative to
`labs/module-15/data-room/`.

**Register (`ai/pilot-register-2026-12.csv`).** 43 rows; stages Pilot 34, POC 6, Pilot (extended) 1,
On hold 1, Rollout 1; baseline measured Y 22, N 16, Partial 5; test set named on 37; `depends_on`
filled on 0. 19 rows have run 12+ months. Unit AI lines 2027: ₪9,130,000 (OPS-01 assistant
₪2,400,000).

1. **Duplicates (4 pairs).** Same task family in two units, kept build chosen by evidence: complaint
   summaries RET-01 (Mishov, no test set, vendor's 90%) → CRD-01 (Bahir, 0.91 on 300, threshold
   0.85); credit memo SME-01 (contractor, no test set) → CORP-01 (0.97 on 120 after covenant fix);
   KYC SME-02 (0.89 on 90) → CMP-01 (0.96 on 250, licence covers business customers); conversation
   summaries DIG-02 (spot check 50, no threshold) → CC-01 (0.89 on 200; Arabic 0.81). Retail's REQ
   "סיכום שיחות בסניפים" is a fifth. Second builds' 2027 lines: ₪760,000.
2. **Assistant.** CFO memo: ₪2.4M, "16% of seats (251 of 1,600)". December: 250 weekly active / 1,600
   seats = 16%, / 380 onboarded = 66%. Oct–Nov pilot seats: Operations 89.4 of 120 (0.74), Contact
   Centre 75.0 of 110 (0.68), HQ groups 0.2–0.35. Agent-studio sessions ≈ 808 (Ops) and 722 (CC) a
   week. Architecture notes: OPS-02 and CC-02 run in the Tzofen agent studio with indexes in the
   tenant; deleted 30 days after the subscription ends.
3. **Double counts (3).** Same environment + same test set: MTG-01/OPS-04 (`docai-mtg-sbx`,
   `mtg_docs_gold_400.csv`), TRS-01/PRV-03 (`trs-llm-sbx`, `mkt_summ_test_60.csv`), FIN-02/OPS-05
   (`matchpoint-fin`, `invoice_match_test_500.csv`); identical eval rows. Double-booked ₪420,000.
4. **Owner.** PRV-02 owner Ariel Mizrahi, left 2026-09-15 (directory). CC-01 owner "Revital Cohen /
   Tom Erez".
5. **Auto-renewal.** PR-2025-117 Mishov: ends 31 Mar 2027, 24-month auto-renewal, 60 days' notice →
   30 Jan 2027, ₪264,000 a year. Also: Katvan AI (MTG-04 and PRV-01, both stops) notice by 15 Mar;
   Kesher CRM notice by 2 Mar with generative features on by default in release 27.1 (Oct 2027);
   Kishron Rank (HR-01) already renewed on 15 Dec 2026 without a DPA.
6. **MRM.** Head + 2 validators; 12 slots a quarter (6 phase-in, 3 annual, 3 AI); 142 models in the
   inventory (63 material, all compliant; 79 other: 18 compliant, 13 in progress, 48 not started =
   61 not compliant before 21 Feb 2027); 0 generative AI entries.
7. **Queue.** 19 submissions: waiting 15, in validation 2 (CRK-01, OPS-01), returned 2 (DIG-01,
   HR-01). Wait median 193 days, longest 437 (RET-03). Minutes: 5 meetings, approved 0, declined 0.
8. **In real use.** Branch FAQ: 31 branches, median 2,072 questions a week (Oct–Dec), thumbs-down 4.9%
   (9.0% in the fee weeks 8–26 Nov). CC-01 macro into Kesher since August. DIG-01 A/B on 2% since 3
   Nov (Committee: "returned"). DIG-03 A/B on 10% (shows public pages only; low tier).
9. **Shadow.** LLMHUB *API USAGE on Elad Ben-Shimon's card: 9 lines Apr–Dec, ₪13,741; proxy CRD –
   Disputes → api.llmhub.io "allowed (uncategorised)": 4,492 requests, 126,950 KB uploaded in Q4.
   AIWRITERPRO MONTHLY expense claims: N. Avraham and S. Gold 10 each (₪798), L. Haddad 7 (₪548);
   proxy DIG – Marketing → app.aiwriterpro.com 2,874 requests. Also CC – Floor →
   translate.freetrans.net 2,342 requests (free translator), branch/DIG/TRS attempts to chat.llmhub.io
   blocked (924 / 390 / 205).
10. **Weak (10).** RET-02 (open compliance question on purpose of use; uplift not run), MTG-02
    (false-accept 0.18 vs 0.05; 2023 price index), MTG-04 (0 users since August, no test set), CRD-04
    (a rules engine already does it), PRV-01 (2 users, no test set), PRV-02 (0.14 factual errors vs
    0.02; owner left), CMP-02 (false negatives 0.09 vs 0.01; 11 true positives auto-closed), CC-03
    (routing 0.61 vs 0.85), DIG-01 (0.76 vs 0.90; Arabic answered in Hebrew; live on 2%), HR-01
    (selection-rate ratio by home town 0.62 vs 0.80; features incl. home town and graduation year).
    Their 2027 lines: ₪1,560,000.
11. **Baselines.** 16 N, 5 Partial.
12. **On paper only.** Policy §5 monthly committee and quarterly pilot review vs 5 meetings; §4
    register within 5 days vs no row for the shadow tools; §6 "public services blocked" vs the
    uncategorised API.
13. **Survey.** 3.1 "lists every AI application with its business owner" vs the register; 3.4 "no AI
    application is in production with customers" vs DIG-01 A/B and CRD letters; 4.2 "blocked" vs the
    proxy.
14. **Denominator.** See 2.
15. **People.** 46 rows: AI work in Cards (5), Digital (6), Treasury (3), Credit Risk (4), Contact
    Centre (3), Operations (3), IT Data & Analytics (8, of whom 2 contractors) — the spokes exist in
    six units and the central data-science team is already in IT. MRM 3.

**Triage result (`triage.py`, the expert's).** 40 builds; tiers of the 40: low 15, medium 14, high 11
(identical to the preset). Actions: stop 10, merge 4, clean 3, route 24, fix then route 2 (TRS-01:
no baseline; CC-01: two owners). Kept 26: low 12 (RET-03, MTG-03, CRD-03, CORP-02, TRS-01, OPS-01,
OPS-02, CC-02, DIG-03, HR-02, FIN-01, FIN-02), medium 8 (RET-04, MTG-01, CRD-01, CRK-02, CMP-01,
OPS-03, CC-01, FIN-03), high 6 (CRD-02, SME-03, CORP-01, TRS-02, TRS-03, CRK-01). Patterns among
the 26: Q&A over documents 5 (RET-03, MTG-03, OPS-02, CC-02, HR-02), drafting 5, extraction and
matching 5, scoring and ranking 7, summarisation 3, search 1.

**Review load (slots; 3 AI slots a quarter).** Today 40 × 2 = 80 → 26.7 quarters; triaged full 52 →
17.3; triaged by-tier validation 26 → 8.7; rights by tier (only 6 high to the queue, 12 slots) with
templates (×1.5) → 2.7 quarters.

**Money (2027).** All AI spend ₪20.13M (central ₪11.0M + units ₪9.13M); 15% = ₪3.02M. Expert:
releases stop ₪1.56M + merges ₪0.76M (merge work ₪0.18M) + double-booking ₪0.42M = ₪2.56M net from
the units; central programme re-cut to hub ₪10.0M (hub team 3.2, validation 1.8, contractor 0.35,
platform 2.4 + run 0.6, templates and eval kit 0.32, catalogue 0.225, reorganisation 0.3, run of
go-lives 0.5, training 0.3 = 9.995) saving ₪1.0M. Total ₪3.56M ≥ ₪3.02M with the assistant kept.
(The CIO's ₪1.1M landing zone shortens the platform's lead time; its money is not counted.)

**Simulation (node, `presets.js` crescent).** Expert after 4 quarters: 26 in production, 6 stopped,
4 merged, backlog 7, 0 incidents, 0 shadow, ₪10.38M; after 12: 36, 2 incidents, ₪29.78M. Today's
set-up after 4: 2 in production, backlog 13, 2 shadow; after 12: 7, backlog 29, wait 5.3 quarters,
23 shadow, ₪21.39M. Central with 6 slots after 4: 5 in production; after 12: 18, 19 shadow.
Federated after 4: 40 live, 10 weak live, 4 duplicates, 5 incidents; after 12: 23 incidents. Expert
with the assistant cut: 2 stalled, 33 in production after 12.
