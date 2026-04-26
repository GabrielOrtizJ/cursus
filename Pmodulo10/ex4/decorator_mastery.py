from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    """Decorator that prints execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that validates power."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int, *args, **kwargs):
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Retry decorator for spells that may fail."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying..."
                          f" (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    print("=== Master’s Tower ===\n")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    print("Testing spell timer...")
    print("Result:", fireball(), "\n")

    print("Testing retrying spell...")

    @retry_spell(3)
    def unstable_spell():
        raise ValueError("Explosion")

    print(unstable_spell(), "\n")

    print("Testing MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Aria"))
    print(guild.validate_mage_name("X"))
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Lightning"))


if __name__ == "__main__":
    main()
