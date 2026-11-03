"""Rebuild the Atlas & Rowe data room and the pilot files, byte for byte.

    python generate.py

Python 3.12+, standard library only. Seeded (20261115): every run writes identical files.
Reading this code (and textbank.py, firm.py, activity.py, signals.py, corpus.py, pilot.py, km.py,
documents.py) spoils the engagement: finish module 12 first.
All people, firms, clients, vendors and rulings are fictional.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True

import activity  # noqa: E402
import corpus  # noqa: E402
import documents  # noqa: E402
import firm  # noqa: E402
import km  # noqa: E402
import pilot  # noqa: E402
import signals  # noqa: E402


def clean() -> None:
    """Remove generated per-document files first, so renamed documents never linger."""
    here = Path(__file__).resolve().parent
    for folder in (here / "knowledge" / "corpus", here.parent / "pilot" / "drafts"):
        for f in folder.glob("*.md") if folder.exists() else []:
            f.unlink()


def main() -> None:
    clean()
    lawyers = firm.build_lawyers()
    clients = firm.build_clients()
    nda = firm.build_nda()
    matters = firm.build_matters(lawyers, clients, nda)
    time_rows = activity.build_time_entries(lawyers, matters)
    activity.set_2026_hours(lawyers)
    activity.write_time(time_rows)
    clients_by_code = firm.write_firm(lawyers, clients, matters, nda)
    signals.write_signals(lawyers, clients_by_code)

    docs = corpus.build_corpus()
    corpus.write_corpus(docs)
    km_rows = km.build_km(docs)
    km.write_km(km_rows)
    km_status = {row[0]: row[7] for row in km_rows}
    qs = pilot.build_questions(docs)
    pilot.write_questions(qs)
    pilot.write_curation(docs, km_status)
    labels, sheet = pilot.build_drafts(docs, qs)
    pilot.write_drafts(labels, sheet)

    documents.write_documents(lawyers, matters, nda, docs, clients_by_code)
    print("Atlas & Rowe data room and pilot files written.")


if __name__ == "__main__":
    main()
