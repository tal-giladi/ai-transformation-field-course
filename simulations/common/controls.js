// Labelled, keyboard-usable form controls. No <form> elements: the served pages forbid form actions.

import { h, uid } from './dom.js';

/**
 * A slider paired with an exact number box. Both are labelled; the slider announces the formatted
 * value (aria-valuetext). onInput(value) fires on every change.
 */
export function rangeField({ label, min, max, step = 1, value, format = String, help, unit = '', onInput }) {
  const id = uid('range');
  const helpId = help ? `${id}-help` : null;
  const out = h('output', { class: 'field-value', for: id });
  const range = h('input', {
    type: 'range', id, min, max, step, value,
    'aria-describedby': helpId,
  });
  const box = h('input', {
    type: 'number', class: 'field-number', min, max, step, value,
    'aria-label': `${label}, exact value${unit ? ` in ${unit}` : ''}`,
    inputmode: 'decimal',
  });

  const show = (v) => {
    out.textContent = format(v);
    range.setAttribute('aria-valuetext', format(v));
  };
  const commit = (v, from) => {
    if (!Number.isFinite(v)) return;
    const clamped = Math.min(Number(max), Math.max(Number(min), v));
    if (from !== range) range.value = String(clamped);
    if (from !== box) box.value = String(clamped);
    show(clamped);
    if (onInput) onInput(clamped);
  };
  range.addEventListener('input', () => commit(Number(range.value), range));
  box.addEventListener('change', () => commit(Number(box.value), box));
  show(Number(value));

  const el = h('div', { class: 'field' },
    h('div', { class: 'field-head' }, h('label', { for: id }, label), out),
    h('div', { class: 'field-row' }, range, unit ? h('span', { class: 'field-unit-wrap' }, box, h('span', { class: 'field-unit', 'aria-hidden': 'true' }, unit)) : box),
    help ? h('p', { class: 'field-help', id: helpId }, help) : null,
  );
  return {
    el,
    get value() { return Number(range.value); },
    set(v) { range.value = String(v); box.value = String(v); show(Number(v)); },
  };
}

/** A checkbox with a label and optional help text. onChange(checked). */
export function toggleField({ label, checked = false, help, onChange }) {
  const id = uid('toggle');
  const helpId = help ? `${id}-help` : null;
  const input = h('input', { type: 'checkbox', id, checked, 'aria-describedby': helpId });
  input.addEventListener('change', () => onChange && onChange(input.checked));
  const el = h('div', { class: 'field field-toggle' },
    h('div', { class: 'toggle-row' }, input, h('label', { for: id }, label)),
    help ? h('p', { class: 'field-help', id: helpId }, help) : null,
  );
  return { el, input, get checked() { return input.checked; } };
}

/** A labelled <select>. options: [{ value, label }]. onChange(value). */
export function selectField({ label, options, value, help, onChange }) {
  const id = uid('select');
  const helpId = help ? `${id}-help` : null;
  const select = h('select', { id, 'aria-describedby': helpId },
    options.map((o) => h('option', { value: o.value, selected: String(o.value) === String(value) }, o.label)));
  select.addEventListener('change', () => onChange && onChange(select.value));
  const el = h('div', { class: 'field' },
    h('div', { class: 'field-head' }, h('label', { for: id }, label)),
    select,
    help ? h('p', { class: 'field-help', id: helpId }, help) : null,
  );
  return { el, select, get value() { return select.value; } };
}

/** A button that is never a submit button. */
export function button(label, onClick, { variant = 'primary', ...props } = {}) {
  return h('button', { type: 'button', class: `btn btn-${variant}`, onClick, ...props }, label);
}

/** A small key-number tile: label, value, optional note. tone: '', 'good', 'bad', 'warn'. */
export function stat(label, value, note, tone = '') {
  return h('div', { class: `stat ${tone ? `stat-${tone}` : ''}` },
    h('div', { class: 'stat-label' }, label),
    h('div', { class: 'stat-value' }, value),
    note ? h('div', { class: 'stat-note' }, note) : null,
  );
}
