import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
H = random.randint(1, M-1)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))
A_bool = A == H
col_sum = np.sum(A_bool, axis=1)
print("Строки в которых встречается значение {}:".format(H))
print(np.argwhere(col_sum).flatten())
print("Строки в которых нет значения {}:".format(H))
print(np.argwhere(col_sum == 0).flatten())