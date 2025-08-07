import subprocess
import os
from PIL import Image

from py_clickshot.backends.cursor_base import CursorProvider
from py_clickshot.backends.screenshot_base import ScreenshotBackend

def take_annotated_screenshot(screenshot: ScreenshotBackend,  cursor: CursorProvider, filepath, resize_percent=50, offset_x=1920):
    coords = cursor.get_position()
    if not coords: return False
    x, y = coords

    temp_path = filepath + ".raw.png"
    resized_path = filepath + ".resized.png"

    screenshot.capture(temp_path)
    orig_img = Image.open(temp_path)
    orig_width, orig_height = orig_img.size

    subprocess.run(["convert", temp_path, "-resize", f"{resize_percent}%", "-strip", "-define", "png:compression-level=9", resized_path])
    resized_img = Image.open(resized_path)
    resized_width, resized_height = resized_img.size

    scaled_x = int(((x - offset_x) / orig_width) * resized_width)
    scaled_y = int((y / orig_height) * resized_height)

    scaled_x = max(0, min(scaled_x, resized_width-1))
    scaled_y = max(0, min(scaled_y, resized_height-1))

    subprocess.run(["convert", resized_path, "-fill", "none", "-stroke", "red", "-strokewidth", "4", "-draw", f"circle {scaled_x},{scaled_y} {scaled_x+10},{scaled_y}", filepath])
    os.remove(temp_path)
    os.remove(resized_path)
    return True
