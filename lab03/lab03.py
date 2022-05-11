import math
from pprint import pprint
import numpy as np
import random

# https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/australian/
lista = []
with open("../australian.dat", "r") as file:
    for line in file:
        # lista.append(line.split())
        # lista.append(list(map(lambda x: float(x), line.split())))
        lista.append(list(float(x) for x in line.split()))


def metryka_euklidesowa(arr1, arr2):
    # return math.sqrt(sum((val1 - val2) ** 2 for val1, val2 in zip(arr1, arr2)))
    suma = 0
    for i in range(len(arr1) - 1):
        suma += (arr1[i] - arr2[i]) ** 2
    return math.sqrt(suma)


"""
obliczyc odleglosci pomiedzy ?
0 1 = 1213 ?
0 2 = 1225 ?
0 3 = 1216,03 ?
"""
print(metryka_euklidesowa(lista[0], lista[1]))
print(metryka_euklidesowa(lista[0], lista[2]))
print(metryka_euklidesowa(lista[0], lista[3]))


"""
DO DOMU
zad 1
policz odleglosc y do wszystkich x gdzie x nalezy do tej listy bez
elementu z indexem 0
zrobic SLOWNIK klucz i wartosc ,kluczem ma byc klasa decyzyjna x,
a wartoscia ma byc lista z odleglosciami
np; gdy klasa dec jest 0, wiec do listry trafiaja
czyli wartosci z
czyli po obliczonej wartości z a), wrzucamy go do dic gdzie jego klucz
to 1 czy 0
"""


def zad1(matrix, y) -> tuple[list[float], dict[float, list[float]]]:
    odleglosci = []
    slownik = {1.0: [], 0.0: []}
    for vec in matrix:
        klucz = vec[0]
        klasa_decyzyjna = vec[-1]
        # slownik.update({klasa_decyzyjna: []}) # naprawic to ponieważ TO nadpisuje pustą listą poprzednią listę z wartością!@!@

        if klucz != 0:
            odleglosci.append(metryka_euklidesowa(matrix[y], vec))
            slownik.setdefault(klasa_decyzyjna, []).append(odleglosci[-1])
            # slownik[klasa_decyzyjna].append(odleglosci[-1])

    # for vec in matrix:
    #     odleglosci.append(metryka_euklidesowa(matrix[y], vec))
    #     slownik.setdefault(vec[0], []).append(odleglosci[-1])

    return odleglosci, slownik


odleglosci, slownik = zad1(lista, 0)
print(slownik[1.0][0])
print(min(odleglosci))

"""
zad 2
napisz funkcje ktora oblicza wyznacznik macierzy kwadratowej
https://integratedmlai.com/find-the-determinant-of-a-matrix-with-pure-python-without-numpy-or-scipy/
"""


def wyznacznik_recursive(matrix):
    if len(matrix) != len(matrix[0]):
        raise "Nie jest to macierz kwadratowa"

    suma = 0
    if len(matrix) == 2 and len(matrix[0]) == 2:
        val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return val

    for col in range(len(matrix[0])):
        sub_matrix = matrix[1:]
        for row in range(len(sub_matrix)):
            sub_matrix[row] = sub_matrix[row][0:col] + sub_matrix[row][col + 1 :]

        znak = (-1) ** (col % 2)
        suma += znak * matrix[0][col] * wyznacznik_recursive(sub_matrix)

    return suma


n = 3
A = [[random.randint(0, 3) for _ in range(n)] for _ in range(n)]
pprint(A)
print(f"Wyznacznik wynosi:", wyznacznik_recursive(A))

# albo
print(np.linalg.det(A))
