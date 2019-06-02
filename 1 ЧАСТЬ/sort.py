import select
import bubble
import insert
import random

dim = 40
bubble_arr = []
insert_arr = []
select_arr = []

CTotal = [0, 0, 0]
MTotal = [0, 0, 0]

for i in range(1, dim+1):
    select_arr.append(i)
    bubble_arr.append(i)
    insert_arr.append(i)

print("\nУПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ:")
print(select_arr)

count = [0, 0]
count = select.select(select_arr, dim)
print("\nУПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ:")
print(select_arr)
CTotal[0] = count[0]
MTotal[0] = count[1]

count = [0, 0]
count = insert.insert(insert_arr, dim)
CTotal[1] = count[0]
MTotal[1] = count[1]

count = [0, 0]
count = bubble.bubble(bubble_arr, dim)
CTotal[2] = count[0]
MTotal[2] = count[1]
print("УПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ:\n")
print("Размер массива: ", dim)
print("Сравнений:    ", CTotal[0], " ", CTotal[1], " ", CTotal[2])
print("Перестановок: ", MTotal[0], " ", MTotal[1], " ", MTotal[2])


select_arr.clear()
bubble_arr.clear()
insert_arr.clear()

for i in range(dim, 0, -1):
    select_arr.append(i)
    bubble_arr.append(i)
    insert_arr.append(i)

print("\nОБРАТНО УПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ: Исходный массив")
print(select_arr)

count = [0, 0]
count = select.select(select_arr, dim)
print("\nОБРАТНО УПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ: Результирующий массив")
print(select_arr)
CTotal[0] = count[0]
MTotal[0] = count[1]

count = [0, 0]
count = insert.insert(insert_arr, dim)
CTotal[1] = count[0]
MTotal[1] = count[1]

count = [0, 0]
count = bubble.bubble(bubble_arr, dim)
CTotal[2] = count[0]
MTotal[2] = count[1]
print("Размер массива: ", dim)
print("Сравнений:    ", CTotal[0], " ", CTotal[1], " ", CTotal[2])
print("Перестановок: ", MTotal[0], " ", MTotal[1], " ", MTotal[2])

NUM = 1500
CTotal.clear()
MTotal.clear()

CTotal = [0, 0, 0]
MTotal = [0, 0, 0]

for n in range(0, NUM):

    select_arr.clear()
    bubble_arr.clear()
    insert_arr.clear()

    select_arr = [random.randint(0, 100) for i in range(dim)]
    for i in range(0, dim):
        bubble_arr.append(select_arr[i])
        insert_arr.append(select_arr[i])

    count = [0, 0]
    count = select.select(select_arr, dim)
    CTotal[0] += count[0]
    MTotal[0] += count[1]

    count = [0, 0]
    count = insert.insert(insert_arr, dim)
    CTotal[1] += count[0]
    MTotal[1] += count[1]

    count = [0, 0]
    count = bubble.bubble(bubble_arr, dim)
    CTotal[2] += count[0]
    MTotal[2] += count[1]

print("\nСЛУЧАЙНАЯ РЕАЛИЗАЦИЯ:")
print("Проведено экспериментов: ", NUM)
print("Размер массива: ", dim)
print("Сравнений:    ", CTotal[0]/NUM, " ", CTotal[1]/NUM, " ", CTotal[2]/NUM)
print("Перестановок: ", MTotal[0]/NUM, " ", MTotal[1]/NUM, " ", MTotal[2]/NUM)