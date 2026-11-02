# Transcript — Dr. Rana Haj-Yahia (DPO)

*Pre-run interview for lessons 09.4 and 09.5. Wednesday 2 December 2026, 16:00, video call, 35
minutes. The interviewer is the new Head of AI Transformation. Read it as if you were sitting in.*

---

**Rana:** Thanks for coming to me before the committee, not after. What do you need?

**Interviewer:** Two things: what the privacy questions are for Smart Intake and Fraud Insight, and
the data rules for an extraction pilot I'll build on the pseudonymised documents.

**Rana:** Start with Smart Intake. Did anyone tell you where it processes documents?

**Interviewer:** The release notes say Kalanit's cloud capture service, EU region, and Annex C of the
agreement says Frankfurt.

**Rana:** I learned that from you, now. The Annex C notice went to the CIO office in August. Health
claims are not on Smart Intake yet, but motor claim forms sometimes describe injuries, and the plan is
to extend it.

**Interviewer:** There's more. Smart Intake copies text it finds into the claim's free-text notes.
In the vendor's batch run on 240 documents, 45 had a diagnosis copied into that field.

**Rana:** Who can see the notes field?

**Interviewer:** As far as I know, every claims user.

**Rana:** Then the notes field must stop receiving diagnoses now, whatever else we decide. Health
information is information of special sensitivity after Amendment 13. I need the data flow, the
sub-processor terms and a privacy impact assessment before it goes to any other line.

**Interviewer:** Is the transfer to Frankfurt itself a problem?

**Rana:** Not in itself: Israeli rules allow transfers to EU countries. The questions are the
contract, what is sent, how long it is kept and whether it is used for anything else. Which brings me
to clause 9.2.

**Interviewer:** The one that lets Kalanit train on anonymised data?

**Rana:** Yes. I objected at the renewal in 2024. It stayed as a "standard clause". Put it in your
paper as an open risk. I'll write the wording.

**Interviewer:** Thank you. For my pilot: I'll use the 240 documents in the data room, already redacted
by the scanning room. The model returns only the fields we ask for. I want to make "no diagnosis, no
extra fields" a test the pilot must pass, not a promise.

**Rana:** That is exactly how I'd like it. And which tool will you use?

**Interviewer:** An enterprise LLM account the CIO approves, with no training on our data and a data
processing agreement. For the offline pilot only redacted documents leave Meridian.

**Rana:** Write that into the pilot charter and send me the vendor's terms. If it goes live, it's a
new processing purpose for claims data and I want a DPIA.

**Interviewer:** And the EU question: travel claims include invoices from European hospitals. Does EU
law reach us?

**Rana:** When the claimant sends us their own invoice, the 2023 regulations on data from the EEA
don't apply to that. If an assistance company gets records straight from a hospital there, ask me.
The EU AI Act is not my area, but I don't see us selling in the EU.

**Interviewer:** [end interview]

**Rana:** — end of interview —

---

**What to notice.** The interviewer came with facts the DPO did not have (Frankfurt, the notes field,
45 diagnoses), turned data minimisation into a test, and asked about the pilot's own data use before
building it.

**Questions nobody asked.** Do staff already use public AI tools, for example to translate foreign documents? Has anyone asked her? Try them in your own interview.
