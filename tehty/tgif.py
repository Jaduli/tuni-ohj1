"""
COMP.CS.100 Ohjelmointi 1
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""
def main():

    day = 3
    month = 1

    while month < 13:

        if month == 2:
            while day < 29:
                print(f"{day}.{month}.")
                day += 7
            day -= 28

        elif month % 2 == 0 and month < 8:
            while day < 31:
                print(f"{day}.{month}.")
                day += 7
            day -= 30

        elif month % 2 != 0 and month < 8:
            while day < 32:
                print(f"{day}.{month}.")
                day += 7
            day -= 31


        elif month % 2 != 0:
            while day < 31:
                print(f"{day}.{month}.")
                day += 7
            day -= 30


        elif month % 2 == 0:
            while day < 32:
                print(f"{day}.{month}.")
                day += 7
            day -= 31



        month += 1

if __name__ == "__main__":
    main()