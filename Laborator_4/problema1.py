from scipy.stats import bernoulli
from matplotlib.pyplot import show, hist, xticks


def deplasare(nr_pasi):
    poz = 0
    lista = []
    while nr_pasi > 0:
        if bernoulli.rvs(0.5) == 1:
            poz += 1
        else:
            poz -= 1
        lista.append(poz)
        nr_pasi -= 1
    return lista


def deplasare_cerc(nr_pasi, nr_noduri):
    poz = 0
    lista = []
    while nr_pasi > 0:
        if bernoulli.rvs(0.5) == 1:
            poz += 1
            if poz > nr_noduri:
                poz = 0
        else:
            poz -= 1
            if poz < 0:
                poz = nr_noduri - 1
        lista.append(poz)
        nr_pasi -= 1
    return lista


def histograma(nr_pasi):
    data = []
    for i in range(1000):
        data.append(deplasare(nr_pasi)[-1])
    bin_edges = [k + 0.5 for k in range(-nr_pasi - 1, nr_pasi + 1)]
    hist(data, bins=bin_edges, density=True, rwidth=0.9, color='green', edgecolor='black')
    xticks(range(-nr_pasi, nr_pasi + 1))
    show()


def histograma_cerc(nr_pasi, nr_noduri):
    data = []
    for i in range(1000):
        data.append(deplasare_cerc(nr_pasi, nr_noduri)[-1])
    bin_edges = [k + 0.5 for k in range(-nr_pasi - 1, nr_pasi + 1)]
    hist(data, bins=bin_edges, density=True, rwidth=0.9, color='green', edgecolor='black')
    xticks(range(-nr_pasi, nr_pasi + 1))
    show()


def problema1():
    # print(bernoulli.rvs(0.25, size=1000))
    print("Deplasare de 1000 de pasi: ")
    print(deplasare(1000))
    histograma(10)
    histograma_cerc(10, 5)
