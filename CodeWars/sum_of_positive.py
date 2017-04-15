def positive_sum(arr):
    positives = []
    for i in arr:
        if i > 0:
            positives.append(i)
    return sum(positives)
    return 0


print(positive_sum([1, 2, 3, 4, 5]))
print(positive_sum([1, -2, 3, 4, 5]))
print(positive_sum([-1, 2, 3, 4, -5]))
print(positive_sum([-1, -2, -3, -4, -5]))