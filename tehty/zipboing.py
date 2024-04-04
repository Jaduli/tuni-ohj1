"""
COMP.CS.100 Ohjelmointi 1
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""
def main():

    amount = input("How many numbers would you like to have? ")
    amount = int(amount)

    number = 1

    while number <= amount:
        if number % 3 == 0 and number % 7 == 0:
            print("zip boing")

        elif number % 3 == 0:
            print("zip")

        elif number % 7 == 0:
            print("boing")

        else:
            print(number)

        number = number + 1





if __name__ == "__main__":
    main()