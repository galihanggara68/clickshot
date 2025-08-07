import termios
import tty
import sys
import threading

class InputControl:
    def __init__(self):
        self.running = True
        self.paused = False
        self._thread = threading.Thread(target=self._key_listener, daemon=True)

    def start(self):
        self._thread.start()

    def _key_listener(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            while self.running:
                key = sys.stdin.read(1)
                if key.lower() == 'p':
                    self.paused = not self.paused
                    print("\n⏯️ Paused" if self.paused else "\n▶️ Resumed")
                elif key.lower() == 'q':
                    print("\n🛑 Quitting...")
                    self.running = False
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
