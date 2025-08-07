import subprocess
from .screenshot_base import ScreenshotBackend

class ScrotScreenshot(ScreenshotBackend):
    def capture(self, output_path: str) -> bool:
        result = subprocess.run(["scrot", output_path])
        return result.returncode == 0