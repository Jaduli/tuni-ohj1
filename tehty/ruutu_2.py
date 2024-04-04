"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
Print a box with input error checking
"""

def print_box(width, height, mark):
    """Print a box with marks m with the width w and height h"""
    w = int(width)
    h = int(height)

    for i in range(0, h):
        print(mark * w)

def read_input(qst):
    """Checks if number input is applicable to the program"""
    legit = False

    while legit == False:

        try:
            nmbr = int(input(qst))


            if nmbr > 0:
                return nmbr
                legit = True

            else:
                legit = False

        except ValueError:
            pass







def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()

    print_box(width, height, mark)


if __name__ == "__main__":
    main()
