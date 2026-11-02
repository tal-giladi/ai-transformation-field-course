// Scenarios for discovery-interview. A scenario is a cast, a question menu per person, the facts the
// answers can reveal and the diagnosis options. To add one, copy `harbor`, keep the same fields and
// write new people, questions and facts. Rules for a good scenario are in simulations/README.md.
//
// Question fields:
//   id, who (cast id), type (rapport | open | workflow | numbers | showme | sameword | leading),
//   text, answer, guarded (answer when trust < needTrust), needTrust, requires / requiresAny (flags),
//   sets (flags), reveals (fact ids), trust (change in this person's trust, -1..+2).

export const DEFAULT_PRESET = 'harbor';

const harbor = {
  label: 'Harbor & Pine — first week of discovery',
  brief:
    'It is your first week as Head of AI and Operations Improvement at Harbor & Pine, a 120-person furniture importer. ' +
    'The CEO told the board in September that an AI customer-service bot would cut support cost by 40% within 90 days. ' +
    'Michal, the COO and your sponsor, has given you five interviews this week and asked for one thing on Thursday: ' +
    'what is the real problem? You have time for 12 questions in total. Choose who to ask and what. ' +
    'Some people will only tell you more once you have asked the right thing first, and how you ask changes what they tell you.',
  budget: 12,
  cast: [
    { id: 'michal', name: 'Michal Peretz', role: 'COO, your sponsor', trust: 3 },
    { id: 'samir', name: 'Samir Haddad', role: 'Customer service manager', trust: 1 },
    { id: 'olga', name: 'Olga Petrenko', role: 'Senior support agent', trust: 1 },
    { id: 'tamar', name: 'Tamar Shalev', role: 'Logistics manager', trust: 2 },
    { id: 'yoav', name: 'Yoav Ben-Ami', role: 'CEO', trust: 2 },
  ],
  facts: [
    { id: 'wismo', key: true, text: 'About 38% of support contacts are “where is my order?” (WISMO).' },
    { id: 'spikes', key: true, text: 'WISMO contacts spike a few days after a container is delayed.' },
    { id: 'promisedDate', key: true, text: 'The delivery date promised at checkout comes from a fixed lead-time table in the web store that nobody updates.' },
    { id: 'etaSheet', key: true, text: 'Logistics keeps the real container ETAs in a sheet; they never reach customers or support.' },
    { id: 'lateness', text: 'Containers from Vietnam and China have run a median 11 days late since June.' },
    { id: 'resolved', text: '“Resolved” means a reply was sent, not that the problem was solved; delivery customers write again.' },
    { id: 'kpi', text: 'The “2-hour first response” KPI counts business hours on email only; the web form and weekends are left out.' },
    { id: 'peak', text: 'Support runs at about 92% utilisation in peak season (November to January).' },
    { id: 'shadow', text: 'Agents draft Russian and Arabic replies in free ChatGPT on their phones, pasting customer names and addresses.' },
    { id: 'board', text: 'The CEO has told the board: a bot, and 40% lower support cost.' },
    { id: 'vendorClaim', text: 'The 40% comes from the chatbot vendor’s 70% deflection figure, measured at other clients.' },
    { id: 'yoavFlex', text: 'The CEO would back a different first project if it shows the board a measured result by January.' },
    { id: 'michalWorry', text: 'Michal suspects the delivery promise, not the support team, is the real problem.' },
  ],
  questions: [
    // Michal Peretz, COO
    {
      id: 'm_good', who: 'michal', type: 'open',
      text: 'What would a good result look like for you by the board meeting in January?',
      answer: 'Something the board believes. Yoav has promised them a bot. What I want is for customers to stop being angry with us. Those are not the same thing, and I am not sure anyone has noticed.',
      sets: ['m_angry'],
    },
    {
      id: 'm_night', who: 'michal', type: 'open',
      text: 'What keeps you up at night about deliveries?',
      answer: 'Containers. When a ship is late, the phones go mad about a week later. I keep thinking the problem is the promise we make at checkout, not the people who answer the phone. But I run operations, so of course I would say that.',
      reveals: ['michalWorry'], sets: ['hint_logistics'],
    },
    {
      id: 'm_bot', who: 'michal', type: 'leading', trust: -1,
      text: 'So the plan is the chatbot the CEO announced, right? We just need to pick the vendor?',
      answer: 'If that is how you see your job… yes, Yoav wants ChatNest. I hoped you would look before you buy.',
    },
    {
      id: 'm_kpi', who: 'michal', type: 'numbers',
      text: 'How is support performance measured today, and who produces the numbers?',
      answer: 'Yoav gets a monthly KPI report: first response in 2 hours, 94% of tickets resolved. Samir produces it. I have never checked how it is calculated.',
      sets: ['kpi_hint'],
    },
    {
      id: 'm_board', who: 'michal', type: 'open',
      text: 'What exactly did the board hear about this project?',
      answer: 'You had better ask Yoav. Privately, not in a meeting. He will tell you more one to one.',
      sets: ['ask_yoav_private'],
    },
    {
      id: 'm_chain', who: 'michal', type: 'workflow',
      text: 'Between checkout and delivery, who touches a customer’s order?',
      answer: 'The web store takes the order and shows a delivery date, purchasing has already ordered the container, logistics brings it through the port, the warehouse delivers. Tamar runs logistics. She is the one who knows when things slip.',
      sets: ['hint_logistics'],
    },

    // Samir Haddad, customer service manager
    {
      id: 's_safe', who: 'samir', type: 'rapport', trust: 2,
      text: 'Before we start: I am not here to cut heads, and nothing you tell me goes into a report with your name on it.',
      answer: 'OK. Thank you. People have been nervous since the CEO’s speech. Ask what you need.',
      sets: ['s_safe'],
    },
    {
      id: 's_slow', who: 'samir', type: 'leading', trust: -1,
      text: 'Your team is too slow, isn’t it? A bot would take most of the load off you.',
      answer: 'If you have already decided, why are you asking me?',
    },
    {
      id: 's_sunday', who: 'samir', type: 'workflow', needTrust: 2,
      text: 'Walk me through a normal Sunday morning in the queue.',
      answer: 'Sunday is the worst. The weekend emails plus the web form. Most of them are the same question: where is my sofa? We answer with the date the website gave them. On Wednesday they write again.',
      guarded: 'Busy. We cope. The team works hard.',
      sets: ['wismo_hint'],
    },
    {
      id: 's_share', who: 'samir', type: 'numbers', needTrust: 2,
      text: 'What share of contacts are “where is my order?” Can you pull it from the helpdesk?',
      answer: 'I ran it last month, for myself: about 38%. It is not in the KPI report. Nobody asked, and it makes us look like we cannot answer a simple question.',
      guarded: 'I would have to check. There are a lot of categories.',
      reveals: ['wismo'],
    },
    {
      id: 's_tickets', who: 'samir', type: 'showme', needTrust: 3, requiresAny: ['wismo_hint', 's_safe'],
      text: 'Can you show me ten tickets from last week, the ones where the customer wrote again?',
      answer: 'Look: eight of these ten are from orders on the same container from Vietnam, the one that was ten days late. Same week, same question, same tone. It happens every time a ship is late.',
      guarded: 'I can send you an export at some point.',
      reveals: ['spikes'],
    },
    {
      id: 's_kpi', who: 'samir', type: 'sameword',
      text: 'When the report says “first response in 2 hours”, what exactly is counted?',
      answer: 'Business hours, email channel only. The web form is not in it and weekends do not count. On a real clock it is more like six or seven hours. That is how the report was set up before me.',
      reveals: ['kpi'],
    },
    {
      id: 's_resolved', who: 'samir', type: 'sameword',
      text: 'In your helpdesk, what does “resolved” mean?',
      answer: 'The agent clicks resolved when the reply is sent. Whether the customer is happy, we find out when they write again. With delivery questions, they almost always write again.',
      reveals: ['resolved'],
    },
    {
      id: 's_peak', who: 'samir', type: 'numbers',
      text: 'How full is the team between November and January?',
      answer: 'About 92% of logged time. Please do not put anything new on us before February. Whatever it is.',
      reveals: ['peak'],
    },

    // Olga Petrenko, senior support agent
    {
      id: 'o_safe', who: 'olga', type: 'rapport', trust: 2,
      text: 'I am looking for what works, not for who breaks rules. Anything you show me stays anonymous.',
      answer: 'Good. Then I can be honest with you.',
      sets: ['o_safe'],
    },
    {
      id: 'o_annoying', who: 'olga', type: 'open',
      text: 'What is the most annoying part of your day?',
      answer: 'Telling people a date I know is wrong. The website says 45 days, the container is still at sea, and I cannot see the container dates anyway.',
      sets: ['olga_no_eta'],
    },
    {
      id: 'o_wismo_walk', who: 'olga', type: 'workflow', needTrust: 2,
      text: 'Walk me through what you do when a customer asks where their order is.',
      answer: 'I open the order in Priority and read the promised date. If it has passed, I email logistics and wait. Tamar answers when she can; she has the real dates in her sheet. Nobody else does.',
      guarded: 'I look it up and tell them. Standard.',
      reveals: ['etaSheet'],
    },
    {
      id: 'o_russian', who: 'olga', type: 'showme', needTrust: 3, requires: ['o_safe'],
      text: 'How do you write the Russian replies so fast? Can you show me?',
      answer: '…You promised. I paste the email into ChatGPT on my phone and ask for a polite Russian reply. Yes, with the name and the address, otherwise it does not sound right. Half the team does it, for Arabic too. It saves us an hour a day.',
      guarded: 'Practice. I have been here a long time.',
      reveals: ['shadow'],
    },
    {
      id: 'o_replace', who: 'olga', type: 'leading', trust: -1,
      text: 'You must be worried that AI will replace you?',
      answer: 'I was not, until now.',
    },
    {
      id: 'o_count', who: 'olga', type: 'numbers',
      text: 'Roughly how many of your emails a day are about delivery dates?',
      answer: 'On a Sunday, half my queue. Midweek, maybe a third. Samir has the real numbers, if he will show you.',
    },

    // Tamar Shalev, logistics manager
    {
      id: 't_delay', who: 'tamar', type: 'open',
      text: 'What happens on your side when a container is delayed?',
      answer: 'The forwarder emails me a new ETA and I update my tracking sheet. Then… that is it, really. Nobody has ever asked me who else needs to know.',
      sets: ['t_delay'],
    },
    {
      id: 't_where', who: 'tamar', type: 'workflow', requires: ['t_delay'],
      text: 'After you update the sheet, where does the new ETA go?',
      answer: 'Nowhere, honestly. Purchasing looks at it sometimes. Support emails me one order at a time. The website does not know, so the customer does not know.',
      reveals: ['etaSheet'], sets: ['eta_nowhere'],
    },
    {
      id: 't_date', who: 'tamar', type: 'sameword', requires: ['t_delay'],
      text: 'When a customer sees “delivery date” on the website, where does that date come from?',
      answer: 'From a table in StoreHub: a fixed lead time per supplier country. Vietnam is 45 days. It was set in 2022 and nobody touches it. My sheet says Vietnam has been running late all summer.',
      reveals: ['promisedDate'],
    },
    {
      id: 't_late', who: 'tamar', type: 'numbers',
      text: 'How late are containers running since the summer, by country?',
      answer: 'Vietnam and China: a median of about 11 days late since June. Turkey and Italy are fine. I can give you the sheet.',
      reveals: ['lateness'],
    },
    {
      id: 't_sheet', who: 'tamar', type: 'showme', requires: ['t_delay'],
      text: 'Can I see the tracking sheet?',
      answer: 'Here. About 140 open containers, an ETA column I update every morning from the forwarder’s emails, and a notes column. It is the only place the real dates exist.',
      reveals: ['etaSheet'],
    },
    {
      id: 't_bot', who: 'tamar', type: 'leading', trust: -1,
      text: 'The chatbot will sort out the delivery questions, won’t it?',
      answer: 'Will it read my sheet? No? Then it will tell customers the same wrong date, just faster.',
    },

    // Yoav Ben-Ami, CEO
    {
      id: 'y_success', who: 'yoav', type: 'open',
      text: 'What would make this a success for you in January?',
      answer: 'A bot live on the website and support cost down 40%. That is what I told the board, and I meant it.',
      reveals: ['board'],
    },
    {
      id: 'y_private', who: 'yoav', type: 'open', requires: ['ask_yoav_private'],
      text: 'Just between us: what do you need to be able to tell the board on 28 January?',
      answer: 'That we did something real, with a number I can defend. I said bot because the vendor made it sound easy. If you bring me something better with a measured result, I will stand behind it. I will not stand in front of them with nothing.',
      reveals: ['yoavFlex', 'board'],
    },
    {
      id: 'y_priority', who: 'yoav', type: 'leading', trust: -1,
      text: 'So you would agree the chatbot is the priority?',
      answer: 'Obviously. That is why you are here.',
    },
    {
      id: 'y_40', who: 'yoav', type: 'numbers',
      text: 'Where does the 40% come from?',
      answer: 'ChatNest’s deck. Seventy percent deflection at their other clients; Eitan showed me. Even half of that is a lot of money.',
      reveals: ['vendorClaim'],
    },
    {
      id: 'y_complaint', who: 'yoav', type: 'open',
      text: 'When did you last hear a customer complaint yourself? What was it about?',
      answer: 'Last week, my neighbour. Her sofa was “arriving Thursday” for three Thursdays in a row. Embarrassing.',
    },
  ],
  diagnoses: [
    {
      id: 'bot', text: 'Support is too slow and too expensive; a chatbot should deflect most contacts.',
      feedback: 'This is the stated ask, not the problem. A bot would read the same wrong promised date and give it to customers faster; the 70% deflection was measured elsewhere.',
    },
    {
      id: 'date', correct: true,
      text: 'Customers are promised a delivery date that is never updated when a container slips, so they write in to ask where their order is.',
      feedback: 'This is the real problem. The fix is plain automation, no AI: compare promised dates with the ETAs in the logistics sheet every day and tell customers first. It removes a large share of WISMO contacts and makes any later bot honest.',
    },
    {
      id: 'kpi', text: 'The support KPI is calculated wrongly; fixing the report would show the team performs well.',
      feedback: 'The KPI really is misleading, but it is a symptom. Fixing the report changes the number, not the customers’ experience.',
    },
    {
      id: 'privacy', text: 'Agents paste customer data into free ChatGPT; the main problem is privacy.',
      feedback: 'A real finding that needs action (a governed tool and a data boundary, without punishing the people who found the workaround), but it does not explain why customers are angry.',
    },
    {
      id: 'logistics', text: 'Logistics is too slow to answer support’s emails about orders.',
      feedback: 'Close, but it blames a person for a design gap: the real ETAs exist; the system simply never passes them to the website or to customers.',
    },
  ],
  lessonPoint:
    'The stated ask is a hypothesis, not the problem. Questions about workflow, numbers and what people mean by their words, ' +
    'asked after you have made it safe to answer, find the real work; leading questions only find your own opinion.',
};

export const PRESETS = { harbor };
