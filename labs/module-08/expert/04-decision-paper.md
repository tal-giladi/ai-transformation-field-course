# Decision paper: chatbot or agent-assist, and the returns policy first

Expert deliverable for lesson 08.4. Version 1.1, Thursday 3 December 2026, for the steering group
(exit point 2). Read by Hila Rosen (counsel) on 2 December for the legal statements, which are hers, not
ours; this paper is not legal advice. Templates: [decision-ready case](../../../templates/decision-ready-case.md),
[claim read-back](../../../templates/claim-read-back.md), [risk register](../../../templates/risk-register.md).

## The decision asked

**Approve:** (1) one returns policy, drafted by us with counsel by 17 December, published after the COO,
CFO and counsel sign; (2) the chatbot restricted to order status and hand-over for anything about
returns, refunds or money from 10 December; (3) an offline test of agent-assist on the 2,000 tickets,
reported on 7 January. **Decline:** extending the chatbot to returns, refunds and WhatsApp in Q1 2027.

**What a "no" means:** the bot keeps stating returns rules Northwind's terms contradict, at about 3,400
returns-policy chats a month company-wide, through Black Friday and the January sale.

## 1. Three options

| | A. Extend the chatbot (the stated ask) | B. Agent-assist (drafts for agents) | C. Do nothing new |
|---|---|---|---|
| Who speaks to the customer | The bot, alone | An agent, with a draft | An agent, with nine macros |
| Who decides refund and fee | The bot, from whichever text it retrieves | Rules on order data; agent confirms | The agent, from four policies |
| Languages | Hebrew, English (Arabic/Russian not before Q3 2027) | Drafts in he, ar, ru, en; Amharic to a person | As today |
| Measured today | 64% of "resolved" chats come back within 7 days; 50 of 69 policy answers contradict the terms | — (tested in 08.5) | 55.6% of returns replies consistent; 32.7% give less than the terms |
| Cost | US$4,800 + US$0.85 per "resolution"; ≈ ₪14 per truly resolved chat | Tokens ≈ ₪0.03 a ticket; owner and checks ≈ ₪12,000 a month | Status quo |
| Liability | Northwind speaks through it; nobody reviews each answer | A person sends every reply | As today |
| Depends on the policy being fixed | Yes, completely | Yes, for its value | — |

**Recommendation: B, after the policy, with the bot narrowed (C for returns).** Not because generation
is bad: because a customer-facing bot can only repeat the policy it is given, and Northwind's policy is
four policies.

## 2. The liability read (counsel's points, as she gave them)

- A chatbot on Northwind's website answering "store credit only" or "30 days, full cash refund" is
  Northwind making a statement to a consumer about cancellation terms. Whether a given answer is
  misleading is for counsel case by case.
- The public case everyone will cite: **Moffatt v. Air Canada**, 2024 BCCRT 149 (British Columbia Civil
  Resolution Tribunal, 14 February 2024). The airline's website chatbot told a grieving customer he could
  claim a bereavement fare after buying; the airline refused; the tribunal held Air Canada liable for
  negligent misrepresentation, rejected the argument that the chatbot was responsible for its own
  words, and ordered it to pay the fare difference (CA$650.88) plus interest and fees. A Canadian small-
  claims tribunal binds no Israeli court; the question it asks ("who is the business speaking
  through?") is the one any court will ask.
- The Consumer Protection Law, 5741-1981 (חוק הגנת הצרכן) prohibits misleading a consumer on a
  material matter, including cancellation conditions (section 2(a)); sets the cancellation window and
  the fee cap for distance sales (sections 14C, 14C1, 14E); allows punitive damages without proof of
  damage when a cancelled transaction is not refunded (section 31A); and claims against a dealer under
  it may be brought as class actions (Class Actions Law, 5766-2006, second schedule, item 1).
- Open with counsel, not assumed in anything we build: whether a chat with the bot counts as a
  "conversation" for the four-month right of senior citizens, people with disabilities and new
  immigrants; the wording on used items; the refund of past deductions (the demand letter).

## 3. The returns policy v2: outline sent to counsel on 7 December

One page, replacing all four texts and the nine macros. Business choices marked ★ for Orly and Boris:

1. Cancel within 14 days of delivery; **★ club members 30 days** (kept from the club terms).
2. Money back to the card within 14 days of the notice; **★ store credit only if the customer asks** (with
   a 5% bonus, to keep part of the breakage).
3. Fee 5% or ₪100, whichever is lower; **★ no handling fee; Northwind pays the drop-off label.**
4. Faulty, not as described, late (more than 6 days order → delivery): no fee, Northwind collects.
5. 65+, disability, new immigrant, purchase in a conversation with an agent: four months from the
   purchase, proof requested.
6. Personalised items excluded unless faulty. **★ Size exchanges free within 30 days.**
7. Escalate the same day: the Authority, a lawyer, a claim, a card dispute, any injury.

Counsel marked it up on 17 December; the marked-up version is the pilot's reference
(`labs/module-08/pilot/policy-for-pilot.md`).

**The money, honestly (for Boris).** Measured in the extract and scaled: handling fees above the cap
≈ ₪1.4M a year; deductions on defect returns ≈ ₪0.4M; shipping deductions ≈ ₪2.3M (★); credit-note
breakage ≈ ₪2.6M a year, part of which goes if credit is optional. Against it: ≈ 6,800 fewer agent
contacts a month (assumed), 96 chargebacks a quarter, and an exposure counsel describes as meaningful.
This is a compliance decision with a cost, not an AI saving.

## 4. Vendor claim read-back (Verbalo)

| Claim | Conditions under which it was measured | Fit with Northwind | Read-back |
|---|---|---|---|
| 62% containment | 40 questions chosen with e-commerce, English, sandbox, 12 May; 4 about returns, none with an exception | Poor: Hebrew, Arabic, Russian; exceptions are the work | Not evidence for production |
| 95% accuracy | Rated by Verbalo's own solution engineer | No independent rater | Not evidence |
| "Resolution" | Conversation ended without hand-over, including closed windows; billed | 64% come back within 7 days | Renegotiate: no agent contact within 72 hours, Verbalo's offer for 24 months (we recommend 12) |
| CSAT 4.6 | Thumbs widget on resolved chats, people who click | 95 down, 45 up in the extract | Not a satisfaction measure |
| Arabic and Russian | "Roadmap" | 28% of chats | Q3 2027 at the earliest, in writing |

Contract actions before the 1 April notice date: counsel review of §5–§7; written opt-out from training
(§7); knowledge content reduced to delivery and order-status pages, reviewed by marketing and counsel.

## 5. Risks if approved

| Risk | Owner | Control |
|---|---|---|
| Policy slips "until after the peak" (future 3 in the debrief) | Orly | Date in the decision record: publication 1 February |
| Agents keep the exceptions document | Meseret | Retire it publicly on the day v2 is published; ask agents what it covered that v2 does not |
| Fee and breakage loss hits 2027 budget | Boris | Shown in the January budget, not discovered in April |
| Gil's board story | Gil, with us | "Fewer contacts per order and a smaller team through attrition, measured monthly" |
