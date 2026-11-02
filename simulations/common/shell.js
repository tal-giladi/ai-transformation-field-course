// The page shell every simulation uses: title, the "educational model" label, a preset picker,
// the "Your situation" brief, an "About this model" panel, a main area and a polite live region.

import { h, add, clear, replace } from './dom.js';
import { load, save } from './storage.js';

export const EDU_LABEL = 'Educational model — simplified on purpose';

/** The preset named in ?preset=, if it exists; otherwise the fallback. */
export function readPresetKey(presets, fallback) {
  let wanted = null;
  try {
    wanted = new URLSearchParams(window.location.search).get('preset');
  } catch {
    wanted = null;
  }
  if (wanted && Object.prototype.hasOwnProperty.call(presets, wanted)) return { key: wanted, unknown: null };
  return { key: fallback, unknown: wanted };
}

function rememberPresetInUrl(key) {
  // Sandboxed pages (opaque origin) may refuse history changes; the picker works without it.
  try {
    const url = new URL(window.location.href);
    url.searchParams.set('preset', key);
    window.history.replaceState(null, '', url.search + url.hash);
  } catch {
    /* ignore */
  }
}

/**
 * about: { intro, equations: [string], assumptions: [string], leftOut: [string] }
 * Each entry is plain text (shown as a list item).
 */
function aboutBody(about) {
  const list = (title, items) => (items && items.length
    ? [h('h3', {}, title), h('ul', {}, items.map((t) => h('li', {}, t)))]
    : null);
  return [
    about.intro ? h('p', {}, about.intro) : null,
    list('How it calculates', about.equations),
    list('Assumptions', about.assumptions),
    list('Left out on purpose', about.leftOut),
  ];
}

/**
 * Build the shell inside #app.
 * opts: { title, tagline, presets: { key: { label, brief } }, defaultPreset, about, onPreset(key) }
 * onPreset runs when the learner picks another scenario; start the first run with shell.presetKey.
 * Returns { main, presetKey, announce(text), setBrief(text) }.
 */
export function mountShell(opts) {
  const root = document.getElementById('app');
  clear(root);
  const { key, unknown } = readPresetKey(opts.presets, opts.defaultPreset);
  let current = key;

  const select = h('select', { id: 'preset-picker' },
    Object.entries(opts.presets).map(([k, p]) => h('option', { value: k, selected: k === current }, p.label)));
  const briefText = h('p', { class: 'brief-text' });
  const notice = h('p', { class: 'notice', role: 'status', hidden: !unknown },
    unknown ? `There is no scenario called “${unknown}”. Showing “${opts.presets[current].label}” instead.` : '');
  const main = h('main', { id: 'sim-main', class: 'sim-main' });
  const live = h('div', { class: 'sr-only', 'aria-live': 'polite', role: 'status' });

  const aboutOpen = load('about-open') === true;
  const about = h('details', { class: 'about', open: aboutOpen },
    h('summary', {}, 'About this model'),
    h('div', { class: 'about-body' }, aboutBody(opts.about || {})),
  );
  about.addEventListener('toggle', () => save('about-open', about.open));

  add(root,
    h('a', { class: 'skip-link', href: '#sim-main' }, 'Skip to the simulation'),
    h('header', { class: 'sim-header' },
      h('div', { class: 'title-row' },
        h('h1', {}, opts.title),
        h('span', { class: 'edu-badge' }, EDU_LABEL),
      ),
      opts.tagline ? h('p', { class: 'tagline' }, opts.tagline) : null,
      h('div', { class: 'preset-row' },
        h('label', { for: 'preset-picker' }, 'Scenario'),
        select,
      ),
      notice,
    ),
    h('section', { class: 'brief', 'aria-labelledby': 'brief-heading' },
      h('h2', { id: 'brief-heading' }, 'Your situation'),
      briefText,
    ),
    about,
    main,
    live,
    h('footer', { class: 'sim-footer' },
      h('p', {}, 'Fictional organizations and people. Numbers are illustrative, not measured. ',
        'Use this to practise a decision, not to make one.')),
  );

  const setBrief = (text) => replace(briefText, text);
  setBrief(opts.presets[current].brief);

  select.addEventListener('change', () => {
    current = select.value;
    notice.hidden = true;
    setBrief(opts.presets[current].brief);
    rememberPresetInUrl(current);
    opts.onPreset(current);
  });

  let liveTimer = null;
  const announce = (text) => {
    // Clear then set, so the same message is read again when repeated.
    live.textContent = '';
    if (liveTimer) clearTimeout(liveTimer);
    liveTimer = setTimeout(() => { live.textContent = text; }, 50);
  };

  // The caller starts the first run itself (shell.presetKey) once it holds the returned object.
  return { main, get presetKey() { return current; }, announce, setBrief };
}

/** A titled panel (section with h2). Returns { el, body }. */
export function panel(title, { id, className = '' } = {}) {
  const headingId = id ? `${id}-h` : undefined;
  const heading = h('h2', { id: headingId }, title);
  const body = h('div', { class: 'panel-body' });
  const el = h('section', { class: `panel ${className}`, id, 'aria-labelledby': headingId }, heading, body);
  return { el, body, heading };
}
