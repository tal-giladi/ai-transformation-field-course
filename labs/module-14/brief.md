# Engagement brief: Lumen SaaS

All people, companies, customers and products are fictional.

## How you were brought in

You applied for a new role in October: **Head of AI Operations** at Lumen SaaS, a 250-person Tel Aviv
company that sells Lumen Shifts (shift scheduling, time clock and payroll prep) to about 3,100 business
customers in Israel, the EU and the US. Revital Azoulay, VP Support, hired you after two interviews and a
conversation with the CEO. You start on **Sunday 29 November 2026**. In Revital's words, from your last
interview:

> "Maya's team built something impressive. Yaron told the board it ships to everyone at Lumen Live in
> February and takes half our tickets by the summer. I believe in it. But it's my customers it talks to,
> and my people who clean up when it's wrong. I need someone who owns AI in operations: what it may do,
> how we know it's working, and what we do when it isn't."

You are an **employee**, not a consultant: there is no exit clause, you will own whatever you approve, and
the VP Product and the CISO are your peers, not your clients.

## The stated ask

The CEO's board update of 21 October 2026: "Ship Lumen Assist, an AI agent that resolves customer issues in
the product, to every customer at **Lumen Live on Tuesday 9 February 2027**; 50% of support contacts
resolved without a person by the end of Q2 2027." The VP Product's GA design gives the agent seven tools.
The executive staff decides the GA scope on **Wednesday 27 January 2027** and expects your "authority model"
there.

Revital's version, in your offer letter: "Make Lumen Assist safe to ship and worth shipping: decide what it
may do and prove it refuses what it must. Own every AI agent that touches a customer account."

## Terms

| Item | Terms |
|---|---|
| Role | Head of AI Operations, Support; reports to Revital Azoulay (VP Support) |
| Start | Sunday 29 November 2026; 90-day plan due to Revital by Thursday 10 December |
| Decision point | Executive staff, Wednesday 27 January 2027: GA scope for Lumen Live (9 February) |
| Budget, Dec 2026 – Mar 2027 | ₪380,000: a contract platform engineer for 12 weeks (₪210,000), an external red-team exercise (₪60,000), tooling and model usage (₪40,000), training for support shift leads (₪20,000), reserve (₪50,000). More needs the CFO. |
| Authority | You can pause Lumen Assist for a safety reason (with Revital). You cannot change the product roadmap, revoke other teams' tokens or change contracts; those need the owner. |
| People | Noam Levi (PM, Lumen Assist) on loan to you two days a week; the two support shift leads; one data analyst on request |

## Who you work with

Revital Azoulay (VP Support, your manager); Yaron Ben-David (CEO); Maya Rosenthal (VP Product, owns Lumen
Assist); Andrei Kogan (CISO); Nurit Gal (General Counsel and DPO); Oren Shalev (CFO); Michal Biton (Director
of Customer Success); Amir Haddad (commercial account lead for Shaked Clinics and Negev Retail Group).

## What you have on day one

- Read access to the data room (`data-room/`, start with `INDEX.md`): customer and billing extracts, the
  Lumen Assist beta's logs (11 October – 26 November), support tickets, IT's token list and admin audit log,
  the help centre's history, policies, product documents and an Enterprise customer's security questionnaire.
- Meetings Revital booked for week 1: Maya (Monday), Andrei (Tuesday), Yonatan Tadesse, tier-2 support
  engineer (Tuesday), Nurit (Wednesday). "The others when you're ready."
- Not yet: production systems (read-only access to the admin console is requested), the LLM provider's
  contract, any customer (Amir wants to "manage the Shaked relationship himself").

## Constraints you know about

- Lumen Live is on 9 February 2027; press and partners have been invited.
- Shaked Clinics, the largest Enterprise contract, renews on 31 March 2027; its security questionnaire is due
  15 January 2027.
- Hanukkah is 4–12 December 2026.
- You are not a lawyer. Privacy, the EU AI Act and customer contracts go to Nurit Gal (General Counsel and
  DPO). This course is not legal advice.

> [!WARNING]
> Lumen Assist can act on customer accounts: credits, plan changes, account security, deletion, emails with
> staff data. Everything in this module uses the synthetic data room, the simulation and a mock agent. Never
> run negative tests or red-team scripts against a live system or real customer accounts without written
> authorisation from the system's owner and security.
