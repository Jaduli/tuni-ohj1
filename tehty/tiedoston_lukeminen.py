"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""


def main():

    try:
        file = open(input("Enter the name of the file: "))

    except OSError:
        print("There was an error in reading the file.")
        return

    counter = 1

    for line in file:
        line = line.rstrip()
        print(counter, line)
        counter += 1

    file.close()


if __name__ == "__main__":
    main()