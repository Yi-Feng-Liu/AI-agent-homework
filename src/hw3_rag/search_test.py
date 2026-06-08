from __future__ import annotations

from .kb_seed import LANGUAGE_KB
from .vector_store import ProgrammingLanguageStore

TEST_QUERIES = [
    "Which language is common for front-end web development?",
    "I want a language for data science and machine learning.",
    "Which language focuses on memory safety and performance?",
]


def main() -> None:
    store = ProgrammingLanguageStore()
    store.upsert_documents(LANGUAGE_KB)

    for i, query in enumerate(TEST_QUERIES, 1):
        print(f"\nQuery {i}: {query}")
        results = store.search(query, k=3)
        for rank, item in enumerate(results, 1):
            print(
                f"  {rank}. {item['title']} | id={item['id']} | distance={item['distance']:.4f}\n"
                f"     {item['document']}"
            )


if __name__ == "__main__":
    main()
