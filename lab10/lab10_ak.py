import math
import random
import numpy as np


def proj_v_u(v, u):
    return (np.transpose(v) @ u / (np.transpose(u) @ u)) * u


def oblicz_e_n(u):
    return u / math.sqrt(np.transpose(u) @ u)


def rozklad_Q_R(A):
    Q = []
    wyniki_u = []
    wyniki_e = []
    for i in range(len(A[0])):
        suma = 0
        v = np.array(A[:, i]).reshape((len(A), 1))

        for j in range(i):
            suma += proj_v_u(v, wyniki_u[j])

        u = v - suma
        e = oblicz_e_n(u)

        wyniki_u.append(u)
        wyniki_e.append(e)

        Q.append(e[:, 0])

    Q = np.array(Q).T
    R = Q.T @ A
    return Q, R


def rozklad_A_K(A, k):
    if len(A) != len(A[0]):
        raise "Macierze nie jest kwadratowa!!!"

    matrice = A
    for _ in range(k):
        Q, R = rozklad_Q_R(matrice)
        matrice = np.linalg.inv(Q) * matrice * Q

    return matrice


# A = np.array(
#     [
#         [1, 1, 1],
#         [1, 0, 0],
#         [1, 0, 1],
#     ]
# )
# A = np.array([
#     [1,0],
#     [1,1],
#     [0,1],
# ])
# A = np.array(
#     [
#         [2, 0],
#         [0, 1],
#         [1, 2],
#     ]
# )


# czasami dziala czasami nie na tej macierzy... idk
n = 2
A = np.random.randint(0, 3, size=(n, n), dtype=np.uint8)
print(A)

Q, R = rozklad_Q_R(A)
print(Q, R)
print(Q @ R)
print(rozklad_A_K(A, 5))
