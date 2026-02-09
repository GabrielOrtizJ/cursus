#!/usr/bin/env python3

# =========================
# Function that raises errors
# =========================

def garden_operations():
    # ValueError
    try:
        print("\nTesting ValueError...")
        print(int("abc"))
    except ValueError as error:
        print(f"Caught ValueError: {error}")

    # ZeroDivisionError
    try:
        print("\nTesting ZeroDivisionError...")
        print(4 / 0)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")

    # FileNotFoundError
    try:
        print("\nTesting FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")

    # KeyError
    try:
        print("\nTesting KeyError...")
        {"rose": "blooming", "oak": "growing"}["missing_plant"]
    except KeyError as error:
        print(f"Caught KeyError: {error}")

    # Multiple Errors
    try:
        print("\nTesting multiple errors together...")
        print(4 / 0)
        open("missing.txt")
    except (ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")


# =========================
# Test Function
# =========================

def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


test_error_types()
