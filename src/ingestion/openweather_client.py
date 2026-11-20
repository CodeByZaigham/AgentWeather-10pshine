import os
import requests
from rich import print

from datetime import datetime


def get_weather(city: str) -> dict:
    """Fetch current weather using Open-Meteo free API."""

    # Get city coordinates
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    geo_response = requests.get(geo_url, params=geo_params)
    geo_response.raise_for_status()

    locations = geo_response.json().get("results", [])

    if not locations:
        return {"error": f"No location found for {city}"}

    lat = locations[0]["latitude"]
    lon = locations[0]["longitude"]

    # Get current weather
    weather_url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "precipitation,"
            "precipitation_probability,"
            "uv_index,"
            "wind_speed_10m,"
            "wind_direction_10m"
        ),
        "timezone": "auto"
    }

    response = requests.get(weather_url, params=params)
    response.raise_for_status()

    current = response.json()["current"]

    return {
        "city": city,
        "time": current["time"],
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "precipitation": current["precipitation"],
        "precipitation_probability": current["precipitation_probability"],
        "uv_index": current["uv_index"],
        "wind_speed": current["wind_speed_10m"],
        "wind_direction": current["wind_direction_10m"]
    }


print(get_weather("Karachi"))
