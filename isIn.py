def isIn(char,aStr):
    if(len(aStr)==1 or aStr==""):
        return False
    if(char<aStr[len(aStr)//2]):
        return isIn(char,aStr[:len(aStr)//2])
    elif(char>aStr[len(aStr)//2]):
        return isIn(char,aStr[len(aStr)//2:])
    else:
        return True

print(isIn('b',"acdfgijklp"))
