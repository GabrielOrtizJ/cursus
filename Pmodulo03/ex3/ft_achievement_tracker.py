#!/usr/bin/env python3

def ft_achievement_tracker() -> None:

    print("=== Achievement Tracker System ===\n")

    players = {'alice': {'first_kill', 'level_10', 'treasure_hunter',
                         'speed_demon'},
               'bob': {'first_kill', 'level_10', 'boss_slayer', 'collector'},
               'charlie': {'level_10', 'treasure_hunter', 'boss_slayer',
                           'speed_demon', 'perfectionist'}}

    alice = players['alice']
    bob = players['bob']
    charlie = players['charlie']

    print(f"Player alice achievements:{alice}")
    print(f"Player bob achievements:{bob}")
    print(f"Player charlie achievements:{charlie}")

    print("\n=== Achievement Analytics ===")
    all_achievements = set()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_all = set.intersection(*players.values())
    print(f"Common to all players: {common_all}")

    shared = set()
    for p1 in players:
        for p2 in players:
            if p1 != p2:
                shared = shared.union(players[p1].intersection(players[p2]))

    rare = all_achievements.difference(shared)
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()
