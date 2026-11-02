# Returns policy v2: the draft the pilot is tested against

Northwind Outfitters, draft of 17 December 2026, written by the engagement team with Adv. Hila Rosen
(legal counsel) as a **draft for the offline pilot only**. It is not yet approved for publication: the
COO and CFO must decide the business choices marked ★, and counsel signs the final text. All people
and companies are fictional. This page is a course exercise, not legal advice.

Open it in lesson 08.5. Lesson 08.4 shows how it was written.

## 1. One rule for everyone

This policy replaces the "Returns and exchanges" page, section 9 of the terms of sale (version 4.2),
clause 5.2 of the Trail Club terms and step 4 of SOP-WH-07. Agents, the website, the chatbot and the
warehouse use this text and nothing else.

## 2. Cancelling a purchase (changed your mind, wrong size, not what you wanted)

2.1 **Window.** Up to 14 days from the day the customer received the item (the law: Consumer
Protection Law, 5741-1981, section 14C(c)).

2.2 **Trail Club and Silver Trail members: 30 days** from delivery, on the same terms (★ business
choice kept from the club terms; more generous than the law).

2.3 **Extended window.** A customer aged 65 or over, a person with a disability or a new immigrant
(certificate issued less than five years ago) may cancel up to **four months from the day of the
purchase** if the purchase included a conversation with Northwind (phone, or chat with an agent)
(section 14C1). Ask for proof of eligibility before refunding. Whether a conversation with the
chatbot counts as a "conversation" is open with counsel (§ 8).

2.4 **Money back.** The refund goes to the means of payment used, within 14 days of the customer's
notice (section 14E). Store credit only if the customer asks for it.

2.5 **Cancellation fee.** 5% of the item's price or ₪100, whichever is lower (section 14E(b)(1)). No
handling fee, no return-shipping deduction (★ business choice: Northwind pays the drop-off label).

2.6 **Opened packaging.** Opening the box to look at the item does not, by itself, stop a
cancellation. Items returned visibly used go to the returns lead, never refused by the clerk alone
(★ counsel to confirm the wording).

## 3. Faulty, not as described, or delivered late

No cancellation fee. Northwind collects the item from the address it was delivered to and refunds the
full price (section 14E(a)). Delivery is late when the gap between order and delivery is more than 6
days (★ the promise is 3 business days).

## 4. What cannot be cancelled

Items made to order, including personalised items, unless faulty (the law excludes goods made
to order from the cancellation right; counsel to cite the exact provision).

## 5. Exchanges

Size or colour exchanges within 30 days of delivery are free (★ business choice).

## 6. Outside every window

The agent may offer an exchange or goodwill credit; the customer is told plainly that the window has
ended. Never promise money.

## 7. Escalate to a team lead, the same day

A customer who mentions the Consumer Protection Authority, a lawyer, a claim or a card dispute; any
injury or safety issue; any request the agent cannot answer from this page.

## 8. Open questions for counsel (not in the pilot)

Whether a chatbot conversation counts as a "conversation" for the extended window; the wording on
used items; refund of fees charged above the cap since 2019 (the demand letter of 22 September 2026).

## Decision codes used in the pilot

| Code | When |
|---|---|
| `refund_minus_fee` | § 2.1 or § 2.2: refund to the card less the fee (§ 2.5) |
| `refund_no_fee_pickup` | § 3: faulty, not as described or late; collect and refund in full |
| `refund_4m_verify` | § 2.3: extended window, proof needed; refund less the fee |
| `outside_window` | § 6 |
| `excluded_custom` | § 4 |
| `exchange_free` | § 5 |
| `status_update` | "Where is my refund?": look it up and say when |
| `escalate_counsel` | § 7 complaints, threats, card disputes |
| `n/a` | Not about returns (order status, product questions, invoices, other) |

Order of checks: complaint → refund status → faulty or late → personalised → exchange → 14 days → club
30 days → extended window → outside.
