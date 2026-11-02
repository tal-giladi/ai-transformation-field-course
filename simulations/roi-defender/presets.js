// Scenarios for roi-defender. A scenario is the sponsor's list of claims for one case, the candidate
// adjustments to each claim on the four ledgers (some real, some not), the truth, the case's costs and
// the finance rules. To add one, copy `harbor` and keep the same fields; `validateScenario` in
// model.js checks the data. Money is ₪ a year unless a field says otherwise.
//
// Claim fields: id, title, claimed, basis, deckLabel / deckClass (what the sponsor's deck says),
//   adjustments [{ id, ledger (sponsor | receiving | control | customer), text, amount (negative
//   reduces), target? (another claim id the amount applies to), real (true if it belongs in the
//   netting), why }], truth { label: measured | directional | assumed, cls: cash | capacity, note }.

export const DEFAULT_PRESET = 'harbor';

const harbor = {
  label: 'Harbor & Pine — the draft pilot’s ROI under finance review',
  brief:
    'January 2027. Michal’s deck for the support-email draft pilot says it is worth ₪1.36 million a year: the 40% the board was promised. ' +
    'Before it goes to the steering group, Ronit (CFO) puts every claim through her review. For each of the seven claims, net it across the ' +
    'four ledgers (the sponsor’s team, the team that receives new work, the review labour that keeps it safe, and the customer’s share of the ' +
    'gain), label it measured, directional or assumed, and say whether it is cash or capacity. Ronit counts measured and directional cash in ' +
    'her expected case, discounts at her 12% hurdle rate over three years, and sends anything above ₪150,000 over three years to the board. ' +
    'Find the number that survives her, and say who must approve it.',
  hourlyCost: 130,
  hurdleRate: 0.12,
  costs: { build: 120000, runningPerYear: 49000, years: 3 },
  approval: [
    { id: 'dept', who: 'The department head and the CFO', max: 50000 },
    { id: 'ceo', who: 'The CEO', max: 150000 },
    { id: 'board', who: 'The board', max: Infinity },
  ],
  claims: [
    {
      id: 'drafts', title: 'Agents save 8 minutes on every AI-drafted reply', claimed: 319500, deckLabel: 'measured', deckClass: 'cash',
      basis: 'Timed on a test set of 400 real emails: 8 minutes saved per accepted draft, 80% accepted. 3,200 written contacts a month (email, web form and WhatsApp routed into the helpdesk), 60% drafted: about 2,460 hours a year at ₪130.',
      adjustments: [
        { id: 'rework', ledger: 'sponsor', amount: -49920, real: true, text: 'The 20% of drafts that are wrong take 5 extra minutes to fix: 384 hours a year.', why: 'Rework is a cost inside the sponsor’s own team; the deck counted only the right drafts’ saving and forgot the wrong ones’ cost.' },
        { id: 'review', ledger: 'control', amount: -99840, real: true, text: 'Every draft is read before it is sent: 2 minutes × 23,040 drafts = 768 hours a year.', why: 'The human check is what makes the pilot safe; it is paid for in the same hours the claim counts.' },
        { id: 'custShare', ledger: 'customer', amount: -63900, real: false, text: 'Customers get faster replies, so take 20% off as their share.', why: 'A faster reply is good for the customer but does not reduce the hours your agents save. The customer’s share matters when the claim counts money the customer keeps or no longer gets.' },
      ],
      truth: { label: 'measured', cls: 'capacity', note: 'Measured on real emails, so it is measured, but it is hours, not cash: nobody has a named plan for them except the temps (claim 7).' },
    },
    {
      id: 'heads', title: 'Two fewer agents from April 2027', claimed: 431400, deckLabel: 'measured', deckClass: 'cash',
      basis: 'Claim 1 frees about two people’s time; attrition will take care of it. 2 × ₪215,700 fully loaded.',
      adjustments: [
        { id: 'once', ledger: 'sponsor', amount: -431400, real: true, text: 'Count the freed hours once: they are claim 1’s hours, and claim 1 nets to well under one person.', why: 'The same hours counted as time saved and again as salaries saved. Count them once, and only after netting.' },
        { id: 'recruit', ledger: 'receiving', amount: 12000, real: false, text: 'Add HR’s saved recruitment fees for the two roles not replaced.', why: 'Nobody is leaving and there is no named plan, so there are no fees to save.' },
      ],
      truth: { label: 'assumed', cls: 'capacity', note: 'No named plan, no date, no owner: Ronit’s rule says freed capacity is not cash until there is one.' },
    },
    {
      id: 'wismo', title: 'Fewer “where is my order?” contacts', claimed: 300000, deckLabel: 'measured', deckClass: 'cash',
      basis: 'WISMO was 38% of contacts and the date fix (live 14 January) is expected to halve it: about 2,300 agent-hours a year.',
      adjustments: [
        { id: 'attrib', ledger: 'sponsor', amount: -300000, real: true, text: 'This drop comes from the delay-email job (no AI), live since 14 January and funded on its own. Without the pilot the drop is the same.', why: 'A real benefit, wrong project. The credible counterfactual (no pilot) has the same drop, so it belongs in the date-fix case.' },
        { id: 'eta', ledger: 'receiving', amount: -27000, real: false, text: 'Logistics updates the ETA sheet daily: 4 hours a week.', why: 'A real cost of the date-fix job. Once the claim moves to that case, net it there; here the claim is already gone.' },
      ],
      truth: { label: 'directional', cls: 'capacity', note: 'The drop is measured, its size a year from now is an estimate, and it is hours, not cash. Either way it is not this pilot’s.' },
    },
    {
      id: 'translate', title: 'The translation service is no longer needed', claimed: 42000, deckLabel: 'measured', deckClass: 'cash',
      basis: 'LinguaFlow invoices for 2025: ₪42,000. Drafts in Russian and Arabic replace it.',
      adjustments: [
        { id: 'mkt', ledger: 'receiving', amount: -12000, real: true, text: 'Marketing still needs LinguaFlow for catalogue copy: keep a small plan at ₪12,000 a year.', why: 'The receiving team: marketing loses a service it relies on unless a smaller plan stays.' },
        { id: 'spot', ledger: 'control', amount: -13000, real: true, text: 'A native speaker spot-checks 1 in 10 Arabic and Russian drafts: about 100 hours a year.', why: 'The control that replaces the professional translator costs time.' },
        { id: 'lang', ledger: 'customer', amount: -10000, real: false, text: 'Customers who write in Russian or Arabic lose a human translator: take ₪10,000 off for their share.', why: 'No money moves to or from the customer here; quality is covered by the spot-check.' },
      ],
      truth: { label: 'measured', cls: 'cash', note: 'Invoices are measured cash, and the contract can be cut on a date.' },
    },
    {
      id: 'credits', title: 'Fewer goodwill credits beyond policy', claimed: 103500, deckLabel: 'measured', deckClass: 'cash',
      basis: 'Damage and returns write-offs were ₪690,000 in 2025; drafts that quote the policy will cut them by 15%.',
      adjustments: [
        { id: 'outcomes', ledger: 'control', amount: -13000, real: true, text: 'Rina must record every claim outcome (missing for 35% today), or nobody can measure this: about 100 hours a year.', why: 'Without recorded outcomes the claim cannot be measured at all; the recording is review labour.' },
        { id: 'custSide', ledger: 'customer', amount: -51750, real: true, text: 'Half of this “saving” is money customers no longer get; some escalate, post a review or stop buying. Count half until it is measured.', why: 'The gain comes out of the customer’s pocket; part of it comes back as complaints and lost sales.' },
        { id: 'rebook', ledger: 'receiving', amount: -5000, real: false, text: 'Finance must re-book the write-offs: ₪5,000.', why: 'No re-booking is needed; this cost does not exist.' },
      ],
      truth: { label: 'assumed', cls: 'cash', note: 'Nobody recorded which credits were outside policy, so the 15% is a guess. Cash if it happens; upside, not the case.' },
    },
    {
      id: 'repeat', title: 'Repeat purchases from faster replies', claimed: 67600, deckLabel: 'measured', deckClass: 'cash',
      basis: 'Replies within an hour lift satisfaction from 63% to 80%; the vendor says that adds 0.1% to B2C revenue (₪67.2 million).',
      adjustments: [
        { id: 'margin', ledger: 'customer', amount: -39200, real: true, text: 'The faster answer is the customer’s gain. What reaches Harbor & Pine is repeat purchases, counted as gross margin (42%), not revenue.', why: 'Revenue is not profit, and most of the gain stays with the customer as a better experience.' },
        { id: 'dup', ledger: 'sponsor', amount: -67600, real: false, text: 'The agents’ time is already in claim 1: remove this claim.', why: 'This claim is about sales, not agent time, so it is not double-counted. It fails for another reason: the uplift is the vendor’s figure.' },
      ],
      truth: { label: 'assumed', cls: 'cash', note: 'A vendor ratio applied to a satisfaction survey that is sent when a reply goes out. Upside at best.' },
    },
    {
      id: 'temps', title: 'No seasonal temps next peak', claimed: 96000, deckLabel: 'measured', deckClass: 'cash',
      basis: 'Samir hired two temps for November–January (₪16,000 a month each). Samir and Michal have signed that the next peak runs without them if the pilot holds its numbers until September.',
      adjustments: [
        { id: 'convert', ledger: 'sponsor', target: 'drafts', amount: -96000, real: true, text: 'Count it once: the temps’ ₪96,000 comes out of the capacity claim 1 frees. Move them from capacity to cash; do not add them.', why: 'This is how capacity becomes cash: a named plan, an owner, a date. The hours leave claim 1 when they become money here.' },
        { id: 'peakReview', ledger: 'control', amount: -49920, real: false, text: 'At peak the drafts still need reading: take off another 384 hours of review.', why: 'Review is already netted in claim 1 for every draft in the year.' },
      ],
      truth: { label: 'directional', cls: 'cash', note: 'A signed decision with a date makes it cash; it depends on the pilot holding up, so it is directional, not measured.' },
    },
  ],
  lessonPoint:
    'Net every claim across all four ledgers before you defend it: the sponsor’s team, the team that receives the work, the review labour that keeps it safe, ' +
    'and the customer’s share. Label each one measured, directional or assumed, count freed hours as capacity until someone owns turning them into money, ' +
    'and ask what happens without the project. The smaller number that survives finance is worth more than the big one that does not.',
  notes: [
    'Hours and minutes follow the pilot-economics harbor preset (3,200 written contacts a month (email, web form and WhatsApp routed into the helpdesk), 60% drafted, 80% right, 8 minutes saved, 2 minutes review, 5 minutes rework, ₪130 an hour).',
    'Build ₪120,000 and about ₪49,000 a year to run (₪4,000 a month fixed plus tokens) also follow pilot-economics.',
    'Hurdle rate 12%, payback preferred within 24 months, approval above ₪150,000 over three years by the board, “freed capacity is not cash”, write-offs ₪690,000 and support salaries ₪3.02 million for 14 people: the CFO’s finance summary in the data room.',
    'The translation contract (₪42,000), the temps (two for three months at ₪16,000 a month), the 15% credit cut and the vendor’s satisfaction-to-revenue ratio are assumptions for the exercise.',
  ],
};

export const PRESETS = { harbor };
