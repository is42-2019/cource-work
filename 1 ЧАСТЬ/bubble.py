def bubble(arr, dim):
    n = 1
    alg_count = [0, 0]

    while n < dim:
        for i in range(dim - n):
            alg_count[0] += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                alg_count[1] += 1
        n += 1
    return alg_count