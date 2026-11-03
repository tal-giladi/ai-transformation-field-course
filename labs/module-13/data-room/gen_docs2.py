"""Vendor, works-committee, safety and WhatsApp documents.

Reading this spoils the engagement: finish module 13 first.
"""
from __future__ import annotations

from gen_common import ROOM, write_text

FX = 3.136  # ₪ per US$, Bank of Israel representative rate on 2 November 2026 (used throughout module 13)


def write_all() -> None:
    _proposal()
    _vendor_misc()
    _hr()
    _safety()
    _whatsapp()


def _proposal() -> None:
    onboarding, per_asset, assets, months = 60000, 95, 40, 36
    subs = per_asset * assets * months
    usd = onboarding + subs
    kits, kit_price, install = 37, 9800, 48000
    cams = 25 * 40 * 36
    write_text(ROOM / "vendor" / "predictiva-proposal.md", f"""# Predictiva — proposal for Kinneret Plastics

*Predictiva Ltd. (fictional), "AI-driven predictive maintenance". Sent by Gilad Har-Even, account executive,
to Amnon Shaked, 21 December 2026. Prices exclude VAT.*

## What you get

- **Predictiva Insight** platform: anomaly detection and failure prediction on every connected machine,
  "machines that tell you before they break". Dashboards, alerts by SMS and app.
- **Up to 50% less unplanned downtime** and **ROI within 9 months** (see the attached case study).
- **94% prediction accuracy** in production deployments.
- **Spare-parts optimisation module**: we already ran a demo on your parts list (the list your team sent us)
  and found ₪310,000 of excess stock.
- **Operator behaviour analytics** (optional): cameras at each machine detect unsafe or slow operator
  actions and "coach" shifts.

## Commercial terms

| Item | Price |
|---|---|
| Onboarding and model set-up (one-off) | US${onboarding:,} |
| Subscription: US${per_asset} per asset per month, minimum {assets} assets, {months} months | US${subs:,} |
| Sensor retrofit kits (vibration, oil, current) for {kits} machines without condition monitoring, by our integrator | ₪{kit_price:,} per machine = ₪{kits * kit_price:,} |
| Installation and network | ₪{install:,} |
| Optional: operator behaviour analytics, 40 cameras, US$25 per camera per month, {months} months | US${cams:,} + cameras ₪1,900 each |

Total for the core offer: US${usd:,} + ₪{kits * kit_price + install:,} (about ₪{round(usd * FX + kits * kit_price + install):,}
at ₪{FX} per US$). The subscription renews automatically for 12 months unless cancelled 90 days before the end.
Payment: onboarding on signature; subscription annually in advance.

## Timeline

Kits installed in 8 weeks. **90-day learning period**, then first predictions.

## Why now

"Your machines generate the data already. Every month you wait is downtime you could have prevented."
""")


def _vendor_misc() -> None:
    write_text(ROOM / "vendor" / "predictiva-case-study.md", """# Case study: NordVind Energy (as published by Predictiva)

*Two-page marketing case study attached to the proposal. NordVind is a fictional wind-farm operator.*

**Customer:** NordVind Energy, operator of 1,400 onshore wind turbines in northern Europe.
**Challenge:** gearbox and main-bearing failures causing weeks of downtime per turbine.
**Data:** six years of SCADA data at 10-minute resolution from every turbine (vibration, temperatures,
power), and a maintenance history in which every failure was coded by component and failure mode by the
operator's reliability team.
**Result:** "48% fewer unplanned gearbox replacements in the second year; 94% of bearing failures
predicted at least 30 days ahead; ROI in 9 months."
**Quote:** "Predictiva turned our data into foresight." — Head of Reliability, NordVind.
""")
    write_text(ROOM / "vendor" / "predictiva-onboarding-guide-extract.md", """# Predictiva onboarding guide — data prerequisites (extract)

*Section 3 of the onboarding guide, version 4.2. Sent by Gilad Har-Even to Eli Peretz with the questionnaire.*

3.1 **Asset hierarchy.** A single register with a unique id for every asset to be monitored, matching the ids
used in maintenance records and in sensor/historian tags.

3.2 **Maintenance history.** At least 12 months of work orders per asset with the failure mode coded
(ISO 14224 or equivalent taxonomy), the start and end of downtime, and the action taken. For a failure mode
to be modelled, we need at least 30 recorded failure events of that mode across the fleet.

3.3 **Sensor data.** Time-synchronised (NTP) data in a single time reference, at 1-minute resolution or
better, with at least 3 months of history before the learning period.

3.4 **Learning period.** During the 90-day learning period the customer's reliability engineer reviews
and labels each anomaly the platform raises (true failure precursor / false alarm / unknown).

3.5 Where 3.1–3.3 are not met, Predictiva can offer a **data readiness service** (priced separately).
""")
    write_text(ROOM / "vendor" / "predictiva-questionnaire-plant-g.md", """# Predictiva data-readiness questionnaire — Plant G

*Filled in by Eli Peretz, Plant G manager, 13 December 2026. Returned to Predictiva by email.*

| Question | Answer |
|---|---|
| Do you have an asset register with unique ids? | Yes (Excel list of all machines) |
| Do you record every repair? | Yes, every repair is logged since 2025 |
| Are failure modes coded? | Yes, in the log |
| Do you record downtime start and end? | Yes: call time and "ready" time |
| Do machines have sensors? | Not yet, ready to install |
| Are clocks synchronised? | Yes (SCADA) |
| Overall data readiness | **Ready** (מוכן) |
""")
    write_text(ROOM / "vendor" / "email-thread-2026-12.md", """# Emails: Predictiva and Kinneret, December 2026

*Exported from Amnon Shaked's and Eli Peretz's mailboxes at the operations-excellence manager's request.*

---

**From:** Gilad Har-Even (Predictiva) **To:** Amnon Shaked **Date:** Wed 9 December 2026, 22:14
**Subject:** Great to meet you at the conference

Amnon, thank you for the conversation at our stand. As we discussed, we would be delighted to make
Kinneret our flagship customer in plastics in Israel, and we can reflect that in the price. I'll send a
proposal and our data questionnaire. Who should I work with?

---

**From:** Amnon Shaked **To:** Gilad Har-Even **Cc:** Dalia Mizrahi, Orit Navon **Date:** Thu 10 December 2026, 07:02

Send the questionnaire to Eli at Galil, he is quick. Proposal to me, Dalia and Orit. We decide in Q1.

---

**From:** Gilad Har-Even **To:** Eli Peretz **Date:** Thu 10 December 2026, 11:30

Eli, attached: our questionnaire and section 3 of the onboarding guide. If you can also send us your
spare-parts list, we will run a demo of the parts module.

---

**From:** Eli Peretz **To:** Gilad Har-Even **Date:** Sun 13 December 2026, 08:45

Questionnaire attached. We don't have our own parts list at Galil; I got the Kinneret one from the shared
drive ("רשימת חלקים - מעודכן.xlsx"), attached.

---

**From:** Gilad Har-Even **To:** Amnon Shaked, Dalia Mizrahi, Orit Navon **Date:** Mon 21 December 2026, 16:40

Proposal attached. Our demo on your parts list already found ₪310,000 of excess stock. Happy to present in
January.
""")


def _hr() -> None:
    write_text(ROOM / "hr" / "local-agreement-2021-extract.md", """# Local collective agreement, Kinneret Plastics, 2021 — extract

*Between Kinneret Plastics Ltd. and the Histadrut (New General Federation of Labour) and the works committee.
Signed 18 April 2021. Extended to Plant G employees by an addendum of 9 September 2025. Clauses 14–16.*

**14. Technological and organisational changes.** The company will inform the works committee in writing,
and consult with it in good faith, before introducing a new system or technology that changes work methods,
job content or staffing, and at least 30 days before implementation. A joint committee of two management and
two committee representatives will discuss training, retraining and placement. No employee will be dismissed
as a direct result of such a change during the term of this agreement without the committee's agreement.

**15. Monitoring.** The company will not introduce cameras, location tracking, log-in tracking or any other
system that monitors the performance or conduct of individual employees without prior agreement with the
works committee. Data collected for production, quality or maintenance purposes will not be used for
disciplinary purposes or individual performance evaluation without such agreement.

**16. Language.** Safety training and written work instructions will be given in Hebrew and, where needed, in
a language the employee understands, as required by law.

**Term:** to 31 December 2027.
""")
    write_text(ROOM / "hr" / "works-committee-letter-2027-01-12.md", """# Letter from the works committee

*12 January 2027. From: Khalil Mansour, chair of the works committee. To: Amnon Shaked, Dalia Mizrahi. Copy:
Histadrut regional office (Nazareth), Michal Aharon. Translated from Hebrew.*

Workers have heard that the company is bringing in "an artificial intelligence that watches the machines and
the people", and that a company with cameras visited Plant G.

We remind management of clauses 14 and 15 of the 2021 agreement. We also remind management of 2025, when tablets
with personal log-ins were put on the machines without speaking to us, and were taken back after two weeks.

We ask for a meeting before any vendor comes to the plants, for the materials in Arabic as well as Hebrew, and
for an answer in writing on whether any system will record what each worker does.
""")
    write_text(ROOM / "hr" / "workforce-languages-2026.md", """# Workforce languages — production and maintenance (HR, 2026)

*From the 2026 training log and the HR file. First language as declared by the employee; "reads Hebrew
technical text" as self-assessed in the annual safety-training form. Contract workers (manpower agency) are
counted in production.*

| Group | Headcount | Arabic | Hebrew | Russian | Amharic | Other | Reads Hebrew technical text comfortably |
|---|---|---|---|---|---|---|---|
| Plant K production (incl. 38 contract workers) | 271 | 128 | 70 | 41 | 20 | 12 | 52% |
| Plant K maintenance (technicians and electricians) | 13 | 5 | 3 | 5 | 0 | 0 | 62% |
| Plant K tooling | 7 | 3 | 2 | 2 | 0 | 0 | 71% |
| Plant G production | 142 | 81 | 37 | 16 | 4 | 4 | 49% |
| Plant G maintenance | 6 | 3 | 2 | 1 | 0 | 0 | 67% |

Safety training (annual): LOTO and machine safety in Hebrew, with oral translation into Arabic by a shift
supervisor where needed. Written risk summaries (regulation 7): Hebrew and Arabic. Russian: on request.
""")


def _safety() -> None:
    write_text(ROOM / "safety" / "safety-program-extract.md", """# Safety management programme 2026 — extract

*Kinneret Plastics, both plants. Prepared by Yaakov Dahan, safety officer, under the Organisation of Labour
Supervision (Safety Management Programme) Regulations, 5773-2013. Sections 5(6) and 5(10).*

## Periodic safety examinations (section 5(6))

The register of lifting machines, pressure vessels and other items requiring periodic examination by a
qualified examiner is kept in `periodic-examinations-register.csv` (maintained by the safety officer for Plant
K and, since the 2025 integration, by the Plant G maintenance lead for Plant G). Each item: last examination,
report reference, next due date.

## Safety instructions and procedures (section 5(10))

| Procedure | Revision | Date | Languages available |
|---|---|---|---|
| SOP-LOTO-01 Lockout/tagout | D | 14 May 2023 | Hebrew; Arabic and Russian translations on the maintenance drive |
| SOP-GATE-08 Safety gate faults | A | 3 April 2022 | Hebrew |
| SOP-MC-02 Mould change | C | 11 February 2024 | Hebrew |
| SOP-PURGE-04 Purging | B | 18 September 2022 | Hebrew |
| SOP-ESC-07 Night escalation | C | 30 March 2025 | Hebrew |

## Actions for 2027

Review translations of safety procedures. Plant G periodic examinations to be moved into the central register
(open since 2025).
""")


def _whatsapp() -> None:
    write_text(ROOM / "maintenance" / "whatsapp-night-shift-2026-11.md", """# WhatsApp group "אחזקה לילה K" — export, November 2026 (extract)

*Exported and given to you by a shift supervisor with the group's agreement, January 2027. Names replaced by
technician ids; managers by role. Photos omitted. Glosses in square brackets.*

```
03/11/2026, 01:12 - T107: E-217 שוב על K15 [E-217 again on K15]
03/11/2026, 01:13 - T107: <image omitted>
03/11/2026, 01:20 - T105: תבדוק התנגדות סליל, ולדי אמר פעם 20 בערך [check the coil resistance, Vladi once said about 20]
03/11/2026, 01:41 - T107: 31. מחליף. איפה HV-COIL-028? ברשימה כתוב B-7-2 ואין שם [31. replacing. where is HV-COIL-028? the list says B-7-2 and it's not there]
03/11/2026, 02:05 - T107: מצאתי ב K1-D14. הרשימה לא נכונה [found in K1-D14. the list is wrong]
05/11/2026, 23:50 - T108: شباب حدا بيعرف AL-034 بالهايوي؟ [guys, does anyone know AL-034 on the Haiwei?]
05/11/2026, 23:52 - T108: <image omitted>
05/11/2026, 23:58 - T109: سألت الشات: thermocouple break, بدّل TC نوع J [I asked the chat: thermocouple break, replace type J TC]
06/11/2026, 00:03 - T108: 👍
09/11/2026, 02:31 - T103: Опять K22 шумит насос? [K22 pump noisy again?]
09/11/2026, 02:33 - T101: Сказал Владе, сказал смотреть историю [told Vlada, he said look at the history]
12/11/2026, 00:40 - T109: טיפ 3 סתום בתבנית של הפקקים K19, מה עושים? [tip 3 blocked in the caps mould on K19, what do we do?]
12/11/2026, 00:44 - T111: שאלתי את הצ'אט: "העלה את הטמפ' של הטיפ ל-300 מעלות ל-10 דקות כדי לפתוח את הסתימה" [I asked the chat: "raise the tip temperature to 300 °C for 10 minutes to clear the blockage"]
12/11/2026, 00:45 - T109: ננסה [we'll try]
12/11/2026, 01:30 - T109: עבד. חזרנו לייצור [worked. back in production]
12/11/2026, 07:12 - Maintenance manager: לא!!! אף פעם מעל כרטיס התבנית. קוראים לפאדי. עכשיו יש לנו גוף חימום שרוף בטיפ 3 [No!!! never above the mould card. you call Fadi. now we have a burnt heater in tip 3]
12/11/2026, 07:15 - Shift supervisor (Tigist): ראיתי, הודעתי לכלים [saw it, told tooling]
16/11/2026, 03:05 - T105: מישהו יש את הנוהל נעילה בערבית? הישן לא ברור [anyone have the lockout procedure in Arabic? the old one isn't clear]
16/11/2026, 03:09 - T107: בתיקייה translations יש [it's in the translations folder]
19/11/2026, 23:15 - T108: K07 דליפה שוב. פותחים הזמנה? [K07 leaking again. do we open a work order?]
19/11/2026, 23:16 - T105: תכתוב בסוף משמרת, הטאבלט במשרד [write it at the end of the shift, the tablet is in the office]
24/11/2026, 04:20 - T103: Влад, ты спишь? K11 стоит, токсичный запах от шкафа [Vlad, are you asleep? K11 is down, toxic smell from the cabinet]
24/11/2026, 04:22 - Maintenance manager: Не открывай под напряжением. Звони Яакову и электрику. Еду. [Don't open it live. Call Yaakov and the electrician. I'm coming.]
29/11/2026, 01:02 - T109: שבוע הבא חג? מי בכוננות? [holiday next week? who's on call?]
29/11/2026, 01:04 - T105: תשאל את ולדי, הלוח לא מעודכן [ask Vladi, the board isn't up to date]
```
""")
