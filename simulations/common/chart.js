// A tiny accessible chart helper: inline SVG drawn by JS, plus the same numbers as a table.
// Series are told apart by colour AND dash pattern, so the chart still reads in greyscale.

import { h, s, clear, uid } from './dom.js';

const DASHES = ['', '6 4', '2 3', '10 3 2 3'];

function niceStep(range, count) {
  const raw = range / count;
  const p = 10 ** Math.floor(Math.log10(raw));
  const f = raw / p;
  const nf = f < 1.5 ? 1 : f < 3 ? 2 : f < 7 ? 5 : 10;
  return nf * p;
}

/** Round tick values covering [min, max]. Exported for tests. */
export function ticks(min, max, count = 5) {
  let lo = min;
  let hi = max;
  if (!Number.isFinite(lo) || !Number.isFinite(hi)) return [0, 1];
  if (lo === hi) {
    lo -= Math.abs(lo) * 0.1 || 1;
    hi += Math.abs(hi) * 0.1 || 1;
  }
  const step = niceStep(hi - lo, count);
  const start = Math.floor(lo / step) * step;
  const end = Math.ceil(hi / step) * step;
  const out = [];
  for (let v = start; v <= end + step / 2; v += step) out.push(Number(v.toFixed(10)));
  return out;
}

function widthOf(container, fallback) {
  const w = container && container.clientWidth;
  return Math.max(280, Math.round(w || fallback));
}

function observe(container, redraw) {
  if (typeof ResizeObserver !== 'function') return;
  let last = container.clientWidth;
  let pending = false;
  const ro = new ResizeObserver(() => {
    if (pending) return;
    pending = true;
    requestAnimationFrame(() => {
      pending = false;
      if (Math.abs(container.clientWidth - last) > 8) {
        last = container.clientWidth;
        redraw();
      }
    });
  });
  ro.observe(container);
}

/**
 * Line chart. opts: {
 *   title, summary (one sentence for screen readers), xLabel, yLabel,
 *   xFormat(v), yFormat(v) (axis ticks), tableX(v), tableY(v) (table cells, default = axis formats),
 *   series: [{ name, points: [{ x, y }] }],
 *   marker: { x, label } (optional vertical line, e.g. "your setting"),
 *   zeroLine: true to emphasise y = 0, height
 * }
 * Returns { el, update(opts) }. Put el in the page; update redraws in place.
 */
export function lineChart(initial) {
  let opts = initial;
  const titleId = uid('chart-title');
  const descId = uid('chart-desc');
  const figure = h('figure', { class: 'chart' });
  const caption = h('figcaption', { class: 'chart-title', id: titleId });
  const plot = h('div', { class: 'chart-plot' });
  const legend = h('ul', { class: 'chart-legend', 'aria-hidden': 'true' });
  const tableWrap = h('div', { class: 'table-wrap' });
  const details = h('details', { class: 'chart-table' }, h('summary', {}, 'Show the numbers as a table'), tableWrap);
  figure.append(caption, plot, legend, details);

  function draw() {
    const o = opts;
    const xf = o.xFormat || String;
    const yf = o.yFormat || String;
    caption.textContent = o.title || '';
    const W = widthOf(plot, 600);
    const H = o.height || 240;
    const m = { l: 60, r: 14, t: 14, b: 44 };
    const all = o.series.flatMap((se) => se.points);
    const xs = all.map((p) => p.x);
    const ys = all.map((p) => p.y).filter(Number.isFinite);
    const xMin = Math.min(...xs);
    const xMax = Math.max(...xs);
    const yT = ticks(Math.min(...ys, o.zeroLine ? 0 : Infinity), Math.max(...ys, o.zeroLine ? 0 : -Infinity), 4);
    const yMin = yT[0];
    const yMax = yT[yT.length - 1];
    const X = (v) => m.l + ((v - xMin) / (xMax - xMin || 1)) * (W - m.l - m.r);
    const Y = (v) => m.t + (1 - (v - yMin) / (yMax - yMin || 1)) * (H - m.t - m.b);

    const svg = s('svg', {
      viewBox: `0 0 ${W} ${H}`, width: W, height: H, role: 'img',
      'aria-labelledby': titleId, 'aria-describedby': descId, class: 'chart-svg',
    });
    svg.appendChild(s('desc', { id: descId, text: o.summary || '' }));

    for (const t of yT) {
      svg.appendChild(s('line', { x1: m.l, x2: W - m.r, y1: Y(t), y2: Y(t), class: t === 0 && o.zeroLine ? 'zero' : 'grid' }));
      svg.appendChild(s('text', { x: m.l - 6, y: Y(t) + 4, 'text-anchor': 'end', class: 'tick', text: yf(t) }));
    }
    const xT = ticks(xMin, xMax, W < 420 ? 3 : 5).filter((t) => t >= xMin - 1e-9 && t <= xMax + 1e-9);
    for (const t of xT) {
      svg.appendChild(s('line', { x1: X(t), x2: X(t), y1: H - m.b, y2: H - m.b + 4, class: 'axis' }));
      svg.appendChild(s('text', { x: X(t), y: H - m.b + 17, 'text-anchor': 'middle', class: 'tick', text: xf(t) }));
    }
    svg.appendChild(s('line', { x1: m.l, x2: W - m.r, y1: H - m.b, y2: H - m.b, class: 'axis' }));
    svg.appendChild(s('line', { x1: m.l, x2: m.l, y1: m.t, y2: H - m.b, class: 'axis' }));
    if (o.xLabel) svg.appendChild(s('text', { x: (m.l + W - m.r) / 2, y: H - 6, 'text-anchor': 'middle', class: 'axis-label', text: o.xLabel }));
    if (o.yLabel) {
      svg.appendChild(s('text', {
        x: 0, y: 0, transform: `translate(12 ${(m.t + H - m.b) / 2}) rotate(-90)`,
        'text-anchor': 'middle', class: 'axis-label', text: o.yLabel,
      }));
    }

    o.series.forEach((se, i) => {
      const pts = se.points.filter((p) => Number.isFinite(p.y));
      if (!pts.length) return;
      const d = pts.map((p, k) => `${k ? 'L' : 'M'}${X(p.x).toFixed(1)} ${Y(Math.min(yMax, Math.max(yMin, p.y))).toFixed(1)}`).join(' ');
      svg.appendChild(s('path', { d, class: `line s${i % 4}`, 'stroke-dasharray': DASHES[i % 4] || null }));
    });

    if (o.marker && Number.isFinite(o.marker.x)) {
      const mx = X(Math.min(xMax, Math.max(xMin, o.marker.x)));
      svg.appendChild(s('line', { x1: mx, x2: mx, y1: m.t, y2: H - m.b, class: 'marker' }));
      const anchor = mx > W - 120 ? 'end' : 'start';
      svg.appendChild(s('text', { x: mx + (anchor === 'end' ? -4 : 4), y: m.t + 10, 'text-anchor': anchor, class: 'marker-label', text: o.marker.label || '' }));
    }

    clear(plot).appendChild(svg);

    clear(legend);
    o.series.forEach((se, i) => {
      const sw = s('svg', { width: 28, height: 10, viewBox: '0 0 28 10', 'aria-hidden': 'true' },
        s('line', { x1: 1, x2: 27, y1: 5, y2: 5, class: `line s${i % 4}`, 'stroke-dasharray': DASHES[i % 4] || null }));
      legend.appendChild(h('li', {}, sw, se.name));
    });

    const tx = o.tableX || xf;
    const ty = o.tableY || yf;
    const xsUnique = [...new Set(o.series.flatMap((se) => se.points.map((p) => p.x)))].sort((a, b) => a - b);
    const table = h('table', {},
      h('caption', { class: 'sr-only' }, o.title || 'Chart data'),
      h('thead', {}, h('tr', {}, h('th', { scope: 'col' }, o.xLabel || 'x'), o.series.map((se) => h('th', { scope: 'col' }, se.name)))),
      h('tbody', {}, xsUnique.map((x) => h('tr', {},
        h('th', { scope: 'row' }, tx(x)),
        o.series.map((se) => {
          const p = se.points.find((q) => q.x === x);
          return h('td', {}, p && Number.isFinite(p.y) ? ty(p.y) : '–');
        }),
      ))),
    );
    clear(tableWrap).appendChild(table);
  }

  draw();
  observe(plot, draw);
  return {
    el: figure,
    update(next) {
      opts = next;
      draw();
    },
    redraw: draw,
  };
}

/**
 * Horizontal bar chart for a few labelled values (e.g. a ledger). opts: {
 *   title, summary, format(v), items: [{ label, value, tone: 'good'|'bad'|'neutral' }]
 * }
 * Returns { el, update(opts) }.
 */
export function barChart(initial) {
  let opts = initial;
  const titleId = uid('chart-title');
  const descId = uid('chart-desc');
  const figure = h('figure', { class: 'chart' });
  const caption = h('figcaption', { class: 'chart-title', id: titleId });
  const plot = h('div', { class: 'chart-plot' });
  const tableWrap = h('div', { class: 'table-wrap' });
  const details = h('details', { class: 'chart-table' }, h('summary', {}, 'Show the numbers as a table'), tableWrap);
  figure.append(caption, plot, details);

  function draw() {
    const o = opts;
    const f = o.format || String;
    caption.textContent = o.title || '';
    const W = widthOf(plot, 600);
    const row = 30;
    const labelW = Math.min(170, Math.round(W * 0.38));
    const valueW = 78;
    const H = o.items.length * row + 10;
    const vals = o.items.map((it) => it.value);
    const lo = Math.min(0, ...vals);
    const hi = Math.max(0, ...vals);
    const span = hi - lo || 1;
    const x0 = labelW + 6;
    const plotW = W - x0 - valueW;
    const X = (v) => x0 + ((v - lo) / span) * plotW;
    const svg = s('svg', {
      viewBox: `0 0 ${W} ${H}`, width: W, height: H, role: 'img',
      'aria-labelledby': titleId, 'aria-describedby': descId, class: 'chart-svg',
    });
    svg.appendChild(s('desc', { id: descId, text: o.summary || '' }));
    o.items.forEach((it, i) => {
      const y = 6 + i * row;
      const a = X(Math.min(0, it.value));
      const b = X(Math.max(0, it.value));
      svg.appendChild(s('text', { x: labelW, y: y + 17, 'text-anchor': 'end', class: 'tick bar-label', text: it.label }));
      svg.appendChild(s('rect', { x: a, y: y + 4, width: Math.max(1, b - a), height: row - 10, rx: 2, class: `bar bar-${it.tone || 'neutral'}` }));
      svg.appendChild(s('text', { x: b + 4, y: y + 17, class: 'tick', text: f(it.value) }));
    });
    svg.appendChild(s('line', { x1: X(0), x2: X(0), y1: 2, y2: H - 2, class: 'zero' }));
    clear(plot).appendChild(svg);

    const table = h('table', {},
      h('caption', { class: 'sr-only' }, o.title || 'Chart data'),
      h('thead', {}, h('tr', {}, h('th', { scope: 'col' }, 'Item'), h('th', { scope: 'col' }, 'Value'))),
      h('tbody', {}, o.items.map((it) => h('tr', {}, h('th', { scope: 'row' }, it.label), h('td', {}, f(it.value))))),
    );
    clear(tableWrap).appendChild(table);
  }

  draw();
  observe(plot, draw);
  return {
    el: figure,
    update(next) {
      opts = next;
      draw();
    },
    redraw: draw,
  };
}
