"""One function to call an LLM, whichever provider you use.

    from fieldkit.llm import complete
    reply = complete("Classify this email: ...", system="You are a support triage assistant.")
    print(reply.text, reply.input_tokens, reply.output_tokens)

Pick the provider with environment variables (never put a key in a file):

    FIELDKIT_PROVIDER = anthropic | openai | ollama | mock     (default: anthropic)
    FIELDKIT_MODEL    = the model id                           (default per provider, below)
    ANTHROPIC_API_KEY / OPENAI_API_KEY                         (the provider's own variable)

`mock` needs no key and no network: it returns a fixed answer so you can test a script for free.
Replies are cached on disk (.fieldkit-cache/ next to where you run the script), so re-running an
eval on the same inputs costs nothing. Delete the folder or pass cache=False to call again.
"""
from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path

DEFAULT_MODELS = {
    # Checked 2026-11-02. Change FIELDKIT_MODEL to use another model; see cost.PRICES for prices.
    "anthropic": "claude-opus-5-5",
    "openai": None,  # no default: set FIELDKIT_MODEL to a current model id from the OpenAI docs
    "ollama": "llama3.2",
    "mock": "mock",
}
CACHE_DIR = Path(".fieldkit-cache")


@dataclass
class Reply:
    text: str
    input_tokens: int
    output_tokens: int
    provider: str
    model: str
    seconds: float
    cached: bool = False


def complete(
    prompt: str,
    system: str | None = None,
    *,
    provider: str | None = None,
    model: str | None = None,
    max_tokens: int = 2000,
    cache: bool = True,
) -> Reply:
    """Send one prompt and return the reply text with token counts."""
    provider = (provider or os.environ.get("FIELDKIT_PROVIDER") or "anthropic").lower()
    if provider not in DEFAULT_MODELS:
        raise ValueError(f"Unknown provider {provider!r}; use one of {sorted(DEFAULT_MODELS)}")
    model = model or os.environ.get("FIELDKIT_MODEL") or DEFAULT_MODELS[provider]
    if not model:
        raise ValueError(f"Set FIELDKIT_MODEL to a model id for provider {provider!r}")

    key = hashlib.sha256(json.dumps([provider, model, system, prompt, max_tokens]).encode()).hexdigest()
    path = CACHE_DIR / f"{key}.json"
    if cache and path.exists():
        return Reply(**{**json.loads(path.read_text(encoding="utf-8")), "cached": True})

    start = time.perf_counter()
    text, tokens_in, tokens_out = _CALLERS[provider](prompt, system, model, max_tokens)
    reply = Reply(text, tokens_in, tokens_out, provider, model, round(time.perf_counter() - start, 2))
    if cache:
        CACHE_DIR.mkdir(exist_ok=True)
        path.write_text(json.dumps(asdict(reply), ensure_ascii=False), encoding="utf-8")
    return reply


def _anthropic(prompt, system, model, max_tokens):
    import anthropic  # pip install -r requirements.txt

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY; retries 429/5xx by itself
    kwargs = {"system": system} if system else {}
    # Lab tasks (classify, draft, extract) don't need deep reasoning: low effort keeps them cheap.
    effort = os.environ.get("FIELDKIT_EFFORT", "low")
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
        output_config={"effort": effort},
        **kwargs,
    )
    if resp.stop_reason == "refusal":
        raise RuntimeError(f"The model declined this request: {resp.stop_details}")
    text = "".join(block.text for block in resp.content if block.type == "text")
    return text, resp.usage.input_tokens, resp.usage.output_tokens


def _openai(prompt, system, model, max_tokens):
    import openai  # pip install -r requirements.txt

    client = openai.OpenAI()  # reads OPENAI_API_KEY
    resp = client.responses.create(
        model=model, input=prompt, instructions=system, max_output_tokens=max_tokens
    )
    return resp.output_text, resp.usage.input_tokens, resp.usage.output_tokens


def _ollama(prompt, system, model, max_tokens):
    # A local model through Ollama (https://ollama.com); no key, nothing leaves your machine.
    host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
    body = {"model": model, "prompt": prompt, "system": system or "", "stream": False,
            "options": {"num_predict": max_tokens}}
    req = urllib.request.Request(f"{host}/api/generate", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        data = json.load(r)
    return data["response"], data.get("prompt_eval_count", 0), data.get("eval_count", 0)


def _mock(prompt, system, model, max_tokens):
    # Deterministic stand-in: answers "other" and counts words as tokens.
    return "other", len(((system or "") + prompt).split()), 1


_CALLERS = {"anthropic": _anthropic, "openai": _openai, "ollama": _ollama, "mock": _mock}
