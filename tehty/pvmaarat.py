"""
COMP.CS.100 Ohjelmointi 1
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""
def main():

    month = 1
    day = 1

    while month < 13:

        if month == 2:
            while day < 29:
                print(f"{day}.{month}.")
                day += 1

        elif month % 2 == 0 and month < 8:
            while day < 31:
                print(f"{day}.{month}.")
                day += 1

        elif month % 2 != 0 and month < 8:
            while day < 32:
                print(f"{day}.{month}.")
                day += 1

        elif month % 2 != 0:
            while day < 31:
                print(f"{day}.{month}.")
                day += 1

        elif month % 2 == 0:
            while day < 32:
                print(f"{day}.{month}.")
                day += 1

        day = 1
        month += 1

if __name__ == "__main__":
    main()