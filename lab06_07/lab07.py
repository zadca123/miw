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


def arithmetic_average(x):
    """srednia arytmetyczna"""
    return sum(x[:-1]) / (len(x) - 1)
    # suma = 0
    # for i in x:
    #     suma += i
    # # return suma / len(x) if x else 0
    # return suma / len(x)


def daml_var(x):
    """wariancja"""
    m = sum(x) / len(x)
    var = sum((i - m) ** 2 for i in x) / len(x)
    return var


def daml_cov(x, y):
    """cowariancja"""
    m = sum(x) / len(x)
    m2 = sum(y) / len(y)
    return sum([(xi - m) * (yi - m2) for xi, yi in zip(x, y)]) / (len(x) - 1)


def std_dev(ls):
    """odchylenie standardowe"""
    n = len(ls)
    mean = sum(ls) / n
    var = sum((x - mean) ** 2 for x in ls) / n
    std_dev = var**0.5
    return std_dev


# print(australia)
print(arithmetic_average(australia[0]))
print(daml_var(australia[0]))
print(std_dev(australia[0]))
print()

# australia = [1,2,3]


def new_arithmetic_average(x):
    return (np.transpose(x) * np.dot(x)) / len(x)
    # return (np.array(x) * np.dot(x)) / len(x)


def new_daml_var(x):
    """wariancja"""
    srednia = sum(x) / len(x)
    var = sum((i - srednia) ** 2 for i in x) / len(x)
    return var


def new_std_dev(ls):
    """odchylenie standardowe"""
    n = len(ls)
    mean = sum(ls) / n
    var = sum((x - mean) ** 2 for x in ls) / n
    std_dev = var**0.5
    return std_dev


# print(new_arithmetic_average(australia[0])) # poprawic
print(new_daml_var(australia[0]))
print(new_std_dev(australia[0]))  # dokonczyc w domu
