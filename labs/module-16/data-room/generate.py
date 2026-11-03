"""Rebuild the Open Hands data room (module 16), byte for byte.

    python generate.py            # rebuilds every data file in this folder
    python generate.py --facts    # also prints the computed facts (for course writers)

Python 3.12+, standard library only. Seeded (20261115): every run writes identical files.
Reading this code (and common.py, textbank.py, people.py, cases.py, money.py, itaudit.py, stats.py,
docs1.py, docs2.py, docs3.py) spoils the engagement: finish module 16 first.
All people, families, organizations and vendors here are fictional.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True

import cases  # noqa: E402
import docs1  # noqa: E402
import docs2  # noqa: E402
import docs3  # noqa: E402
import itaudit  # noqa: E402
import money  # noqa: E402
import people  # noqa: E402
import stats  # noqa: E402


def main() -> None:
    staff = people.write_staff()
    vols = people.build_volunteers()
    people.write_volunteers(vols)
    tlog = people.build_time_log()
    survey = people.build_survey()
    fams = cases.build_cases()
    cases.write_cases(fams)
    notes = cases.build_notes(fams)
    funders = money.write_funders()
    donors = money.build_donors()
    card = money.build_card()
    money.write_accounts()
    audit = itaudit.build_audit(vols)
    facts = stats.compute(staff, vols, fams, notes, tlog, survey, donors, card, audit, funders)
    docs1.write(facts)
    docs2.write(facts)
    docs3.write(facts)
    if "--facts" in sys.argv:
        print(json.dumps(facts, ensure_ascii=False, indent=1))
    print("Open Hands data room written.")


if __name__ == "__main__":
    main()
