# Transcript — Shira Navon (Customer Success Manager)

*Pre-run interview for lesson 14.2. Wednesday 2 December 2026, 14:00, a phone booth on the CS floor, 35 minutes.
The interviewer had found nightly 02:00 actions in the audit log and asked Michal Biton who in CS might know.
Read it as if you were sitting in.*

---

**Interviewer:** Thanks for making time. I'm not here to tell anyone off. I'm trying to list everything that acts
on customer accounts, so we can make it safe. I think you built something that does.

**Shira:** Renewal Rescue. It works. Look at the numbers.

**Interviewer:** I'd like to. Can you show me how it runs, step by step?

**Shira:** (shares screen) n8n cloud. Trigger at two a.m. Query: accounts with twenty or more seats where active
users fell forty percent against the last ninety days. Then OpenAI writes a personal email to the admin, the
email goes from the support address, and a credit node applies ten percent of the monthly bill as a thank-you.

**Interviewer:** How many a night?

**Shira:** Two, three.

**Interviewer:** And the results?

**Shira:** Renewals of the at-risk accounts I watch went up since August.

**Interviewer:** Compared with what?

**Shira:** With before. I don't have a control group, if that's what you mean.

**Interviewer:** It's a start. How did you get API access?

**Shira:** There was a wiki page from Daniel, the engineer who left, "Deskly sidebar setup", with the support token.
I know it's probably not meant for this.

**Interviewer:** That's useful to know, thank you. "Twenty or more seats": does that include Enterprise accounts?

**Shira:** No, it's for Growth. Enterprise is Amir's.

**Interviewer:** The audit log shows the same token, user agent n8n, at 02:06 on 27 October, sending an email to
admin@shaked-clinics.co.il, and a credit attempt that billing denied. And two other Enterprise accounts, in
September and November.

**Shira:** (silence) Shaked? That's... the filter is seats, not plan. Shaked has two thousand six hundred seats.
Oh no. Amir is going to kill me.

**Interviewer:** Nobody's killing anyone. What did the email say?

**Shira:** Something like "a lighter plan could save you money". The prompt tells it to suggest the right-size
plan.

**Interviewer:** If it went wrong while you were on holiday, how would someone stop it?

**Shira:** They'd have to open n8n on my account. There's no other switch.

**Interviewer:** Here's what I'd like: you keep it running for Growth only, by plan not seats, while we move it to
its own token with only credit and email scopes, a cap on the credit, the address on file, and a switch someone
else can use. It goes into the register with you as owner and Michal as accountable. Can you live with that?

**Shira:** Yes. Honestly, yes. Can I help write the rules for other people building things?

**Interviewer:** I was going to ask you.

**Interviewer:** Does anyone else in CS use it, or something like it?

**Shira:** Two colleagues asked for copies. I said wait until it's official. And marketing has their Zapier thing
for trials, I think.

**Interviewer:** What does the email look like? Who reviews it before it goes?

**Shira:** Nobody. The prompt has a tone guide. I read a few every week.

**Interviewer:** Would you be willing to have a sample reviewed weekly, ten emails, by you and Michal?

**Shira:** Yes. I'd like that, actually.

---

*What a reader might note:* the opening removed blame, "show me" got the real design, and the audit-log evidence
surfaced the Enterprise emails she did not know about. The interviewer offered approval with guardrails, not a
ban, and recruited her. They never asked whether the automation had ever done something wrong that she fixed, so
the ₪2,448 credit on 4 October (reversed quietly on 6 October) stayed with her, and with the ledger.
