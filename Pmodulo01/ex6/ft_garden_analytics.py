#!/usr/bin/env python3

"""Here we also use inheritance with polymorphism;
 plant is the parent class that its children and the
 methods get info, grow and register"""


class Plant:
    def __init__(self, name, height):
        self.name = name.capitalize()
        self.height = height

    def grow(self):
        self.height += 1

    def get_info(self):
        return f"- {self.name}: {self.height}cm"

    def register(self, stats):
        stats.regular += 1


"""floweringplant is a child of plant and has the attributes color and the
 methods get info and register"""


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        return f"{super().get_info()}, {self.color} flowers (blooming)"

    def register(self, stats):
        stats.flowering += 1


"""PrizeFlower is a child of FloweringPlant and has the attributes
 prize_points and the methods get info and register."""


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self):
        return f"{super().get_info()}, Prize points: {self.prize_points}"

    def register(self, stats):
        stats.prize += 1
        stats.points += self.prize_points


"""GardenManage is the garden manager; it has methods such as add_plant,
grow_all, report, validate height, create_garden_network, and resume_scores,
 and attributes such as gardens and total_gardens."""


class GardenManager:
    gardens = {}
    total_gardens = 0

    """This is our auxiliary tool, GardenStats. It will help us collect
      statistics from all gardens and has a report method.
    """

    class GardenStats:
        def __init__(self):
            self.total_growth = 0
            self.regular = 0
            self.flowering = 0
            self.prize = 0
            self.points = 0

        def report(self):
            print(
                f"\nPlants added: {self.regular + self.flowering + self.prize}"
                f", Total growth: {self.total_growth}cm")
            print(
                f"Plant types: {self.regular} regular, {self.flowering} "
                f"flowering, {self.prize} prize flowers")

    def __init__(self, name):
        self.name = name.capitalize()
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.gardens[self.name] = self
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        plant.register(self.stats)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self):
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.total_growth += 1
            print(f"{plant.name} grew 1cm")

    def report(self):
        print(f"\n=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())
        self.stats.report()

    @staticmethod
    def validate_height(height):
        if height > 0:
            print("\nHeight validation test: True")
        else:
            print("\nHeight validation test: False")

    @classmethod
    def create_garden_network(cls):
        return list(cls.gardens.keys())

    @classmethod
    def resume_scores(cls):
        print("Garden scores -", end=" ")
        for garden in cls.gardens.values():
            print(f"{garden.name}: {garden.stats.points}", end="  ")
        print(f"\nTotal gardens managed: {cls.total_gardens}")


print("=== Garden Management System Demo ===\n")

alice = GardenManager("Alice")
bob = GardenManager("bob")

alice.add_plant(Plant("Oak Tree", 100))
alice.add_plant(FloweringPlant("Rose", 25, "red"))
alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

alice.grow_all()
alice.report()

alice.stats.points += 208
bob.stats.points += 92

GardenManager.validate_height(10)

GardenManager.resume_scores()
