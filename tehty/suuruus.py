"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def is_the_list_in_order(list):
    """
    Tarkistaa, onko annetun listan numerot suuruusjärjestyksessä.

    :param list: numerolista
    :return: True tai False
    """

    sorted_list = sorted(list)

    if list == sorted_list:
        return True
    else:
        return False


def main():

    is_the_list_in_order(list)


if __name__ == "__main__":
    main()