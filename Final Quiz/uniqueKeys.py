def uniqueKeys(aDict):
    bDict={}
    uniqueKeysList=[]
    for i in aDict:
        if aDict[i] not in bDict:
            bDict[aDict[i]]=i
        else:
            bDict[aDict[i]]+=i
    for i in aDict:
        if i== bDict[aDict[i]]:
            uniqueKeysList+=[i]
    print(uniqueKeysList)
