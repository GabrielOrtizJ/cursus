from abc import ABC, abstractmethod


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass
