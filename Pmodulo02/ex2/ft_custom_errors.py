#!/usr/bin/env python3
class GardenError(Exception):
    """Base error for garden-related problems"""
    pass


class PlantError(GardenError):
    """Error related to plants"""
    def __init__(self, msg="The tomato plant is wilting!"):
        super().__init__(msg)


class WaterError(GardenError):
    """Error related to watering"""
    def __init__(self, msg="Not enough water in the tank!"):
        super().__init__(msg)


def check_plant():
    print("Testing PlantError...")
    raise PlantError()


def check_water():
    print("Testing WaterError...")
    raise WaterError()


def raise_plant_error():
    raise PlantError()


def raise_water_error():
    raise WaterError()


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")

    try:
        check_plant()
    except PlantError as error:
        print("Caught PlantError:", error, "\n")

    try:
        check_water()
    except WaterError as error:
        print("Caught WaterError:", error)

    print("\nTesting catching all garden errors...")

    try:
        raise_plant_error()
    except GardenError as error:
        print("Caught a garden error:", error)

    try:
        raise_water_error()
    except GardenError as error:
        print("Caught a garden error:", error, "\n")

    print("All custom error types work correctly!")


test_custom_errors()
