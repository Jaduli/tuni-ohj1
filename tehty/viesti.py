"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def read_message():
    """
    Pyytää käyttäjää antamaan lauseita, tyhjä input palauttaa listan lauseista.

    :return: lista annetuista lauseista
    """

    cont = True

    list = []

    while cont == True:
        row = input()

        if row != "":
            list.append(row)

        elif row == "":
            break

    return list


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")

    msg = read_message()

    print("The same, shouting:")

    for i in range(0, len(msg)):
        row = msg[i].upper()
        print(row)


if __name__ == "__main__":
    main()
