import math

def polysum(n,s):
    return round(0.25*n*s*s/math.tan(math.pi/n)+(n*s)**2,4)

n=int(input("Enter the number of sides: "))
s=int(input("Enter the length of each side: "))
print(polysum(n,s))
