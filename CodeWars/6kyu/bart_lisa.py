names_list = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]
names_list1 = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
names_list2 = [{'name': 'Bart'}, {'name': 'Lisa'}]
names_list3 = [{'name': 'Bart'}]


def namelist(names):
    names_list = [d['name'] for d in names]
    str_names = ','.join(names_list)
    final_string = str_names[::-1].replace(",", " & ", 1)[::-1]
    print(final_string)


namelist(names_list)
namelist(names_list1)
namelist(names_list2)
namelist(names_list3)
