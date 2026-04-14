from abc import ABC, abstractmethod


class TransformCapability(ABC):
    transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
