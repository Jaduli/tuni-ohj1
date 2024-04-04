"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""


def main():

    filename = input("Enter the name of the score file: ")

    try:
        results = open(filename, mode="r")

    except OSError:
        print("File not found.")
        return

    lines_in_file = results.readlines()

    results_list = []

    for result in lines_in_file:
        result = result.split()
        results_list.extend(result)

    final_results = {}

    for i in results_list:
        indexi = results_list.index(i)

        if indexi % 2 == 0:
            if i not in final_results:
                final_results[i] = 0

        else:
            final_results[results_list[indexi-1]] = final_results[results_list[indexi-1]] + int(i)

    sorted_keys = sorted(final_results.keys())

    sorted_results = {}

    for key in sorted_keys:
        sorted_results[key] = final_results[key]

    print("Contestant score:")

    for key, value in sorted_results.items():
        print(key, value)


if __name__ == "__main__":
    main()