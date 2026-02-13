#!/usr/bin/env python3

import sys
import math


def calculate_distance(p1: tuple, p2: tuple) -> float:
    """
    Calculate the Euclidean distance between two 3D points.

    This function receives two tuples representing coordinates in 3D space
    (x, y, z). It applies the standard Euclidean distance formula and returns
    the resulting value as a float. It assumes both tuples contain exactly
    three numeric values.
    """
    (x1, y1, z1) = p1
    (x2, y2, z2) = p2
    return float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))


def ft_coordinate_system(x=None, y=None, z=None) -> None:
    """
    Process 3D coordinates from parameters or command-line arguments.

    This function supports two modes of operation:
    - If x, y, and z are provided as parameters, it uses them directly.
    - Otherwise, it attempts to parse coordinates from sys.argv.

    It validates the input format, handles errors gracefully, prints the
    parsed coordinates, and computes the distance from the origin (0, 0, 0).
    The function also demonstrates tuple unpacking when too many arguments
    are provided.
    """
    print("=== Game Coordinate System ===\n")
    errs = "Error details - Type: ValueError, Args: (\""
    start = (0, 0, 0)
    # with parameters

    if x is not None and y is not None and z is not None:
        coords = (x, y, z)
        print(f"Coordinates received as parameters: {coords}")
        distance = calculate_distance(coords, start)
        print(f"Distance between (0, 0, 0) and {coords}: {distance}\n")
        return

    # with arguments

    if len(sys.argv) == 1:
        print("arguments are missing")
        return

    if len(sys.argv) == 2:
        try:
            coords = tuple(int(i) for i in sys.argv[1].split(","))
            print(f"Parsing coordinates: {sys.argv[1]}")
            print(f"Parsed position: {coords}")
            distance = calculate_distance(coords, start)
            print(f"Distance between (0, 0, 0) and {coords}: {distance}\n")
        except ValueError as error:
            print(f"Parsing invalid coordinates: \"{sys.argv[1]}\"")
            print(f"Error parsing coordinates: {error}")
            print(f"{errs}{error}"",)")
        return

    if len(sys.argv) == 4:
        try:
            coords = tuple(int(i) for i in sys.argv[1:4])
            print(f"Position created: {coords}")
            distance = calculate_distance(coords, start)
            print(f"Distance between (0, 0, 0) and {coords}: {distance}\n")
        except ValueError as error:
            print(f"Parsing invalid coordinates: \"{sys.argv[1:4]}\"")
            print(f"Error parsing coordinates: {error}")
            print(f"{errs}{error}"",)")

        return

    if len(sys.argv) == 3:
        print("an argument is missing or superfluous")
        return

    print("Too many arguments")
    coords = (3, 4, 0)
    print("Unpacking demonstration")
    print("Player at x=3, y=4, z=0")
    (x, y, z) = coords
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
