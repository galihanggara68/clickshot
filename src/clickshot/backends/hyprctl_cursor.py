# clickshot/backends/hyprctl_cursor.py
import subprocess
from .cursor_base import CursorProvider

class HyprctlCursor(CursorProvider):
    def get_position(self):
        try:
            result = subprocess.run(["hyprctl", "cursorpos"], capture_output=True, text=True)
            x, y = map(int, result.stdout.strip().split(","))
            return x, y
        except Exception:
            return None
