// Per-module validator for writers (planning tool, not imported). Adapted from activist-law-course.
// Usage (from the course root): node curriculum/tools/check-module.mjs 03
// Uses js-yaml from the Academy repo's node_modules.
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";

const require = createRequire("C:/Users/TalGiladi/OneDrive/repos/tals-academy/package.json");
const yaml = require("js-yaml");

const NN = process.argv[2];
if (!/^\d{2}$/.test(NN ?? "")) {
  console.error("usage: node curriculum/tools/check-module.mjs NN");
  process.exit(2);
}
const root = process.cwd();
const problems = [];
const warn = (f, m) => problems.push(`${f}: ${m}`);
const SECTIONS = ["The situation", "What to do", "Watch out", "Your turn", "References"];
const BAD_HTML = /<(div|script|style|iframe|svg|button|form|input|object|embed|span|p|img|a|table)\b|\son\w+\s*=/i;

function checkLinks(file, body) {
  const dir = path.dirname(file);
  for (const m of body.matchAll(/!?\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g)) {
    let target = m[1];
    if (/^(https?:|mailto:|#)/.test(target)) continue;
    target = target.split("#")[0].split("?")[0];
    if (!target) continue;
    const abs = path.resolve(root, dir, target);
    if (!fs.existsSync(abs)) warn(file, `broken link ${m[1]}`);
  }
  if (/\]\(\/(?!\))/.test(body)) warn(file, "link with leading slash");
}

function checkQuiz(file, min, max) {
  if (!fs.existsSync(path.join(root, file))) return warn(file, "missing");
  let qs;
  try {
    qs = yaml.load(fs.readFileSync(path.join(root, file), "utf8"));
  } catch (e) {
    return warn(file, `YAML parse error: ${e.message.split("\n")[0]}`);
  }
  if (!Array.isArray(qs)) return warn(file, "not a list");
  if (qs.length < min || qs.length > max) warn(file, `${qs.length} questions, expected ${min}-${max}`);
  const ids = new Set();
  const pos = [0, 0, 0, 0];
  for (const q of qs) {
    const where = `${file} ${q.id}`;
    if (!q.id || ids.has(q.id)) warn(where, "missing or duplicate id");
    ids.add(q.id);
    if (typeof q.question !== "string" || !q.question.trim()) warn(where, "no question");
    if (!Array.isArray(q.options) || q.options.length !== 4) { warn(where, "needs exactly 4 options"); continue; }
    if (new Set(q.options.map((o) => String(o).trim())).size !== 4) warn(where, "options not distinct");
    if (![0, 1, 2, 3].includes(q.correct)) { warn(where, "correct must be 0-3"); continue; }
    pos[q.correct]++;
    if (typeof q.explanation !== "string" || !q.explanation.trim()) warn(where, "no explanation");
    if ("source" in q) warn(where, "has source: field");
    if (q.options.some((o) => /\b(all|none) of the above\b/i.test(String(o)))) warn(where, "all/none of the above");
    const lens = q.options.map((o) => String(o).length);
    const c = lens[q.correct];
    const others = lens.filter((_, i) => i !== q.correct);
    const avg = others.reduce((a, b) => a + b, 0) / 3;
    if (c > Math.max(...others) && c > avg * 1.25) warn(where, `correct option noticeably longest (${c} vs avg ${Math.round(avg)})`);
  }
  if (qs.length >= 8 && pos.some((p) => p === 0)) warn(file, `correct positions not spread: ${pos.join("/")}`);
  if (qs.length >= 4 && pos.some((p) => p > Math.ceil(qs.length * (qs.length > 20 ? 0.35 : 0.5)))) warn(file, `correct positions clustered: ${pos.join("/")}`);
}

const lessonDir = path.join("lessons", `module-${NN}`);
const files = fs.existsSync(lessonDir) ? fs.readdirSync(lessonDir).filter((f) => /^lesson-\d{2}\.md$/.test(f)).sort() : [];
if (!files.length) warn(lessonDir, "no lessons");
for (const f of files) {
  const rel = path.join(lessonDir, f).replace(/\\/g, "/");
  const raw = fs.readFileSync(rel, "utf8");
  if (raw.includes("\r")) warn(rel, "CRLF line endings");
  const fm = /^---\n([\s\S]*?)\n---\n/.exec(raw);
  if (!fm) { warn(rel, "no front-matter"); continue; }
  let data;
  try { data = yaml.load(fm[1]); } catch (e) { warn(rel, `front-matter YAML error: ${e.message.split("\n")[0]}`); continue; }
  const MM = f.slice(7, 9);
  const id = `${NN}.${Number(MM)}`;
  if (data.id !== id) warn(rel, `id "${data.id}" should be "${id}"`);
  if (data.module !== Number(NN)) warn(rel, "module number wrong");
  for (const k of ["minutes", "practice_minutes", "prerequisites", "objectives", "volatility", "sources", "last_verified"])
    if (!(k in data)) warn(rel, `front-matter missing ${k}`);
  if (!Array.isArray(data.sources) || !data.sources.length) warn(rel, "no sources");
  for (const p of data.prerequisites ?? []) if (!/^\d{2}\.\d+$/.test(p)) warn(rel, `bad prerequisite ${p}`);
  const body = raw.slice(fm[0].length);
  const noCode = body.replace(/```[\s\S]*?```/g, "").replace(/`[^`\n]*`/g, "");
  const h1 = noCode.match(/^# .+$/gm) ?? [];
  if (h1.length !== 1 || !h1[0].startsWith(`# ${id} · `)) warn(rel, `H1 must be exactly one "# ${id} · Title"`);
  const afterH1 = body.split(/^# .+$/m)[1] ?? "";
  const firstPara = afterH1.trim().split(/\n\s*\n/)[0] ?? "";
  if (!firstPara || /^[#>*\-|!<`]/.test(firstPara) || /^_/.test(firstPara)) warn(rel, "intro paragraph after H1 missing or not plain");
  const h2 = [...noCode.matchAll(/^## (.+)$/gm)].map((m) => m[1].trim());
  if (JSON.stringify(h2) !== JSON.stringify(SECTIONS)) warn(rel, `## sections must be exactly: ${SECTIONS.join(" | ")} (found: ${h2.join(" | ")})`);
  if (BAD_HTML.test(noCode)) warn(rel, "disallowed raw HTML");
  checkLinks(rel, body);
  checkQuiz(rel.replace(/\.md$/, ".quiz.yaml"), 3, 5);
}
const mq = `assessments/module-${NN}-quiz.md`;
if (!fs.existsSync(mq)) warn(mq, "missing");
else {
  const t = fs.readFileSync(mq, "utf8");
  if (/^#{1,3}\s*(Answers|Answer Key)/im.test(t)) warn(mq, "answers heading");
  checkLinks(mq, t);
  checkQuiz(`assessments/module-${NN}-quiz.quiz.yaml`, 8, 10);
}
const proj = fs.existsSync("projects") ? fs.readdirSync("projects").filter((f) => f.startsWith(`m${NN}-`)) : [];
if (!proj.length) warn("projects", `no projects/m${NN}-*.md`);
for (const p of proj) checkLinks(`projects/${p}`, fs.readFileSync(`projects/${p}`, "utf8"));
// Labs: every module has labs/module-NN/README.md; every engagement module (08-17) has the full pack.
const labDir = `labs/module-${NN}`;
if (!fs.existsSync(`${labDir}/README.md`)) warn(labDir, "missing README.md");
else checkLinks(`${labDir}/README.md`, fs.readFileSync(`${labDir}/README.md`, "utf8"));
if (Number(NN) >= 8 && Number(NN) <= 17)
  for (const f of ["brief.md", "data-room/INDEX.md", "data-room/generate.py", "personas/README.md", "expert"])
    if (!fs.existsSync(`${labDir}/${f}`)) warn(labDir, `missing ${f}`);
for (const f of fs.existsSync(`curriculum/inbox/templates`) ? fs.readdirSync("curriculum/inbox/templates") : [])
  if (!/\.md$/.test(f)) warn("curriculum/inbox/templates", `not markdown: ${f}`);

console.log(problems.length ? problems.join("\n") : "");
console.log(`${problems.length} problems in module ${NN}`);
process.exit(problems.length ? 1 : 0);
