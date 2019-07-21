import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

sum_e = np.sum(A)
sum_c = np.sum(A, axis=0)
A = np.vstack((A, [sum_c/sum_e]))
print("Новая матрица:\n {} ".format(A))