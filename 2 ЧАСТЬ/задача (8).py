import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
A = np.random.randint(-100, 100, (N, M))
print("Матрица:\r\n{}".format(A))

A_bool = A < 0
num_cols = np.sum(A_bool, axis=0)
num_rows = np.sum(A_bool, axis=1)
A = np.vstack((A, [num_cols]))
A = np.column_stack((A, np.append(num_rows, 0)))
print("Новая матрица:\n {} ".format(A))