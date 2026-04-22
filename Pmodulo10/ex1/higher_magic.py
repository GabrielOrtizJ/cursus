from typing import Callable


def spell(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return spell1


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return base_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return condition


def spell_sequence(spells: list[Callable]) -> Callable:
    return spells


def main():
    print("main no hay nada aun")

    # test_values = [20, 18, 8]
    # test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


if __name__ == "__main__":
    main()
