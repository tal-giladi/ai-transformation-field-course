"""Shadow-AI census (lesson 01.6), Track B.

Pulls the AI signals out of four exports and prints one table per source, by department, never
by person: the web proxy log, the browser-extension inventory, the expense claims and the SaaS list.
Python is worth it here because the same census has to be re-run every quarter on fresh exports:
the host list below is the part you maintain.

Run from this folder:
    python census.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))

import pandas as pd  # noqa: E402

from fieldkit.data import data_room, load  # noqa: E402

# Hosts that mean AI use. Keep this list yourself: proxy categories miss new tools
# (two of these are "Uncategorized" in the Harbor & Pine proxy).
AI_HOSTS = {
    "chatgpt.com": "ChatGPT",
    "chat.openai.com": "ChatGPT",
    "gemini.google.com": "Gemini",
    "claude.ai": "Claude",
    "app.copygenie.io": "CopyGenie",
    "api.linguaflow.ai": "LinguaFlow",
    "capi.grammarly.com": "Grammarly",
    "www.deepl.com": "DeepL",
    "match-ai.peoplewise.io": "PeopleWise AI match",
}
AI_WORDS = r"(?i)openai|chatgpt|copygenie|midjourney|anthropic|claude|gemini|linguaflow|deepl|grammarly|\bai\b"


def main() -> None:
    room = data_room("harbor-and-pine")
    pd.set_option("display.width", 200)

    proxy = load(room / "it" / "proxy-log.csv")
    ai = proxy[proxy["dest_host"].isin(AI_HOSTS)].copy()
    ai["tool"] = ai["dest_host"].map(AI_HOSTS)
    print(f"Proxy log {proxy['timestamp'].min():%d %b} - {proxy['timestamp'].max():%d %b %Y}: "
          f"{len(ai)} of {len(proxy)} requests go to AI tools")
    by_dept = ai.groupby(["tool", "department"]).agg(
        requests=("dest_host", "size"),
        users=("user_id", "nunique"),
        median_bytes_out=("bytes_out", "median"),
    )
    print(by_dept.to_string(), "\n")
    print("Proxy category of each AI host (a category filter alone would miss these):")
    print(ai.groupby("dest_host")["url_category"].first().to_string(), "\n")
    print("Median bytes sent per request, for comparison: docs.google.com =",
          proxy.loc[proxy["dest_host"] == "docs.google.com", "bytes_out"].median(), "\n")

    ext = load(room / "it" / "browser-extensions.csv")
    ai_ext = ext[ext["extension_name"].str.contains(AI_WORDS, regex=True)]
    print("Browser extensions with AI, machines per department:")
    print(ai_ext.groupby(["extension_name", "department"])["device"].nunique().to_string(), "\n")

    exp = load(room / "it" / "expenses.csv")
    ai_exp = exp[exp["merchant"].str.contains(AI_WORDS, regex=True)]
    print("AI subscriptions in expense claims (look at payment_method and category):")
    print(ai_exp.groupby(["merchant", "department", "payment_method", "category"])
          .agg(claims=("amount_ils", "size"), total_ils=("amount_ils", "sum")).to_string())
    print(f"Total: {ai_exp['amount_ils'].sum():,.2f} ILS in {len(ai_exp)} claims\n")

    # Traces of chatbot drafting left in agents' replies: assistant preambles and unfilled placeholders,
    # in the four languages the team writes in. Report the count by language, never the agent.
    traces = (r"(?i)certainly! here|here's a polite|بالتأكيد! إليك|конечно! вот|вот улучшенная версия"
              r"|\[имя клиента\]|\[customer name\]|\[שם הלקוח\]|\[اسم العميل\]")
    emails = load(room / "support" / "emails.csv")
    hits = emails[emails["reply_body"].fillna("").str.contains(traces, regex=True)]
    print(f"Agent replies with chatbot traces: {len(hits)} of {len(emails)} sampled emails")
    print(hits["email_id"].to_string(index=False), "\n")

    saas = load(room / "it" / "saas-list.csv")
    print("SaaS list, AI features as IT recorded them:")
    print(saas.loc[saas["ai_features"].notna(), ["application", "business_owner", "ai_features", "ai_enabled"]]
          .to_string(index=False))


if __name__ == "__main__":
    main()
