# 03 · Baselines, opportunity map and the one-page case

For the management forum, Thursday 17 December 2026 (15 minutes). Head of Digital Services.

## Baseline sheet

| Measure | Definition | Value | Label | Owner of the measure from now |
|---|---|---|---|---|
| Permits-family contacts | Contacts with topic in the permits family, 4% caller sample × 25 | ≈ 6,600 a month (33.8% of ≈ 19,570) | Measured | Larisa Gurevich |
| Repeat contacts, permits family | Same caller, same topic, within 14 days | 35.0% (others 12.2%) | Measured | Larisa Gurevich, monthly |
| Callbacks completed by the promised date | `completed_at` ≤ `promised_by_date` | 47.3% all; 42.4% permits family | Measured | Division heads; reported by 106 |
| Served in the chosen language | `served_language` = `contact_language`, handled contacts | ar 39.7%, ru 75.9%, am 26.7%, en 89.6% | Measured | Orna Ziv |
| Right answer on the phone | Mystery shopper, quality unit's coding | 54.2% (n = 120); 42.3% where the rule changed in 2026 | Measured (small n) | Quality unit, quarterly |
| Pages out of date (permits) | Page vs council decision 2025/118 | 9 of 24, plus the 2025 fee table linked from 6 pages | Measured | Each division's content owner |
| Rejections with a usable reason | Letter names the condition, the document and the objection route | 0 of 417 | Measured | Eli Saban |
| Cost of a contact | Agent cost per hour ÷ contacts per hour | ≈ ₪130 an hour loaded (budget line 1612-410 ÷ 26 ÷ 1,884 h), ≈ 3.7 min a contact ≈ ₪8 | Directional | Treasurer |

## Opportunity map (permits and fees)

| Candidate | Feed | Type | Screen | Verdict |
|---|---|---|---|---|
| A. Public chatbot on today's website (CivicTalk proposal) | Top-down (mayor's office) | Generate, alone | Data gate fails: 9 of 24 pages wrong; Arabic answers from 2023 pages or machine translation; no content owner; procurement route unclear | **Stop** for now |
| B. One owned, dated knowledge pack for permits and fees, published in four languages | Findings 1, 2, 7, 8 | Not AI | Owners available if the DG names them; 3–4 weeks of editors' time | **Go** |
| C. Decision letters with the condition, the document and the objection route, in the applicant's language | Findings 6, 7; Amal | Not AI (template change in Rishuyit; translation reviewed once) | Needs Eli Saban and IT; legal adviser on wording | **Go** |
| D. Callbacks measured on completion; repeat contacts reported monthly | Findings 3, 4 | Not AI | Export exists; definition change by the DG | **Go** |
| E. Assistant for 106 agents: grounded answers from B, source cited, refuses individual cases, four languages | Requests (Larisa: "for my agents first") | Generate, with a person | Go with a condition: B first; evaluated on our questions; works committee consulted | **Go with condition** |
| F. Machine translation of letters for the desk (replacing Tsega's phone app) | Shadow AI | Generate, with a person | Personal data in letters; tool approval by the CISO | **Go with condition** after C |
| G. Ruti | Shadow AI | Generate, alone | Breaches IS-07; outdated; personal data on a free platform | **Stop now** (Monday) |

## The case (one page, as presented)

**Decision asked on 17 December:** (1) the DG names content owners for permits and fees in four
divisions, with a publication date of 1 March 2027; (2) the forum approves B, C and D; (3) the forum
approves an internal test of E on the city's own questions, reported on 2 February; (4) the forum asks
the council's finance committee to re-label budget line 1611-780 from "smart municipal chatbot" to
"resident information and language service", ₪600,000, with the use decided on 2 February.

**Why.** Permits-family contacts are a third of 106's work; a third of them repeat within two weeks; a
resident who asks in Arabic is answered in Arabic four times in ten; half the parking refusals give a
reason nobody can act on. None of that is fixed by a new channel that reads the same pages.

**What it is worth, labelled.** If B, C and D bring permits-family repeats from 35% to 20% (assumed),
about 990 fewer contacts a month, ≈ 61 agent hours (≈ ₪8,000 a month of capacity, not cash). An agent
assistant (E) adds about 58 net hours a month at 90% accuracy and 0.3 review minutes (directional, from
`fieldkit.cost.pilot_value`), and loses money at 0.6 review minutes. The case is not hours: it is that
the city stops giving residents wrong answers, serves Arabic speakers as well as Hebrew speakers, and
can show the comptroller and the council a measure that means something.

**What it costs.** B: about 120 editor hours plus 4 × 20 hours of division owners, and a translation
order (within line 1611-751). C: a Rishuyit template change (IT, about 10 days) and one reviewed
translation of eight letters. D: none. E (test): model usage of about ₪150 a month at today's prices
plus my time; a small purchase through the treasurer.

**What "no" means.** The website keeps telling Arabic, Russian and English readers the 2025 rules; the
desk keeps refusing leased cars under an abolished rule; any chatbot launched in February repeats both.

**For the mayor on 4 February** (draft for Eyal): "From 1 March: every answer from the city in your
language, every refusal with its reason, every callback measured. And we are testing an assistant for
our 106 team, in four languages, live when it passes."
