from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using the chosen operation."""
    if not spells:
        return 0

    ops = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }

    if operation not in ops:
        raise ValueError("Unknown operation")

    func = ops[operation]
    return reduce(func, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Return partial enchantments with power=50 and different elements."""
    fire = partial(base_enchantment, 50, "fire")
    ice = partial(base_enchantment, 50, "ice")
    earth = partial(base_enchantment, 50, "earth")
    return {"fire": fire, "ice": ice, "earth": earth}


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using memoization."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    """Return a singledispatch spell handler."""

    @singledispatch
    def cast(spell) -> str:
        return "Unknown spell type"

    @cast.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @cast.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @cast.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return cast


def main():
    print("=== Ancient Library ===\n")

    print("Testing spell reducer...")
    print("Sum:", spell_reducer([10, 20, 30, 40], "add"))
    print("Product:", spell_reducer([10, 20, 30, 40], "multiply"))
    print("Max:", spell_reducer([10, 20, 30, 40], "max"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["a", "b", "c"]))
    print(dispatcher(3.14))


if __name__ == "__main__":
    main()
