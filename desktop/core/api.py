"""Shared RetroAchievements API helpers and response validation."""

from datetime import datetime

import requests

from desktop.core.constants import RA_API_BASE


def trimmer(text, max_units=128):
    """Trim text to fit within Discord's UTF-16 unit limit."""
    encoded = text.encode("utf-16-le")
    if len(encoded) <= max_units * 2:
        return text

    result = ""
    size = 0
    for ch in text:
        ch_size = len(ch.encode("utf-16-le"))
        if size + ch_size > (max_units - 3) * 2:
            return result + "..."
        result += ch
        size += ch_size
    return result


class APIResponseError(Exception):
    """Raised when RetroAchievements returns an unexpected payload shape."""


def ra_get_user_summary(username, apikey):
    """Fetch the current RetroAchievements session summary for a user."""
    now = datetime.now()
    no_cache = now.strftime("%d%m%Y%H%M%S")
    url = f"{RA_API_BASE}/API_GetUserSummary.php"
    params = {"u": username, "y": apikey, "g": 0, "a": 0, "noCache": no_cache}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        raise APIResponseError
    return data


def ra_get_game(username, apikey, game_id):
    """Fetch static metadata for the currently active RetroAchievements game."""
    url = f"{RA_API_BASE}/API_GetGame.php"
    params = {"z": username, "y": apikey, "i": game_id}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        raise APIResponseError
    return data


def ra_get_user_progress(username, apikey, game_id):
    """Fetch the current user's achievement progress for one game."""
    url = f"{RA_API_BASE}/API_GetUserProgress.php"
    params = {"u": username, "y": apikey, "i": game_id}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        raise APIResponseError
    return data


def format_api_error(exc):
    """Return a user-safe API error message without leaking query params."""
    if isinstance(exc, requests.Timeout):
        return "API error: request timed out"
    if isinstance(exc, requests.ConnectionError):
        return "API error: network unavailable"

    response = getattr(exc, "response", None)
    if response is not None and response.status_code:
        if response.status_code == 401:
            return "Invalid Web API Key"
        return f"API error: HTTP {response.status_code}"

    return "API error: request failed"
