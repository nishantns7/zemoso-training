def iterPower(base,exp):
    power=1
    for i in range(exp):
        power=power*base
    return power
s=input("Enter the base: ")
if '.' in s:
    base=float(s)
else:
    base=int(s)
exp=int(input("Enter the exponent: "))
print(iterPower(base,exp))
