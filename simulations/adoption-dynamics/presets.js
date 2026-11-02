// Presets for adoption-dynamics. To add one, copy an entry, give it a new key, and change the team,
// the names (fictional), the old ways of working people return to, and the value of one qualified use.

export const DEFAULT_PRESET = 'harbor';

export const PRESETS = {
  harbor: {
    label: 'Harbor & Pine — support team, AI reply drafts',
    team: 'support agents',
    task: 'answering damage, assembly, return and B2B messages with the AI draft',
    brief:
      'The reply-drafts pilot for written contact passed its go/no-go and starts on 1 February 2027. All 14 people in support get a licence; ' +
      '12 of them answer written contact (the manager and the claims coordinator do other work). The vendor’s admin dashboard will show licences and weekly ' +
      'active users. Michal, the COO, wants to know in August whether the tool is used on the work that matters. ' +
      'Plan the first 26 weeks: which levers, from which week. Then read the dashboard honestly: who uses it on real ' +
      'emails, and who quietly went back to the old way.',
    teamSize: 14,
    opportunityShare: 12 / 14,
    usesPerWeek: 25,
    minutesPerUse: 5,
    seed: 20270201,
    names: ['Olga', 'Lior', 'Hila', 'Yusuf', 'Marina', 'Avital', 'Kobi', 'Rana', 'Dima', 'Shira', 'Natan', 'Inbal', 'Sergei', 'Maya'],
    oldWays: ['the old reply templates', 'typing replies from scratch', 'free ChatGPT on a personal phone', 'copying an old ticket’s reply'],
  },
  generic: {
    label: 'Generic — 40-person sales operations team, AI quote assistant',
    team: 'sales operations staff',
    task: 'preparing customer quotes and order confirmations with the assistant',
    brief:
      'A distributor rolls out an AI quote assistant to a 40-person sales operations team; about 30 of them prepare ' +
      'quotes, the rest handle logistics paperwork. Licences are bought for everyone on day one. The sales director ' +
      'wants a dashboard for the quarterly review. Plan 26 weeks of rollout and see what the dashboard can and cannot tell you.',
    teamSize: 40,
    opportunityShare: 0.75,
    usesPerWeek: 15,
    minutesPerUse: 8,
    seed: 4040,
    names: ['Adi', 'Boaz', 'Carmel', 'Dalia', 'Eli', 'Fadi', 'Gal', 'Hadas', 'Ido', 'Jamal', 'Keren', 'Lena', 'Moti', 'Nili',
      'Omer', 'Pnina', 'Ran', 'Sigal', 'Tal', 'Uri', 'Vered', 'Wasim', 'Yael', 'Ziv', 'Amir', 'Bat-El', 'Chen', 'Dor',
      'Efrat', 'Galit', 'Hagai', 'Irit', 'Yonatan', 'Karin', 'Liat', 'Meir', 'Noam', 'Orly', 'Rami', 'Smadar'],
    oldWays: ['the old Excel quote sheet', 'copying last month’s quote', 'asking a colleague to do it', 'a free AI tool on a personal account'],
  },
};
