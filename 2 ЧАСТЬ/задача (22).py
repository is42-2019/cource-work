import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)

A = np.random.randint(0, 2, (N, M))
print("Матрица:\r\n{}".format(A))


a = [i % 2 for i in np.sum(A, axis=1)]
A = np.insert(A, M, a, axis=1)
print("Новая матрица:\n {} ".format(A))