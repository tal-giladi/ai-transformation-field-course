"""Rebuild Vantage Logistics' data room byte for byte (Python 3.12+, standard library only).

    python generate.py

The other gen_*.py files in this folder are its parts. Reading them spoils the engagement: finish
module 17 first.
"""
import gen_customs
import gen_docs1
import gen_docs2
import gen_finance
import gen_it
import gen_ops
import gen_portal


def main() -> None:
    counts = {}
    # gen_docs2 reads the route file written by gen_ops, so ops comes first.
    for part in (gen_ops, gen_customs, gen_portal, gen_finance, gen_it, gen_docs1, gen_docs2):
        counts.update(part.build())
    for k, v in counts.items():
        print(f"{k:24s} {v}")


if __name__ == "__main__":
    main()
