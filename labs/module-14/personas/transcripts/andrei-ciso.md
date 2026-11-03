# Transcript — Andrei Kogan (CISO)

*Pre-run interview for lesson 14.2. Tuesday 1 December 2026, 10:00, Andrei's desk and whiteboard, 40 minutes.
Read it as if you were sitting in.*

---

**Andrei:** Another AI person. What do you need?

**Interviewer:** To understand who acts on customer accounts today, and as whom. I've read the token list and the
audit log.

**Andrei:** Then you've seen svc-support-admin.

**Interviewer:** Created March 2024 by Daniel Weiss, for the helpdesk sidebar. Scopes include credits, plans,
2FA, export, delete and email. And the beta agent uses it.

**Andrei:** Over-scoped. I know. I haven't had time. Maya says "same token support has used since 2024". That's
the problem, not the argument.

**Interviewer:** Daniel left in June. Are there other tokens whose creator has left?

**Andrei:** (draws) Three that I know of. That one, the marketing Zapier token, Gal's, she left in September.
And the R&D Slack bot, Amit's, August.

**Interviewer:** Why are they still active?

**Andrei:** Because if I revoke them something breaks at two in the morning and I get the call. Nobody owns them,
so nobody can tell me what breaks.

**Interviewer:** What does the audit log record?

**Andrei:** Writes. Actor, token, user agent, source, action, customer, result. Not reads.

**Interviewer:** So if three systems share one token, the log can only tell them apart by user agent and timing.

**Andrei:** Exactly. Which is not an audit trail. It's archaeology.

**Interviewer:** The feature flag is called the kill switch in Product's runbook. What does it stop?

**Andrei:** It hides the widget. Ask R&D how Assist runs tool calls. If there's a queue, a flag in the UI doesn't
drain it.

**Interviewer:** 2FA in the GA design: three security questions.

**Andrei:** Name, email, last invoice. All on every invoice PDF. ASP-2 says channel on file. Callback or link to
the admin email. Anything else is a social-engineering kit.

**Interviewer:** Deletion?

**Andrei:** The API delete purges at once. The console is soft, fourteen days. If the agent deletes, it must be
the soft path, and honestly, it shouldn't delete at all.

**Interviewer:** Your position at exec staff was no write access until Q3.

**Andrei:** Still is.

**Interviewer:** What would make you say yes for Starter and Growth on the ninth of February?

**Andrei:** (long pause) Its own identity, only the scopes it needs, no delete. Limits enforced in the tool layer,
not in the prompt. 2FA only through the channel on file. A kill switch I have tested myself. And the log
readable per action.

**Interviewer:** If I bring you that, tested, by mid-January?

**Andrei:** Then we talk.

**Interviewer:** Who would test the kill switch with you?

**Andrei:** R&D on-call. Eyal will give me someone if you ask him, not if I ask.

**Interviewer:** What do you want logged per action?

**Andrei:** The message that triggered it, the documents it read, the tool call with arguments, who approved, the
result. And the identity. Without that, an incident report is a guess.

**Interviewer:** Retention of that trace?

**Andrei:** Ask Nurit. It will contain customer staff data.

---

*What a reader might note:* the interviewer arrived having read the tokens and the audit log, which earned a real
conversation, and turned "is it safe?" into "what would make you say yes?". They got the leavers' tokens and the
kill-switch doubt. They never showed Andrei the audit-log rows with user agent `n8n` at 02:00 under
svc-support-admin, so he still does not know a business user runs an automation with that token every night.
