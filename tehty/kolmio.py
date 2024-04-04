"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
Trangle's Area when the Sides Are Known
"""

from math import sqrt

def area(a,b,c):
    """
    Function to calculate the area of a triangle
    using the length of its sides a, b and c
    """
    s = (a+b+c)/2

    area_abc = sqrt(s*(s-a)*(s-b)*(s-c))

    return area_abc



def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    answer = area(a,b,c)

    print(f"The triangle's area is {answer:.1f}")


if __name__ == "__main__":
    main()
