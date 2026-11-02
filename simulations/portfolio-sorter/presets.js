// Scenarios for portfolio-sorter. A scenario is a set of use-case cards, the receiving teams (with the
// absorption capacity the learner must ask for), and the expert's view. To add one, copy `harbor` and
// keep the same fields. All money is shekels per month unless the field says otherwise.
//
// Card fields: id, title, proposer, summary, claimedBenefit, benefitBasis, evidence (measured | mixed |
// claim), source (measured | internal | vendor), evidenceText, volume, volumeUnit, errorRate, errorText,
// costPerError, buildCost, team, absorbHours, ceoPriority?, trapPick?, expertRating {value, feasibility,
// risk} (1-5; risk 5 = worst), expertNote, truth (revealed after commit).

export const DEFAULT_PRESET = 'harbor';

const harbor = {
  label: 'Harbor & Pine — nine candidate use cases',
  brief:
    'Three weeks into the job. Discovery is done and nine use cases are on the table at Harbor & Pine: the CEO’s chatbot, ' +
    'ideas from the teams, two things vendors are selling, and one AI feature that is already switched on. Michal wants a ' +
    'portfolio of at most three for the board in January. First you lock your scoring criteria, before you see the list, ' +
    'so that nobody (including you) can bend them to fit a favourite. Then score each card on its evidence, net the cost of ' +
    'errors, and ask the teams that will have to absorb the change what they can actually take on.',
  teams: [
    { id: 'support', name: 'Support', contact: 'Samir Haddad', capacity: 30,
      answer: 'Until February, 30 hours a month, total, for anything new: training, checking, new steps. We are at 92%. From February, maybe double.' },
    { id: 'logistics', name: 'Logistics', contact: 'Tamar Shalev', capacity: 12,
      answer: 'If a job reads my sheet, I need about an hour a week to keep it clean. I can give up to 12 hours a month.' },
    { id: 'sales', name: 'B2B sales', contact: 'Yaniv Carmi', capacity: 20,
      answer: 'Twenty hours a month is fine, as long as someone else builds it.' },
    { id: 'marketing', name: 'Marketing', contact: 'Noa Levi', capacity: 15,
      answer: 'Plenty! Well… realistically 15 hours a month, with the catalogue launch in December.' },
    { id: 'purchasing', name: 'Purchasing', contact: 'the purchasing lead', capacity: 10,
      answer: 'Two buyers, both on container bookings for the spring. Ten hours a month at most.' },
    { id: 'claims', name: 'Claims desk', contact: 'Rina (the damage-claims clerk)', capacity: 4,
      answer: 'I am one person. Four hours a month, and only if it does not touch the log I keep.' },
    { id: 'hr', name: 'HR', contact: 'Dana Katz', capacity: 6,
      answer: 'Peak-season hiring for the warehouse. Six hours a month.' },
  ],
  cards: [
    {
      id: 'chatbot', title: 'Customer-service chatbot', proposer: 'Yoav Ben-Ami, CEO (announced to the board)',
      summary: 'A web chat bot from ChatNest answers customers 24/7 and hands over to an agent when it cannot.',
      claimedBenefit: 113000, benefitBasis: '40% of ₪3.4M a year support cost, from the vendor’s 70% deflection',
      evidence: 'claim', source: 'vendor', evidenceText: 'Vendor deck: “70% of contacts deflected”. Demo built by the vendor.',
      volume: 4200, volumeUnit: 'bot answers a month', errorRate: 0.1, errorText: 'a wrong or made-up answer', costPerError: 150,
      buildCost: 380000, team: 'support', absorbHours: 60, ceoPriority: true, trapPick: true,
      expertRating: { value: 2, feasibility: 2, risk: 4 },
      expertNote: 'Later, on Harbor & Pine’s own data, after the date fix.',
      truth: 'The 70% was measured on US English retail with order tracking integrated. Here 38% of contacts are “where is my order?” and the bot would read the same wrong promised date. The demo ran on the 2023 catalogue copy. Realistic deflection: about 10–15%.',
    },
    {
      id: 'delayNotify', title: 'Promised-date fix and proactive delay emails', proposer: 'You, from the discovery interviews',
      summary: 'A daily job compares each open order’s promised date with the container ETA in the logistics sheet, emails the customer when it slips, and updates the checkout lead times. No AI.',
      claimedBenefit: 16000, benefitBasis: 'about 1,150 fewer WISMO contacts a month × 6.5 min × ₪130 an hour',
      evidence: 'measured', source: 'measured', evidenceText: 'Helpdesk export: WISMO is 38% of contacts and clusters about 12 days after a container’s original ETA, just after the promised date passes. Orders: a median 11 days late for Vietnam and China since June.',
      volume: 210, volumeUnit: 'delay emails a month', errorRate: 0.02, errorText: 'a wrong ETA in the sheet sent to a customer', costPerError: 60,
      buildCost: 35000, team: 'logistics', absorbHours: 4,
      expertRating: { value: 5, feasibility: 5, risk: 1 },
      expertNote: 'Do first. Plain automation, cheap, measured, and it makes any later bot honest.',
      truth: 'Needs no AI. Six weeks after launch WISMO contacts fell by about half and order cancellations dropped. It also gave the CEO a measured result for the board.',
    },
    {
      id: 'emailDrafts', title: 'Support-email triage and draft replies', proposer: 'Samir Haddad and Olga Petrenko, support',
      summary: 'AI sorts incoming emails (damage, assembly, returns, B2B quotes) and drafts a reply in Hebrew, Arabic, Russian or English. An agent checks and sends every reply.',
      claimedBenefit: 10000, benefitBasis: 'about 109 hours a month freed after review time (pilot-economics model)',
      evidence: 'mixed', source: 'internal', evidenceText: 'Time sheets: email is about 70% of logged support time (measured). Minutes saved per draft: estimated from Olga’s own use.',
      volume: 1920, volumeUnit: 'drafts a month', errorRate: 0.015, errorText: 'a wrong reply that gets past the review', costPerError: 120,
      buildCost: 120000, team: 'support', absorbHours: 25,
      expertRating: { value: 4, feasibility: 4, risk: 2 },
      expertNote: 'Pilot from February, after peak season, with the source shown beside each draft.',
      truth: 'Worked once the review screen showed the customer’s email and the order beside the draft. It also replaced a privacy problem: agents had been drafting Russian and Arabic replies in free ChatGPT with customer data.',
    },
    {
      id: 'quotes', title: 'B2B quote drafting assistant', proposer: 'Yaniv Carmi, Head of B2B Sales',
      summary: 'Drafts hotel and office quotes from the customer’s request email, ready for a salesperson to check and send.',
      claimedBenefit: 8750, benefitBasis: '140 quotes a month × 25 min saved × ₪150 an hour',
      evidence: 'measured', source: 'measured', evidenceText: 'Two-week time study by the sales lead: 68 quotes, 45 minutes each on average. Two-week trial of a draft tool.',
      volume: 140, volumeUnit: 'quotes a month', errorRate: 0.04, errorText: 'a wrong price or discount that reaches the customer', costPerError: 900,
      buildCost: 70000, team: 'sales', absorbHours: 10,
      expertRating: { value: 3, feasibility: 4, risk: 3 },
      expertNote: 'Yes, with one condition: prices are read from Priority, never written by the model.',
      truth: 'The 4% error rate came from the trial, where the model wrote the prices itself. Reading prices from the ERP cut wrong prices to under 1%, and the net benefit roughly doubled.',
    },
    {
      id: 'copy', title: 'AI marketing copy generator', proposer: 'Noa Levi, marketing director',
      summary: 'A copywriting tool writes product descriptions and newsletter text in four languages.',
      claimedBenefit: 2600, benefitBasis: '20 hours a month of copywriting, Noa’s estimate',
      evidence: 'claim', source: 'internal', evidenceText: 'Noa’s estimate. No measurement.',
      volume: 300, volumeUnit: 'texts a month', errorRate: 0.02, errorText: 'a wrong dimension or material on a product page', costPerError: 250,
      buildCost: 15000, team: 'marketing', absorbHours: 8,
      expertRating: { value: 2, feasibility: 5, risk: 2 },
      expertNote: 'Not a portfolio bet: a governance decision (approve one tool, set the data boundary).',
      truth: 'Marketing already uses CopyGenie Pro, paid on a personal card. The real decision is to approve one business tool with a data boundary and a fact check against the product master, not to fund a project.',
    },
    {
      id: 'reorder', title: 'ERP “AI smart reorder” module', proposer: 'The ERP reseller, via purchasing',
      summary: 'An add-on module suggests purchase orders automatically to cut inventory.',
      claimedBenefit: 25000, benefitBasis: 'vendor: 15% less inventory carrying cost',
      evidence: 'claim', source: 'vendor', evidenceText: 'Reseller case study from another customer.',
      volume: 1800, volumeUnit: 'SKU suggestions a month', errorRate: 0.03, errorText: 'a stock-out or an over-order', costPerError: 160,
      buildCost: 90000, team: 'purchasing', absorbHours: 15, trapPick: true,
      expertRating: { value: 1, feasibility: 3, risk: 3 },
      expertNote: 'No. Not AI, and the case study does not transfer.',
      truth: 'It is a rules engine (minimum and maximum thresholds) marketed as AI. The case study was a grocery distributor with weekly deliveries, not 60-day sea containers. Purchasing already runs the same min/max rules.',
    },
    {
      id: 'damageClaims', title: 'Automatic damage-claim decisions', proposer: 'Ronit Avraham, CFO',
      summary: 'A model approves or rejects customer damage claims from the photos and the order, without waiting for a person.',
      claimedBenefit: 3250, benefitBasis: '25 hours a month of Rina’s time × ₪130 an hour',
      evidence: 'mixed', source: 'internal', evidenceText: 'Volume measured: about 260 claims a month. Accuracy: assumed from a vendor webinar.',
      volume: 260, volumeUnit: 'claims a month', errorRate: 0.12, errorText: 'a valid claim rejected or an invalid one paid', costPerError: 1200,
      buildCost: 80000, team: 'claims', absorbHours: 12, trapPick: true,
      expertRating: { value: 1, feasibility: 1, risk: 5 },
      expertNote: 'Not now. First record every claim’s outcome for three months.',
      truth: 'The approval outcome is missing for about 35% of claims, so there are no labels to train or test on. The “QA review within 48 hours” in the handbook exists only on paper. A wrong rejection is a consumer-protection complaint.',
    },
    {
      id: 'hrMatch', title: 'PeopleWise AI candidate match', proposer: 'Already on (HR software update)',
      summary: 'The HR system ranks job applicants by “fit” for each opening.',
      claimedBenefit: 2000, benefitBasis: 'vendor release notes: hire 30% faster',
      evidence: 'claim', source: 'vendor', evidenceText: 'Vendor release notes.',
      volume: 120, volumeUnit: 'applicants ranked a month', errorRate: 0.01, errorText: 'an unfair ranking that leads to a discrimination complaint', costPerError: 20000,
      buildCost: 0, team: 'hr', absorbHours: 6, trapPick: true,
      expertRating: { value: 1, feasibility: 5, risk: 5 },
      expertNote: 'Not a bet: switch it off until it has been reviewed, and add it to the AI inventory.',
      truth: 'Nobody decided to use it: an automatic update turned it on in March 2026, and HR did not know. It belongs in the AI inventory and the risk review, not in the portfolio.',
    },
    {
      id: 'assembly', title: 'Assembly-question answers from supplier manuals', proposer: 'Olga Petrenko, support',
      summary: 'AI answers “how do I assemble this?” questions from the supplier manuals, for an agent to check and send.',
      claimedBenefit: 8200, benefitBasis: '540 assembly questions a month (measured) × 80% answered × 7 min',
      evidence: 'mixed', source: 'internal', evidenceText: 'Volume measured: assembly questions are about 9% of tickets. Answer quality: five tries in a chat tool.',
      volume: 430, volumeUnit: 'answers a month', errorRate: 0.05, errorText: 'a wrong instruction (a broken item, or an injury)', costPerError: 300,
      buildCost: 60000, team: 'support', absorbHours: 20,
      expertRating: { value: 3, feasibility: 2, risk: 3 },
      expertNote: 'Later: after the email pilot has built the review routine and the manuals are cleaned.',
      truth: 'About 40% of the supplier manuals are scanned images with poor translations. A good second wave for support, not a first one: support cannot absorb two changes before February.',
    },
  ],
  expert: {
    criteria: {
      weights: { value: 40, feasibility: 30, risk: 30 },
      rules: { netErrors: true, halfClaims: true, askCapacity: true, ceoBonus: false, vendorAsMeasured: false },
    },
    picks: ['delayNotify', 'emailDrafts', 'quotes'],
    mustHave: 'delayNotify',
    summary: 'Date fix first (no AI, measured, cheap), the support-email pilot from February, and B2B quote drafts with prices read from the ERP. The chatbot waits for its own data; the HR feature and the copy tool are governance decisions, not bets.',
  },
  lessonPoint:
    'Lock the criteria before you open the list, score on evidence rather than on who proposed it, net the expected cost of errors from every benefit, and ask the receiving team what it can absorb. ' +
    'At Harbor & Pine the best first move needs no AI at all.',
};

export const PRESETS = { harbor };
