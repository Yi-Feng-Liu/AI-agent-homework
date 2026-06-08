from __future__ import annotations

from .chat_manager import MultiToolChatManager


def main() -> None:
    manager = MultiToolChatManager()
    print("Homework 4 - Time and Weather Tools. Type 'exit' to quit.")
    while True:
        user_input = input("You> ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Bye.")
            break
        if not user_input:
            continue
        answer = manager.ask(user_input)
        print(f"Assistant> {answer}\n")


if __name__ == "__main__":
    main()
