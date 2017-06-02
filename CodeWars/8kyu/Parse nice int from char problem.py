def get_age(age):
    for item in age:
        if item.isdigit():
            return int(item)


print(get_age("0 years old"))
print(get_age("2 years old"))
print(get_age("4 years old"))
print(get_age("5 years old"))
print(get_age("7 years old"))