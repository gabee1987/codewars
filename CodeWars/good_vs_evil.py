# Good:
# Hobbits - 1
# Men - 2
# Elves - 3
# Dwarves - 3
# Eagles - 4
# Wizards - 10

# Evil:
# Orcs - 1
# Men - 2
# Wargs - 2
# Goblins - 2
# Uruk Hai - 3
# Trolls - 5
# Wizards - 10


def goodVsEvil(good, evil):
    good_army = good.split(' ')
    evil_army = evil.split(' ')
    good_result = [(int(good_army[0]) * 1) +
                   (int(good_army[1]) * 2) +
                   (int(good_army[2]) * 3) +
                   (int(good_army[3]) * 3) +
                   (int(good_army[4]) * 4) +
                   (int(good_army[5]) * 10)]

    evil_result = [(int(evil_army[0]) * 1) +
                   (int(evil_army[1]) * 2) +
                   (int(evil_army[2]) * 2) +
                   (int(evil_army[3]) * 2) +
                   (int(evil_army[4]) * 3) +
                   (int(evil_army[5]) * 5) +
                   (int(evil_army[6]) * 10)]
    if int(good_result[0]) > int(evil_result[0]):
        return "Battle Result: Good triumphs over Evil"
    elif int(good_result[0]) < int(evil_result[0]):
        return "Battle Result: Evil eradicates all trace of Good"
    elif int(good_result[0]) == int(evil_result[0]):
        return "Battle Result: No victor on this battle field"

print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
print(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'))

print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
print(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'))
