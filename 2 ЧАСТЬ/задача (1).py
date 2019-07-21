import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

sum = A.sum(axis=0)
i = sum.argmax(axis=0)
max = A.max(axis=0)
max = max[i]
print("Наибольший элемент: {}".format(max))