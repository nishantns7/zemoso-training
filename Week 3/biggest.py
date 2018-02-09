animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(animals):
    max=0
    for i in animals.keys():
        if(len(animals[i])>max):
            maxKey=i
    if(len(animals)==0):
        return
    print(maxKey)

biggest(animals)
