"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def reverse_name(name):
    """
    Kääntää sukunimen ja etunimen muotoon etunimi, sukunimi.

    :param name: Nimi
    :return: Nimi muodossa etunimi, sukunimi
    """
    name = name.strip()

    if name.find(",") > -1:
        last_first = name.split(",")
        first_last = last_first[1] + " " + last_first[0]
        first_last = first_last.strip()

        return first_last
    else:
        return name

def main():

    reverse_name()


if __name__ == "__main__":
    main()