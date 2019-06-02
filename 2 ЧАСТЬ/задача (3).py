import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

sum = A.sum(axis=0)
i = sum.argmin(axis=0)
min = A.min(axis=0)
min = min[i]
print("Минимальный элемент: {}".format(min))