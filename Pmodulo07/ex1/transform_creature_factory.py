from ..ex0.factory import CreatureFactory
from .concrete_creatures import Shiftling, Morphagon


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self):
        return Morphagon("Morphagon", "Normal/Dragon")
