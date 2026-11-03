"""ai/, vendor/ documents, incident/ documents, people/ letters, customers/gefen e-mail."""
import csv


from gen_common import ROOT, write_md, write_csv

REGISTER = [
    ["AI-01", "Tzir Route", "Tzir AI", "I. Barkan", "North; Centre; South; Europe", "Live", "Medium",
     "Dispatcher approves every plan", "Fuel and km -18% (Tzir dashboard)", "2027-03-01"],
    ["AI-02", "Tzir Docs", "Tzir AI", "I. Barkan", "Haifa; Ashdod; airport", "Live", "Medium",
     "Licensed agent reviews every declaration", "99.2% accuracy; 8 FTE freed", "2027-03-01"],
    ["AI-03", "Tzir Assist", "Tzir AI", "I. Barkan", "All customers", "Live", "Low",
     "Hand-over to an agent on request", "35% deflection (target)", "2027-03-15"],
    ["AI-04", "Kotev Assist", "Kotev", "I. Barkan", "All office staff", "Live", "Low", "Users check outputs",
     "Productivity", "2026-12-01"],
    ["AI-05", "Ayin Drive", "Ayin Drive", "M. Azulay", "South (60 cabs)", "Pilot", "Low",
     "Safety officer reviews alerts", "Fewer accidents (target)", "2027-01-15"],
    ["AI-06", "Nezek Vision", "Nezek Vision", "I. Barkan", "Modi'in DC", "POC complete - scaling Q3", "Low",
     "Supervisor confirms damage", "Claims handling -40% (vendor)", "2027-02-28"],
    ["AI-07", "Quote assistant", "Taarif", "I. Barkan", "Sales", "Live", "Low", "Sales manager approves quote",
     "Faster quotes", "2026-10-15"],
    ["AI-08", "Warehouse demand and labour forecast", "in-house", "L. Gabay", "Modi'in DC", "Live", "Low",
     "Supervisor adjusts plan", "Overtime -14% (Modi'in vs Ashdod)", "2027-04-20"],
]


def register() -> int:
    header = ["system_id", "system", "vendor", "business_owner", "scope", "status", "risk_rating",
              "human_oversight", "value_evidence", "last_review"]
    return write_csv("ai/ai-register-2027-03.csv", header, REGISTER)


HANDOVER = """
# Handover note — Itai Barkan, 27 May 2027

Short, sorry. The register (`ai-register-2027-03.csv`) is the master list; Noa keeps it.

- **Tzir platform.** All three modules run; Yaniv Sasson is our contact. Anniversary of the Route order form is 1 October — check MSA 7.4 before July.
- **Docs incident.** Vendor says contained. Dmitri has the ticket. My 14/4 note to Ofer on Docs review is relevant here.
- **Route.** Retraining depends on the Mabat feed; I asked IT in November.
- **Forecast.** Lior built it and runs it. Nobody else has access; he should not stay alone with it.
- **Nezek.** POC finished; somebody needs to stop the billing.
- **Kotev.** Svetlana asked about seats in March; I didn't get to it.
- **Works committee.** Moti handles it.

Good luck. I'm reachable once if you need context: 052-5550178.
"""

MODEL_CARD = """
# Tzir Route — model card (vendor document, version 3.4, October 2026)

**What it does.** Builds daily delivery routes for a depot: sequence of stops, assignment to trucks, expected arrival windows. Plans go to the planner console and, when the dispatcher releases them, to the driver app.

**Model.** Gradient-boosted travel-time model per road segment and hour, plus a vehicle-routing solver.

**Training data.** GPS traces of 1,140 commercial fleets in Israel, **January 2021 to June 2023**; public road network (OpenStreetMap snapshot, July 2023); historical delivery windows.

**Customer adaptation.** "Customer-specific fine-tuning runs quarterly from the customer's telematics feed once the feed has been validated."

**Driver score.** Optional feature: a 0–100 score per driver from harsh braking, idling, deviation from plan and phone handling events. "Intended for coaching. Not designed for disciplinary decisions."

**Known limitations.** Road closures not present in the network snapshot must be entered by the customer in the console; travel-time estimates assume traffic patterns similar to the training period.

**Baseline for savings.** The value dashboard compares the optimised plan with a naive shortest-path sequence of the same stops (see dashboard documentation).
"""

FORECAST = """
# Warehouse demand and labour forecast — back-test (Lior Gabay, April 2027)

Model: weekly pallets per client and shift at Modi'in DC, gradient boosting on 3 years of WMS history, client promotions and holidays. Output: suggested labour plan per shift, which the supervisor adjusts.

| Back-test, 20 held-out weeks (2026) | Supervisor's spreadsheet | Model |
|---|---|---|
| Weekly pallet forecast error (MAPE) | 18.4% | 11.2% |
| Weeks with error above 25% | 6 | 1 |

Live since 3 January 2027 at Modi'in DC only. Ashdod DC still plans with the spreadsheet, so it is a fair comparison for overtime (`operations/warehouse-overtime-weekly.csv`).

Running it: I retrain monthly by hand and check the error on the last four weeks. No documentation beyond this page; the code is in my repository on the company cloud.
"""

MSA = """
# Tzir AI — master services agreement MSA-TZ-2026 (extract of clauses)

*Signed 15 September 2026 by Ofer Lavi (Vantage) and Tzir AI Ltd. Extract prepared by Legal for the AI programme.*

**4.3 Changes to the Services.** Supplier may update the Services from time to time. Supplier shall give Customer at least fourteen (14) days' written notice of any material change to the models or processing logic of the Services, other than urgent security fixes.

**7.4 Regional scope.** At each anniversary of an Order Form's start date, Customer may reduce the regions or seats under that Order Form by written notice given not less than ninety (90) days before the anniversary. Seat fees reduce accordingly; platform fees are unaffected.

**9.1 Data.** Customer's data, including documents uploaded to the Services, remains Customer's. Supplier processes it only on Customer's documented instructions and for providing the Services.

**9.3 Data incidents.** Supplier shall notify Customer without undue delay after becoming aware of any incident affecting Customer's data, and shall provide the information Customer reasonably requires, including logs.

**11.2 Service credits.** For each month in which a Severity 1 defect remains unresolved for more than five business days, Customer is entitled to a credit of 10% of that month's fees for the affected Order Form.

**12.1 Value reporting.** Supplier provides a value dashboard. Figures are estimates based on Supplier's methodology and are not warranted.

**14.2 Termination for cause.** Either party may terminate an Order Form for material breach not cured within thirty (30) days of written notice.
"""

ORDER_FORMS = """
# Tzir AI — order forms under MSA-TZ-2026 (summary prepared by Procurement)

| Order form | Module | Signed | Signed by | Start | Term | Monthly | One-off | Total over term |
|---|---|---|---|---|---|---|---|---|
| TZ-OF-101 | Tzir Route | Tue 15 Sep 2026 | O. Lavi | 1 Oct 2026 | 36 months | ₪135,000 | — | ₪4,860,000 |
| TZ-OF-102 | Tzir Docs | Wed 16 Sep 2026 | O. Lavi | 1 Nov 2026 | 36 months | ₪130,000 | — | ₪4,680,000 |
| TZ-OF-103 | Tzir Assist | Thu 17 Sep 2026 | O. Lavi | 1 Dec 2026 | 36 months | ₪95,000 | ₪1,450,000 | ₪4,870,000 |

Approval route recorded by Procurement for each order form: "CEO (up to ₪5M)".

TZ-OF-101 seats: 310 driver-app seats at ₪290 and 24 planner seats at ₪1,100 a month, by region (North 104 + 6, Centre 70 + 8, South 92 + 6, Europe 44 + 4), and a platform fee of ₪18,700 a month.
"""


def dashboard() -> str:
    with open(ROOT / "operations" / "route-daily-by-depot.csv", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    saved_km = 0
    tool_routes = 0
    for x in rows:
        if x["km_naive_baseline"] and x["date"] <= "2027-05-31":
            saved_km += int(x["km_naive_baseline"]) - int(x["km_tool_plan"])
            tool_routes += int(x["routes_tool_planned"])
    rate = 4.10
    to_date = round(saved_km * rate)
    per_route = saved_km / tool_routes
    all_routes_year = sum(int(x["routes"]) for x in rows if "2026-06-01" <= x["date"] <= "2027-05-31") * 365 / 245
    annual = round(per_route * all_routes_year * rate, -4)
    return f"""
# Tzir value dashboard — Vantage Logistics (export, 31 May 2027)

*Generated by Tzir AI. Figures are estimates per Tzir methodology (MSA 12.1).*

| Metric | Value |
|---|---|
| Regions live | 4 (North, Centre, South, Europe) |
| Active drivers | 310 |
| Routes optimised to date (since 8 Nov 2026) | {tool_routes:,} |
| Kilometres saved to date | {saved_km:,} |
| Savings to date | ₪{to_date:,} |
| Annualised savings at full scope | ₪{annual:,.0f} |
| Plan adherence | 100% (assumed) |

**Methodology.** Kilometres saved = naive baseline km − optimised plan km, for every route planned in Tzir Route. The naive baseline is the shortest-path sequence of the same stops in the order received. Savings = km saved × ₪4.10 per km (Tzir default: fuel, tyres and driver time). Active drivers = licensed driver-app seats. Annualised savings scale the saving per optimised route to all routes in the licensed regions.
"""


INCIDENT = """
# Incident record INC-27-0518-01 (IT service management export, 3 June 2027)

| Field | Value |
|---|---|
| Opened | Tue 18 May 2027 09:20, from Customer Service (call from customer C1007) |
| Systems | Tzir Docs, Tzir Assist |
| Severity | P1 |
| Incident lead | Dmitri Volkov |
| Status | **Contained** (Sat 22 May 2027 11:20) |
| Summary | Customer C1007 saw another importer's invoice in the portal (Tzir Assist, "my documents"). Customs query on the value of one of C1007's declarations. |
| Root cause | Duplicate invoice numbers from suppliers (vendor analysis) |
| Personal data involved | None (per vendor) |
| Customers affected | C1007 |
| Notifications | C1007: account manager call, 18 May |
| Legal | n/a |
| Customs | Queries handled by brokerage as usual |

**Timeline**

- 18 May 09:20 — call from C1007; ticket opened; vendor engaged.
- 18 May 15:40 — customs query on C1007 declaration confirmed; brokerage informed.
- 19 May 08:10 — "my documents" feature switched off in Tzir Assist.
- 21 May 14:00 — vendor hotfix 4.2.1 deployed.
- 22 May 11:20 — vendor reports no further mismatches; status set to contained at CEO's request.
- 28 May — vendor RCA received.

**Open actions:** none.
"""

RCA = """
# Root cause analysis — Tzir AI, 28 May 2027

**Customer:** Vantage Logistics. **Incident:** document mismatch in Tzir Docs (customer ref. INC-27-0518-01).

**Summary.** Between 3 and 20 May 2027, 42 declarations were pre-filled with a supplier invoice belonging to another shipment. The cause was duplicate invoice numbers issued by the customer's suppliers (consolidators in Shenzhen and Ningbo reuse numeric series).

**Contributing factor.** Release 4.2 (2 May) improved invoice-number normalisation to handle formatting variants in scanned invoices. This increased the match rate and, combined with duplicate supplier numbering, caused some invoices to match the wrong shipment.

**Corrective action.** Hotfix 4.2.1 (21 May) preserves alphabetic supplier prefixes in the matching key. No mismatches observed since.

**Personal data.** None. The affected documents are commercial invoices and packing lists.

**Recommendations to customer.** Ask suppliers to use unique invoice numbers; ensure licensed agents review every pre-filled declaration before submission, as required by the Tzir Docs user guide.
"""

RELEASE = """
# Tzir platform release 4.2 — release notes (published 2 May 2027)

Platform-wide maintenance release, deployed to all customers on Sunday 2 May 2027, 06:00.

**Tzir Docs**
- Improved invoice-number normalisation: non-alphanumeric characters and alphabetic prefixes are removed before matching, increasing the auto-match rate on noisy scans by 3.1% in our benchmark.
- Tariff classification model updated for the 2027 nomenclature changes.
- Faster attachment of supplier documents to the customer's file and portal.

**Tzir Route**
- Planner console: new colour scheme.

**Tzir Assist**
- Answers can now include links to documents attached to the customer's files.

*4.2.1 (21 May): matching key keeps alphabetic supplier prefixes.*
"""

WC_LETTER = """
# Works committee letter, 3 March 2027

*Original in Hebrew; English translation by HR below.*

לכבוד: מר עופר לביא, מנכ"ל; גב' ענת גולד, סמנכ"לית משאבי אנוש
הנדון: מצלמות בתאי הנהגים ו"ציון נהג" — דרישה להפסקה מיידית ולקיום היוועצות

1. בחודשים ינואר–פברואר הותקנו מצלמות "עין דרייב" ב-60 משאיות באזור הדרום, והופעל "ציון נהג" באפליקציית המסלולים בכל האזורים, ללא הודעה לוועד וללא היוועצות, בניגוד לסעיף 14 להסכם הקיבוצי.
2. ביום 24.2 זומן נהג לשימוע על בסיס נתוני "ציון נהג".
3. אנו דורשים: הפסקת השימוש במצלמות ובציון; התחייבות שנתונים אלה לא ישמשו להליכים משמעתיים; פגישה עם ההנהלה בתוך 14 יום.
4. ככל שלא יתקיים האמור, הוועד ישקול את צעדיו, לרבות הכרזה על סכסוך עבודה.

בכבוד רב, אבי אוחנה, יו"ר הוועד; טספאיה וורקו, נציג הנהגים

**Translation.** To Mr Ofer Lavi, CEO; Ms Anat Gold, VP HR. Re: cameras in drivers' cabs and the "driver score" — demand to stop immediately and to consult. (1) In January–February "Ayin Drive" cameras were installed in 60 trucks in the South and a "driver score" was switched on in the route app in all regions, without notice to the committee and without consultation, contrary to clause 14 of the collective agreement. (2) On 24 February a driver was summoned to a hearing on the basis of "driver score" data. (3) We demand: that the cameras and the score stop being used; an undertaking that this data will not be used in disciplinary proceedings; a meeting with management within 14 days. (4) Failing that, the committee will consider its steps, including declaring a labour dispute. Avi Ohana, chair; Tesfaye Worku, drivers' representative.
"""

AGREEMENT = """
# Collective agreement 2024–2027 — extract (clause 14, technology)

*Vantage Logistics and the employees' representative organisation; covers drivers, warehouse and customs staff in Israel. Valid to 31 December 2027.*

**14.1** Before introducing a technological means that monitors employees, measures an individual employee's performance, or materially changes working methods, the company will give the works committee written notice at least thirty days in advance, with the purpose of the means, the data collected, who may access it and for how long it is kept, and will consult with the committee in good faith.

**14.2** Data from such a means will not serve as a basis for disciplinary proceedings unless agreed in writing with the committee.

**14.3** Location data from vehicles is collected for operational and safety purposes; access is limited to dispatch, the transport safety officer and, on request, the employee.

**14.4** Disputes under this clause go first to a joint committee of two management and two employee representatives.
"""

GEFEN = """
# E-mail from Gefen Medical Distribution, 19 May 2027

**From:** Orit Ben-Shushan, VP Supply Chain, Gefen Medical Distribution Ltd.
**To:** Ronit Cohen-Elbaz (VP Customers, Vantage)
**Cc:** Gefen legal
**Subject:** Another importer's invoice in our portal — and our shipments held

Ronit,

Yesterday one of my planners opened a file in your portal and found the commercial invoice of a company we don't know, with their prices. The same day Customs at Haifa Port queried the value on two of our declarations and held the shipments; today a third is held. These are sterile consumables for hospitals.

I need, in writing, by Wednesday 26 May:
1. How another company's documents got into our file, and whether our invoices were shown to anyone else.
2. What was declared on our behalf, and what you are doing to correct it.
3. When our shipments will be released.

You know our tender for 2028–2030 opens in September. I would like to be able to recommend you.

Orit
"""


def build() -> dict:
    n = register()
    for rel, text in (("ai/handover-note-itai-barkan-2027-05-27.md", HANDOVER),
                      ("ai/tzir-route-model-card.md", MODEL_CARD),
                      ("ai/forecast-backtest-2027-04.md", FORECAST),
                      ("vendor/tzir-msa-extract.md", MSA), ("vendor/tzir-order-forms.md", ORDER_FORMS),
                      ("vendor/tzir-value-dashboard-2027-05.md", dashboard()),
                      ("incident/INC-27-0518-01-record.md", INCIDENT), ("incident/tzir-rca-2027-05-28.md", RCA),
                      ("incident/tzir-release-notes-4.2.md", RELEASE),
                      ("people/works-committee-letter-2027-03-03.md", WC_LETTER),
                      ("people/collective-agreement-extract.md", AGREEMENT),
                      ("customers/gefen-email-2027-05-19.md", GEFEN)):
        write_md(rel, text)
    return {"register": n, "docs-ai-vendor-incident": 12}
