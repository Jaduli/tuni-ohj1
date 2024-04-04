"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():

    run_program = True

    while run_program:
        product = input("Enter product name: ")

        str_product = product.replace(" ","")

        if str_product == "":
            run_program = False
            print("Bye!")
            break

        if str_product in PRICES:
            print(f"The price of {str_product} is {PRICES[str_product]:.2f} e")
        else:
            print(f"Error: {str_product} is unknown.")

    pass


if __name__ == "__main__":
    main()
