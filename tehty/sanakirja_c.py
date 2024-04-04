"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def print_dictionary(dictionary):
    """
    Tulostaa annetun kirjaston

    :param dictionary: kirjasto
    """
    print("Dictionary contents:")

    dic_list = list(dictionary.keys())
    dic_list.sort()
    contents = ", ".join(dic_list)
    print(contents)

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    print_dictionary(english_spanish)

    while True:

        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")

            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            eng = input("Give the word to be added in English: ")
            spn = input("Give the word to be added in Spanish: ")

            english_spanish[eng] = spn

            print_dictionary(english_spanish)

        elif command == "R":
            word = input("Give the word to be removed: ")

            if word in english_spanish:
                del english_spanish[word]
            else:
                print(f"The word {word} could not be found from the dictionary.")

        elif command == "P":
                print()
                spanish_english = {}

                for key, value in english_spanish.items():
                    spanish_english[value] = key


                print("English-Spanish")
                for word in sorted(english_spanish):
                    print(word, english_spanish[word])

                print()

                print("Spanish-English")
                for word in sorted(spanish_english):
                    print(word, spanish_english[word])

                print()

        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            text_split = text.split()

            i = 0
            for word in text_split:
                if word in english_spanish:
                    word = english_spanish[word]
                    text_split[i] = word
                i+=1

            translated = " ".join(text_split)
            print("The text, translated by the dictionary: ")
            print(translated)

        elif command == "Q":

            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
