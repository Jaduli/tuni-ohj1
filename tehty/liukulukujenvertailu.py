"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146

Ohjelma liukulukujen vertailuun
"""

EPSILON = 0.000000001

def compare_floats(float1, float2, EPSILON):
    """
    Funktio jolla tutkitkitaan, onko kaksi liukulukua float1 ja float2
    samoja annetun epsilonin tarkkuudella vertailtuna.
    """

    return abs(float1 - float2) < EPSILON



def main():

    print(compare_floats(float1, float2, EPSILON))

if __name__ == "__main__":
    main()
