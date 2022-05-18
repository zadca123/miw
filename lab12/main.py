import numpy as np
import random
import math
from pprint import pprint

# wszystko do poprawy


def iloczyn_skalarny(v1, v2):
    # return np.dot(v1, v2)
    return np.transpose(v1) @ v2


def dlugosc_wektora(v1, v2):
    result = abs(iloczyn_skalarny(v1, v2))
    return math.sqrt(result)


# ma wyjsc diagonalna macierz z tego
def baza_ortoGonalna(M):
    rows, cols = len(M), len(M[0])
    result = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            result[i][j] = dlugosc_wektora(M[i], M[:, j : j + 1])

    return result


# ma wyjsc diagonalna macierz jednostkowa ( przemnozyc przez diagonalna przez transpozycje )
def baza_ortoNormalna(M):
    return baza_ortoGonalna(M) @ M.T


# normalizacja, (podzielic przez dlugosc vektora)
def baza_znormalizowana(M):
    result = baza_ortoNormalna(M)
    for i in range(len(result)):
        dl = dlugosc_wektora(result[i], result[i])
        for j in range(len(result[0])):
            result[i][j] = result[i][j] / dl

    return result


# przemnozyc macierz transponowana BT przez wektor R8(zeszyt)
def foo():
    pass


BT = np.array(
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, -1, -1, -1, -1],
        [1, 1, -1, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, -1, -1],
        [1, -1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, -1],
    ]
)
B = BT.T
print("Baza ortogonalna:\n", baza_ortoGonalna(B))
print("Baza ortonormalna:\n", baza_ortoNormalna(B))
print("Baza znormalizowana:\n", baza_znormalizowana(B))
# print(B)

# x1 = np.array([8, 6, 2, 3, 4, 6, 6, 5])
# result = np.array(size=matrice.shape)
# print(result)
