"""First-day data-room read (lesson 01.5), Track B.

Lists every CSV in a data room with its row count, columns, the date range it covers and the share
of blank cells, so you can fill the "What is here" part of the data-room first read in minutes
instead of opening 25 files one by one. It does not judge the data: that is your job.

Run from this folder:
    python first_read.py                      # Harbor & Pine
    python first_read.py module-08            # another data room
    python first_read.py --csv first-read.csv # also save the table as CSV
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))

import pandas as pd  # noqa: E402

from fieldkit.data import data_room, load  # noqa: E402


def describe(path: Path, room: Path) -> dict:
    df = load(path)
    dates = [c for c in df.columns if pd.api.types.is_datetime64_any_dtype(df[c])]
    first = last = ""
    if dates:
        lo = min(df[c].min() for c in dates if df[c].notna().any())
        hi = max(df[c].max() for c in dates if df[c].notna().any())
        first, last = lo.date().isoformat(), hi.date().isoformat()
    cells = df.shape[0] * df.shape[1]
    blank = float(df.isna().sum().sum()) / cells if cells else 0.0
    return {
        "file": path.relative_to(room).as_posix(),
        "rows": len(df),
        "columns": df.shape[1],
        "date_columns": ", ".join(dates) or "(none parsed)",
        "first_date": first,
        "last_date": last,
        "blank_cells_%": round(100 * blank, 1),
        "header_sample": ", ".join(map(str, df.columns[:6])),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("room", nargs="?", default="harbor-and-pine")
    parser.add_argument("--csv", help="also write the table to this CSV file")
    args = parser.parse_args()

    room = data_room(args.room)
    rows = [describe(p, room) for p in sorted(room.rglob("*.csv")) if "personas" not in p.parts]
    table = pd.DataFrame(rows)
    with pd.option_context("display.max_rows", None, "display.max_columns", None, "display.width", 200):
        print(table.drop(columns=["header_sample"]).to_string(index=False))
    docs = sorted(p.relative_to(room).as_posix() for p in room.rglob("*.md") if "personas" not in p.parts)
    print(f"\n{len(rows)} CSV files, {len(docs)} documents:")
    for d in docs:
        print("  ", d)
    print("\nHeaders that are not English (hand-kept files, worth a closer look):")
    for r in rows:
        if any(ord(ch) > 127 for ch in r["header_sample"]):
            print("  ", r["file"], "->", r["header_sample"])
    if args.csv:
        table.to_csv(args.csv, index=False, encoding="utf-8")
        print(f"\nSaved {args.csv}")


if __name__ == "__main__":
    main()
