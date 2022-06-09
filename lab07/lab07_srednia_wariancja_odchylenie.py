import numpy as np
import math
import matplotlib.pyplot as plt
from pprint import pprint
from itertools import combinations

australia = []
with open("../australian.dat", "r") as file:
    for line in file:
        australia.append(list(map(lambda x: float(x), line.split())))

"""
Praca Domowa.
W oparciu o operacje wektorowe proszę napisać funkcję do obliczania średniej arytmetycznej oraz wariancji i odchylenia standardowego
"""


def srednia_arytmetyczna(x):
    return sum(x[:-1]) / (len(x) - 1)


def wariancja(x):
    m = sum(x) / len(x)
    var = sum((i - m) ** 2 for i in x) / len(x)
    return var


def kowariancja(x, y):
    m = sum(x) / len(x)
    m2 = sum(y) / len(y)
    return sum([(xi - m) * (yi - m2) for xi, yi in zip(x, y)]) / (len(x) - 1)


def odchylenie_standardowe(x):
    n = len(x)
    mean = sum(x) / n
    var = sum((i - mean) ** 2 for i in x) / n
    odchylenie_standardowe = var ** 0.5
    return odchylenie_standardowe


# print(australia)
print(srednia_arytmetyczna(australia[0]))
print(wariancja(australia[0]))
print(odchylenie_standardowe(australia[0]))
print()

# australia = [1,2,3]


def new_srednia_arytmetyczna(x):
    # return (np.array(x) * np.dot(x,x)) / len(x)
    return (np.transpose(x) * np.dot(x, x)) / len(x)


def new_wariancja(x):
    """wariancja"""
    srednia = sum(x) / len(x)
    var = sum((i - srednia) ** 2 for i in x) / len(x)
    return var


def new_odchylenie_standardowe(x):
    """odchylenie standardowe"""
    n = len(x)
    mean = sum(x) / n
    var = sum((i - mean) ** 2 for i in x) / n
    odchylenie_standardowe = var ** 0.5
    return odchylenie_standardowe


print(new_srednia_arytmetyczna(australia[0]))
print(new_wariancja(australia[0]))
print(new_odchylenie_standardowe(australia[0]))
