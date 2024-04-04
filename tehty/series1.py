"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""


def main():

    file = input("Enter the name of the file: ")

    movies_dict = {}
    try:
        file = open(file, "r")
        for rivi in file:
            line = rivi.split(";")
            movie = line[0]

            genres = line[1:]
            genres = str(genres)
            genres = genres.replace("[","").replace("'","").replace("]","").strip(r'\n').split(",")

            for i in range(len(genres)):
                if genres[i] not in movies_dict:
                    movies_dict[genres[i]] = []

                movies_dict[genres[i]].append(movie)

    except OSError:
        print("Error")

    keygenres = []
    for key in movies_dict.keys():
        keygenres.append(key)

    keygenres.sort()

    strgenres = ", ".join(keygenres)

    print("Available genres are:", strgenres)

    while True:
        chosen_genre = input("> ")

        if chosen_genre == "exit":
            break

        try:
            movies_list = []
            genre = movies_dict[chosen_genre]

            for value in genre:
                movies_list.append(value)

            movies_list.sort()

            for movie in movies_list:
                print(movie)

        except KeyError:
            pass


if __name__ == "__main__":
    main()