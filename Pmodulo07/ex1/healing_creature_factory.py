from ..ex0.factory import CreatureFactory
from .concrete_creatures import Sproutling, Bloomelle


class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self):
        return Bloomelle("Bloomelle", "Grass/Fairy")
