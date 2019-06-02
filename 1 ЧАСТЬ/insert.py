def insert(arr, dim):

    alg_count = [0, 0]

    for i in range(1, dim):
        temp = arr[i]
        j = i - 1
        while j >= 0:
            alg_count[0] += 1
            if arr[j] > temp:
                alg_count[1] += 1
                arr[j + 1] = arr[j]
                arr[j] = temp
            j -= 1
    return alg_count