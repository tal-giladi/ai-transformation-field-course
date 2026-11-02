---
id: "06.4"
module: 6
minutes: 20
practice_minutes: 120
prerequisites: ["06.3", "05.1", "04.1"]
objectives:
  - "Define a qualified event and an opportunity-aware population from a real usage export joined with HR and rota data, and compute the qualified-use rate per week."
  - "Find quiet non-adoption — who stopped, when, and back to what — and turn it into a finding about the work, not about the people."
  - "Ask frontline managers the three questions and read their answers against the data."
  - "Design usage monitoring that is lawful and proportionate under Israeli privacy and labour law, and say what goes to counsel."
volatility: implementation
sources:
  - title: "Privacy Protection Authority — היבטי פרטיות במעקב אחר עובדים בעבודה מרחוק (Privacy aspects of monitoring employees working remotely), 17 October 2023 (PDF, Hebrew)"
    url: https://www.gov.il/BlobFolder/policy/remotework/ar/remote-work-privacy-aspects.pdf
  - title: "law.co.il (Haim Ravia) — Monitoring employees' email severely restricted (Isakov Inbar, National Labour Court, 8 Feb 2011)"
    url: https://www.law.co.il/en/articles/2011/04/25/monitoring-employees-email-severely-restricted/
  - title: "Chambers Practice Guides — Data Protection & Privacy 2026: Israel (Or-Hof Law): s. 11 notice items, Isakov tests, Amendment 13 in force 14 Aug 2025"
    url: https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel
  - title: "Kol Zchut — employer use of technological means to monitor employees working from home (summary of the PPA position)"
    url: https://www.kolzchut.org.il/he/%D7%A9%D7%99%D7%9E%D7%95%D7%A9_%D7%91%D7%90%D7%9E%D7%A6%D7%A2%D7%99%D7%9D_%D7%98%D7%9B%D7%A0%D7%95%D7%9C%D7%95%D7%92%D7%99%D7%99%D7%9D_%D7%9C%D7%A6%D7%95%D7%A8%D7%9A_%D7%9E%D7%A2%D7%A7%D7%91_%D7%90%D7%97%D7%A8_%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D_%D7%94%D7%9E%D7%91%D7%A6%D7%A2%D7%99%D7%9D_%D7%90%D7%AA_%D7%A2%D7%91%D7%95%D7%93%D7%AA%D7%9D_%D7%91%D7%91%D7%99%D7%AA
  - title: "Microsoft Learn — Microsoft Copilot usage report (enabled vs active users; opening the pane is not active use; user names hidden by default), updated 14 July 2026"
    url: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage
  - title: "IBM Lead AI Transformation certificate (Coursera) — course 5, module 4: qualified-use rate, opportunity-aware population, Goodhart on the dashboard; IBM Enterprise AI Transformation and Consulting certificate — course 3: altitude problem, frontline-manager sampling, quiet non-adoption"
    url: https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution
last_verified: "2026-11-02"
---

# 06.4 · The honest adoption dashboard

The vendor's dashboard will say that 75% of licence holders were active in the eighth week. It counts a panel that opens by itself when a ticket opens, two marketing licences nobody uses, and three agents who quietly stopped using the drafts a month ago. In this lesson you build the dashboard that tells Michal the truth, from Harbor & Pine's real usage export joined with the HR roster and Samir's rota: a qualified event, the people who could have used the tool each week, the qualified-use rate, the people who stopped — when, and back to what — the three questions for the frontline manager, and the rules that keep the monitoring of employees lawful and proportionate. At the end you have a one-page adoption dashboard for the gate-1 pre-read and the spec behind it.

## The situation

Sunday 28 March 2027. The drafts have been live for eight weeks; gate 1 is on Thursday 1 April ([05.1](../module-05/lesson-01.md)). The charter says value numbers are read only after drafts are inserted on at least 60% of eligible tickets for two consecutive weeks. Samir, asked on Thursday how it is going, said: "Everyone is on it. The panel is open on every screen." Avi has exported the panel's admin analytics for 1 February – 28 March (`usage/ai-usage-export.csv`: date, user, feature, events) and Dana has sent the roster of licence holders as of 31 March (`usage/hr-roster.csv`). Samir's rota is in the lab (`labs/module-06/queue-rota-2027.csv`).

You have promised two things in writing: the AUP says usage is reported "by team, not by person" ([04.1](../module-04/lesson-01.md), §6), and the rule of use says override logs are never used in performance reviews ([05.1](../module-05/lesson-01.md)).

The IBM certificates give the vocabulary: licence ≠ adoption ≠ value; the qualified-use rate (people with a defined meaningful use ÷ the opportunity-aware population, over a window that fits the work); Goodhart's law on the dashboard; the altitude problem (adoption looks better the higher you ask); quiet non-adoption as evidence (who stopped, when, back to what); and frontline-manager sampling. IBM never opens a real export. Here you do.

## What to do

### Step 1 — Read the export before you count anything

Open the file and list what each field means and what can fire it. Five features appear:

| Feature | What fires it | Use? |
|---|---|---|
| `panel_opened` | The panel opens with every ticket, by itself | **No** — it measures tickets opened, not use |
| `triage_suggestion_accepted` | Agent accepts the suggested category | A click; weak |
| `draft_generated` | Agent clicks "Draft" | Trying, not using |
| `draft_inserted` | Agent puts the draft into the reply box | **Yes** — the draft entered the real work |
| `translate_inbound` | Agent translates the customer's message | Real use, but not the pilot's outcome |

Microsoft makes the same distinction for its own product: in the Copilot usage report, opening the Copilot pane does not count as active use; submitting a prompt does, and user names are hidden in usage reports by default (Microsoft Learn, page updated 14 July 2026). Whatever tool you meet, find out which events fire by themselves before you trust an "active users" figure.

### Step 2 — Define the qualified event and the window

Write the definition so anyone can recompute it:

> **Qualified user-week:** a person in the opportunity-aware population with at least **5** `draft_inserted` events in the pilot week (pilot week *n* = the seven days from Monday 1 February + 7(*n*−1); week 1 = 1–7 February). **Sustained user:** qualified in at least 3 of the last 4 weeks.

Why 5: about one a working day, a floor rather than a target — every agent handles dozens of written contacts a week. Why a week: the work cycle is daily, and Samir plans in weeks. Then check that the conclusion does not depend on the threshold (Step 4). The definition is stable but correctable: if you change it, run the old and the new side by side for two weeks and say so.

### Step 3 — Build the opportunity-aware population, week by week

The denominator is the people who could have used the drafts that week, not the licences. Join the export to the roster on email and apply three rules:

1. **Role:** only roles that answer written contact (Support Agent, Senior Support Agent). Samir (manager) and Rina (claims; her licence is used for inbound translation) are reported separately; Noa and Shir (marketing) have no drafting task at all.
2. **Status:** out from the first pilot week that starts after they stopped working. Hila Dahan, maternity leave from 21 February → out from week 4. Adi Golan, resigned, last day 4 March → in for week 5, out from week 6.
3. **Absence** that the roster does not show (annual leave, sickness) is read from the rota as context, not used to remove people: Daniel had three days of leave in week 8.

At Harbor & Pine the population is 12 people in weeks 1–3, 11 in weeks 4–5, 10 in weeks 6–8. Neither leaver is a non-adopter: Hila inserted 23, 29 and 31 drafts in her three weeks; Adi was a steady user until her last day.

### Step 4 — Compute the qualified-use rate and put the vendor view beside it

Track A (spreadsheet): add a `week` column (`=INT((A2-DATE(2027,2,1))/7)+1`), filter `feature = draft_inserted`, pivot users × weeks with the sum of `events`, look up role and status from the roster, then count per week the people in the population with 5 or more. Track B: `python adoption_dashboard.py` does the same and prints every table below.

| Week (from) | Licences | Active, any event | Population | Qualified | Qualified rate |
|---|---|---|---|---|---|
| 1 (1 Feb) | 16 | 16 (100%) | 12 | 12 | 100% |
| 2 (8 Feb) | 16 | 14 (88%) | 12 | 12 | 100% |
| 3 (15 Feb) | 16 | 14 (88%) | 12 | 12 | 100% |
| 4 (22 Feb) | 16 | 13 (81%) | 11 | 8 | 73% |
| 5 (1 Mar) | 16 | 13 (81%) | 11 | 8 | 73% |
| 6 (8 Mar) | 16 | 12 (75%) | 10 | 7 | 70% |
| 7 (15 Mar) | 16 | 12 (75%) | 10 | 7 | 70% |
| 8 (22 Mar) | 16 | 12 (75%) | 10 | 6 | 60% |

Sustained users in weeks 5–8: **7 of 10**. Week 8's 6 of 10 includes Daniel's leave week (2 drafts on two working days); the sustained figure is the one to lead with. The threshold check: at 1, 5 or 10 inserted drafts a week, weeks 6–8 give 7, 7 and 6 or 7 of 10 — the conclusion does not move.

Three more lines belong on the page. **Drafts inserted per week** fell from 435 (week 3) to 280–310 (weeks 4–8), while the share of generated drafts that were inserted stayed at 64–77%: the people still using the drafts accept them at about the same rate; fewer people use them. **Licences:** 16 held, 10 needed for drafting, Rina's used for translation, Samir's barely (10 drafts generated, none inserted in eight weeks), Noa's and Shir's one event each in week 1 — two licences to reclaim. **The adoption gate** (≥ 60% of eligible tickets with a draft inserted) cannot be read from this export: it has no ticket counts. Ask Avi for the helpdesk report of eligible tickets by channel. As a sanity check only: with WhatsApp carrying most written contact and the WhatsApp agents inserting no drafts (Step 5), the gate is very unlikely to be met.

[Simulation: Adoption dynamics](../../simulations/adoption-dynamics/index.html?preset=harbor)

The simulation models a simplified Harbor team (14 licences, 12 people who do the target work, made-up first names) over 26 weeks: choose training (none, generic, role-based), champions, office hours, workflow redesign, a manager mandate and removing the old path, and compare "licences active", "weekly active users" and "people with qualified use", then open the "who stopped" view. Try a manager mandate from week 2 and watch active use rise while qualified use does not: Goodhart on the dashboard. The lesson works without it.

### Step 5 — Find quiet non-adoption: who stopped, when, back to what

Define it before you look: **used the drafts (qualified in at least 2 of weeks 1–3), then below the threshold in each of weeks 6–8, while still in the population and still working tickets** (the panel opened on 50 or more tickets a week). The last condition separates someone who stopped using the tool from someone who stopped working.

At Harbor & Pine three of the ten people in the week-8 population meet it. Inserted drafts per week: 16 / 21 / 31 / 2 / 0 / 0 / 0 / 0; 29 / 31 / 28 / 3 / 0 / 0 / 0 / 0; and 34 / 24 / 14 / 6 / 0 / 0 / 0 / 0, while their panel opened on 74–140 tickets every week. Their raw event totals stay between 89 and 154 a week, so the vendor dashboard counts all three as active.

**When:** two stopped in week 4 (22–28 February); the third faded from week 2 and reached zero in week 5.

**Join the rota** (`queue-rota-2027.csv`, by name and week): all three moved to the new **WhatsApp pod** on 22 February, when Samir reorganised the queues after Hila's leave; the third had been doing two and three WhatsApp days a week since week 2. In week 8 everyone else in the population works email and the web form. **Join the champions' issues log** (06.3): WhatsApp drafts too long and letter-style, logged 16 February (I-05), still open; old WhatsApp quick replies with "delivery date as shown in your order" back in Deskly since 8 February (I-07), still open in March.

One more source explains why nobody saw it coming: WhatsApp shadow mode in the first two weeks ([05.6](../module-05/lesson-06.md)) rated the hidden drafts for correctness and safety against what agents sent. It did not measure whether fixing a six-line letter-style draft is faster than typing two lines on a chat, which is the question the pod answered with its feet.

**Back to what?** The export cannot say: when nobody clicks "Draft", nothing is logged. The data say *when* and *where*; only people can say *back to what*. The likely answer — typing short replies and using the old quick replies — is a hypothesis until someone asks (Step 6, and the conversations in [06.6](lesson-06.md)). If confirmed, it matters for quality, not just adoption: the old quick reply sends the date that the redesign removed with the macro ([06.1](lesson-01.md), Step 5).

So the finding is about the work: **"From 22 February the WhatsApp queue — most of our written contact — has run almost without drafts. The three people on it used the drafts well on email; on WhatsApp the drafts are slower than typing (I-05) and an old quick reply with the order date is back (I-07)."** Not "three agents resist".

### Step 6 — Ask the frontline manager the three questions

The altitude problem: Samir's "everyone is on it" is an honest report of what he sees (panels open on every screen), and a hypothesis. Sample the frontline manager with three questions, and read each answer against the data:

1. **Do you expect and recognise use of the drafts, on the work where they help?** Samir: "I told everyone to use it." Data: he set up the WhatsApp pod on the queue where the drafts did not work, and nobody told the pod they could skip them.
2. **Do you use it yourself, where the team can see?** Samir: "I don't really take tickets." Data: 10 drafts generated, none inserted in eight weeks. In a 14-person team the manager's visible use is a signal; he could draft his own escalation replies.
3. **Do you talk about how the work is done with the drafts in your regular conversations with each person?** IBM puts this as "raise it in performance conversations". At Harbor & Pine the rule of use rules out usage numbers in reviews, so ask about coaching, not counting: does he ask "what did the drafts get wrong for you this week?" Samir: "Not yet."

Ask the same three of Olga as team lead. Then ask Samir the "back to what" question about the pod, as the manager who set it up, not about named people: "When the pod gets a WISMO message on WhatsApp, how does the reply get written?"

### Step 7 — Keep the monitoring lawful and proportionate

The usage export is personal data about employees: it names each agent and records what they did, day by day. Israeli law gives the frame; whether a specific practice is lawful is counsel's call.

- **The Privacy Protection Law, 5741-1981 (חוק הגנת הפרטיות, התשמ"א-1981)**, with Amendment 13 in force since 14 August 2025: collecting personal data carries the section 11 notice duty — purpose, who receives it, whether providing it is required — and Amendment 13 strengthened enforcement (Chambers' 2026 Israel guide).
- **Labour case law.** In *Isakov Inbar* (National Labour Court, 8 February 2011) the court required a clear policy on employees' use of company systems, brought to their attention and set in their contracts, and treated employees' consent with suspicion because of the power gap (law.co.il; Chambers).
- **The Privacy Protection Authority's position paper on monitoring employees working remotely (17 October 2023).** It is about remote work, but it restates the principles the courts apply to workplace monitoring generally: good faith, disclosure and transparency, legitimacy, proportionality and purpose limitation. Three points apply directly. The monitoring tool must fit its purpose (the paper's example: hours worked are checked with log-in times, not with productivity monitoring of browsing). Monitoring of activity on the employee's computer counts among the more intrusive measures and needs detailed written notice: how it is done, what data, how often, what it is used for, where it is kept and for how long — in plain language that takes account of the employees' languages. And the authority recommends a privacy impact assessment before monitoring employees, with the DPO involved.

For Harbor & Pine, that becomes the monitoring section of the dashboard spec:

| Rule | Harbor & Pine |
|---|---|
| Purpose, written | Run the pilot: fix the workflow, offer help, read the gate. Not to evaluate individuals. |
| Minimum data | Feature counts per user per day from the panel; no prompt or reply content in the dashboard |
| Who sees what | Michal, Samir, steering group: team and week only. Per-person weekly table: the pilot lead only, to offer help through a champion |
| Never | In performance reviews, in disciplinary steps, ranked lists, league tables |
| Notice before collection | In the comms pack ([06.5](lesson-05.md)), in Hebrew, Arabic, Russian and English: what is logged, why, who sees it, how long it is kept |
| Retention | Per-person table deleted at gate 2 (30 September 2027); team figures kept; the vendor's terms keep prompts and outputs in its analytics store for 24 months (`vendors/deskly-ai-addon-terms.md` §3.4) — check what was agreed in 04.3 |
| Assessment | Add employee usage data to the DPIA from [04.4](../module-04/lesson-04.md) |
| To counsel or the DPO | (1) Is the per-person view, used only for help, within the notice we gave? (2) Is the vendor's 24-month analytics retention, which holds named agents' drafts, acceptable, or must it be shortened? |

Harbor & Pine has no works committee. Where there is one, the PPA paper notes the courts' view that the policy be set in consultation with the employees' representatives — lesson 06.5 covers what changes.

## Watch out

- **Counting events that fire by themselves.** `panel_opened` made three non-users look active for five weeks. Classify every event before counting.
- **Licences as the denominator.** 16 licences, 10 people with the task. The rate against licences is a procurement number.
- **Leavers counted as non-adopters.** Hila and Adi were good users. Join HR status before you call anyone a stopper.
- **Naming people in the dashboard.** The finding is a queue and a design defect. A list of three names in a steering pack becomes a performance file, breaks the AUP's promise and teaches the team to hide.
- **Small groups that re-identify.** In a team of ten, "the WhatsApp pod" is three people everyone can name. Team-level is not anonymous here: frame the finding on the queue's drafts, and agree with the manager, before the pre-read goes out, how he will talk about it to the team.
- **Reading value before the adoption gate.** With most written contact running without drafts, minutes-per-contact figures describe the email queue only.
- **Mandating your way out.** "Everyone inserts five drafts a week" will raise the number and lower the quality; the simulation shows it. Fix the WhatsApp drafts and remove the old quick replies instead.

## Your turn

### Inputs

- In the module download: [`usage/ai-usage-export.csv`](../../labs/common/harbor-and-pine/usage/ai-usage-export.csv), [`usage/hr-roster.csv`](../../labs/common/harbor-and-pine/usage/hr-roster.csv), [`vendors/deskly-ai-addon-terms.md`](../../labs/common/harbor-and-pine/vendors/deskly-ai-addon-terms.md); in `labs/module-06/`: `queue-rota-2027.csv`, `champions-issues-log.csv`, `adoption_dashboard.py`, `adoption-dashboard-metrics.csv` ([lab README](../../labs/module-06/README.md)).
- Your AUP §6 (04.1), the rule of use and adoption gate (05.1), the DPIA (04.4).
- Template: [adoption dashboard spec](../../templates/adoption-dashboard-spec.md).

### Steps

1. Classify the five features: which fire by themselves, which are use.
2. Write the qualified event, the window and the sustained-user rule.
3. Build the population per week with reasons for every exclusion.
4. Compute the qualified-use rate per week and put the vendor-style rate beside it; check the threshold at 1, 5 and 10.
5. Find quiet non-adoption with a rule you wrote first; join the rota and the issues log; write who, when, where and what you still need to ask.
6. Write the three frontline-manager questions for Samir and Olga, and the "back to what" question.
7. Write the monitoring section: purpose, data, who sees what, never, notice, retention, DPIA, questions for counsel.
8. Put it on one page for the gate-1 pre-read, team-level only.

**Track B (Python).** Run `python adoption_dashboard.py` and check its tables against your spreadsheet; then `--threshold 10`. Python is worth it here because the dashboard is rebuilt every week from a new export, and the joins (roster status by week, rota by week) are where spreadsheet copies go wrong. The per-person table prints only with `--who`; read the note at the top of the script before you use it.

### Time

120 minutes: 20 to read the export and define, 40 for population and rates, 30 for quiet non-adoption and the manager questions, 30 for the monitoring section and the one-pager (Track B: about 80 in total).

### Done when

- [ ] `panel_opened` is excluded from use, with the reason.
- [ ] The population changes by week, and every exclusion has a reason from the roster.
- [ ] The qualified-use rate sits next to the vendor-style rate for all eight weeks, with the threshold check.
- [ ] Quiet non-adoption is defined before it is counted, and the finding names a queue and a cause to test, not people.
- [ ] The one-pager says the adoption gate cannot be read from the export and what is needed.
- [ ] The monitoring section covers purpose, minimum data, access, "never", notice, retention, DPIA and two questions for counsel.

<details><summary>Reference answer</summary>

**Script output (Track B, abridged):**

```text
=== 3. Qualified-use rate (qualified = at least 5 drafts inserted in the week) ===
 week   from  population  qualified_users qualified_rate vendor_active_rate
    1 01 Feb          12               12           100%               100%
    4 22 Feb          11                8            73%                81%
    6 08 Mar          10                7            70%                75%
    8 22 Mar          10                6            60%                75%
Sustained users in weeks 5-8 (qualified in at least 3 of the 4 weeks, still in the population): 7 of 10

=== 6. Quiet non-adoption: stopped inserting drafts but still working tickets ===
3 of 10 people in the week-8 population used the drafts in weeks 1-3 and inserted fewer than 5 a week
in each of weeks 6-8, while the panel still opened on 50+ tickets a week for each of them.
They stopped from week(s): 4, 5 (week 4 = 22 Feb - 28 Feb).
Main queue in the week they stopped: WhatsApp pod x3
Main queue in week 8 of everyone else in the population: email + web form x7
```

**Adoption dashboard — AI drafts pilot — weeks 1–8 (1 February – 28 March 2027)** — for the gate-1 pre-read; team-level; prepared 28 March by the pilot lead

> **Headline.** The drafts are used steadily on email and the web form — 7 of the 10 agents who answer written contact are sustained users — and hardly at all on WhatsApp, which carries most written contact. Since 22 February the WhatsApp queue has run almost without drafts. The adoption gate cannot be read yet and is unlikely to be met.

| Measure | Weeks 1–3 | Week 8 | Note |
|---|---|---|---|
| Licences held / needed for drafting | 16 / 12 | 16 / 10 | Reclaim 2 (marketing, one event each) |
| Vendor "active users" | 100%, 88%, 88% | 75% | Counts the panel opening by itself |
| Qualified-use rate (≥ 5 inserted / week) | 100% | 60% (6 of 10; one on leave) | Sustained users weeks 5–8: 7 of 10 |
| Drafts inserted per week | 306, 355, 435 | 285 | Insert ÷ generate steady at 64–77% |
| People who stopped while still working tickets | — | 3 of 10, all in the WhatsApp pod | From 22 February |
| Adoption gate (≥ 60% of eligible tickets, 2 weeks) | — | Not computable from the export | Helpdesk report requested from Avi, due 30 March |

**Finding.** The WhatsApp drafts are slower to fix than typing (issue I-05, open since 16 February) and the old quick replies with "delivery date as shown in your order" are back in the helpdesk (I-07, open since 24 February). The three agents moved to the WhatsApp pod on 22 February had used the drafts well on email. To confirm with Samir and Olga: how WhatsApp replies are written now.

**Decisions asked for:** (1) switch WhatsApp drafts off until the WhatsApp style passes its test set (pilot lead, now); (2) delete the migrated quick replies (Avi, 30 March); (3) a champion sits with the WhatsApp pod one hour a week; (4) gate 1 reads value for email and web form only, labelled as such, and the WhatsApp reading moves to a dated re-check (13 May).

**Frontline-manager questions — Samir, 25 March (answers against data):** expects use — "yes, I told them" / set up the pod where drafts did not work; own visible use — "I don't take tickets" / 10 generated, none inserted; talks about the drafts in one-to-ones — "not yet". Olga: expects — yes; own use — the heaviest user on the team; talks about it — "only when someone asks me".

**Monitoring:** as in the Step 7 table. Notice was given in the comms pack on 24 January (06.5); DPIA updated 29 March; questions to counsel sent via Ronit on 29 March (per-person view for help only; vendor's 24-month retention).

**What a weaker answer does:** reports "75% active" from the vendor screen, or "3 agents not using the tool" with their names in the steering pack. Both are wrong: the first is the panel opening by itself, the second turns a broken WhatsApp workflow into a performance problem for three people and breaks the AUP's promise.

</details>

## References

- Privacy Protection Authority, [Privacy aspects of monitoring employees working remotely](https://www.gov.il/BlobFolder/policy/remotework/ar/remote-work-privacy-aspects.pdf), 17 October 2023 (Hebrew): principles, purpose fit (§30), detailed notice for intrusive monitoring (§35), policy and employee representatives (§36), suspect consent (§38), privacy impact assessment and DPO (§58). Summary in Hebrew: [Kol Zchut](https://www.kolzchut.org.il/he/%D7%A9%D7%99%D7%9E%D7%95%D7%A9_%D7%91%D7%90%D7%9E%D7%A6%D7%A2%D7%99%D7%9D_%D7%98%D7%9B%D7%A0%D7%95%D7%9C%D7%95%D7%92%D7%99%D7%99%D7%9D_%D7%9C%D7%A6%D7%95%D7%A8%D7%9A_%D7%9E%D7%A2%D7%A7%D7%91_%D7%90%D7%97%D7%A8_%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D_%D7%94%D7%9E%D7%91%D7%A6%D7%A2%D7%99%D7%9D_%D7%90%D7%AA_%D7%A2%D7%91%D7%95%D7%93%D7%AA%D7%9D_%D7%91%D7%91%D7%99%D7%AA).
- *Isakov Inbar*, National Labour Court, 8 February 2011 — summary by [law.co.il](https://www.law.co.il/en/articles/2011/04/25/monitoring-employees-email-severely-restricted/); Chambers, [Data Protection & Privacy 2026: Israel](https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/israel). The judgment and the PPA paper are in Hebrew; ask counsel before relying on them. Not legal advice.
- Microsoft Learn, [Microsoft Copilot usage report](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage) (checked 2 November 2026).
- IBM, [Lead AI Transformation certificate](https://www.coursera.org/professional-certificates/ibm-lead-ai-transformation-strategy-governance-execution), course 5; [Enterprise AI Transformation and Consulting certificate](https://www.coursera.org/professional-certificates/ibm-enterprise-ai-transformation-and-consulting), course 3. Named, not re-taught.
- Template: [adoption dashboard spec](../../templates/adoption-dashboard-spec.md). Simulation: adoption dynamics (above).
- Earlier: [04.1 · The AI acceptable-use policy](../module-04/lesson-01.md), [04.4 · AI inventory, risk tiering and the DPIA](../module-04/lesson-04.md), [05.1 · The pilot charter](../module-05/lesson-01.md), [06.3 · Champions](lesson-03.md). Next: [06.5 · The comms pack](lesson-05.md).
