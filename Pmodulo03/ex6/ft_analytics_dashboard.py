#!/usr/bin/env python3
"""
Demonstrates mastery of Python comprehensions.
"""


def ft_analytics_dashboard() -> None:
    """
    Demonstrates list, dictionary, and set comprehensions using
    simple analytics from sample game data.
    """
    print("=== Game Analytics Dashboard ===")

    info = {
        "players": {
            "alice": {
                "level": 41,
                "total_score": 2824,
                "sessions_played": 13,
                "favorite_mode": "ranked",
                "achievements_count": 5,
            },
            "bob": {
                "level": 16,
                "total_score": 4657,
                "sessions_played": 27,
                "favorite_mode": "ranked",
                "achievements_count": 2,
            },
            "charlie": {
                "level": 44,
                "total_score": 9935,
                "sessions_played": 21,
                "favorite_mode": "ranked",
                "achievements_count": 7,
            },
            "diana": {
                "level": 3,
                "total_score": 1488,
                "sessions_played": 21,
                "favorite_mode": "casual",
                "achievements_count": 4,
            },
            "eve": {
                "level": 33,
                "total_score": 1434,
                "sessions_played": 81,
                "favorite_mode": "casual",
                "achievements_count": 7,
            },
            "frank": {
                "level": 15,
                "total_score": 8359,
                "sessions_played": 85,
                "favorite_mode": "competitive",
                "achievements_count": 1,
            },
        },
        "sessions": [
            {"player": "bob", "duration_minutes": 94, "score": 1831,
             "mode": "competitive", "completed": False},
            {"player": "bob", "duration_minutes": 32, "score": 1478,
             "mode": "casual", "completed": True},
            {"player": "diana", "duration_minutes": 17, "score": 1570,
             "mode": "competitive", "completed": False},
            {"player": "alice", "duration_minutes": 98, "score": 1981,
             "mode": "ranked", "completed": True},
            {"player": "diana", "duration_minutes": 15, "score": 2361,
             "mode": "competitive", "completed": False},
            {"player": "eve", "duration_minutes": 29, "score": 2985,
             "mode": "casual", "completed": True},
            {"player": "frank", "duration_minutes": 34, "score": 1285,
             "mode": "casual", "completed": True},
            {"player": "alice", "duration_minutes": 53, "score": 1238,
             "mode": "competitive", "completed": False},
            {"player": "bob", "duration_minutes": 52, "score": 1555,
             "mode": "casual", "completed": False},
            {"player": "frank", "duration_minutes": 92, "score": 2754,
             "mode": "casual", "completed": True},
            {"player": "eve", "duration_minutes": 98, "score": 1102,
             "mode": "casual", "completed": False},
            {"player": "diana", "duration_minutes": 39, "score": 2721,
             "mode": "ranked", "completed": True},
            {"player": "frank", "duration_minutes": 46, "score": 329,
             "mode": "casual", "completed": True},
            {"player": "charlie", "duration_minutes": 56, "score": 1196,
             "mode": "casual", "completed": True},
            {"player": "eve", "duration_minutes": 117, "score": 1388,
             "mode": "casual", "completed": False},
            {"player": "diana", "duration_minutes": 118, "score": 2733,
             "mode": "competitive", "completed": True},
            {"player": "charlie", "duration_minutes": 22, "score": 1110,
             "mode": "ranked", "completed": False},
            {"player": "frank", "duration_minutes": 79, "score": 1854,
             "mode": "ranked", "completed": False},
            {"player": "charlie", "duration_minutes": 33, "score": 666,
             "mode": "ranked", "completed": False},
            {"player": "alice", "duration_minutes": 101, "score": 292,
             "mode": "casual", "completed": True},
            {"player": "frank", "duration_minutes": 25, "score": 2887,
             "mode": "competitive", "completed": True},
            {"player": "diana", "duration_minutes": 53, "score": 2540,
             "mode": "competitive", "completed": False},
            {"player": "eve", "duration_minutes": 115, "score": 147,
             "mode": "ranked", "completed": True},
            {"player": "frank", "duration_minutes": 118, "score": 2299,
             "mode": "competitive", "completed": False},
            {"player": "alice", "duration_minutes": 42, "score": 1880,
             "mode": "casual", "completed": False},
            {"player": "alice", "duration_minutes": 97, "score": 1178,
             "mode": "ranked", "completed": True},
            {"player": "eve", "duration_minutes": 18, "score": 2661,
             "mode": "competitive", "completed": True},
            {"player": "bob", "duration_minutes": 52, "score": 761,
             "mode": "ranked", "completed": True},
            {"player": "eve", "duration_minutes": 46, "score": 2101,
             "mode": "casual", "completed": True},
            {"player": "charlie", "duration_minutes": 117, "score": 1359,
             "mode": "casual", "completed": True},
        ],
        "game_modes": ["casual", "competitive", "ranked"],
        "achievements": [
            "first_blood", "level_master", "speed_runner", "treasure_seeker",
            "boss_hunter", "pixel_perfect", "combo_king", "explorer",
        ],
    }

    players = info["players"]

    print("\n=== List Comprehension Examples ===")

    high_scores = [
        name for name, data in players.items()
        if data["total_score"] > 2000
    ]
    print(f"High scorers (>2000): {high_scores}")

    doubled = [data["total_score"] * 2 for data in players.values()]
    print(f"Scores doubled: {doubled}")

    active_players = [
        name for name, data in players.items()
        if data["sessions_played"] > 20
    ]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {
        name: data["total_score"] for name, data in players.items()
    }
    print(f"Player scores: {player_scores}")

    score_categories = {
        name: (
            "high" if data["total_score"] > 5000
            else "medium" if data["total_score"] > 2000
            else "low"
        )
        for name, data in players.items()
    }

    category_counts = {
        cat: sum(1 for c in score_categories.values() if c == cat)
        for cat in {"high", "medium", "low"}
    }

    print(f"Score categories: {category_counts}")

    achievement_map = {
        name: data["achievements_count"]
        for name, data in players.items()
    }
    print(f"Achievement counts: {achievement_map}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {s["player"] for s in info["sessions"]}
    print(f"Unique players: {sorted(unique_players)}")

    unique_modes = {s["mode"] for s in info["sessions"]}
    print(f"Active modes: {unique_modes}")

    unique_achievements = {a for a in info["achievements"]}

    print(f"Unique achievements: {set(sorted(unique_achievements)[:3])}")

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    total_achievements = len(unique_achievements)
    avg_score = sum(player_scores.values()) / total_players

    top_player = max(players, key=lambda p: players[p]["total_score"])
    top_score = players[top_player]["total_score"]
    top_ach = players[top_player]["achievements_count"]

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_achievements}")
    print(f"Average score: {avg_score}")
    print(
        f"Top performer: {top_player} "
        f"({top_score} points, {top_ach} achievements)"
    )


if __name__ == "__main__":
    ft_analytics_dashboard()
