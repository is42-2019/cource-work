import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

sum_elements = np.sum(A)
sum_cols = np.sum(A, axis=1)
A = np.column_stack((A, sum_cols/sum_elements))
print("Новая матрица:\n {} ".format(A))