def array_manip(array):
    result_array = []
    for num in range(0, len(array)):
        for i in range(i+1, len(array), 1):
            if array[num] < array[i]:
                result_array.append(array[i])
    return result_array











print(array_manip([8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]))
print(array_manip([ 2, 4, 18, 16, 7, 3, 9, 13, 18, 10 ]))