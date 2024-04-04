"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, nimi, hinta):
        """
        Tuote, jolle annetaan nimi ja hinta

        :param nimi: tuotteen nimi
        :param hinta: tuotteen hinta
        """

        self.__nimi = nimi
        self.__hinta = hinta
        self.__alennusprosentti = 0.0
        self.__alennettuhinta = hinta


    def set_sale_percentage(self, alennusprosentti2):
        """
        Asettaa alennetun hinnan annetulla alennusprosentilla

        :param alennusprosentti2: alennusprosentti
        :return: None
        """
        self.__alennusprosentti = alennusprosentti2
        self.__alennettuhinta = (self.__hinta *
                                 (1 - self.__alennusprosentti / 100))

    # TODO: Define all the methods here.  You can see what they are,
    #       what parameters they take, and what their return value is
    #       by examining the main-function carefully.
    #
    #       You also need to consider which attributes the class needs.
    #
    #       You are allowed to modify the main function, but your
    #       methods have to stay compatible with the original
    #       since the automatic tests assume that.

    def get_price(self):
        """
        Palauttaa alennetun hinnan

        :return: alennettu hinta
        """

        return self.__alennettuhinta

    def printout(self):
        """
        Tulostaa tuotteen nimen, alkuperäisen hinnan ja alennusprosentin

        :return: None
        """
        print(self.__nimi)
        print(f"  price: {self.__hinta:.2f}")
        print(f"  sale%: {self.__alennusprosentti:.2f}")


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
