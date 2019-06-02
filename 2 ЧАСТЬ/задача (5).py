import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

average_rows = np.average(A, axis=1)
average_cols = np.average(A, axis=0)
A = np.vstack((A, [average_cols]))
A = np.column_stack((A, np.append(average_rows, 0)))
print("Новая матрица:\n {} ".format(A))