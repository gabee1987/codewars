def validate(message):
    while True:
        list = message.split(" ")
        if list[0] == 'MDZHB':
            return True
        else:
            return False
        if len(list[1]) == 2:
            return True
        else:
            return False
        if len(list[2]) == 3:
            return True
        else:
            return False
        if list[3] == isupper():
            return True
        else:
            return False
        if len(list[4,5,6,7]) == 2:
            return True
        else:
            return False




msg = list(message.split(' '))
    if len(msg) != 8:
        return False
    if msg[0] != str('MDZHB'):
        return False
    if not (len(msg[1]) == 2 and msg[1].isdigit()):
        return False
    if not (len(msg[2]) == 3 and msg[2].isdigit()):
        return False
    if not (msg[3].isalpha() and msg[3].isupper()):
        return False
    for i in msg[4:]:
        if not msg[i].isdigit or len(msg[i]) == 2:
            return False
    else:  
      return True


 msg = message.split()
    if len(msg) != 8:
        return False
    if msg[0] != "MDZHB":
        return False
    if not (len(msg[1]) == 2 and msg[1].isdigit()):
        return False
    if not (len(msg[2]) == 3 and msg[2].isdigit()):
        return False
    if not (msg[3].isalpha and msg[3].isupper()):
        return False
    for i in msg[-4:]:
        if not i.isdigit() or len(i) != 2:
              return False
    return True


l = message.split()
    if len(l) != 8:
        return False
    if l[0] != "MDZHB":
        return False
    if not (l[1].isdigit() and len(l[1]) == 2):
        return False
    if not (l[2].isdigit() and len(l[2]) == 3):
        return False
    if not (l[3].isalpha() and l[3].isupper):
        return False
    for i in l[-4:]:
        if not i.isdigit() or len(i)!=2:
            return False 
    return True
