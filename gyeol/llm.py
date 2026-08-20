"""xAI Grok client with structured JSON output."""
from __future__ import annotations
import json
import os
from typing import Any
from openai import OpenAI

def get_client() -> OpenAI:
    api_key = os.getenv("XAI_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("XAI_API_KEY 또는 OPENAI_API_KEY 환경변수가 필요합니다.")
    base_url = os.getenv("XAI_BASE_URL", "https://api.x.ai/v1")
    return OpenAI(api_key=api_key, base_url=base_url)

def chat_json(system: str, user: str, model: str = "grok-3") -> dict[str, Any]:
    client = get_client()
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=0.7,
        response_format={"type": "json_object"},
    )
    content = resp.choices[0].message.content or "{}"
    return json.loads(content)

def chat_text(system: str, user: str, model: str = "grok-3") -> str:
    client = get_client()
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=0.8,
    )
    return resp.choices[0].message.content or ""
