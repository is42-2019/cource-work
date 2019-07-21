import numpy as np

for i in range(1, 6):
    task_file = "СЛАУ_" + str(i) + ".csv"
    m = np.genfromtxt(task_file, delimiter=';')
    A = np.genfromtxt(task_file, delimiter=';', usecols=(range(len(m-1))))
    B = np.genfromtxt(task_file, delimiter=';', usecols=(len(m)))
    slau = np.linalg.solve(A, B)
    print("Решение" + str(i), slau)