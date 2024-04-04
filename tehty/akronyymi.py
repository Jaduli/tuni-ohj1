"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def create_an_acronym(sentence):
    """
    Luo akronyymin annetusta lauseesta.

    :param sentence: lause, josta tehdään akronyymi
    :return: akronyymi
    """
    list = sentence.strip().split(" ")

    acronym = []

    words = len(list)

    for i in range(0, words):
        letter = list[i][0]
        letter = letter.upper()

        acronym.append(letter)

    acronym = "".join(acronym)

    return acronym


def main():

    create_an_acronym()

if __name__ == "__main__":
    main()