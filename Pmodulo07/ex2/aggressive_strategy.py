from .strategy import BattleStrategy, InvalidCreatureStrategy
from ex0.creature import Creature
from ex1.transform_capability import TransformCapability


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
