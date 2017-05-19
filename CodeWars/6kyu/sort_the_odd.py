array1 = [5, 3, 2, 8, 1, 4]
array2 = [5, 3, 1, 8, 0]
array3 = []


def sort_array(source_array):
    return sorted(source_array, key=lambda num: -(num % 2))

print(sort_array(array1))
print(sort_array(array2))
print(sort_array(array3))
