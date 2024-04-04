# COMP.CS.100 Python-ohjelma.
# Tekijä: Jade Pitkänen
# Opiskelijanumero: 151842146

def main():
    string = input("How do you feel? (1-10) ")
    number = int(string)
    if number <= 10 and number > 0:
        if number > 7 and number != 10:
            print("A suitable smiley would be :-)")
        elif number <= 7 and number >= 4:
            print("A suitable smiley would be :-|")
        elif number < 4 and number != 1:
            print("A suitable smiley would be :-(")
        elif number == 10:
            print("A suitable smiley would be :-D")
        else:
            print("A suitable smiley would be :'(")
    else:
        print("Bad input!")


if __name__ == "__main__":
    main()