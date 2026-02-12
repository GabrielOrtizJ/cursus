#!/usr/bin/env python3

import sys
import math
"""
This module processes 3D coordinates from command-line arguments,
calculates distances between points, and demonstrates tuple operations.
"""


def calculate_distance(p1: tuple, p2: tuple) -> float:
    """
    Calculate Euclidean distance between two 3D points.

    Args:
    p1: First point as (x, y, z)
    p2: Second point as (x, y, z)

    Returns:
    Distance between p1 and p2 as float
    """
    (x1, y1, z1) = p1
    (x2, y2, z2) = p2
    return float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))


def ft_coordinate_system():
    """
    Process 3D coordinates from command-line arguments.

    Handles different input formats:
    - Single string "x,y,z"
    - Three separate arguments x y z
    - Error cases and edge conditions
    """
    print("=== Game Coordinate System ===\n")
    error = "invalid literal for int() with base 10"
    origin = (0, 0, 0)
    if len(sys.argv) == 1:
        print("Empty coordinates")
    elif len(sys.argv) == 2:
        try:
            coords = tuple(int(i) for i in sys.argv[1].split(","))
            print(f"Parsing coordinates: {sys.argv[1]}")
            print(f"Parsed position: {coords}")
            distance = calculate_distance(coords, origin)
            print(f"Distance between (0, 0, 0) and {coords}: {distance}\n")
        except ValueError:
            print(f"Error parsing coordinates: {error}")
            print(f"Error details - Type: ValueError, Args: {error}")
            return
    elif len(sys.argv) == 3:
        print("Oopsie you're missing a dimension")
        return
    elif len(sys.argv) == 4:
        try:
            coords = tuple(int(i) for i in sys.argv[1:4])
            print(f"Position created: {coords}")
            distance = calculate_distance(coords, origin)
            print(f"Distance between (0, 0, 0) and {coords}: {distance}\n")
        except ValueError:
            print(f"Error parsing coordinates: {error}")
            print(f"Error details - Type: ValueError, Args: {error}")
            return
    else:
        print("Too many arguments")
        coords = (3, 4, 0)
        print("Unpacking demonstration:")
        print("Player at x=3, y=4, z=0")
        (X, Y, Z) = coords
        print(f"Coordinates: X={X}, Y={Y}, Z={Z}")


if __name__ == "__main__":
    ft_coordinate_system()
