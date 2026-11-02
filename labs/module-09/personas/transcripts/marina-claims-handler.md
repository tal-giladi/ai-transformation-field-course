# Transcript — Marina Kogan (Senior Claims Handler, Health and Travel)

*Pre-run interview for lesson 09.2. Tuesday 10 November 2026, 13:30, at Marina's desk in Ramat Gan,
30 minutes. The interviewer is the new Head of AI Transformation. Read it as if you were sitting in.*

---

**Marina:** Another AI person. Welcome. Sit, the chair is clean.

**Interviewer:** Thanks. I'm trying to learn how claims really work before anyone changes anything.
Could you show me the last file you closed?

**Marina:** This one. Travel, medical, Batumi. The clinic invoice is in Russian, the medical report is
in Georgian, the boarding passes are fine. Total in lari.

**Interviewer:** What did you have to do to close it?

**Marina:** Ask twice. First the list, then the medical report "in Hebrew or English", because nobody
here reads Georgian. Then wait three weeks for the translation.

**Interviewer:** Why wasn't the translation on the first list?

**Marina:** Because the standard list for travel medical doesn't say it. So for any clinic that isn't
English, the second request is certain. And the first list goes out late anyway: intake waits until
the agent sends "everything".

**Interviewer:** How often is that — the second request?

**Marina:** In my team, most foreign files. In Hebrew files, less.

**Interviewer:** What goes wrong when you read foreign invoices?

**Marina:** American dates are month first. Russian clinics write "12 окт." instead of numbers. Thai
invoices are in baht and people forget to convert. And the new clerks add 18% VAT to invoices from an
עוסק פטור, an exempt dealer, who has no VAT at all.

**Interviewer:** Have you seen Smart Intake?

**Marina:** Not on our line. Haifa says it leaves Arabic amounts empty and sometimes writes the wrong
date with a big confidence score. And it copied a diagnosis into the notes once, on a motor claim.

**Interviewer:** If we tested a tool that reads these documents, what would you want it tested on?

**Marina:** On ours. Foreign invoices, Arabic receipts, bad photos from the app. Not on nice Hebrew
forms from the scanner.

**Interviewer:** Would you help rate the results?

**Marina:** After the winter. Two hours a week. Not in January; in January I don't exist.

**Interviewer:** Understood. Thank you, this is exactly what I needed.

**Marina:** That's all? Usually they ask about AI.

**Interviewer:** I'll come back with a test set and you can tell me what I got wrong.

**Interviewer:** [end interview]

**Marina:** — end of interview —

---

**What to notice.** "Show me the last file you closed" produced the concrete failure modes the eval
must test (US dates, Russian month names, currencies, exempt dealers) and the cause of second
document requests. The interviewer asked her what to test on and secured rating time after the peak.

**Questions nobody asked.** How does she actually read a Georgian or Thai invoice today, while waiting for a translation? What would make it safe to tell you? Try them in your own interview.
