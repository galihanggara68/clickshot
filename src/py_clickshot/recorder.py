import os
import time
import datetime
import select
import evdev
from evdev import InputDevice, categorize, ecodes
from py_clickshot.input_listener import InputControl
from py_clickshot.screenshot import take_annotated_screenshot
from py_clickshot.html_writer import init_html, append_html, finalize_html

def start_recording(output_dir, screenshot, cursor):
    output_dir = os.path.expanduser(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    html_path = os.path.join(output_dir, "index.html")
    init_html(html_path)

    devices = [InputDevice(path) for path in evdev.list_devices()]
    pointers = [d for d in devices if any(k in d.name.lower() for k in ["mouse", "touchpad", "pointer"])]
    if not pointers:
        print("No pointer or touchpad found.")
        return

    print("Monitoring devices:")
    for d in pointers:
        print(f" - {d.path} ({d.name})")

    control = InputControl()
    control.start()

    counter = 0
    touch_down_time = None
    TOUCH_CODE = ecodes.BTN_TOUCH
    TOUCH_CLICK_THRESHOLD = 0.15

    try:
        while control.running:
            if control.paused:
                time.sleep(0.1)
                continue

            r, _, _ = select.select(pointers, [], [], 0.1)
            for device in r:
                for event in device.read():
                    if event.type == ecodes.EV_KEY:
                        key_event = categorize(event)
                        now = time.time()

                        if key_event.scancode == TOUCH_CODE:
                            if key_event.keystate == key_event.key_down:
                                touch_down_time = now
                            elif key_event.keystate == key_event.key_up and touch_down_time:
                                if now - touch_down_time <= TOUCH_CLICK_THRESHOLD:
                                    _capture(screenshot,  cursor, output_dir, counter, html_path)
                                    counter += 1
                                touch_down_time = None

                        elif key_event.scancode == ecodes.BTN_LEFT and key_event.keystate == key_event.key_down:
                            _capture(screenshot,  cursor, output_dir, counter, html_path)
                            counter += 1

    except KeyboardInterrupt:
        print("\n⛔ Exiting...")
    finally:
        finalize_html(html_path)


def _capture(screenshot,  cursor, save_dir, step, html_path):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}_{step}.png"
    filepath = os.path.join(save_dir, filename)
    if take_annotated_screenshot(screenshot,  cursor, filepath):
        append_html(html_path, filename, step, timestamp)
        print(f"✅ Step {step} captured at {timestamp}")
