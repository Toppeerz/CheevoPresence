"""Generic desktop platform adapter used as a non-Windows fallback."""

import base64

from desktop.platform.base import PlatformServices


class GenericPlatformServices(PlatformServices):
    """Provide simple cross-platform defaults until native adapters exist."""

    startup_toggle_label = "Launch on system startup"
    settings_menu_default = False

    def protect_api_key(self, value):
        """Encode the API key so plaintext is not written directly."""
        if not value:
            return ""
        return base64.b64encode(value.encode("utf-8")).decode("ascii")

    def unprotect_api_key(self, value):
        """Decode a previously encoded API key."""
        if not isinstance(value, str) or not value:
            return ""
        try:
            return base64.b64decode(value).decode("utf-8")
        except (ValueError, TypeError, UnicodeDecodeError):
            return ""

    def supports_self_update(self):
        """Report that the generic fallback does not support self-updating yet."""
        return False
