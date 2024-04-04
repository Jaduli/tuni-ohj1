"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def calculate_angle(angle1, angle2=90):
    """
    Laskee kolmannen kulman suuruuden.

    :param angle1: Ensimmäisen kulman suuruus asteina
    :param angle2: Toisen kulman suuruus asteina
    :return: Kolmannen kulman  suuruus asteina
    """

    angle1 = int(angle1)
    angle2 = int(angle2)

    angle3 = 180 - angle1 - angle2

    return angle3


def main():

    print(calculate_angle(angle1, angle2))

if __name__ == "__main__":
    main()