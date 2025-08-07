from abc import ABC, abstractmethod

class ScreenshotBackend(ABC):
    @abstractmethod
    def capture(self, output_path: str) -> bool:
        pass
