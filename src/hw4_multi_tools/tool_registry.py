"""Tool registry for homework 4."""

from __future__ import annotations

import json
from typing import Any

from .tools.time_tool import TIME_TOOL_SCHEMA, get_current_time
from .tools.weather_tool import WEATHER_TOOL_SCHEMA, get_weather


class ToolRegistry:
    def __init__(self) -> None:
        self.schemas = [TIME_TOOL_SCHEMA, WEATHER_TOOL_SCHEMA]

    def run(self, tool_name: str, args_json: str) -> str:
        try:
            args = json.loads(args_json) if args_json else {}
        except json.JSONDecodeError:
            return "Error: invalid JSON arguments."

        if tool_name == "get_current_time":
            timezone = str(args.get("timezone", "Asia/Taipei"))
            return get_current_time(timezone)
        if tool_name == "get_weather":
            city = str(args.get("city", "")).strip()
            if not city:
                return "Error: city is required."
            return get_weather(city)
        return f"Unknown tool: {tool_name}"
