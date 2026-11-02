# Transcript — Gil Navon (Account Executive, Kalanit Systems)

*Pre-run interview for lesson 09.4. Thursday 3 December 2026, 10:00, Meridian's meeting room 4, 45
minutes. The interviewer is the new Head of AI Transformation; Noam Segal (Meridian's Kalanit product
owner) is present and silent. Read it as if you were sitting in.*

---

**Gil:** Meridian is one of our most innovative customers. I'm glad you're on board. Pro would make you
the first insurer in Israel with network analytics.

**Interviewer:** Thanks for coming. Before Pro, I need to understand what is live. Can we go through
three numbers from your materials, one by one?

**Gil:** Of course.

**Interviewer:** Smart Intake, 97.4% field-level accuracy. What documents was that measured on?

**Gil:** Our benchmark set in the lab. Five hundred claim forms.

**Interviewer:** Which language, and typed or handwritten?

**Gil:** Hebrew motor forms, typed, scanned at 300 dpi. It's the standard benchmark.

**Interviewer:** On your batch run of our 240 documents, I get 82% overall and 62% on Arabic documents.
Is there a known issue with Arabic?

**Gil:** Some garages use Eastern Arabic digits. The capture service doesn't map them yet. It's fixed in
9.6, second quarter of 2027.

**Interviewer:** Thank you. Second number: Fraud Insight identified 78% of fraud-flagged claims, AUC
0.81. What does "fraud-flagged" mean?

**Gil:** Claims your SIU flagged. The SUSPECT flag in Kalanit.

**Interviewer:** So flagged for investigation, not confirmed as fraud.

**Gil:** Those are the labels the customer has. Confirmed outcomes are rarely recorded.

**Interviewer:** Then the test shows the score imitates past referrals. Third: the ₪20 million.
Where does "10% of claims" come from?

**Gil:** Industry studies. Our marketing team has the source; I'll send it.

**Interviewer:** Please. How is the Fraud Insight score computed?

**Gil:** It's AI-driven, explainable: every factor that fires is shown to the SIU.

**Interviewer:** Does it learn from Meridian's outcomes, or is it fixed weights?

**Gil:** The template is configured per market. For Israel, from our consortium analysis. It's fully
explainable, every point has a reason.

**Interviewer:** I'll need the factor list and weights in writing, and the analysis behind the
template. Can you send both by Tuesday?

**Gil:** I'll check with the product team about the analysis. The factor list is in your configuration
export already.

**Interviewer:** Last thing: if we wanted to change the configuration, what does it take?

**Gil:** The opt-out window closed in September, unfortunately. But let's talk about how Pro fixes all
of this.

**Interviewer:** Not today. I'll send you a written list of questions.

**Interviewer:** [end interview]

**Gil:** — end of interview —

---

**What to notice.** Reading back each claim with "measured on what?" got the 97.4% conditions, the
Arabic digits issue and the fact that the fraud label is a referral. Asking for things in writing with
a date is the right close.

**Questions nobody asked.** Can Meridian switch auto-referral off, or remove a factor, today, and at what cost? Does the score learn at all, and where do the template's weights come from? Try them in your own interview.
