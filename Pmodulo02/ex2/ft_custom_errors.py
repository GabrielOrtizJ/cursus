#!/usr/bin/env python3

"""
Module demonstrating custom exception handling for a garden system.
It defines a hierarchy of garden-related errors and functions that
intentionally trigger them to show how they can be caught and managed.
"""


# Base custom exception for all garden-related issues
class GardenError(Exception):
    """Base error for garden-related problems"""
    pass


# Error specifically related to plant issues
class PlantError(GardenError):
    """Error related to plants"""
    def __init__(self, msg="The tomato plant is wilting!"):
        # Call parent constructor with a default message
        super().__init__(msg)


# Error specifically related to watering issues
class WaterError(GardenError):
    """Error related to watering"""
    def __init__(self, msg="Not enough water in the tank!"):
        # Call parent constructor with a default message
        super().__init__(msg)


# Function that checks plant status and may raise PlantError
def check_plant(status):
    print("Testing PlantError...")

    if status == "bad":
        raise PlantError()
    elif status == "good":
        print("All OK")
    else:
        print("¿?")


# Function that checks water level and may raise WaterError
def check_water(water):
    if water < 0:
        raise WaterError()

    print("All OK")
    print("Testing WaterError...")


# Function that tests all custom errors and demonstrates catching them
def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")

    # Test PlantError handling
    try:
        check_plant("bad")
    except PlantError as error:
        print("Caught PlantError:", error, "\n")

    # Test WaterError handling
    try:
        check_water(-1)
    except WaterError as error:
        print("Caught WaterError:", error)

    print("\nTesting catching all garden errors...")

    # Demonstrate catching any GardenError (PlantError is a subclass)
    try:
        raise PlantError()
    except GardenError as error:
        print("Caught a garden error:", error)

    try:
        raise WaterError()
    except GardenError as error:
        print("Caught a garden error:", error, "\n")

    print("All custom error types work correctly!")


test_custom_errors()
