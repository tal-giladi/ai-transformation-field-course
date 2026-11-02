# Transcript — Alexei Morozov (Head of IT and BI)

*Pre-run interview for lesson 08.2. Monday 9 November 2026, 11:00, BI room, 35 minutes. The interviewer
is the outside consultant. Read it as if you were sitting in: note what the interviewer found out, what
they missed, and which questions worked.*

---

**Interviewer:** Thanks for setting up the data room so quickly. I want to make sure I read it the way
you built it. What exactly is the extract?

**Alexei:** A random one percent of customers, with all their orders since March, their returns, their
Tikra contacts since May and their Verbalo sessions when they were logged in. Multiply counts by a hundred
for the company.

**Interviewer:** Why customers and not contacts?

**Alexei:** So you can follow one customer across channels. A random sample of contacts breaks the
journeys.

**Interviewer:** And the 2,000 written tickets?

**Alexei:** Different. Random from the whole company, September and October, email, web form and
WhatsApp, with the order facts and the agent's reply. Names and phones removed.

**Interviewer:** In contacts.csv, what is handle_time_sec?

**Alexei:** From the moment the agent opens the conversation to the reply being sent or the call ending.

**Interviewer:** And after_contact_work_sec?

**Alexei:** Time in the wrap-up form after that. Return authorisations, notes.

**Interviewer:** The Q2 report's AHT footnote includes after-contact work; the Q3 one doesn't seem to.
When did the KPI formulas last change?

**Alexei:** Fourteenth of June. Two changes. AHT stopped including after-contact work; Meseret asked.
And the report's contact count became agent contacts only; bot conversations go into containment. Gil
asked for that one.

**Interviewer:** Is that written down anywhere?

**Alexei:** BI's change log in Confluence. Nobody has asked for it before. I'll share it.

**Interviewer:** Please. So Q2 AHT and Q3 AHT are not the same measure.

**Alexei:** Correct. Each is calculated correctly for its definition.

**Interviewer:** The language column: is it reliable?

**Alexei:** For calls it's the IVR choice. For written, Tikra's auto-detection. Arabic written in Latin
letters comes out as English. A few come out as Persian or Urdu. Amharic is often blank.

**Interviewer:** Order numbers?

**Alexei:** Agents type them. NW-4…, nw4…, just the digits, sometimes with a hash. Normalise before you
join.

**Interviewer:** In bot-sessions.csv, some customer ids are empty.

**Alexei:** Not logged in. About four in ten. Verbalo doesn't know who they are.

**Interviewer:** The returns file: are refund dates the date the money left, or the date it was
approved?

**Alexei:** The date finance's run paid it. The run is on Thursdays.

**Interviewer:** And who owns each KPI definition?

**Alexei:** Nobody, formally. Whoever asked last.

**Interviewer:** Can I get access to the live helpdesk later for the pilot? Read-only, a sandbox?

**Alexei:** A sandbox, yes. Send a request through Orly. Two weeks.

**Interviewer:** Thank you. I'll send the request today.

*[end of transcript]*
