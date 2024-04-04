"""
COMP.CS.100 Ohjelmointi 1
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
Tehtävä
"""
def main():
    answer = False
    ask = "0"

    while answer == False:

        while ask != "y":
            ask = input("Answer y or n: ")

            if ask != "n":
                print("Incorrect entry")

        print("Well, let's stop this, then.")
        answer = True

if __name__ == "__main__":
    main()