def recurPower(base,exp):
    if(exp==0):
        return 1
    elif(exp==1):
        return base
    else:
        return base*recurPower(base,exp-1)

base=int(input("Enter the base: "))
exp=int(input("Enter the exponent: "))
print(recurPower(base,exp))
