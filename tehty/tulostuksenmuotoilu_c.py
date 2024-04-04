"""
COMP.CS.100 Ohjelmointi 1
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:>4}", end="")
        print()

if __name__ == "__main__":
    main()
