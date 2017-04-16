def maxSequence(arr):
    highest = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            temp_arr = arr[i:j+1]
            if sum(temp_arr) > highest:
                highest = sum(temp_arr)
    return highest





print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(maxSequence([]))  # 0
