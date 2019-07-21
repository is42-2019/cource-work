import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
H = random.randint(1, 10)

A = np.random.randint(0, 10, (N, M))
print("Матрица:\r\n{}".format(A))

A_bool = A == H
row_sum = np.sum(A_bool, axis=0)
print("Столбцы в которых встречается значение {}:".format(H))
print(np.argwhere(row_sum).flatten())
print("Столбцы в которых нет значения {}:".format(H))
print(np.argwhere(row_sum == 0).flatten())