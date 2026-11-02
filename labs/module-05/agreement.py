"""Lesson 05.2 (Track B): how far do two labellers agree?

    python agreement.py my-labels.csv                     # you vs the team's adjudicated labels
    python agreement.py olga.csv yana.csv                 # labeller A vs labeller B

Each file needs `item_id` and a category column (`your_category`, or `category`); fill
labelling-sample-40.csv (written by build_test_set.py) to make yours. Prints the share of items on
which the two agree, Cohen's kappa (agreement corrected for the agreement you would get by chance
from each labeller's category mix), the confusion pairs and the items to adjudicate.
No API key, no network.
"""
import sys
from collections import Counter
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent


def read(path: str) -> pd.Series:
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    col = next(c for c in ("your_category", "category", "expected_category") if c in df.columns)
    key = "item_id" if "item_id" in df.columns else "email_id"
    return df.set_index(key)[col].str.strip().str.lower()


if len(sys.argv) not in (2, 3):
    raise SystemExit(__doc__)
a = read(sys.argv[1])
if len(sys.argv) == 3:
    b, b_name = read(sys.argv[2]), Path(sys.argv[2]).stem
else:  # compare with the adjudicated labels, by test-set item id
    test = pd.read_csv(HERE / "test-set.csv", dtype=str, keep_default_na=False)
    b, b_name = test.set_index("item_id")["expected_category"], "adjudicated labels"
pairs = pd.DataFrame({"a": a, "b": b}).dropna()
pairs = pairs[(pairs["a"] != "") & (pairs["b"] != "")]
if pairs.empty:
    raise SystemExit("No item has a label in both files: fill the category column first.")

n = len(pairs)
observed = (pairs["a"] == pairs["b"]).mean()
pa, pb = Counter(pairs["a"]), Counter(pairs["b"])
expected = sum(pa[c] * pb[c] for c in set(pa) | set(pb)) / n ** 2
kappa = (observed - expected) / (1 - expected) if expected < 1 else 1.0

print(f"Items labelled by both: {n}")
print(f"Agreement: {100 * observed:.1f}%  (disagreement rate {100 * (1 - observed):.1f}%)")
print(f"Cohen's kappa: {kappa:.2f}  (chance agreement {100 * expected:.1f}%)")
print("Rough reading: above 0.8 the category definitions work; 0.6-0.8 fix the definitions where the "
      "pairs below cluster; under 0.6 the labels are not yet a ground truth.")
diff = pairs[pairs["a"] != pairs["b"]]
if len(diff):
    print(f"\nWhere {Path(sys.argv[1]).stem} and {b_name} disagree (pair: count):")
    for (x, y), k in Counter(zip(diff["a"], diff["b"])).most_common():
        print(f"  {x} vs {y}: {k}")
    print("\nItems to adjudicate: " + ", ".join(diff.index))
