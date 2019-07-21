import numpy as np
import random

N = np.random.randint(1, 10)
M = np.random.randint(1, 10)
K = np.random.randint(1, N)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

M_n = np.sum(A, axis=0) * (-1)
A = np.vstack((A, M_n))
print("Новая матрица:\r\n{}\n".format(A))