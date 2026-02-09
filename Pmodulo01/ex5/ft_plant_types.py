#!/usr/bin/env python3

"""Here we use inheritance to create a parent class and other child
classes where plant is the parent and flower, tree, and vegetable are
 children of plant."""


class Plant():
    def __init__(self, name, height, days):
        self.name = name.capitalize()
        self.height = height
        self.days = days

    def info(self, plant_type):
        return f"{self.name} ({plant_type}): {self.height}cm, {self.days} days"


"""flower is a child of plant and has color as an attribute and two
 methods bloom and get_info"""


class Flower(Plant):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        return f"\n{self.info('Flower')}, {self.color} color"


"""tree is a child of plant and has the attribute trunk_diameter and
 two methods produce_shade and get_info"""


class Tree(Plant):
    def __init__(self, name, height, days, trunk_diameter):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.trunk_diameter * 2
        print(f"{self.name} provides {shade} square meters of shade")

    def get_info(self):
        return f"\n{self.info('Tree')}, {self.trunk_diameter}cm diameter"


"""vegetable is a child of plant and has the attributes harvest_season,
nutritional_value and a get_info method"""


class Vegetable(Plant):
    def __init__(self, name, height, days, harvest_season, nutritional_value):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        return (
            f"\n{self.info('Vegetable')}, {self.harvest_season} harvest")


flowers = [
    Flower("Rose", 25, 30, "red"),
    Flower("Orchidaceae", 30, 35, "purple")
]

trees = [
    Tree("oak", 500, 1825, 50),
    Tree("birch", 30, 2500, 60)
]

vegetables = [
    Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
    Vegetable("lettuce", 30, 150, "autumn", "vitamina K")
]

print("=== Garden Plant Types ===")

for flower in flowers:
    print(f"{flower.get_info()}")
    flower.bloom()

for tree in trees:
    print(f"{tree.get_info()}")
    tree.produce_shade()

for vegetable in vegetables:
    print(f"{vegetable.get_info()}")
    print(f"{vegetable.name} is rich in {vegetable.nutritional_value}")
