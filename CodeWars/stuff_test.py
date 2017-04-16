s = 'sTreSS'
print(next(x for x in s if len([y for y in s if y == x.lower()]) == 1))


