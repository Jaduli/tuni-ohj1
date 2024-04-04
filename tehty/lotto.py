"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""


def input_check(nall, ndrawn):
    """
    Tarkistaa, ovatko annetut arvot valideja.

    :return: Totuusarvo True, jos arvot ovat funktioon sopivia
    """

    if nall > 0 and ndrawn > 0 and nall - ndrawn >= 0:
        return True

    elif nall <= 0 or ndrawn <= 0:
        print("The number of balls must be a positive number.")
        return False

    elif nall - ndrawn < 0:
        print("At most the total number of balls can be drawn.")
        return False


def probability(nall, ndrawn):
    """
    Laskee todennäköisyyden saada jokainen lotossa arvottu numeropallo oikein.

    :param nall: Kaikkien arvottavien pallojen määrä
    :param ndrawn: Arvonnassa nostettujen pallojen määrä
    :return: Mahdollisuus saada kaikki numerot oikein
    """

    factorial1 = 1
    factorial2 = 1
    factorial3 = 1


    for i in range (1, nall + 1):
        factorial1 = factorial1 * i

    for i in range (1, ndrawn + 1):
        factorial2 = factorial2 * i

    for i in range (1, nall - ndrawn + 1):
        factorial3 = factorial3 * i

    nsequences = int(factorial1 / (factorial3 * factorial2))

    return f"1/{nsequences}"


def main():

    nall = int(input("Enter the total number of lottery balls: "))
    ndrawn = int(input("Enter the number of the drawn balls: "))

    if input_check(nall, ndrawn):
        print(f"The probability of guessing all {ndrawn} balls correctly is",
              probability(nall, ndrawn))


if __name__ == "__main__":
    main()