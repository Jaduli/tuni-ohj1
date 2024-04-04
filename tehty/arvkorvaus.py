"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def convert_grades(grades):
    """
    Muuttaa annetun arvosanalistan välillä 1-5 olevan numeron numeroksi 6.

    :param list: arvosanalista
    """

    index = 0

    for grade in grades:
        if grade != 0:
            grades[index] = 6

        index += 1


def main():


    convert_grades()



if __name__ == "__main__":
    main()
