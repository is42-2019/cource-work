import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
L = random.randint(1, N)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

A = A + A[L]
print("Новая матрица:\n {} ".format(A))