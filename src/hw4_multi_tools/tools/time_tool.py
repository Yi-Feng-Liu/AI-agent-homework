"""Time tool for homework 4."""

from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

TIME_TOOL_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_current_time",
        "description": "取得目前時間。預設台北時區。",
        "parameters": {
            "type": "object",
            "properties": {
                "timezone": {
                    "type": "string",
                    "description": "IANA 時區名稱，例如 Asia/Taipei。",
                    "default": "Asia/Taipei",
                }
            },
            "additionalProperties": False,
        },
    },
}


def get_current_time(timezone: str = "Asia/Taipei") -> str:
    try:
        now = datetime.now(ZoneInfo(timezone))
    except Exception:
        timezone = "Asia/Taipei"
        now = datetime.now(ZoneInfo(timezone))
    return now.strftime(f"%Y-%m-%d %H:%M:%S ({timezone})")
