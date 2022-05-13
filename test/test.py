import numpy as np
import random
import math

# v1 = np.array([random.randint(0, 10) for _ in range(5)])
# v2 = np.array([random.randint(0, 10) for _ in range(5)])

v1 = [2, 0, 1]
v2 = [0, 1, 2]


def dot_product_for_vectors(v1, v2):
    if len(v1) != len(v2):
        return "Vectors dont have the same lengths"

    result = 0
    for i, j in zip(v1, v2):
        result += i * j
    return result


print(dot_product_for_vectors(v1, v2))


M1 = np.random.randint(10, size=(4, 6))
M2 = np.random.randint(10, size=(4, 6))


def dot_products_for_matrices(M1, M2):
    if len(M1) != len(M2) or len(M1[0]) != len(M2[0]):
        raise "Matrices dont have the same lengths of rows or columns"
    results = []
    for v1, v2 in zip(M1, M2):
        results.append(dot_product_for_vectors(v1, v2))
    return results


# print(dot_products_for_matrices(M1, M2))


# code challenge 2
print(dot_product_for_vectors(v1, v2))
print(dot_product_for_vectors(5 * v1, 3 * v2))

# print(v1 @ 2)
print(np.transpose(v1) @ v2)
print(np.transpose([2 * x for x in v1]) @ [3 * x for x in v2])


def vector_length(v):
    return math.sqrt(np.transpose(v) @ v)


print(vector_length(v1))
