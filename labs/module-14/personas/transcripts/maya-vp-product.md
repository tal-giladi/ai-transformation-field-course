# Transcript — Maya Rosenthal (VP Product)

*Pre-run interview for lesson 14.2. Monday 30 November 2026, 11:00, glass meeting room, 40 minutes. Read it as
if you were sitting in.*

---

**Maya:** So. Are you here to help us ship or to stop us?

**Interviewer:** To help you ship something that stays shipped. Can you walk me through the GA design, tool by
tool?

**Maya:** Seven tools. Read account, issue credit, change plan, reset 2FA, delete data, email customer, create
ticket. All executing at GA. All plans.

**Interviewer:** Enterprise too?

**Maya:** Enterprise is where the value is. Big accounts, lots of admin questions.

**Interviewer:** How is the credit limit set?

**Maya:** Five hundred shekels, in the system prompt. The model follows it.

**Interviewer:** Is it checked anywhere outside the model? In the tool layer, or billing?

**Maya:** The prompt is the check. It's worked in the beta.

**Interviewer:** The tool-call log shows twelve credits above five hundred in the beta, between ₪504 and ₪4,032.

**Maya:** (looks at the screen) That's... those are the downgrade ones? That was the article. Marketing published
a campaign page. That's a content problem, not the agent.

**Interviewer:** The agent followed the article over the prompt, because the prompt says the help centre is the
source of truth.

**Maya:** Okay. So we fix the article process.

**Interviewer:** And put the five hundred somewhere the model can't talk its way past. Can we come back to that?

**Maya:** Fine.

**Interviewer:** 2FA resets: how does the agent verify the caller?

**Maya:** Three questions. Admin name, admin email, last invoice amount.

**Interviewer:** Support's procedure says those aren't verification: they're on every invoice PDF.

**Maya:** Andrei's procedure. For the agent we wanted no friction.

**Interviewer:** Deletion?

**Maya:** Admin API delete after the customer confirms twice in chat. The console delete is UI-only.

**Interviewer:** The API delete is a hard delete; the console keeps data for fourteen days.

**Maya:** I didn't know that. Noam would.

**Interviewer:** What volume do you expect at GA?

**Maya:** About eighty agent requests a day for Starter and Growth at first: fifty look-ups, eleven credits, six
plan changes, three 2FA resets, ten bug tickets. Enterprise maybe twenty more.

**Interviewer:** If credits and plan changes needed one approver for the first two weeks, that's about seventeen
approvals a day. Support's shift leads have about thirty a day of capacity.

**Maya:** Approvals kill the experience.

**Interviewer:** For two weeks, for two tools, with a date when they come off if the log is clean. Would that
kill it?

**Maya:** ...Show me on paper. With dates.

**Interviewer:** I will. What happens to the conversation data?

**Maya:** Stored in full for quality. From Q2 we want to fine-tune our own model on it.

**Interviewer:** Has Nurit seen that?

**Maya:** Not yet. It's Q2.

---

*What a reader might note:* the interviewer had read the tool-call log, which turned "the model follows it" into
a real conversation about where limits live; they kept the incident framed as "what the agent reads". They
found the fine-tuning plan. They never asked what had been promised outside the company about Lumen Live (a
reseller and a journalist), which is the pressure behind "all tools, all plans".
