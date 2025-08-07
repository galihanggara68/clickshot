from abc import ABC, abstractmethod
from typing import Optional

class CursorProvider(ABC):
    @abstractmethod
    def get_position(self) -> Optional[tuple[int, int]]:
        pass
