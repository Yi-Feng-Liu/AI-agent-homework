"""Tool registry for homework 2."""

from __future__ import annotations

import json
from typing import Any, Callable

from .tools.calculator import CALCULATE_TOOL_SCHEMA, execute_calculate_tool

ToolExecutor = Callable[[dict[str, Any]], str]


class ToolRegistry:
    def __init__(self) -> None:
        self._tools = {"calculate": execute_calculate_tool}
        self._schemas = [CALCULATE_TOOL_SCHEMA]

    @property
    def schemas(self) -> list[dict[str, Any]]:
        return self._schemas

    def run(self, tool_name: str, args_json: str) -> str:
        if tool_name not in self._tools:
            return f"Unknown tool: {tool_name}"
        try:
            args = json.loads(args_json) if args_json else {}
        except json.JSONDecodeError:
            return "Error: invalid JSON arguments."
        return self._tools[tool_name](args)
