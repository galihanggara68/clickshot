import subprocess
from .cursor_base import CursorProvider

class XdotoolCursor(CursorProvider):
    def get_position(self):
        try:
            result = subprocess.run(["xdotool", "getmouselocation"], capture_output=True, text=True)
            parts = dict(part.split(":") for part in result.stdout.strip().split())
            return int(parts["x"]), int(parts["y"])
        except:
            return None