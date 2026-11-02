import { h, replace, focusEl } from '../common/dom.js';
import { mountShell, panel } from '../common/shell.js';
import { selectField, button, stat } from '../common/controls.js';
import { lineChart } from '../common/chart.js';
import { pct, num, hours, plural } from '../common/format.js';
import { simulate, whoStopped, EMPTY_PLAN, WEEKS, K } from './model.js';
import { PRESETS, DEFAULT_PRESET } from './presets.js';

const WEEK_OPTIONS = [0, 1, 2, 3, 4, 6, 8, 10, 12, 16, 20];
const weekOptions = WEEK_OPTIONS.map((w) => ({ value: String(w), label: w === 0 ? 'Off' : `From week ${w}` }));

const LEVERS = [
  { key: 'champions', label: 'Champions', help: 'One respected person in the team, given time to help others on real work.' },
  { key: 'officeHours', label: 'Office hours', help: 'A weekly slot to bring a stuck case. Help grows over the first weeks.' },
  { key: 'redesign', label: 'Workflow redesign', help: 'The tool is built into the step where the work happens (the draft opens beside the email), not a separate window.' },
  { key: 'mandate', label: 'Manager mandate', help: '“Everyone uses the tool every week; we will check the dashboard.”' },
  { key: 'removeOldPath', label: 'Remove the old path', help: 'The old templates and the side route are switched off. Nothing to go back to.' },
];

const TRAINING = [
  { value: 'none', label: 'No training' },
  { value: 'generic', label: 'Generic (vendor webinar, features tour)' },
  { value: 'role', label: 'Role-based, on the team’s real work' },
];

const ABOUT = {
  intro: 'Each team member is simulated week by week for 26 weeks. Seeded randomness: the same plan and seed always give the same run.',
  equations: [
    'Every person gets a licence in week 1. Licences active = team size, every week.',
    `First try: each week a person who has not tried has a chance of 5–30% (their own curiosity), plus ${pct(K.tryChampions)} while champions run, plus a one-off ${pct(K.tryTraining.generic)} (generic) or ${pct(K.tryTraining.role)} (role-based) in the training week, plus ${pct(K.tryForced)} while a mandate runs or the old path is gone.`,
    `Skill = own starting skill (15–50%) + training (generic +${pct(K.skillTraining.generic)}, role-based +${pct(K.skillTraining.role)}) + champions +${pct(K.skillChampions)} + office hours (+${pct(K.skillOfficeHoursPerWeek)} a week, up to +${pct(K.skillOfficeHoursMax)}) + workflow redesign +${pct(K.skillRedesign)}; at most ${pct(K.skillMax)}.`,
    `Active this week: with probability = habit (starts at ${pct(K.habitStart)}). Under a mandate, or with the old path gone, an inactive person logs some use anyway with probability ${pct(K.forcedActivity)}.`,
    `Qualified use this week (only people whose work includes the target tasks): probability = skill; × ${K.mandateQualityFactor} for use forced by a mandate; × ${K.noOldPathQualityFactor} for use forced by a removed old path.`,
    `Habit: +${pct(K.habitUp)} after a week with qualified use; −${pct(K.habitDown)} after active use without it; −${pct(K.habitIdle)} after an inactive week.`,
    `Quiet stop: after ${K.stopAfterWeeksWithoutValue} weeks in a row without qualified use (from week 3), a person goes back to their old way. Not possible once the old path is gone.`,
    `Coming back: ${pct(K.returnAlone)} a week alone, +${pct(K.returnWithSupport)} while champions or office hours run, +${pct(K.returnOnRedesign)} in the week of the workflow redesign; everyone, once the old path is gone.`,
    'Weekly active users = people with any use that week. Qualified-use rate = people with qualified use ÷ people whose work includes the target tasks.',
    'The numbers on the tiles are averages of weeks 23–26.',
  ],
  assumptions: [
    'A qualified event is use on the tasks that matter, done properly (here: a reply drafted with the tool and sent after a real check).',
    'Generic training raises curiosity more than skill; role-based training on real work raises skill.',
    'A mandate measured on the activity dashboard produces activity (Goodhart’s law).',
  ],
  leftOut: [
    'Team politics, turnover, a manager who models the behaviour (or not), and the quality of the tool itself.',
    'The privacy rules for monitoring individual usage: in a real team you report teams, not named people, unless policy and law allow it (lesson 06.4).',
  ],
};

let shell;
let plan;
let seed;
let runs = [];
let last = null;
let stoppedOpened = false;
let debriefShown = false;
let view = {};

const preset = () => PRESETS[shell.presetKey];

function start(key) {
  plan = { ...EMPTY_PLAN };
  seed = PRESETS[key].seed;
  runs = [];
  last = null;
  stoppedOpened = false;
  debriefShown = false;
  build();
}

function planText(p) {
  const parts = [];
  if (p.training !== 'none' && p.trainingWeek > 0) parts.push(`${p.training === 'role' ? 'role-based' : 'generic'} training wk ${p.trainingWeek}`);
  for (const l of LEVERS) if (p[l.key] > 0) parts.push(`${l.label.toLowerCase()} wk ${p[l.key]}`);
  return parts.length ? parts.join(' · ') : 'licences only';
}

function build() {
  const p = preset();
  const planPanel = panel('Your 26-week plan', { id: 'plan' });
  const trainingWeek = selectField({
    label: 'Training week', options: weekOptions.filter((o) => o.value !== '0'), value: '1',
    onChange: (v) => { plan.trainingWeek = plan.training === 'none' ? 0 : Number(v); },
  });
  const training = selectField({
    label: 'Training', options: TRAINING, value: plan.training,
    help: 'Once, in the week you choose below.',
    onChange: (v) => { plan.training = v; plan.trainingWeek = v === 'none' ? 0 : Number(trainingWeek.value); },
  });
  const group1 = h('fieldset', { class: 'group' }, h('legend', {}, 'Training'), training.el, trainingWeek.el);
  const group2 = h('fieldset', { class: 'group' }, h('legend', {}, 'Other levers'),
    LEVERS.map((l) => selectField({
      label: l.label, options: weekOptions, value: String(plan[l.key]), help: l.help,
      onChange: (v) => { plan[l.key] = Number(v); },
    }).el));
  view.runButton = button(`Run ${WEEKS} weeks`, () => run());
  planPanel.body.append(
    h('p', { class: 'muted small' }, `${p.teamSize} ${p.team}; ${Math.round(p.teamSize * p.opportunityShare)} of them do the target work: ${p.task}.`),
    group1, group2,
    h('div', { class: 'btn-row' }, view.runButton,
      button('Same plan, other week-to-week luck', () => { seed += 1; run(); }, { variant: 'secondary' })),
  );

  view.results = h('div', {}, h('p', { class: 'muted' }, 'Choose your levers and run the 26 weeks. You can run as many plans as you like and compare them.'));
  const results = panel('The dashboard', { id: 'results' });
  results.body.appendChild(view.results);

  view.stoppedBody = h('div');
  const stopped = panel('Who stopped', { id: 'stopped' });
  view.stoppedHeading = stopped.heading;
  view.stoppedButton = button('Open the “who stopped” view', () => {
    stoppedOpened = true;
    renderStopped();
    focusEl(stopped.heading);
  }, { variant: 'secondary', disabled: true });
  stopped.body.append(
    h('p', {}, 'The vendor dashboard counts logins. It does not show who tried the tool, found nothing in it for their work and quietly went back to the old way.'),
    view.stoppedButton, view.stoppedBody);

  view.runsBody = h('div');
  const runsPanel = panel('Your runs', { id: 'runs' });
  runsPanel.body.appendChild(view.runsBody);

  const debrief = panel('Debrief', { id: 'debrief', className: 'debrief' });
  view.debriefHeading = debrief.heading;
  view.debrief = h('div');
  view.debriefButton = button('Show the debrief for my last run', () => {
    debriefShown = true;
    renderDebrief();
    focusEl(debrief.heading);
  }, { disabled: true });
  debrief.body.append(view.debriefButton, view.debrief);

  replace(shell.main,
    h('div', { class: 'layout layout-2' }, planPanel.el, h('div', { class: 'stack' }, results.el, stopped.el, runsPanel.el)),
    debrief.el);
}

function run() {
  const p = preset();
  last = { plan: { ...plan }, seed, result: simulate(p, plan, seed) };
  runs.unshift(last);
  runs = runs.slice(0, 6);
  stoppedOpened = false;
  view.stoppedButton.disabled = false;
  view.debriefButton.disabled = false;
  renderResults();
  replace(view.stoppedBody);
  renderRuns();
  if (debriefShown) renderDebrief();
  const s = last.result.summary;
  shell.announce(`Run finished. Weekly active users ${pct(s.activeRate)}, qualified-use rate ${pct(s.qualifiedRate)}.`);
}

function renderResults() {
  const p = preset();
  const { weeks, summary: s } = last.result;
  const chart = lineChart({
    title: 'Licences, weekly active users and qualified users',
    summary: `By week 26: ${num(s.licences)} licences, about ${num(s.activeRate * s.teamSize)} weekly active users, about ${num(s.qualifiedRate * s.opportunityPopulation)} people with qualified use.`,
    xLabel: 'Week', yLabel: 'People',
    xFormat: (v) => num(v), tableX: (v) => `Week ${v}`, yFormat: (v) => num(v), zeroLine: true,
    marker: last.plan.mandate > 0 ? { x: last.plan.mandate, label: 'mandate' } : last.plan.removeOldPath > 0 ? { x: last.plan.removeOldPath, label: 'old path removed' } : null,
    series: [
      { name: 'Licences active', points: weeks.map((w) => ({ x: w.week, y: w.licences })) },
      { name: 'Weekly active users', points: weeks.map((w) => ({ x: w.week, y: w.active })) },
      { name: 'People with qualified use', points: weeks.map((w) => ({ x: w.week, y: w.qualified })) },
    ],
  });
  replace(view.results,
    h('p', { class: 'small muted' }, `Plan: ${planText(last.plan)}. Weeks 23–26 on the tiles.`),
    h('h3', {}, 'What the vendor dashboard shows'),
    h('div', { class: 'stats' },
      stat('Licences active', num(s.licences), 'assigned in week 1'),
      stat('Weekly active users', pct(s.activeRate), `peak ${pct(s.peakActiveRate)} in week ${s.peakWeek}`, s.activeRate >= 0.7 ? 'good' : ''),
    ),
    h('h3', {}, 'What the honest dashboard shows'),
    h('div', { class: 'stats' },
      stat('Qualified-use rate', pct(s.qualifiedRate), `of the ${num(s.opportunityPopulation)} who do the target work`, s.qualifiedRate >= 0.5 ? 'good' : s.qualifiedRate < 0.3 ? 'bad' : 'warn'),
      stat('Hours saved per week', hours(s.hoursSavedPerWeek), `${p.usesPerWeek} uses × ${p.minutesPerUse} min per qualified user`),
      stat('Gap: active minus qualified', pct(Math.max(0, s.goodhartGap)), 'activity that is not value', s.goodhartGap > 0.3 ? 'bad' : ''),
      stat('Quietly stopped', stoppedOpened ? num(s.quietStoppers) : '?', stoppedOpened ? `${num(s.stillStopped)} still on the old way` : 'open the “who stopped” view'),
    ),
    chart.el,
  );
}

function renderStopped() {
  if (!last) return;
  renderResults();
  const list = whoStopped(last.result);
  const s = last.result.summary;
  if (!list.length) {
    replace(view.stoppedBody, h('p', {}, 'Nobody tried the tool and then quietly went back to the old way in this run.'),
      s.neverTried ? h('p', {}, `${plural(s.neverTried, 'person', 'people')} never tried it at all.`) : null);
    return;
  }
  replace(view.stoppedBody,
    h('p', {}, `${plural(list.length, 'person', 'people')} tried the tool and then stopped in week 3 or later. ${num(s.stillStopped)} are still on the old way in week 26.`,
      s.neverTried ? ` ${plural(s.neverTried, 'person', 'people')} never tried it.` : ''),
    h('div', { class: 'table-wrap' }, h('table', {},
      h('caption', { class: 'sr-only' }, 'People who stopped using the tool'),
      h('thead', {}, h('tr', {}, ['Name', 'Tried', 'Stopped', 'Went back to', 'Week 26'].map((c) => h('th', { scope: 'col' }, c)))),
      h('tbody', {}, list.map((x) => h('tr', {},
        h('th', { scope: 'row' }, x.name, x.hasOpportunity ? '' : ' (no target work)'),
        h('td', {}, `wk ${x.triedWeek}`),
        h('td', {}, `wk ${x.stoppedWeek}`),
        h('td', {}, x.backTo),
        h('td', {}, x.cameBack ? `came back (wk ${x.returnedWeek})` : x.stillCountedActive ? 'still counted as active' : 'on the old way'),
      ))))),
    list.some((x) => x.stillCountedActive)
      ? h('p', { class: 'callout callout-warn' }, 'Some people who stopped in practice are still counted as weekly active users: they log a use to satisfy the mandate.')
      : null,
    list.some((x) => /free|personal/i.test(x.backTo))
      ? h('p', { class: 'callout callout-warn' }, 'Some went back to a free AI tool on a personal account: quiet non-adoption can turn into shadow AI.')
      : null,
    h('p', { class: 'small muted' }, 'In a real team: report patterns by team and week, not named people, unless your policy and the law allow it. Ask the quiet non-adoption questions instead: who stopped, when, and back to what? Then ask frontline managers whether they expect the tool to be used, use it visibly themselves, and talk about it in regular conversations about the work.'),
  );
  shell.announce(`${list.length} people stopped quietly.`);
}

function renderRuns() {
  replace(view.runsBody, h('div', { class: 'table-wrap' }, h('table', {},
    h('caption', { class: 'sr-only' }, 'Your recent runs, newest first'),
    h('thead', {}, h('tr', {}, ['Plan', 'Weekly active', 'Qualified use', 'Hours saved / week', 'Quietly stopped'].map((c) => h('th', { scope: 'col' }, c)))),
    h('tbody', {}, runs.map((r, i) => h('tr', {},
      h('th', { scope: 'row' }, `${i === 0 ? 'Latest: ' : ''}${planText(r.plan)}${r.seed !== preset().seed ? ` (luck ${r.seed - preset().seed})` : ''}`),
      h('td', {}, pct(r.result.summary.activeRate)),
      h('td', {}, pct(r.result.summary.qualifiedRate)),
      h('td', {}, hours(r.result.summary.hoursSavedPerWeek)),
      h('td', {}, num(r.result.summary.quietStoppers)),
    ))))));
}

function renderDebrief() {
  if (!last) return;
  const s = last.result.summary;
  const pl = last.plan;
  const pts = [];
  pts.push(`Licences were ${num(s.licences)} out of ${num(s.teamSize)} every single week, whatever you did. A licence count says what you bought, not what people do.`);
  if (pl.mandate > 0) {
    pts.push(`The mandate pushed weekly active users to ${pct(s.activeRate)}, but only ${pct(s.qualifiedRate)} use the tool on the work that matters. About ${pct(s.forcedShare)} of the team logs use only because it is measured. That is Goodhart’s law: the dashboard became the target and stopped measuring adoption.`);
  }
  if (pl.training === 'generic' && !pl.redesign) {
    pts.push(`Generic training lifted the early peak (${pct(s.peakActiveRate)} in week ${s.peakWeek}) and then it faded: people learned the features, not how to do their own work with them.`);
  }
  if (pl.training !== 'role') pts.push('Without role-based training on the team’s real work, skill stays low and people stop finding value.');
  if (!pl.redesign) pts.push('The workflow was never redesigned, so the tool stayed a separate window next to the real work. Redesign gives the biggest lift to qualified use in this model.');
  if (pl.removeOldPath > 0 && (pl.training !== 'role' || !pl.redesign || pl.removeOldPath < pl.redesign)) {
    pts.push('You removed the old path before the new one worked. Activity jumped because there was no choice, but much of the forced use is not done well.');
  } else if (pl.removeOldPath > 0) {
    pts.push('You removed the old path only after the new one worked. That order matters: it locks in a habit people already have.');
  }
  if (!stoppedOpened) pts.push('You never opened the “who stopped” view. The quiet stoppers are invisible on the vendor dashboard; you only find them if you look.');
  else pts.push(`${plural(s.quietStoppers, 'person', 'people')} tried the tool and quietly went back to the old way. That is the signal a licence count and an activity count both hide.`);
  if (s.qualifiedRate >= 0.55 && s.goodhartGap < 0.25) pts.push('This plan built real adoption: the activity on the dashboard is mostly use on the work that matters.');

  replace(view.debrief,
    h('p', {}, `Your last run: ${planText(pl)}. Weekly active ${pct(s.activeRate)}, qualified use ${pct(s.qualifiedRate)}, ${hours(s.hoursSavedPerWeek)} saved a week.`),
    h('ul', {}, pts.map((x) => h('li', {}, x))),
    h('h3', {}, 'The point of this lesson'),
    h('p', { class: 'lesson-point' },
      'Licences ≠ adoption ≠ value. Measure qualified use among the people who actually do the target work, look for who quietly stopped and what they went back to, and never set activity as the target: a mandate inflates the dashboard without changing the work.'),
    h('p', { class: 'small muted' }, 'Try for yourself: a plan that reaches high qualified use without a mandate, then add a mandate from week 2 and compare the two rows in “Your runs”.'),
  );
}

shell = mountShell({
  title: 'Adoption dynamics',
  tagline: '26 weeks of rollout: licences, weekly active users, and the use that actually matters.',
  presets: PRESETS,
  defaultPreset: DEFAULT_PRESET,
  about: ABOUT,
  onPreset: start,
});
start(shell.presetKey);
