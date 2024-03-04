from random import sample
from math import comb, perm
from itertools import permutations, combinations


def aranjamente(cuvant, k):
    if k > len(cuvant):
        print("K trebuie să fie mai mic sau egal cu lungimea cuvântului.")
        return

    aranj = list(permutations(cuvant, k))
    permutare_aleatoare = ''.join(sample(cuvant, k))
    numar_aranjamente = perm(len(cuvant), k)

    print("a)")
    print(f"Aranjamente de {k} litere din '{cuvant}':")
    for aranjament in aranj:
        print(''.join(aranjament))

    print()
    print("b)")
    print(f"Numărul total de aranjamente: {numar_aranjamente}")
    print()
    print("c)")
    print(f"Permutare aleatoare de {k} litere din '{cuvant}': {permutare_aleatoare}")


def combinari(cuvant, k):
    if k > len(cuvant):
        print("K trebuie să fie mai mic sau egal cu lungimea cuvântului.")
        return

    combi = list(combinations(cuvant, k))
    combinare_aleatoare = ''.join(sample(cuvant, k))
    numar_combinari = comb(len(cuvant), k)

    print("a)")
    print(f"Combinări de {k} litere din '{cuvant}':")
    for combinare in combi:
        print(''.join(combinare))
    print()
    print("b)")
    print(f"Numărul total de combinări: {numar_combinari}")

    print()
    print("c)")
    print(f"Combinare aleatoare de {k} litere din '{cuvant}': {combinare_aleatoare}")
