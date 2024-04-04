"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def input_to_list(n):
    """
    Funktio muodostaa käyttäjän tekemän listan numeroita.

    :param n: listan numeroiden määrä
    :return: numerolista
    """

    nlist = []

    print(f"Enter {n} numbers:")

    x = 0

    while x < n:
        number = int(input())

        nlist.append(number)

        x += 1

    return nlist


def main():

    n = int(input("How many numbers do you want to process: "))

    numberlist = input_to_list(n)

    nsearch = int(input("Enter the number to be searched: "))

    found = False
    amount = 0

    for number in numberlist:

        if number == nsearch:
            found = True
            amount += 1

    if found:
        print(f"{nsearch} shows up {amount} times among the numbers you have "
              f"entered.")
    else:
        print(f"{nsearch} is not among the numbers you have entered.")


if __name__ == "__main__":
    main()