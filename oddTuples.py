def oddTuples(aTuple):
    newTuple=()
    for t in range(len(aTuple)):
        if(not(t%2)):
            newTuple=newTuple+(aTuple[t],)
    return newTuple

print(oddTuples(('I','am','a','test','tuple')))
