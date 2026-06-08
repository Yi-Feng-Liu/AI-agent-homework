"""Chat manager for homework 4 multi-tool function calling."""

from __future__ import annotations

from common.config import DEFAULT_MODEL
from common.openai_client import create_client
from .tool_registry import ToolRegistry

SYSTEM_PROMPT = (
    "你是生活助理。你可以使用 get_current_time 和 get_weather 兩個工具。"
    "當問題涉及時間時呼叫時間工具；涉及天氣時呼叫天氣工具；"
    "如果同一句包含兩種需求，請在同一輪先後呼叫兩個工具，再整合回覆。"
)


class MultiToolChatManager:
    def __init__(self) -> None:
        self.client = create_client()
        self.registry = ToolRegistry()
        self.messages: list[dict] = [{"role": "system", "content": SYSTEM_PROMPT}]

    def ask(self, user_text: str) -> str:
        self.messages.append({"role": "user", "content": user_text})

        while True:
            resp = self.client.chat.completions.create(
                model=DEFAULT_MODEL,
                messages=self.messages,
                tools=self.registry.schemas,
                tool_choice="auto",
            )
            msg = resp.choices[0].message

            if msg.tool_calls:
                self.messages.append(msg.model_dump(exclude_none=True))
                for call in msg.tool_calls:
                    result = self.registry.run(call.function.name, call.function.arguments)
                    self.messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": call.id,
                            "name": call.function.name,
                            "content": result,
                        }
                    )
                continue

            answer = msg.content or ""
            self.messages.append({"role": "assistant", "content": answer})
            return answer
