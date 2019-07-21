import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
L = random.randint(1, M)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

diagonal_main = np.diagonal(A)
print("Элементы главной диагонали:\r\n{}".format(diagonal_main))
sum_diagonal_main = np.sum(diagonal_main)
print("Cумма элементов главной диагонали:\r\n{}".format(sum_diagonal_main))
diagonal_side = np.diagonal(A[::-1])
print("Элементы побочной диагонали:\r\n{}".format(diagonal_side))
sum_diagonal_side = np.sum(diagonal_side)
print("сумму элементов побочной диагонали:\r\n{}".format(sum_diagonal_side))