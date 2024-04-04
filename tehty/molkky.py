"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

class Player:

    def __init__(self, player):

        self.__player = player
        self.__turns_n = 0
        self.__points = 0
        self.__hits = 0
        self.__value = 0
        self.__cheers = True

    def get_name(self):
        return self.__player

    def get_points(self):
        return self.__points

    def add_points(self, amount):
        self.__points += amount
        self.__turns_n += 1
        self.__value = amount

        if self.__points > 50:
            print(self.__player, "gets penalty points!")
            self.__points = 25
            self.__cheers = False


        elif self.__points >= 40 and self.__points <= 49:
            print(f"{self.__player} needs only {50 - self.__points} points. "
                  f"It's better to avoid knocking down the pins with "
                  f"higher points.")

    def cheers(self, pts):
        average = self.__points / self.__turns_n

        if pts > average and self.__cheers == True:
            print(f"Cheers {self.__player}!")

        self.__cheers = True

    def has_won(self):
        if self.__points == 50:
            return True

    def hit_percentage(self):
        if self.__value > 0:
            self.__hits += 1

        try:
            hit_p = (self.__hits / self.__turns_n) * 100

        except ZeroDivisionError:
            hit_p = 0.0

        self.__value = 0

        return hit_p

# TODO:
# a) Implement the class Player here.


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)
        in_turn.cheers(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p,",
              f"hit percentage {player1.hit_percentage():.1f}")
        print(player2.get_name() + ":", player2.get_points(), "p,",
              f"hit percentage {player2.hit_percentage():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
