def find_children(dancing_brigade):
    ordered_string = sorted(dancing_brigade, key=lambda c: (c.upper(), c[0].islower()))
    return str(''.join(ordered_string))




print(find_children("abBA"))  # "AaBb"
print(find_children("AaaaaZazzz"))  # "AaaaaaZzzz"
print(find_children("CbcBcbaA"))  # "AaBbbCcc"
print(find_children("xXfuUuuF"))  # "FfUuuuXx"
print(find_children(""))  # ""
