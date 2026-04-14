from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2.battle_strategy import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidCreatureStrategy,
)


def battle(opponents):
    creatures = []
    for factory, strategy in opponents:
        creature = factory.create_base()
        creatures.append((creature, strategy))

    print("*** Tournament ***")
    print(f"{len(creatures)} opponents involved")

    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            creature1, strategy1 = creatures[i]
            creature2, strategy2 = creatures[j]
            print("* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")
            try:
                act1 = strategy1.act(creature1)
                print(act1)
                act2 = strategy2.act(creature2)
                print(act2)
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
        opps_list = [f'({f}+{s})' for f, s in opps]
        opps_str = ', '.join(opps_list)
        print(f"[ {opps_str} ]")
        opponents = [(factories[f], strategies[s]) for f, s in opps]
        battle(opponents)
        print()  # extra line between tournaments
