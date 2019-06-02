import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
K = random.randint(1, M)
L = random.randint(1, N)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

parts = [
    A[:L, :K],
    A[:L, K:],
    A[L:, :K],
    A[L:, K:],]
for i in range(len(parts)):
    print("Cумма элементов {} части: {}".format(i+1, np.sum(parts[i])))