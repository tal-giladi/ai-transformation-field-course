// Number formatting shared by every simulation (pure, no DOM; safe to import in node).

const MINUS = '−';

function grouped(n, decimals) {
  return Math.abs(n).toLocaleString('en-US', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
}

function sign(n) {
  return n < 0 && Math.abs(n) >= 0.5 * 10 ** -6 ? MINUS : '';
}

/** Plain number with thousands separators: 12,345 or 3.5. */
export function num(n, decimals = 0) {
  if (!Number.isFinite(n)) return n > 0 ? '∞' : '–';
  const r = Number(n.toFixed(decimals));
  return sign(r) + grouped(r, decimals);
}

/** Israeli shekels: ₪12,345 or −₪1,200. */
export function ils(n, decimals = 0) {
  if (!Number.isFinite(n)) return '–';
  const r = Number(n.toFixed(decimals));
  return `${sign(r)}₪${grouped(r, decimals)}`;
}

/** Compact shekels for chart ticks: ₪12k, −₪1.2M. */
export function ilsShort(n) {
  if (!Number.isFinite(n)) return '–';
  const a = Math.abs(n);
  let body;
  if (a >= 1e6) body = `${trim(a / 1e6)}M`;
  else if (a >= 1e3) body = `${trim(a / 1e3)}k`;
  else body = trim(a);
  return `${n < 0 && a > 0 ? MINUS : ''}₪${body}`;
}

function trim(x) {
  return String(Number(x.toFixed(x >= 10 ? 0 : 1)));
}

/** US dollars: $1,234.50 */
export function usd(n, decimals = 2) {
  if (!Number.isFinite(n)) return '–';
  const r = Number(n.toFixed(decimals));
  return `${sign(r)}$${grouped(r, decimals)}`;
}

/** A fraction shown as a percentage: pct(0.381) -> "38%", pct(0.381, 1) -> "38.1%". */
export function pct(fraction, decimals = 0) {
  if (!Number.isFinite(fraction)) return '–';
  return `${num(fraction * 100, decimals)}%`;
}

/** Hours: "108.8 h". */
export function hours(n, decimals = 1) {
  if (!Number.isFinite(n)) return '–';
  return `${num(n, decimals)} h`;
}

/** Minutes: "2.5 min". */
export function minutes(n, decimals = 1) {
  if (!Number.isFinite(n)) return '–';
  return `${num(n, Number.isInteger(n) ? 0 : decimals)} min`;
}

/** Months to breakeven, or "never" when the pilot never pays back. */
export function monthsText(n) {
  if (!Number.isFinite(n) || n < 0) return 'never';
  if (n === 0) return 'immediately';
  return `${num(n, 1)} months`;
}

/** "1 question" / "3 questions". */
export function plural(n, one, many = `${one}s`) {
  return `${num(n)} ${n === 1 ? one : many}`;
}
