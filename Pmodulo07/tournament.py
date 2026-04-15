from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidCreatureStrategy,
)


def battle(opponents):
    print("\n*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("\n* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")

            try:
                if not strategy1.is_valid(creature1):
                    raise InvalidCreatureStrategy(
                        f"Invalid Creature '{creature1.name}'"
                        f"for this {strategy1.__class__.__name__.lower()}"
                        " strategy"
                    )
                print(strategy1.act(creature1))

                if not strategy2.is_valid(creature2):
                    raise InvalidCreatureStrategy(
                        f"Invalid Creature '{creature2.name}'"
                        f" for this {strategy2.__class__.__name__.lower()}"
                        " strategy"
                    )
                print(strategy2.act(creature2))

            except InvalidCreatureStrategy as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    factories = {
        "Flame": FlameFactory(),
        "Aqua": AquaFactory(),
        "Healing": HealingCreatureFactory(),
        "Transform": TransformCreatureFactory(),
    }

    strategies = {
        "Normal": NormalStrategy(),
        "Aggressive": AggressiveStrategy(),
        "Defensive": DefensiveStrategy(),
    }

    tournaments = [
        (
            "Tournament 0 (basic)",
            [("Flame", "Normal"), ("Healing", "Defensive")],
        ),
        (
            "Tournament 1 (error)",
            [("Flame", "Aggressive"), ("Healing", "Defensive")],
        ),
        (
            "Tournament 2 (multiple)",
            [
                ("Aqua", "Normal"),
                ("Healing", "Defensive"),
                ("Transform", "Aggressive"),
            ],
        ),
    ]

    for name, opps in tournaments:
        print(name)
        opps_list = [f"({f}+{s})" for f, s in opps]
        print(f"[ {', '.join(opps_list)} ]")

        opponents = [(factories[f], strategies[s]) for f, s in opps]
        battle(opponents)
