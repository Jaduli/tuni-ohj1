"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def read_message():
    """
    Pyytää käyttäjää antamaan lauseita, tyhjä input palauttaa listan lauseista.

    :return: lista annetuista lauseista
    """

    cont = True

    list = []

    while cont == True:
        row = input()

        if row != "":
            list.append(row)

        elif row == "":
            break

    return list


def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]



    letter = text.lower()

    if letter in regular_chars:
        position = regular_chars.index(letter)
        encrypted = encrypted_chars[position]

        if text.isupper():
            encrypted = encrypted.upper()


        return encrypted

    else:
        return text

def row_encryption(sentence):
    """
    Creates an encrypted message using the encrypt-function.

    :param sentence: sentence to encrypt
    :return: encrypted sentence
    """

    complete = []

    for i in range(0, len(sentence)):
        letter = encrypt(sentence[i])
        complete.append(letter)

    complete = "".join(complete)

    return complete

def main():

    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for i in range(0, len(msg)):
        print(row_encryption(msg[i]))


if __name__ == "__main__":
    main()