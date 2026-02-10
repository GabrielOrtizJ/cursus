#!/usr/bin/env python3

"""
Module that demonstrates exception handling with a simple plant‑watering
system.It shows how try/except/finally works when iterating through a list
 of plants,including how cleanup code always runs even if an error occurs.
"""


def water_plants(plant_list):
    # Attempt to water each plant in the list
    try:
        print("Opening watering system")

        # Loop through all plants
        for plant in plant_list:
            # If a plant is None, this simulates an invalid entry
            if plant is None:
                raise TypeError(plant)

            print(f"Watering {plant}")

    # Handle the case where a None value is found
    except TypeError:
        print("Error: Cannot water None - invalid plant!")

    # Code inside finally always runs, even if an error occurred
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    # First test: everything works normally
    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    # Second test: includes an invalid plant (None)
    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])

    print("\nCleanup always happens, even with errors!")


test_watering_system()
