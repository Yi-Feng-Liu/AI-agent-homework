"""Chat manager for homework 1."""

from __future__ import annotations

from typing import List, Dict

from common.config import DEFAULT_MODEL
from common.openai_client import create_client
from .system_prompt import SYSTEM_PROMPT


Message = Dict[str, str]


class RoleChatManager:
    def __init__(self) -> None:
        self.client = create_client()
        self.messages: List[Message] = [{"role": "system", "content": SYSTEM_PROMPT}]

    def ask(self, user_text: str) -> str:
        self.messages.append({"role": "user", "content": user_text})
        resp = self.client.chat.completions.create(model=DEFAULT_MODEL, messages=self.messages)
        answer = resp.choices[0].message.content or ""
        self.messages.append({"role": "assistant", "content": answer})
        return answer
