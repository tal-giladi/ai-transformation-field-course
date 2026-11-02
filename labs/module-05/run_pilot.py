"""Lesson 05.3 (Track B): run the pilot (triage + draft reply) over a test set.

Two modes:
  llm       every item goes through fieldkit.llm.complete with the system prompt in system-prompt.md,
            and the JSON reply is parsed into category, language, flags and draft;
  baseline  no model at all: the keyword rules in pilot_lib.py and the alphabet of the message.
            Every LLM run is compared with it (05.4). Its numbers are exactly reproducible.

Run from this folder (build the sets first with build_test_set.py):
    python run_pilot.py --mode baseline --set test        # free, no key
    python run_pilot.py --set dev --limit 20              # try the prompt on 20 dev items first
    python run_pilot.py --set dev                         # tune the prompt on the 200 dev items
    python run_pilot.py --set test                        # then score it once on the 400 test items
    python run_pilot.py --set negative                    # the 24 hand-written negative tests

The provider and model come from FIELDKIT_PROVIDER and FIELDKIT_MODEL (see ../common/README.md).
FIELDKIT_PROVIDER=mock runs the whole pipeline without a key or network (it answers "other").
Replies are cached in .fieldkit-cache/, so re-running the same prompt on the same items is free.
The output goes to runs/<mode>-<set>-<model>.csv (or --out); score it with score.py.
"""
import argparse
import os
import sys
import time
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "common"))

import pandas as pd

from fieldkit.llm import DEFAULT_MODELS, complete
from pilot_lib import (LANGUAGES, item_message, keyword_classify, load_system_prompt, parse_reply,
                       script_language)

SETS = {"test": "test-set.csv", "dev": "dev-set.csv", "negative": "negative-tests.csv"}

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("--set", choices=SETS, default="dev")
ap.add_argument("--mode", choices=["llm", "baseline"], default="llm")
ap.add_argument("--limit", type=int, default=0, help="only the first N items (a cheap trial)")
ap.add_argument("--out", help="output CSV (default runs/<mode>-<set>-<model>.csv)")
args = ap.parse_args()

path = HERE / SETS[args.set]
if not path.exists():
    raise SystemExit(f"{path.name} not found: run  python build_test_set.py  first")
items = pd.read_csv(path, dtype=str, keep_default_na=False)
if args.limit:
    items = items.head(args.limit)

provider = (os.environ.get("FIELDKIT_PROVIDER") or "anthropic").lower()
model = os.environ.get("FIELDKIT_MODEL") or DEFAULT_MODELS.get(provider) or ""
system, version = load_system_prompt()
if args.mode == "baseline":
    provider, model, version = "baseline", "keywords-v1", "-"

rows = []
start = time.perf_counter()
for n, r in enumerate(items.to_dict("records"), 1):
    if args.mode == "baseline":
        lang = script_language(r["message"]) or script_language(r["subject"])
        category = keyword_classify(r["subject"], r["message"])
        out = {"label": category, "language": lang,
               "reply_language": lang if lang in LANGUAGES and category != "spam" else "none",
               "flags": "", "draft": "",
               "note_to_agent": "", "format_ok": True}
        tokens_in = tokens_out = 0
        seconds, cached = 0.0, False
    else:
        try:
            reply = complete(item_message(r), system=system, max_tokens=1200)
            out = parse_reply(reply.text)
            tokens_in, tokens_out = reply.input_tokens, reply.output_tokens
            seconds, cached = reply.seconds, reply.cached
            model = reply.model
        except Exception as exc:  # a failed call is a result too: keep going, count it
            out = {"label": "error", "language": "", "reply_language": "", "flags": "", "draft": "",
                   "note_to_agent": f"{type(exc).__name__}: {exc}"[:300], "format_ok": False}
            tokens_in = tokens_out = 0
            seconds, cached = 0.0, False
    rows.append({"item_id": r["item_id"], "category": out["label"], "language": out["language"],
                 "reply_language": out["reply_language"], "flags": out["flags"], "draft": out["draft"],
                 "note_to_agent": out["note_to_agent"], "format_ok": out["format_ok"],
                 "provider": provider, "model": model, "prompt_version": version,
                 "input_tokens": tokens_in, "output_tokens": tokens_out, "seconds": seconds,
                 "cached": cached})
    if n % 25 == 0 or n == len(items):
        print(f"  {n}/{len(items)} items", flush=True)

run = pd.DataFrame(rows)
run["run_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
out_path = Path(args.out) if args.out else HERE / "runs" / f"{args.mode}-{args.set}-{model or provider}.csv"
out_path.parent.mkdir(exist_ok=True)
run.to_csv(out_path, index=False, encoding="utf-8", lineterminator="\n")

print(f"\n{len(run)} items · mode {args.mode} · provider {provider} · model {model} · prompt v{version}")
print(f"Format errors: {int((~run['format_ok']).sum())} · call errors: {int((run['category'] == 'error').sum())}")
print(f"Tokens in/out: {int(run['input_tokens'].sum())} / {int(run['output_tokens'].sum())} · "
      f"cached replies: {int(run['cached'].sum())} · {time.perf_counter() - start:.1f} s")
print(f"Wrote {out_path.relative_to(HERE) if out_path.is_relative_to(HERE) else out_path}. "
      f"Next:  python score.py {out_path.name if out_path.parent == HERE / 'runs' else out_path}")
