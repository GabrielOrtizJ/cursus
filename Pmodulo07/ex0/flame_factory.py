from .factory import CreatureFactory
from .concrete_creatures import Flameling, Pyrodon


class FlameFactory(CreatureFactory):

    def create_base(self):
        return Flameling("Flameling", "Fire")

    def create_evolved(self):
        return Pyrodon("Pyrodon", "Fire/Flying")
