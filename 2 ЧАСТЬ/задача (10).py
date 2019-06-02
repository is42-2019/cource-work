import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
K = random.randint(1, M)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

a = A[:, K]
a = a.reshape(len(a), 1)
A = A * a
print("Новая матрица:\n {} ".format(A))