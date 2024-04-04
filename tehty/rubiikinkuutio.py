"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""



def main():

    list_of_times = []

    performance = 1

    while performance <= 5:
        time = float(input(f"Enter the time for performance {performance}: "))
        list_of_times.append(time)
        performance += 1

    list_of_times.remove(max(list_of_times))
    list_of_times.remove(min(list_of_times))

    times3 = 0

    for time in list_of_times:
        times3 += time

    avarage = times3 / 3

    print(f"The official competition score is {avarage:.2f} seconds.")


if __name__ == "__main__":
    main()