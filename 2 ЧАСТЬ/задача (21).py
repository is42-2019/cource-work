import numpy as np
import random

N = random.randint(1, 10)

A = np.random.randint(0, 100, (N, N))
print("Матрица:\r\n{}".format(A))

for i in range(1, N-1):
    b = (A[i+1, i-1] + A[i-1, i+1])/2
    A[i+1, i-1] = b
    A[i-1, i+1] = b
print("Новая матрица:\n {} ".format(A))