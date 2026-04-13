from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, tipe: str):
        self.name = name
        self.tipe = tipe

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.tipe} type Creature"
