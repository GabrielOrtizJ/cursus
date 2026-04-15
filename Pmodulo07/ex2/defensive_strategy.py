from .strategy import BattleStrategy, InvalidCreatureStrategy
from ex0.creature import Creature
from ex1.heal_capability import HealCapability


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
