"""
COMP.CS.100 Ohjelmointi 1, syksy 2023
Tekijä: Jade Pitkänen, jade.pitkanen@tuni.fi
Opiskelijanumero: 151842146
Paracetamol/Panadol/Tylenol Dosing Advisor
"""

def calculate_dose(weight, previous, total24):
    """
    Calculate the dose of parasetamol based on weight, previous dose
    and total dose over 24h
    """
    max_6h = weight * 15
    max_24h = 4000

    if previous < 6 or total24 >= max_24h:
        return 0

    elif total24 + max_6h <= max_24h:
        return max_6h

    elif total24 + max_6h > max_24h:
        dose = max_24h - total24
        return dose


def main():
    weight = float(input("Patient's weight (kg): "))
    previous = float(input("How much time has passed from the previous dose (full hours): "))
    total24 = float(input("The total dose for the last 24 hours (mg): "))

    dose = int(calculate_dose(weight, previous, total24))

    print(f"The amount of Parasetamol to give to the patient: {dose}")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()
