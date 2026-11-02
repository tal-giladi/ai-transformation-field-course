"""Lesson 08.5 (Track B): run the agent-assist pilot over the written tickets.

Three modes:
  rules    no model at all: keyword intent, keyword cues, the policy as rules, a template draft.
           Every LLM run is compared with it. Its numbers are exactly reproducible.
  llm      one call per ticket: the model reads the order facts and the message and returns intent,
           cues, decision, fee, escalation and a draft (system-prompt.md).
  hybrid   the model reads (intent and cues), the rules decide (pilot_lib.decide), the model writes
           the draft for that decision: two calls per ticket. The design lesson 08.4 recommends.

Sets (fixed split of the 2,000 tickets, see sets.py): dev (300, tune the prompt here), test (1,700,
score once per prompt version), track-a (the 200 test tickets used in the spreadsheet track),
negative (the 12 hand-written negative tests).

    python run_assist.py --mode rules --set test           # free, no key
    python run_assist.py --mode llm --set dev --limit 20   # first LLM calls
    python run_assist.py --mode hybrid --set test

Provider and model come from FIELDKIT_PROVIDER and FIELDKIT_MODEL (../../common/README.md).
FIELDKIT_PROVIDER=mock runs the whole pipeline without a key. Replies are cached in .fieldkit-cache/.
Output: runs/<mode>-<set>-<model>.csv; score it with score.py.
"""
import argparse
import csv
import os
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "common"))

from pilot_lib import (decide, item_prompt, keyword_intent, load_system_prompt, parse_reply, script_language,
                       template_draft, text_cues)
from sets import load_set

CUE_MAP = {"defect": "defect", "age_65_plus": "age", "new_immigrant": "immigrant", "disability": "disability",
           "legal_threat": "legal", "injury": "injury"}

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("--mode", choices=["rules", "llm", "hybrid"], default="rules")
ap.add_argument("--set", choices=["dev", "test", "track-a", "negative", "all"], default="test")
ap.add_argument("--limit", type=int, default=0)
ap.add_argument("--out")
args = ap.parse_args()

rows = load_set(args.set)
if args.limit:
    rows = rows[: args.limit]
if args.mode != "rules":
    from fieldkit.llm import DEFAULT_MODELS, complete
    provider = (os.environ.get("FIELDKIT_PROVIDER") or "anthropic").lower()
    model = os.environ.get("FIELDKIT_MODEL") or DEFAULT_MODELS.get(provider) or "unknown"
    system, version = load_system_prompt()
else:
    provider, model, version = "none", "rules", "rules-1.0"

out_rows = []
for i, row in enumerate(rows, 1):
    lang = script_language(row["message"])
    lang = lang if lang in ("he", "ar", "ru", "en", "am") else "he"
    tin = tout = 0
    if args.mode == "rules":
        intent = keyword_intent(row["message"])
        cues = text_cues(row["message"])
        decision, fee = decide(row, intent, cues)
        escalate = intent == "complaint_legal" or bool(cues & {"legal", "injury"}) or lang == "am"
        draft = template_draft(decision, lang, row, fee)
        reply_lang = lang if lang != "am" else "he"
        cue_list = sorted(cues)
    else:
        reply = complete(item_prompt(row), system=system)
        tin, tout = reply.input_tokens, reply.output_tokens
        data = parse_reply(reply.text)
        intent = data.get("intent", "other")
        cue_list = data.get("cues", [])
        escalate = bool(data.get("escalate"))
        reply_lang = data.get("reply_language", "")
        if args.mode == "llm":
            decision, fee, draft = data.get("decision", "n/a"), float(data.get("fee_ils") or 0), data.get("draft", "")
        else:  # hybrid: rules decide, the model writes the draft for that decision
            cues = {CUE_MAP[c] for c in cue_list if c in CUE_MAP}
            decision, fee = decide(row, intent, cues)
            ask = (f"{item_prompt(row)}\n\nDECISION (from Northwind's rules, do not change it): {decision}; "
                   f"fee {fee:g} shekels. Write only the draft reply text for the agent, in the customer's language.")
            r2 = complete(ask, system=system)
            tin, tout = tin + r2.input_tokens, tout + r2.output_tokens
            draft = r2.text.strip()
            escalate = escalate or decision == "escalate_counsel"
    out_rows.append([row["ticket_id"], intent, decision, f"{fee:.2f}", "y" if escalate else "n", " ".join(cue_list),
                     reply_lang, draft, tin, tout, provider, model, version,
                     "deterministic" if args.mode == "rules" else datetime.now().isoformat(timespec="seconds")])
    if i % 100 == 0:
        print(f"{i}/{len(rows)}")

(HERE / "runs").mkdir(exist_ok=True)
out = Path(args.out) if args.out else HERE / "runs" / f"{args.mode}-{args.set}-{model.replace('/', '_')}.csv"
with out.open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["ticket_id", "intent", "decision", "fee_ils", "escalate", "cues", "reply_language", "draft",
                "tokens_in", "tokens_out", "provider", "model", "prompt_version", "run_at"])
    w.writerows(out_rows)
print(f"{len(out_rows)} tickets -> {out}")
