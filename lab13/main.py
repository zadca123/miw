import numpy as np
from numpy.linalg import eigh, norm

A = np.array([[-5, 2, 3], [2, 5, 1], [-3, 1, -5]])

print(A)

ev, V = eigh(A.T @ A)

u0 = A @ V[:, 0] / norm(A @ V[:, 0])
u1 = A @ V[:, 1] / norm(A @ V[:, 1])
u2 = A @ V[:, 2] / norm(A @ V[:, 2])

print(ev, V, u0, u1, u2)

U = np.array([u0, u1, u2]).T
D = U.T @ A @ V

print(A)
print(U @ D @ V.T)
