"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""


def main():
    run = True
    word_count = {}

    print("Enter rows of text for word counting. Empty row to quit.")
    while run == True:
        sentence = input()

        if sentence == "":
            run = False
            break

        lower_sentence = sentence.lower()
        split_sentence = lower_sentence.split(" ")

        for word in split_sentence:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    for word in sorted(word_count):
        print(f"{word} : {word_count[word]} times")

if __name__ == "__main__":
    main()