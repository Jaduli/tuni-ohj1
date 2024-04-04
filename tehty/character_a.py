"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""

class Character:

    def __init__(self, name):

        self.__name = name
        self.__backpack = {}


    def give_item(self, item):

        if item not in self.__backpack.keys():
            self.__backpack[item] = 0

        self.__backpack[item] += 1


    def remove_item(self, item):

        if item in self.__backpack.keys():
            self.__backpack[item] -= 1

            if self.__backpack[item] == 0:
                del self.__backpack[item]


    def get_name(self):
        return self.__name


    def has_item(self, item):

        if item in self.__backpack.keys():
            return True

        else:
            return False


    def how_many(self, item):

        if item in self.__backpack.keys():
            return self.__backpack[item]

        else:
            return 0


    def printout(self):

        print("Name:", self.__name)

        sorted_dict = {}

        for key in sorted(self.__backpack.keys()):
            sorted_dict[key] = self.__backpack[key]

        if len(sorted_dict) > 0:
            for item, amount in sorted_dict.items():
                print(" ", amount, item)

        else:
            print("  --nothing--")


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
