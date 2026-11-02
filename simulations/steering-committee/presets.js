// Scenarios for steering-committee. A scenario is pure data: a cast, an agenda of rounds (each a
// question from one member and the answers you can give), and the outcomes with their "six months
// later". An engagement module adds a preset by copying `harbor` and changing the cast, the paper and
// the rounds; no code changes. `validateScenario` in model.js checks the data (see simulations/README.md).
//
// Cast fields: id, name, role, concern (shown to the learner), mood (0 hostile … 4 champion),
//   weight (how much their view counts in the room's support), sponsor? (true for the sponsor).
// Round fields: id, speaker (cast id), prompt, when? (condition), advocate? (true for the moment the
//   sponsor argues past the evidence), choices.
// Choice fields: id, type (a key of TYPES in model.js), text, reply (what happens next),
//   moods { castId: delta }, honesty (delta; negative = the paper got less honest), sets [flags].
// Outcome fields: id, kind (approved | conditions | sentBack | killed), title, when? (condition; the
//   last outcome has none), text, later [{ when?, text }] (first match wins; one without when).
// Conditions are described at the top of model.js.

export const DEFAULT_PRESET = 'harbor';

// The minutes carry a bigger number than the paper: an overclaim that was never taken back.
const INFLATED = {
  any: [
    { honesty: { lte: -2 } },
    { flag: 'bigNumber' }, { flag: 'overclaim40' }, { flag: 'allCash' }, { flag: 'overclaimBoard' },
    { all: [{ any: [{ flag: 'michalNumber' }, { flag: 'numberStands' }] }, { notFlag: 'recovered' }] },
  ],
};

const harbor = {
  label: 'Harbor & Pine — steering meeting on the pilot',
  brief:
    'Tuesday 19 January 2027, 45 minutes. You present the recommendation to Harbor & Pine’s steering group: approve phase 1 of the ' +
    'support-email draft pilot (drafts for damage, assembly, returns and B2B quotes; a person sends every reply), with ₪120,000 ' +
    'released in two stages and a gate on 1 April. Your paper says: about ₪113,000 a year in cash (the translation contract cut to a ' +
    'small plan, and no peak-season temps next winter), about 570 agent-hours a year of capacity on top, which is not cash, and a ' +
    'three-year cost of about ₪267,000, so the board must approve it on 28 January. The delay-email fix (no AI) went live on ' +
    'Thursday 14 January. Each member has a concern; answer them one by one and leave with a decision.',
  paper: [
    'Ask: approve phase 1 with conditions; ₪48,000 now, ₪72,000 at the 1 April gate; take it to the board on 28 January.',
    'Cash, expected case: about ₪113,000 a year. Capacity: about 570 agent-hours a year (not cash).',
    'Evidence: a test set of 400 real emails, drafted and timed in December and January; minutes and error rate measured on that set, not on live traffic yet (shadow mode starts in February).',
    'Three-year cost about ₪267,000 (build ₪120,000 plus about ₪49,000 a year to run): above ₪150,000, so the board decides.',
  ],
  cast: [
    { id: 'yoav', name: 'Yoav Ben-Ami', role: 'CEO, chairs the meeting', concern: 'Told the board in September: a bot, and 40% lower support cost. Needs something true to say on 28 January.', mood: 2, weight: 2 },
    { id: 'ronit', name: 'Ronit Avraham', role: 'CFO', concern: 'Savings that exist only on slides. Signed the 2022 CRM case that was written off. Wants staged money and claims she can audit.', mood: 1, weight: 2 },
    { id: 'michal', name: 'Michal Peretz', role: 'COO, your sponsor', concern: 'Backed you for three months. Wants the programme to look big enough to matter to Yoav and the board.', mood: 3, weight: 1.5, sponsor: true },
    { id: 'avi', name: 'Avi Mizrahi', role: 'IT manager (one-person IT)', concern: 'Will be the one called when it breaks. Wants to know who supports it and where customer data goes.', mood: 2, weight: 1 },
    { id: 'samir', name: 'Samir Haddad', role: 'Customer service manager', concern: 'Heard “40% lower support cost” at the town hall. Afraid this is about cutting his team.', mood: 1, weight: 1 },
  ],
  rounds: [
    {
      id: 'open', speaker: 'yoav',
      prompt: 'You have the floor. We have 45 minutes, and I have a board pack to finish.',
      choices: [
        {
          id: 'answer', type: 'answerFirst',
          text: '“We recommend phase 1 of the draft pilot with two money gates. Today I am asking for ₪48,000 now and your agreement to take the case to the board on the 28th. Three reasons, then your questions.”',
          reply: 'Yoav nods and looks at the clock less. Ronit underlines “₪48,000 now”.',
          moods: { yoav: 1, ronit: 1 }, sets: ['answerFirst'],
        },
        {
          id: 'story', type: 'background',
          text: '“Let me take you through how we got here: eight weeks of discovery, the interviews, what we found in the data room…”',
          reply: 'Twelve minutes in, Yoav interrupts: “So what are you asking us for?”',
          moods: { yoav: -1 },
        },
        {
          id: 'big', type: 'overclaim',
          text: '“This programme can deliver ₪1.36 million a year: the 40% we promised the board.”',
          reply: 'Yoav smiles. Ronit writes “1.36M?” in the margin and circles it twice.',
          moods: { yoav: 1, michal: 1, ronit: -2 }, honesty: -2, sets: ['bigNumber'],
        },
      ],
    },
    {
      id: 'board', speaker: 'yoav',
      prompt: 'I told the board a bot and 40% lower support cost. What do I tell them on the 28th?',
      choices: [
        {
          id: 'ev', type: 'evidence',
          text: '“What we measured: 38% of contacts were ‘where is my order?’, caused by the delivery date we promise at checkout. The date fix went live last Thursday; we will measure the drop from February. What we infer: a bot would have answered them with the same wrong date. So: we fixed the cause first, and the AI pilot is next, with numbers we measured.”',
          reply: 'Yoav repeats it back: “Fixed the cause first, measured pilot next.” He writes it down.',
          moods: { yoav: 1, ronit: 1 }, honesty: 1, sets: ['evidence'],
        },
        {
          id: 'track', type: 'overclaim',
          text: '“Tell them we are on track for the 40%. This pilot is step one.”',
          reply: 'Yoav relaxes. Ronit: “On track according to what?” Nobody answers.',
          moods: { yoav: 2, ronit: -2 }, honesty: -2, sets: ['overclaim40'],
        },
        {
          id: 'concede', type: 'concede',
          text: '“The 40% will not happen this year, and I would rather you hear that from me today than from the numbers in June. I will help you write the board slide.”',
          reply: 'A long pause. Then Yoav: “Fine. Write me the slide, and make it something I can defend.”',
          moods: { yoav: -1, ronit: 1 }, honesty: 1, sets: ['badNewsEarly'],
        },
        {
          id: 'later', type: 'defer',
          text: '“That is a communications question. Perhaps for you and Michal after this meeting?”',
          reply: 'Yoav: “I am asking you.” He moves on, irritated.',
          moods: { yoav: -1 },
        },
      ],
    },
    {
      id: 'money', speaker: 'ronit',
      prompt: 'Whose budget does the saving land in, and how was it measured?',
      choices: [
        {
          id: 'ev', type: 'evidence',
          text: '“About ₪113,000 a year is cash: the translation contract we cut to a small plan, and the two peak-season temps Samir has agreed not to hire next winter. The other 570 hours or so are capacity, not cash. Minutes per draft were timed on a test set of 400 real emails.”',
          reply: 'Ronit checks two lines against the paper. “Good. That I can audit.”',
          moods: { ronit: 2 }, honesty: 1, sets: ['cashCapacity'],
        },
        {
          id: 'all', type: 'overclaim',
          text: '“It all lands in Customer Service: about ₪1.3 million a year once it is running.”',
          reply: 'Ronit: “In whose payroll line, from which month?” Samir stiffens: one point three million sounds like people.',
          moods: { ronit: -2, samir: -1 }, honesty: -2, sets: ['allCash'],
        },
        {
          id: 'weak', type: 'concede',
          text: '“The minutes come from a test set, not live traffic. That is exactly why the ₪72,000 waits for the 1 April gate.”',
          reply: 'Ronit: “Then the gate is the case. Fine.”',
          moods: { ronit: 1 }, honesty: 1, sets: ['conceded'],
        },
        {
          id: 'send', type: 'defer',
          text: '“I will send you the model after the meeting.”',
          reply: 'Ronit: “The model is the meeting.” She makes a note.',
          moods: { ronit: -1 },
        },
      ],
    },
    {
      id: 'advocate', speaker: 'michal', advocate: true,
      prompt: 'Let me add something. Once this is live across every category I would expect closer to ₪500,000 a year. We can get near what the board expects.',
      choices: [
        {
          id: 'agree', type: 'overclaim',
          text: '“Yes. At full scale ₪500,000 is realistic.”',
          reply: 'Michal looks pleased; Yoav brightens. Ronit puts her pen down.',
          moods: { michal: 1, yoav: 1, ronit: -2 }, honesty: -2, sets: ['michalNumber'],
        },
        {
          id: 'blunt', type: 'blunt',
          text: '“That number is not supported. The evidence says ₪113,000.”',
          reply: 'The room goes quiet. Michal: “I see.” Ronit almost smiles.',
          moods: { michal: -2, ronit: 1 }, honesty: 1, sets: ['michalCorrected'],
        },
        {
          id: 'reframe', type: 'reframe',
          text: '“Michal is right that there is more upside, and phase 2 is designed to test it. In the paper ₪113,000 is the expected case; anything above it is labelled an assumption we test at the September gate, so the board holds us to what we have measured.”',
          reply: 'Michal: “Fair. September, then.” Ronit writes “upside = assumption” and nods.',
          moods: { ronit: 1 }, honesty: 1, sets: ['upsideLabelled'],
        },
        {
          id: 'offline', type: 'defer',
          text: '“Let’s take the numbers offline.”',
          reply: '“₪500,000 at full scale” goes into the minutes unchallenged.',
          moods: { ronit: -1 }, honesty: -1, sets: ['numberStands'],
        },
      ],
    },
    {
      id: 'which', speaker: 'ronit', when: { any: [{ flag: 'michalNumber' }, { flag: 'numberStands' }] },
      prompt: 'So which number goes to the board: the ₪113,000 in your paper, or Michal’s ₪500,000?',
      choices: [
        {
          id: 'paper', type: 'evidence',
          text: '“The paper’s ₪113,000. ₪500,000 is a direction, not a figure. It goes in as an upside to be tested in September.”',
          reply: 'Ronit: “Thank you.” Michal is visibly annoyed, but the minutes now say ₪113,000.',
          moods: { ronit: 1, michal: -1 }, honesty: 2, sets: ['recovered'],
        },
        {
          id: 'big', type: 'overclaim',
          text: '“₪500,000. The paper is conservative.”',
          reply: 'Ronit: “Then I would like to see the model that says so.” Michal relaxes; Ronit does not.',
          moods: { ronit: -2 }, honesty: -2, sets: ['overclaimBoard'],
        },
        {
          id: 'both', type: 'defer',
          text: '“Let’s show both and let the board choose.”',
          reply: 'Ronit: “The board will remember the bigger one.”',
          moods: { ronit: -1 }, honesty: -1,
        },
      ],
    },
    {
      id: 'repair', speaker: 'michal', when: { flag: 'michalCorrected' },
      prompt: 'Michal goes quiet and looks at her notes. She does not speak up when Yoav glances at her.',
      choices: [
        {
          id: 'credit', type: 'reframe',
          text: '“Michal pushed for the shadow-mode run that gave us these numbers. The upside she sees is what phase 2 is designed to test.”',
          reply: 'Michal looks up. “And we will know by September.” She is back in the meeting.',
          moods: { michal: 2 }, sets: ['michalRepaired'],
        },
        {
          id: 'move', type: 'defer',
          text: 'Move on to Avi’s question.',
          reply: 'Michal says nothing for the rest of the meeting.',
          sets: ['michalCold'],
        },
      ],
    },
    {
      id: 'it', speaker: 'avi',
      prompt: 'Who supports this at two in the morning, and where does customer data go?',
      choices: [
        {
          id: 'ev', type: 'evidence',
          text: '“The draft tool runs under the data-processing agreement we signed: no training on our data, 30-day retention, hosted in the EU. If it fails, agents write replies by hand as they do today; switching drafts off is one setting. What is not solved is out-of-hours support: the managed-service quote is one of the conditions.”',
          reply: 'Avi: “That I can live with.” He asks for the agreement by email.',
          moods: { avi: 2 }, honesty: 1, sets: ['itPlan'],
        },
        {
          id: 'iso', type: 'overclaim',
          text: '“It is fully secure: the vendor is ISO 27001 certified.”',
          reply: 'Avi: “A certificate is not an answer to who I call at two in the morning.”',
          moods: { avi: -1 }, honesty: -1,
        },
        {
          id: 'gap', type: 'concede',
          text: '“Today the answer is you, Avi, and that is not fair to you. Condition two: an out-of-hours support line from the managed-service provider before go-live.”',
          reply: 'Avi, surprised: “Thank you. Nobody has said that out loud before.”',
          moods: { avi: 1 }, honesty: 1, sets: ['itPlan', 'conceded'],
        },
        {
          id: 'vendor', type: 'defer',
          text: '“We will work that out with the vendor during the build.”',
          reply: 'Avi folds his arms: “So, no.”',
          moods: { avi: -2 }, sets: ['riskOpen'],
        },
      ],
    },
    {
      id: 'team', speaker: 'samir',
      prompt: 'A straight question. Is this about cutting my team?',
      choices: [
        {
          id: 'straight', type: 'evidence',
          text: '“No cuts are in this case. The only cash from people’s time is not hiring two temps next peak, and that was your decision. The rest of the freed time stays with your team, for the backlog and the peak.”',
          reply: 'Samir exhales. “Then I want Olga in the design of the review step.” Yoav agrees.',
          moods: { samir: 2 }, honesty: 1, sets: ['noCuts'],
        },
        {
          id: 'notnow', type: 'defer',
          text: '“Let’s not get into headcount today.”',
          reply: 'Samir hears “yes”. He will tell his team so tonight.',
          moods: { samir: -1 },
        },
        {
          id: 'likely', type: 'inference',
          text: '“The board will expect savings, so some reduction is likely over time.”',
          reply: 'Samir: “Then I would like that in writing before my people train the thing that replaces them.”',
          moods: { samir: -2 }, honesty: -1,
        },
      ],
    },
    {
      id: 'decide', speaker: 'yoav',
      prompt: 'We have five minutes left. What exactly do you want from us?',
      choices: [
        {
          id: 'conditions', type: 'askDecision',
          text: '“Approve phase 1 with conditions: ₪48,000 now; ₪72,000 at the 1 April gate if the four gate conditions in the charter hold (drafts accepted, review time, wrong replies, peak hours); an out-of-hours support line before go-live; the case goes to the board on the 28th. Can we minute that as approved?”',
          reply: 'Yoav looks around the table: “Any objection?”',
          moods: { ronit: 1 }, sets: ['asked', 'conditions'],
        },
        {
          id: 'all', type: 'askDecision',
          text: '“Approve the full ₪120,000 today, so we can move fast.”',
          reply: 'Ronit: “All of it, before anything is measured live?” Yoav looks around the table.',
          moods: { ronit: -1 }, sets: ['asked'],
        },
        {
          id: 'reflect', type: 'defer',
          text: '“I suggest everyone reflects on the paper and we meet again in two weeks.”',
          reply: 'Yoav: “Two weeks is after the board.” He closes his laptop.',
          sets: ['noDecision'],
        },
        {
          id: 'whatever', type: 'defer',
          text: '“Whatever the committee thinks is best.”',
          reply: 'Silence. Yoav: “Then let’s come back to it.”',
          sets: ['noDecision'],
        },
      ],
    },
  ],
  outcomes: [
    {
      id: 'killed', kind: 'killed', title: 'Killed',
      when: { any: [{ support: { lt: 1.4 } }, { all: [{ mood: { who: 'ronit', lte: 0 } }, { mood: { who: 'yoav', lte: 1 } }] }] },
      text: 'Yoav: “Let’s park the AI programme until after the board.” Nobody argues.',
      later: [
        { text: 'Six months later: support costs are unchanged and the board minutes say “evaluating vendors”. The ChatNest account executive is back with a new deck. Olga still drafts Russian replies on her phone, and the shadow-mode numbers are out of date.' },
      ],
    },
    {
      id: 'noAsk', kind: 'sentBack', title: 'Sent back: no decision was asked for, so none was made', when: { flag: 'noDecision' },
      text: 'Nobody said no. Nobody was asked to say yes. The item is “to be continued”.',
      later: [
        { text: 'Six months later: the board meeting passed with “under review”. Spring peak planning went ahead without the pilot. When you finally get a slot in April, the shadow-mode numbers are three months old and Ronit asks you to re-run them.' },
      ],
    },
    {
      id: 'itOpen', kind: 'sentBack', title: 'Sent back: the support and data question is open',
      when: { all: [{ flag: 'riskOpen' }, { mood: { who: 'avi', lte: 1 } }] },
      text: 'Yoav: “Bring Avi’s answer in writing and we will decide next month.”',
      later: [
        { text: 'Six months later: approved in March after Avi’s questions were answered on paper. The pilot started a month late, after the deadline for the April gate, so the first live numbers arrive in July.' },
      ],
    },
    {
      id: 'redo', kind: 'sentBack', title: 'Sent back: Ronit wants the model redone',
      when: { all: [{ honesty: { lte: -3 } }, { mood: { who: 'ronit', lte: 1 } }] },
      text: 'Ronit: “Bring it in the finance template, with every claim labelled measured, directional or assumed.” Yoav agrees.',
      later: [
        { text: 'Six months later: the redone case is approved in March at ₪113,000 a year, the number your paper had all along. Ronit approves it, and adds a note to her folder about the meeting where the number was bigger.' },
      ],
    },
    {
      id: 'conditions', kind: 'conditions', title: 'Approved with conditions',
      when: { all: [{ flag: 'asked' }, { flag: 'conditions' }, { support: { gte: 2.2 } }] },
      text: 'Minuted: phase 1 approved, ₪48,000 released, ₪72,000 at the 1 April gate, out-of-hours support before go-live; the case goes to the board on 28 January.',
      later: [
        { when: INFLATED, text: 'Six months later: the April gate passed, but the board minutes carry a bigger number than your paper. Measured cash by July is about ₪10,000 (the translation contract; the temps saving can only show next winter), as the paper said. Ronit asks why the board heard something else, and your next case (B2B quote drafts) comes back with “show me the actuals first”.' },
        { when: { flag: 'michalCold' }, text: 'Six months later: at the April gate email and web form passed, WhatsApp drafts went back to shadow mode for a fix, and the ₪72,000 was released with WhatsApp re-gated in July. The paper stayed honest. But Michal stopped copying you on the board drafts; you learned about the September agenda from Ronit. You kept the number and lost the sponsor.' },
        { text: 'Six months later: at the April gate email and web form passed, WhatsApp drafts went back to shadow mode for a named fix, and the ₪72,000 was released with WhatsApp re-gated in July. The translation contract was cut in March. Yoav told the board “we fixed the cause first; a measured pilot is next”, and the board asked for the September numbers instead of a bot. Michal presented the April results herself. Samir is planning the next peak without temps.' },
      ],
    },
    {
      id: 'approved', kind: 'approved', title: 'Approved (no conditions)',
      when: { all: [{ flag: 'asked' }, { support: { gte: 2.2 } }] },
      text: 'Minuted: ₪120,000 approved today; the case goes to the board on 28 January.',
      later: [
        { when: INFLATED, text: 'Six months later: all ₪120,000 is spent. Review time crept up to 4.5 minutes a draft in April and nothing was set up to stop it. Cash so far: about ₪10,000. The board minutes have the big number; Ronit adds this case to her folder next to the 2022 CRM.' },
        { text: 'Six months later: the money went out in one go. Review time crept up to 4.5 minutes a draft in April and, with no gate, nobody looked until June. The pilot survived, but Ronit now asks for gates on everything you bring her.' },
      ],
    },
    {
      id: 'thin', kind: 'sentBack', title: 'Sent back: not enough support in the room',
      text: 'Yoav: “I’m not hearing a yes around this table. Let’s take it to the next meeting.”',
      later: [
        { text: 'Six months later: approved in April after a round of one-to-one meetings you could have had before the steering group. The live pilot started after the April gate would have fallen, so the first measured numbers arrive in August.' },
      ],
    },
  ],
  lessonPoint:
    'A steering meeting decides on what it hears first and believes what it can check. Lead with the ask, separate what you measured from what you infer, ' +
    'concede the weak point and tie it to a condition, and ask for the decision in words that can be minuted. When the sponsor argues past the evidence, ' +
    'keep the number in the paper honest without taking their face: label their upside as an assumption to test and give them the credit.',
  notes: [
    'Cash of about ₪113,000 a year, about 570 agent-hours, build ₪120,000 and about ₪49,000 a year to run match the roi-defender and pilot-economics harbor presets.',
    'The board threshold is ₪150,000 total over three years (CFO’s finance summary in the data room).',
    'The date fix went live on 14 January 2027 (course story); the results “six months later” are assumptions for the exercise.',
  ],
};

export const PRESETS = { harbor };
