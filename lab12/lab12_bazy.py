import numpy as np
import random
import math
from pprint import pprint

# wszystko do poprawy


def iloczyn_skalarny(v1, v2):
    # return np.dot(v1, v2)
    return np.transpose(v1) @ v2


def dlugosc_wektora(v1, v2):
    # result = abs(iloczyn_skalarny(v1, v2))
    result = iloczyn_skalarny(v1, v2)
    return math.sqrt(result)


# ma wyjsc diagonalna macierz z tego
def baza_ortoGonalna(M):
    return M.T @ M


# ma wyjsc diagonalna macierz jednostkowa ( przemnozyc przez diagonalna przez transpozycje )
def baza_ortoNormalna(M):
    M_jedn = []
    for vec in M.T:
        dlugosc = dlugosc_wektora(vec, vec)
        vec = vec / dlugosc
        M_jedn.append(vec)

    M_jedn = np.array(M_jedn)
    # return M_jedn
    # return np.round(M_jedn)
    # return np.round(baza_ortoGonalna(M_jedn))
    return np.round(baza_ortoGonalna(M_jedn), decimals=1)


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
B_diag = baza_ortoGonalna(B)
B_jedn = baza_ortoNormalna(B)

print("Baza ortogonalna:\n", B_diag)
print("Baza ortonormalna:\n", B_jedn)

# przemnozyc macierz transponowana B_jedn przez wektor R8(zeszyt)
R8 = np.array([8, 6, 2, 3, 4, 6, 6, 5])
print(B_jedn.T @ R8)
