import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
K = random.randint(1, M)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

col = np.random.randint(-9, 10, N)
print("Столбец для вставки: {}".format(col))
A = np.insert(A, K, col, axis=1)
print("Новая матрица:\n {} ".format(A))