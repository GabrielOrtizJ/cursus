#!/usr/bin/env python3

"""
Module that demonstrates how common built‑in Python exceptions work.
Each block intentionally triggers a specific error type so it can be
caught and handled without stopping program execution.
"""


def garden_operations():
    # Test ValueError by trying to convert a non‑numeric string to int
    try:
        print("\nTesting ValueError...")
        print(int("abc"))  # This will fail because "abc" is not a number
    except ValueError as error:
        print(f"Caught ValueError: {error}")

    # Test ZeroDivisionError by dividing by zero
    try:
        print("\nTesting ZeroDivisionError...")
        print(4 / 0)  # Division by zero always raises ZeroDivisionError
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")

    # Test FileNotFoundError by trying to open a missing file
    try:
        print("\nTesting FileNotFoundError...")
        open("missing.txt")  # File does not exist
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")

    # Test KeyError by accessing a non‑existent dictionary key
    try:
        print("\nTesting KeyError...")
        print({"1": "uno", "2": "dos"}["missing_plant"])  # Key not present
    except KeyError as error:
        print(f"Caught KeyError: {error}")

    # Test catching multiple possible errors in one block
    try:
        print("\nTesting multiple errors together...")
        print(4 / 0)          # First error triggered
        open("missing.txt")   # Would also fail, but never reached
    except (ZeroDivisionError, FileNotFoundError, KeyError, ValueError):
        print("Caught an error, but program continues!")


def test_error_types():
    # Entry point for running all error demonstrations
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


test_error_types()
