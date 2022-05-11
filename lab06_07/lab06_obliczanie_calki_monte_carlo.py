import random
import numpy as np
import math


def monte_carlo1(func, a=0, b=np.pi, N=100):
    # wektor z rand liczbami z przedzialu (a,b) o wielkosci N
    ar = np.array([random.uniform(a, b) for _ in range(N)])

    # zmienna przechowujaca sume funkcji na elementach ar
    integral = sum((func(x) for x in ar))

    wynik = (b - a) / float(N) * integral

    print(f"Wynik operacji monte carlo: {wynik}.")


def func(x):
    return x


monte_carlo1(func, 0, 1, 100)
# y = x; wynik powinien być 0.5
