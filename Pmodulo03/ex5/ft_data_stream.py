#!/usr/bin/env python3
"""
This module demonstrates generator functions for streaming data processing.
It includes finite and infinite generators for game events and sequences.
"""


def game_event_stream(n: int):
    """
    Generate simulated game events.
    Args:
        n: Number of events to generate
    Yields:
        Tuples of (event_id, player, level, event_type)
    """
    players = ("alice", "bob", "charlie")
    events = ("killed monster", "found treasure", "leveled up")

    for i in range(1, n + 1):
        player = players[i % 3]
        level = (i % 15) + 1
        event = events[i % 3]
        yield i, player, level, event


def fibonacci_stream():
    """
    Infinite Fibonacci sequence generator.
    """
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream():
    """
    Infinite prime number generator
    """
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num
        num += 1


def ft_data_stream() -> None:
    """
    Process game events using generators and demonstrate streaming analytics.

    Features:
    - Processing 1000 game events with constant memory usage
    - Event filtering and counting
    - Demonstration of finite and infinite generators
    """
    print("=== Game Data Stream Processor ===")

    total_events = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    print("Processing 1000 game events...")

    for event_id, player, level, action in game_event_stream(1000):
        total_events += 1

        if total_events <= 10:
            print(
                f"Event {event_id}: Player {player} "
                f"(level {level}) {action}"
            )

        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasure_events += 1
        if action == "leveled up":
            level_up_events += 1

    print("...")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: Simulated")

    print("\n=== Generator Demonstration ===")

    fib = fibonacci_stream()
    print("Fibonacci sequence (first 10):", end=" ")
    for _ in range(10):
        print(next(fib), end=", ")
    print()

    primes = prime_stream()
    print("Prime numbers (first 5):", end=" ")
    for _ in range(50):
        print(next(primes), end=", ")
    print()


if __name__ == "__main__":
    ft_data_stream()
