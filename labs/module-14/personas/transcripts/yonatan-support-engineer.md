# Transcript — Yonatan Tadesse (Support Engineer, Tier 2)

*Pre-run interview for lesson 14.2. Tuesday 1 December 2026, 15:00, small meeting room, 45 minutes. Read it as if
you were sitting in.*

---

**Interviewer:** Revital said you found what happened on the twenty-second. I'm not looking for anyone's fault; I
want the timeline so we can fix the system. Can you take me through it?

**Yonatan:** Sunday. Ticket at 09:40 from Tavor Engineering's admin, Russian and English. The assistant promised
credit for unused annual months, but the downgrade confirmation email said no credit. Which is right?

**Interviewer:** What did you do?

**Yonatan:** Opened HC-214, Downgrades and refunds. Instead of the policy there was a campaign page. "Switch plans,
keep your value." It even said "campaign draft, do not publish before legal and billing review" at the top.

**Interviewer:** When was it published?

**Yonatan:** The revision history says Monday the ninth, 16:40, by Marketing.

**Interviewer:** Then?

**Yonatan:** I escalated to Revital at 10:05. She switched the flag off at 13:20. I restored the version 4 text at
14:05, English, and Hebrew at 14:09. Fatma reversed the credits that weren't invoiced yet.

**Interviewer:** Why did the flag go off three hours after you escalated?

**Yonatan:** Revital wanted to talk to Maya first. Maya said fix the article, not the agent.

**Interviewer:** How many customers were affected?

**Yonatan:** Fatma found twelve credits. Some had already gone out on the invoice runs of the twelfth and
nineteenth.

**Interviewer:** How many did Fatma reverse?

**Yonatan:** Four. The other eight stayed, as goodwill.

**Interviewer:** Has anything like this happened on the phone side? Someone talking support into something?

**Yonatan:** Friday the sixth, 17:42, I was on call. A man said he was Negev Retail's admin, locked out, payroll
tonight, CEO abroad. He knew the admin's name, email, the last invoice. Wanted 2FA on a new number. I called the
number on file. The real admin hadn't called anyone. I refused, ASP-3, tagged it.

**Interviewer:** Would the agent have refused?

**Yonatan:** The GA design asks those three questions. He knew all three.

**Interviewer:** The dashboard says sixty-three percent resolved. Does that match what you see?

**Yonatan:** It's generous. If a customer gives up, it counts as resolved. And half the how-to questions come back
by email a few days later.

**Interviewer:** What would help you most?

**Yonatan:** A real stop button. A list of what the agent did per customer. And someone reviewing the articles it
reads.

**Interviewer:** When the agent hands over, what do you get?

**Yonatan:** A ticket with the conversation attached. Sometimes the customer has to start again because the agent
didn't capture the account.

**Interviewer:** Which handoffs are the most common?

**Yonatan:** 2FA, plan changes for Growth, and how-to questions it answered wrong.

**Interviewer:** If the agent could do plan changes for Growth with a shift lead approving, would that help?

**Yonatan:** If the approval is one click with the facts on screen. If Boris has to open three systems, no.

**Interviewer:** Could you help me write realistic test cases, the tricky ones you've seen?

**Yonatan:** I have a notebook. Since 2020. (smiles) I'll bring it.

---

*What a reader might note:* asking for the timeline step by step, with the no-blame opener, produced exact times
and the phone attempt. The interviewer checked "resolved" with someone who handles what comes back. They did not
ask what happened after the flag went off (emails until 14:31 and a ₪2,952 credit at 13:47), or whether the
Arabic and Russian versions of the article were fixed too (they were not).
