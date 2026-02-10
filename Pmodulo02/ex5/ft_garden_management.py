#!/usr/bin/env python3


class GardenError(Exception):
    """Base error for garden-related problems"""
    pass


class PlantError(GardenError):
    """Error related to plants"""
    pass


class WaterError(GardenError):
    """Error related to watering"""
    pass


class GardenManager:

    def __init__(self):
        self.plants = {}

    def add_plant(self, name, water, sun):
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants[name] = {
            "water": water,
            "sun": sun
        }

    def water_plants(self):
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("Not enough water in tank")

            for plant in self.plants:
                print(f"Watering {plant} - success")

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name):
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' does not exist")

        water = self.plants[name]["water"]
        sun = self.plants[name]["sun"]

        if water < 1:
            raise PlantError(f"Water level {water} is too low (min 1)")
        if water > 10:
            raise PlantError(f"Water level {water} is too high (max 10)")
        if sun < 2:
            raise PlantError(f"Sunlight hours {sun} is too low (min 2)")
        if sun > 12:
            raise PlantError(f"Sunlight hours {sun} is too high (max 12)")

        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management():
    print("=== Garden Management System ===")

    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
        print("Added tomato successfully")

        garden.add_plant("lettuce", 15, 6)
        print("Added lettuce successfully")

        garden.add_plant("", 4, 6)
    except PlantError as error:
        print("Error adding plant:", error)

    print("Watering plants...")
    try:
        garden.water_plants()
    except WaterError as error:
        print("Error watering plants:", error)

    print("Checking plant health...")
    try:
        garden.check_plant_health("tomato")
        garden.check_plant_health("lettuce")
    except PlantError as error:
        print("Error checking lettuce:", error)

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as error:
        print("Caught GardenError:", error)
        print("System recovered and continuing...")

    print("Garden management system test complete!")


test_garden_management()