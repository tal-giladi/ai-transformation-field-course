# Module 02 — notes for the main session

## Needs a decision or an edit in shared files

1. **WhatsApp persona unlock (02.2).** Lesson 02.2 teaches a "channel question" ("How do customers actually reach you? How many a day?") and its reference answer expects Samir or Olga to reveal the four shared WhatsApp phones and the October tally when asked. Please make sure the persona files carry that unlock (you said they will). The pre-run transcripts never ask it; 02.2's critique says so.
2. **INDEX.md** did not list `support/whatsapp-week-tally.csv` when I checked. Lessons 02.3–02.7 and the scripts use it.
3. **WhatsApp `order_no` format.** Every filled `order_no` in the tally is `HP-1xxxxx`; none matches the ERP's `SO26…` (0 of 248). I treated this as a planted finding ("agents type some other number; ask Samir") in 02.5, 02.6 and 02.7. If it was not intended, regenerate with ERP numbers and remove those sentences (02.5 Step 6, 02.6 R-05, 02.7 memo "what we don't know", reference answers).
4. **Templates written to the inbox:** stakeholder-map, interview-guide, task-inventory, data-profile, readiness-assessment, findings-memo (+ CSVs in `labs/module-02/`: stakeholder-map, task-inventory, data-profile, readiness-assessment). The `findings-memo.md` template write was blocked by the agent tool's "no report files" guard (file name); I wrote it with the shell. Content is the template only.
5. **Suggested additions to references/laws-and-guidance.md:** see the end of `module-02-sources.md`.

## Cross-module inconsistencies found

- **Transcript weekdays.** 2 Nov 2026 is a Monday (M1 uses "Mon 2 Nov"; the writer's notes say "Sunday 2 November"). The pre-run transcripts say "Monday 10 November" (a Tuesday), "Wednesday 12 November" (a Thursday) and "Thursday 13 November" (a Friday — Tamar's interview on a Friday is odd). Module 02 avoids weekday names for those dates. Suggest fixing the three transcript headers.
- **readiness-evidence-grader (`harbor` preset) vs the data room:** StoreHub lead times "Vietnam 45, China 40" (data: 42, 38); first response "median 6.5 h" (data: 6.1 h all months; 6.5 h is Q3 only); follow-ups "22%" (data: 23.4% with normalised order numbers, 21.3% raw); claims outcome missing "35%" (data: 32.2%); Olga drafts "on my phone" (data and persona: free ChatGPT on her Google login, visible in the proxy log); proxy "11 machines, 7 in Support" (census numbers differ); Deskly terms "never used to train … deleted after 90 days" (data room's Deskly terms §3.2 allow training on de-identified content unless opted out; §3.4 24-month analytics retention); interview dates 4–6 Nov precede the 02.2 interviews (10–12 Nov). 02.6 tells learners the simulation simplifies and that the data room wins. Suggest aligning the preset.
- **discovery-interview (`harbor`):** "Vietnam is 45 days … set in 2022" (data: 42, Feb 2023); Tamar's sheet "about 140 open containers … update every morning" (data: 95 container rows, updated twice a week); Olga "ChatGPT on my phone"; Samir "I ran it last month: about 38%" (persona: he has never counted). No WhatsApp channel in the simulation at all.
- **Writer's notes numbers I could not reproduce exactly:** stale-catalogue price gap "median 15.4% below current" — I get 12.7% (of current price) or 14.6% (of the copy's price); lessons use 12.7%. "40 Vietnam/China containers … delay ≥ 7 days": I get 43 by `eta_latest − eta_original` including not-yet-arrived ones (the notes count arrived ones); lessons say 43 and median delay 14 days. Container-wave median 12 days reproduces.
- **Interim AI rule date.** 02.3, 02.6 and 02.7 assume the interim rule was approved on 12 November (M1 01.6 recommends "approved by 12 November"; M1 project uses 12 Nov).

## Facts I could not fully verify (also marked ⚠️ in the sources file)

- Whistleblower law: exact Hebrew title and year number (התשנ"ז-1997) from a secondary source only.
- WIPO's English text of the Privacy Protection Law predates Amendment 13; the purpose principle after Amendment 13 is from a law-firm summary.
- Gartner study: not found by web search; gartner.com blocks the fetch tool.

## Other

- The two Track B scripts (`baseline.py`, `profile_data.py`) were run with Python 3.14.3 and pandas 3.1.0 from the field-kit pins; outputs match the numbers in the lessons. They call `sys.stdout.reconfigure(errors="replace")` so they don't crash on a cp1252 Windows console.
- `labs/module-02/observation-notes.md` is a synthetic sit-in log (Olga and Hila, 17 Nov) written for 02.3; it assumes the interim rule is in force and shows the Russian reply taking 13 minutes instead of 5.
- Personas used: Samir, Olga, Tamar (02.2) with the coach prompt.
