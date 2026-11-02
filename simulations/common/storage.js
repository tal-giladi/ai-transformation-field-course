// localStorage is optional: a sandboxed iframe (allow-scripts only) has an opaque origin and
// throws on access. Every read and write is wrapped; callers must work when these return null/false.

const PREFIX = 'aitf-sim:';

export function load(key) {
  try {
    const raw = window.localStorage.getItem(PREFIX + key);
    return raw === null ? null : JSON.parse(raw);
  } catch {
    return null;
  }
}

export function save(key, value) {
  try {
    window.localStorage.setItem(PREFIX + key, JSON.stringify(value));
    return true;
  } catch {
    return false;
  }
}
