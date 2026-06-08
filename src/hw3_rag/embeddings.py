"""Embedding helpers for homework 3."""

from __future__ import annotations

import os

from common.openai_client import create_client

EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")


def get_embedding(text: str) -> list[float]:
    client = create_client()
    resp = client.embeddings.create(model=EMBEDDING_MODEL, input=text)
    return resp.data[0].embedding
