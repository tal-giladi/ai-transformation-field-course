# Module 04 — notes for the main session

## Needs a decision or an edit in shared files

1. **Templates in the inbox (12):** acceptable-use-policy, tools-and-data-classes, approved-restricted-use-list, data-boundary, vendor-ai-questionnaire, claim-read-back, vendor-poc-protocol, dpia-for-ai, risk-register, regulatory-map, governance-charter, ai-intake-register. Spreadsheet companions in `labs/module-04/`. Add them to `templates/README.md`. The lessons' 42 remaining checker problems are only links to these inbox templates.
2. **AI inventory template (M1) — suggested addition, not redrafted:** module 4 adds tier columns (`max_data_class`, `decides_about_people`, `acts_without_person`, `harm_if_wrong`, `reaches_outside`, `people_or_contacts_per_month`, `new_recipients`, `tier`, `tier_reason`, `override_by_date_reason`, `dpia`). If you want them in `templates/ai-inventory.md`, a one-line "Module 4 adds…" note under "How to fill it" would do; `labs/module-04/ai-inventory-tiering.csv` already has them.
3. **EU hotel customers are a persona-only fact.** Tal's brief says Harbor & Pine "has a few EU B2B hotel customers". Nothing in the data room shows it (all B2B ship-to cities in `orders.csv` are Israeli). Lesson 04.6 introduces it as something Yaniv Carmi (B2B) told the learner: three hotel groups headquartered in Cyprus and Greece buy for their hotels in Eilat and Tel Aviv; orders ship to Israel, invoiced in shekels; procurement managers email from Nicosia and Athens. If you want it discoverable, add a Yaniv persona line or a B2B customer list to the data room. (Eitan's persona says he covers "Israel and Cyprus" — consistent.)
4. **references/laws-and-guidance.md:** suggested updates at the end of `module-04-sources.md` (final DPO position statement July 2026, Directive 1/2024, the 2023 EEA regulations, the 2001 transfer regulations, Omnibus details, NIST revision, OWASP).

## Simulation vs data room (risk-register-tester, `harbor`)

04.5 tells learners the simulation simplifies and the data room wins, and names three differences. Suggest aligning the preset:

- `shadow` sample: "1,212 visits to chatgpt.com and gemini from 11 machines, 7 of them in Support". Data room proxy log (11–22 Oct): about 230 generative-AI chat requests (chatgpt.com 160 from Customer Service, 38 Marketing, 18 Purchasing; Gemini 9; Claude 5), 5 distinct Customer Service users; the 9-machine figure is the LinguaFlow extension. Suggested text: "Proxy log 11–22 Oct: 160 ChatGPT requests from Customer Service, LinguaFlow extension on 9 machines. Logged, not blocked."
- `retention` control and sample: "Data-retention note: support data deleted after 24 months; AI logs after 90 days … written in 2024". The data room's `policies/data-retention-note.md` is dated 22 Oct 2026 and says Deskly tickets are kept "Forever — no deletion rule set"; Deskly's add-on keeps AI content 24 months in analytics (§3.4). The risk's truth (amber, paper) still works if the control text becomes "The DPIA says AI content is deleted after 90 days" and the sample shows the add-on's 24-month analytics setting.
- `vendor`: "Data-processing agreement signed: no training … 30-day retention, EU hosting". Deskly's terms as received allow training unless opted out, 24-month analytics, US region. 04.5 frames the sim's row as the state after the opt-out and renegotiation (04.3). Fine as an assumption; consider adding to `notes`.
- `hiring` sample: "on since the 14 March 2026 update; 212 candidates". Release notes: published 10 March, rolled out 15–22 March. Suggest "since the March 2026 update"; 212 is an assumption (add to `notes`).
- `stale` test: "SOFA-118, discontinued in 2024". Data room SKUs look like `HP-SOF-1028`; discontinued example in the data is HP-DTB-1097 (Bergen table, 1 Aug 2025). Suggest using it.
- `claimsQA` test: claim id "C-2291" does not match the claims log format (`DC-26-001` … `DC-26-149`); suggest e.g. "DC-26-112".

## Cross-module inconsistencies

- **Eitan transcript weekday.** `personas/transcripts/eitan-chatnest.md` says "Thursday 20 November 2026"; 20 Nov 2026 is a Friday (Israeli weekend). 04.8 says "20 November" without a weekday. Suggest "Thursday 19 November".
- **Exchange rate.** The finance planning rate is ₪3.70/US$ (Oct 2026); the Bank of Israel representative rate on 2 Nov 2026 was ₪3.136/US$ (and ₪3.5168/€). Lessons 04.3 and 04.8 show both (planning rate for business cases, BoI for market figures); 04.2 uses BoI for the euro (the finance summary has no euro rate). `simulations/README.md` and `pilot-economics` use 3.6–3.7; worth a note somewhere that the company rate is deliberately conservative, or update the data room's rate.
- **Approval thresholds.** 04.2 corrects itself to the finance summary: up to ₪50,000 department head + CFO (not "management").
- **ChatNest three-year cost** ≈ ₪278,000 at ₪3.70 (₪85,000 + US$1,450 × 36), so a board decision; consistent with 03.5 (about ₪64,000 a year in platform fees + ₪85,000).
- **Dates used in module 4:** AUP approved 19 Nov, effective 22 Nov 2026; extensions removed and LinguaFlow forced sign-in by 30 Nov; Deskly opt-out sent 18 Nov; first review group 10 Dec 2026 (second Thursday); P-01 DPIA v0.3 26 Nov; risk-register testing 25–26 Nov. Modules 5–7 may want to reuse them.

## Facts I could not fully verify (also ⚠️ in the sources file)

- The Hebrew texts of Amendment 13, the Data Security Regulations (Regulation 15) and the transfer regulations: all statements rest on law-firm summaries (Chambers 2026, Barnea Jaffa Lande, Pearl Cohen, EBN). Lessons attribute them and route readings to counsel.
- The PPA's final DPO position statement (July 2026) and Directive 1/2024: known only through law-firm and Digital Policy Alert summaries.
- NIST AI 600-1's exact risk names: the final PDF could not be read; names match search summaries and module 02.
- The PPA AI guidance's status: no final version found (Chambers, March 2026, still says draft; the references list says the same). gov.il's PPA pages were not searched in Hebrew.

## Other

- Opening the NIST AI 600-1 PDF in the built-in browser triggered a file-save dialog on Tal's screen (no file was needed; it can be cancelled).
- `labs/module-04/tier_inventory.py` uses only the standard library; tested with Python 3.14.3: 14 rows → 3 High, 10 Medium, 1 Low.
- Persona used: Eitan (04.8). Avi optional in 04.3. No new personas or data-room files were needed.
