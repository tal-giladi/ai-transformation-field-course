// Presets for pilot-economics. To add one, copy an entry, give it a new key and change the numbers.
// Token prices and the exchange rate are examples: tell learners to put in today's numbers.

export const DEFAULT_PRESET = 'harbor';

export const PRESETS = {
  harbor: {
    label: 'Harbor & Pine — support email triage and draft replies',
    item: 'email',
    items: 'emails',
    brief:
      'You are Head of AI and Operations Improvement at Harbor & Pine, a 120-person furniture importer. ' +
      'The pilot from module 5 sorts incoming support emails (damage claims, assembly questions, returns, ' +
      'B2B quotes) and drafts a reply in Hebrew, Arabic, Russian or English; an agent reads every draft ' +
      'and sends it. WISMO ("where is my order?") emails are out of scope: the delivery-date fix handles them. ' +
      'The 14-person support team costs about ₪3.4M a year and runs at about 92% utilisation in peak season. ' +
      'Ronit, the CFO, wants one number she can check: what the pilot is worth per month after the human ' +
      'check, and when it pays back. Find where the human review eats the saving before she does.',
    params: {
      volume: 3200,
      automationRate: 0.6,
      accuracy: 0.8,
      minutesSaved: 8,
      reviewMinutes: 2,
      reworkMinutes: 5,
      hourlyCost: 130,
      tokensIn: 2500,
      tokensOut: 400,
      priceIn: 3,
      priceOut: 15,
      fx: 3.6,
      fixedMonthly: 4000,
      buildCost: 120000,
    },
    notes: [
      'Volume: about 3,200 non-WISMO support emails a month (assumption for the exercise; measure it from the helpdesk export in 02.4).',
      'Hourly cost: ₪3.4M a year for 14 people, about 1,870 paid hours each, is about ₪130 an hour fully loaded.',
      'Build cost ₪120,000 stays under the ₪150,000 line above which the board must approve.',
      'Review minutes: 2 minutes per draft is what the team guessed. The oversight-under-load simulation shows what a real check takes.',
    ],
  },
  generic: {
    label: 'Generic — supplier invoice extraction',
    item: 'invoice',
    items: 'invoices',
    brief:
      'A 300-person distributor wants AI to read supplier invoices and fill the accounting entry; a clerk ' +
      'checks each entry before it is posted. The vendor quotes 92% field-level accuracy from its own test set. ' +
      'Finance asks whether the pilot pays back within a year and how much clerk time it really frees. ' +
      'Move the accuracy and review sliders until you can say where the value comes from and where it disappears.',
    params: {
      volume: 10000,
      automationRate: 0.85,
      accuracy: 0.92,
      minutesSaved: 4,
      reviewMinutes: 1,
      reworkMinutes: 6,
      hourlyCost: 110,
      tokensIn: 3000,
      tokensOut: 300,
      priceIn: 1,
      priceOut: 4,
      fx: 3.6,
      fixedMonthly: 8000,
      buildCost: 250000,
    },
    notes: [
      'The 92% was measured by the vendor on its own invoices, not yours: test it on your own sample before you use it.',
    ],
  },
};
