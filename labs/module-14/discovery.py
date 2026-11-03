"""Discovery numbers for Lumen SaaS (Track B, lessons 14.2 and 14.3).

    python discovery.py

Prints: who acts as which identity in the audit log; credits by issuer; what the agent did with each help
article version; tool calls after the feature flag went off; emails to addresses not on the account;
the beta's resolution rate under two definitions; card expenses for AI and automation services; tokens
whose creator has left. Standard library only (plus fieldkit's data-room finder). Timestamps are Israel time.
"""
from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))

from fieldkit.data import data_room  # noqa: E402

ROOM = data_room("module-14")


def rows(rel: str) -> list[dict]:
    with (ROOM / rel).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def dt(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")


def identities(audit):
    print("\n== 1. Who acts as whom (admin audit log, 1 Sep - 26 Nov) ==")
    for (actor, ua), n in Counter((a["actor"], a["user_agent"]) for a in audit if a["actor_type"] == "token").most_common():
        hours = Counter(dt(a["timestamp"]).hour for a in audit if a["actor"] == actor and a["user_agent"] == ua)
        top = ", ".join(f"{h:02d}h" for h, _ in hours.most_common(3))
        print(f"{actor:20} {ua:28} {n:5} actions   busiest hours {top}")


def credits(ledger):
    print("\n== 2. Credits by issuer and note (2 Aug - 26 Nov) ==")
    g = defaultdict(lambda: [0, 0, 0])
    for c in ledger:
        key = c["issued_by"] if c["channel"] == "console" else f"api:{c['note'][:38]}"
        g[key][0] += 1
        g[key][1] += int(c["amount_ils"])
        g[key][2] = max(g[key][2], int(c["amount_ils"]))
    for k, (n, tot, mx) in sorted(g.items(), key=lambda x: -x[1][1])[:14]:
        print(f"{k:52} {n:4} credits  ₪{tot:>8,}  max ₪{mx:,}")
    big = [c for c in ledger if c["channel"] == "api" and int(c["amount_ils"]) > 500]
    print(f"API credits above ₪500: {len(big)}")
    for c in big:
        print(f"  {c['created_at']} {c['customer_id']} ₪{int(c['amount_ils']):,} {c['status']:9} run {c['invoice_run']}  {c['note'][:50]}")


def articles(revs, retr, calls, sessions):
    print("\n== 3. HC-214: versions and what the agent did ==")
    for r in revs:
        if r["article_id"] == "HC-214" and r["published_at"] >= "2025":
            print(f"  {r['language']} v{r['revision']} {r['published_at']} {r['published_by']:16} {r['change_note']}")
    hit = {r["session_id"] for r in retr if r["article_id"] == "HC-214"}
    sess = {s["session_id"]: s for s in sessions}
    cr = {c["session_id"]: c for c in calls if c["tool"] == "issue_credit"}
    print("  downgrade conversations that retrieved HC-214:")
    for sid in sorted(hit, key=lambda x: sess[x]["started_at"]):
        s = sess[sid]
        if s["intent"] != "account.downgrade":
            continue
        c = cr.get(sid)
        print(f"   {s['started_at']} {sid} {s['customer_id']} {s['language']}  "
              + (f"credit ₪{int(c['amount_ils']):,} executed {c['executed_at']}" if c else "no credit"))


def kill_switch(flags, calls):
    print("\n== 4. Feature flag vs tool execution ==")
    for f in flags:
        print(f"  {f['timestamp']} {f['flag']:24} {f['change']:13} {f['changed_by']}")
    off = next(dt(f["timestamp"]) for f in flags if f["change"] == "off")
    late = [c for c in calls if dt(c["requested_at"]) < off <= dt(c["executed_at"])]
    print(f"  tool calls requested before the flag went off and executed after it: {len(late)}")
    for c in late:
        print(f"   requested {c['requested_at'][11:]} executed {c['executed_at'][11:]} {c['tool']:15} {c['amount_ils'] or c['target']}")


def emails(calls, customers):
    print("\n== 5. Emails to addresses not on the account ==")
    own = {c["customer_id"]: c["admin_email"].split("@")[1] for c in customers}
    e = [c for c in calls if c["tool"] == "email_customer"]
    bad = [c for c in e if not c["target"].endswith("@" + own[c["customer_id"]])]
    print(f"  {len(bad)} of {len(e)} sends")
    for c in bad:
        print(f"   {c['executed_at']} {c['customer_id']} -> {c['target']}  ({c['note']})")


def resolution(sessions, tickets):
    print("\n== 6. Resolution: dashboard vs 7 days ==")
    n = len(sessions)
    dash = sum(1 for s in sessions if s["outcome"] != "handoff")
    later = defaultdict(list)
    for s in sessions:
        later[(s["customer_id"], s["intent"])].append(dt(s["started_at"]))
    for t in tickets:
        later[(t["customer_id"], t["category"])].append(dt(t["created_at"]))
    good = 0
    for s in sessions:
        if s["outcome"] in ("closed_by_customer", "abandoned"):
            t0 = dt(s["started_at"])
            if not any(t0 < x <= t0 + timedelta(days=7) for x in later[(s["customer_id"], s["intent"])]):
                good += 1
    print(f"  sessions {n}; dashboard 'resolved by Assist' {100 * dash / n:.1f}%; "
          f"no handoff, no ticket and no repeat on the same intent within 7 days {100 * good / n:.1f}%")
    print("  outcomes:", dict(Counter(s["outcome"] for s in sessions)))
    print("  languages:", dict(Counter(s["language"] for s in sessions)))
    print(f"  sessions with PII flags: {sum(1 for s in sessions if s['pii_flags'])}")


def fleet(tokens, staff, expenses, inventory):
    print("\n== 7. Tokens, people and spend ==")
    left = {s["email"].split("@")[0]: s["left_date"] for s in staff if s["status"] == "left"}
    for t in tokens:
        flag = f"creator left {left[t['created_by']]}" if t["created_by"] in left else ""
        print(f"  {t['token_id']} {t['name']:22} by {t['created_by']:14} {t['scopes'][:60]:60} {flag}")
    print("  AI and automation vendors on cards (Jan-Nov):")
    g = defaultdict(int)
    for e in expenses:
        g[(e["department"], e["vendor"], e["description"])] += int(e["amount_ils"])
    for (d, v, desc), tot in sorted(g.items()):
        print(f"   {d:17} {v:18} {desc:45} ₪{tot:,}")
    print(f"  IT inventory lists {len(inventory)}: " + "; ".join(i["system"] for i in inventory))


def main() -> None:
    audit, ledger = rows("it/admin-audit-log.csv"), rows("billing/credits-ledger.csv")
    calls, sessions = rows("assist-beta/tool-calls.csv"), rows("assist-beta/sessions.csv")
    identities(audit)
    credits(ledger)
    articles(rows("support-kb/help-centre-revisions.csv"), rows("assist-beta/retrievals.csv"), calls, sessions)
    kill_switch(rows("it/feature-flags-log.csv"), calls)
    emails(calls, rows("customers/customers.csv"))
    resolution(sessions, rows("support/tickets.csv"))
    fleet(rows("it/api-tokens.csv"), rows("people/staff-directory.csv"), rows("it/saas-expenses-ai-2026.csv"),
          rows("it/ai-inventory-2026-09.csv"))


if __name__ == "__main__":
    main()
