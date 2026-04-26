from collections.abc import Callable


def mage_counter() -> Callable:
    """Return a counter function that remembers how many
    times it was called."""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Return a function that accumulates power over time."""
    total = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    """Return a function that applies an enchantment to an item."""
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    """Return a dict with store() and recall() closures."""
    storage: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        storage[key] = value

    def recall(key: str) -> object:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main():
    print("=== Memory Depths ===\n")

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(counter_a())  # 1
    print(counter_a())  # 2
    print(counter_b())  # 1

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(acc(20))  # 120
    print(acc(30))  # 150

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print(vault["recall"]("secret"))
    print(vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
