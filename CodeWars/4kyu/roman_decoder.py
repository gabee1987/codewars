def solution(roman):
    """complete the solution by transforming 
    the roman numeral into an integer"""

    roman_keys = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    current = 0
    last = 0
    for i in roman[::-1]:
        if roman_keys[i] >= last:
            current += roman_keys[i]
        else:
            current -= roman_keys[i]
        last = roman_keys[i]
    return current



print(solution('XXI'))
print(solution('MMVIII'))