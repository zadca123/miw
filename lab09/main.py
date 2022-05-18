import numpy as np
import math


def iloczyn_skalarny(v):
    return np.transpose(v) @ v


def dlugosc_wektora(v):
    return math.sqrt(iloczyn_skalarny(v))


def pomnoz_przez_skalar(skalar, v):
    for i in range(len(v)):
        v[i] *= skalar

    # wynik = np.array(map(lambda x: x * skalar, v))
    # wynik = [skalar*x for x in v]
    return v


def proj(v, u):
    return (np.transpose(v) @ u / (np.transpose(u) @ u)) * u


def create_e(v):
    return v / dlugosc_wektora(v)


def create_u(v, u):
    return v - proj(v, u)


def create_Q(*args, **kwargs):
    matrice = np.array(args[0])
    for arg in args[1:]:
        matrice = np.append(matrice, arg)

    return matrice


def create_R(Q, A):
    return Q.T @ A


A = np.array([[1, 1, 0], [0, 1, 1]])
x = np.array(A[0])
print(iloczyn_skalarny(x))
print(dlugosc_wektora(x))


v1 = u1 = np.array([1, 2, 3])
v2 = np.array([3, 2, 1])
e1 = create_e(u1)
u2 = create_u(v2, u1)
e2 = create_e(u2)
Q = create_Q(e1, e2)
print(Q.T)
print(A)
print(A.T @ A)
# print(create_R(Q, A))
