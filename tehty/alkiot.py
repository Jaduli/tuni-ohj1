"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def are_all_members_same(list):
    """
    Tutkii, onko annetussa listassa ainoastaan yhtä numeroa.

    :param list: Tutkittava lista
    :return: True tai False
    """

    if len(list) > 0:
        first_number = list[0]

        for number in list:
            if number == first_number:
                result = True
            else:
                result = False
                break

        return result
    else:
        return True



def main():


    are_all_members_same(list)


if __name__ == "__main__":
    main()