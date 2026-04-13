from .factory import CreatureFactory
from .concrete_creatures import Aquabub, Torragon


class AquaFactory(CreatureFactory):

    def create_base(self):
        return Aquabub("Aquabub", "Water")

    def create_evolved(self):
        return Torragon("Torragon", "Water")
