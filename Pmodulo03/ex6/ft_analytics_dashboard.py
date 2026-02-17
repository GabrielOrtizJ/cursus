#!/usr/bin/env python3
"""
Demonstrates mastery of Python comprehensions.
"""


def ft_analytics_dashboard() -> None:
    """
    Demonstrates list, dictionary, and set comprehensions
    in a way that matches the expected output.
    """
    print("=== Game Analytics Dashboard ===")

    players = ["alice", "bob", "charlie", "diana"]
    scores = [2300, 1800, 2150, 2050]
    achievements = {
        "alice": [
            "first_kill", "level_10", "boss_slayer",
            "speed_demon", "treasure_hunter"
            ],
        "bob": [
            "first_kill", "level_5", "collector"
            ],
        "charlie": [
            "level_10", "treasure_hunter", "boss_slayer",
            "speed_demon", "perfectionist", "first_kill", "collector"
        ],
        "diana": [
            "level_5", "treasure_hunter", "boss_slayer"
            ]
    }
    regions = ["north", "east", "central", "north"]

    print("\n=== List Comprehension Examples ===")

    high_scorers = [
        players[i] for i in range(len(players)) if scores[i] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [score * 2 for score in scores]
    print(f"Scores doubled: {doubled_scores}")

    active_players = [
        player for i, player in enumerate(players) if scores[i] > 0]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {players[i]: scores[i] for i in range(len(players))}
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high": sum(1 for score in scores if score > 2000),
        "medium": sum(1 for score in scores if 2000 >= score > 1800),
        "low": sum(1 for score in scores if score <= 1800)
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {
        player: len(achievements[player]) for player in players}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {player for player in players}
    print(f"Unique players: {unique_players}")

    unique_achievements = {
        ach for ach_list in achievements.values() for ach in ach_list}
    print(f"Unique achievements: {unique_achievements}")

    unique_regions = {region for region in regions}
    print(f"Active regions: {unique_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(scores) / total_players
    top_performer = max(player_scores, key=player_scores.get)
    top_score = player_scores[top_performer]
    top_achievements = achievement_counts[top_performer]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(f"Top performer: {top_performer} ({top_score} points,"
          f" {top_achievements} achievements)")


if __name__ == "__main__":
    ft_analytics_dashboard()