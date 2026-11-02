# Data boundary

One page per approved AI tool that says what happens to the data: what enters, what must not, where it travels, who sees inputs, outputs and logs, whether the vendor trains on it, how long it stays, who can change any of that, and what happens at exit. Write it after the vendor review and before any personal data flows; it becomes part 3 of the governance charter and most of a DPIA's data map. Lesson [04.3](../lessons/module-04/lesson-03.md) shows how.

## How to fill it

- Fill every row from the vendor's terms, the DPA and the admin console, citing the clause or setting.
- "Where it travels" lists every sub-processor and country, including human reviewers.
- Write "unknown — asked [date]" rather than guessing; an unknown blocks class D data.
- "Our controls" are settings and routines with owners, not intentions.
- Re-issue it whenever the vendor notifies a sub-processor or terms change.

## Template

```markdown
# Data boundary — [tool, plan] — v[n], [date]
Business owner: [name] · Technical owner: [name] · Vendor review: [link] · DPIA: [link or not needed + reason]

| Question | Answer | Source (clause / setting) |
|---|---|---|
| What data enters | | |
| What must not enter | | |
| Where it travels (processors, countries) | | |
| Who sees inputs and outputs (vendor staff, reviewers, our admins) | | |
| Vendor training on our data | | |
| Retention (operational, logs, analytics, backups) | | |
| Who can change these settings | | |
| Exit (export, deletion, deadlines) | | |
| Our controls (setting · owner · check frequency) | | |
| Open questions (asked to whom, when) | | |
```

## Example

Harbor & Pine — LinguaFlow Business, 18 November 2026:

| Question | Answer | Source |
|---|---|---|
| What data enters | Text of customer and supplier messages and draft replies selected for translation | DPA §3.1 |
| Where it travels | LinguaFlow (Ireland, Netherlands) on EuroCloud; MailRelay (Ireland) for account emails | DPA §5, §6 |
| Vendor training | None | DPA §4.1 |
| Retention | Zero, except 24-hour encrypted troubleshooting logs | DPA §4.1 |
| Our controls | Extension forced to the Business account, personal accounts blocked (Avi, checked monthly); free extension removed by 30 Nov | DPA §9 |
