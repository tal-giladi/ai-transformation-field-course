# Pilot — Harbor & Pine

Build, evaluate and prepare for launch Harbor & Pine's support triage and reply-drafts pilot, then recommend go or no-go for production. This is module 5's practical: everything from the charter to the monitoring spec, on the real (synthetic) data room, with numbers you produced yourself.

## The brief

It is 14 January 2027. The board decides on 28 January whether to release the first stage of the reply-drafts pilot (₪48,000 now, ₪72,000 from 1 April only if gate 1 is met, lesson [03.9](../lessons/module-03/lesson-09.md)). The steering committee meets on 19 January and wants a pilot that works on Harbor & Pine's own messages, an honest evaluation of it, a plan for how the human check, the release and the monitoring will work, and your recommendation.

The pilot: triage plus a draft reply for every written contact (email and web form now; WhatsApp once it is routed into the helpdesk on 1 February), in Hebrew, Arabic, Russian and English. A human agent reads every draft and sends it. "Where is my order?" drafts quote the updated delivery date from the date fix. Gate 1 (1 April): at least 80% of drafts accepted with no or light edits on at least 400 real messages, at least 70% in each language; median review time 2.5 minutes or less; wrong replies reaching customers no higher than today; measured hours covering the temps.

## Deliverables

| # | Deliverable | Template | Lesson |
|---|---|---|---|
| 1 | Pilot charter with rule of use, and value measurement plan | [pilot charter](../templates/pilot-charter.md), [value measurement plan](../templates/value-measurement-plan.md) | [05.1](../lessons/module-05/lesson-01.md) |
| 2 | Test-set spec, your 40-item labelling result and at least 26 negative tests | [test-set spec](../templates/test-set-spec.md) | [05.2](../lessons/module-05/lesson-02.md) |
| 3 | **Working pilot**: your prompt version with its change log, and run files (or the filled scoring sheet) for the development set, the 400-item test set and the negative tests | `labs/module-05/system-prompt.md`, `scoring-sheet.csv` (module 5 download) | [05.3](../lessons/module-05/lesson-03.md) |
| 4 | **Eval report** against the gates, with today and the keyword baseline beside your run | [eval report](../templates/eval-report.md) | [05.4](../lessons/module-05/lesson-04.md) |
| 5 | Human-review design | [human-review design](../templates/human-review-design.md) | [05.5](../lessons/module-05/lesson-05.md) |
| 6 | Release plan and production-readiness checklist | [production-readiness checklist](../templates/production-readiness-checklist.md) | [05.6](../lessons/module-05/lesson-06.md) |
| 7 | **Monitoring spec**: logging, signals, change control, calendar | [monitoring spec](../templates/monitoring-spec.md), `labs/module-05/monitoring-signals.csv` | [05.7](../lessons/module-05/lesson-07.md) |
| 8 | **Go / no-go recommendation**: one page for the steering committee | below | — |

The go / no-go page: the recommendation in the first sentence (go, go with conditions, or no-go and what would change it); the three numbers it rests on, each labelled measured, directional or assumed; the conditions, each with an owner and a date; what was not tested; and what a "no" would mean.

## Steps

1. Write the charter and the value measurement plan (05.1); have the rule of use agreed with Samir (roleplay or transcript).
2. Label the 40-item sample, compute agreement and kappa, write the test-set spec and your two extra negative tests (05.2).
3. Build the pilot in Track A or Track B; iterate on the development set only; run the test set and negative tests once with your final version (05.3). No key? Run Track B with `FIELDKIT_PROVIDER=mock` to prove the pipeline, and do the evaluation in Track A.
4. Score it, rate at least 60 drafts blind with 10 real agent replies mixed in, and write the eval report (05.4).
5. Design the human check; run the oversight simulation (05.5).
6. Write the release plan and fill the readiness checklist (05.6).
7. Write the monitoring spec (05.7).
8. Write the go / no-go page. Check every number in it against the deliverable it comes from.

Time: about 6 hours beyond the lessons' own exercises, most of it in steps 3 and 4.

## Self-assessment rubric

| Criterion | Strong | Weak |
|---|---|---|
| Charter | Falsifiable hypothesis; thresholds identical to the gates; stop rules with trigger, action, person; rule of use with logging fields and their limits | "Prove AI value"; new thresholds; "human in the loop" as the whole rule of use |
| Value plan | Indicator the budget owner reads; same-instrument baseline; paired quality metrics; a holdout or another named counterfactual with its label | Total hours before and after; self-reported time; no pair |
| Test set | Population and limits stated; sized from the gate with intervals; dev/test split; two-labeller protocol; pseudonymisation with residue check; negative tests for rare harms | Hand-picked examples; labels from the helpdesk field; tuning on the test set; no negative tests |
| Working pilot | Facts only from the context line; structured output; fenced customer text; versioned prompt with reasons; every item accounted for | Prompt holds prices and policies; unversioned edits; dropped items |
| Eval report | Verdict first; per category and language with n; today and the baseline beside the model; negative tests one by one; blind ratings; failure types; labels on every number | One accuracy figure; no baseline; offline numbers presented as production results |
| Human check | Four conditions answered; capacity screen at peak tied to the ROI line; a design answer to each reason reviewers stop; accountability rule; marking decided with counsel | "Agents review every draft" with no minutes, routing or feedback |
| Release | Shadow mode for what was not tested; one change per stage with entry conditions; rollback rehearsed; "sent cannot be unsent"; readiness lines with owners and consequences | Big-bang go-live; rollback means the switch only; checklist filled after launch |
| Monitoring | Minimal logging with retention question; every signal with threshold, cadence, owner, response; every stop rule as a trigger; model and vendor changes trigger re-runs before release | A dashboard; full-text logs; "we will monitor quality" |
| Recommendation | One sentence first; three labelled numbers; conditions with owners and dates; what "no" means | A summary of the work; no decision; unlabelled numbers |

<details><summary>Model answer</summary>

The lessons' reference answers are the expert deliverables 1–7: the charter and value plan ([05.1](../lessons/module-05/lesson-01.md)), the test-set spec ([05.2](../lessons/module-05/lesson-02.md)), the rule-to-test map and change log ([05.3](../lessons/module-05/lesson-03.md)), the eval report ([05.4](../lessons/module-05/lesson-04.md)), the human-review design ([05.5](../lessons/module-05/lesson-05.md)), the release plan and readiness checklist ([05.6](../lessons/module-05/lesson-06.md)) and the monitoring spec ([05.7](../lessons/module-05/lesson-07.md)). The real, reproducible numbers in them (today's helpdesk field 64.0%, keyword rules 98.2% on triage and 2 of 24 negative tests, 96 of 151 WISMO replies with a date already in the past) come from `labs/module-05/score.py`; the LLM figures are the course's illustrative worked example. Your own run replaces them.

**Go / no-go — reply drafts — for the steering committee of 19 January 2027**

> **Recommendation: go, with conditions.** Release stage 1 on Sunday 1 February: drafts on request
> for email and web form in all four languages, every reply checked and sent by an agent, a random
> 10% of tickets held out; WhatsApp in shadow mode for two weeks.
>
> **What it rests on.** (1) On 400 real messages, drafts were accepted with no or light edits 82% of
> the time, Arabic 72% on 50 messages (*measured on the test set; directional for production*).
> (2) Today, 63.6% of agents' "where is my order?" replies give a delivery date already in the past;
> drafts quote the updated date from logistics (*measured*). (3) At 82% and 2 review minutes, about
> 117 agent-hours a month are freed at peak, which is capacity, not cash, until the temps decision
> (*directional*).
>
> **Conditions.** Order data shown beside every draft and the load rule live by 28 January
> (integrator, Avi). Arabic acceptance re-measured on 100 production drafts by 1 March (Lina). WhatsApp
> "where is my order?" drafts stay off until the web-store order lookup works (Noa, Avi, 12 February).
> Counsel's view on what customers are told about AI-assisted replies before 1 February (Ronit).
> Logging and monitoring live by 29 January (pilot lead).
>
> **Not tested.** WhatsApp; peak-season volume; real reviewers under load; follow-ups after a draft
> was sent. Gate 1 on 1 April measures them.
>
> **If the answer is no.** Agents keep writing Russian and Arabic replies without a tool (about 13
> minutes for a careful Russian reply, observed), with pressure to return to free chatbots; the
> wrong-date replies continue until the date fix's effect shows; the temps decision for the next peak
> cannot be made on evidence by September.

</details>
