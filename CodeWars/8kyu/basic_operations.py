def basic_op(operator, value1, value2):
    outcome = 0
    if operator == '+':
        outcome = value1 + value2
    if operator == '-':
        outcome = value1 - value2
    if operator == '*':
        outcome = value1 * value2
    if operator == '/':
        outcome = value1 / value2
    return int(outcome)








print(basic_op('+', 4, 7))
print(basic_op('-', 15, 18))
print(basic_op('*', 5, 5))
print(basic_op('/', 49, 7))