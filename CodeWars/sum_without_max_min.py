def sum_array(arr):
    without_max_min = []
    if not arr or len(arr) <= 2 :
        return 0
    else:
        for i in arr:
            arr.remove(min(arr))
            arr.remove(max(arr))
            return sum(arr)







print(sum_array(None))
print(sum_array([]))
print(sum_array([3]))
print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([6, 0, 1, 10, 10]))
print(sum_array([-6, -20, -1, -10, -12]))
print(sum_array([3, 5]))
print(sum_array([-3, -5]))
