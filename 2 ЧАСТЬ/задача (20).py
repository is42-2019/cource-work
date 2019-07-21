import numpy as np
import random

N = random.randint(1, 10)

A = np.random.randint(0, 100, (N, N))
print("Матрица:\r\n{}".format(A))

a = b = np.fliplr(A).diagonal(1)
a_prod = a.prod()
print("Элементы которые выше побочной диагонали: \n" + str(a) + "\nИх сумма = " + str(a_prod))

b = np.fliplr(A).diagonal(-1)
b_prod = b.prod()
print("Элементы которые ниже побочной диагонали: \n" + str(b) + "\nИх сумма = " + str(b_prod))