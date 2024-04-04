"""
COMP.CS.100 Ohjelmointi 1
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""
def main():

    amount = input("How many Fibonacci numbers do you want? ")
    amount = int(amount)

    f_1 = 1
    f_2 = 1


    amount_2 = 3

    if amount == 1:
        print(f"1. {f_1}")

    elif amount == 2:
        print(f"1. {f_1}\n2. {f_2}")

    elif amount > 0:
        print(f"1. {f_1}")
        print(f"2. {f_2}")
        for i in range(1,amount - 1):

            f_uusi = f_1 + f_2
            print(f"{amount_2}. {f_uusi}")
            amount_2 += 1

            f_1 = f_2
            f_2 = f_uusi







if __name__ == "__main__":
    main()