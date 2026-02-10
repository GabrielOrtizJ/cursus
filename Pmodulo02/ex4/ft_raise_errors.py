#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Checks if a plant is healthy and has correct info.
    Raises ValueError if any value is invalid.
    Returns success msg if everything is correct
    """
    max = "is too high (max 12)"
    # Checks plant name
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    # Checks water level
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    # Checks sunlight hours
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} {max}")

    # If all checks pass
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    # Test with all valid values
    print("\nTesting good values...")
    try:
        print(check_plant_health("tomato", 6, 9))
    except ValueError as error:
        print("Error:", error)

    # Test empty plant name
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 6, 9)
    except ValueError as error:
        print("Error:", error)

    # Test invalid water level
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 9)
    except ValueError as error:
        print("Error:", error)

    # Test invalid sunlight hours
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 6, 0)
    except ValueError as error:
        print("Error:", error)

    print("\nAll error raising tests completed!")


test_plant_checks()
