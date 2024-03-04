import numpy as np


def problema1():
    print("a) ")
    # Numărul de simulări repetate
    num_simulations = 100000

    # Numărul de persoane în grup
    num_people = 23

    # Numărul de zile într-un an (365 pentru un an ne-bisect, 366 pentru un an bisect)
    num_days_in_year = 365

    # Variabila pentru a număra câte simulări au cel puțin două persoane cu aceeași zi de naștere
    count = 0

    for _ in range(num_simulations):
        # Generați aleator 23 de zile de naștere pentru cele 23 de persoane
        birthdays = np.random.randint(1, num_days_in_year + 1, num_people)

        # Verificați dacă există cel puțin două zile de naștere egale în grup
        if len(birthdays) != len(set(birthdays)):
            count += 1

    # Calcularea probabilitatii
    probability = count / num_simulations

    print(
        f"Probabilitatea că cel puțin două persoane dintr-un grup de {num_people} au aceeași zi de naștere este aproximativ {probability:.4f}")

    print("b)")
    # Calcularea probabilității că cel puțin două persoane dintr-un grup de 23 au aceeași zi de naștere
    probability = 1.0
    for i in range(23):
        probability *= (365 - i) / 365

    probability = 1 - probability
    print(
        f"Probabilitatea este  {probability:.4f}")
