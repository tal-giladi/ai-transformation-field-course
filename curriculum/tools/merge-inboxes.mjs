// Main-session tool (planning, not imported): merges module inboxes into shared files.
// Usage (from the course root): node curriculum/tools/merge-inboxes.mjs [template-file.md ...]
// Idempotent: moves template drafts into templates/, rebuilds the templates README list and the glossary.
import fs from "node:fs";
import path from "node:path";

const read = (f) => fs.readFileSync(f, "utf8").replace(/\r/g, "");
const list = (dir, re) => (fs.existsSync(dir) ? fs.readdirSync(dir).filter((f) => re.test(f)).sort() : []);

// Templates: move drafts that are not yet published.
const tIn = "curriculum/inbox/templates";
// Optional args: template file names to move (others stay in the inbox, e.g. while an agent still writes them).
const only = process.argv.slice(2);
for (const f of list(tIn, /\.md$/).filter((f) => !only.length || only.includes(f))) {
  if (!fs.existsSync(path.join("templates", f))) fs.renameSync(path.join(tIn, f), path.join("templates", f));
  else console.log(`template exists, left in inbox: ${f}`);
}
const tItems = list("templates", /\.md$/)
  .filter((f) => f !== "README.md")
  .map((f) => {
    const h1 = (read(path.join("templates", f)).match(/^# (.+)$/m) ?? [, f])[1].trim();
    return { h1, line: `- [${h1}](${f})` };
  })
  .sort((a, b) => a.h1.localeCompare(b.h1, "en"))
  .map((t) => t.line);
const tHead = read("templates/README.md").split("\n## All templates")[0].trimEnd();
fs.writeFileSync("templates/README.md", `${tHead}\n\n## All templates\n\n${tItems.join("\n")}\n`);

// Glossary: keep the existing terms, add inbox terms, dedupe by term (case-insensitive), sort.
const terms = new Map();
const add = (line) => {
  const m = /^- \*\*(.+?)\*\*/.exec(line);
  if (m && !terms.has(m[1].toLowerCase())) terms.set(m[1].toLowerCase(), line.trim());
};
const gParts = read("glossary.md").split("\n## Terms");
for (const line of (gParts[1] ?? "").split("\n")) add(line);
for (const f of list("curriculum/glossary-inbox", /^module-\d{2}\.md$/))
  for (const line of read(`curriculum/glossary-inbox/${f}`).split("\n")) add(line);
const gLines = [...terms.keys()].sort((a, b) => a.localeCompare(b, "en")).map((k) => terms.get(k));
fs.writeFileSync("glossary.md", `${gParts[0].trimEnd()}\n\n## Terms\n\n${gLines.join("\n")}\n`);

console.log(`templates ${tItems.length}, terms ${terms.size}`);
