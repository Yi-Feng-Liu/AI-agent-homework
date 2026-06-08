from __future__ import annotations

from .kb_seed import LANGUAGE_KB
from .vector_store import ProgrammingLanguageStore


def main() -> None:
    store = ProgrammingLanguageStore()
    store.upsert_documents(LANGUAGE_KB)
    print(f"Seeded {len(LANGUAGE_KB)} programming language documents.")


if __name__ == "__main__":
    main()
