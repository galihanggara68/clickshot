import subprocess
from .screenshot_base import ScreenshotBackend

class GrimScreenshot(ScreenshotBackend):
    def __init__(self, output: str = "*"):
        self.output = output

    def capture(self, output_path: str) -> bool:
        result = subprocess.run(["grim", "-o", self.output, output_path])
        return result.returncode == 0
