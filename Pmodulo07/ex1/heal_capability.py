from abc import ABC, abstractmethod
from typing import Any, Optional


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Optional[Any]) -> str:
        pass
