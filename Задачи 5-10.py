#Задача 5
print('Задача 5')
import numpy as np
import numpy.linalg
import numpy.matlib
arr = np.random.sample((3,4))
print(arr)
avgsto=np.average(arr, axis=0)
avgstr=np.average(arr, axis=1)
print(avgsto)
print(avgstr)
arr1=np.array([[avgsto[0],avgsto[1],avgsto[2], avgsto[3], 0],
               [0,0,0,0, avgstr[0]],
               [0,0,0,0, avgstr[1]],
               [0,0,0,0, avgstr[2]]])
print(arr1)

# Задача 6
print('Задача 6')
sum=np.sum(arr)
print(sum)
sums=np.sum(arr, axis=0)
print(sums)
sums=sums/sum
print(sums)
arr2=np.array([[sums[0],sums[1],sums[2], sums[3], 0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]])
print(arr2)

# Задача 7
print('Задача 7')
sum1=np.sum(arr)
print(sum1)
sums1=np.sum(arr, axis=1)
print(sums1)
sums1=sums1/sum1
print(sums1)
arr3=np.array([[0,0,0,0, sums[0]],
               [0,0,0,0,sums[1]],
               [0,0,0,0,sums[2]]])
print(arr3)

# Задача 8
print('Задача 8')
arr[0,1]=-5
arr[2,3]=-10
arr4=np.where(arr<0,1,0)
#np.where(arr4>0,arr4,0*arr4)
print(arr4)
otrstr=np.sum(arr4, axis=1)
otrstol=np.sum(arr4, axis=0)
arr5=np.array([[otrstol[0],otrstol[1],otrstol[2], 0, 0],
               [0,0,0,0,otrstr[0]],
               [0,0,0,0,otrstr[1]],
               [0,0,0,0,otrstr[2]]])
print(arr5)




