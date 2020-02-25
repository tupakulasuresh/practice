def remove_duplicates(array):
    start = 0
    while start < len(array) - 1:
        if array[start] == array[start + 1]:
            array.pop(start)
        else:
            start += 1
    print array
    return len(array)


print remove_duplicates([1, 1, 2])
print remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
