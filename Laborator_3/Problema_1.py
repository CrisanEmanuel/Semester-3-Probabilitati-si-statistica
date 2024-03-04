from random import choices, sample
from math import comb, perm


def problema1():
    print("PROBLEMA 1")
    print("i) Prin simulari")
    nr_simulari = 10000
    caz_fav = 0
    caz_pos = 0
    for i in range(nr_simulari):
        bile_extrase = sample(['red', 'blue', 'green'], counts=[5, 3, 2], k=3)
        if bile_extrase.__contains__('red'):
            caz_pos += 1
        if bile_extrase[0] == 'red' and bile_extrase[1] == 'red' and bile_extrase[2] == 'red':
            caz_fav += 1

    p = caz_fav / caz_pos
    print("P(B|A) = ", p)

    print()
    print("ii) Teoretica")
    probabilityA = 1 - comb(5, 3) / comb(10, 3)
    probabilityBA = comb(5, 3) / comb(10, 3)

    probabilityBAcond = probabilityBA / probabilityA
    print("P(B|A)=", probabilityBAcond)
