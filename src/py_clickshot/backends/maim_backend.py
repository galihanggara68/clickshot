import subprocess
from .screenshot_base import ScreenshotBackend

class MaimScreenshot(ScreenshotBackend):
    def capture(self, output_path: str) -> bool:
        result = subprocess.run(["maim", output_path])
        return result.returncode == 0