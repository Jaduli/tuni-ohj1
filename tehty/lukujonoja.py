"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""



def main():

    for i in range(0,101):
        if i % 2 == 0:
            print(i)

    for i in range(0,101):
        if i % 2 == 0:
            print(100-i)

if __name__ == "__main__":
    main()