"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""



def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    Prints a box.

    :param width: Width of the box
    :param height:  Height of the box
    :param border_mark: Border mark of the box
    :param inner_mark: Inner mark of the box
    """

    print(width * border_mark)

    for i in range(0, height - 2):
        print(f"{border_mark}{(width - 2) * inner_mark}{border_mark}")

    print(width * border_mark)


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
