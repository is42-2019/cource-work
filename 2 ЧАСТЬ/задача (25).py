import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
K = random.randint(1, M)
L = random.randint(1, N)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

A_bool = A == 0
col = np.sum(A_bool, axis=1)
A = np.insert(A, M, col, axis=1)
row = np.append(np.sum(A_bool, axis=0), 0)
A = np.insert(A, N, row, axis=0)
print("Новая матрица:\n {} ".format(A))