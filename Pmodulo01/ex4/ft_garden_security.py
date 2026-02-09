#!/usr/bin/env python3

"""In this secure plant class, we use an encapsulation method
 which is basically converting attributes to private attributes.
 The advantages of this are that it provides more security and
makes them more difficult to access."""


class SecurePlant():
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.__height = height
        self.__age = age

        print(f"Plant created: {self.name}")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_info(self):
        return (
            f"Current plant: {self.name}"
            f" ({self.get_height()}cm, {self.get_age()} days)")

    def set_height(self, height):
        errheight = "Invalid operation attempted: height"
        if height < 0:
            print(f"\n{errheight} {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age):
        errage = "Invalid operation attempted: age"
        if age < 0:
            print(f"\n{errage} {age} days [REJECTED]")
            print("Security: Negative age rejected \n")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")


print("=== Garden Security System ===")

plant = SecurePlant("rose", 20, 20)
plant.set_height(25)
plant.set_age(30)
plant.set_height(-5)

print(plant.get_info())
