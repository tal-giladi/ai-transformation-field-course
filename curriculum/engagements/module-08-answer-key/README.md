# Northwind Outfitters — answer key (writers only, never linked from lessons)

Built by `labs/module-08/data-room/generate.py --answer-key <this folder>` (seed 20261108).

| File | What it holds |
|---|---|
| `contacts-and-sessions-truth.csv` | For every row of `contacts.csv` (K-…) and `bot-sessions.csv` (VB-…): the true intent, the issue it belongs to, whether it is a repeat of that issue, whether a bot session was followed by a recontact, and the customer's true language |
| `customers-truth.csv` | True language, 65+, new immigrant and disability flags for the 3,400 sampled customers |
| `returns-truth.csv` | True return reason and days after delivery for every return |

The 2,000 written tickets' labels are not here: they ship to learners in `labs/module-08/pilot/labels-2000.csv` (the test set needs ground truth). Numbers derived from these files are in `../module-08.md`, marked *truth*.
