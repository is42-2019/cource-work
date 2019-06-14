# Задача 1
print('Задача 1')
import numpy as np
import numpy.linalg
import numpy.matlib
arr = np.random.sample((3,4))
print(arr)
sums=np.sum(arr, axis=0)
print(sums)
row_index=np.argmax(sums, axis=0)
print(row_index)
print(sums[row_index])
arr0=arr.transpose()
el=np.max(arr0[row_index])
print(el)

# Задача 2
print('Задача 2')
avg=np.average(arr, axis=1)
print(avg)
row_index1=np.argmax(avg, axis=0)
print(row_index1)
print(avg[row_index1])
el1=np.max(arr[row_index1])
print(el1)

# Задача 3
print('Задача 3')
#arrt=arr.transpose()
arrt =np.abs(arr)
sum1=np.sum(arrt, axis=0)
print(sum1)
row_index2=np.argmax(sum1)
print(row_index2)
arrt0=arrt.transpose()
el2=np.min(arrt0[row_index2])
print(el2)

# Задача 4
print('Задача 4')
avg2= np.average(arr, axis=1)
print(avg2)
el3=np.min(avg2)
print(el3)







