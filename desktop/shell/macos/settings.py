"""macOS settings window scaffold.

This file will eventually host the native macOS settings UI for the shared runtime.
"""

from desktop.runtime.controller import AppController


class MacOSSettingsWindow:
    """Placeholder for the future native macOS settings window."""

    def __init__(self, controller: AppController, on_close=None, on_quit=None):
        self.controller = controller
        self.on_close = on_close
        self.on_quit = on_quit

    def show(self):
        """Open the native macOS settings window when implemented."""
        raise NotImplementedError("The macOS settings window has not been implemented yet.")
