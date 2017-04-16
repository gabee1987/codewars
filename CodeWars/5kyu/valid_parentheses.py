def valid_parentheses(string):
    counter = 0
    for char in string:
        if char == '(':
            counter += 1
        if char == ')':
            counter -= 1
        if counter < 0:
            return False
    if counter != 0:
        return False
    return True






print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))