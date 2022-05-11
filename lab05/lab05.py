import math
import numpy as np
from pprint import pprint
import random
import matplotlib.pyplot as plt

#############################################
################ LAB 4 ######################
#############################################

# https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/australian/
lista = []
with open("../australian.dat", "r") as file:
    for line in file:
        lista.append(list(float(x) for x in line.split()))


def metryka_euklidesowa(arr1, arr2):
    suma = 0
    for i in range(len(arr1) - 1):
        suma += (arr2[i] - arr1[i]) ** 2
        # suma += (arr1[i] - arr2[i]) ** 2
    return math.sqrt(suma)


def pary(row, matrix):
    odleglosci = []
    # row = [1 for _ in range(14)]  # ???

    # for x in range(len(matrix)):
    #     klasa_decyzyjna = matrix[x][-1]
    #     para = klasa_decyzyjna, metryka_euklidesowa(matrix[row], matrix[x])
    #     odleglosci.append(para)

    for item in matrix:
        klasa_decyzyjna = item[-1]
        odl = metryka_euklidesowa(row, item)
        para = klasa_decyzyjna, odl
        odleglosci.append(para)

    return odleglosci


def zad2(lista_par):
    slownik = {}
    for klasa, metryka in lista_par:
        slownik.setdefault(klasa, []).append(metryka)
    return slownik


def zad3(slownik1, k):
    slownik2 = {}
    for key, val in slownik1.items():
        val.sort()
        slownik2.update({key: sum(val[:k])})
    return slownik2


punkt_x = [1 for _ in range(14)]
lista_par = pary(punkt_x, lista)
# lista_par = pary(lista[0], lista)
var2 = zad2(lista_par)
var3 = zad3(var2, 3)

#############################################
################ LAB 5 ######################
#############################################


# """
# PRACA DOMOWA
# zad 1
# jak obliczyc metryke euklidesowo dla dwoch obiektów korzystajac z wektorów i operacji na wektorach
# """


def metryka_euklidesowav2(matrix1, matrix2):
    suma = 0
    for arr1, arr2 in zip(matrix1, matrix2):
        for val1, val2 in zip(arr1[:-1], arr2[:-1]):
            suma += (val1 - val2) ** 2
            # suma += (arr1[i] - arr2[i]) ** 2
    return math.sqrt(suma)


lista2 = []
with open("../australian.dat", "r") as file:
    for line in file:
        lista2.append(list(float(x) + 5 for x in line.split()))
# print(metryka_euklidesowav2(lista, lista2))

"""
NA LEKCJI
knn? ogarnąć co to jest..!!!
def zad3v2(slownik1, k):
te zadanie ma byc...
slownik2 = {}
for key, val in slownik1.items():
slownik2.update({key: sum(val[:k])})
return slownik2
print(zad3v2(var2,3))
"""


def metryka_euklidesowa2(arr1, arr2, decision=False):
    if decision == False:
        arr1 = np.array(arr1)
        arr2 = np.array(arr2)
    else:
        arr1 = np.array(arr1[:-1])
        arr2 = np.array(arr2[:-1])
    # v = arr2 - arr1 # wydaje się że nie ma różnicy
    v = arr1 - arr2  # wydaje się że nie ma różnicy
    return math.sqrt(np.dot(v, v))


# print(metryka_euklidesowa(lista[0], lista[3]))
# print(metryka_euklidesowa2(lista[0], lista[3], True))

# 28 lutego, godz 1.10 wykładu, to jest mówione teraz na lekcji


def odleglosc_kropek():
    """oblicz odleglosc kropki od pogrupowacc..."""

    pass


"""praca domowa

zad: program który będzie całkował (oznaczona??)
1. metoda monte carlo(okreslic maximum w przedziale)
2. metoda trapezu lub prostokataw
3. metoda srodki masy i kolorowanie
"""
