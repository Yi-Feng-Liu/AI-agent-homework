"""Vector store wrapper for homework 3."""

from __future__ import annotations

from pathlib import Path

import chromadb

from .embeddings import get_embedding


class ProgrammingLanguageStore:
    def __init__(self, persist_dir: str = "data/chroma") -> None:
        base = Path(persist_dir)
        base.mkdir(parents=True, exist_ok=True)
        self.client = chromadb.PersistentClient(path=str(base))
        self.collection = self.client.get_or_create_collection(name="programming_languages")

    def upsert_documents(self, items: list[dict]) -> None:
        ids = [item["id"] for item in items]
        docs = [f"{item['title']}: {item['content']}" for item in items]
        metas = [{"title": item["title"]} for item in items]
        embeddings = [get_embedding(text) for text in docs]
        self.collection.upsert(ids=ids, documents=docs, metadatas=metas, embeddings=embeddings)

    def search(self, query: str, k: int = 3) -> list[dict]:
        query_embedding = get_embedding(query)
        result = self.collection.query(query_embeddings=[query_embedding], n_results=k)

        matches: list[dict] = []
        ids = result.get("ids", [[]])[0]
        docs = result.get("documents", [[]])[0]
        metas = result.get("metadatas", [[]])[0]
        distances = result.get("distances", [[]])[0]

        for idx, doc, meta, dist in zip(ids, docs, metas, distances):
            matches.append(
                {
                    "id": idx,
                    "title": (meta or {}).get("title", ""),
                    "document": doc,
                    "distance": dist,
                }
            )
        return matches
