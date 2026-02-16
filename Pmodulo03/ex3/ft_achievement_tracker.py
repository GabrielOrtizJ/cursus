#!/usr/bin/env python3

def ft_achievement_tracker() -> None:

    print("=== Achievement Tracker System ===\n")

    players = {
        'alice': ['first_blood', 'pixel_perfect', 'speed_runner',
                  'first_blood', 'first_blood'],
        'bob': ['level_master', 'boss_hunter', 'treasure_seeker',
                'level_master', 'level_master'],
        'charlie': ['treasure_seeker', 'boss_hunter', 'combo_king',
                    'first_blood', 'boss_hunter', 'first_blood',
                    'boss_hunter', 'first_blood'],
        'diana': ['first_blood', 'combo_king', 'level_master',
                  'treasure_seeker', 'speed_runner', 'combo_king',
                  'combo_king', 'level_master'],
        'eve': ['level_master', 'treasure_seeker', 'first_blood',
                'treasure_seeker', 'first_blood', 'treasure_seeker'],
        'frank': ['explorer', 'boss_hunter', 'first_blood', 'explorer',
                  'first_blood', 'boss_hunter']
    }

    alice = players['alice']
    bob = players['bob']
    charlie = players['charlie']

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    # All unique achievements
    all_achievements = set()
    for achievements in players.values():
        all_achievements |= set(achievements)

    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    # Common to all players
    common_all = set.intersection(*(set(a) for a in players.values()))
    print(f"Common to all players: {common_all}")

    # Shared achievements (appear in 2+ players)
    shared = set()
    for p1 in players:
        for p2 in players:
            if p1 != p2:
                shared |= (set(players[p1]) & set(players[p2]))

    # Rare achievements (only 1 player)
    rare = all_achievements - shared
    print(f"Rare achievements (1 player): {rare}\n")

    # Alice vs Bob comparisons
    alice_set = set(alice)
    bob_set = set(bob)

    print(f"Alice vs Bob common: {alice_set & bob_set}")
    print(f"Alice unique: {alice_set - bob_set}")
    print(f"Bob unique: {bob_set - alice_set}")


if __name__ == "__main__":
    ft_achievement_tracker()
