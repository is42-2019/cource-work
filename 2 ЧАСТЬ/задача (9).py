import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
K = random.randint(1, M)
L = random.randint(1, N)

A = np.random.randint(0, 2, (N, M))
print("Матрица:\r\n{}".format(A))

A_slice = A[:L, :K]
print("Срез:\r\n{}".format(A_slice))
slice_bool = A_slice == 0
zero_elements = slice_bool.sum()
print("Количество элементов:\n {} ".format(zero_elements))