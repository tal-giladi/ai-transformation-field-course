# SmartStock AI and AutoRecon — configuration export

*Screens copied by Avi Mizrahi from the ERP add-ons, 20 October 2026, at the request of the COO for
"the AI list". Both add-ons are sold by Optimo Systems Ltd (fictional).*

## SmartStock AI — "AI-powered smart reorder"

Vendor banner on the login screen:

> **SmartStock AI** — Artificial intelligence that knows what you'll sell before you do.

### Settings → Replenishment rules (company level)

| Setting | Value |
|---|---|
| Review cycle | Weekly, Sunday 06:00 |
| Reorder trigger | Available stock + on order < **Min** |
| Order quantity | **Max** − (available stock + on order), rounded up to carton multiple |
| Min | Average weekly sales (last 13 weeks) × (supplier lead time in weeks + safety weeks) |
| Max | Min + average weekly sales × order cycle weeks |
| Safety weeks | Vietnam/China: 3 · Turkey: 2 · Italy: 2 |
| Seasonality factor | Manual, per month (set by Purchasing): Nov–Jan × 1.4, Aug–Sep × 1.2 |
| Exclusions | SKUs flagged "made to order" |
| Output | Suggested purchase orders for buyer approval in Priority |

### Settings → "AI insights"

| Setting | Value |
|---|---|
| Demand sensing | Not licensed |
| Anomaly alerts | Off |

### Buyer notes (Eyal Navon, in the comments field)

"We approve about 80% of the suggestions as they are. Seasonality factors updated every January."

## AutoRecon — "intelligent auto-match"

### Settings → Matching rules (applied in this order)

1. Exact amount + same date + bank reference contains invoice number → match.
2. Exact amount ± ₪1 within 3 days + customer name contains account name → match.
3. Same amount, several open invoices → leave for the accountant.
4. Anything else → unmatched list.

Match rate last month: 87% automatic, 13% manual.
