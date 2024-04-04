"""
COMP.CS.100 Ohjelmointi 1
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""
def main():

    amount = input("How many numbers would you like to have? ")
    amount = int(amount)



    for number in range(1, amount+1):
        if number % 3 == 0 and number % 7 == 0:
            print("zip boing")

        elif number % 3 == 0:
            print("zip")

        elif number % 7 == 0:
            print("boing")

        elif number > 0:
            print(number)



if __name__ == "__main__":
    main()