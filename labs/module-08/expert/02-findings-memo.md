# Findings memo — Northwind Outfitters customer service

Expert deliverable for lesson 08.2. Version 1.0, Monday 23 November 2026, for Orly Ben-David; shared
with the steering group on 26 November after a private session with each person named in it. Template:
[findings memo](../../../templates/findings-memo.md). Company figures are the 1% customer extract × 100
unless marked. Every finding is labelled **measured** (computed from Northwind's data), **reported**
(someone told us) or **inferred**.

## The answer first

The chatbot is not what is driving cost and pressure in customer service. **Returns are.** About 45% of
agent contacts are about returns, refunds and fees; they repeat because Northwind gives customers four
different answers and pays card refunds a median of 17 days after the request. Since mid-June the team
has shrunk from 42 to 30 agents while repeat contacts almost doubled; the headline "AHT down 30%" is a
change of definition, not a change in work.

## Findings

**1. Repeat contacts nearly doubled after the chatbot launch and the cuts.** Measured: share of agent
contacts from a customer who contacted Northwind about the same order in the previous 7 days, 17.2%
from 1 May to 14 June (379 contacts in the extract) → 32.1% in Q3. Northwind has never reported this
measure (both KPI reports: "not tracked"), so 1 May – 14 June is the only baseline. Consequence: the
team handles more contacts per order; any saving claimed from the bot must be netted against them.

**2. "AHT down 30%" compares two different measures.** Measured and reported: from 14 June, AHT excludes
after-contact work (BI change log; Q2 vs Q3 report footnotes). Like for like (handling + after-contact
work), AHT rose from 7.9 minutes before 15 June to 8.9 after. Consequence: the board slide's −30% should
be withdrawn or footnoted.

**3. Returns drive about 45% of agent contacts.** Measured, three ways that disagree: helpdesk category
"Returns & refunds" 33.4% (+4.4% "Damage / defect", but 15.4% "General" and 3.7% blank); tag `returns`
37.5%; the 2,000 written tickets read and labelled: 53.5% returns, refunds, fees and exchanges. We use
"about 45% (38–54%)" until the category field is fixed.

**4. Four written policies, nine macros.** Measured: the returns page (14 days, unopened only, store
credit, 10% + ₪39), the terms of sale §9 (money back within 14 days of notice, fee 5% or ₪100 whichever
lower, defects collected), Trail Club terms 5.2 (30 days, refund), warehouse SOP-WH-07 (credit for
opened items, 10% + ₪39). Agents choose: in the 2,000 tickets, today's reply matched one consistent
reading of Northwind's own terms in 55.6% of returns tickets (test set, n = 691). Reported (frontline,
not attributed): an unofficial document tells experienced agents which rule to apply "when the
customer pushes". Consequence: the answer a customer gets depends on who answers and how hard they push.

**5. Refunds are slow and step 2 of the SOP exists only on paper.** Measured: card refunds a median 17
days after the request (66% over 14 days); every card refund is paid on a Thursday; inspection a median
3 business days before 1 August and 8 after (the SOP says 2). Reported: two of four returns clerks were
moved to the warehouse floor in July. Consequence: "where is my refund?" is about one agent contact in
ten, and repeats.

**6. The chatbot states returns policy, often a version Northwind's own terms contradict.** Measured: of
69 chatbot answers to returns-policy questions (excluding hand-overs and "didn't understand"), 26 promise
"30 days, full cash refund" and 24 say "store credit only"; 19 match the terms of sale. Example:
transcript 2, a non-member told "30 days, full refund", refused a week later; the Consumer Protection
Authority inquiry of 17 August. The bot answers Arabic and Russian messages in Hebrew (121 of 439
sessions are in another language). Consequence: Northwind is making statements about cancellation
rights through a channel nobody reviewed. Legal assessment is for counsel.

**7. "Containment" is not resolution, and it is billed.** Measured: of logged-in chatbot sessions Verbalo
counts as resolved, 64.1% were followed by an agent contact from the same customer within 7 days
(n = 170; 78% for returns-policy questions). Each is billed at US$0.85 (order form §3).

**8. The team was cut against an untested tool and is now overloaded.** Measured: 42 agents in June,
30 in September; contacts per agent ≈ 600 a month in May–June, ≈ 1,220 in August–October; median
written first response 2.6 h (May) → 8.1 h (September); median phone wait 83 s → 225 s (October).
No test or evaluation of the bot exists in the data room; the vendor's results were measured on 40
English questions chosen with e-commerce. Reported: about 26 agents on the floor on a normal day.

**9. Legal and contract exposure is open.** Measured (logs): counsel's review of the returns page has
been "awaiting business decision" since April; 9 Authority inquiries and 4 small claims in 2026 on
returns; a demand letter threatening a class action on cancellation fees and store credit (22
September). The Verbalo contract was not reviewed by counsel; §7 lets Verbalo train on conversation
data unless Northwind opts out; renewal notice is due by 1 April 2027.

## What we did not find

No evaluation of the chatbot; no repeat-contact report; no owner for KPI definitions; no 2025 contact
data (seasonality unknown).

## Recommended next steps (phase 2)

1. Measure the cost of each option against cost per order and repeat-contact rate (08.3).
2. Decide the chatbot's role and the returns policy together with counsel (08.4, by 3 December).
3. Test agent-assist offline on the 2,000 tickets against a policy counsel has marked up (08.5).
4. No further reduction in agents before the January decision (a recommendation to Orly; HR decides).

Checked against sources by a second reader (Alexei, numbers; Meseret, the floor description) on 24
November.
