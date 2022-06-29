def how_many(aDict):
    if len(aDict) == 0:
        return None

    key = ''
    length = ''
    for i in aDict:
        if len(aDict[i]) >= len(length):
            key = i
            length = aDict[i]
        # elif len(aDict) == 1 and len(aDict[i]) == 0:
        #     return i
    return key


animals = {'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': []}

all_animals = how_many(animals)
print(all_animals)