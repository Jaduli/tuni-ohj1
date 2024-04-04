"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
Projekti 2
"""

"""
Ohjelma kysyy käyttäjältä päivien määrän ja näiden päivien lämpötilat.
Lämpötiloista lasketaan mediaani ja keskiarvo sekä lopuksi tarkastellaan
kuinka paljon pienempi tai suurempi päivän lämpötila oli keskiarvoon 
verrattuna.
"""


def create_temperature_list(number_of_days):
    """
    Kysyy käyttäjältä päivien lämpötilan ja muodostaa niistä listan.

    :param number_of_days: päivien möörö
    :return: lista lämpötiloista
    """

    list = []

    for i in range(1, number_of_days + 1):
        dayi_temp = float(input(f"Enter day {i}. temperature in Celcius: "))
        list.append(dayi_temp)

    return list


def count_mean_from_list(list, n):
    """
    Laskee annetun listan keskiarvon.

    :param list: numerolista
    :param n: numeroiden määrä listassa
    :return: listan numeroiden keskiarvo
    """

    total = sum(list)
    mean = total / n

    return mean


def calculate_median_from_list(list, n):
    """
    Laskee annetun listan mediaanin.

    :param list: numerolista
    :param n: numeroiden määrä listassa
    :return: listan mediaani
    """

    list_sorted = sorted(list)
    median_position = n / 2

    if median_position != int(median_position):
        median = list_sorted[int(median_position)]
    else:
        median_position = int(median_position)
        median = (list_sorted[median_position] +
                  list_sorted[median_position - 1]) / 2

    return median


def over_at_median(value, median):
    """
    Tarkastaa onko annettu arvo yhtä suuri tai suurempi kuin annettu keskiarvo.

    :param value: arvo
    :param mean: keskiarvo
    :return: True tai False
    """

    if value >= median:
        return True

    elif value < median:
        return False


def main():
    ndays = int(input("Enter amount of days: "))

    temperatures = create_temperature_list(ndays)

    print()

    mean = count_mean_from_list(temperatures, ndays)
    print(f"Temperature mean: {mean:.1f}C")

    median = calculate_median_from_list(temperatures, ndays)
    print(f"Temperature median: {median:.1f}C")

    print()
    print("Over or at median were: ")
    for i in range(0, ndays):
        if over_at_median(temperatures[i], median):
            print(f"Day {i+1:2}. {temperatures[i]:5.1f}C difference to mean: "
                  f"{temperatures[i] - mean:5.1f}C")

    print()
    print("Under median were: ")
    for i in range(0, ndays):
        if not over_at_median(temperatures[i], median):
            print(f"Day {i+1:2}. {temperatures[i]:5.1f}C difference to mean: "
                  f"{temperatures[i] - mean:5.1f}C")


if __name__ == "__main__":
    main()