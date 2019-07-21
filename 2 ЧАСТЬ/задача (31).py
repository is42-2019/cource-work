import numpy as np
import random

N = np.random.randint(1, 10)
M = np.random.randint(1, 10)
K = np.random.randint(1, M)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

M_n = np.sum(A, axis=1) * (-1)
A = np.hstack((A, M_n.reshape(-1, 1)))
print("Новая матрица:\r\n{}\n".format(A))