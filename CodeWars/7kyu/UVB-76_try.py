message = "MDZHB 85 596 KLASA 81 00 02 91"
message2 = "MDZHB 12 733 EDINENIE 67 79 66 32"
message3 = "MDZHV 60 130 VATRUKH 58 89 54 54"


def validate(message):
    msg = message.split(' ')
    if len(msg) != 8:
        return False
    if msg[0] != 'MDZHB':
        return False
    if not (len(msg[1]) == 2 and msg[1].isdigit()):
        return False
    if not (len(msg[2]) == 3 and msg[2].isdigit()):
        return False
    if not (msg[3].isalpha() and msg[3].isupper()):
        return False
    for i in msg[-4:]:
        if not i.isdigit or i != 2:
            return False
    return True

print(validate(message))