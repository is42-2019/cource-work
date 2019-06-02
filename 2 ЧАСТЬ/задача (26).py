import numpy as np
import random

N = random.randint(1, 10)
M = random.randint(1, 10)
K = random.randint(1, M-1)
L = random.randint(1, N-1)

A = np.random.randint(0, 100, (N, M))
print("Матрица:\r\n{}".format(A))

parts = [
    A[:L, :K],
    A[:L, K:],
    A[L:, :K],
    A[L:, K:],]
for i in range(len(parts)):
    print("Cреднее арифметическое {} части: {}".format(i+1, np.average(parts[i])))