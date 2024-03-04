from random import randrange

from scipy.stats import binom

from Problema_1 import problema1
from Problema_2 import problema2
from Problema_3 import  simulare25, histograma_trei
from Problema_4 import problema4

if __name__ == "__main__" :
    #problema1()
    # problema2()

    # Problema 3
    # alegeriX = [randrange(0, 6) for _ in range(100000)]
    # pb = 0.6  # de a alege o bila cu valoarea 1
    # nr = 5
    # print("Probabilitatea simulata:")
    # print(simulare25(alegeriX))
    # Prob_calc = binom.cdf(5, nr, pb) - binom.cdf(2, nr, pb)
    # print("Probabilitate tehnica:")
    # print(Prob_calc)
    # histograma_trei(alegeriX)

    problema4()


