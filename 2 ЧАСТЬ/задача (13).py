import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

max = np.max(A, axis=0)
A = A / max
print("Новая матрица:\n {} ".format(A))