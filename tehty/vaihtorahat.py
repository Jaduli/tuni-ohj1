# COMP.CS.100 Python-ohjelma.
# Tekijä: Jade Pitkänen
# Opiskelijanumero: 151842146

def main():

    paid = input("Purchase price: ")
    money = input("Paid amount of money: ")

    pp = int(paid)  #purchase price
    pm = int(money) #paid money

    price = pm - pp

    if price <= 0:
        print("No change")

    else:
        print("Offer change:")
        change10 = price // 10
        if change10 > 0:
            print(change10,"ten-euro notes")

        price = price % 10

        change5 = price // 5
        if change5 > 0:
            print(change5,"five-euro notes")

        price = price % 5

        change2 = price // 2
        if change2 > 0:
            print(change2,"two-euro coins")

        price = price % 2

        change1 = price
        change1 = int(change1)
        if change1 > 0:
            print(change1, "one-euro coins")

if __name__ == "__main__":
    main()