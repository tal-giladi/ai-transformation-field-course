// Scenarios for incident-tabletop. A scenario is pure data: the starting state, a list of injects
// (what you learn at each hour and the decisions you take), the runbook to compare against, and the
// scoring constants. To add one, copy `harbor` and keep the same fields; `validateScenario` in
// model.js checks the data.
//
// Inject fields: id, t (hours since detection), when (clock text), info, extra [{ ifFlag | ifNotFlag,
//   text }], exposure (customers harmed between this inject and the next while the feature is fully on
//   and the cause is not fixed), decisions.
// Decision fields: id, label, when? ({ ifFlag | ifNotFlag }), options.
// Option fields: id, step (runbook step id), quality (best | ok | poor), text, result,
//   effects { running?: 'all' | 'partial' | 'off', sets?: [flags], trust?: { customers, staff, leaders },
//   docs?: points, cost?: ₪, delay?: hours until a containing action takes effect (default 0.25) }.
// Never state a legal deadline as fact: options about reporting send the question to the DPO or counsel.

export const DEFAULT_PRESET = 'harbor';

const harbor = {
  label: 'Harbor & Pine — the draft pilot promises refunds',
  brief:
    'Monday 15 March 2027, 09:40. Harbor & Pine’s support-email draft pilot has been live since 1 February: the tool drafts a reply, ' +
    'an agent reads it and sends it. Noa from marketing forwards you a public post: a customer’s screenshot of a reply promising a full ' +
    'refund for a damaged sofa and telling her to keep it, which is outside the returns policy. You are the incident lead. ' +
    'The incident unfolds over four days. At each point you get new information and take two or three decisions: contain, ' +
    'communicate, fix and report. You are scored on harm, time to contain, trust and documentation, and compared with a runbook.',
  fixedFlag: 'fixed',
  start: { running: 'all', harmed: 8, trust: { customers: 50, staff: 60, leaders: 60 } },
  scoring: {
    harmPerCustomer: 6,
    containBands: [
      { hours: 0.5, score: 100 }, { hours: 1, score: 85 }, { hours: 3, score: 60 },
      { hours: 6, score: 40 }, { hours: 24, score: 20 }, { hours: 1000, score: 5 },
    ],
  },
  injects: [
    {
      id: 'h0', t: 0, when: 'Monday 09:40',
      info: 'Noa forwards a public Facebook post with 40 shares: a screenshot of your reply to a damaged-sofa claim. “We are sorry. We will refund the full ₪4,200 and you are welcome to keep the sofa.” Your policy: repair or a replacement part; a refund only if repair is impossible, and the item is collected. Damage and returns emails arrive at about two an hour.',
      exposure: 1,
      decisions: [
        {
          id: 'contain', label: 'Contain',
          options: [
            { id: 'pauseCat', step: 'contain', quality: 'best', text: 'Switch off drafts for damage and returns now; agents write those by hand. Other categories keep their drafts.', result: 'Done at 09:55. Damage and returns replies are slower today; the rest of the queue is unaffected.', effects: { running: 'partial', trust: { staff: -3 } } },
            { id: 'pauseAll', step: 'contain', quality: 'ok', text: 'Switch off the whole pilot; everyone goes back to writing every reply by hand.', result: 'Done at 09:55. Safe, but the whole team is back to full manual load for a problem in two categories.', effects: { running: 'off', trust: { staff: -10 } } },
            { id: 'keep', step: 'contain', quality: 'poor', text: 'Keep it running and message the agents to check refund wording carefully.', result: 'Agents have been approving these drafts in seconds for weeks. A message does not change that.', effects: {} },
          ],
        },
        {
          id: 'lead', label: 'Who knows, and who decides',
          options: [
            { id: 'log', step: 'detect', quality: 'best', text: 'Open an incident log now (time, what we know, who decides), name yourself incident lead, and tell Michal and Samir.', result: 'Michal: “Thanks for telling me first. Keep me posted every few hours.”', effects: { docs: 2, trust: { leaders: 5 }, sets: ['logOpen'] } },
            { id: 'wait', step: 'detect', quality: 'poor', text: 'Wait until you know more before telling anyone.', result: 'At 11:15 Michal hears about it from Noa, not from you.', effects: { trust: { leaders: -10 } } },
            { id: 'reply', step: 'communicate', quality: 'poor', text: 'Reply on the post straight away: “This was an AI error; we cannot honour it.”', result: 'Two hundred angry comments in an hour: the company is blaming a machine for its own letter.', effects: { trust: { customers: -20, leaders: -5 } } },
          ],
        },
      ],
    },
    {
      id: 'h1', t: 0.8, when: 'Monday 10:30',
      info: 'Samir searched the replies sent since 1 March: 7 replies in 6 days promise a full refund, or a refund without collecting the item, on damage claims. Every one of the 7 drafts was approved in under 10 seconds. Five agents sent them, Olga among them.',
      extra: [{ ifNotFlag: 'logOpen', text: 'Nobody has written anything down yet; three people are now investigating the same thing in parallel.' }],
      exposure: 2,
      decisions: [
        {
          id: 'fix', label: 'Fix',
          options: [
            { id: 'cause', step: 'fix', quality: 'best', text: 'Before changing anything, ask Avi what changed in the tool since last week: prompt, model and knowledge sources.', result: 'Avi starts pulling the vendor console’s change history.', effects: { sets: ['lookingForCause'] } },
            { id: 'patch', step: 'fix', quality: 'poor', text: 'Add “never promise refunds” to the prompt and switch drafts back on for damage and returns.', result: 'The new line makes the drafts hedge, but they still quote the wrong policy text. The cause is still there.', effects: { running: 'all', sets: ['patched'] } },
            { id: 'blame', step: 'fix', quality: 'poor', text: 'Ask Samir to give the five agents a written warning for not reading the drafts.', result: 'Olga stops raising problems. The cause is still there.', effects: { trust: { staff: -25 }, sets: ['blame'] } },
          ],
        },
        {
          id: 'customers', label: 'The seven customers',
          options: [
            { id: 'honour', step: 'communicate', quality: 'best', text: 'Agree with Michal and Ronit to honour the 7 written promises, call each customer today, and ask counsel whether anything more is needed.', result: 'About ₪21,000. Two customers thank you publicly in the thread.', effects: { cost: 21000, docs: 1, trust: { customers: 15, leaders: 5 }, sets: ['honour'] } },
            { id: 'retract', step: 'communicate', quality: 'poor', text: 'Email the 7 customers that the promise was an error and the normal policy applies.', result: 'Two of them post your email in the Facebook thread.', effects: { trust: { customers: -20 }, sets: ['retracted'] } },
            { id: 'holdCust', step: 'communicate', quality: 'ok', text: 'Do nothing with the customers until the cause is known.', result: 'Quiet for now. Three of the seven write again asking when the refund arrives.', effects: { trust: { customers: -5 } } },
          ],
        },
      ],
    },
    {
      id: 'h2', t: 2.3, when: 'Monday 12:00',
      info: 'Avi found it. On 10 March someone added the “Customer Service” shared-drive folder to the tool’s knowledge sources, to give it the new assembly guides. The folder also holds the 2023 returns policy (full refund on damage, no collection) and a 2025 export of damage claims with customers’ names, addresses and order numbers. One draft sent on 12 March quotes another customer’s name and street address as “a similar case”. The change was made in the vendor console. Nobody tested it and there is no record of who approved it.',
      exposure: 3,
      decisions: [
        {
          id: 'privacy', label: 'The other customer’s data',
          options: [
            { id: 'dpo', step: 'escalate', quality: 'best', text: 'Treat it as a possible privacy incident: preserve the logs, write down which data went to whom, and brief the privacy officer or outside privacy counsel today. They decide whether and when it must be reported to the Privacy Protection Authority and whether the person whose data was disclosed must be told.', result: 'Counsel asks for the log and the facts by 16:00 and takes the reporting question.', effects: { docs: 2, trust: { leaders: 5 }, sets: ['privacyEscalated'] } },
            { id: 'assert', step: 'escalate', quality: 'ok', text: 'Report it to the Privacy Protection Authority within 24 hours, as the law requires.', result: 'You file before anyone checked what the rules require for this database and this kind of incident. Counsel later asks why they were not consulted; the report has two facts wrong.', effects: { docs: 1, sets: ['assertedDeadline'] } },
            { id: 'minimise', step: 'escalate', quality: 'poor', text: 'One address sent to one customer: not worth escalating.', result: 'Nobody tells the customer whose address was disclosed, and nobody decides whether it had to be reported.', effects: { trust: { leaders: -10, customers: -10 }, sets: ['privacyIgnored'] } },
          ],
        },
        {
          id: 'source', label: 'The cause',
          options: [
            { id: 'remove', step: 'fix', quality: 'best', text: 'Remove the shared-drive folder from the knowledge sources, re-index, and write 20 negative tests: damage emails that tempt a refund, and requests that could pull another customer’s data.', result: 'Re-indexed by 13:00. The negative tests run overnight.', effects: { sets: ['fixed', 'tested'], delay: 0.75 } },
            { id: 'model', step: 'fix', quality: 'poor', text: 'Ask the vendor to roll back the model version.', result: 'The vendor confirms nothing changed on their side; the model is the same. An afternoon lost.', effects: {} },
            { id: 'later', step: 'contain', quality: 'ok', text: 'No changes to the tool until next week; damage and returns drafts stay off until then.', result: 'Safe, but the damage queue grows by hand and the cause is still in the tool.', effects: { running: 'partial', trust: { staff: -5 } } },
          ],
        },
      ],
    },
    {
      id: 'h3', t: 5.3, when: 'Monday 15:00',
      info: 'The post has 300 shares. A reporter from a consumer-news site asks for a comment by 17:00. Yoav calls you: “What is going on, and what do I say if the board chair calls?”',
      extra: [
        { ifFlag: 'retracted', text: 'Your email to the seven customers is quoted in the reporter’s question.' },
        { ifNotFlag: 'fixed', text: 'The cause is still in the tool.' },
      ],
      exposure: 4,
      decisions: [
        {
          id: 'public', label: 'The reporter',
          options: [
            { id: 'holding', step: 'communicate', quality: 'best', text: 'A short, true statement the company owns: “A tool that helps our agents draft replies used an out-of-date policy document. We are contacting every affected customer and honouring what we wrote. A person reads every reply, and we have added a check.”', result: 'The article runs with your statement in full. It is a one-day story.', effects: { docs: 1, trust: { customers: 10, leaders: 5 } } },
            { id: 'none', step: 'communicate', quality: 'poor', text: '“No comment.”', result: 'The headline: “Furniture importer silent after AI refund blunder”.', effects: { trust: { customers: -10 } } },
            { id: 'vendor', step: 'communicate', quality: 'poor', text: 'Say it was a technical glitch at the AI vendor.', result: 'The vendor replies publicly that the configuration was the customer’s. The story gets a second day.', effects: { trust: { customers: -5, leaders: -10 }, sets: ['blamedVendor'] } },
          ],
        },
        {
          id: 'ceo', label: 'Yoav',
          options: [
            { id: 'brief', step: 'escalate', quality: 'best', text: 'Give Yoav one page: what happened, how many customers, what is contained, what is not known yet, what you decided, and the next update at 09:00 tomorrow.', result: 'Yoav forwards your page to the board chair before the chair calls.', effects: { docs: 1, trust: { leaders: 15 } } },
            { id: 'calm', step: 'escalate', quality: 'poor', text: 'Tell him it is under control and nothing to worry about.', result: 'At 18:00 the board chair forwards Yoav the article. He did not know about the privacy part.', effects: { trust: { leaders: -10 }, sets: ['reassured'] } },
          ],
        },
      ],
    },
    {
      id: 'h4', t: 23.3, when: 'Tuesday 09:00',
      info: 'Samir wants drafts back on for every category today: his team wrote 60 damage replies by hand yesterday and the queue is two days behind.',
      extra: [
        { ifFlag: 'fixed', text: 'The 20 negative tests passed on the re-indexed sources: no refund promises outside policy, no other customer’s data.' },
        { ifNotFlag: 'fixed', text: 'Nothing in the tool has changed yet: the old policy and the claims export are still in its sources.' },
      ],
      exposure: 12,
      decisions: [
        {
          id: 'restore', label: 'Restore',
          options: [
            { id: 'staged', step: 'restore', quality: 'best', text: 'Turn drafts back on for the other categories now; damage and returns after three days in shadow mode, with the source shown beside each draft.', result: 'Damage and returns drafts come back on Friday after shadow mode shows no repeats.', effects: { running: 'partial', trust: { staff: 5 }, sets: ['staged'] } },
            { id: 'allOn', step: 'restore', quality: 'ok', text: 'Turn everything back on today.', result: 'The queue clears by Wednesday.', effects: { running: 'all', trust: { staff: 10 } } },
            { id: 'stayOff', step: 'restore', quality: 'poor', text: 'Keep everything off until the board meeting.', result: 'The team is back to full manual load for weeks; two agents ask whether the pilot is cancelled.', effects: { running: 'off', trust: { staff: -15, leaders: -5 } } },
          ],
        },
        {
          id: 'check', label: 'The check that would have caught it',
          options: [
            { id: 'moneyFlag', step: 'restore', quality: 'best', text: 'Add a rule: any draft that mentions a refund, credit or compensation is flagged and needs a second look, and review time on flagged drafts is measured.', result: 'About 1 draft in 12 is flagged; a second look takes 40 seconds.', effects: { sets: ['moneyFlag'] } },
            { id: 'remind', step: 'restore', quality: 'poor', text: 'Remind the agents to read every draft carefully.', result: 'Review time goes up for two days, then back to 9 seconds.', effects: { trust: { staff: -5 } } },
          ],
        },
        {
          id: 'lateFix', label: 'The cause (still open)', when: { ifNotFlag: 'fixed' },
          options: [
            { id: 'remove', step: 'fix', quality: 'best', text: 'Remove the shared-drive folder from the knowledge sources, re-index and run negative tests before anything else.', result: 'Fixed by 11:00, a day later than it could have been.', effects: { sets: ['fixed', 'tested'], delay: 2 } },
            { id: 'skip', step: 'fix', quality: 'poor', text: 'The prompt change will do; no need to touch the sources.', result: 'The old policy stays in the tool.', effects: {} },
          ],
        },
      ],
    },
    {
      id: 'h5', t: 71.3, when: 'Thursday 09:00',
      info: 'The post has gone quiet. Michal wants a write-up for Monday’s steering group.',
      extra: [
        { ifFlag: 'privacyEscalated', text: 'Counsel’s view on the disclosed address came back on Wednesday, with a recommendation on reporting and on telling the customer.' },
        { ifFlag: 'privacyIgnored', text: 'Nobody has looked at the disclosed address since Monday.' },
      ],
      exposure: 0,
      decisions: [
        {
          id: 'review', label: 'The review',
          options: [
            { id: 'blameless', step: 'review', quality: 'best', text: 'A blameless review: timeline, cause (a knowledge-source change with no test and no approval), what worked, what did not, and actions with owners and dates: change control for sources and prompts, negative tests on every change, the money flag.', result: 'The steering group adopts the change-control rule on Monday.', effects: { docs: 3, trust: { staff: 10, leaders: 5 } } },
            { id: 'email', step: 'review', quality: 'poor', text: 'A short email: “Resolved, cause found, no further action.”', result: 'In June someone adds another folder to the sources.', effects: { trust: { leaders: -5 } } },
            { id: 'names', step: 'review', quality: 'poor', text: 'A review that names the agents who sent the replies.', result: 'The agents read it. Next time, nobody reports a strange draft.', effects: { docs: 1, trust: { staff: -20 } } },
          ],
        },
        {
          id: 'record', label: 'The record',
          options: [
            { id: 'full', step: 'detect', quality: 'best', text: 'Complete the incident log: who decided what and when, the customers contacted, counsel’s decision on reporting, and the evidence kept.', result: 'When the auditor asks in October, the answer takes ten minutes.', effects: { docs: 2 } },
            { id: 'emails', step: 'detect', quality: 'poor', text: 'The record is in people’s emails; that is enough.', result: 'In October nobody can say who decided to honour the seven promises, or why.', effects: {} },
          ],
        },
      ],
    },
  ],
  runbook: [
    { id: 'detect', title: 'Log and lead', text: 'Open an incident log at once, name one incident lead, and tell the sponsor and the owner of the affected team. Keep the log to the end.' },
    { id: 'contain', title: 'Contain first', text: 'Stop the harm with the narrowest switch that works (here: drafts off for two categories), before looking for the cause.' },
    { id: 'escalate', title: 'Escalate', text: 'Leadership gets facts, unknowns and the next update time. A possible privacy incident goes to the DPO or privacy counsel the same day; they decide whether, to whom and by when it is reported.' },
    { id: 'communicate', title: 'Communicate', text: 'Contact affected customers directly and keep what you wrote to them unless counsel says otherwise. Public statements: short, true and owned by the company, not blamed on a tool or a vendor.' },
    { id: 'fix', title: 'Find and fix the cause', text: 'Ask what changed (prompt, model, sources, settings) before changing anything. Fix the cause, then prove it with negative tests.' },
    { id: 'restore', title: 'Restore in stages', text: 'Bring back what is safe first; bring the affected part back after shadow mode, with the check that would have caught it.' },
    { id: 'review', title: 'Blameless review', text: 'Timeline, cause, what worked, and actions with owners and dates. The fix for “a person approved it in 10 seconds” is the design of the check, not a warning letter.' },
  ],
  flagNotes: [
    { flag: 'assertedDeadline', text: 'You reported “within 24 hours, as the law requires”. This model does not state legal deadlines: whether a privacy incident is reportable, to whom and by when depends on the regulations, the database and the facts. Brief the DPO or privacy counsel the same day, let them decide, and log the decision.' },
    { flag: 'privacyIgnored', text: 'One address sent to one stranger is still a disclosure of personal data. The decision whether it must be reported, and whether the person must be told, belongs to the DPO or counsel, not to the incident lead.' },
    { flag: 'patched', text: 'A prompt line on top of a wrong source is not a fix: the drafts kept quoting the old policy. Ask what changed first.' },
    { flag: 'blame', text: 'Seven drafts approved in under 10 seconds is a design signal (load, a tool that is usually right, no flag for money), not seven bad agents. Lesson 05.5 is about this.' },
    { flag: 'blamedVendor', text: 'The change was yours. Blaming the vendor in public is both untrue and easy to disprove.' },
    { flag: 'retracted', text: 'Retracting a written promise in writing, with a post already public, turns one bad reply into a second story. Ask counsel; most companies honour it and fix the cause.' },
  ],
  lessonPoint:
    'In an AI incident, contain first with the narrowest switch that works, then ask what changed before you fix anything. ' +
    'Write it down from the first minute, give leaders facts and the next update time, and send every privacy question to the DPO or counsel the same day instead of guessing the law. ' +
    'Restore in stages with the check that would have caught it, and review without blame: an approval in 10 seconds is a design failure.',
  notes: [
    'Volumes (two damage or returns emails an hour), the seven replies, ₪21,000 to honour them and the four-day timeline are assumptions for the exercise.',
    'Pilot live from 1 February 2027 matches adoption-dynamics. The shared-drive folder echoes the stale-copy finding in the data room.',
    'Israeli privacy rules (the Privacy Protection Law, its Amendment 13 and the data-security regulations) decide what is reportable; the model deliberately sends that question to the DPO or counsel.',
  ],
};

export const PRESETS = { harbor };
