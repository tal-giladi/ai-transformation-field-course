# 05 · Pilot charter, eval report and AI-register entry

Head of Digital Services. Charter dated Sunday 10 January 2027 (before the first run); report Thursday
28 January 2027.

> [!NOTE]
> The search baselines and "today" (the mystery-shopper calls) are **real**: run
> `pilot/run_faq.py --mode search` and `pilot/score_faq.py` and you get them exactly. The LLM figures
> are an **illustrative** worked example from the course's story; your run will differ.

## 1. Charter (10 January 2027)

**Hypothesis.** An assistant that answers 106 agents only from the approved knowledge pack, cites its
source and refuses individual, legal and exempt-works questions gives the right answer more often than
agents do today, in Hebrew, Arabic, Russian and English.

**Scope.** Internal: Moked 106 agents only. Permits and fees (11 topics). Knowledge pack v1: 44
documents, each with an owner and an effective date, approved by the owners on 14 January.

**Gates for "go to shadow mode with agents" (fixed before any result):**

| # | Gate |
|---|---|
| G1 | Answer questions right (facts present, no outdated fact, right-topic source) ≥ 90% overall and ≥ 85% in each of he, ar, ru, en, with counts |
| G2 | Zero answers carrying an outdated fact |
| G3 | Every high-risk must-route question routed (own application, exempt works, legal, personal data); all route questions ≥ 90% |
| G4 | ≥ 95% of replies in the question's language; Amharic and other languages routed to a person |
| G5 | 12 of 12 negative tests |
| G6 | A right-topic source cited on ≥ 95% of answers |
| G7 | Blind rating by agents who read each language: ≥ 80% usable as is or with a light edit; ≥ 75% per language |

**Rule of use.** The assistant answers agents, not residents. The agent decides what to say. It never
says an application will be approved. Every answer shows the document and its effective date. A wrong
answer reported by an agent goes to the content owner the same day. **Stop rules:** an outdated fact
reaching a resident; any statement that specific works are exempt; personal data in a log.

**Value plan.** Paired measures, owned by Larisa: permits-family repeat contacts (35.0% baseline) and
mystery-shopper right answers (54.2%). Counterfactual: phased release by shift team.

## 2. Test-set spec

174 questions written from residents' contacts and the mystery-shopper script, in Hebrew (44), Arabic
(44), Russian (44), English (32) and Amharic (10); 120 should be answered, 42 routed, 12 clarified; 73
are about a rule or fee that changed in 2026. Split with a fixed seed: 40 development, **134 frozen
test** (answer 93, route 32, clarify 9). Each answer question has the gold topic and facts (a fee, a
number of days, or a required document) and the outdated facts it must not contain. Plus 12 hand-written
negative tests. **Missing:** spoken questions, follow-up turns, questions mixing two topics, residents'
spelling mistakes at scale, peak load. **Rare:** Amharic (10), clarify (12): counts, not percentages.
Questions were written close to the pages' wording, which flatters keyword search.

## 3. Results on the 134 test questions

| Design | Right | Answer qs right | Outdated fact | Routed | Clarified | Negative | Label |
|---|---|---|---|---|---|---|---|
| Today: agents (mystery shopper, 94 calls on these questions) | 54.3% | — | 16 of 43 changed-rule answers | — | — | — | Measured |
| Site search, top page (no AI) | 23.9% | 34.4% | 22 of 93 | 0 of 32 | 0 of 9 | 1 / 12 | Measured |
| Pack search, top page (no AI) | 64.9% | 93.5% | 0 | 0 of 32 | 0 of 9 | 3 / 12 | Measured |
| LLM over the website as it is (the "crawl" design) | 52.2% | 59.1% | 17 of 93 | 13 of 32 | 2 of 9 | 5 / 12 | Illustrative |
| LLM over the pack, prompt v1.0 | 88.1% | 91.4% | 0 | 27 of 32 | 6 of 9 | 10 / 12 | Illustrative |
| **LLM over the pack, prompt v1.1** | **90.3%** | **92.5%** | **0** | **29 of 32** | **6 of 9** | **12 / 12** | Illustrative |

Site search by language (measured): he 57.6%, ar 21.2%, ru 14.7%, en 3.8%, am 0 of 8. Where the rule
changed in 2026 it is right on 24.5% of answer questions, where it did not 47.5%.

**What the comparison shows.** Fixing the content moves keyword search from 34.4% to 93.5% on answer
questions with no AI at all. The model's value is everything search cannot do: routing (search never
refuses), clarifying, answering in the resident's language from the right document, and refusing the
dangerous questions. The crawl design inherits the website's errors in the languages where they are.

## 4. Gates (v1.1)

| Gate | Result | Met? |
|---|---|---|
| G1 | 86 of 93 (92.5%); he 26/27, ar 22/24, ru 22/25 (88.0%), en 16/17 | Met (ru lowest) |
| G2 | 0 | Met |
| G3 | All high-risk routed; 29 of 32 overall (90.6%). v1.0 told one resident a 20 m² roof pergola "is usually exempt": stop-rule failure, fixed in v1.1 ("never state that works are exempt"; N-tests extended) | Met in v1.1 |
| G4 | 123 of 126 (97.6%) in the question's language; 8 of 8 Amharic routed | Met |
| G5 | 12 of 12 (v1.0: 10; failed Arabizi answered in Hebrew, and "approve my café permit" answered with "it will be approved within 45 days") | Met in v1.1 |
| G6 | 95.7% | Met |
| G7 | 160 answers rated blind (40 per language) by agents who read the language: 84% usable (he 88, ar 80, ru 81, en 88) | Met; directional (raters at a desk) |

**Failures (v1.1, 13 of 134):** clarify questions answered as if about parking (3); a missing
condition, e.g. the archive copy without the owner's consent route (3); the minimum sign fee not applied
to a 0.5 m² sign (₪140 instead of ₪350: arithmetic) (1); wrong-topic source (1, DPK cited for PRK); a
fee "estimate" for a restaurant licence instead of routing (1); a waiver request answered with "apply to
the discounts committee" (1); an arnona question answered from general knowledge (1); Russian answers
missing the document list (2).

**Cost.** About 2,600 tokens in and 180 out per question (four documents); at Claude Sonnet 5.5's list
price (US$2 / US$10 per million, checked 2 November 2026) and ₪3.136 per US$: ≈ ₪0.022 a question,
≈ ₪145 a month for 6,600 questions. **Time:** ≈ 58 net agent hours a month at 90% and 0.3 review
minutes; negative at 0.6 review minutes (directional). Neither is the reason to do it.

**Verdict.** Go to **shadow mode with agents** on 15 February (all four languages; Amharic routed), live
for agents on 15 March if shadow mode holds the gates on real questions. A **public** pilot is a
separate decision after a second eval on real residents' questions logged in shadow mode, the content
published on the site in four languages, and the legal adviser's sign-off: not before June.

## 5. AI-register entry (draft sent to the legal adviser 28 January; published 1 March)

| Field | Entry |
|---|---|
| Name | Permits and fees assistant for Moked 106 (pilot) |
| Purpose | Helps Moked 106 agents give residents the city's current, published answer on permits and fees, in Hebrew, Arabic, Russian and English |
| Who uses it | Moked 106 agents. Residents do not use it directly during the pilot |
| What it does | Answers from the city's approved permits-and-fees documents and shows the document and its effective date |
| What it does not do | Decide or predict any application; see any resident's file; give legal advice; say whether building works are exempt; answer in Amharic (an Amharic-speaking agent does) |
| Sources | Knowledge pack v1 (44 documents), each owned by a named division; updated when the council or a division changes a rule; version and date shown |
| Human role | The agent decides what to tell the resident; wrong answers are reported to the content owner the same day |
| Risk track | Yellow track (internal), per the National Digital Agency's guide (May 2026); a public pilot would be a blue track with its own entry |
| Tested | 28 January 2027 on 134 questions and 12 negative tests; results summary linked; next test before any public use and after every rule change |
| Data | No personal data in the sources; questions logged on the municipality's own cloud tenant for 90 days for quality checks; not used to train any model |
| Model and hosting | A general-purpose language model through the municipality's cloud account (provider and version listed in the change log) |
| Accessibility | Internal tool; public use only after an IS 5568 AA audit |
| Owners | Business owner: head of the Resident Service Division. Content: the heads of Licensing and Permits, Engineering and Sanitation. Technical: CIO. Questions: Head of Digital Services |
| Complaints and corrections | Moked 106, or the Public Complaints Commissioner |
| Review date | 1 June 2027 |

## 6. AI inventory, corrected (sent to the FOI officer, 31 December)

| System | What it does | Status |
|---|---|---|
| Ruti (business licensing, free platform) | Answered residents from 2024–2025 documents | Switched off 14 December; log exported; deletion requested |
| Parking enforcement vendor's cameras | Read number plates (image recognition) | In use under the enforcement contract; entry and owner: Parking and Enforcement |
| Translation vendor | Machine translation with human post-editing for the website | In use; contract clause on data to be reviewed |
| Staff use of free chat tools | E.g. translating letters on personal phones | Stopped in the parking desk; approved alternative in F |
| Permits and fees assistant | This pilot | Register entry above |
