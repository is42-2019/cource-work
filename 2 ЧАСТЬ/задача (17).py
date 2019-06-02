import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
L = random.randint(1, M)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

row = np.random.randint(-9, 10, M)
print("Строка для вставки: {}".format(row))
A = np.insert(A, L, row, axis=0)
print("Новая матрица:\n {} ".format(A))