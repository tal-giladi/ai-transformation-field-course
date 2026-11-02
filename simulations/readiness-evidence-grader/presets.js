// Scenarios for readiness-evidence-grader. A scenario is a pile of dated evidence items, the true
// status of each, the verdict options and how a steering group reacts to each verdict when the report
// is honest and when it is over-claimed. To add one, copy `harbor` and keep the same fields;
// `validateScenario` in model.js checks the data.
//
// Item fields: id, kind (interview | dashboard | policy | export | vendor | email | screen), source,
//   date (shown as written), area (readiness dimension), text, truth (verified | reported |
//   contradicted), by [item ids that verify or contradict it], why, challenge (what someone in the
//   steering group asks if it is called verified; needed for every item that is not verified).
// Verdict fields: id, label, text, best?, reactions { honest, overclaimed }, tones { honest, overclaimed }
//   (good | warn | bad), changeIt (what would change the verdict).

export const DEFAULT_PRESET = 'harbor';

const harbor = {
  label: 'Harbor & Pine — readiness evidence, November 2026',
  brief:
    'Mid-November 2026, two weeks into the job. Your readiness assessment for Harbor & Pine is due at Thursday’s steering group. ' +
    'You have 17 pieces of evidence: interview notes, a KPI report, the handbook, profiles of the data exports you ran yourself, vendor ' +
    'material and some emails. Sort each one: verified (you checked it against data you hold, or saw it yourself), reported (someone ' +
    'says so; you have not checked) or contradicted (data you hold says otherwise). Every finding keeps its date and source. Then choose a ' +
    'verdict, proceed, phase or not yet, and see how the steering group reacts.',
  overclaimThreshold: 2,
  items: [
    {
      id: 'samirWismo', kind: 'interview', source: 'Samir Haddad, customer service manager', date: '10 Nov 2026', area: 'Value',
      text: '“About a third of our contacts are customers asking where their order is.”',
      truth: 'verified', by: ['tickets'], why: 'Your own profile of the ticket export shows 38%, once the old and new delivery categories are combined. Reported by Samir, verified by the data.',
    },
    {
      id: 'tickets', kind: 'export', source: 'You: profile of tickets.csv (1 May–31 Oct 2026)', date: '6 Nov 2026', area: 'Data',
      text: '2,529 tickets. “Where is my order?” is 38% once “Delivery” (before 1 July) and “Delivery status” (after) are combined; 28% sit in “Other”; about 6% are duplicates sent within an hour.',
      truth: 'verified', why: 'Your own analysis of a full export, with the category change found and handled.',
    },
    {
      id: 'kpi', kind: 'dashboard', source: 'Q3 KPI report (customer service with Finance BI)', date: '6 Oct 2026', area: 'Process',
      text: 'Average first response 2.0 hours, target met; resolution rate 100%.',
      truth: 'contradicted', by: ['times'], why: 'The report counts business hours, email only, weekdays only, and “resolved” means a reply was sent. Your export says otherwise.',
      challenge: 'Ronit: “Your report lists ‘first response 2 hours’ as verified. Your own export says a median of 6.1 hours. Which one is true?”',
    },
    {
      id: 'times', kind: 'export', source: 'You: same export, all channels and all days', date: '7 Nov 2026', area: 'Process',
      text: 'Median first response 6.1 hours (clock time, all channels; 6.5 in Q3 alone). 23% of tickets marked “resolved” are followed by a new ticket from the same customer about the same order within 14 days.',
      truth: 'verified', why: 'Computed from timestamps in a full export.',
    },
    {
      id: 'handbook', kind: 'policy', source: 'Customer service handbook, page 12', date: 'March 2024', area: 'Governance',
      text: '“Damage claims are reviewed by QA within 48 hours.”',
      truth: 'contradicted', by: ['claims'], why: 'There is no QA role and no QA step in the claims log. A step that exists only on paper.',
      challenge: 'Michal: “If QA reviews every claim, why does Rina’s log have no outcome for a third of them?”',
    },
    {
      id: 'claims', kind: 'export', source: 'You: profile of damage-claims-log.csv (kept by Rina)', date: '7 Nov 2026', area: 'Data',
      text: 'Outcome missing for 32% of claims. No QA field. The org chart has no QA role.',
      truth: 'verified', why: 'Your own profile of the only record of claim outcomes. It also means these outcomes cannot be used as training labels yet.',
    },
    {
      id: 'chatnest', kind: 'vendor', source: 'ChatNest sales deck (Eitan Gross)', date: 'Sep 2026', area: 'Value',
      text: '“Our bot deflects 70% of customer contacts.”',
      truth: 'reported', why: 'A vendor figure measured at other clients (US English retail, with order tracking integrated). Nothing you hold contradicts it, and nothing checks it for Harbor & Pine. Report it, with its conditions.',
      challenge: 'Ronit: “Verified by whom? The 70% was measured at other clients, on US English retail.”',
    },
    {
      id: 'avi', kind: 'interview', source: 'Avi Mizrahi, IT manager', date: '11 Nov 2026', area: 'Technology and security',
      text: '“Nobody here puts customer data into ChatGPT. It is against policy.”',
      truth: 'contradicted', by: ['proxy'], why: 'The proxy log shows AI chat sites on seven support machines. Avi believes the policy; the log shows practice.',
      challenge: 'Yoav: “You list Avi’s statement as verified, and two pages later the proxy log shows ChatGPT on seven support machines?”',
    },
    {
      id: 'proxy', kind: 'export', source: 'You: profile of proxy-log.csv (October)', date: '6 Nov 2026', area: 'Technology and security',
      text: 'chatgpt.com and chat.openai.com: 4 Customer Service users (160 requests), plus 2 in Marketing and 1 in Purchasing; Gemini 2 more. Logged, not blocked.',
      truth: 'verified', why: 'Your own analysis of the log.',
    },
    {
      id: 'olga', kind: 'interview', source: 'Senior support agent (not attributed)', date: '11 Nov 2026', area: 'People',
      text: '“I draft the Russian replies in ChatGPT, on my own Google login. It is much faster.”',
      truth: 'reported', why: 'Consistent with the proxy log, but the log shows a pseudonymised user, not her, and you did not see it. Report it, unattributed, as consistent with what the log shows.',
      challenge: 'Avi: “How did you verify that? And who is this?” The room starts guessing names.',
    },
    {
      id: 'eta', kind: 'email', source: 'Tamar Shalev to the logistics mailbox', date: '28 Oct 2026', area: 'Process',
      text: '“Container from Ho Chi Minh delayed 14 days; ETA updated in the tracking sheet.” You checked: the sheet has the new ETA, and the 41 orders on that container still show the old promised date in StoreHub.',
      truth: 'verified', why: 'You checked the email against the tracking sheet and the orders yourself: the real ETAs exist and never reach customers.',
    },
    {
      id: 'storehub', kind: 'screen', source: 'StoreHub delivery settings (you, with the web manager)', date: '6 Nov 2026', area: 'Data',
      text: 'Lead-time table: Vietnam 42 days, China 38, Turkey 21, Italy 28. Last edited 14 February 2023.',
      truth: 'verified', why: 'You saw the settings yourself. This is where the promised date comes from.',
    },
    {
      id: 'paperwork', kind: 'interview', source: 'Samir Haddad, customer service manager', date: '10 Nov 2026', area: 'People',
      text: '“My agents spend about half their day on damage-claim paperwork.”',
      truth: 'reported', why: 'Plausible, but nothing measures it: the timesheets have three coarse buckets and the claims log records no time. Report it and say how you would measure it.',
      challenge: 'Ronit: “Half the day on paperwork: where is that measured? The timesheets have three buckets.”',
    },
    {
      id: 'timesheets', kind: 'export', source: 'You: profile of timesheets.csv', date: '8 Nov 2026', area: 'People',
      text: 'Support ran at 92% utilisation in the November 2025–January 2026 peak. The “email” bucket is about 70% of logged time.',
      truth: 'verified', why: 'Your own analysis. The buckets are coarse, so say what they can and cannot show.',
    },
    {
      id: 'dana', kind: 'interview', source: 'Dana Katz, HR manager', date: '12 Nov 2026', area: 'Governance',
      text: '“We do not use any AI in hiring.”',
      truth: 'contradicted', by: ['peoplewise'], why: 'The PeopleWise update switched an AI candidate match on in March. Dana did not know.',
      challenge: 'Dana, in the meeting: “I told you we don’t use AI.” Avi puts the PeopleWise settings on the screen: the AI match is on.',
    },
    {
      id: 'peoplewise', kind: 'screen', source: 'PeopleWise release notes, and the settings you opened with Dana', date: '6 Nov 2026', area: 'Governance',
      text: 'Release notes (14 March 2026): “AI candidate match is now on by default.” In the settings: on, and 212 candidates have a match score.',
      truth: 'verified', why: 'The vendor’s note alone would be reported; you checked the setting yourself with the owner.',
    },
    {
      id: 'deskly', kind: 'vendor', source: 'Email from Deskly’s account manager to Avi', date: '3 Nov 2026', area: 'Technology and security',
      text: '“Customer content is never used to train our models and is deleted after 90 days.”',
      truth: 'contradicted', by: ['desklyTerms'], why: 'The signed add-on terms say otherwise: §3.2 lets Deskly train on de-identified content unless you opt out in writing, and §3.4 keeps prompts and outputs 24 months in analytics. A sales email does not change a contract.',
      challenge: 'Ronit: “Which document binds us, the email or the terms we signed?” Nobody had compared them.',
    },
    {
      id: 'desklyTerms', kind: 'policy', source: 'Deskly AI add-on terms of service, as received by Samir with the quote', date: '14 Oct 2026', area: 'Technology and security',
      text: '§3.2: Deskly may use customer content in de-identified form to train and evaluate models unless the customer opts out in writing. §3.4: prompts and outputs kept 30 days, and 24 months in the analytics store.',
      truth: 'verified', why: 'You read the terms yourself, clause by clause. What they say is verified; whether the settings match them is the next check.',
    },
  ],
  verdicts: [
    {
      id: 'proceed', label: 'Proceed',
      text: 'Start the AI pilots now: the draft replies and the chatbot evaluation.',
      reactions: {
        honest: 'Ronit reads your own findings back to you: “The KPI is wrong, a third of claim outcomes are missing, staff paste customer data into ChatGPT, and you want to proceed?” Sent back to come with a phased plan.',
        overclaimed: 'Approved quickly: the report says most things are verified. Six weeks later the 2-hour KPI, the QA step and “nobody uses ChatGPT” turn out to be paper. The pilot stalls, and your report is the thing people quote.',
      },
      tones: { honest: 'warn', overclaimed: 'bad' },
      changeIt: 'Recorded claim outcomes, an AI-use rule in force, and the date fix measured.',
    },
    {
      id: 'phase', label: 'Phase', best: true,
      text: 'The promised-date fix (no AI) now; the draft-reply pilot from February in shadow mode, once claim outcomes are recorded and the AI-use rule is out; the chatbot not yet.',
      reactions: {
        honest: 'Approved. Ronit: “Every finding has a date and a source; I can check any of them.” Yoav takes the date fix to the board as the first measured result, and the February conditions are minuted with owners.',
        overclaimed: 'Approved, on conditions built on findings you called verified. When the first one falls over in the meeting, the group starts re-checking all your other findings, and the February start slips while they do.',
      },
      tones: { honest: 'good', overclaimed: 'warn' },
      changeIt: 'To proceed with the draft pilot: four weeks of recorded claim outcomes and the AI-use rule published. To consider the chatbot: a quarter of the date fix measured, and the vendor showing deflection on Harbor & Pine’s own data.',
    },
    {
      id: 'notYet', label: 'Not yet',
      text: 'No AI work until the data, the policies and the support KPIs are fixed.',
      reactions: {
        honest: 'Yoav: “So we do nothing until when?” Your own verified findings support a fix that needs no AI (the promised date) and a pilot that can start in shadow mode. The group asks you to come back next week with a phased plan.',
        overclaimed: 'The group is confused: your report says most things are verified and fine, and your verdict says nothing is ready. Sent back.',
      },
      tones: { honest: 'warn', overclaimed: 'bad' },
      changeIt: 'Not yet is right for the chatbot, not for everything: a verdict can differ by use case.',
    },
  ],
  lessonPoint:
    'A readiness finding is only as strong as its source and its date. Mark each one verified, reported or contradicted, and keep the date: ' +
    'an interview tells you where to look, a policy tells you what should happen, and only data you hold tells you what does. ' +
    'An honest report with three contradictions in it gets a phased yes; a report that calls everything verified gets a fast yes and a slow collapse.',
  notes: [
    'Percentages, the KPI definitions, the missing outcomes, the proxy log, the PeopleWise update and the stale lead-time table follow the planted findings in the data room.',
    'The 41 orders on the delayed container, the 212 scored candidates, the Deskly terms and the meeting reactions are assumptions for the exercise.',
  ],
};

export const PRESETS = { harbor };
