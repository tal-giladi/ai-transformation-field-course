// A table that turns into labelled blocks on narrow screens (class "stack" in sim.css). Explicit ARIA
// roles keep it a table for screen readers when CSS changes its display.

import { h } from './dom.js';

/**
 * stackTable({ caption, head: [string], rows: [{ th: node|string, cells: [node|string] }] })
 * head[0] is the row-header column; head[1..] label the cells (shown before each cell when stacked).
 */
export function stackTable({ caption, head, rows }) {
  return h('div', { class: 'table-wrap' }, h('table', { class: 'stack', role: 'table' },
    caption ? h('caption', { class: 'sr-only' }, caption) : null,
    h('thead', { role: 'rowgroup' }, h('tr', { role: 'row' }, head.map((t) => h('th', { scope: 'col', role: 'columnheader' }, t)))),
    h('tbody', { role: 'rowgroup' }, rows.map((r) => h('tr', { role: 'row' },
      h('th', { scope: 'row', role: 'rowheader' }, r.th),
      r.cells.map((c, i) => h('td', { role: 'cell', 'data-label': head[i + 1] }, c)))))));
}
