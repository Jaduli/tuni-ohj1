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

    filename = input("Enter the name of the file: ")

    try:
        modfile = open(filename, mode="w")

    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    counter = 1

    print("Enter rows of text. Quit by entering an empty row.")

    lines_list = read_message()

    try:
        for line in lines_list:
            print(counter, line, file=modfile)
            counter += 1

    except:
        print(f"Writing the file {filename} was not successful.")
        return


    modfile.close()

    print(f"File {filename} has been written.")


if __name__ == "__main__":
    main()