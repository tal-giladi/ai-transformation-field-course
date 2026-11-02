// Scenarios for operating-model-scaler. A scenario is pure data; `validateScenario` in model.js checks it.
//
// Fields: label, brief, startYear, quarters, units [{ id, name, maturity (1–3), appetite (0–1: how
//   readily it builds outside the process when it waits), pilots [{ t (theme; the same theme in two
//   units is a duplicate), name, r (low | med | high), weak? (would fail a proper review), dependsOn? }] }],
//   arrivals [{ q, unit, t, name, r, weak? }] (new pilots during the three years),
//   money { budgetPerYear, slotCost (₪ per review slot per quarter), coe { central, federated, hub } (₪ per
//     quarter for the central team), roads { platform | templates | catalogue: { build, run, lead } },
//     runOnPlatform, runOffPlatform (₪ per pilot in production per quarter), reorg },
//   build { byMaturity { 1, 2, 3 } (quarters to make a pilot production-ready), central (quarters when the
//     central team builds), centralCapacity (pilots the central team works on at once), platformSaves },
//   review { templatesFactor }, shadow { waitQuarters, rate }, risk { base { low, med, high }, weakFactor,
//     shadowFactor, platformFactor, validation { full, standard, light, standards } },
//   regulator { findingQuarters, badAnswerQuarters }, keyPerson { documented, undocumented: { share, quarters } },
//   driftTheme, events [{ id, q (0-based quarter), title, text, inject?, wave?, resultNotLive?, options [{ id,
//     text, result, resultClean?, resultFinding?, resultBad?, effects }] }],
//   startConfig, federatedConfig, naiveAnswers, expert { config, answers, why }, hubSpoke, verdict, notes,
//   lessonPoint.
// Effects: cost, appetite, shadow (kill | adopt), merge (theme), killTheme, regulator (answer | delay |
//   vendorList), keyPerson (contractor | second | accept), budgetCut (share), slotsCut, pausePlatform
//   (quarters), drift (retire | retrain | keep), wave (route | ignore). Regulator results are this model’s
//   consequences, not a statement of what a real supervisor does.

export const DEFAULT_PRESET = 'crescent';

const pil = (t, name, r, extra = {}) => ({ t, name, r, ...extra });

const HUB_SPOKE = [
  { id: 'platform', road: 'platform', text: 'The shared platform: hosting, access control, logging, monitoring', expert: 'hub', why: 'Built once, used by every unit; it is what makes a paved road paved.' },
  { id: 'templates', road: 'templates', text: 'Standards, templates and the evaluation kit', expert: 'hub', why: 'The same test everywhere lets units decide low- and medium-risk go-lives safely.' },
  { id: 'catalogue', road: 'catalogue', text: 'The catalogue of every model and AI tool, with an owner', expert: 'hub', why: 'Duplicates, shadow builds and the regulator’s question are all answered from it.' },
  { id: 'highRisk', text: 'Independent validation of high-risk models', expert: 'hub', why: 'Model risk management is a constant: the same bar for every unit, run by people who did not build it.' },
  { id: 'lowRisk', text: 'The go-live decision for low-risk tools on the paved road', expert: 'spoke', why: 'Centralising it fills the queue with work that does not need a central eye.' },
  { id: 'build', text: 'Building the use case: discovery, domain knowledge, the people who use it', expert: 'spoke', why: 'Units know the work; a central team far from it builds slowly and builds the wrong thing.' },
  { id: 'adoption', text: 'Adoption and training in the unit', expert: 'spoke', why: 'Only the unit can change how its people work.' },
];

const crescent = {
  label: 'Crescent Bank — 40 pilots, nothing in production',
  brief:
    'Crescent Bank has 4,000 staff in 14 business units and 40 AI pilots, none in production. Every pilot today waits for one central ' +
    'committee that validates every model in full. You are asked to design how AI gets from pilot to production for the next three ' +
    'years: the operating model, who decides go-live, how many central review slots a quarter, how deep model risk validation goes, ' +
    'and which paved roads to fund. Then you play twelve quarters, answer what happens (shadow builds, duplicates, a supervisor’s ' +
    'question, a resignation, a budget cut) and adjust the design whenever you like. Done means pilots in production, few incidents, ' +
    'no shadow estate and a budget you can defend.',
  startYear: 2027,
  quarters: 12,
  units: [
    { id: 'retail', name: 'Retail Banking', maturity: 2, appetite: 0.6, pilots: [pil('complaints', 'Complaint summaries', 'med'), pil('nbo', 'Next-best-offer prompts', 'med', { weak: true }), pil('branch-faq', 'Branch staff FAQ assistant', 'low'), pil('churn', 'Churn early warning', 'med')] },
    { id: 'mortgages', name: 'Mortgages', maturity: 1, appetite: 0.3, pilots: [pil('doc-extract', 'Mortgage document extraction', 'med'), pil('valuation', 'Valuation sanity check', 'high', { weak: true }), pil('mortgage-faq', 'Mortgage FAQ for advisers', 'low'), pil('broker-emails', 'Broker email drafts', 'low', { weak: true })] },
    { id: 'cards', name: 'Cards & Payments', maturity: 3, appetite: 0.8, pilots: [pil('complaints', 'Complaint summaries', 'med'), pil('fraud-triage', 'Fraud alert triage', 'high'), pil('dispute-letters', 'Dispute letter drafts', 'low'), pil('chargeback', 'Chargeback case summaries', 'low', { weak: true })] },
    { id: 'sme', name: 'SME Banking', maturity: 2, appetite: 0.5, pilots: [pil('credit-memo', 'Credit memo drafts', 'high'), pil('kyc-docs', 'KYC document checks', 'med'), pil('preapproval', 'SME credit pre-approval', 'high')] },
    { id: 'corporate', name: 'Corporate Banking', maturity: 2, appetite: 0.3, pilots: [pil('credit-memo', 'Credit memo drafts', 'high'), pil('rm-briefs', 'Relationship-manager briefs', 'low')] },
    { id: 'private', name: 'Private Banking', maturity: 1, appetite: 0.2, pilots: [pil('client-letters', 'Client letter drafts', 'low', { weak: true }), pil('portfolio-comment', 'Portfolio commentary', 'high', { weak: true })] },
    { id: 'treasury', name: 'Treasury & Markets', maturity: 3, appetite: 0.4, pilots: [pil('market-summaries', 'Daily market summaries', 'low'), pil('surveillance', 'Trade surveillance alerts', 'high'), pil('liquidity', 'Liquidity forecast', 'high')] },
    { id: 'creditrisk', name: 'Credit Risk', maturity: 3, appetite: 0.2, pilots: [pil('early-warning', 'Early-warning signals', 'high'), pil('covenants', 'Covenant extraction', 'med')] },
    { id: 'compliance', name: 'Compliance & AML', maturity: 2, appetite: 0.3, pilots: [pil('kyc-docs', 'KYC document checks', 'med'), pil('aml-triage', 'AML alert triage', 'high', { weak: true })] },
    { id: 'ops', name: 'Operations', maturity: 2, appetite: 0.5, pilots: [pil('assistant', 'Bank-wide assistant rollout', 'low'), pil('procedures', 'Procedure assistant', 'low', { dependsOn: 'assistant' }), pil('reconciliation', 'Reconciliation exceptions', 'med')] },
    { id: 'contact', name: 'Contact Centre', maturity: 2, appetite: 0.7, pilots: [pil('call-summary', 'Call summaries', 'med'), pil('knowledge', 'Agent knowledge assistant', 'low', { dependsOn: 'assistant' }), pil('complaint-routing', 'Complaint routing', 'med', { weak: true })] },
    { id: 'digital', name: 'Digital Channels', maturity: 3, appetite: 0.9, pilots: [pil('chatbot', 'Customer chatbot', 'med', { weak: true }), pil('call-summary', 'Call summaries', 'med'), pil('app-search', 'In-app search', 'low')] },
    { id: 'hr', name: 'HR', maturity: 1, appetite: 0.4, pilots: [pil('cv-screening', 'CV screening', 'high', { weak: true }), pil('policy-faq', 'HR policy FAQ', 'low')] },
    { id: 'finance', name: 'Finance', maturity: 2, appetite: 0.3, pilots: [pil('variance', 'Variance commentary', 'low'), pil('invoice-match', 'Invoice matching', 'low'), pil('expense-audit', 'Expense audit sampling', 'med')] },
  ],
  arrivals: [
    { q: 3, unit: 'treasury', t: 'fx-commentary', name: 'FX client commentary', r: 'low' },
    { q: 5, unit: 'sme', t: 'cashflow', name: 'Cash-flow insights for SME clients', r: 'med' },
    { q: 7, unit: 'retail', t: 'call-summary', name: 'Branch call summaries', r: 'med' },
  ],
  money: {
    budgetPerYear: 11000000,
    slotCost: 150000,
    coe: { central: 1200000, federated: 300000, hub: 800000 },
    roads: {
      platform: { build: 2400000, run: 300000, lead: 2 },
      templates: { build: 200000, run: 40000, lead: 1 },
      catalogue: { build: 150000, run: 25000, lead: 1 },
    },
    runOnPlatform: 20000,
    runOffPlatform: 45000,
    reorg: 300000,
  },
  build: { byMaturity: { 1: 3, 2: 2, 3: 2 }, central: 2, centralCapacity: 8, platformSaves: 1 },
  review: { templatesFactor: 1.5 },
  shadow: { waitQuarters: 2, rate: 0.35 },
  risk: {
    base: { low: 0.01, med: 0.03, high: 0.06 },
    weakFactor: 3, shadowFactor: 2, platformFactor: 0.5,
    validation: { full: 0.3, standard: 0.45, light: 0.7, standards: 0.6 },
  },
  regulator: { findingQuarters: 2, badAnswerQuarters: 3 },
  keyPerson: { documented: { share: 0.2, quarters: 1 }, undocumented: { share: 0.4, quarters: 2 } },
  driftTheme: 'preapproval',
  events: [
    {
      id: 'shadow', q: 1, title: 'Shadow builds surface',
      text: 'Information security finds two AI tools in daily use that never went near the process: Cards drafts dispute letters through a public chatbot API paid on a credit card, and Digital writes marketing copy on a personal subscription.',
      inject: [
        { unit: 'cards', t: 'shadow-cards-api', name: 'Dispute letters on a public chatbot API', r: 'med' },
        { unit: 'digital', t: 'shadow-digital-copy', name: 'Marketing copy on a personal subscription', r: 'med' },
      ],
      options: [
        { id: 'adopt', text: 'Bring both into the process: catalogue them, review them, and move them onto the paved road', result: 'Both go into the review queue. The units see that coming forward is safe.', effects: { shadow: 'adopt' } },
        { id: 'kill', text: 'Shut both down and send a warning to every unit head', result: 'Both are switched off. The next ones will be better hidden: every unit’s appetite for building outside the process rises.', effects: { shadow: 'kill', appetite: 0.15 } },
        { id: 'leave', text: 'Note them and move on; there is no time', result: 'Both keep running, unreviewed.', effects: {} },
      ],
    },
    {
      id: 'duplicates', q: 2, title: 'The same build, twice',
      text: 'Retail Banking and Cards are both building complaint summarisation, on two different vendors, with two budgets. Each says theirs is further along.',
      options: [
        { id: 'merge', text: 'Merge: one build owned by Cards (the more mature unit), serving both', result: 'One build, one vendor, one owner; Retail’s team joins it.', effects: { merge: 'complaints' } },
        { id: 'both', text: 'Let both continue; competition is healthy', result: 'Both continue. Two vendors, two reviews, two run costs.', effects: {} },
        { id: 'stopBoth', text: 'Stop both until there is a bank-wide design', result: 'Both are stopped. Complaints stay manual.', effects: { killTheme: 'complaints' } },
      ],
    },
    {
      id: 'regulator', q: 4, title: 'The supervisor asks',
      text: 'The bank’s supervisor asks for an inventory of AI and models in use, with an owner for each and the validation evidence for those that affect customers. (In this model, an incomplete answer leads to a finding and a pause on new medium- and high-risk launches; what a real supervisor does is for compliance and counsel to judge.)',
      options: [
        { id: 'answer', text: 'Send the inventory and validation evidence we have now', result: '', resultClean: 'The catalogue lists every model with its owner and validation; the answer goes in on time and closes the question.', resultFinding: 'The answer is incomplete: no full inventory, or no independent validation of high-risk models. A finding follows and new medium- and high-risk launches pause for two quarters.', effects: { regulator: 'answer' } },
        { id: 'delay', text: 'Ask for time, and build the catalogue properly first (₪400,000)', result: 'The catalogue is built in a rush and ready next quarter; launches pause for this quarter only.', effects: { regulator: 'delay', cost: 400000 } },
        { id: 'vendorList', text: 'Send the list of AI vendors and contracts from procurement', result: 'A vendor list is not a model inventory. A finding follows and launches pause for three quarters.', effects: { regulator: 'vendorList' } },
      ],
    },
    {
      id: 'keyPerson', q: 5, title: 'A key person leaves',
      text: 'The head of model validation resigns; two of her validators follow her to a fintech.',
      options: [
        { id: 'contractor', text: 'Bring in a validation contractor for six months (₪350,000)', result: 'The contractor covers half the gap.', effects: { keyPerson: 'contractor', cost: 350000 } },
        { id: 'second', text: 'Second two strong people from the units into validation', result: 'Review capacity holds, but unit builds pause for a quarter.', effects: { keyPerson: 'second' } },
        { id: 'accept', text: 'Accept the gap and recruit', result: 'Review slots drop until the new people arrive.', effects: { keyPerson: 'accept' } },
      ],
    },
    {
      id: 'budget', q: 6, title: 'A 15% budget cut',
      text: 'The CFO cuts the AI budget by 15% from next quarter and asks what you will cut. The bank-wide assistant rollout is the biggest single line on the list.',
      options: [
        { id: 'acrossBoard', text: 'Cut across the board: one review slot less, and pause the platform’s expansion for a quarter', result: 'Everything slows a little; nothing stops.', effects: { budgetCut: 0.15, slotsCut: 1, pausePlatform: 1 } },
        { id: 'cutSlots', text: 'Cut two review slots', result: 'The review queue slows.', effects: { budgetCut: 0.15, slotsCut: 2 } },
        { id: 'pausePlatform', text: 'Pause the platform for three quarters', result: 'Paved roads close until it restarts; low-risk work goes back to the queue.', effects: { budgetCut: 0.15, pausePlatform: 3 } },
        { id: 'cutAssistant', text: 'Cut the bank-wide assistant rollout', result: 'The assistant is cancelled. Nobody checked what depended on it.', effects: { budgetCut: 0.15, killTheme: 'assistant' } },
      ],
    },
    {
      id: 'drift', q: 8, title: 'A model drifts',
      text: 'Since rates moved, SME Banking’s credit pre-approval model approves noticeably more marginal applicants.',
      resultNotLive: 'The pre-approval model never reached production, so nothing drifted; the question goes back to the queue with it.',
      options: [
        { id: 'retrain', text: 'Retrain it and validate it independently before it continues (₪250,000)', result: 'Retrained, revalidated, back in service with monitoring.', effects: { drift: 'retrain', cost: 250000 } },
        { id: 'retire', text: 'Retire it and go back to manual pre-approval', result: 'Retired; SME pre-approval is manual again.', effects: { drift: 'retire' } },
        { id: 'keep', text: 'Keep it running and watch the numbers', result: 'It was validated independently and its monitoring holds; it keeps running.', resultBad: 'Nobody validated it independently; marginal approvals turn into losses and a risk incident.', effects: { drift: 'keep' } },
      ],
    },
    {
      id: 'wave', q: 10, title: 'AI arrives in a vendor release',
      text: 'A vendor release switches on generative features in the CRM and the HR system: six “AI pilots” nobody asked for, already in staff hands.',
      wave: [
        { unit: 'retail', t: 'crm-email', name: 'CRM email drafting', r: 'low' },
        { unit: 'sme', t: 'crm-summary', name: 'CRM account summaries', r: 'low' },
        { unit: 'corporate', t: 'crm-insights', name: 'CRM deal insights', r: 'med' },
        { unit: 'contact', t: 'crm-replies', name: 'CRM reply suggestions', r: 'med' },
        { unit: 'hr', t: 'hr-reviews', name: 'Performance review drafting', r: 'high' },
        { unit: 'hr', t: 'hr-jobads', name: 'Job ad drafting', r: 'low' },
      ],
      options: [
        { id: 'route', text: 'Treat them as new models: catalogue, then the normal route by risk', result: 'All six enter the normal route.', effects: { wave: 'route' } },
        { id: 'ignore', text: 'They came with the vendor, so they are the vendor’s problem', result: 'All six stay on, unreviewed.', effects: { wave: 'ignore' } },
        { id: 'switchOff', text: 'Switch them all off', result: 'Switched off. Staff who liked them look for other tools.', effects: { appetite: 0.1 } },
      ],
    },
  ],
  startConfig: { archetype: 'central', rights: 'central', slots: 3, mrm: 'full', roads: { platform: false, templates: false, catalogue: false } },
  federatedConfig: { archetype: 'federated', rights: 'unit', slots: 0, mrm: 'light', roads: { platform: false, templates: false, catalogue: false } },
  naiveAnswers: { shadow: 'leave', duplicates: 'both', regulator: 'answer', keyPerson: 'accept', budget: 'cutAssistant', drift: 'keep', wave: 'ignore' },
  expert: {
    config: { archetype: 'hub', rights: 'tiered', slots: 3, mrm: 'tiered', roads: { platform: true, templates: true, catalogue: true } },
    answers: { shadow: 'adopt', duplicates: 'merge', regulator: 'answer', keyPerson: 'contractor', budget: 'acrossBoard', drift: 'retrain', wave: 'route' },
    why: 'Hub-and-spoke from the first quarter: the hub funds the platform, the templates with the evaluation kit and the catalogue, and validates high-risk models; units build and decide low- and medium-risk go-lives on the paved road. Shadow builds are brought in, duplicates merged, the cut spread so the assistant (which two later initiatives depend on) survives.',
  },
  hubSpoke: HUB_SPOKE,
  verdict: { incidentSlack: 1, maxShadow: 2 },
  notes: [
    'Crescent Bank, its units and pilots are fictional. 4,000 staff, 14 units and 40 pilots are from the engagement plan; the pilots’ names, risk tiers and which ones are weak (10 of 40) are assumptions.',
    'Money (₪ a quarter unless stated): budget ₪11M a year; a review slot ₪150,000; the central team ₪1.2M (central CoE), ₪0.8M (hub), ₪0.3M (federated); platform ₪2.4M over two quarters then ₪300,000; templates ₪200,000 then ₪40,000; catalogue ₪150,000 then ₪25,000; each pilot in production ₪20,000 on the platform or ₪45,000 off it; a reorganisation ₪300,000.',
    'Build: 3 quarters in a maturity-1 unit, 2 in maturity 2–3, 2 for the central team (which works on 8 pilots at a time); the platform saves a quarter for low- and medium-risk pilots.',
    'Review effort in slots: full validation 2 per model; by tier 0.5 (low), 1 (medium), 2 (high); light 0.5. Templates make each slot go 1.5 times as far. Weak pilots are stopped by any review except the light one, and by a unit’s own test when the evaluation kit exists.',
    'Shadow builds: each quarter a unit has any pilot waiting two quarters or more (for review or for the central builders), it adds 0.35 × its appetite (0–1) towards a tool built outside the process; each whole one goes live unreviewed.',
    'Incidents per pilot in production per quarter: 1% (low), 3% (medium), 6% (high); ×3 if weak; ×2 for shadow tools; ×0.5 on the platform; ×0.3 after full validation, ×0.45 after a standard one, ×0.6 with hub standards or the paved road, ×0.7 after a light check. Expected incidents add up; each whole one is an incident.',
    'The supervisor’s reaction is this model’s, not a statement of what a real supervisor would do.',
  ],
  lessonPoint:
    'Centralise the constants and delegate the variables: the hub owns the platform, the standards and evaluation kit, the catalogue and high-risk validation; units own discovery, building, adoption and low-risk go-lives on the paved road. A central queue for everything does not make AI safe, it makes it slow and pushes it into the shadows; no centre at all makes it fast, duplicated and risky.',
};

// ---------- generic ----------

const generic = {
  label: 'Generic — an insurer with 12 units and 24 pilots',
  brief:
    'A 1,500-person insurer has 12 business units and 24 AI pilots, none in production. Design how pilots reach production over three ' +
    'years: the model, the decision rights, central review slots, validation depth and paved roads. Play twelve quarters, answer the ' +
    'events and adjust as you go.',
  startYear: 2027,
  quarters: 12,
  units: [
    { id: 'motor', name: 'Motor claims', maturity: 2, appetite: 0.6, pilots: [pil('claim-summary', 'Claim summaries', 'med'), pil('damage-photos', 'Damage photo triage', 'high', { weak: true })] },
    { id: 'home', name: 'Home claims', maturity: 1, appetite: 0.4, pilots: [pil('claim-summary', 'Claim summaries', 'med'), pil('home-faq', 'Adjuster FAQ', 'low')] },
    { id: 'health', name: 'Health', maturity: 2, appetite: 0.3, pilots: [pil('pre-auth', 'Pre-authorisation checks', 'high'), pil('member-letters', 'Member letters', 'low', { weak: true })] },
    { id: 'life', name: 'Life & savings', maturity: 1, appetite: 0.2, pilots: [pil('advice-notes', 'Advice note drafts', 'high', { weak: true }), pil('policy-search', 'Policy search', 'low')] },
    { id: 'underwriting', name: 'Underwriting', maturity: 3, appetite: 0.5, pilots: [pil('risk-score', 'Commercial risk scoring', 'high'), pil('submission-extract', 'Submission extraction', 'med')] },
    { id: 'fraud', name: 'Fraud', maturity: 3, appetite: 0.3, pilots: [pil('fraud-flags', 'Fraud flags', 'high'), pil('network-graph', 'Network analysis', 'med')] },
    { id: 'service', name: 'Customer service', maturity: 2, appetite: 0.8, pilots: [pil('call-summary', 'Call summaries', 'med'), pil('assistant', 'Company-wide assistant', 'low')] },
    { id: 'digital', name: 'Digital', maturity: 3, appetite: 0.9, pilots: [pil('chatbot', 'Quote chatbot', 'med', { weak: true }), pil('call-summary', 'Call summaries', 'med')] },
    { id: 'distribution', name: 'Agents & brokers', maturity: 1, appetite: 0.5, pilots: [pil('broker-faq', 'Broker FAQ', 'low', { dependsOn: 'assistant' }), pil('lead-score', 'Lead scoring', 'med')] },
    { id: 'finance', name: 'Finance', maturity: 2, appetite: 0.2, pilots: [pil('reserving-notes', 'Reserving commentary', 'med'), pil('invoice', 'Invoice matching', 'low')] },
    { id: 'hr', name: 'HR', maturity: 1, appetite: 0.4, pilots: [pil('cv', 'CV screening', 'high', { weak: true }), pil('hr-faq', 'HR policy FAQ', 'low')] },
    { id: 'legal', name: 'Legal & compliance', maturity: 2, appetite: 0.2, pilots: [pil('contract-review', 'Contract clause review', 'med'), pil('complaints-log', 'Complaint classification', 'low')] },
  ],
  arrivals: [{ q: 4, unit: 'motor', t: 'repair-quotes', name: 'Repair quote checks', r: 'med' }],
  money: {
    budgetPerYear: 6000000,
    slotCost: 120000,
    coe: { central: 800000, federated: 200000, hub: 500000 },
    roads: {
      platform: { build: 1600000, run: 200000, lead: 2 },
      templates: { build: 150000, run: 30000, lead: 1 },
      catalogue: { build: 100000, run: 20000, lead: 1 },
    },
    runOnPlatform: 15000,
    runOffPlatform: 35000,
    reorg: 200000,
  },
  build: { byMaturity: { 1: 3, 2: 2, 3: 2 }, central: 2, centralCapacity: 5, platformSaves: 1 },
  review: { templatesFactor: 1.5 },
  shadow: { waitQuarters: 2, rate: 0.35 },
  risk: crescent.risk,
  regulator: crescent.regulator,
  keyPerson: crescent.keyPerson,
  driftTheme: 'risk-score',
  events: [
    {
      id: 'duplicates', q: 2, title: 'Two claim-summary builds',
      text: 'Motor and Home claims are both building claim summaries, on different tools.',
      options: [
        { id: 'merge', text: 'Merge into one build owned by Motor', result: 'One build serves both.', effects: { merge: 'claim-summary' } },
        { id: 'both', text: 'Let both continue', result: 'Two builds continue.', effects: {} },
      ],
    },
    {
      id: 'regulator', q: 4, title: 'The regulator asks',
      text: 'The regulator asks for an inventory of models in use and validation evidence for those affecting customers. (In this model, an incomplete answer means a pause on new medium- and high-risk launches.)',
      options: [
        { id: 'answer', text: 'Send what we have', result: '', resultClean: 'The catalogue answers it.', resultFinding: 'Incomplete: launches of medium- and high-risk models pause for two quarters.', effects: { regulator: 'answer' } },
        { id: 'delay', text: 'Ask for time and build the catalogue (₪300,000)', result: 'Catalogue ready next quarter; a one-quarter pause.', effects: { regulator: 'delay', cost: 300000 } },
      ],
    },
    {
      id: 'budget', q: 6, title: 'A 15% budget cut',
      text: 'Finance cuts the AI budget by 15%. The company-wide assistant is the biggest line.',
      options: [
        { id: 'acrossBoard', text: 'Cut across the board', result: 'Everything slows a little.', effects: { budgetCut: 0.15, slotsCut: 1, pausePlatform: 1 } },
        { id: 'cutAssistant', text: 'Cut the company-wide assistant', result: 'Cancelled. Nobody checked what depended on it.', effects: { budgetCut: 0.15, killTheme: 'assistant' } },
      ],
    },
    {
      id: 'drift', q: 8, title: 'A scoring model drifts',
      text: 'The commercial risk-scoring model is pricing a growing segment too low.',
      resultNotLive: 'The model never reached production, so nothing drifted.',
      options: [
        { id: 'retrain', text: 'Retrain and validate independently (₪200,000)', result: 'Back in service, validated.', effects: { drift: 'retrain', cost: 200000 } },
        { id: 'keep', text: 'Keep it running and watch', result: 'Validated and monitored, it holds.', resultBad: 'Unvalidated, it misprices a book of business: a risk incident.', effects: { drift: 'keep' } },
      ],
    },
  ],
  startConfig: { archetype: 'central', rights: 'central', slots: 2, mrm: 'full', roads: { platform: false, templates: false, catalogue: false } },
  federatedConfig: { archetype: 'federated', rights: 'unit', slots: 0, mrm: 'light', roads: { platform: false, templates: false, catalogue: false } },
  naiveAnswers: { duplicates: 'both', regulator: 'answer', budget: 'cutAssistant', drift: 'keep' },
  expert: {
    config: { archetype: 'hub', rights: 'tiered', slots: 2, mrm: 'tiered', roads: { platform: true, templates: true, catalogue: true } },
    answers: { duplicates: 'merge', regulator: 'answer', budget: 'acrossBoard', drift: 'retrain' },
    why: 'Hub-and-spoke with the platform, templates and catalogue funded from the start; high-risk models validated centrally, everything else decided in the units on the paved road.',
  },
  hubSpoke: HUB_SPOKE,
  verdict: { incidentSlack: 1, maxShadow: 2 },
  notes: ['Every number in this generic preset is an assumption chosen to make the trade-offs visible; the rates and multipliers are the same as Crescent’s.'],
  lessonPoint: crescent.lessonPoint,
};

export const PRESETS = { crescent, generic };
