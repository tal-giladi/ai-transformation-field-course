"""Rebuild Crescent Bank's data room byte for byte (Python 3.12+, standard library only).

    python generate.py

The other gen_*.py files in this folder are its parts. Reading them spoils the engagement: finish
module 15 first.
"""
import gen_docs
import gen_docs2
import gen_logs
import gen_people
import gen_register


def main() -> None:
    counts = {}
    for part in (gen_docs, gen_docs2, gen_register, gen_logs, gen_people):
        counts.update(part.build())
    for k, v in counts.items():
        print(f"{k:16s} {v}")


if __name__ == "__main__":
    main()
