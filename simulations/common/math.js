// Small numeric helpers (pure, no DOM).

/** Evenly spaced values from a to b inclusive (n intervals, n + 1 values). */
export function steps(a, b, n) {
  const out = [];
  for (let i = 0; i <= n; i += 1) out.push(Number((a + ((b - a) * i) / n).toFixed(6)));
  return out;
}

/** Clamp x into [lo, hi]. */
export function clamp(x, lo, hi) {
  return Math.min(hi, Math.max(lo, x));
}
