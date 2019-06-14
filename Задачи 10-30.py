#Задача 10
print('Задача 10')
import numpy as np
import numpy.linalg
import numpy.matlib
arr = np.random.sample((3,4))
print(arr)
k=2
arr1=np.array([arr[0,k],arr[1,k],arr[2,k]])
print(arr1)
for i in range(3):
    for j in range(4):
        arr[i,j]=arr[i,j]*arr1[i]
print(arr)

#Задача 11
print("_________________________________________________")
print('Задача 11')
k=2
for i in range(3):
    for j in range(4):
        arr[i,j]=arr[i,j]+arr[k,j]
print(arr)

#Задача 12
print("_________________________________________________")
print('Задача 12')
arr1=np.max(arr, axis=1)
for i in range(3):
    for j in range(4):
        arr[i,j]=arr[i,j]/arr1[i]
print(arr)

#Задача 13
print("_________________________________________________")
print('Задача 13')
arr1=np.max(arr, axis=0)
print(arr1)
for j in range(4):
    for i in range(3):
        arr[i,j]=arr[i,j]/arr1[j]
print(arr)

#Задача 14
print("_________________________________________________")
print('Задача 14')
m=np.max(arr)
print('Максимальный элемент=',m)
arr=arr/m
print(arr)

#Задача 15
print("_________________________________________________")
print('Задача 15')
m=3
n=4
arr2=np.arange(m*n).reshape(m,n)
print(arr2)
h=2
l1=np.where(arr2==h,1,0)
L2=np.count_nonzero(l1, axis=0)
L3=np.where(L2>0,'есть','нет')
print(L3)



#Задача 16
print("_________________________________________________")
print('Задача 16')
m=3
n=4
arr2=np.arange(m*n).reshape(m,n)
print(arr2)
k=2
L=np.vsplit(arr2,(k-1,k))
print(L)
arr3=np.vstack((L[0],L[2]))
print(arr3)

#Задача 17
print("_________________________________________________")
print('Задача 17')
arr = np.random.sample((3,4))
print(arr)
arr1=np.append(arr,[[0,0,0,0]], axis=0)
print(arr1)

#Задача 18
print("_________________________________________________")
print('Задача 18')
arr = np.random.sample((4,4))
print(arr)
arr1=np.diag(arr)
print(arr1)
sum=np.sum(arr1)
print('Сумма элементов главной диагонали=', sum)
for i in range(4):
    k=arr[i,j]
    arr[i,i]=arr[n-i-1,i]
    arr[n - i - 1, i]=k
print(arr)
arr2=np.diag(arr)
sum2=np.sum(arr2)
print('Сумма элементов побочной диагонали=', sum2)

#Задача 19
print("_________________________________________________")
print('Задача 19')
arr = np.random.sample((4,4))
print(arr)
arr2=np.diag(arr,k=1)
sum1=np.sum(arr2)
arr3=np.diag(arr, k=-1)
sum2=np.sum(arr3)
print('Сумма элементов первой диагонали=', sum1)
print('Сумма элементов второй диагонали=', sum2)

#Задача 20
print("_________________________________________________")
print('Задача 20')
arr = np.random.sample((4,4))
print(arr)
arr=np.fliplr(arr)
print(arr)
arr2=np.diag(arr,k=1)
sum1=np.sum(arr2)
arr3=np.diag(arr, k=-1)
sum2=np.sum(arr3)
print('Сумма элементов первой диагонали=', sum1)
print('Сумма элементов второй диагонали=', sum2)

#Задача 21
print("_________________________________________________")
print('Задача 21')
arr = np.random.sample((4,4))
print(arr)
arr2=np.diag(arr,k=1)
arr3=np.diag(arr, k=-1)
arrsum=(arr2+arr3)/2
print(arrsum)
arr[1,0]=arrsum[0]
arr[0,1]=arrsum[0]
arr[2,1]=arrsum[1]
arr[1,2]=arrsum[1]
arr[3,2]=arrsum[2]
arr[2,3]=arrsum[2]
print('Новая матрица')
print(arr)

#Задача 22
print("_________________________________________________")
print('Задача 22')
arr = np.random.randint(0,2, size=(3,4))
print(arr)
sum=np.sum(arr, axis=1)
print(sum)
arr1=np.where(sum%2!=0,1,0)
print(arr1)
arr=np.append(arr,[[arr1[0]],[arr1[1]],[arr1[2]]],axis=1)
print('Новая матрица')
print(arr)

#Задача 23
print("_________________________________________________")
print('Задача 23')
arr = np.random.sample((4,4))
print(arr)
arr1=np.triu(arr)
print(arr1)
sum=np.sum(arr1)
print('Сумма элементов выше главной диагонали=',sum)
arr=np.fliplr(arr)
arr1=np.triu(arr)
p=1
print(arr1)
for i in range(4):
    for j in range(4):
        if arr1[i,j]!=0:
            p=p*arr1[i,j]
print('Произведение элементов выше побочной диагонали=',p)

#Задача 24
print("_________________________________________________")
print('Задача 24')
arr = np.random.randint(0,2, size=(3,4))
print(arr)
k=2
m=2
arr2=arr[0:k,0:m]
arr3=arr[0:k,m:4]
arr4=arr[k:4,0:m]
arr5=arr[k:4,m:4]
print(arr2)
print(arr3)
print(arr4)
print(arr5)
sum1=np.sum(arr2)
sum2=np.sum(arr3)
sum3=np.sum(arr4)
sum4=np.sum(arr5)
print('Сумма элементов первого массива=',sum1)
print('Сумма элементов второго массива=',sum2)
print('Сумма элементов третьего массива=',sum3)
print('Сумма элементов четвертого массива=',sum4)

#Задача 26
print("_________________________________________________")
print('Задача 26')
arr = np.random.randint(0,2, size=(3,4))
print(arr)
k=2
m=2
arr2=arr[0:k,0:m]
arr3=arr[0:k,m:4]
arr4=arr[k:4,0:m]
arr5=arr[k:4,m:4]
print(arr2)
print(arr3)
print(arr4)
print(arr5)
sum1=np.average(arr2)
sum2=np.average(arr3)
sum3=np.average(arr4)
sum4=np.average(arr5)
print('Среднее значение элементов первого массива=',sum1)
print('Среднее значение элементов второго массива=',sum2)
print('Среднее значение элементов третьего массива=',sum3)
print('Среднее значение элементов четвертого массива=',sum4)


