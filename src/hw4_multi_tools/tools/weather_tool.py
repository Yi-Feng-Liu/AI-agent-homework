"""Weather tool for homework 4 using Open-Meteo (no API key)."""

from __future__ import annotations

from typing import Any

import requests

WEATHER_TOOL_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "查詢城市目前天氣。",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "城市名稱，例如 Taipei。",
                }
            },
            "required": ["city"],
            "additionalProperties": False,
        },
    },
}


def _get_coordinates(city: str) -> tuple[float, float, str] | None:
    url = "https://geocoding-api.open-meteo.com/v1/search"
    resp = requests.get(url, params={"name": city, "count": 1, "language": "en", "format": "json"}, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    results = data.get("results") or []
    if not results:
        return None
    row = results[0]
    return float(row["latitude"]), float(row["longitude"]), row.get("name", city)


def get_weather(city: str) -> str:
    try:
        geo = _get_coordinates(city)
        if not geo:
            return f"Cannot find city: {city}"
        lat, lon, resolved_name = geo

        url = "https://api.open-meteo.com/v1/forecast"
        params: dict[str, Any] = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,apparent_temperature,weather_code,wind_speed_10m",
            "timezone": "auto",
        }
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        current = resp.json().get("current", {})

        temp = current.get("temperature_2m")
        feels = current.get("apparent_temperature")
        wind = current.get("wind_speed_10m")
        code = current.get("weather_code")
        return (
            f"{resolved_name} weather now: temperature {temp}°C, feels like {feels}°C, "
            f"wind {wind} km/h, weather_code {code}."
        )
    except Exception as exc:
        return f"Weather lookup failed: {exc}"
