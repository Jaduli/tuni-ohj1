"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def print_verse(animal,sound):
    """Print the verse to the song Old McDonald Had a Farm"""
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {animal}")
    print("E-I-E-I-O")
    print(f"With a {sound} {sound} here")
    print(f"And a {sound} {sound} there")
    print(f"Here a {sound}, there a {sound}")
    print(f"Everywhere a {sound} {sound}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")

def main():

    print_verse("cow","moo")
    print()
    print_verse("pig","oink")
    print()
    print_verse("duck","quack")
    print()
    print_verse("horse","neigh")
    print()
    print_verse("lamb","baa")


if __name__ == "__main__":
    main()