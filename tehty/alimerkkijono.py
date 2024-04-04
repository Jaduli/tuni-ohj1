"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
"""

def longest_substring_in_order(text):
    """
    Lyötää sanan pisimmän aakkosjärjestyksessä olevan pätkän.

    :param text: sana
    :return: pisin aakkosjärjestyksessä oleva pätkä
    """

    list1 = []
    new_list = []

    if len(text) == 1:
        return text

    else:
        for i in range(0, len(text)-1):

            if text[i] == text[:]:
                return text[i]

            elif text[i] <= text[i+1]:
                 new_list.append(text[i])
                 if i == len(text)-2:
                     new_list.append(text[i+1])
                 if len(new_list) > len(list1):
                     list1 = new_list

            else:
                new_list.append(text[i])
                if len(new_list) > len(list1):
                    list1 = new_list
                new_list = []

    longest = "".join(list1)

    return longest




def main():

    longest_substring_in_order()


if __name__ == "__main__":
    main()