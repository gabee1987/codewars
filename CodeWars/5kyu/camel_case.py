def to_camel_case(text):
    not_camel = str(text.replace('_', ''))
    return not_camel






print(to_camel_case(''))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))