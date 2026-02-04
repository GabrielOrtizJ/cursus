#!/usr/bin/env python3

class Plant():
    def __init__(self, name, height, days):
        self.name = name.capitalize()
        self.height = height
        self.days = days

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self):
        return (f"{self.name} ({self.height}cm, {self.days} days)")


plants = [
    Plant("rose", 25, 30),
    Plant("oak", 200, 365),
    Plant("cactus", 5, 90),
    Plant("sunflower", 80, 45),
    Plant("fern", 15, 120)
]

print("=== Plant Factory Output ===")

num = 0
for plant in plants:
    print(f"Created: {plant.get_info()}")
    num += 1

print(f"\nTotal plants created: {num}")
