"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146

Projekti: Laivanupotus-peli.
Pelaaja syöttää koordinaatteja ja yrittää upottaa kaikki laivat.
Vaatii tiedoston laivojen koordinaateista.
"""


class Battleship:
    """
    Battleship eli sotalaiva, jota käytetään laivanupotus-pelissä.
    """

    def __init__(self, ship_type, coordinates):
        """
        Battleship-oliolla on tyyppi, koordinaatit, pituus, laivaan osuneiden
        ammuksien määrä ja tieto siitä, onko laiva upotettu vai ei.

        :param ship_type: laivan tyyppi, esim. submarine
        :param coordinates: laivan koordinaatit laudalla
        """

        self.__ship_type = ship_type
        self.__coordinates = coordinates
        self.__length = len(coordinates)
        self.__shots = 0
        self.__sunk = False

    def set_sunk_value(self):
        """
        Tarkastaa, onko laiva upotettu, ja muuttaa olion totuusarvoa
        tarvittaessa.
        """

        if self.__length == self.__shots:
            self.__sunk = True

    def get_sunk_value(self):
        """
        Palauttaa totuusarvon, onko laiva upotettu vai ei.
        Upotettu laiva = True.

        :return: True tai False
        """

        return self.__sunk

    def check_shot(self, coord):
        """
        Tarkastaa, onko annettu koordinaatti myös laivan koordinaatti, eli
        osuttiinko laivaan. Osuessa olion osumien määrää korotetaan yhdellä.

        :param coord: ammunnan koordinaatti
        """

        if coord in self.__coordinates:
            self.__shots += 1

    def get_type(self):
        """
        Palauttaa laivan tyypin.

        :return: str, laivan tyyppi
        """

        return self.__ship_type

    def get_coordinates(self):
        """
        Palauttaa laivan koordinaattilistan.

        :return: list, laivan koordinaattilista
        """

        return self.__coordinates


def file_as_dict(filename):
    """
    Tekee annetusta tiedostosta sanakirjan, jossa on avaimena rivin ensimmäinen
    sana ja arvona lista muista rivin arvoista. Laivanupotusta varten
    koordinaatit muutetaan myös isoiksi kirjaimiksi. Oletuksena muoto
    str;str;str;...

    :param filename: yhteensopiva tiedosto
    :return: tiedostosta luotu sanakirja tai vihetilanteessa None
    """

    try:
        file = open(filename, "r")

    except FileNotFoundError:
        print("File can not be read!")
        return None

    information_dict = {}

    for line in file:
        stripped_line = line.strip()
        split_line = stripped_line.upper().split(";")
        information_dict[split_line[0]] = split_line[1:]

    return information_dict


def check_dict(dict_name):
    """
    Tarkastaa ovatko annetun sanakirjan arvot sopivia ohjelman laivanupotus
    -peliä varten. Koordinaatin tulee olla muotoa [kirjain][numero], jossa
    kirjain on väliltä A-J ja numero väliltä 0-9. Kahdella laivalla ei saa
    olla samaa koordinaattia.

    :param dict_name: sanakirja, jossa on arvona lista koordinaatteja
    :return: True tai False
    """

    # muodostetaan koordinaateista lista, jotta voidaan tarkastaa, onko
    # kahdella tai useammalla laivalla sama koordinaatti
    coords_list = []

    min_row, max_row = 0, 9
    min_col, max_col = "A", "J"

    for list in dict_name.values():
        for coord in list:
            if (min_col <= coord[0] <= max_col
                    and min_row <= int(coord[1:]) <= max_row):

                if coord in coords_list:
                    print("There are overlapping ships in the input file!")
                    return False

                else:
                    coords_list.append(coord)

            else:
                print("Error in ship coordinates!")
                return False

    return True


def create_ships(filename):
    """
    Luo annetun tiedoston perusteella Battleship-olioita ja lisää ne listaksi.
    Tiedoston rivit oletuksella muodossa str;str;str;...

    :param filename: tiedoston nimi
    :return: lista Battleship-olioita
    """

    file = open(filename, "r")

    list_of_ships = []

    for line in file:
        stripped_line = line.strip()
        split_line = stripped_line.upper().split(";")

        ship = Battleship(split_line[0], split_line[1:])
        list_of_ships.append(ship)

    return list_of_ships


def print_board(hit_coords, miss_coords, sunk_coords):
    """
    Tulostaa laivanupotus-pelin pelilaudan.

    :param hit_coords: lista osumien koordinaateista
    :param miss_coords: lista ohi menneiden ammuksien koordinaateista
    :param sunk_coords: lista koordinaateista, joissa on uponnut laiva
    :return: koordinaattien perusteella luotu pelilauta
    """

    print()
    print("  A B C D E F G H I J")

    rows_list = []  # lista riveistä pelilaudalla

    for i in range(0, 10):
        row = [str(i), " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        rows_list.append(row)
        # Lisätään rivit listaan yksi kerrallaan.
        # Lisätään rivin alkuun i, jotta numerolla voidaan käsitellä
        # oikeaa riviä tulostuksessa.

    for miss in miss_coords:
        column = ord(miss[0]) - ord("A") + 1
        # huomioidaan rivin ensimmäinen alkio i, eli lisätään arvoon 1
        row = int(miss[1])

        rows_list[row][column] = "*"

    for hit in hit_coords:
        column = ord(hit[0]) - ord("A") + 1
        row = int(hit[1])

        rows_list[row][column] = "X"

    for sunk in sunk_coords:
        # jos laiva on upotettu, X:n sijaan tulostetaan kohtaan laivan tyypin
        # ensimmäinen kirjain
        column = ord(sunk[0]) - ord("A") + 1
        row = int(sunk[1])

        rows_list[row][column] = sunk[2]

    for row in rows_list:
        # tulostetaan lauta rivi kerrallaan
        row_index = rows_list.index(row)

        print(row_index, " ".join(row[1:]), row_index)

    print("  A B C D E F G H I J")
    print()


def check_input(input):
    """
    Tarkastaa, onko syöte ohjelmaan yhteensopiva koordinaatti.
    On sopiva = True. Syöte Q palauttaa "quit".

    :param input: syöte
    :return: True tai False tai "quit"
    """

    # Oletetaan, että syöte on sopiva. Muutetaan arvoa tarvittaessa
    check = True

    # määritetään koordinaateille rajat
    min_row, max_row = 0, 9
    min_col, max_col = "A", "J"

    try:
        if input == "Q":
            return "quit"

        elif (input[0].isalpha() and min_col <= input[0] <= max_col
              and min_row <= int(input[1:]) <= max_row):
            pass

        else:
            check = False

    # virhetilanteessa (esim. tyhjä syöte) palautetaan False
    except:
        check = False

    return check


def main():
    file_name = input("Enter file name: ")

    # luodaan tiedostosta sanakirja, jotta voidaan tarkistaa sen
    # yhteensopivuus peliin
    game_info = file_as_dict(file_name)
    if game_info == None:
        return

    if check_dict(game_info) == False:
        return

    ships = create_ships(file_name)

    # muodostetaan koordinaateille aluksi tyhjä lista
    hit_coords = []
    miss_coords = []
    sunk_coords = []

    print_board(hit_coords, miss_coords, sunk_coords)

    while True:
        user_input = input("Enter place to shoot (q to quit): ").upper()

        check = check_input(user_input)

        if check == "quit":
            print("Aborting game!")
            return

        elif check == False:
            print("Invalid command!")
            pass

        else:

            if user_input in hit_coords or user_input in miss_coords:
                print("Location has already been shot at!")

            else:
                for ship in ships:
                    ship.check_shot(user_input)

                    ship_coords = ship.get_coordinates()
                    if user_input in ship_coords:
                        hit_coords.append(user_input)

                        if user_input in miss_coords:
                            miss_coords.remove(user_input)

                    if (user_input not in hit_coords and user_input not in
                            miss_coords):
                        miss_coords.append(user_input)

                    ship.set_sunk_value()
                    if ship.get_sunk_value() == True:
                        ship_type = ship.get_type()
                        print(f"You sank a {ship_type.lower()}!")

                        for coord in ship_coords:
                            sunk_coords.append(coord + ship_type[0])
                            # lisätään koordinaatin perään laivan alkukirjain,
                            # jota käytetään laudan tulostuksessa

                        ships.remove(ship)

        print_board(hit_coords, miss_coords, sunk_coords)

        if len(ships) == 0:
            print("Congratulations! You sank all enemy ships.")
            break


if __name__ == "__main__":
   main()
