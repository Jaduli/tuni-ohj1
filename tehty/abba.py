"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def count_abbas(text):
    """
    Laskee montako kertaa sana "abba" esiintyy tekstissä.

    :param text: teksti
    :return: "abba"-sanojen määrä
    """

    counter = 0

    if len(text) > 3:
        for i in range(0, len(text)):
            abba = text.find("abba")

            if abba > -1:
                counter += 1
                text = text[abba + 1:]

    return counter


def main():

    count_abbas()


if __name__ == "__main__":
    main()