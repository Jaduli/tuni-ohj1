"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""


def repeat_name(name,n):
    """Print the name in lyrics to the song Yogi bear n amount of times"""
    if name == "Yogi":
        for i in range(0,n):
            print("Yogi, Yogi Bear")

    elif name == "Boo Boo":
        for i in range(0, n):
            print("Boo Boo, Boo Boo Bear")

    elif name == "Cindy":
        for i in range(0, n):
            print("Cindy, Cindy Bear")


def verse(lyric, bear):
    """Print the verse to the song Yogi Bear using the function repeat_name"""
    print(lyric)
    print(f"{bear}, {bear}")
    print(lyric)
    repeat_name(bear,3)
    print(lyric)
    repeat_name(bear,1)


def main():

    verse("I know someone you don't know","Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()