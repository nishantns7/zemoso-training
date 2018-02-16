animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
#animals['b'].append('bear')
#animals['b'].append('boa constrictor')
#animals['b'].append('boar')
def biggest(animals):
    max=0
    for i in animals.keys():
        if(len(animals[i])>max):
            max=len(animals[i])
            maxKey=i
    if(len(animals)==0):
        return
    print(maxKey)
biggest(animals)
