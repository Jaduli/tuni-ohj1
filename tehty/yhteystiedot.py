"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def read_file(file):
    """
    Lukee tiedoston ja palauttaa siitä tehdyn sanakirjaston, jossa on avain
    (esim. nimi) ja arvo (esim. Antti Salminen).

    :param file: luettava tiedosto
    :return: sanakirjasto
    """

    try:
        opened_file = open(file, mode="r")

        keys = opened_file.readline()
        keys = keys.rstrip().split(";")


        information_dict = {}

        for line in opened_file:

            line = line.rstrip()
            line = line.split(";")

            new_dict = {}

            for i in range(1, len(line)):
                if line[i] == "":
                    pass

                else:
                    new_dict[keys[i]] = line[i]

            information_dict[line[0]] = new_dict

        opened_file.close()

        return information_dict


    except OSError:
        print("File not found")


def main():

    read_file()




if __name__ == "__main__":
    main()