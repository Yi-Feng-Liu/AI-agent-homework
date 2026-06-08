from __future__ import annotations

from .chat_manager import RoleChatManager


def main() -> None:
    manager = RoleChatManager()
    print("Homework 1 - English Vocabulary Tutor. Type 'exit' to quit.")
    while True:
        user_input = input("You> ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Bye.")
            break
        if not user_input:
            continue
        answer = manager.ask(user_input)
        print(f"Tutor> {answer}\n")


if __name__ == "__main__":
    main()
