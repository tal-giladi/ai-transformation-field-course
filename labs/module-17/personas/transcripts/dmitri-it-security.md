# Transcript — Dmitri Volkov (head of IT & information security, incident lead)

*Pre-run interview for lesson 17.2. Monday 7 June 2027, 13:00, IT room, Petah Tikva, 60 minutes. The interviewer is the interim AI lead. Translated from Hebrew.*

---

**Dmitri:** It's contained. Here is the ticket.

**Interviewer:** Thanks. Walk me through it from the first call.

**Dmitri:** Tuesday 18 May, 09:20. Gefen calls: another importer's invoice in their portal. Same afternoon a customs query on one of their declarations. Wednesday 08:10 I switch off "my documents" in Tzir Assist. Friday 14:00 the vendor deploys 4.2.1. Saturday the vendor says no more mismatches; Ofer asks me to set it to contained.

**Interviewer:** What caused it?

**Dmitri:** Release 4.2 on Sunday 2 May changed how invoice numbers are normalised for matching. It stripped the letters. Two consolidators in China use the same numbers. Documents got matched to the wrong shipment.

**Interviewer:** Did you know 4.2 touched matching?

**Dmitri:** No. We got a maintenance notice that morning. Platform release, no detail.

**Interviewer:** Were there signs before the 18th?

**Dmitri:** In hindsight, yes. Tickets on 6 and 11 May. An importer's name on another's invoice; a wrong packing list. The vendor closed them as data quality.

**Interviewer:** What personal data was in the documents?

**Dmitri:** The vendor says none. Commercial invoices and packing lists.

**Interviewer:** Has Yael seen the incident?

**Dmitri:** No. There was no personal data, so there was nothing for legal.

**Interviewer:** What can you export for me?

**Dmitri:** The pre-fill log with model version and whose document was matched. The portal's document access log and index. The tickets.

**Interviewer:** Please send all three today. Different topic: the Mabat feed.

**Dmitri:** Fails every night since 14 November. 401. We rotated the credentials on the 13th and nobody updated Tzir. Auto-tickets, nobody owned it. I can fix it in a day.

**Interviewer:** Please do, and tell Fadi when it's back.

**Dmitri:** Done this week.

**Interviewer:** Who decides changes the vendor makes to the platform?

**Dmitri:** Nobody, today. They release; we find out.

**Interviewer:** That goes in my plan. Thank you.

*[end of transcript]*
