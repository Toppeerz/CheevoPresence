"""macOS menu-bar shell scaffold.

This file will eventually host the menu-bar app and its status item.
It is the future macOS counterpart to the current Windows tray shell.
"""

from desktop.runtime.controller import AppController


class MacOSMenuBarApp:
    """Placeholder for the future native macOS menu-bar app."""

    def __init__(self, controller: AppController):
        self.controller = controller

    def run(self):
        """Start the macOS menu-bar loop when implemented."""
        raise NotImplementedError("The macOS menu-bar shell has not been implemented yet.")
