words = ['aabb', 'abcd', 'bbaa', 'dada']
sorted_words = []
for i in words:
    a = sorted(i)
    b = "".join(a)
    sorted_words.append(b)
print(sorted_words)


