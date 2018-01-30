def iterPower(base,exp):
    power=1
    for i in range(exp):
        power=power*base
    return power
base=int(input("Enter the base: "))
exp=int(input("Enter the exponent: "))
print(iterPower(base,exp))
