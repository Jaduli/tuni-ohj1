"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

from math import pi

def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            side = 0
            square(side)

            pass

        elif answer == "r":
            side1 = 0
            side2 = 0
            rectangle(side1, side2)

            pass

        elif answer == "c":
            r = 0
            circle(r)

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()


def square(side):
    """
    Laskee neliön pinta-alan ja piirin sen sivun perusteella.

    :param side: Neliön sivun pituus.
    """
    while side_check(side) == False:
        side = float(input("Enter the length of the square's side: "))

    scircumference = 4 * side
    ssurface_area = side * side

    circumference(scircumference)
    surface_area(ssurface_area)


def rectangle(side1, side2):
    """
    Laskee suorakulmion piirin ja pinta-alan sen sivujen perusteella.

    :param side1: Suorakulmion ensimmäinen sivu.
    :param side2: Suorakulmion toinen sivu.
    """

    while side_check(side1) == False:
        side1 = float(input("Enter the length of the rectangle's side 1: "))

    while side_check(side2) == False:
        side2 = float(input("Enter the length of the rectangle's side 2: "))


    rcircumference = side1 * 2 + side2 * 2
    rsurface_area = side1 * side2

    circumference(rcircumference)
    surface_area(rsurface_area)


def circle(r):
    """
    Laskee ympyrän pinta-alan ja kehän.

    :param r: Ympyrän säde.
    """
    while side_check(r) == False:
        r = float(input("Enter the circle's radius: "))

    ccircumference = 2 * pi * r
    csurface_area = pi * r * r

    circumference(ccircumference)
    surface_area(csurface_area)


def side_check(sidex):
    """
    Tarkistaa onko annettu sivun arvo validi.

    :param sidex: Sivun pituus.
    :return: Totuusarvo True, jos sivun pituus on positiivinen
    """
    if sidex > 0:
        return True

    else:
        return False


def circumference(value):
    """
    Tulostaa halutun piirin tai kehän.

    :param value: Piiri tai kehä
    """
    print(f"The circumference is {value:.2f}")

def surface_area(value):
    """
    Tulostaa halutun pinta-alan.

    :param value: Pinta-ala
    """
    print(f"The surface area is {value:.2f}")


def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
