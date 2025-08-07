from abc import ABC, abstractmethod

class CursorProvider(ABC):
    @abstractmethod
    def get_position(self) -> tuple[int, int] | None:
        pass
