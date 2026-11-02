# Module 11 — notes for the main session

Written 2026-11-02 by the module 11 agent. Nothing committed. `node curriculum/tools/check-module.mjs 11` → 0 problems. Generator run twice: identical hashes for every data and pilot file. Data room 1.4 MB, lab folder under 3 MB.

## For the sidebar (lesson titles = H1s)

- **Module 11 — Givat Oren municipality** (suggested)
  - 11.1 · The call
  - 11.2 · Discovery
  - 11.3 · Diagnosis
  - 11.4 · The hard part
  - 11.5 · Build: a permit-FAQ assistant, evaluated
  - 11.6 · Readout and debrief
  - Module quiz: `assessments/module-11-quiz.md`. Project: `projects/m11-givat-oren.md`.

## Templates

No new template drafts. Every link goes to an existing file in `templates/`.

**Suggestion (Tal decides):** an `ai-register-entry` template (public, plain-language record of an AI system a public body uses). Lesson 11.5 gives the fields inline and `labs/module-11/expert/05-…` has a filled example; it would also serve modules 15 (bank) and 16 (nonprofit transparency). It is not in the build-spec's template table, so I did not draft it.

## Simulation presets

Linked only existing generic presets: `pilot-economics?preset=generic` (11.3, 11.5) and `vendor-rfp?preset=generic` (11.4). No Givat Oren preset exists. Proposed `givatoren` presets, numbers from `curriculum/engagements/module-11.md`:

1. **pilot-economics `givatoren`** (11.3, 11.5): volume 6,600 permits-family contacts a month; automationRate 0.7; accuracy 0.9; minutesSaved 1.5; reviewMinutes 0.3; reworkMinutes 3.0; hourlyCost 130; tokensIn 2,600, tokensOut 180; priceIn 2, priceOut 10 (Sonnet 5.5 list); fx 3.136; fixedMonthly 6,000; buildCost 120,000. Per `fieldkit.cost`: 57.8 net hours, ₪1,406 a month, breakeven 85 months; negative at 0.6 review minutes or 80% accuracy. Lesson point: the assistant's value is not hours.
2. **steering-committee `givatoren`** (11.6): chair the director-general (Ronit), the chief of staff (Eyal, the sponsor-as-advocate branch: "launch for the conference"), legal adviser (Samer), head of 106 (Larisa), CIO (Dmitri), works committee chair (Moshe, for the 106 item), treasurer; outcomes map to the three futures.
3. **vendor-rfp `givatoren`** (11.4): CivicTalk and two or three fictional competitors; demo conditions reveal = benchmark of 200 Hebrew questions written and scored by the vendor; "30 authorities" = all products; crawl incl. old pages; machine translation for Arabic; PoC on the city's 134 questions.
4. **discovery-interview `givatoren`** (11.2) and **readiness-evidence-grader `givatoren`** would fit: the Q3 report vs the exports vs the mystery shopper is a natural verified/reported/contradicted set.

## Facts not verified / to check before publishing

- Tender amounts: only the October 2021 figures from the Wikisource text (₪145,500 / ₪710,600). Current indexed amounts not found; the lessons tell learners to ask the treasurer ⚠️.
- Laws read on Hebrew Wikisource, not the official consolidated texts (Municipalities Ordinance, Tenders Regulations, FOI Law, Decisions and Reasons Law, Accessibility Regulations, Basic Law, Public Complaints Commissioner Law) ⚠️. The Decisions and Reasons Law fetch mentioned "three months" in s.6(b) next to 45 days in s.2: lessons cite only ss.2, 2A, 6(a) ⚠️.
- IS 5568 Part 1: current edition and WCAG basis (2.0 per Kol Zchut) not confirmed on the SII site ⚠️.
- The National Digital Agency guide (May 2026): read in the English informal translation; the Hebrew prevails and was not opened ⚠️. No statement found that it applies to local authorities; lessons say "written for public-sector entities; as far as this course found, does not bind a municipality".
- Duty to consult the works committee: sourced to a 2015 law-firm update on case law (not municipality-specific) plus the fictional 2019 local agreement ⚠️.
- Next municipal elections "2028" (city profile, brief, 11.6) is from general knowledge (five-year cycle after the February 2024 elections), not opened ⚠️.
- Reg. 3(15) and the real local-authorities' economic company: lessons describe 3(15) from the regulation text and use a fictional purchasing company in the data room; the real company is not named ⚠️.
- Arabic, Russian and Amharic text (knowledge pack, test questions, Ruti log) was written by the agent: a native-speaker read is worth doing, especially the Amharic (10 questions, 1 negative test) and the Arabizi negative test.
- The parking-permit fees, procedures and other municipal rules are fictional (Givat Oren's own); the lessons and INDEX say so. Real fees for business licences, dogs etc. were avoided.

## Design decisions worth knowing

- **Entry role:** the accidental owner (Head of Digital Services, an employee): mandate from the director-general, not the mayor's office; no budget; no authority over content; no exit date. Dates: 26 Nov 2026 – 4 Feb 2027 (management forum 2 Feb), overlapping module 10's 15 Nov – 21 Jan; different organizations, no conflict.
- **The eval:** 174 test questions (he 44, ar 44, ru 44, en 32, am 10), behaviour labels answer/route/clarify, gold facts and stale facts; 40 dev / 134 test. Four designs: site search and pack search (no AI; real, reproducible), LLM over the site and LLM over the pack (illustrative, labelled, following modules 5 and 8). "Today" is the quality unit's mystery-shopper calls joined to the test questions (real). Headline: pack search 93.5% on answer questions vs site search 34.4% — the content fix carries the accuracy, the model earns its place by routing and clarifying. Questions are written close to page wording, which flatters keyword search; the lessons say so.
- The LLM pipeline was proven with `FIELDKIT_PROVIDER=mock` and the mock run deleted.
- Transcripts end without annotations; what each interviewer missed is in the lessons' reference answers (as in module 8).
- `curriculum/engagements/module-12.md` exists in the tree; not mine, not touched.

## Cross-module notes

- Module 8's Air Canada material is linked (08.4) rather than re-cited; MyCity is the public case here, verified against The Markup (2024 and 2026).
- The National Digital Agency guide (May 2026) is new since `references/laws-and-guidance.md` was written; modules 9, 15 and 17 may want it too.
