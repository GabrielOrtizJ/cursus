#!/usr/bin/env python3
def check_temperature(temp_str):
    """ Function to calculate if the temperature is perfect for plants, I test
    here the exception valueError."""
    try:
        temp_int = int(temp_str)
        if temp_int < 0:
            return f"Error: {temp_int}°C is too cold for plants (min 0°C)"
        elif temp_int > 40:
            return f"Error {temp_int}°C is too hot for plants (max 40°C)"
        else:
            return f"Temperature {temp_int}°C is perfect for plants!"
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"


def test_temperature_input():
    """ this is the check to show tests in this program """
    tests = [25, "abc", 100, -50]

    for test in tests:
        print(f"Testing temperature: {test}")
        print(check_temperature(test))


print("\nAll tests completed - program didn't crash!")

test_temperature_input()
