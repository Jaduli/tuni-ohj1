"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""


def main():

    bus_times = [630, 1015, 1415, 1620, 1720, 2000]

    current_time = int(input("Enter the time (as an integer): "))

    bus_times.append(current_time)

    bus_times.sort()

    position = bus_times.index(current_time) + 1

    index = 0

    print("The next buses leave:")


    while index < 3:
        if position <= 6:
            print(bus_times[position])
            position += 1
            index += 1
        else:
            position = 0




if __name__ == "__main__":
    main()