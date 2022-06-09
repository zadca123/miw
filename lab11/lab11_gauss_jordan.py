import numpy as np
import random
import math

# https://www.codesansar.com/numerical-methods/gauss-jordan-method-python-program-output.htm
def gauss_jordan_elimination(A):  # Applying Gauss Jordan Elimination
    # A = np.insert(A, len(A), np.ones(n), axis=1)E
    n = len(A)

    if n > len(A[0]):
        raise "Mniejsza badz równa liczba kolumn co do wierszy"

    for i in range(n):
        if A[i][i] == 0.0:
            raise "Dzielenie przez zero!!!"

        for j in range(n):
            if i != j:
                ratio = A[j][i] / A[i][i]
                for k in range(n + 1):
                    A[j][k] = A[j][k] - ratio * A[i][k]

    wynik = np.zeros(n)
    for i in range(n):
        wynik[i] = A[i][n] / A[i][i]

    return wynik


n = 100
A = [[random.randint(1, 10) for _ in range(n + 1)] for _ in range(n)]
gauss = gauss_jordan_elimination(A)
for i, val in enumerate(gauss):
    print(f"X{i} = {val}")
