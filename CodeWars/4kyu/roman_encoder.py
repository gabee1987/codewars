def solution(n):
    roman_keys = [
                (1000, 'M'),
                (900, 'CM'),
                (500, 'D'),
                (400, 'CD'),
                (100, 'C'),
                (90, 'XC'),
                (50, 'L'),
                (40, 'XL'),
                (10, 'X'),
                (9, 'IX'),
                (5, 'V'),
                (4, 'IV'),
                (1, 'I')
                ]
    roman = ''
    while n > 0:
        for i, r in roman_keys:
            while n >= i:
                roman += r
                n -= i
    return roman


print(solution(1))
print(solution(4))
print(solution(6))
print(solution(45))
print(solution(567))
print(solution(2017))