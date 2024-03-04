from random import sample
from math import factorial
from itertools import permutations


def problema_2():
    # a)
    print("a)")
    cuvant = "word"
    permutari = list(permutations(cuvant))

    for permutare in permutari:
        print(''.join(permutare))

    # b)
    print()
    print("b)")
    numar_permutari = factorial(len(cuvant))
    print(f"Numărul total de permutări pentru cuvântul '{cuvant}' este {numar_permutari}")

    # c)
    print()
    print("c)")
    permutare_aleatoare = ''.join(sample(cuvant, len(cuvant)))
    print("Permutare aleatoare a cuvântului 'word':", permutare_aleatoare)
