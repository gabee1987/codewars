
import collections


def first_non_repeating_letter(string):
    unique = ""
    for character in string:
        if string.lower().count(character.lower()) == 1:
            unique += character
    if not unique:
        return ""
    return unique[0]


print(first_non_repeating_letter(''))
print(first_non_repeating_letter('abba'))  # ''
print(first_non_repeating_letter('aa'))  # ''
print(first_non_repeating_letter('~><#~><'))  # '#'
print(first_non_repeating_letter('hello world, eh?'))  # 'w'
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))  # ','
print(first_non_repeating_letter('sTreSS'))  # 'T'
