from ex0.creature import Creature
from .heal_capability import HealCapability
from .transform_capability import TransformCapability
from typing import Optional


class Sproutling(Creature, HealCapability):
    def attack(self):
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Optional[str]):
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self):
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: Optional[str]):
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def attack(self):
        if getattr(self, "transformed", False):
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def attack(self):
        if getattr(self, "transformed", False):
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."
