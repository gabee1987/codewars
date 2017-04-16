def countBits(n):
    bits = format(n, "08b")
    return len(bits)
    print(len(bits))

print(countBits(0))
print(countBits(4))
print(countBits(7))
print(countBits(9))
print(countBits(10))
print(countBits(1234))