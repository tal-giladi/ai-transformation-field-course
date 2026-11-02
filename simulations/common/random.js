// Seeded random numbers (pure, no DOM). Same seed -> same run, so a debrief can be reproduced.

/** A 32-bit hash of a string, for turning a preset name into a seed. */
export function hashString(text) {
  let h = 2166136261;
  for (let i = 0; i < text.length; i += 1) {
    h ^= text.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

/** mulberry32: small, fast, good enough for teaching models. Returns floats in [0, 1). */
export function mulberry32(seed) {
  let a = seed >>> 0;
  return function next() {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/** A random generator with helpers. seed may be a number or a string. */
export function makeRng(seed) {
  const next = mulberry32(typeof seed === 'string' ? hashString(seed) : seed);
  return {
    next,
    /** true with probability p */
    chance: (p) => next() < p,
    /** integer in [min, max] */
    int: (min, max) => min + Math.floor(next() * (max - min + 1)),
    /** uniform float in [min, max) */
    range: (min, max) => min + next() * (max - min),
    /** one element of an array */
    pick: (arr) => arr[Math.floor(next() * arr.length)],
    /** a shuffled copy */
    shuffle(arr) {
      const out = arr.slice();
      for (let i = out.length - 1; i > 0; i -= 1) {
        const j = Math.floor(next() * (i + 1));
        [out[i], out[j]] = [out[j], out[i]];
      }
      return out;
    },
  };
}

