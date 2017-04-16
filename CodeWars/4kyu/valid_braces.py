def validBraces(string):
    parenthesis_counter = 0
    brackets_counter = 0
    curlybrackets_counter = 0
    for char in string:
        if char == '(':
            parenthesis_counter += 1
        elif char == ')':
            parenthesis_counter -= 1
        elif char == '[':
            brackets_counter += 1
        elif char == ']':
            brackets_counter -= 1
        elif char == '{':
            curlybrackets_counter += 1
        elif char == '}':
            curlybrackets_counter -= 1
        elif parenthesis_counter or brackets_counter or curlybrackets_counter < 0:
            return False
    if parenthesis_counter or brackets_counter or curlybrackets_counter != 0:
        return False
    return True





print(validBraces( "()" ))
print(validBraces( "[(])" ))