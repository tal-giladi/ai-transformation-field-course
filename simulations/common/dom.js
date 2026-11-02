// Tiny DOM helpers shared by every simulation. No innerHTML anywhere: all text goes in as text.

const SVG_NS = 'http://www.w3.org/2000/svg';
let counter = 0;

/** A unique id for label/aria wiring. */
export function uid(prefix = 'id') {
  counter += 1;
  return `${prefix}-${counter}`;
}

function setProps(el, props) {
  for (const [key, val] of Object.entries(props || {})) {
    if (val === undefined || val === null || val === false) continue;
    if (key === 'class') el.setAttribute('class', String(val));
    else if (key === 'text') el.textContent = String(val);
    else if (key.startsWith('on') && typeof val === 'function') el.addEventListener(key.slice(2).toLowerCase(), val);
    else if (key === 'value') el.value = String(val);
    else if (key === 'checked') el.checked = Boolean(val);
    else if (key === 'selected') el.selected = Boolean(val);
    else if (key === 'disabled') el.disabled = Boolean(val);
    else if (key === 'hidden') el.hidden = Boolean(val);
    else el.setAttribute(key, val === true ? '' : String(val));
  }
}

/** Append children; strings and numbers become text nodes; null/false are skipped; arrays are flattened. */
export function add(el, ...children) {
  for (const child of children.flat(Infinity)) {
    if (child === null || child === undefined || child === false) continue;
    el.appendChild(typeof child === 'object' ? child : document.createTextNode(String(child)));
  }
  return el;
}

/** Create an HTML element: h('button', { class: 'btn', onClick: fn }, 'Label'). */
export function h(tag, props, ...children) {
  const el = document.createElement(tag);
  setProps(el, props);
  return add(el, ...children);
}

/** Create an SVG element with attributes. */
export function s(tag, attrs, ...children) {
  const el = document.createElementNS(SVG_NS, tag);
  for (const [key, val] of Object.entries(attrs || {})) {
    if (val === undefined || val === null || val === false) continue;
    if (key === 'text') el.textContent = String(val);
    else el.setAttribute(key, String(val));
  }
  return add(el, ...children);
}

/** Remove every child. */
export function clear(el) {
  while (el.firstChild) el.removeChild(el.firstChild);
  return el;
}

/** Replace the children of el. */
export function replace(el, ...children) {
  clear(el);
  return add(el, ...children);
}

/** Move keyboard focus to an element (a heading gets tabindex=-1 first). */
export function focusEl(el) {
  if (!el) return;
  if (!el.hasAttribute('tabindex')) el.setAttribute('tabindex', '-1');
  try {
    el.focus({ preventScroll: false });
  } catch {
    el.focus();
  }
}
