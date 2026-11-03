# Lumen Assist — GA design (v3, 18 November 2026; owner: Maya Rosenthal, VP Product)

**Goal.** Lumen Assist resolves customer issues end to end inside the product. GA at **Lumen Live, 9
February 2027**, for every plan. Target 50% of support contacts resolved without a person by end of Q2 2027.

## Tools at GA

| Tool | What it does | How it runs at GA |
|---|---|---|
| Read account | Plan, seats, invoices, recent tickets | Executes |
| Issue credit | Credit on the next invoice | Executes; **limit ₪500 per credit, set in the system prompt** |
| Change plan | Seats and plan changes, all plans | Executes |
| Reset 2FA | Moves an admin's second factor to a new phone | Executes after the agent asks **three security questions** (admin name, admin email, last invoice amount) |
| Delete data | Deletes an account's schedules, staff records and history | Executes via Admin API `DELETE /accounts/{id}/data` after the customer confirms twice in chat |
| Email customer | Sends account documents (invoices, exports) | Executes; to the address the customer gives |
| Create ticket | Hands over to a person or engineering | Executes |

**Identity.** All tools call the Admin API with `svc-support-admin` (already integrated with Deskly; no new
security review needed).

**Logging.** Action log (tool, customer, amount, timestamp) to the analytics warehouse; weekly report.

**Safety.** System prompt rules (see `assist-system-prompt-v7.md`); the model provider's content filter;
kill switch = feature flag `assist_enabled`.

**Humans.** No approvals at GA ("approvals would kill the experience"). Customers can always ask for a person.

**Volume.** Projected from the beta: about **80 agent requests a day** in the first weeks of GA for Starter
and Growth (≈ 50 look-ups, 11 credits, 6 plan changes, 3 2FA resets, 10 bug tickets); Enterprise adds
about 20 a day.

**Knowledge.** Assist searches all published help-centre articles, in the customer's language.

**Data.** Conversations are stored in full for quality review. From Q2 2027 we plan to fine-tune a Lumen
model on beta and GA conversations.

**Open questions.** None blocking.
