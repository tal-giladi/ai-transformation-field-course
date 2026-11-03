"""Rebuild the Lumen SaaS data room, byte for byte.

    python generate.py

Python 3.12+, standard library only. Seeded (20261129): every run writes identical files.
Reading this code (and textbank.py, customers.py, beta.py, fleet.py, kb.py, docs1.py, docs2.py,
docs3.py) spoils the engagement: finish module 14 first.
All people, companies and products are fictional.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True

import beta  # noqa: E402
import customers  # noqa: E402
import docs1  # noqa: E402
import docs2  # noqa: E402
import docs3  # noqa: E402
import fleet  # noqa: E402
import kb  # noqa: E402
import stats  # noqa: E402


def main() -> None:
    custs = customers.build_customers()
    renewals = customers.build_renewals(custs)
    customers.write_customers(custs, renewals)
    customers.write_contracts(custs)
    customers.write_staff()
    customers.write_shifts()

    b = beta.build(custs)
    tickets = beta.build_tickets(custs, b)
    beta.write(b, tickets)

    b["rescue"] = fleet.build_rescue(custs)
    ledger = fleet.build_ledger(custs, b)
    fleet.write_fleet(custs, b, ledger)

    kb.write_kb()
    facts = stats.compute(custs, renewals, b, ledger)
    docs1.write(facts)
    docs2.write(facts)
    docs3.write(facts, custs, b)
    print("Lumen SaaS data room written.")


if __name__ == "__main__":
    main()
