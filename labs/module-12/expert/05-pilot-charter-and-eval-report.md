# 05 · Pilot charter, eval report and revised ROI — precedent search with a citation gate

> [!NOTE]
> Search, citation-gate (rules) and ROI figures are **real**: run `pilot/search.py`,
> `pilot/verify_citations.py` and `roi_model.py` and you get them exactly. The LLM-judge and
> assistant-answer figures are an **illustrative** worked example; your run will differ.

## Charter (dated Sunday 20 December 2026, before the first run)

**Hypothesis.** Over a curated corpus, a research assistant with a citation gate gives lawyers sourced
answers they can check in a fraction of the time, with no unverified citation reaching a partner.

**Scope.** The 78 research documents, curated (65 current). Two groups: Tech & IP (fixed-fee work) and
litigation research (Karim's team). Hebrew and English. No client documents. Tool: the firm's approved
enterprise assistant (Track A) or the scripts with an approved API (Track B).

| # | Threshold for "go to a supervised pilot in January" | Why |
|---|---|---|
| G1 | Retrieval: top result is a gold document for ≥ 90% of questions in each language; no superseded document in the top 3 | A stale first answer is the near miss |
| G2 | Citation gate rules: every invented document, wrong paragraph, non-verbatim quote and superseded document caught; 0 false alarms | Rules are exact; anything less is a bug |
| G3 | Reader step: ≥ 90% of misstated citations caught, false alarms ≤ 10% | Judgement is where the risk sits |
| G4 | Assistant answers over the curated corpus: ≥ 95% of citations pass the gate, 0 invented | The tool's own error rate |
| G5 | Negative tests: 8 of 8 behave as expected (`negative-questions.csv`) | Out of scope, injection, advice, stale cite |
| G6 | Checking time ≤ 2 min per citation with the gate (≈ 10 min by hand) | The value is in checking, not in typing |

**Rule of use.** The assistant proposes; a lawyer checks; nothing goes to a partner with a citation
that failed the gate; the answer shows the paragraph beside each sentence; "Not found in the corpus" is
a valid answer. **Stop rules:** any invented citation reaching a partner pauses the pilot; any client
information found in a prompt pauses it and goes to Orit. **Value measure:** research hours per memo
(time entries, narratives), Tech & IP fixed-fee overrun, write-offs on research lines; paired with
citations failing the gate before partner review.

## Results

**Search (real).**

| Corpus | Top result gold (en / he) | Gold recall@5 | Stale in top 3 (reversed points) |
|---|---|---|---|
| Uncurated, 78 docs | 39 of 48 (19 / 20) | 71.7% | 12 of 12 |
| Curated, 65 docs | 48 of 48 (24 / 24) | 74.1% (en 78.1, he 70.1) | 0 of 12 |
| Curated + Hebrew prefix stripping | 48 of 48 | 73.6% | 0 of 12 |

G1 met only after curation. Light Hebrew stemming did not help; Hebrew recall stays below English.

**Citation gate on the 160-citation test set (real for rules).**

| Check | Caught | Note |
|---|---|---|
| Invented documents | 18 of 18 | all from the general assistant |
| Wrong paragraph | 7 of 7 | |
| Non-verbatim quote | 9 of 9 | |
| Superseded, with the KM index status | 2 of 14 | the index marks 2 of 13 stale documents |
| Superseded, with the curated status | 14 of 14 | |
| Misstated (rules) | 0 of 22 | needs a reader |
| False alarms on 90 good citations (rules) | 0 | |
| Keyword-overlap "support" | 20 of 22 misstated | but 48 false alarms of 90: useless |

Rules with curation: 48 of 70 bad citations caught (68.6%), 0 false alarms: **G2 met.** Bad citations by
source: general assistant 42 of 80; vendor PoC 28 of 80 (none invented; 10 superseded, 12 misstated).

**Reader step (illustrative).** An LLM judge (one call per citation, the paragraph and the claim) caught
20 of 22 misstated citations with 6 false alarms of 90; the two misses were "a different proposition"
claims close to the paragraph's topic. With a lawyer reviewing every flag and a 10% sample of passes:
22 of 22 in the run. **G3 met (illustrative).**

**Assistant over the curated corpus (illustrative).** 48 answers, 171 citations; 164 passed (95.9%); 0
invented; failures: 4 misstated, 2 wrong paragraph, 1 non-verbatim quote. N-01 to N-08: 7 of 8; N-05
(injection) answered from the corpus correctly but added "the Supreme Court has held" without a
citation; prompt v1.1 adds "never refer to courts or cases outside the documents". After v1.1: 8 of 8.
**G4, G5 met (illustrative).**

**Checking time (directional).** Karim timed 40 citations: by hand median 9.5 minutes; with the gate's
table (paragraph beside the claim) median 1.4 minutes. **G6 met, directional:** an associate at a desk
in December, not at 23:00.

**Verdict.** Proceed to a supervised pilot in the two groups from 17 January, on the curated corpus
only, under the interim rule. Not tested: research outside the corpus, live client questions, Russian,
reviewers under load, the effect on write-offs.

## Revised ROI (real model, assumed inputs labelled)

Year 1 (2027), `roi_model.py`, saving 30% net of verification (assumed until the pilot times it):

| | 0: do nothing | A: 90 seats, billing unchanged | B: curate, control, re-price, pilot |
|---|---|---|---|
| Research hours saved | — | 4,634 | 2,163 |
| Fees lost on billable work | — | −₪2,417,502 | −₪564,084 |
| Freed hours (capacity, not cash) | — | 1,666 | 1,470 |
| Customer's share (Carmel) | −₪648,794 (15%) | −₪648,794 | −₪432,529 (package at −10%) |
| Control costs | — | −₪240,000 | −₪420,000 (curation + librarian) |
| Tools | — | −₪403,540 | −₪107,738 |
| Tech & IP packages from the overrun cut | — | — | +₪834,841 (assumed half of ₪1.67M) |
| **Net cash** | **−₪648,794** | **−₪3,709,836** | **−₪689,509** |
| Against doing nothing | | −₪3,061,042 | −₪40,715 |

The case for B is not a year-1 profit; it is that B stops a loss A would lock in, prices the customer's
share instead of conceding it, and pays for the knowledge any tool needs.
