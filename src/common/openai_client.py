"""OpenAI client factory."""

from __future__ import annotations

from openai import OpenAI

from .config import get_openai_api_key


def create_client() -> OpenAI:
    return OpenAI(api_key=get_openai_api_key())
