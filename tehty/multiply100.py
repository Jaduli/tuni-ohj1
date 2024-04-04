"""
COMP.CS.100 Ohjelmointi 1
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""
def main():

    number = input("Choose a number: ")

    number = int(number)

    multiply = 1

    while number*multiply < 100:
        print(multiply,"*",number,"=",number * multiply)
        multiply = multiply + 1
    else:
        print(multiply,"*",number,"=",number * multiply)


if __name__ == "__main__":
    main()