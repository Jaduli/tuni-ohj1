"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator
        self.__reciprocal = 0

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        Simplifies the fraction based on it's greatest common divisor.
        """
        divisor = greatest_common_divisor(self.__numerator, self.__denominator)

        self.__denominator = self.__denominator // divisor
        self.__numerator = self.__numerator // divisor


    def complement(self):
        """
        Turns fraction into it's complement

        :return: new fraction
        """
        if self.__numerator < 0 or self.__denominator < 0:
            numerator = abs(self.__numerator)
            denominator = abs(self.__denominator)
            
        else:
            numerator = -self.__numerator
            denominator = self.__denominator

        complement = Fraction(numerator, denominator)

        return complement

    def reciprocal(self):
        """
        Turns fraction into it's reciprocal

        :return: new fraction
        """

        numerator = self.__denominator
        denominator = self.__numerator

        reciprocal = Fraction(numerator, denominator)

        return reciprocal


    def multiply(self, frac2):
        """
        Multiplies two fractions together

        :return: new fraction
        """

        numerator = self.__numerator * frac2.__numerator
        denominator = self.__denominator * frac2.__denominator

        result = Fraction(numerator, denominator)

        return result

    def divide(self, frac2):
        """
        Divides two fractions

        :return: new fraction
        """

        reciprocal2 = frac2.reciprocal()
        numerator = reciprocal2.__numerator * self.__numerator
        denominator = reciprocal2.__denominator * self.__denominator

        result = Fraction(numerator, denominator)

        return result

    def add(self, frac2):
        """
        Adds fraction with given fraction.

        :return: new fraction
        """

        denominator = self.__denominator * frac2.__denominator

        numerator1 = self.__denominator * frac2.__numerator
        numerator2 = self.__numerator * frac2.__denominator

        numerator = numerator1 + numerator2

        result = Fraction(numerator, denominator)

        return result


    def deduct(self, frac2):
        """
        Deducts given fraction from fraction.

        :return: new fraction
        """
        denominator = self.__denominator * frac2.__denominator

        numerator2 = self.__denominator * frac2.__numerator
        numerator1 = self.__numerator * frac2.__denominator

        numerator = numerator1 - numerator2

        result = Fraction(numerator, denominator)

        return result

    def __lt__(self, fraction_object):
        return eval(self.deduct(fraction_object).return_string()) < 0

    def __le__(self, fraction_object):
        return eval(self.deduct(fraction_object).return_string()) > 0

    def __str__(self):
        return self.return_string()

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def main():

    list_of_values = {}

    while True:
        operation = input("> ")

        if operation == "quit":
            print("Bye bye!")
            break

        elif operation == "add":
            fraction = input("Enter a fraction in the form integer/integer: ")
            numerator_str, denominator_str = fraction.split("/")

            numerator = int(numerator_str)
            denominator = int(denominator_str)

            new_fraction = Fraction(numerator, denominator)

            name = input("Enter a name: ")
            list_of_values[name] = new_fraction

        elif operation == "print":
            name = input("Enter a name: ")

            if name not in list_of_values.keys():
                print(f"Name {name} was not found")
                continue

            print(name, "=", list_of_values[name])

        elif operation == "list":
            sorted_list = {}

            sorted_keys = sorted(list_of_values.keys())

            for key in sorted_keys:
                sorted_list[key] = list_of_values[key]

            for key, value in sorted_list.items():
                print(key, "=", value)

        elif operation == "*":
            key1 = input("1st operand: ")

            if key1 not in list_of_values.keys():
                print(f"Name {key1} was not found")
                continue

            key2 = input("2nd operand: ")

            if key2 not in list_of_values.keys():
                print(f"Name {key2} was not found")
                continue

            operand1 = list_of_values[key1]
            operand2 = list_of_values[key2]

            result = operand1.multiply(operand2)
            print(operand1, "*", operand2, "=", result)

            result.simplify()
            print("simplified", result)

        elif operation == "file":
            file_name = input("Enter the name of the file: ")

            try:
                file = open(file_name, "r")

            except FileNotFoundError:
                print("Error: the file cannot be read.")
                continue

            for line in file:
                try:
                    name, rest = line.split("=")

                    numerator_str, denominator_str = rest.split("/")

                    numerator = int(numerator_str)
                    denominator = int(denominator_str)

                    new_fraction = Fraction(numerator, denominator)

                    list_of_values[name] = new_fraction
                except:
                    print("Error: the file cannot be read.")
                    break


        else:
            print("Unknown command!")



if __name__ == "__main__":
    main()