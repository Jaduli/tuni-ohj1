"""
COMP.CS.100 Ohjelmointi 1
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""
def main():

    number = input("Choose a number: ")

    number = int(number)

    multiply = 1

    while multiply <= 10:
        print(multiply,"*",number,"=",number * multiply)
        multiply = multiply + 1


if __name__ == "__main__":
    main()