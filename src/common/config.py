"""Shared configuration helpers."""

from __future__ import annotations

import os
from dotenv import load_dotenv

load_dotenv()


DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def get_openai_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set. Please provide it in env or .env file.")
    return api_key
