from collections.abc import Callable, callable
from typing import List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a new spell that casts spell1 and spell2 with the same arguments."""
    def combined(target: str, power: int) -> tuple[str, str]:
        if callable(spell1) and callable(spell2):
            return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a new spell where the power is multiplied before casting."""
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a spell that only casts if condition(target, power) is True."""
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: List[Callable]) -> Callable:
    """Return a spell that casts all spells in order and returns a list of results."""
    def sequence(target: str, power: int) -> List[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {power} HP to {target}"


def freeze(target: str, power: int) -> str:
    return f"{target} is frozen with {power} ice power"


def main():
    print("=== Higher Realm (auto-generated tests) ===\n")

    test_values = [20, 18, 8]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    spells = [fireball, heal, freeze]

    # 1. spell_combiner
    print("Testing spell_combiner...\n")
    combined = spell_combiner(fireball, heal)

    for target in test_targets:
        for value in test_values:
            print(f"{target} / {value} → {combined(target, value)}")
    print()

    # 2. power_amplifier
    print("Testing power_amplifier...\n")
    mega_fireball = power_amplifier(fireball, 3)

    for target in test_targets:
        for value in test_values:
            print(f"{target} / {value} → {mega_fireball(target, value)}")
    print()

    # 3. conditional_caster
    print("Testing conditional_caster...\n")

    def condition(t, p):
        return p >= 15

    conditional_spell = conditional_caster(condition, freeze)

    for target in test_targets:
        for value in test_values:
            print(f"{target} / {value} → {conditional_spell(target, value)}")
    print()

    # 4. spell_sequence
    print("Testing spell_sequence...\n")
    sequence = spell_sequence(spells)

    for target in test_targets:
        for value in test_values:
            print(f"{target} / {value} → {sequence(target, value)}")


if __name__ == "__main__":
    main()
