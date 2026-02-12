#!/usr/bin/env python3

import sys


def ft_score_analytics() -> None:

    print("=== Player Score Analytics ===")

    scores = []

    try:
        if len(sys.argv) < 2:
            print("No scores provided. Usage: python3 ft_score_analytics.py"
                  "<score1> <score2> ...")
        else:
            i = 1
            # add players
            while i < len(sys.argv):
                scores.append(int(sys.argv[i]))
                i += 1

            print(f"Scores processed: {scores}")
            print(f"Total players {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    ft_score_analytics()
