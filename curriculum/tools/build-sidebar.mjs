// Main-session tool (planning, not imported): rebuilds _sidebar.md from finished modules.
// Usage (from the course root): node curriculum/tools/build-sidebar.mjs
// A module is listed once its curriculum/status/module-NN.log contains "module done".
// Lesson numbers run across the course; link titles come from each lesson's H1.
import fs from "node:fs";

const MODULES = {
  1: "Walking In",
  2: "Discovery That Finds the Real Work",
  3: "From Findings to a Funded Portfolio",
  4: "Guardrails You Can Ship in Week Two",
  5: "Building and Testing a Pilot",
  6: "Making People Use It",
  7: "Readouts, Decisions and the Operating Rhythm",
  8: "Northwind Outfitters: The Chatbot That Should Not Replace Support",
  9: "Meridian Mutual: Claims, Fraud and a Regulated Verdict",
  10: "Galil Health: Choosing an Ambient Scribe",
  11: "Givat Oren: A Municipality's Citizen Assistant",
  12: "Atlas & Rowe: AI in a Law Firm",
  13: "Kinneret Plastics: When the Data Is Not Ready",
  14: "Lumen SaaS: Shipping an Agent",
  15: "Crescent Bank: Forty Pilots, Nothing in Production",
  16: "Open Hands: A Nonprofit With No Budget",
  17: "Vantage Logistics: Rescuing a Failing Program",
  18: "Your Engagement",
};
// Planned lesson counts (plan §6), so running numbers do not shift while modules are unfinished.
const PLANNED = { 1: 7, 2: 7, 3: 9, 4: 8, 5: 7, 6: 6, 7: 9, 18: 5 };
const STAGES = { 1: "Stage 1 — The field kit", 8: "Stage 2 — Ten engagements", 18: "Stage 3 — Capstone" };

const pad = (n) => String(n).padStart(2, "0");
const read = (f) => fs.readFileSync(f, "utf8").replace(/\r/g, "");
const top = ["- [Home](/)", "- [Glossary](glossary.md)", "- [Templates](templates/README.md)"];
for (const f of fs.existsSync("references") ? fs.readdirSync("references").filter((f) => f.endsWith(".md")).sort() : []) {
  const h1 = (read(`references/${f}`).match(/^# (.+)$/m) ?? [, f])[1].trim();
  top.push(`- [${h1}](references/${f})`);
}

const out = [...top];
let running = 0;
for (const [n, title] of Object.entries(MODULES)) {
  const NN = pad(n);
  const log = `curriculum/status/module-${NN}.log`;
  const dir = `lessons/module-${NN}`;
  const files = fs.existsSync(dir) ? fs.readdirSync(dir).filter((f) => /^lesson-\d{2}\.md$/.test(f)).sort() : [];
  const done = fs.existsSync(log) && /^module done$/m.test(read(log));
  if (STAGES[n] && done) out.push("", `- ${STAGES[n]}`);
  if (!done) { running += Math.max(files.length, PLANNED[n] ?? 6); continue; }
  out.push(`- **Module ${n} — ${title}**`);
  for (const f of files) {
    running++;
    const h1 = read(`${dir}/${f}`).match(/^# \d{2}\.\d+ · (.+)$/m);
    out.push(`  - [${pad(running)} · ${h1 ? h1[1].trim() : f}](${dir}/${f})`);
  }
  out.push(`  - [Module ${n} quiz](assessments/module-${NN}-quiz.md)`);
}
fs.writeFileSync("_sidebar.md", out.join("\n") + "\n");
// docsify preview sidebar: same links with a leading slash.
fs.writeFileSync("_site_sidebar.md", out.join("\n").replace(/\]\((?!\/\))/g, "](/") + "\n");
console.log(`sidebar: ${out.filter((l) => l.startsWith("  - [") && !l.includes("quiz")).length} lessons listed`);
