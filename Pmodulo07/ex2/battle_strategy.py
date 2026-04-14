from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.heal_capability import HealCapability
from ex1.transform_capability import TransformCapability


class InvalidCreatureStrategy(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            msg = (
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
            raise InvalidCreatureStrategy(msg)
        actions = [
            creature.transform(),
            creature.attack(),
            creature.revert(),
        ]
        return "\n".join(actions)


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            msg = (
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
            raise InvalidCreatureStrategy(msg)
        actions = [
            creature.attack(),
            creature.heal(None),
        ]
        return "\n".join(actions)
