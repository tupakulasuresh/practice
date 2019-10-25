
def get_subarray(array, size):
    arr_len = len(array)
    start = 0
    for index in range(1, arr_len - size + 1):
        if array[start] < array[index]:
            start = index
    return array[start:start + size]

A = [6, 4, 7, 2, 5]
k = 3
print get_subarray(A, k)

A = [1, 4, 3, 2, 5]
k = 4
print get_subarray(A, k)

