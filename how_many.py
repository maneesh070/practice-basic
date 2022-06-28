def how_many(aDict):
    length = 0
    for i in aDict:
        length += len(aDict[i])
    return length

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

all_animals = how_many(animals)
print(all_animals)