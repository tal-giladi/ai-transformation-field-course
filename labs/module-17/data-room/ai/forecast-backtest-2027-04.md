# Warehouse demand and labour forecast — back-test (Lior Gabay, April 2027)

Model: weekly pallets per client and shift at Modi'in DC, gradient boosting on 3 years of WMS history, client promotions and holidays. Output: suggested labour plan per shift, which the supervisor adjusts.

| Back-test, 20 held-out weeks (2026) | Supervisor's spreadsheet | Model |
|---|---|---|
| Weekly pallet forecast error (MAPE) | 18.4% | 11.2% |
| Weeks with error above 25% | 6 | 1 |

Live since 3 January 2027 at Modi'in DC only. Ashdod DC still plans with the spreadsheet, so it is a fair comparison for overtime (`operations/warehouse-overtime-weekly.csv`).

Running it: I retrain monthly by hand and check the error on the last four weeks. No documentation beyond this page; the code is in my repository on the company cloud.
