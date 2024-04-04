"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():

    reverse_list = {}

    for key, value in PRICES.items():
        reverse_list[value] = key

    for product in sorted(reverse_list):
        print(f"{reverse_list[product]} {product:.2f}")

    pass


if __name__ == "__main__":
    main()
