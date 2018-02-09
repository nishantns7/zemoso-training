animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(animals):
    value=len(animals)
    for i in animals.keys():
        if(type(animals[i]=='list')):
            value+=len(animals[i])-1
    return value

print(how_many(animals))
