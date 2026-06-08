from __future__ import annotations

from .chat_manager import CalculatorChatManager


def main() -> None:
    manager = CalculatorChatManager()
    print("Homework 2 - Calculator Function Calling. Type 'exit' to quit.")
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
