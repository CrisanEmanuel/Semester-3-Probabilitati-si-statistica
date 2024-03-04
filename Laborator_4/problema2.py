from scipy.stats import hypergeom, geom
import numpy as np


def problema2():
    # Parametri pentru loteria 6/49
    N = 49  # Numărul total de bilete
    K = 6  # Numărul de numere câștigătoare
    n = 6  # Numărul de numere trase la fiecare extragere

    # Distribuția hipergeometrică pentru a calcula numărul de bilete câștigătoare într-o extragere
    distributie_hypergeom = hypergeom(N, K, n)

    # Distribuția geometrică pentru a calcula numărul de extrageri până la primul bilet câștigător
    # distributie_geom = geom(1 / float(distributie_hypergeom.sf(2)))

    # Lista pentru stocarea rezultatelor simulării
    rezultate_simulare = []

    # Simularea jocului de loto
    while True:
        # Generăm un număr de bilete necâștigătoare până la primul bilet câștigător
        nr_bilete_necastigatoare = 0
        numar_incercari = 1000
        for _ in range(numar_incercari):  # Număr maxim de încercări
            if distributie_hypergeom.rvs(size=1)[0] < 3:
                nr_bilete_necastigatoare += 1
            else:
                break
        else:
            raise ValueError("Nu s-a găsit un bilet câștigător în " + numar_incercari + " de încercări")

        # Adăugăm rezultatul la lista de rezultate
        rezultate_simulare.append(nr_bilete_necastigatoare)

        # Verificăm dacă avem cel puțin 3 numere câștigătoare pe biletul curent
        if distributie_hypergeom.rvs(size=1)[0] >= 3:
            break

    return rezultate_simulare


# Simulăm jocul de loto de n ori
n_simulari = 100
rezultate_totale = []

for _ in range(n_simulari):
    rezultate_totale.extend(problema2())

# 1) Lista care conține numărul de bilete necâștigătoare până la primul bilet câștigător
print("Lista numărului de bilete necâștigătoare până la primul bilet câștigător:")
print(rezultate_totale)


# 2) Estimarea probabilității evenimentului "cel puțin 10 bilete succesive sunt necâștigătoare până când jucătorul nimereste un bilet câștigător"
probabilitate_estimata = np.mean(np.array(rezultate_totale) >= 10)
print("\nEstimarea probabilității:", probabilitate_estimata)

# Calculul valorii teoretice a probabilității

p = hypergeom.pmf(3, 49, 6, 6)
probabilitate_teorica = 1 - geom.cdf(9, p)
print("Valoarea teoretică a probabilității:", probabilitate_teorica)









































# def problema2():
#     # Parametri pentru distributia hypergeometrica
#     N = 49  # Numarul total de numere posibile
#     K = 6   # Numarul de numere castigatoare
#     n = 6   # Numarul de numere extrase
#
#     # Parametri pentru distributia geometrica
#     p = hypergeom.pmf(3, N, K, n)  # Probabilitatea de a obtine cel putin 3 numere castigatoare
#     numar_simulari = 1000
#
#     # Partea 1: Generare lista cu numarul de bilete necastigatoare pana la primul bilet castigator
#     lista_bilete_necastigatoare = []
#     for _ in range(numar_simulari):
#         bilete_necastigatoare = 0
#         while True:
#             bilete_necastigatoare += 1
#             if np.random.rand() <= p:
#                 break
#         lista_bilete_necastigatoare.append(bilete_necastigatoare)
#
#     # Partea 2: Estimare probabilitatea evenimentului "cel putin 10 bilete succesive sunt necastigatoare pana cand jucatorul nimereste un bilet castigator"
#     numere_necastigatoare_pana_la_10 = np.array(lista_bilete_necastigatoare)[:10]
#     probabilitate_simulata = np.mean(numere_necastigatoare_pana_la_10 >= 10)
#
#     # Calcul teoretic pentru distributia geometrica
#     probabilitate_teorica = 1 - geom.cdf(9, p)
#
#     # Afisare rezultate
#     print("Lista cu numarul de bilete necastigatoare pana la primul bilet castigator:")
#     print(lista_bilete_necastigatoare)
#     print("\nProbabilitatea simulata pentru cel putin 10 bilete succesive necastigatoare:", probabilitate_simulata)
#     print("Probabilitatea teoretica pentru cel putin 10 bilete succesive necastigatoare:", probabilitate_teorica)



