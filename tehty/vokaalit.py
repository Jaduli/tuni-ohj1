"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""


def main():

    vowels = ["a", "e", "i", "o", "u", "y", "ä", "ö"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p",
                  "q", "r", "s", "t", "v", "w", "x", "z"]

    vowel_count = 0
    consonant_count = 0

    word = input("Enter a word: ")

    word_lenght = int(len(word))

    for letter in range(0, word_lenght):
        if word[letter] in vowels:
            vowel_count += 1

        elif word[letter] in consonants:
            consonant_count += 1


    print(f"The word \"{word}\" contains {vowel_count} vowels and "
          f"{consonant_count} consonants.")


if __name__ == "__main__":
    main()