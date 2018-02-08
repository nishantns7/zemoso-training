def applyToEach(L,f):
    for i in range(len(L)):
        L[i]=f(L[i])

#def timesFive(x):
#    return x*5

testList=[1,-4,8,-9]
applyToEach(testList,abs)
#applyToEach(testList,timesFive)
