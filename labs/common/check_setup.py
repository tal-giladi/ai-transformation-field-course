"""Check that the Python track is ready: Python version, packages, and (optionally) your LLM.

    python check_setup.py          # no network, no cost
    python check_setup.py --llm    # also sends one tiny prompt to your provider (costs a fraction of a cent)
"""
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ok = True
if sys.version_info < (3, 12):
    print(f"Python {sys.version.split()[0]}: please use 3.12 or newer")
    ok = False
else:
    print(f"Python {sys.version.split()[0]}: ok")

for name in ("pandas", "tabulate", "matplotlib", "yaml"):
    try:
        module = importlib.import_module(name)
        print(f"{name} {getattr(module, '__version__', '')}: ok")
    except ImportError:
        print(f"{name}: missing - run: python -m pip install -r requirements.txt")
        ok = False

from fieldkit.data import data_room  # noqa: E402

try:
    print(f"Harbor & Pine data room: {data_room('harbor-and-pine')}")
except FileNotFoundError as exc:
    print(exc)
    ok = False

if "--llm" in sys.argv:
    from fieldkit.llm import complete

    reply = complete("Reply with the single word: ready", max_tokens=200, cache=False)
    print(f"LLM {reply.provider}/{reply.model}: {reply.text.strip()!r} "
          f"({reply.input_tokens} in, {reply.output_tokens} out, {reply.seconds}s)")

print("All set." if ok else "Fix the lines above, then run this again.")
