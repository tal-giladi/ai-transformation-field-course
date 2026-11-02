// Presets for oversight-under-load. To add one, copy an entry, give it a new key, change the numbers
// and the target (the design goal the learner must meet).

export const DEFAULT_PRESET = 'harbor';

export const PRESETS = {
  harbor: {
    label: 'Harbor & Pine — agents checking AI-drafted replies',
    item: 'draft',
    items: 'drafts',
    brief:
      'The support-email pilot is live in shadow mode at Harbor & Pine. About 90 AI-drafted replies a day ' +
      '(more on Sunday, after the weekend) wait for one of three agents, who each set aside 1.5 hours a day to ' +
      'check drafts between phone calls. About one draft in five is wrong: a wrong refund rule, a promised date ' +
      'that does not exist, a Russian reply in the wrong register. A careful check takes about 3 minutes. ' +
      'It is November: peak season, the team is at about 92% utilisation. Samir, the support manager, can give ' +
      'at most 6 agent-hours a day to checking. Design the check so that no more than 10 wrong replies reach ' +
      'customers in two working weeks.',
    params: {
      itemsPerDay: 90,
      reviewers: 3,
      hoursPerReviewer: 1.5,
      errorRate: 0.2,
      checkMinutes: 3,
      sourceShown: false,
      flagFeedback: false,
      days: 10,
    },
    target: { maxEscaped: 10, maxReviewerHoursPerDay: 6 },
    notes: [
      '90 drafts a day is roughly the pilot-economics preset: 3,200 written contacts a month × 60% handled ÷ 22 working days.',
      'The pilot-economics preset assumes 2 review minutes per draft. Here a real check takes 3, or about 2 with the source beside the draft.',
    ],
  },
  generic: {
    label: 'Generic — adjusters checking AI claim summaries',
    item: 'summary',
    items: 'summaries',
    brief:
      'An insurer’s AI writes a one-page summary of each new claim file; an adjuster checks it before it ' +
      'goes into the decision. About 400 summaries a day, 8 adjusters with 3 hours a day each for checking, ' +
      'and the model is usually right: about 8% of summaries miss or misstate something that matters. ' +
      'A real check against the file takes 5 minutes. The claims director can fund at most 30 adjuster-hours ' +
      'a day. Keep the misstated summaries that slip through to 20 or fewer in two weeks.',
    params: {
      itemsPerDay: 400,
      reviewers: 8,
      hoursPerReviewer: 3,
      errorRate: 0.08,
      checkMinutes: 5,
      sourceShown: false,
      flagFeedback: false,
      days: 10,
    },
    target: { maxEscaped: 20, maxReviewerHoursPerDay: 30 },
    notes: [
      'A tool that is usually right is the hardest one to keep checking: vigilance falls faster when errors are rare.',
    ],
  },
};
