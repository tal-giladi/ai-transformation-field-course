"""Rebuild the Tzurim Academic College data room (module 18, the capstone) byte for byte.

    python generate.py

Python 3.12+, standard library only. Writes every file in this folder's subfolders. Reading the
generator spoils the capstone: submit your deliverables first.
"""
from __future__ import annotations

import csv
import sys

sys.dont_write_bytecode = True
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gen_common import COHORTS, ROOM  # noqa: E402
import gen_docs  # noqa: E402
import gen_docs2  # noqa: E402
import gen_it  # noqa: E402
import gen_ops  # noqa: E402
import gen_students  # noqa: E402


def report_figures(students: list[dict]) -> dict:
    """First-year 'dropout' as the registrar's 2019 report query computes it."""
    counted_active = {"10", "21", "41", "60"}
    out = {}
    for cohort in COHORTS:
        group = [s for s in students if s["cohort"] == cohort]
        gone = sum(1 for s in group if s["y1"] not in counted_active)
        out[cohort] = (len(group), round(100 * gone / len(group), 1))
    progs = {}
    for s in students:
        if s["cohort"] == 2025:
            n, g = progs.get(s["prog"], (0, 0))
            progs[s["prog"]] = (n + 1, g + (s["y1"] not in counted_active))
    out["by_programme_2025"] = {k: (n, round(100 * g / n, 1)) for k, (n, g) in sorted(progs.items())}
    return out


def main() -> None:
    students = gen_students.build()
    gen_ops.inquiries(students)
    first = gen_ops.lms_and_scores(students)
    gen_ops.red_list_and_contacts(students, first)
    gen_it.build()
    figures = report_figures(students)
    gen_docs.build(figures)
    gen_docs2.build()
    n = sum(1 for p in ROOM.rglob("*") if p.is_file() and p.suffix in (".csv", ".md") and p.name != "INDEX.md")
    size = sum(p.stat().st_size for p in ROOM.rglob("*") if p.is_file())
    print(f"Wrote {n} data files; folder size {size / 1e6:.2f} MB")
    for cohort in COHORTS:
        n_c, pct = figures[cohort]
        print(f"  cohort {cohort}: {n_c} students, report figure {pct}%")


if __name__ == "__main__":
    main()
