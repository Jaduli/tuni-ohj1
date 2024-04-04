"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""


def print_box(w_str, h_str, m):
    """Print a box with marks m with the width w and height h"""
    w = int(w_str)
    h = int(h_str)

    for i in range(0, h):
        print(m * w)



def main():
    w_str = input("Enter the width of a frame: ")
    h_str = input("Enter the height of a frame: ")
    m = input("Enter a print mark: ")
    print()
    print_box(w_str, h_str, m)


if __name__ == "__main__":
    main()