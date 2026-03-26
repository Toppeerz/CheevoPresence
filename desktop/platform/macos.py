"""macOS-specific adapter scaffold."""

from desktop.platform.generic import GenericPlatformServices


class MacOSPlatformServices(GenericPlatformServices):
    """Placeholder macOS adapter until native login/keychain hooks are added."""

    startup_toggle_label = "Launch on macOS login"
    settings_menu_default = True
