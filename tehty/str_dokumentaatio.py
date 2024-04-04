"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def capitalize_initial_letters(sentence):
    """
    Muuttaa lauseen sanojen ensimmäiset kirjaimet isoiksi ja muut pieniksi
    kirjaimiksi.

    :param sentence: lause
    :return: muunnettu lause
    """

    list = sentence.lower().strip().split()

    complete = []

    for i in range(0, len(list)):
        letter = list[i][0].upper()
        string = letter + list[i][1:]
        complete.append(string)

    complete = " ".join(complete)

    return complete

def main():

    capitalize_initial_letters()

if __name__ == "__main__":
    main()