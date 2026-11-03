"""Firm documents built from the generated data: profile, org chart, finance summary, partners' minutes,
the research memo with reviewers' comments. Policies, client and vendor documents are in documents2.py."""
from __future__ import annotations

from collections import defaultdict

import documents2
from common import ROOM, fill, ils, write_md

M = 1_000_000


def _finance(matters):
    by_type = defaultdict(lambda: [0, 0, 0, 0])
    by_group = defaultdict(lambda: [0, 0, 0, 0])
    for m in matters:
        for agg in (by_type[m["type"]], by_group[m["group"]]):
            agg[0] += m.get("b25", 0); agg[1] += m.get("wv25", 0)
            agg[2] += m.get("b26", 0); agg[3] += m.get("wv26", 0)
    tot = [sum(v[i] for v in by_type.values()) for i in range(4)]
    return by_type, by_group, tot


def write_documents(lawyers, matters, nda, docs, clients_by_code) -> None:
    by_type, by_group, tot = _finance(matters)
    assoc = [l for l in lawyers if l["role"] == "associate"]
    a25 = sum(l["h2025"] for l in assoc) / len(assoc)
    a26 = sum(l["h2026"] for l in assoc) / len(assoc) * 12 / 9
    v = {"billed25": f"{tot[0] / M:.1f}", "worked25": f"{tot[1] / M:.1f}", "real25": f"{100 * tot[0] / tot[1]:.0f}",
         "billed26": f"{tot[2] / M:.1f}", "real26": f"{100 * tot[2] / tot[3]:.0f}",
         "a25": f"{a25:,.0f}", "a26": f"{a26:,.0f}", "util": f"{100 * a26 / 1850:.0f}"}
    v["type_rows"] = "\n".join(
        f"| {t} | {ils(b[0])} | {100 * b[0] / tot[0]:.0f}% | {100 * b[0] / b[1]:.0f}% | {ils(b[2])} | {100 * b[2] / b[3]:.0f}% |"
        for t, b in sorted(by_type.items(), key=lambda x: -x[1][0]))
    v["group_rows"] = "\n".join(
        f"| {g} | {ils(b[0])} | {100 * b[0] / b[1]:.0f}% | {ils(b[2])} | {100 * b[2] / b[3]:.0f}% |"
        for g, b in sorted(by_group.items(), key=lambda x: -x[1][0]))

    write_md(ROOM / "firm" / "firm-profile.md", fill(PROFILE, v))
    write_md(ROOM / "firm" / "finance-summary-2026.md", fill(FINANCE, v))
    write_md(ROOM / "firm" / "partners-meeting-2026-10-22-minutes.md", fill(MINUTES, v))

    lines = ["# Atlas & Rowe — people by practice group", "",
             "HR summary, 1 November 2026. Lawyers only; interns and staff are counted at the end. "
             "Full list with hours and rates: `people/lawyers.csv`.", ""]
    for g in ["Corporate", "Litigation", "Real estate", "Banking & finance", "Tech & IP", "Employment"]:
        ls_ = [l for l in lawyers if l["group"] == g]
        ps = [l for l in ls_ if l["role"] != "associate"]
        intl = [l for l in ls_ if l["desk"] == "International"]
        lines += [f"## {g}", "", f"{len(ps)} partners, {len(ls_) - len(ps)} associates"
                  + (f" (International desk: {len(intl)} lawyers, English work product)" if intl else "") + ".", "",
                  "| Partner | Role | Desk |", "|---|---|---|"]
        lines += [f"| {p['name']} ({p['id']}) | {p['role'].replace('_', ' ')} | {p['desk'] or '—'} |" for p in ps]
        lines.append("")
    lines += ["## Management and support", "",
              "- Managing partner: Adv. Yoav Dagan (since 2021). Management committee: Yoav Dagan, Shmuel Atlas, "
              "Noa Friedman, Orit Levinson, Eli Ben-Hamo (finance director, non-voting).",
              "- General counsel and ethics partner: Adv. Orit Levinson.",
              "- Knowledge management: Adv. Tamar Golan (0.6 FTE). The librarian post has been vacant since March 2026.",
              "- Finance 6, IT 2 (with a managed service provider), secretariat 22, other staff 19, interns 11."]
    write_md(ROOM / "firm" / "org-chart.md", "\n".join(lines))

    nc = [d for d in docs if d.topic == "non-compete"]
    r_old = next(d for d in nc if d.kind == "ruling" and d.superseded_by)
    r2 = next(d for d in nc if d.id == r_old.superseded_by)
    r1 = next(d for d in nc if d.kind == "ruling" and any(k == "non-compete:P2" for _, k in d.paras))
    r3 = next(d for d in nc if d.kind == "ruling" and any(k == "non-compete:P4" for _, k in d.paras))
    matter = next(m for m in sorted(matters, key=lambda x: x["id"])
                  if m["partner"] == "L002" and m["opened"] == 2026 and m["type"] == "hourly")
    write_md(ROOM / "research" / "memo-non-compete-draft-v2.md",
             fill(MEMO, {"r_old": r_old.id, "r2": r2.id, "r1": r1.id, "r3": r3.id, "matter": matter["id"], "client": matter["client"]}))
    documents2.write(v, nda, clients_by_code)


PROFILE = """
# Atlas & Rowe, Advocates — firm profile

From the firm's welcome pack for new lawyers (updated September 2026).

Atlas & Rowe (אטלס אנד רואו, עורכי דין) is a Tel Aviv commercial law firm founded in 1994 by Avraham
Atlas and David Rowe. Offices on Menachem Begin Road. 90 lawyers (26 partners, 64 associates), 11
interns and about 50 staff.

**Practice groups.** Corporate and M&A (with the International desk for foreign investors, working in
English), commercial litigation, real estate, banking and finance, technology and IP, employment.

**Clients.** Israeli companies (retail, insurance, banking, technology, real estate), foreign funds and
investors, start-ups (fixed-fee packages from the Tech & IP group). Work in Hebrew and English; lawyers
also speak Arabic, Russian and French.

**How we bill.** Hourly at the firm's rates, capped budgets, fixed fees and monthly retainers. 2025
fees billed: ₪{{billed25}}M.

**Systems.** Documents in the DMS ("Archive"), time in TimeLedger, precedents in the precedent bank
(Mikbatz, inside Archive). Email and Office. Internet through the managed service provider's proxy.

**Values.** "Partners' judgement on every file." Every client document is confidential; ethical walls
are set in Archive by the risk team.
"""

FINANCE = """
# Finance summary for the management committee

Prepared by Eli Ben-Hamo, finance director, 28 October 2026. Figures from TimeLedger; 2026 is January
to September. Matter-level data: `billing/matters.csv`.

## Fees and realisation

2025: fees billed ₪{{billed25}}M; worked value (hours × standard rates) ₪{{worked25}}M; realisation {{real25}}%.
2026, January–September: fees billed ₪{{billed26}}M; realisation {{real26}}%.

| Billing type | Billed 2025 | Share | Realisation 2025 | Billed Jan–Sep 2026 | Realisation 2026 |
|---|---|---|---|---|---|
{{type_rows}}

| Practice group | Billed 2025 | Realisation 2025 | Billed Jan–Sep 2026 | Realisation 2026 |
|---|---|---|---|---|
{{group_rows}}

Realisation on fixed fees = fee ÷ worked value; below 100% means more hours than the fee pays for.

## Hours

Associates' billable target: 1,850 hours. Average recorded: {{a25}} in 2025; {{a26}} in 2026 so far
(annualised), about {{util}}% of target. Partners' targets: 1,400 (equity), 1,600 (salaried).

## Partner compensation (summary)

Modified lockstep. 70% of points by seniority; 30% "contribution", half of which is the partner's own
billed hours and half origination and management. Points are reviewed each January.

## Requests for the 2027 budget

| Request | From | Amount | Comment |
|---|---|---|---|
| Parshan AI licence, 90 seats, 24 months | N. Friedman | US$103,680 a year after the 20% launch discount + US$25,000 set-up (≈ ₪403,000 in year 1 at ₪3.136) | Cost only; no revenue effect modelled |
| Knowledge management: librarian post | T. Golan | ₪240,000 a year | Deferred in 2025 and 2026 |
| IT: DLP upgrade | IT | ₪60,000 | |
"""

MINUTES = """
# Partners' meeting — minutes (extract)

Thursday 22 October 2026, 18:00–20:30, boardroom. Chair: Yoav Dagan (managing partner). Present: 24
of 26 partners. In attendance: Eli Ben-Hamo (finance), Tamar Golan (knowledge management, item 3).

## 1. Third-quarter figures (E. Ben-Hamo)

Fees billed January–September ₪{{billed26}}M; realisation {{real26}}%. Associates' hours about {{util}}% of target.
Litigation lost the panel tender of an insurance client in September (A. Mor: "lost on price").

## 2. Artificial intelligence (N. Friedman, S. Atlas, O. Levinson)

N. Friedman presented Parshan AI (demo to partners on 8 October). Her slide: "Lawyers save 6.2 hours a
week. 6.2 h × 90 lawyers × 44 weeks × ₪950 = ₪23.3M of capacity a year, for ₪0.4M." Launch discount of
20% if the firm signs by 31 December 2026. "The large firms have all bought something. Our associates
use ChatGPT anyway; better a safe tool."

S. Atlas objected: these tools invent cases ("the American lawyers fined for ChatGPT cases, and now
our own Supreme Court"); client confidentiality; "our clients pay for judgement, not for speed. If we
work faster on hourly files, we bill less."

O. Levinson: the Bar Association's ethics committee published an expanded opinion on lawyers' use of
AI in September; the firm has no AI policy, and one client has sent outside-counsel guidelines with an
AI clause. A firm-wide rule is needed whatever is decided about Parshan.

Straw poll on "sign Parshan before 31 December": 11 in favour, 9 against, 4 abstaining.

**Decided:** the managing partner will engage an outside consultant to advise the partnership; vote at
the partners' meeting on Thursday 14 January 2027. N. Friedman to circulate a draft AI policy.

## 3. Knowledge management (T. Golan)

T. Golan asked again for the librarian post and for time to review the precedent bank ("people are
using templates nobody has checked since 2019"). Deferred to the 2027 budget discussion.
"""

MEMO = """
# Research memo — draft v2 (with reviewers' comments)

Exported from Archive with comments, 4 November 2026, at the consultant's request (client name removed).

| Field | Value |
|---|---|
| Matter | {{matter}} (client [{{client}}]) |
| To | S.A. |
| From | Y.P. (International desk, lent to litigation for this matter) |
| Created | 19 October 2026 22:58 |
| Last saved | 19 October 2026 23:40 |

**Question.** Can our client enforce the 24-month non-compete in its former sales manager's employment
agreement and obtain an interim injunction?

**Short answer.** Yes, the prospects are good.

1. Courts enforce a two-year non-compete against a sales manager who signed it knowingly
   [{{r_old}} ¶3].
2. In FCR-2022-318 the court granted an injunction against a former regional manager who had received
   a retention bonus, holding that the bonus was consideration for the restriction [FCR-2022-318 ¶6].
3. Paying special consideration for the restriction makes the non-compete valid [{{r1}} ¶5]. Our
   client paid a signing bonus of ₪40,000.
4. A non-solicitation clause limited to the customers the employee served is more readily enforced
   than a general non-compete [{{r3}} ¶3]; the agreement has one, as a fallback.

**Recommendation.** File for an interim injunction this week.

---

**Comments**

- ש.א., 20.10.2026 08:12: "טוב. לשלוח ללקוח היום." *(Good. Send to the client today.)*
- K.N., 20.10.2026 09:41: "Holding the email. I can't find FCR-2022-318 in Mikbatz or anywhere else.
  {{r_old}} was reversed on appeal in {{r2}}. Point 3 says the opposite of {{r1}} ¶5. Let's talk before
  anything goes out."
- ש.א., 20.10.2026 11:05: "תתקנו ותשלחו." *(Fix it and send.)*
"""
