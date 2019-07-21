import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

Average = A.mean(axis=1)
index = Average.argmin(axis=0)
min = Average.min(axis=0)
print("Наименьшее значение среди средних значений: {}".format(min))