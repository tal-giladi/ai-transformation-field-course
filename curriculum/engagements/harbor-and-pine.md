# Harbor & Pine — writer's notes (never imported)

The warm-up organization for Stage 1 (modules 1–7). Every Stage 1 lesson practises on it. The data
room lives in `labs/common/harbor-and-pine/` so every module zip includes it.

## The company

- **Harbor & Pine Ltd.** (הארבור אנד פיין בע"מ), furniture and home-goods importer, founded 2009.
  ~120 employees. Revenue ~₪96M (2025). Imports from Vietnam, China, Turkey and Italy by sea
  container (Haifa and Ashdod ports). Sells B2C (website + showrooms in Tel Aviv and Haifa, ~70% of
  revenue) and B2B (hotels, offices, ~30%).
- Sites: head office and warehouse in Rishon LeZion; showrooms in Tel Aviv and Haifa.
- Systems: Priority ERP (orders, stock, purchasing); a cloud helpdesk ("Deskly", fictional) for
  support email and web form; a cloud phone system (call logs); Shopify-like web store ("StoreHub",
  fictional); Google Workspace; an HR SaaS ("PeopleWise", fictional) that added an "AI candidate
  match" feature in an auto-update in March 2026; a shipping-tracking spreadsheet the logistics team
  keeps by hand from the freight forwarder's emails. IT is one person plus an outside MSP.
- No works committee (too small and not unionised); labour law still applies.

## Who the learner is

Michal Peretz (COO) hired the learner as "Head of AI and Operations Improvement", reporting to her,
start date Sunday 2 November 2026. The CEO, Yoav Ben-Ami (founder's son), came back from a
conference and told the board in September: "we'll have an AI customer-service bot and an AI
strategy within 90 days, and cut support cost by 40%". The board meets on 28 January 2027.

## Stated ask vs hidden truth

- **Stated ask (CEO):** a chatbot that replaces a big part of the 14-person support team, and an AI
  strategy for the board.
- **Hidden truth:** ~38% of support contacts are "where is my order?" (WISMO). They are caused by the
  delivery date promised at checkout, which comes from a fixed lead-time table in the web store and is
  never updated when a container is delayed. Logistics knows the real ETAs (in their tracking
  sheet) but nobody tells customers. The biggest, cheapest win is plain automation: a daily job that
  compares promised dates with container ETAs and emails customers proactively — no AI. A chatbot
  would answer WISMO with the same wrong date.
- The AI pilot that does make sense (module 5): support-email triage + draft replies for the
  remaining categories (damage claims, assembly questions, returns, B2B quotes), in Hebrew, Arabic,
  Russian and English, with a human sending every reply.
- **Second hidden layer:** support agents already use free ChatGPT to draft replies, pasting customer
  names, phone numbers and addresses (a privacy problem under the Privacy Protection Law and its
  Amendment 13). They do it because it saves time on Russian and Arabic replies. The lead (Olga) is
  the best agent on the team and the secret enthusiast — punish her and you lose the pilot's best ally.

## Planted findings (each must be discoverable from the data, never stated)

1. WISMO share ~38% of tickets; spikes follow container delays in `shipments.csv` by 3–10 days.
2. Promised delivery dates in `orders.csv` come from a fixed lead time per supplier country;
   actual delivery lags by a median of 11 days for Vietnam/China orders since June 2026.
3. Three baselines for "first response time": helpdesk export (median ~6.5 business-and-weekend
   hours… compute from timestamps), the CEO's KPI report (says "2 hours", business hours only,
   excludes the web form channel and weekends), the phone-system log (answered calls, minutes).
4. The helpdesk status "resolved" is set by the agent when they send a reply, not when the issue is
   solved; ~22% of "resolved" tickets get a follow-up from the same customer within 14 days
   (a new ticket, not a reopen — find by customer_id + order_id).
5. Category field: ~28% "Other/כללי"; categories were redefined on 1 July 2026 (old "Delivery" split
   into "Delivery status" and "Delivery damage") — a report definition change.
6. Duplicates: ~6% of tickets are the same customer emailing twice within an hour.
7. Damage claims: approval outcome recorded only in `damage-claims-log.csv`, kept by one person
   (Rina), missing for ~35% of claims (outcome never recorded → not a training label).
8. The handbook says "damage claims are reviewed by QA within 48 hours"; there is no QA role and no
   such step in the data (a step that exists only on paper).
9. Stale copy: `catalog/products-2023-shared-drive-copy.csv` on the shared drive; the ChatNest demo
   was built on it (wrong prices, discontinued items).
10. Shadow AI: proxy log shows chat.openai.com/chatgpt.com, gemini, claude.ai, deepl, a "Grammarly"
    extension, and an AI copy SaaS; expenses show "CopyGenie Pro" and ChatGPT Plus on personal cards
    (marketing, one buyer); browser-extension inventory shows an AI translation extension on 9
    machines; the HR SaaS release notes show the AI candidate-match feature turned on by default.
11. Counting rule trap: the ERP's "smart reorder" is a rules engine (min/max thresholds) marketed as
    AI; the accounting "auto-match" is rules. Not AI for the inventory.
12. Time sheets: support agents log time in three coarse buckets; the "email" bucket is
    ~70% of logged time; the team is at ~92% utilisation in Nov–Jan (peak season).
13. Finance: support cost ~₪3.4M/yr fully loaded; CFO's hurdle rate 12%; any project above
    ₪150k needs board approval.
14. The flawed AI-drafted findings memo (for 02.7) says WISMO is 15% (it counted only the new
    category since July), cites a "Gartner 2025 study" that does not exist, and misreads the KPI
    report's 2-hour figure as the median.
15. The previous consultant's roadmap (for 07.7) puts the chatbot first, assumes 70% deflection from
    the vendor deck, has no gates, and schedules everything in Q1 during peak season.

## The cast (persona pack)

| Persona | Role | Type | Hidden / unlock |
|---|---|---|---|
| Yoav Ben-Ami | CEO | sponsor's boss, board-facing | Already told the board "40%"; unlock: ask what he told the board, privately |
| Michal Peretz | COO, the sponsor | sponsor | Worried logistics is the real problem; unlock: ask what keeps her up at night about delivery |
| Ronit Avraham | CFO | sceptic, finance | Has a hurdle rate and template; burned by a 2022 CRM project; unlock: ask how the last big project was judged |
| Samir Haddad | Customer Service Manager | middle manager | Knows WISMO is the top driver; afraid of headcount cuts; unlock: promise of no attribution + ask for a normal day |
| Olga Petrenko | Senior support agent | frontline, secret enthusiast | Uses ChatGPT daily with customer data; unlock: show you are not hunting people, ask how she writes Russian replies so fast |
| Avi Mizrahi | IT manager (one-person IT) | IT/security | Knows the proxy shows AI sites; never acted; unlock: ask what the proxy logs |
| Tamar Shalev | Logistics manager | data steward / receiving team | Keeps the ETA sheet; knows promised dates are wrong; nobody asked; unlock: ask where ETA updates go |
| Noa Levi | Marketing director | process owner who adds scope | Keeps adding "while you're at it" items; uses CopyGenie on a personal card |
| Dana Katz | HR manager | HR, workforce | Didn't know the AI candidate match was turned on; worried about training time in peak season |
| Eitan Gross | ChatNest account executive | vendor AE | The 70% deflection was measured on US English retail with order tracking integrated |

Lessons that use them: 01.2 (Michal), 01.3 (Noa), 02.2 (Samir, Olga, Tamar), 03.5–03.6 (Yoav,
Ronit, Michal, Samir), 03.9 (Yoav), 04.8 (Eitan), 06.6 (Samir, Olga, Dana), 07.3 (Yoav), 07.4 (all
seniors).

## Timeline (data dates)

- Tickets, emails, orders, shipments: 1 May 2026 – 31 October 2026.
- Pilot usage export (06.4): weeks 1–8 after a pilot start of 1 February 2027 (synthetic future).
- Learner starts 2 November 2026. Board: 28 January 2027.
