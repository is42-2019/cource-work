import numpy as np
import random

N = random.randint(1, 10)

A = np.random.randint(0, 100, (N, N))
print("Матрица:\r\n{}".format(A))

a = np.diagonal(A, 1)
a_sum = a.sum()
print("Элементы которые выше главной диагонали: \n" + str(a) + "\nИх сумма = " + str(a_sum))
b = np.diagonal(A, -1)
b_sum = b.sum()
print("Элементы которые ниже главной диагонали: \n" + str(b) + "\nИх сумма = " + str(a_sum))