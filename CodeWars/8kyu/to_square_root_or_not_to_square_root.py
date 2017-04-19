import math


def square_or_square_root(arr):
    output_arr = []
    for num in arr:
        if int(math.sqrt(num))**2 == num:
            output_arr.append(math.sqrt(num))
        else:
            output_arr.append(num**2)
    return list(map(int, output_arr))









print(square_or_square_root([4, 3, 9, 7, 2, 1 ]))
print(square_or_square_root([100, 101, 5, 5, 1, 1]))
print(square_or_square_root([1, 2, 3, 4, 5, 6]))