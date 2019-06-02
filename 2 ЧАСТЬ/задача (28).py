import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
K = random.randint(1, M-1)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

A = np.delete(A, K, axis=1)
print("Новая матрица:\n {} ".format(A))