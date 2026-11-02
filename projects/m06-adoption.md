# The adoption pack for Harbor & Pine

The module 6 practical: everything that makes Harbor & Pine's drafts pilot used, and used well — the workflow redesign, the training session pack, the champions playbook, the honest adoption dashboard, the comms pack and the notes from the three resistance conversations — made consistent, so that every promise to the team is the same in every document, every number traces to the usage export, and every finding about use points at the work rather than at people. Most pieces start as your answers to lessons 06.1–06.6; the practical asks you to finish them, make them agree, and write the adoption section of the gate-1 pre-read. Plan 6 hours if you completed the lessons' "Your turn" tasks, longer if you did not.

## The brief

It is Wednesday 31 March 2027, evening. Gate 1 is tomorrow at 10:00. Michal Peretz, the COO, wants "one adoption pack, not six documents: what we changed, how we trained them, what the numbers really say, what we promised the team, and what we are doing about WhatsApp. If Ronit asks whether the hours are real, if Dana asks who sees the per-person figures, or if Yoav asks why a third of the agents stopped, the answer has to be in there, the same everywhere."

You have the Harbor & Pine data room (especially `usage/ai-usage-export.csv` and `usage/hr-roster.csv`), the module 6 lab files (rota, issues log, training folder, scene cards, transcripts), the personas, and everything from modules 1–5: the AUP and its logging section (04.1), the DPIA (04.4), the pilot charter with the rule of use, the stop rules and the adoption gate (05.1).

## Deliverables

| # | Deliverable | Template | Built in |
|---|---|---|---|
| 1 | Workflow redesign v1.0: three workflows marked step by step, old paths with switch-off dates, handoffs, freed hours, impact by role, handbook changes | [workflow redesign](../templates/workflow-redesign.md) | 06.1 |
| 2 | Training session pack: plan with roster, eight exercise cards (or your own) with a trainer key, run sheet, job aid, exit check, what the dry run changed | [training session plan](../templates/training-session-plan.md) | 06.2 |
| 3 | Champions playbook with the huddle decisions on the open issues as of 28 February | [champions playbook](../templates/champions-playbook.md) | 06.3 |
| 4 | Adoption dashboard: the one-pager for the pre-read, the spec with metric definitions, and the monitoring section | [adoption dashboard spec](../templates/adoption-dashboard-spec.md) | 06.4 |
| 5 | Comms pack: promise table with approvals, sequence, announcement, Samir's talking points, FAQ, monitoring notice, the works-committee page | [comms plan](../templates/comms-plan.md) | 06.5 |
| 6 | Notes from the three resistance conversations, the actions agreed, and the correction to the team | — | 06.6 |
| 7 | Adoption section of the gate-1 pre-read (one page): headline, numbers, what cannot be read yet, decisions asked for | — | this project |

## Steps

1. **Collect** deliverables 1–6 from your lesson work. Where you skipped a "Your turn", do it now; the lessons' reference answers show the standard but are not yours to copy.
2. **Recompute the numbers** from the export yourself (Track A pivot or `labs/module-06/adoption_dashboard.py`) and check every figure in the pack against it: population per week, qualified-use rate, sustained users, drafts inserted, licences, quiet non-adoption.
3. **Make the promises agree.** One set of wording on monitoring in the AUP §6, the rule of use, the FAQ's notice, the dashboard spec, the champions playbook and the training script. One approved wording on jobs, used word for word in the FAQ, Samir's talking points and the trainer's script. List every difference you fix.
4. **Make the dates agree.** Go-live and WhatsApp routing 1 February; phones handed in 4 February; training 8–11 February with the champions' dry run on 7 February; WhatsApp drafts on 15 February; WhatsApp pod 22 February; team meeting 24 January; gate 1 on 1 April; per-person data deleted 30 September 2027.
5. **Check every finding about use** points at a queue, a step or a design defect, never at named people, and that small-group re-identification is handled.
6. **Write the gate-1 adoption section** (deliverable 7).
7. **Self-assess** with the rubric below, then run the [coach prompt](../labs/common/coach-prompt.md) on deliverable 7 and the FAQ with the rubric as the checklist.

## Rubric

| Criterion | Strong | Weak |
|---|---|---|
| Workflow redesign | Built from evidence; every step marked with a reason; every removal dated and owned; receiving teams named; freed hours have a destination and an indicator | A spec of the tool; "agents should prefer the draft"; logistics absent; hours "saved" with no destination |
| Training | Goal is a behaviour; every person has a group or a reason (temps, leave); real cases with one planted error each; most of the hour hands-on; exit check results private; a rule that changes the session | Features tour; invented examples; attendance as the measure; exit check sent to the manager |
| Champions | Jobs and "never" lines in writing; chosen by language and respect; time in the rota and priced; every issue decided and told; back-ups for the overloaded expert | Fans chosen by the manager; time "on top"; a log that only collects; champions as monitors |
| Adoption dashboard | Events classified; population by week from HR status; qualified-use rate beside the vendor view; threshold checked; quiet non-adoption defined first and framed on the work; what the export cannot answer said | "75% active"; licences as the denominator; leavers counted as stoppers; three names in the pack |
| Monitoring and law | Purpose, minimum data, access, never, notice, retention, DPIA, questions for counsel; Israeli sources cited with dates; nothing stated as settled law | "We don't monitor"; consent forms as the answer; legal conclusions asserted |
| Comms | Every promise approved by the person who can keep it; the 40% and the temps addressed; sequence puts the manager and champions first; notice in four languages; works-committee page names who, before what, about what | "No one will lose their job"; "the 40% is not relevant"; email first; English only |
| Resistance | Prepared per person with "what I cannot promise"; the unlocking question asked; the expert's change brought into change control without blame; dated actions; written correction | Arguing the data; promising others' decisions; punishing or ignoring the workaround |
| Consistency | Same wording, dates and numbers across all seven deliverables; differences listed and fixed | The FAQ, the AUP and the dashboard say different things about who sees what |

<details><summary>Model answer</summary>

The reference answers in each lesson are the model for deliverables 1–6: [06.1](../lessons/module-06/lesson-01.md) (redesign v1.0 with the three workflows, old paths, freed hours and impact table), [06.2](../lessons/module-06/lesson-02.md) (session plan v1.1, roster with the temps decision, what the dry run changed), [06.3](../lessons/module-06/lesson-03.md) (playbook v1.0 and the 28 February huddle), [06.4](../lessons/module-06/lesson-04.md) (script output, one-pager, monitoring table), [06.5](../lessons/module-06/lesson-05.md) (comms pack v1.0 with approvals) and [06.6](../lessons/module-06/lesson-06.md) (what each conversation found and missed, the correction). The full training materials are in `labs/module-06/training/`. What the integrated pack adds:

**Consistency fixes a strong pack makes.**

- One monitoring promise everywhere: feature counts per person and day; team and week for Michal, Samir and the steering group; the per-person weekly table with the pilot lead only, to offer help; never in reviews, rankings or discipline; per-person data deleted 30 September 2027. The AUP §6 said "by team, not by person" — the pack adds, in the FAQ notice and the AUP's next version, the pilot lead's help-only view, so the notice covers what is actually done.
- One job wording, used verbatim in the FAQ, Samir's talking points and the session script: "No one in the Customer Service team will be dismissed or have their role reduced because of this pilot while it runs — until the decision on 30 September 2027."
- One set of numbers from the export: population 12 / 11 / 10; qualified 100% in weeks 1–3, 73% in weeks 4–5, 70% in weeks 6–7, 60% in week 8 (one on leave); sustained 7 of 10; drafts inserted 435 at the peak week, 280–310 since; vendor "active" 75% in week 8; 16 licences, 2 to reclaim.
- The WhatsApp story told the same way in the dashboard, the issues log, the conversation notes and the correction: the drafts did not work on WhatsApp (I-05) and an old path came back (I-07); the pod used them well on email.

**Gate-1 adoption section (excerpt).** "Adoption — answer first: on email and the web form the drafts are used steadily (7 of 10 agents are sustained users); on WhatsApp, most of our written contact, they are hardly used since 22 February, because the WhatsApp drafts were too long and an old quick reply came back. Both are fixed or switched off as of today. The adoption gate (60% of eligible tickets) is not met overall and cannot yet be read by channel; the helpdesk report arrives on 6 April. We ask: (1) read value at gate 1 for email and web form only, labelled 'email and web form, attributed by the holdout'; (2) re-check WhatsApp on 13 May after the WhatsApp style passes its test set; (3) note that Russian figures since 10 March await a test-set re-run of a settings change made outside change control, now recorded; (4) Michal's decision on Adi's post by 8 April, told to the team. Nothing in this pack names individuals; in a team of ten, please do not ask who."

</details>
